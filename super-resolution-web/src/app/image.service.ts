import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ImageService {
  public hasUploadedPhoto = false;

  constructor(private http: HttpClient) {
  }

  public uploadImage(image: File, scale: number): Observable<Response> {
    const formData = new FormData();

    formData.append('image', image);
    formData.append('scale', '' + scale);

    return this.http.post<Response>('https://localhost:5001/api/image', formData);
  }
}
