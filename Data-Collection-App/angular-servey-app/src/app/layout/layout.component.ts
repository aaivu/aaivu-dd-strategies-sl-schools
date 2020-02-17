import { Component, OnInit } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-layout',
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss']
})
export class LayoutComponent implements OnInit {

  title = '';
  countArr = [];
  constructor(private translate: TranslateService, private route: ActivatedRoute) {
    // this language will be used as a fallback when a translation isn't found in the current language
    translate.setDefaultLang('en');

    // the lang to use, if the lang isn't available, it will use the current loader to get them
    translate.use('en');
  }

  changeLng(l) {
    this.translate.use(l);
  }

  ngOnInit() {
    this.route.data.subscribe(data => {
      this.title = data.title;
      this.countArr = [];
      for (let i = 0; i < data.count; i ++){
        this.countArr.push(i + 1);
      }
    })
  }

}
