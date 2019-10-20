import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageScalerComponent } from './image-scaler.component';

describe('ImageScalerComponent', () => {
  let component: ImageScalerComponent;
  let fixture: ComponentFixture<ImageScalerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ImageScalerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ImageScalerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
