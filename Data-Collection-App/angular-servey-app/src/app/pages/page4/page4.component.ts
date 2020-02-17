import { Component, OnInit } from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page4',
  templateUrl: './page4.component.html',
  styleUrls: ['./page4.component.scss']
})
export class Page4Component implements OnInit {
  answers = {
    fa_o: '',
    fa_e: '',
    ma_o: '',
    ma_e: '',
    sib: '',
    sib_edu: ''
  };
  constructor(private userAPI: UserService, private router: Router, private actRoute: ActivatedRoute) { }

  ngOnInit() {
  }

  done() {
    console.log(this.answers);
    let edu_level = {
      "Less Than O/L": "1",
      "O/L": "2",
      "A/L": "3",
      "University": "4"
    };

    let fa_e = edu_level[this.answers.fa_e];
    let ma_e = edu_level[this.answers.ma_e];
    let sib_edu = '';
    Object.values(this.answers.sib_edu).forEach(val => {
      sib_edu += edu_level[val] + ', ';
    });

    this.userAPI.setBulk({
      f_edu : fa_e,
      father_job : this.answers.fa_o,
      m_edu : ma_e,
      mother_job : this.answers.ma_o,
      s_num: this.answers.sib,
      s_edu : sib_edu.substr(0, sib_edu.length - 2),
      family: true
    }).subscribe(data => {
      console.log(data);
      if(data.success){
        this.userAPI.setUser(data['newUser']);
        this.router.navigate(['/student/data'], {relativeTo: this.actRoute});
      }
    });

  }

  getTheArray(){
    return new Array(this.answers.sib);
  }

}
