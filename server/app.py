from flask import Flask, request
import os
from langChain import Model_Class

import ollama
models = ['gemma:2b', 'gemma:7b']
model = models[0]
current_file_name = ""
file_dict = {}

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'Hello, World! This is Flask running in Electron.'

@app.route('/send', methods=['POST'])
def send():
    global current_file_name
    if request.method == 'POST':
        json = request.json
        bytes_base64 = json.get('data')
        filename = json.get('fileName')
        current_file_name = filename
        
        folder_name = "data/"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print("Folder created correctly")

        file_path = folder_name + filename
        rebuild_file(bytes(bytes_base64['data']), file_path)

        model_class = Model_Class(file_path)
        text = model_class.get_pdf_text()
        text = model_class.format_text_per_page(text)

        file_dict[filename] = {'model_class': model_class, 'text': text}

        return text, 200


@app.route('/full_text_summarize', methods=['POST'])
def full_text_summarize():
    if request.method == 'POST':
        json = request.json
        input_text = json.get('data')

        text = file_dict[current_file_name]['model_class'].get_summarize(input_text)
        #print(text['output_text'])
        text = '\n'.join(text['output_text'].split("\n")[1:])
        return text, 200
    else:
        return "", 404

@app.route('/short_text_summarize', methods=['POST'])
def short_text_summarize():
    if request.method == 'POST':
        json = request.json
        input_text = json.get('data')

        text = file_dict[current_file_name]['model_class'].get_short_summarize(input_text)
        return text, 200
    else:
        return "", 404

"""
@app.route('/answer_question', methods=['POST'])
def answer_question():
    if request.method == 'POST':
        json = request.json
        input_text = json.get('data')

        Model_Class.init_chain(text)
        Model_Class.get_answer(input_text)
        return text, 200
    else:
        return "", 404
"""


@app.route('/selected_questions', methods=['POST'])
def selected_questions():
    if request.method == 'POST':
        json = request.json
        input_text = json.get('data')
        text = file_dict[current_file_name]['model_class'].get_questions(input_text)
        return text, 200
    else:
        return "", 404

"""
@app.route('/chapter_bulletpoints', methods=['POST'])
def chapter_bulletpoints():
    if request.method == 'POST':
        json = request.json
        input_text = json.get('data')
        text = get_bulletpoints(input_text)
        return text, 200
    else:
        return "", 404
"""


def rebuild_file(bytes, file_path):    
    with open(file_path, 'wb') as file:
        file.write(bytes)    
        print("File successfully rebuilt.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=23456)





