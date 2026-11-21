import { Injectable } from "@angular/core";
import { Square } from "../components/square/square";

@Injectable({ providedIn: 'root' })
export class GameTurn {
    public currentPlayer!: string;
    public playedSquare!: Square;

    public setCurrentPlayer(currentPlayer: string): void {
        this.currentPlayer = currentPlayer;
    }

    public setPlayedSquare(data: Square): void {
        this.playedSquare = data
    }
}
