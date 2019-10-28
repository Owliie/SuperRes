import {Component} from '@angular/core';
import {ImageService} from '../image.service';
import {MatSnackBar, SimpleSnackBar} from '@angular/material';

class ImageSnippet {
  pending = false;
  status = 'init';

  constructor(public src: string, public file: File) {
  }
}

@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html',
  styleUrls: ['./image-upload.component.scss']
})
export class ImageUploadComponent {

  constructor(private imageService: ImageService, private snackBar: MatSnackBar) {
  }

  scale = 2;
  selectedFile: ImageSnippet;

  private onSuccess() {
    this.selectedFile.pending = false;
    this.selectedFile.status = 'ok';
    this.snackBar.open('Image uploaded successfully!',
      'Dismiss',
      {duration: 2000, panelClass: ['success-snackbar']});
    this.imageService.hasUploadedPhoto = true;
  }

  private onError() {
    this.selectedFile.pending = false;
    this.selectedFile.status = 'fail';
    this.selectedFile.src = '';
    this.snackBar.open('Image upload failed!',
      'Dismiss',
      {duration: 2000, panelClass: ['danger-snackbar']});
  }

  processFile(imageInput: any) {
    const file = imageInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', (event: any) => {
      this.selectedFile = new ImageSnippet(event.target.result, file);
      this.selectedFile.pending = true;

      this.imageService.uploadImage(this.selectedFile.file, this.scale).subscribe(
        (res) => {
          this.onSuccess();
        },
        (err) => {
          console.error(err);
          this.onError();
        });
    });

    reader.readAsDataURL(file);
    reader.onload = (event) => { // called once readAsDataURL is completed
      this.imageService.changeImage(reader.result);
    }
  }

  formatLabel(value: number) {
    return 'x' + Math.pow(2, value);
  }

  changeScale(event: any) {
    this.scale = Math.pow(2, event.value);
  }

  disposeImage() {
    this.selectedFile = null;
    this.imageService.hasUploadedPhoto = false;
  }
}
