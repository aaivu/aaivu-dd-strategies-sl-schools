import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomePageComponent } from './home-page/home-page.component';
import {Routing} from './app.router';
import { LayoutComponent } from './layout/layout.component';
import {FlexLayoutModule} from '@angular/flex-layout';
import {DataService} from './service/data.service';
import { Page1Component } from './pages/page1/page1.component';

import {TranslateLoader, TranslateModule} from '@ngx-translate/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import {SuiModule} from "ng2-semantic-ui";
import {FormsModule} from "@angular/forms";
import { Page2Component } from './pages/page2/page2.component';
import { Page3Component } from './pages/page3/page3.component';
import { Page4Component } from './pages/page4/page4.component';
import { Page5Component } from './pages/page5/page5.component';
import { Page6Component } from './pages/page6/page6.component';
import { Page7Component } from './pages/page7/page7.component';
import { Page8Component } from './pages/page8/page8.component';
import { Page9Component } from './pages/page9/page9.component';
import { Page10Component } from './pages/page10/page10.component';
import { FinishComponent } from './pages/finish/finish.component';
import { DataComponent } from './data/data.component';
import { StdMarksComponent } from './dashboards/std-marks/std-marks.component';
import {
  TchMarksComponent
} from './dashboards/tch-marks/tch-marks.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { RegisterPageComponent } from './register-page/register-page.component';
import { MarksFormComponent } from './pages/marks-form/marks-form.component';
import { MarksCorelationsComponent } from './dashboards/marks-corelations/marks-corelations.component';
import { StdDashComponent } from './dashboards/std-dash/std-dash.component';
import { TchDashComponent } from './dashboards/tch-dash/tch-dash.component';
import { LearningStylesComponent } from './dashboards/learning-styles/learning-styles.component';


@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    LayoutComponent,
    Page1Component,
    Page2Component,
    Page3Component,
    Page4Component,
    Page5Component,
    Page6Component,
    Page7Component,
    Page8Component,
    Page9Component,
    Page10Component,
    FinishComponent,
    DataComponent,
    StdMarksComponent,
    TchMarksComponent,
    LoginPageComponent,
    RegisterPageComponent,
    MarksFormComponent,
    MarksCorelationsComponent,
    StdDashComponent,
    TchDashComponent,
    LearningStylesComponent,
  ],
  imports: [
    BrowserModule,
    Routing,
    FlexLayoutModule,
    HttpClientModule,
    SuiModule,
    FormsModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpClient]
      }
    }),
  ],
  providers: [DataService, HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }


// AoT requires an exported function for factories
export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
