# Autonomous-RAG-Explorer ðŸ¤–ðŸ“–

[![LangChain](https://img.shields.io/badge/Framework-LangChain-blue.svg)](https://github.com/langchain-ai/langchain)
[![OpenAI](https://img.shields.io/badge/AI-GPT--4-orange.svg)](https://openai.com/)
[![VectorDB](https://img.shields.io/badge/Database-ChromaDB-lightgrey.svg)](https://www.trychroma.com/)

A powerful **Retrieval-Augmented Generation (RAG)** system that allows you to have intelligent conversations with your documents. Built with **LangChain**, **OpenAI**, and **ChromaDB**.

## ðŸŒŸ Key Features
- **Contextual Awareness:** Uses vector embeddings to retrieve relevant information from your files.
- **Support for PDFs:** Seamlessly ingest and process PDF documents.
- **State-of-the-Art LLMs:** Leverages GPT-4 for accurate and human-like responses.
- **Local Vector Storage:** Uses ChromaDB for efficient document indexing.

## âš™ï¸ How it Works
1. **Load:** Documents are loaded and split into manageable chunks.
2. **Embed:** Text chunks are converted into numerical vectors using OpenAI Embeddings.
3. **Store:** Vectors are stored in a high-performance vector database.
4. **Retrieve:** When a question is asked, the system finds the most relevant chunks.
5. **Generate:** An LLM generates an answer based on the retrieved context.

## ðŸ› ï¸ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/peter160789/Autonomous-RAG-Explorer.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## ðŸš€ Usage
```python
from rag_engine import RAGEngine

engine = RAGEngine(openai_api_key="your-key")
engine.process_document("my_handbook.pdf")
print(engine.query("Explain the security protocol."))
```

---
Developed by [Peter](https://github.com/peter160789)
