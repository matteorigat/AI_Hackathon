const url = "http://192.168.79.127:5000";

const sendFile = async function(data) {
    const path = url + '/send';

    try {
        const response = await fetch(path, {
            method: 'POST',
            body: data
        });

        if (response.ok) {
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
