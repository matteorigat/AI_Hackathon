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
	win.removeMenu();
    //win.webContents.openDevTools();

    ipcMain.on('open-file-dialog', (event) => {
		dialog.showOpenDialog(mainWindow, {
			properties: ['openFile']
		}).then(result => {
			if (!result.canceled) {
				win.webContents.send('start-loader');

				filePath = result.filePaths[0];
				console.log("Selected: " + filePath);
				
				fs.readFile(filePath, async (err, data) => {
					if (err) {
						console.error('Error reading file:', err);
						return;
					}

					fileName = filePath.split("\\").pop();
					text = await api.sendFile(fileName, data);
					win.webContents.send('file-text', {'text': text});
				});
			}
		}).catch(err => {
			console.log(err);
		});
	});

	ipcMain.on('summarize', async (event, text) => {
		summary = await api.summarize(text)
			.then(summary => {
				console.log(summary);
				win.webContents.send('open-modal', summary);
			});
	});

	ipcMain.on('summarize-selected', async (event, text) => {
		summary = await api.summarizeSelected(text)
			.then(summary => {
				console.log(summary);
				win.webContents.send('open-modal', summary);
			});
	});

	ipcMain.on('message', async (event, [lastResponse, context]) => {
		message = await api.sendChat(lastResponse, context)
			.then(message => {
				console.log("msg: " + message);
				win.webContents.send('message-reply', message);
				return message;
			});
	});

	ipcMain.on('send-link', async (event, link) => {
		text = await api.sendLink(link)
			.then(text => {
				console.log(text);
				win.webContents.send('web-text', {'text': text});
			});
	});
}

function createTestWindow() {
	const win = new BrowserWindow({
        width: 1200,
        height: 900,
        webPreferences: {
            contextIsolation: false,
            nodeIntegration: true
        }
    });

	ipcMain.on('question', async (event) => {
		await api.askQuestion()
			.then(question => {
				console.log(question);
				win.webContents.send('question-text', {"question": question});
			});
	})

	return win;
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