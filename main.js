const {app, BrowserWindow} = require('electron')
const path = require('path')

let mainWindow

function createWindow () {
  // Create the browser window.
    mainWindow = new BrowserWindow({
        width: 1080,
        height: 720,
        webPreferences: {
        preload: path.join(__dirname, 'preload.js')
    }
  })

    mainWindow.loadFile(
      
      url.format({
        pathname: path.join(__dirname, './SuperResolution.Web/SuperResolution.Web/ClientApp/dist/index.html'),
        protocol: "file:",
        slashes: true,
      })
      
      )

    mainWindow.setMenu(null)

    mainWindow.on('closed', function () {

        mainWindow = null
  })
}

app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  
    if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {

    if (mainWindow === null) createWindow()
})
