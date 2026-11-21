import { ChangeDetectorRef, Component, EventEmitter, inject, Input, Output } from '@angular/core';
import { GameTurn } from '../../services/game_turn';

@Component({
  selector: 'c4-square',
  standalone: true,
  templateUrl: './square.html',
  styleUrl: './square.scss'
})

export class Square {
    private turnManager = inject(GameTurn);
    @Input() row: any
    @Input() col: any
    private player: string|null
    public dimmed: boolean
    private available: boolean
    private humanClickable: boolean
    @Output() playerMovedEvent = new EventEmitter<string>();

    constructor(private ref: ChangeDetectorRef){
        this.player = null;
        this.dimmed = false;
        this.available = false;
        this.humanClickable = false;
    }

    public setPlayer(player: string): void {
        this.player = player;
        this.available = false;
        this.ref.detectChanges();
    }

    public setAvailable(): void {
        this.available = true;
        this.humanClickable = true;
        this.ref.detectChanges();
    }

    public setCpuTurn(): void {
        this.humanClickable = false;
        this.ref.detectChanges();
    }


    public reset(): void{
        this.player = null;
        this.dimmed = false;
        this.available = false;
        this.humanClickable = false;
        this.ref.markForCheck();
    }

    public dim(): void{
        this.dimmed = true;
        this.available = false;
        this.humanClickable = false;
        this.ref.detectChanges();
    }

    public isPlayer1(): boolean{
        return this.player == "player1";
    }

    public isPlayer2(): boolean{
        return this.player == "player2";
    }

    public isAvailable(): boolean{
        return this.available;
    }

    public isHumanClickable(): boolean{
        return this.humanClickable;
    }

    public playHumanMove(): void{
        if(this.humanClickable){
            this.playMove()
        }
    }

    public playMove(): void{
        if(this.isAvailable()){
            console.log("Playing on row " + this.row + ", col " + this.col);
            this.setPlayer(this.turnManager.currentPlayer);
            this.turnManager.setPlayedSquare(this);
            this.playerMovedEvent.emit();
        }
    }
}