import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import { Network } from 'vis';

@Component({
  selector: 'app-marks-corelations',
  templateUrl: './marks-corelations.component.html',
  styleUrls: ['./marks-corelations.component.scss']
})
export class MarksCorelationsComponent implements OnInit {

  @ViewChild('mynetwork6') visElement6: ElementRef;
  @ViewChild('mynetwork7') visElement7: ElementRef;
  @ViewChild('mynetwork8') visElement8: ElementRef;

  // create an array with edges

  constructor() { }

  ngOnInit() {

    const nodes = [
      {id: 2, label: 'First Language'},
      {id: 4, label: 'Mathematics'},
      {id: 5, label: 'Science'},
      {id: 3, label: 'English Language'},
      {id: 1, label: 'Religion'},
      {id: 6, label: 'History'},
      {id: 7, label: 'Citizenship Education'},
      {id: 11, label: 'PTS'},
      {id: 12, label: 'Art'},
      {id: 10, label: 'Geography'},
      {id: 9, label: 'Second Langauge'},
      {id: 8, label: 'Health'}
    ];

    const edges_6 = [
      {from: 1, to: 2, width:3},
      {from: 1, to: 3, width:1},
      {from: 1, to: 8, width:3},
      {from: 2, to: 3, width:3},
      {from: 2, to: 8, width:1},
      {from: 2, to: 9, width:1},
      {from: 2, to: 10, width:1},
      {from: 2, to: 12, width:1},
      {from: 3, to: 9, width:1},
      {from: 4, to: 5, width:1},
      {from: 5, to: 6, width:1},
      {from: 5, to: 7, width:1},
      {from: 5, to: 10, width:3},
      {from: 7, to: 10, width:1},
      {from: 8, to: 9, width:3},
      {from: 9, to: 10, width:1}
    ];
    const edges_7 = [
      {from: 1, to: 2, width:1},
      {from: 1, to: 3, width:1},
      {from: 1, to: 4, width:1},
      {from: 1, to: 8, width:3},
      {from: 1, to: 10, width:3},
      {from: 1, to: 11, width:1},
      {from: 2, to: 5, width:1},
      {from: 2, to: 10, width:3},
      {from: 3, to: 4, width:1},
      {from: 3, to: 9, width:1},
      {from: 4, to: 5, width:1},
      {from: 4, to: 8, width:1},
      {from: 4, to: 10, width:3},
      {from: 5, to: 8, width:1},
      {from: 5, to: 10, width:3},
      {from: 7, to: 8, width:1},
      {from: 8, to: 10, width:3}
    ];
    const edges_8 = [
      {from: 1, to: 5, width:3},
      {from: 1, to: 6, width:3},
      {from: 1, to: 7, width:1},
      {from: 3, to: 4, width:1},
      {from: 3, to: 5, width:1},
      {from: 3, to: 6, width:3},
      {from: 3, to: 10, width:3},
      {from: 5, to: 6, width:3},
      {from: 5, to: 7, width:1},
      {from: 5, to: 8, width:1},
      {from: 6, to: 7, width:1},
      {from: 6, to: 10, width:3},
      {from: 6, to: 11, width:1},
      {from: 7, to: 8, width:3}
    ];

    let options = {
      width: '800px',
      height: '500px',
      physics: {
        repulsion: {
          nodeDistance: 100,
          springLength: 100
        }
      }
    };

    new Network(this.visElement6.nativeElement, {nodes: nodes, edges: edges_6}, options);
    new Network(this.visElement7.nativeElement, {nodes: nodes, edges: edges_7}, options);
    new Network(this.visElement8.nativeElement, {nodes: nodes, edges: edges_8}, options);
  }

}
