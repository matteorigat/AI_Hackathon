const url = "http://192.168.79.34:23456";

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

module.exports = {
    sendFile
};
