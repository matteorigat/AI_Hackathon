import ollama

models = ['gemma:2b', 'gemma:7b']
model = models[0]

def get_bulletpoints(text):
    text_input ="Make a bullet point text summarization of the following text: "+ text
    response = ollama.chat(model=model, messages=[
        {
            "role": "system",
            "content": "You are an expert text summarizer"
        },
        {
            "role": "user",
            "content": text_input
        },
    ])
    return '\n'.join(response['message']['content'].split("\n")[1:])

def get_summarization(text):
    text_input ="Make a concise summarization of the following text, knowing that they are pages of a pdf:"+ text
    response = ollama.chat(model=model, messages=[
        {
            "role": "system",
            "content": "You are an expert text summarizer"
        },
        {
            "role": "user",
            "content": text_input
        },
    ])
    return '\n'.join(response['message']['content'].split("\n")[1:])

def make_questions(text, question):
    text_input ="Given the following context: "+ text + " answer the following question: "+ question
    response = ollama.chat(model=model, messages=[
        {
            "role": "user",
            "content": text_input
        },
    ])
    return response['message']['content']

def get_questions(text):
    text_input ="Generate 10 questions about the following text "+ text
    response = ollama.chat(model=model, messages=[
        {
            "role": "system",
            "content": "You are an expert question maker"
        },
        {
            "role": "user",
            "content": text_input
        },
    ])
    return response['message']['content']

