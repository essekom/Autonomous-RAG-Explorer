from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader

class RAGEngine:
    def __init__(self, openai_api_key):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)

    def process_document(self, file_path):
        """Load and index a PDF document."""
        loader = PyPDFLoader(file_path)
        documents = loader.load_and_split()
        self.vector_db = Chroma.from_documents(documents, self.embeddings)
        
    def query(self, question):
        """Query the document using RAG."""
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever()
        )
        return qa_chain.run(question)

if __name__ == "__main__":
    # Example usage
    # engine = RAGEngine(api_key="your-key")
    # engine.process_document("data.pdf")
    # print(engine.query("What is the main topic?"))
    print("RAG Engine Initialized. Ready for document processing.")
