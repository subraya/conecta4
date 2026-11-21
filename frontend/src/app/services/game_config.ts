import { inject, Injectable } from "@angular/core";
import { Player } from "../models/player";
import { ApiService } from "./api_service";
import { TranslateService } from '@ngx-translate/core';

@Injectable({ providedIn: 'root' })
export class GameConfig {
    private api = inject(ApiService);
    private mode = "play";
    private locale!: string;
    private players!: Array<Player>|any;
    private translate = inject(TranslateService);

    constructor() {
        this.loadPlayers();
        this.loadLocale();
    }

    public setMode(newMode: string): void {
        this.mode = newMode;
    }

    public getMode(): string {
        return this.mode;
    }

    public setLocale(newLocale: string): void {
        this.api.updateLocale(newLocale);
        this.locale = newLocale;
    }

    public getLocale(): string {
        return this.locale;
    }

    public getPlayers() {
        return this.players;
    }

    public savePlayers(player1: Player, player2: Player) {
        this.api.updatePlayer(player1);
        this.api.updatePlayer(player2);
        this.players = [player1, player2];
    }

    private async loadPlayers() {
        console.log("load")
        this.players = await this.api.getPlayers();
    }

    private async loadLocale() {
        const resp: any = await this.api.getLocale();
        this.locale = resp["locale"];
        this.translate.use(this.locale);
    }
}
