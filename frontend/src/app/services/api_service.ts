import { inject, Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from "rxjs";
import { Player } from "../models/player";

@Injectable({ providedIn: 'root' })
export class ApiService {
  private api = inject(HttpClient);
  private baseUrl = "http://127.0.0.1:8000";

  public getLocale() {
    return firstValueFrom(this.api.get(this.baseUrl + '/locale'));
  }

  public updateLocale(locale: string) {
    const params = { locale: locale };
    console.log("helloooo")
    return firstValueFrom(this.api.put(this.baseUrl + '/locale', params));
  }

  public getPlayers() {
    return firstValueFrom(this.api.get(this.baseUrl + '/players'));
  }

  public updatePlayer(player: Player): Promise<Object> {
    return firstValueFrom(this.api.put(this.baseUrl + '/players/' + player.id, player));
  }

  public simulateGame(): Promise<Object> {
    const params = { "rows": 6, "columns": 7, "goal": 4 };
    return firstValueFrom(this.api.post(this.baseUrl + "/simulate-game", params));
  }

  public startGame() {
    const params = {};
    return this.api.post(this.baseUrl + "/games", params);
  }

  public getCurrentTurn(gameId: string) {
    return this.api.get(this.baseUrl + '/games/' + gameId + '/current_turn');
  }

  public playMove(gameId: string, row: number, col: number, playerId: string) {
    const params = { game_id: gameId, row: Number(row), col: Number(col), player_id: playerId };
    return this.api.post(this.baseUrl + '/games/' + gameId + '/move', params);
  }

  public getMoveSuggestion(gameId: string) {
    return this.api.get(this.baseUrl + '/games/' + gameId + '/cpu_move');
  }
}