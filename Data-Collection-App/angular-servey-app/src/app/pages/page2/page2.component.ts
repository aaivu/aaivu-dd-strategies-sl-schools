import { Component, OnInit } from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page2',
  templateUrl: './page2.component.html',
  styleUrls: ['./page2.component.scss']
})
export class Page2Component implements OnInit {
  answers = {
    q4: {},
    q5 : '',
    q6 :{},
    q7 : '',
    q8 : '',
    q9 : ''
  };

  constructor(private userAPI: UserService, private router: Router, private activeRouter: ActivatedRoute) { }

  ngOnInit() {
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
    let fav_sub = '';
    Object.keys(this.answers.q4).forEach(sub => {
      if(this.answers.q4[sub]) {
        fav_sub += subs_names[sub] + ', '
      }
    });

    let les_sub = '';
    Object.keys(this.answers.q6).forEach(sub => {
      if(this.answers.q6[sub]) {
        les_sub += subs_names[sub] + ', '
      }
    });

    this.userAPI.setBulk({
      'Fav Subject': fav_sub,
      'Fav Lession': this.answers.q5,
      'hard sub': les_sub,
      'hard lessions' : this.answers.q7,
      'ambition': this.answers.q8,
      'scholarship': this.answers.q9
    }).subscribe(data => {
      console.log(data);
      if(data.success) {
        this.userAPI.setUser(data['newUser']);
        this.router.navigate(['..', '2'], {relativeTo: this.activeRouter})
      }
    })
  }

}
