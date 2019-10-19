import {Component} from '@angular/core';
import {ContactsDialogComponent} from './contacts-dialog/contacts-dialog.component';
import {AboutUsDialogComponent} from './about-us-dialog/about-us-dialog.component';
import {ProductDialogComponent} from './product-dialog/product-dialog.component';

/**
 * @title Autosize sidenav
 */
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  providers: [ContactsDialogComponent, AboutUsDialogComponent, ProductDialogComponent]
})
export class AppComponent {
  constructor(private contacts: ContactsDialogComponent, private aboutUs: AboutUsDialogComponent,
              private product: ProductDialogComponent) {}

  public openContactsDialog(): void {
    this.contacts.openContactsDialog();
  }
  public openAboutUsDialog(): void {
    this.aboutUs.openAboutUsDialog();
  }
  public openProductDialog(): void {
    this.product.openProductDialog();
  }
}
