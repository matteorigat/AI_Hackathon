from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
import chromadb

# https://github.com/ollama/ollama/blob/main/docs/tutorials/langchainpy.md

# for load a webpage
#loader = WebBaseLoader("https://www.gutenberg.org/files/1727/1727-h/1727-h.htm")
#data = loader.load()

class Chain_Class:
    def __init__(self):
        self.ollama = Ollama(base_url='http://localhost:11434', model="gemma:2b")

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


    def get_summarization(self, document):

        map_prompt_template = """
                              Write a summary of this chunk of text that includes the main points and any important details.
                              {text}
                              """

        map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])

        combine_prompt_template = """
                              Write a concise summary of the following text delimited by triple backquotes.
                              Return your response in bullet points which covers the key points of the text.
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




