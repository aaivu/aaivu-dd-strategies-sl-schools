import { Component, OnInit } from '@angular/core';
import {UserService} from "../../service/user.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-page10',
  templateUrl: './page10.component.html',
  styleUrls: ['./page10.component.scss']
})
export class Page10Component implements OnInit {
  answers = {};
  constructor(private userAPI: UserService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
  }

  done() {
    let res = {};

    Object.keys(this.answers).forEach(k => {
      res['Lci_' + k] = this.answers[k].substr(4);
    });
    res['lci'] = true;

    console.log(res);
    this.userAPI.setBulk(res).subscribe(data => {
      console.log(data);
      if(data.success){
        this.userAPI.setUser(data.newUser);
        this.router.navigate(['/student/data'], {relativeTo: this.activatedRoute});
      }
    })
  }
}
