const url = "http://192.168.79.127:5000";

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
            const responseData = await response.json();
            const rispostaElement = document.getElementById('risposta');
            if (rispostaElement) {
                rispostaElement.textContent = responseData.message;
            }
            console.log('File sent successfully!');
        } else {
            console.error('Failed to send file:', response.status);
        }
    } catch (error) {
        console.error('An error occurred while sending the file:', error);
    }
}

module.exports = {
    sendFile
};
