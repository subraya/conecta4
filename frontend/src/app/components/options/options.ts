import { Component, inject, Input } from '@angular/core';
import { GameConfig } from '../../services/game_config';
import { Router } from '@angular/router';
import { TranslateDirective, TranslateService } from '@ngx-translate/core';
import { Player } from '../../models/player';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'c4-options',
  standalone: true,
  templateUrl: './options.html',
  styleUrl: './options.scss',
  imports: [
    TranslateDirective,
    FormsModule
  ]
})

export class OptionsComponent {
  private router = inject(Router);
  private gameConfig = inject(GameConfig);
  private translate = inject(TranslateService);
  public locale = this.gameConfig.getLocale();
  @Input() public player1!: Player;
  @Input() public player2!: Player;

  public goBack(): void {
    this.gameConfig.savePlayers(this.player1, this.player2);
    this.router.navigate(['']);
  }

  public setLocale(loc: string): void {
    this.locale = loc;
    this.gameConfig.setLocale(loc);
    this.translate.use(loc);
  }

  ngOnInit() {
    const players = this.gameConfig.getPlayers();
    this.player1 = players.find((p: Player) => p.key == "player1");
    this.player2 = players.find((p: Player) => p.key == "player2");
  }
}