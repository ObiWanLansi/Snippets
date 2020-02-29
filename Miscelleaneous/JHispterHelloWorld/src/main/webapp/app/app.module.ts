import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import './vendor';
import { JHispterHellWorldSharedModule } from 'app/shared/shared.module';
import { JHispterHellWorldCoreModule } from 'app/core/core.module';
import { JHispterHellWorldAppRoutingModule } from './app-routing.module';
import { JHispterHellWorldHomeModule } from './home/home.module';
import { JHispterHellWorldEntityModule } from './entities/entity.module';
// jhipster-needle-angular-add-module-import JHipster will add new module here
import { MainComponent } from './layouts/main/main.component';
import { NavbarComponent } from './layouts/navbar/navbar.component';
import { FooterComponent } from './layouts/footer/footer.component';
import { PageRibbonComponent } from './layouts/profiles/page-ribbon.component';
import { ErrorComponent } from './layouts/error/error.component';

@NgModule({
  imports: [
    BrowserModule,
    JHispterHellWorldSharedModule,
    JHispterHellWorldCoreModule,
    JHispterHellWorldHomeModule,
    // jhipster-needle-angular-add-module JHipster will add new module here
    JHispterHellWorldEntityModule,
    JHispterHellWorldAppRoutingModule
  ],
  declarations: [MainComponent, NavbarComponent, ErrorComponent, PageRibbonComponent, FooterComponent],
  bootstrap: [MainComponent]
})
export class JHispterHellWorldAppModule {}
