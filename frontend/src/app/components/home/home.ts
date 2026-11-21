import { Component, inject } from '@angular/core';
import { GameConfig } from '../../services/game_config';
import { Router } from '@angular/router';
import { TranslateDirective } from '@ngx-translate/core';

@Component({
  selector: 'c4-home',
  standalone: true,
  templateUrl: './home.html',
  styleUrl: './home.scss',
  imports: [
    TranslateDirective
  ]
})

export class HomeComponent {
  private router = inject(Router);
  private gameConfig = inject(GameConfig);

  
  public goSimulation(): void {
    this.gameConfig.setMode("simulation");
    this.router.navigate(['simulation'],  {browserUrl: ''});
  }

  public goPlay(): void {
    this.gameConfig.setMode("play");
    this.router.navigate(['simulation'],  {browserUrl: ''});
  }

  public goOptions(): void {
    this.router.navigate(['options'],  {browserUrl: ''});
  }
}