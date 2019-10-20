import {Component} from '@angular/core';
import {MatDialog} from '@angular/material';

export interface ContactsInfo {
  name: string;
  email: string;
  github: string;
}

const contactsInfos: ContactsInfo[] = [
  {name: 'Mihail Gerginov', email: 'mihailgerginov01@gmail.com', github: 'TheRandomTroll'},
  {name: 'Victor Velev', email: 'victorivelev@gmail.com', github: 'VIVelev'},
  {name: 'Martin Yordanov', email: 'martistj@gmail.com', github: 'xxm0703'},
  {name: 'Georgi Lyubenov', email: 'joro2404@gmail.com', github: 'joro2404'},
  {name: 'Aneta Tsvetkova', email: 'anetastsvetkova@gmail.com', github: 'Owliie'},
];

@Component({
  selector: 'app-contacts-dialog',
  templateUrl: './contacts-dialog.component.html',
  styleUrls: ['./contacts-dialog.component.scss']
})
export class ContactsDialogComponent {
  constructor(public dialog: MatDialog) {
  }

  openContactsDialog() {
    const dialogRef = this.dialog.open(ContactsContentDialogComponent,
      {width: '70%'});

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}

@Component({
  selector: 'app-contacts-content-dialog',
  templateUrl: './contacts-dialog.component.html',
  styleUrls: ['./contacts-dialog.component.scss']
})
export class ContactsContentDialogComponent {
  displayedColumns: string[] = ['name', 'email', 'github'];
  dataSource = contactsInfos;
}
