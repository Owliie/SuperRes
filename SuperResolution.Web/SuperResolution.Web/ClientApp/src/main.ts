import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

export function getBaseUrl() {
    let href = document.getElementsByTagName('base')[0].href;
    return href.indexOf("http://") === -1 ? "http://localhost:9223/" : href;
}

const providers = [
    { provide: 'BASE_URL', useFactory: getBaseUrl, deps: [] }
];

if (environment.production) {
    enableProdMode();
}

platformBrowserDynamic(providers).bootstrapModule(AppModule)
    .catch(err => console.log(err));
