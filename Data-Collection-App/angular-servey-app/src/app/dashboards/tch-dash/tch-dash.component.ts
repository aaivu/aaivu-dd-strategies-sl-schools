import {Component, OnInit} from '@angular/core';
import * as Chart from 'chart.js'
import {AuthService} from "../../service/auth.service";
import {UserService} from "../../service/user.service";

@Component({
  selector: 'app-tch-dash',
  templateUrl: './tch-dash.component.html',
  styleUrls: ['./tch-dash.component.scss']
})
export class TchDashComponent implements OnInit {

  canvas: any;
  ctx: any;
  loading = true;
  students;
  summery = {
    "Sinhala": [0, 0, 0, 0, 0],
    "Mathematics": [0, 0, 0, 0, 0],
    "Science": [0, 0, 0, 0, 0],
    "Art": [0, 0, 0, 0, 0],
    "Citizenship_Education": [0, 0, 0, 0, 0],
    "English": [0, 0, 0, 0, 0],
    "Religion": [0, 0, 0, 0, 0],
    "History": [0, 0, 0, 0, 0],
    "Geography": [0, 0, 0, 0, 0],
    "PTS": [0, 0, 0, 0, 0],
    "Health": [0, 0, 0, 0, 0],
  };

  learningStyles = [0, 0, 0];

  com_sub = [
    "Sinhala",
    "Mathematics",
    "Science",
    "Art",
    "Citizenship_Education",
    "English",
    "Religion",
    "History",
    "Geography",
    "PTS",
    "Health"
  ];

  constructor(private auth: AuthService, private userAPI: UserService) {
  }

  ngOnInit() {
    console.log(this.auth.teacherData);
    if (this.auth.teacherData) {
      this.students = this.auth.teacherData;
      this.calculateValues();
    } else {
      this.userAPI.getTeacherData().subscribe(data => {
        if (data['success']) {
          this.students = data['students'].filter(a => {
            return !!a['predicted']['learningStyle']
          });
          this.auth.teacherData = this.students;
          this.calculateValues();
        }
      })
    }
  }

  getGrade(s) {
    s = parseInt(s);
    if (s > 75) {
      return ['A', 0]
    } else if (s > 65) {
      return ['B', 1]
    } else if (s > 55) {
      return ['C', 2]
    } else if (s > 40) {
      return ['S', 3]
    } else {
      return ['F', 4]
    }
  }

  calculateValues() {
    this.students.forEach(s => {
      this.learningStyles[s['predicted']['learningStyle']]++;
      this.com_sub.forEach(sub => {
        this.summery[sub][this.getGrade(s['predicted'][sub + '_mark'])[1]]++;
      });
    });
    this.initGraphs();
  }

  initGraphs() {
    setTimeout(() => {
      this.canvas = document.getElementById('myChart');
      this.ctx = this.canvas.getContext('2d');
      let myCart = new Chart(this.ctx, {
        type: 'doughnut',
        data: {
          datasets: [{
            data: this.learningStyles,
            backgroundColor: ['#ff3980', '#fed546', '#3f94ee']
          }],
          labels: [
            'Composite',
            'Experimental',
            'Methodological'
          ]
        },
        options: {
          responsive: true
        }
      });


      this.com_sub.forEach(sub => {
        const canvas: any = document.getElementById(sub + 'Chart');
        const ctx: any = canvas.getContext('2d');
        let chart = new Chart(ctx, {
          type: 'doughnut',
          data: {
            datasets: [{
              data: this.summery[sub],
              backgroundColor: ['#03b500', '#96fc8a', '#fff600', '#ffb4b4', '#ff5a5a']
            }],
            labels: ['A', 'B', 'C', 'S', 'F']
          },
          options: {
            responsive: true,
            legend: {
              display: false
            }
          }
        });
      });
      this.loading = false;
    }, 200);
  }

}
