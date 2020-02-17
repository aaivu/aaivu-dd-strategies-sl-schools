import { Component, OnInit } from '@angular/core';
import {UserService} from "../service/user.service";
import {AuthService} from "../service/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {

  login = {
    username: '',
    password: ''
  };

  constructor(private userAPI: UserService, private auth: AuthService, private router: Router) { }

  ngOnInit() {
  }

  submit_form() {
    this.userAPI.login(this.login).subscribe(data => {
      if(data.success){
        this.auth.setUser(data.user);
        console.log('successfully logged in');
        console.log(data);
        if(data.user.type === 's') {
          this.router.navigate(['student'])
        } else if(data.user.type === 't') {
          this.router.navigate(['teacher'])
        } else if(data.user.type === 'p') {
          this.router.navigate(['parents'])
        }
      } else {
        console.log('error');
      }
    });
  }
}
