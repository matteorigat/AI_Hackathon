from flask import Flask, send_file, request
import os
import shutil

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'Hello, World! This is Flask running in Electron.'

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        data = request.data
        print(data)

        return 'File salvato con successo', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
