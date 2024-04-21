const { ipcRenderer } = require('electron');

ipcRenderer.on('start-loader-eval', () => {
    var loaderContainer = document.getElementById('loaderContainer');
    loaderContainer.style.display = 'block';
});

ipcRenderer.on('question-text', (event, question)=> {
    console.log(question);
    document.getElementById('question-text').innerHTML = question;
});


document.addEventListener('DOMContentLoaded', function() {

    console.log("sus");
    ipcRenderer.send('question');

});

document.getElementById('sendAnswerButton').addEventListener('click', (event) => {
    ipcRenderer.send('send-answer', document.getElementById('answerInput').value);
});


ipcRenderer.on('answer-text', (event, text)=> {
    console.log(text);
    document.getElementById('answer-text-box').innerHTML = text;
});