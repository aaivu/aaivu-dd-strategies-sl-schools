import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private domain = 'http://localhost:5000/api/user/';
  private headder = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient, private auth: AuthService) {
  }

  register(data): Observable<any> {
    return this.http.post(this.domain + 'create', data, this.headder)
  }

  login(data): Observable<any> {
    return this.http.post(this.domain + 'login', data, this.headder)
  }

  setData(key, value): Observable<any> {
    let data = {};
    data[key] = value;
    return this.http.post(this.domain + 'data/update', {
      id : this.auth.user._id['$oid'],
      data: data
    }, this.headder)
  }

  setBulk(data): Observable<any> {
    return this.http.post(this.domain + 'data/update', {
      id: this.auth.user._id['$oid'],
      data: data
    }, this.headder)
  }

  setUser(user) {
    this.auth.setUser(user);
  }

  setAnalitics(): Observable<any> {
    return this.http.post(this.domain + 'data/analytics', {
      id: this.auth.user._id['$oid'],
    }, this.headder)
  }

  getTeacherData() {
    return this.http.get(this.domain + 'teacher/getdata', this.headder)
  }
}
