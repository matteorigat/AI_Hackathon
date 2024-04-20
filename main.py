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


# importing required classes
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('pdf/EdTech Challenge.pdf')

# printing number of pages in pdf file
print(len(reader.pages))


for page in reader.pages:
    print(page.extract_text())
    print("-------------------------------------------------------------")