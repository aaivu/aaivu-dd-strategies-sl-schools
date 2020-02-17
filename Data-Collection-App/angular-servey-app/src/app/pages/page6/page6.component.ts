import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-page6',
  templateUrl: './page6.component.html',
  styleUrls: ['./page6.component.scss']
})
export class Page6Component implements OnInit {

  answers = {
    q17: {},
    q18: {}
  };
  clubSelector = {};

  constructor() { }

  ngOnInit() {
  }

  hasAny() {
    let res = false;
    Object.keys(this.answers.q17).forEach((key) => {
      res = res || this.answers.q17[key]
    });
    return res;
  }

  getKeys() {
    return Object.keys(this.answers.q17);
  }

  check(sub, grade) {
    const obj = this.clubSelector[sub] || {};
    obj['g_' + grade] = !obj['g_' + grade];
    this.clubSelector[sub] = obj;
  }

}
