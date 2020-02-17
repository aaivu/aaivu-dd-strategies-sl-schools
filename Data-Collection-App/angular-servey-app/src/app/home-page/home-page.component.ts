import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {TranslateService} from "@ngx-translate/core";
import {UserService} from "../service/user.service";
import {AuthService} from "../service/auth.service";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  person: any;
  user;
  constructor(private route: ActivatedRoute, private userAPI: UserService, private auth: AuthService,
              private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe(data => {
      this.person = data.person;
      if(this.person === 'student') {
        this.router.navigate(['data'], {relativeTo: this.activatedRoute});
      } else if (this.person === 'teacher') {
        this.router.navigate(['tch-dash'], {relativeTo: this.activatedRoute});
      }
    });
    this.user = this.auth.user;
    if(!this.user) {
      this.router.navigate(['/login']);
    }
  }

}
