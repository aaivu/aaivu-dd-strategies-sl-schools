import {SuiModalService, TemplateModalConfig, ModalTemplate} from 'ng2-semantic-ui';
import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import * as Chart from 'chart.js'
import {AuthService} from "../../service/auth.service";
import {DATA} from "../../service/information";
import {InstructionService} from "../../service/instruction.service";

export interface IContext {
  data: any;
}

@Component({
  selector: 'app-std-marks',
  templateUrl: './std-marks.component.html',
  styleUrls: ['./std-marks.component.scss']
})
export class StdMarksComponent implements OnInit, AfterViewInit {
  @ViewChild('modalTemplate')
  public modalTemplate: ModalTemplate<IContext, string, string>;

  canvas: any;
  ctx: any;

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
    "Tamil",
    "Health"
  ];
  user;
  averages = DATA.averages;

  constructor(public modalService: SuiModalService, public auth: AuthService, public instService: InstructionService) {
  }

  ngOnInit() {
    this.user = this.auth.user;
  }

  public open(subject) {
    const config = new TemplateModalConfig<IContext, string, string>(this.modalTemplate);

    let insts = this.instService.getInstruction(2);

    console.log(insts);
    config.closeResult = "closed!";
    config.size = 'large';
    config.mustScroll = true;
    config.context = {
      data: {
        sub: subject,
        inst: {
          study: insts.study,
          exam: insts.exam,
          group: insts.group
        }
      }
    };

    let marks = [];
    let avg_marks = [];
    [1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(m => {
      marks.push(this.user['row_data'][subject + '_' + m]);
      avg_marks.push(this.averages[subject + '_' + m])
    });
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
          labels: ['6 - I', '6 - II', '6 - III', '7 - I', '7 - II', '7 - III', '8 - I', '8 - II'],
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
          }
          ]
        },
        options: {
          responsive: true
        }
      });
    }, 300);
  }

  ngAfterViewInit(): void {

  }

  getInstructionSet(oldMarks, newMarks) {
    if(oldMarks >= 70) {
      if(newMarks - oldMarks > -10) {
        return "You are doing well. keep it up"
      } else {
        return "Work hard to maintain your level"
      }
    } else if(oldMarks >= 45) {
      if(newMarks - oldMarks > 10){
        return "Good work, Keep it up"
      } else if(newMarks - oldMarks > -10) {
        return "You are OK, but work harder to improve"
      } else {
        return "Focus more on your studies. Work harder"
      }
    } else {
      return "Focus more on your studies. Work harder"
    }
  }

}
