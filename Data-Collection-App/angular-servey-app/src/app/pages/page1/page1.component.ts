import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-page1',
  templateUrl: './page1.component.html',
  styleUrls: ['./page1.component.scss']
})
export class Page1Component implements OnInit {
  answers = {
    q1 : '',
    q2 : '',
    q3 : ''
  };
  constructor() { }

  ngOnInit() {
  }

}
