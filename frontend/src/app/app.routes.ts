import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home';
import { GameArea } from './components/game-area/game-area';
import { OptionsComponent } from './components/options/options';

export const routes: Routes = [
    {
        path: '',
        component: HomeComponent,
    },
    {
        path: 'simulation',
        component: GameArea,
    },
    {
        path: 'options',
        component: OptionsComponent,
    },
];
