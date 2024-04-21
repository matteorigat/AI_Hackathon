# leggere pdf
# riassunto overview sopra i capitoli o i testi
#  Bullet points o cose del genere
# generazione domande di fine capitolo
#  verifica della correttezza delle risposte
# Generazione delle flashcards
# estrazione del testo da audio / video (magari usare ffmpeg)
# riutilizzo delle operazioni precedenti con la trascrizione
# Dare opzione di usare font che possono leggere persone dislessiche (?)
# Dare opzione di fare un read aloud

import gemma
import pdf_miner
import langChain
from langchain_community.document_loaders import PyPDFLoader

if __name__ == '__main__':
    # Example usage
    pdf_path = 'pdf/P1-10-sequence-learning.pdf'
    text = pdf_miner.extract_text_from_pdf(pdf_path)

    #text = pdf_miner.format_text(text)
    #print(text)
    #print("\n----------------------------------------------------------------\n")
    #print(gemma.get_summarization(text))
    #print(gemma.get_questions(text))



    """
    # PDF pagina per pagina
    text = pdf_miner.format_text_per_page(text)
    print(text[0])
    print("\n----------------------------------------------------------------\n")
    #for page in text:
        #print(gemma.get_summarization(page))
        #print("QUESTIONS:       " + gemma.get_questions(page))


    # QA
    langChain = langChain.Chain_Class()
    langChain.init_chain(text)
    print(langChain.get_answer("What is the LSTM method?"))
    
    """



    """
    pdf_loader = PyPDFLoader(pdf_path)
    pages = pdf_loader.load_and_split()
    print(pages[0].page_content)

    # summerize
    langChain = langChain.Chain_Class(pdf_path)
    print(langChain.get_summarize(pages)['output_text'])
    """



    # web page summarize
    Model_Class = langChain.Model_Class(pdf_path)
    text_array = Model_Class.get_webpage("https://en.wikipedia.org/wiki/Large_language_model")
    for doc in Model_Class.formatted_webpage(text_array):
        print(doc.page_content)

    print("\n----------------------------------------------------------------\n")
    print(Model_Class.get_web_summarize(text_array)['output_text'])

