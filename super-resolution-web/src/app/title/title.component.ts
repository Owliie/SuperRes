import { Component, OnInit, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-title',
  templateUrl: './title.component.html',
  styleUrls: ['./title.component.scss']
})
export class TitleComponent implements OnInit {

  constructor(private viewContainerRef: ViewContainerRef) { }

  ngOnInit() {
  }

  selfDestruct(): void {
    this.viewContainerRef
    .element
    .nativeElement
    .parentElement
    .removeChild(this.viewContainerRef.element.nativeElement);
  }
}
