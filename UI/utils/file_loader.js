const { ipcRenderer } = require('electron');

// add file button handler
document.getElementById('fileUploadButton')
    .addEventListener('click', (event) => {
        ipcRenderer.send('open-file-dialog');
    });