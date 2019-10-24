const {app, BrowserWindow} = require('electron');
const path = require('path');
const url = require('url');

let mainWindow;

function createWindow() {
    // Create the browser window.
    mainWindow = new BrowserWindow({
        width: 1080,
        height: 720,
    });

    mainWindow.loadURL('file://B:/Visual\ Studio\ Projects/SuperRes/super-resolution-web/dist/super-resolution/index.html');

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', function () {

    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {

    if (mainWindow === null) createWindow();
});
