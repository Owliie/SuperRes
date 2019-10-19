import {Component} from '@angular/core';
import {ContactsDialogComponent} from './contacts-dialog/contacts-dialog.component';

/**
 * @title Autosize sidenav
 */
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  providers: [ContactsDialogComponent]
})
export class AppComponent {
  constructor(private contacts: ContactsDialogComponent){}

  public openContactsDialog(): void {
    this.contacts.openContactsDialog();
  }
}
