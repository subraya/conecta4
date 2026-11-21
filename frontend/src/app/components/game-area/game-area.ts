import { ChangeDetectorRef, Component, inject, OnInit, QueryList, ViewChildren } from '@angular/core';
import { TranslateDirective, TranslateService } from '@ngx-translate/core';
import { ApiService } from '../../services/api_service';
import { Square } from '../square/square';

import { GameConfig } from '../../services/game_config';
import { Router } from '@angular/router';
import { GameTurn } from '../../services/game_turn';
import { sleep_secs } from '../../common/utils';
import { Player } from '../../models/player';

@Component({
  selector: 'c4-game-area',
  standalone: true,
  imports: [Square, TranslateDirective],
  templateUrl: './game-area.html',
  styleUrl: './game-area.scss',
})

export class GameArea implements OnInit {
    private router = inject(Router);
    private translate = inject(TranslateService);
    private turnManager = inject(GameTurn);
    private gameConfig = inject(GameConfig);
    private api = inject(ApiService);
    public gameMode: string;
    private gameId!: string;
    private players: Array<Player>;
    public numRows = 6;
    public numColumns = 7;
    public dummyRows = Array.from(Array(this.numRows).keys())
    public dummyCols = Array.from(Array(this.numColumns).keys())
    private simulation: any
    private winnerCombination!: Array<Square>|null;
    public winner!: string|null;
    @ViewChildren(Square) squares!: QueryList<Square>

    constructor(private ref: ChangeDetectorRef) {
        this.gameMode = this.gameConfig.getMode();
        this.players = this.gameConfig.getPlayers();
    }

    ngOnInit() {
        console.log("GameArea started")
        if(this.gameMode == "play"){
            this.api.startGame().subscribe( (resp: any) => {
                console.log(resp)
                this.gameId = resp["game_id"];
                this.api.getCurrentTurn(this.gameId).subscribe((resp: any) => {
                    this.prepareNextTurn(resp);
                });
            });
        }
    }

    public newGame(): void {
        this.clearBoard();
        this.api.startGame().subscribe( (resp: any) => {
            console.log(resp)
            this.gameId = resp["game_id"];
            this.api.getCurrentTurn(this.gameId).subscribe((resp: any) => {
                this.prepareNextTurn(resp);
            });
        });
    }

    async simulate() {
        this.clearBoard();
        await this.getSimulation()
        let currentPlayer = "player1"
        for (const move of this.simulation.moves) {
            await sleep_secs(1)
            let sq = this.findSquare(move[1], move[0])
            sq?.setPlayer(currentPlayer)
            if(currentPlayer=="player1"){
                currentPlayer = "player2"
            }
            else
                currentPlayer = "player1"
        }

        this.winner = this.simulation.winner + " wins!"
        this.winnerCombination = this.simulation.winner_combination
        this.highlightWinnerCombination()
        this.ref.detectChanges()
    }

    public playerMoved(): void {
        const sq = this.turnManager.playedSquare;
        this.api.playMove(this.gameId, sq.row, sq.col, this.turnManager.currentPlayer).subscribe((resp: any) => {
            if(resp["winner"]) {
                this.finishGame(resp);
            } else
                this.prepareNextTurn(resp);
        });
    }

    public goBack(): void {
        this.router.navigate(['']);
    }

    public getGameStatusText(){
        if(this.winner == "draw") {
            return this.translate.instant("game.result.draw");
        } else if (this.winner) {
            return this.translate.instant("game.result.win", {playerName: this.getPlayerName(this.winner)});
        }
        if (this.turnManager.currentPlayer) {
            return this.translate.instant("game.currentPlayer", {playerName: this.getPlayerName(this.turnManager.currentPlayer)});
        }
        return "";
    }
    
    async getSimulation() {
        console.log("Simulate game");
        this.clearBoard();
        this.simulation = await this.api.simulateGame();
    }

    private getPlayerName(key: string): string {
        return this.players.find(pl => pl.key == key)?.name || key;
    }

    private clearBoard() {
        this.squares.forEach(sq => sq.reset());
        this.winner = null;
        this.winnerCombination = null;
    }

    private findSquare(row: number, col: number): Square|undefined {
        return this.squares.find(sq => sq.row == row && sq.col == col);
    }

    private async prepareNextTurn(turnInfo: any) {
        this.turnManager.setCurrentPlayer(turnInfo["current_player"]);
        for(let coords of turnInfo["free_squares"]) {
            this.findSquare(coords[1], coords[0])?.setAvailable();
        }
        this.ref.detectChanges();

        const nextPlayer = this.turnManager.currentPlayer;
        if(this.gameConfig.getPlayers().find((p: Player) => p.key == nextPlayer).type == "cpu") {
            for(let coords of turnInfo["free_squares"]) {
                this.findSquare(coords[1], coords[0])?.setCpuTurn();
            }

            console.log("waiting cpu move");
            let gameId = this.gameId;
            await sleep_secs(2)
            this.api.getMoveSuggestion(gameId).subscribe((resp: any) => {
                if(resp["game_id"] == this.gameId) {
                    const coords = resp["square"]
                    const sq = this.findSquare(coords[1], coords[0])
                    console.log(sq)
                    sq?.playMove();
                }
                else
                    console.log("Got move for mismatching game id " + resp["game_id"] + ". Ignoring move")
            });
        }  
    }

    private finishGame(winnerInfo: any): void{
        this.winner = winnerInfo["winner"];
        this.winnerCombination = winnerInfo["winner_combination"] || [];
        this.highlightWinnerCombination();
        this.ref.detectChanges();
    }

    private highlightWinnerCombination(): void{
        this.squares.forEach(sq => {
            const winnerSquare = this.winnerCombination?.find((wc: any) => wc[0] == Number(sq.col) && wc[1] == Number(sq.row));
            if(!winnerSquare){
                sq.dim();
            }
        });
    }
}