import { bootstrapApplication } from '@angular/platform-browser';
import { Component } from '@angular/core';
import { appConfig } from './app/app.config';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  template: `
    <router-outlet></router-outlet>
  `
})
export class App {}

bootstrapApplication(App, appConfig);