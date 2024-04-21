const { ipcRenderer } = require('electron');

ipcRenderer.on('start-loader', () => {
    var loaderContainer = document.getElementById('loaderContainer');
    loaderContainer.style.display = 'block';
});

document.getElementById('fileUploadButton')
    .addEventListener('click', (event) => {
        ipcRenderer.send('open-file-dialog');
    });

document.getElementById('summarizeButton')
    .addEventListener('click', (event) => {
        var selection = window.getSelection();
        var selectedText = selection.toString();

        if (selectedText !== "") {
            ipcRenderer.send('summarize-selected', selectedText);
            console.log("SUMMARIZE SELECTED");
        } else {
            text = document.getElementById('file-text').innerHTML;
            ipcRenderer.send('summarize', text);
            console.log("SUMMARIZE");
        }
    });


ipcRenderer.on('file-text', (event, pages)=> {
    i = 1;
    text = '<br>';
    pages.text.forEach(page => {
        text += "<b>Page " + i + "</b><br>" + page + "<br><br>";
        i++;
    });
    
    var loaderContainer = document.getElementById('loaderContainer');
    loaderContainer.style.display = 'none';
    document.getElementById('file-text').innerHTML = text;
});

ipcRenderer.on('open-modal', (event, summary) => {
    console.log("MODAL");
    document.getElementById('summarizeText').innerHTML = summary;
    document.getElementById('summarizeModal').style.display = "block";
})