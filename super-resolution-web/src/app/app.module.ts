import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AngularMaterialModule } from './angular-material.module';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {ContactsContentDialogComponent, ContactsDialogComponent} from './contacts-dialog/contacts-dialog.component';
import {MatDialogModule} from '@angular/material';

@NgModule({
  declarations: [
    AppComponent,
    ContactsDialogComponent,
    ContactsContentDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    AngularMaterialModule,
    MatDialogModule
  ],
  entryComponents: [
    ContactsDialogComponent,
    ContactsContentDialogComponent
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
