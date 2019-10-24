import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AngularMaterialModule } from './angular-material.module';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {ContactsContentDialogComponent, ContactsDialogComponent} from './contacts-dialog/contacts-dialog.component';
import {MatDialogModule, MatProgressSpinnerModule, MatSnackBarModule} from '@angular/material';
import {AboutUsContentDialogComponent, AboutUsDialogComponent} from './about-us-dialog/about-us-dialog.component';
import {ProductContentDialogComponent, ProductDialogComponent} from './product-dialog/product-dialog.component';
import { ImageUploadComponent } from './image-upload/image-upload.component';
import {HttpClientModule} from '@angular/common/http';
import { ImageScalerComponent } from './image-scaler/image-scaler.component';
import { TitleComponent } from './title/title.component';

@NgModule({
  declarations: [
    AppComponent,
    ContactsDialogComponent,
    ContactsContentDialogComponent,
    AboutUsDialogComponent,
    AboutUsContentDialogComponent,
    ProductDialogComponent,
    ProductContentDialogComponent,
    ImageUploadComponent,
    ImageScalerComponent,
    TitleComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    AngularMaterialModule,
    MatDialogModule,
    HttpClientModule,
    MatSnackBarModule,
    BrowserAnimationsModule,
    MatProgressSpinnerModule
  ],
  entryComponents: [
    ContactsContentDialogComponent,
    AboutUsContentDialogComponent,
    ProductContentDialogComponent
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
