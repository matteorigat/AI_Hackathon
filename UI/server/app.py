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
        # Verifica se la richiesta contiene un file
        print(request.files)
        if 'file' not in request.files:
            return 'Nessun file inviato', 400
        
        """file = request.files['file']
        # Verifica se il file è stato selezionato
        if file.filename == '':
            return 'Nessun file selezionato', 400
        
        # Salva il file sul server
        upload_folder = 'upload'
        file.save(os.path.join(upload_folder, file.filename))"""

        return 'File salvato con successo', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
