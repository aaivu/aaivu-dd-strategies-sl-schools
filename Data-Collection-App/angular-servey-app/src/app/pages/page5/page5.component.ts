import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-page5',
  templateUrl: './page5.component.html',
  styleUrls: ['./page5.component.scss']
})
export class Page5Component implements OnInit {
  answers = {
    q16: {}
  };
  tutSelector = {};

  constructor() { }

  ngOnInit() {
  }

  hasAny() {
    let res = false;
    Object.keys(this.answers.q16).forEach((key) => {
      res = res || this.answers.q16[key]
    });
    return res;
  }

  getKeys() {
    return Object.keys(this.answers.q16);
  }

  check(sub, grade) {
    const obj = this.tutSelector[sub] || {};
    obj['g_' + grade] = !obj['g_' + grade];
    this.tutSelector[sub] = obj;
  }

}
