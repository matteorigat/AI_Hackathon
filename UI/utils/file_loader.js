const { ipcRenderer } = require('electron');

// add file button handler
document.getElementById('fileUploadButton')
    .addEventListener('change', (event) => {
        const file = event.target.files[0];
        ipcRenderer.send('open-file-dialog', file);
    });