const { ipcRenderer } = require('electron');

ipcRenderer.on('start-loader', () => {
    var loaderContainer = document.getElementById('loaderContainer');
    loaderContainer.style.display = 'block';
});

document.getElementById('fileUploadButton')
    .addEventListener('click', (event) => {
        ipcRenderer.send('open-file-dialog');
    });

document.getElementById('addLinkButton')
    .addEventListener('click', (event) => {
        ipcRenderer.send('send-link', document.getElementById('linkInput').value);
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

ipcRenderer.on('web-text', (event, pages)=> {
    i = 1;
    text = '<br>';
    pages.text.forEach(page => {
        text += page + "<br>";
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
});

document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.getElementById('messages');
    const userPrefix = 'user: ';
    const systemPrefix = 'system: ';
    const userMessages = [];
    const systemMessages = [];

    function addMessage(message, isUser) {
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('message');
      if (isUser) {
        messageDiv.textContent = userPrefix + message;
        userMessages.push(message);
      } else {
        messageDiv.textContent = systemPrefix + message;
        systemMessages.push(message);
      }
      messagesContainer.appendChild(messageDiv);
      messagesContainer.appendChild(document.createElement('br')); // Aggiunge una nuova riga dopo il messaggio
    }

    function addTextareaAndButton() {
      const textarea = document.createElement('textarea');
      textarea.classList.add('form-control', 'mb-3');
      textarea.placeholder = 'Inserisci testo';
      textarea.rows = '3';

      const button = document.createElement('button');
      button.classList.add('btn', 'btn-outline-secondary', 'mb-3');
      button.type = 'button';
      button.innerHTML = '<i class="fas fa-paper-plane send-icon"></i> Invia';

      button.addEventListener('click', function() {
        const textareaValue = textarea.value.trim();
        if (textareaValue !== '') {
            addMessage(textareaValue, true); // Aggiunge il messaggio dell'utente
            textarea.disabled = true;
            button.disabled = true;

            context = []
            for (i = 0; i < userMessages.length-1; i++) {
                context.push("user: " + userMessages[i] + "\n");
                context.push("system: " + systemMessages[i] + "\n");
            }
            
            ipcRenderer.send('message', [textareaValue, context]);
            
            ipcRenderer.on('message-reply', (event, message) => {
                addMessage(message, false);
                addTextareaAndButton();
            });
        }
      });

      messagesContainer.appendChild(textarea);
      messagesContainer.appendChild(button);
      textarea.focus();
    }

    addTextareaAndButton();
  });

  ipcRenderer.on('toggle-summarize', () => {
    var button = document.getElementById('summarizeButton');
    if (button.innerText === 'Summarize') {
        button.innerHTML = '<div class="loaderButton"></div>';
    } else {
        button.innerText = 'Summarize';
    }
});