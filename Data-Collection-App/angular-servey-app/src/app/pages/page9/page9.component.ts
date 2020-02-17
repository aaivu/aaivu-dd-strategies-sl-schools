import { Component, OnInit } from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page9',
  templateUrl: './page9.component.html',
  styleUrls: ['./page9.component.scss']
})
export class Page9Component implements OnInit {
  answers = {};

  constructor(private userAPI: UserService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
  }

  done() {
    console.log(this.answers);
    //routerLink="../2"

    let res = {};

    Object.keys(this.answers).forEach(k => {
      res['Lci_' + k] = this.answers[k].substr(4);
    });

    console.log(res);
    this.userAPI.setBulk(res).subscribe(data => {
      if(data.success){
        this.router.navigate(['..', '4'], {relativeTo: this.activatedRoute});
      }
    })
  }
}
