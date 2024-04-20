const { ipcRenderer } = require('electron');

document.getElementById('fileUploadButton')
    .addEventListener('click', (event) => {
        ipcRenderer.send('open-file-dialog');
    });


ipcRenderer.on('file-text', (event, pages)=> {
    text = pages.text.join(' ');
    document.getElementById('file-text').innerHTML = text;
});