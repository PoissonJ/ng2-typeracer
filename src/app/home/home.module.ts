import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HomeComponent } from './index';

@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    FormsModule,
    BrowserModule
  ],
  exports: [
    HomeComponent
  ]
})
export class HomeModule {
}
