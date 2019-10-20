import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material';

@Component({
  selector: 'app-about-us-dialog',
  templateUrl: './about-us-dialog.component.html',
  styleUrls: ['./about-us-dialog.component.scss']
})
export class AboutUsDialogComponent {
  constructor(public dialog: MatDialog) {}
  openAboutUsDialog() {
    const dialogRef = this.dialog.open(AboutUsContentDialogComponent, {width: '50%'});

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}

@Component({
  selector: 'app-about-us-content-dialog',
  templateUrl: './about-us-dialog.component.html',
})
export class AboutUsContentDialogComponent {}
