const { ipcRenderer } = require('electron');

document.getElementById('fileUploadButton')
    .addEventListener('click', (event) => {
        ipcRenderer.send('open-file-dialog');
    });


ipcRenderer.on('file-text', (event, pages)=> {
    i = 1;
    text = '<br>';
    pages.text.forEach(page => {
        text += "<b>Page " + i + "</b><br>" + page + "<br><br>";
        i++;
    });
    document.getElementById('file-text').innerHTML = text;
});