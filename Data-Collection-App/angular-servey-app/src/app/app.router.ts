import {RouterModule, Routes} from '@angular/router';
import {HomePageComponent} from './home-page/home-page.component';
import {LayoutComponent} from './layout/layout.component';
import {Page5Component} from "./pages/page5/page5.component";
import {Page4Component} from "./pages/page4/page4.component";
import {Page3Component} from "./pages/page3/page3.component";
import {Page2Component} from "./pages/page2/page2.component";
import {Page9Component} from "./pages/page9/page9.component";
import {Page8Component} from "./pages/page8/page8.component";
import {Page7Component} from "./pages/page7/page7.component";
import {Page6Component} from "./pages/page6/page6.component";
import {Page10Component} from "./pages/page10/page10.component";
import {DataComponent} from "./data/data.component";
import {StdMarksComponent} from "./dashboards/std-marks/std-marks.component";
import {TchMarksComponent} from "./dashboards/tch-marks/tch-marks.component";
import {LoginPageComponent} from "./login-page/login-page.component";
import {RegisterPageComponent} from "./register-page/register-page.component";
import {MarksFormComponent} from "./pages/marks-form/marks-form.component";
import {MarksCorelationsComponent} from "./dashboards/marks-corelations/marks-corelations.component";
import {StdDashComponent} from "./dashboards/std-dash/std-dash.component";
import {TchDashComponent} from "./dashboards/tch-dash/tch-dash.component";
import {LearningStylesComponent} from "./dashboards/learning-styles/learning-styles.component";


const ROUTS: Routes = [
  {path: 'login', component: LoginPageComponent},
  {path: 'signup', component: RegisterPageComponent},
  {
    path: 'student/data/subjects', component: LayoutComponent,
    data: {title: 'Subject', count: 2}, children: [
      {path: '', redirectTo: '1', pathMatch: 'full'},
      {path: '1', component: Page2Component},
      {path: '2', component: Page3Component},
    ]
  },
  {
    path: 'student/data/family', component: LayoutComponent,
    data: {title: 'Family Background', count: 1}, children: [
      {path: '', redirectTo: '1', pathMatch: 'full'},
      {path: '1', component: Page4Component},
    ]
  },
  {
    path: 'student/data/extracurricular', component: LayoutComponent,
    data: {title: 'Extracurricular Activities', count: 2}, children: [
      {path: '', redirectTo: '1', pathMatch: 'full'},
      {path: '1', component: Page5Component},
      {path: '2', component: Page6Component},
    ]
  },
  {
    path: 'student/data/learning-style', component: LayoutComponent,
    data: {title: 'Learning Styles', count: 4}, children: [
      {path: '', redirectTo: '1', pathMatch: 'full'},
      {path: '1', component: Page7Component},
      {path: '2', component: Page8Component},
      {path: '3', component: Page9Component},
      {path: '4', component: Page10Component},
    ]
  },
  {path: 'student/data/performance', component: MarksFormComponent},
  {
    path: ':person', component: HomePageComponent, children: [
      {path: 'std-dash', component: StdDashComponent},
      {path: 'tch-dash', component: TchDashComponent},
      {path: 'correlation', component: MarksCorelationsComponent},
      {path: 'data', component: DataComponent},
      {path: 'std-marks', component: StdMarksComponent},
      {path: 'tch-marks', component: TchMarksComponent},
      {path: 'learning-styles', component: LearningStylesComponent}
    ]
  },
  {path: '**', pathMatch: 'full', redirectTo: 'login'}
];

export const Routing = RouterModule.forRoot(ROUTS);

