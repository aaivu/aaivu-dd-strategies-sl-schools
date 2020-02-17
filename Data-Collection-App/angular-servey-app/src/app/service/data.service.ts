import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable()
export class DataService {

  appPath = 'http://localhost:3000/ds/';
  currentId = '';

  constructor(private http: HttpClient) { }

  create() {
    this.http.post(this.appPath + 'create', {}).subscribe(data => {
      this.currentId = data['id'];
    });
  }

  update(page, data) {
    this.http.post(this.appPath + this.currentId + '/update?page='+ page, data).subscribe(data => {
      return data;
    });
  }

  read(id): Promise<any> {
    return new Promise(resolve => {
      this.http.get(this.appPath + id).subscribe(data => {
        resolve(data);
      })
    });
  }

  readPage(id, page): Promise<any> {
    return new Promise(resolve => {
      this.http.get(this.appPath + id + '/' + page).subscribe(data => {
        resolve(data);
      })
    });
  }


}
