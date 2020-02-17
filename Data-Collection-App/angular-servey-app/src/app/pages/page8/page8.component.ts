import { Component, OnInit } from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page8',
  templateUrl: './page8.component.html',
  styleUrls: ['./page8.component.scss']
})
export class Page8Component implements OnInit {
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
        this.router.navigate(['..', '3'], {relativeTo: this.activatedRoute});
      }
    })
  }
}
