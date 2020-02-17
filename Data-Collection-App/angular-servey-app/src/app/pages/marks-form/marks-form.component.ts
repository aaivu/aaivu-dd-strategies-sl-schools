import {Component, OnInit} from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";
import {AuthService} from "../../service/auth.service";
import {init} from "protractor/built/launcher";

@Component({
  selector: 'app-marks-form',
  templateUrl: './marks-form.component.html',
  styleUrls: ['./marks-form.component.scss']
})
export class MarksFormComponent implements OnInit {
  marks = {};
  com_sub = {
    "1": "Sinhala",
    "2": "Mathematics",
    "3": "Science",
    "4": "Art",
    "5": "Citizenship_Education",
    "6": "English",
    "7": "Religion",
    "8": "History",
    "9": "Geography",
    "10": "PTS",
    "11": "Tamil",
    "12": "Health"
  };

  loading = false;

  constructor(private auth: AuthService, private userAPI: UserService, private router: Router, private activeRouter: ActivatedRoute) {
  }

  ngOnInit() {
    if (this.auth.user) {
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].forEach(v => {
        [1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(k => {
          this.marks[this.com_sub[v] + '_' + k] = this.auth.user['row_data'][this.com_sub[v] + '_' + k];
        })
      });
    }
  }

  done() {
    this.loading = true;
    console.log(this.marks);
    this.marks['marks'] = true;
    this.userAPI.setBulk(this.marks).subscribe(data => {
      if (data.success) {
        this.userAPI.setUser(data['newUser']);
        console.log(data);


        this.userAPI.setAnalitics().subscribe(data => {
          if(data.success) {
            this.userAPI.setUser(data['newUser']);
            this.loading = false;
            this.router.navigateByUrl('/student/data', {relativeTo: this.activeRouter})
          }
        });
      }
    });
  }

  randomFill() {

    const rand = (min, max) => {
      let val = (min + Math.round(Math.random() * 100 % (max - min))) % 100;
      return val < 20 ? 20 : val;
    };

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].forEach(v => {
      let initVal = rand(20, 80);
      [1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(k => {
        initVal = rand(initVal - 10, initVal + 10);
        this.marks[this.com_sub[v] + '_' + k] = initVal;
      })
    });
  }

}
