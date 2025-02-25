const url = "http://127.0.0.1:23456";

const sendFile = async function(fileName, data) {
    const path = url + '/send';

    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fileName, data })
        });

        if (response.ok) {
            text = await response.json()
                .then(data => data)
                .catch(err => console.log(err));
            
            console.log('File sent successfully!');
            return text;
        } else {
            console.error('Failed to send file:', response.status);
        }
    } catch (error) {
        console.error('An error occurred while sending the file:', error);
    }
}

const sendLink = async (link) => {
    const path = url + '/send_web';
    data = link;
    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data })
        });

        if (response.ok) {
            text = await response.json()
                .then(data => data)
                .catch(err => console.log(err));
            
            console.log('Link sent successfully!');
            return text;
        } else {
            console.error('Failed to send link:', response.status);
        }
    } catch (error) {
        console.error('An error occurred while sending the link:', error);
    }
}


const summarize = async (text) => {
    const path = url + '/full_text_summarize';
    data = text;
    
    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data })
        });
    
        if (response.ok) {
            text = await response.text();
            return text;
        } else {
            console.log("Failed to receive summary", response.status);
            return null;
        }
    } catch (err) {
        console.error('An error occurred while sending the file:', err);
    }
}

const summarizeSelected = async (text) => {
    const path = url + '/short_text_summarize';
    data = text;
    
    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data })
        });
    
        if (response.ok) {
            text = await response.text();
            return text;
        } else {
            console.log("Failed to receive summary", response.status);
            return null;
        }
    } catch (err) {
        console.error('An error occurred while sending the file:', err);
    }
}

const sendChat = async (lastResponse, context) => {
    const path = url + '/chat';
    data = lastResponse;
    
    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data, context })
        });
    
        if (response.ok) {
            text = await response.text();
            return text;
        } else {
            console.log("Failed to receive message", response.status);
            return null;
        }
    } catch (err) {
        console.error('An error occurred while sending the message:', err);
    }
}

const askQuestion = async () => {
    const path = url + '/ask_question';

    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            text = await response.text();
            return text;
        } else {
            console.log("Failed to receive question", response.status);
            return null;
        }
    } catch (err) {
        console.error('An error occurred while asking the question:', err);
    }
}

const sendResponse = async (answer) => {
    const path = url + '/send_answer';
    data = answer;

    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data })
        });

        if (response.ok) {
            text = await response.text();
            return text;
        } else {
            console.log("Failed to send answer", response.status);
            return null;
        }
    } catch (err) {
        console.error('An error occurred while sending the answer:', err);
    }
}

module.exports = {
    sendFile,
    summarize,
    summarizeSelected,
    sendChat,
    sendLink,
    askQuestion,
    sendResponse
};
