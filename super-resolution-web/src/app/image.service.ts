import {Injectable} from '@angular/core';
import {BehaviorSubject, Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ImageService {
  public hasUploadedPhoto = false;
  private imageSource = new BehaviorSubject(null);
  public image = this.imageSource.asObservable();

  constructor(private http: HttpClient) {
  }

  public uploadImage(image: File, scale: number): Observable<Response> {
    const formData = new FormData();

    formData.append('image', image);
    formData.append('scale', '' + scale);

    return this.http.post<Response>('https://localhost:5001/api/image', formData);
  }

  public changeImage(image: string | ArrayBuffer) {
    this.imageSource.next(image);
  }
}
