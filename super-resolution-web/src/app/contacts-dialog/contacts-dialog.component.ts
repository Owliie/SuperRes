import {Component} from '@angular/core';
import {MatDialog} from '@angular/material';

@Component({
  selector: 'app-contacts-dialog',
  templateUrl: './contacts-dialog.component.html',
  styleUrls: ['./contacts-dialog.component.scss']
})
export class ContactsDialogComponent {
  constructor(public dialog: MatDialog) {
  }

  openContactsDialog() {
    const dialogRef = this.dialog.open(ContactsContentDialogComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}

@Component({
  selector: 'app-contacts-content-dialog',
  templateUrl: './contacts-dialog.component.html',
})
export class ContactsContentDialogComponent {
}
