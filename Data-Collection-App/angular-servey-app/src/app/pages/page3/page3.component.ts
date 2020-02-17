import {Component, OnInit} from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page3',
  templateUrl: './page3.component.html',
  styleUrls: ['./page3.component.scss']
})
export class Page3Component implements OnInit {
  answers = {
    q10: {}
  };
  subSelector = {};

  constructor(private userAPI: UserService, private router: Router, private activatedRoute: ActivatedRoute) {
  }

  ngOnInit() {
    // setInterval(() => {
    //   console.log(this.answers);
    //   console.log(this.subSelector);
    // }, 3000);
  }

  hasAny() {
    let res = false;
    Object.keys(this.answers.q10).forEach((key) => {
      res = res || this.answers.q10[key]
    });
    return res;
  }

  getKeys() {
    return Object.keys(this.answers.q10);
  }

  check(sub, grade) {
    const obj = this.subSelector[sub] || {};

    obj['g_' + grade] = !obj['g_' + grade];

    this.subSelector[sub] = obj;
  }

  done() {
    const subs_names = {
      "1": "sinhala",
      "2": "maths",
      "3": "science",
      "4": "art",
      "5": "dance",
      "6": "buddhism",
      "7": "history",
      "8": "tamil",
      "9": "english",
      "10": "geology"
    };

    let results = '';
    Object.keys(this.subSelector).forEach(sub => {
      let val = this.subSelector[sub];
      results += subs_names[sub] + '_' +
        (val['g_6'] ? '1' : '0') +
        (val['g_7'] ? '1' : '0') +
        (val['g_8'] ? '1' : '0') + ', ';
    });
    console.log(results.substr(0, results.length - 2));
    results = results.substr(0, results.length - 2);

    this.userAPI.setBulk({'tution': results, 'basic': true}).subscribe(data => {
      if (data.success) {
        this.userAPI.setUser(data['newUser']);
        this.router.navigate(['/student/data'], {relativeTo: this.activatedRoute});
      }
    })
  }

}

//{"q10":{"1":true,"4":true,"7":true}}
//{"2":{"g_6":true},"3":{"g_6":true,"g_7":true,"g_8":true},"4":{"g_7":true,"g_8":true}}
