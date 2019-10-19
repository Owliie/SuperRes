import { Component } from '@angular/core';
import {MatDialog} from '@angular/material';

@Component({
  selector: 'app-product-dialog',
  templateUrl: './product-dialog.component.html',
  styleUrls: ['./product-dialog.component.scss']
})
export class ProductDialogComponent {
  constructor(public dialog: MatDialog) {}
  openProductDialog() {
    const dialogRef = this.dialog.open(ProductContentDialogComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }
}

@Component({
  selector: 'app-product-content-dialog',
  templateUrl: './product-dialog.component.html',
})
export class ProductContentDialogComponent {}
