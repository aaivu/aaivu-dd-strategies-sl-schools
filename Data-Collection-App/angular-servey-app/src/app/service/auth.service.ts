import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  user;
  teacherData;
  constructor() { }

  setUser(user) {
    this.user = user;
  }
}
