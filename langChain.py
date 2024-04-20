from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain




from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


import chromadb
import ollama

# https://github.com/ollama/ollama/blob/main/docs/tutorials/langchainpy.md

# for load a webpage
#loader = WebBaseLoader("https://www.gutenberg.org/files/1727/1727-h/1727-h.htm")
#data = loader.load()

class Model_Class:
    def __init__(self, path):
        self.file_path = path
        self.model = "gemma:2b"
        self.ollama = Ollama(base_url='http://localhost:11434', model=self.model)


    def get_pdf_text(self):
        text_per_page = {}
        for page_layout in extract_pages(self.file_path):
            page_text = ""
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    page_text += element.get_text()
            text_per_page[page_layout.pageid] = page_text
        return text_per_page

    def format_text_per_page(self, output_dict):
        formatted_output = []
        for page_num, text in output_dict.items():
            text = text.replace('\n', ' ')
            formatted_output.append(f"{text}") #f"Page {page_num}:\n{text}\n\n"
        return formatted_output

    def init_chain(self, text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500)
        all_splits = text_splitter.create_documents(text)

        oembed = OllamaEmbeddings(base_url="http://localhost:11434", model="gemma:2b")
        self.vectorstore = Chroma.from_documents(documents=all_splits, embedding=oembed)

    def get_answer(self, question):
        # docs = vectorstore.similarity_search(question)
        # print(docs)
        # print("\n\n\n\n")

        qachain = RetrievalQA.from_chain_type(self.ollama, retriever=self.vectorstore.as_retriever())
        response = qachain.invoke({"query": question})

        return response


    def get_summarize(self, document):

        map_prompt_template = """
                              Write a very short summary of this chunk of text that includes the main points and any important details.
                              {text}
                              """

        map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])

        combine_prompt_template = """
                              Write a concise summary of the following text delimited by triple backquotes.
                              Return your response in bullet points which covers the key points of the text.
                              Do not forget the points from the top to the bottom of the text.
                              ```{text}```
                              BULLET POINT SUMMARY:
                              """

        combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=["text"])

        map_reduce_chain = load_summarize_chain(
            self.ollama,
            chain_type="map_reduce",
            map_prompt=map_prompt,
            combine_prompt=combine_prompt,
            return_intermediate_steps=True,
        )

        map_reduce_outputs = map_reduce_chain({"input_documents": document})

        return map_reduce_outputs

    def get_short_summarize(self, text):
        text_input = "Make a concise summarization of the following text, knowing that they are pages of a pdf:" + text
        response = ollama.chat(model=self.model, messages=[
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

    def get_questions(self, text):
        text_input = "Generate 10 questions about the following text " + text
        response = ollama.chat(model=self.model, messages=[
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

    def get_bulletpoints(self, text):
        text_input = "Make a bullet point text summarization of the following text: " + text
        response = ollama.chat(model=self.model, messages=[
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




