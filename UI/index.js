const { app, BrowserWindow, ipcMain, dialog } = require('electron');  
const fs = require('fs');
const api = require("./utils/api");

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 900,
        webPreferences: {
            contextIsolation: false,
            nodeIntegration: true
        }
    });

    win.loadFile('index.html');
    win.webContents.openDevTools();

    ipcMain.on('open-file-dialog', (event, file) => {
		api.sendPDF(file);
	});
}

app.whenReady().then(() => {
    mainWindow = createWindow();

    app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
});