import {SuiModalService, TemplateModalConfig, ModalTemplate} from 'ng2-semantic-ui';
import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import * as Chart from 'chart.js'
import {AuthService} from "../../service/auth.service";
import {DATA} from "../../service/information";
import {InstructionService} from "../../service/instruction.service";
import {UserService} from "../../service/user.service";

export interface IContext {
  data: any;
}

@Component({
  selector: 'app-tch-marks',
  templateUrl: './tch-marks.component.html',
  styleUrls: ['./tch-marks.component.scss']
})
export class TchMarksComponent implements OnInit {

  @ViewChild('modalTemplate')
  public modalTemplate: ModalTemplate<IContext, string, string>;

  canvas: any;
  ctx: any;

  students = [];
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

  averages = DATA.averages;

  constructor(private userAPI: UserService, public modalService: SuiModalService,
              public auth: AuthService, public instService: InstructionService) {
  }

  ngOnInit() {
    this.userAPI.getTeacherData().subscribe(data => {
      if (data['success']) {
        this.students = data['students'].filter(a => {
          return !!a['predicted']['learningStyle']
        });
        this.auth.teacherData = this.students;
      }
    })
  }

  getLearningStyleName(n) {
    switch (n) {
      case '0':
        return 'Composite';
      case '1':
        return 'Experimental';
      case '2':
        return 'Methodological';
    }
  }

  public openModal(subject, user) {
    console.log(subject, user);
    const config = new TemplateModalConfig<IContext, string, string>(this.modalTemplate);

    config.closeResult = "closed!";
    config.size = 'large';
    config.mustScroll = true;
    config.context = {
      data: {
        sub: subject,
      }
    };

    let marks = [];
    let avg_marks = [];
    [1, 2, 3, 4, 5, 6, 7, 8].forEach(m => {
      marks.push(user['row_data'][subject + '_' + m]);
      avg_marks.push(this.averages[subject + '_' + m])
    });
    console.log(marks);
    this.modalService
      .open(config)
      .onApprove(result => { /* approve callback */
      })
      .onDeny(result => { /* deny callback */
      });
    setTimeout(() => {
      this.canvas = document.getElementById('myChart');
      this.ctx = this.canvas.getContext('2d');
      let myChart = new Chart(this.ctx, {
        type: 'line',
        data: {
          labels: ['6 - I', '6 - II', '6 - III', '7 - I', '7 - II', '7 - III', '8 - I', '8 - II', '8 - III'],
          datasets: [{
            label: 'Marks',
            data: marks.slice(0, 8),
            fill: false,
            borderColor: 'red',
            backgroundColor: [
              'red',
            ],
            borderWidth: 2
          }, {
            label: 'Average Marks',
            data: avg_marks.slice(0, 8),
            fill: false,
            borderColor: 'blue',
            backgroundColor: [
              'blue',
            ],
            borderWidth: 2
          }, {
            label: 'Predicted',
            data: [{x: '8 - II', y: marks[7]}, {x: '8 - III', y: user['predicted'][subject + '_mark']}],
            fill: false,
            borderColor: 'green',
            borderDash: [10, 5],
            backgroundColor: [
              'green',
            ],
            borderWidth: 2
          }
          ]
        },
        options: {
          responsive: true
        }
      });
    }, 300);
  }

}
