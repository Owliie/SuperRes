import {Component, Input, OnInit} from '@angular/core';
import {ImageUploadComponent} from '../image-upload/image-upload.component';
import {ImageService} from '../image.service';

@Component({
  selector: 'app-image-scaler',
  templateUrl: './image-scaler.component.html',
  styleUrls: ['./image-scaler.component.scss'],
  providers: [ImageUploadComponent]
})
export class ImageScalerComponent implements OnInit {
  private image: File;
  constructor(private imageService: ImageService, public imageUploaded: ImageUploadComponent) {}

  ngOnInit() {
    this.imageService.image.subscribe(image => this.image = image);
  }

}
