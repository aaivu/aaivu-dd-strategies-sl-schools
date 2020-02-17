import { Component, OnInit } from '@angular/core';
import {AuthService} from "../service/auth.service";

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.scss']
})
export class DataComponent implements OnInit {

  user;
  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.user = this.auth.user;
  }

}
