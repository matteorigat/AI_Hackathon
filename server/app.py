from flask import Flask, send_file, request
import os

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'Hello, World! This is Flask running in Electron.'

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        json = request.json
        bytes_base64 = json.get('data')
        filename = json.get('fileName')
        
        folder_name = "data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print("Folder created correctly")

        print(bytes_base64['data'])
        rebuild_file(bytes(bytes_base64['data']), filename)
        return 'File salvato con successo', 200
    
def rebuild_file(bytes, filename):    
    with open("data/" + filename, 'wb') as file:
        file.write(bytes)    
        print("File successfully rebuilt.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')