import { Component } from '@angular/core';

@Component({
  selector: 'as-home',
  templateUrl: 'app/home/home.html',
  styleUrls: [
    'app/home/home.css'
  ]
})
export class HomeComponent {
  public text: string[] = ['Hi', 'how', 'are', 'you'];
  public activeWordIndex: number = 0;
  public userInput: string;
  private lengthOfText: number = this.text.length;
  private onLastWord: boolean = false;

  public userTyped() {
    if (this.onLastWord) {
      console.log('on last word');
      if (this.userInput.length === this.text[this.lengthOfText - 1].length) {
        this.userInput = '';
        this.activeWordIndex = -1;
      }
    } else {
      if (this.userInput.slice(-1) === ' ') {
        this.activeWordIndex++;
        this.userInput = '';
      }
      if (this.activeWordIndex === this.lengthOfText - 1) {
        this.onLastWord = true;
        console.log('on last word');
      }
    }
  }
}
