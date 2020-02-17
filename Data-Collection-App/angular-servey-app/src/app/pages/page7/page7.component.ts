import { Component, OnInit } from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page7',
  templateUrl: './page7.component.html',
  styleUrls: ['./page7.component.scss']
})
export class Page7Component implements OnInit {
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
        this.router.navigate(['..', '2'], {relativeTo: this.activatedRoute});
      }
    })
  }

}
