import { Component, OnInit } from '@angular/core';
import {UserService} from "../service/user.service";

@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.scss']
})
export class RegisterPageComponent implements OnInit {

  user = {
    username: 'viranmalaka',
    email: 'dg@gdsc.cd',
    name: 'Viran',
    password: 'test',
    confirm: 'test',
    type: {name: 'Student', id: 's'}
  };

  options = [
    {name: 'Student', id: 's'},
    {name: 'Teacher', id: 't'},
    {name: 'Parent', id: 'p'}];

  constructor(private userService: UserService) { }

  ngOnInit() {
  }

  submit_form() {
    if(this.user.password === this.user.confirm){
      this.userService.register({
        username: this.user.username,
        email: this.user.email,
        name: this.user.name,
        password: this.user.password,
        type: this.user.type.id
      }).subscribe(data => {
        console.log(data);
      })
    }
  }
}
