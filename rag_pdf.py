from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# LOAD FILE AND TAKE THE TEXTS FTOM THE FILE
loader = PyPDFLoader(r"C:\Users\Yahya\Downloads\RAG PDF\data\swiss_faq.pdf")
docs = loader.load()
texts = [page.page_content for page in docs]
full_text = "\n".join(texts)

# SPLIT TEXT BEING CHUNK
text_splitter = RecursiveCharacterTextSplitter(
  chunk_size = 1024,
  chunk_overlap = 200
)

chunks = text_splitter.split_text(full_text)

# EMBEDDING MODEL
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# INTEGRATION WITH VECTOR DATABASE
vector_store = FAISS.from_texts(chunks, embedding_model)
path_vector = r"C:\Users\Yahya\Downloads\RAG PDF\vector_store"
vector_store.save_local(path_vector)

# INTEGRATION LLM MODEL WITH VECTOR DATABASE
base_url="http://127.0.0.1:1234/v1"
api_key="lm-studio"
MODEL = "phi-3-mini-4k-instruct"

LLM = ChatOpenAI(
  openai_api_base = base_url,
  openai_api_key = api_key,
  model_name = MODEL,
  streaming = True
)

messages = [
  SystemMessage(content = "You will receive a user's query and possible content where the answer might be. If the answer is found, provide it, if not, state that the answer does not exist.")
]

# INTEGRATION QUERY WITH VECTOR DATABASE
vector_database = FAISS.load_local(path_vector, embedding_model, allow_dangerous_deserialization=True )

def retrieve_context(query):
    """Cari teks yang relevan dari FAISS berdasarkan query."""
    results = vector_database.similarity_search(query, k=5)
    context = "\n\n".join([doc.page_content for doc in results])
    return context
  
# TEST CHATBOT RAG

def main():
  while True:
    user_input = input("> ")
    print()

    if user_input in ["exit", "bye", "quit"]:
      break

    context = retrieve_context(user_input)
    
    print(f"CONTEXT : {context}")
    print()

    prompt = (
      f"Context = {context}\n\n"
      f"User Question = {user_input}\n\n"
    )

    messages.append(HumanMessage(content=prompt))

    response = LLM.stream(messages)
    history_chat = ""

    for chunk in response:
      print(chunk.content, end="", flush=True)
      history_chat += chunk.content

    messages.append(AIMessage(content=history_chat))

    print("\n")
    
if __name__ == "__main__":
  main()