from populate_database import load_documents
import spacy 
from populate_database import split_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    filtered_text = ' '.join([word for word in text.split() if word.lower() not in stop_words])
    return filtered_text


DATA_PATH = "data"
data = load_documents()

print(data[0])







