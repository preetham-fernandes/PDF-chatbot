## Overview
This project implements a response retrieval chat interface that retrieves answers from a knowledge base consisting of PDFs. The system processes and indexes the documents, allowing users to query them through a chatbot interface. The chatbot leverages natural language processing (NLP) and vector search to find the most relevant responses.

## Technical Architecture
The system consists of the following components:

1. User Interface (Frontend):
   - A web-based chat interface built using *Streamlit*.
   - Allows users to enter queries and view responses.
   
2. Backend Processing:
   - Manages query processing and response retrieval.
   - Uses the *Gemini API* for response generation and refinement.

3. Document Processing Pipeline:
   - Converts PDFs into text using PyMuPDF.
   - Chunking and embedding generation using LangChain.
   - Stores processed embeddings in memory for quick retrieval.
   
4. Response Retrieval:
   - Uses LangChain for semantic search and retrieval.
   - Finds the closest matching responses based on user queries.
   
5. Knowledge Base:
   - PDFs are processed on-demand with no persistent storage.
   
6. LLM-based Augmentation:
   - Uses the *Gemini API* to refine or re-rank responses before sending them to the user.
![WhatsApp Image 2025-02-24 at 11 17 02 PM](https://github.com/user-attachments/assets/90f6f2d6-9ffb-4b18-949f-dc157449f3f5)
   
## Information Flow
1. User submits a query through the Streamlit interface.
2. Backend converts the query into an embedding vector.
3. LangChain searches for relevant document chunks.
4. Top-ranked document excerpts are retrieved and optionally refined by the Gemini API.
5. The response is sent back to the frontend for display.
6. Users can provide feedback to improve retrieval accuracy.

## Tech Stack
### Frontend:
- Streamlit

### Backend:
- Python
- LangChain for query processing
- Gemini API for response generation

### Data Processing:
- PyMuPDF (PDF Parsing)
- SentenceTransformers for embeddings
- LangChain for retrieval

### Storage:
- No persistent storage; embeddings are kept in memory

## Example Query & Response
### Input:
> "What are the key safety regulations mentioned in the compliance document?"

### Process:
- The query is embedded and searched in memory.
- The top-matching document excerpts are retrieved.
- The Gemini API summarizes and refines the response.

### Output:
> "The compliance document outlines key safety regulations including proper equipment handling, mandatory training sessions, and emergency response procedures. Employees must adhere to these protocols to ensure workplace safety."

## How to Run Locally
1. Clone the repository:
   sh
   git clone [https://github.com/yourusername/response-retrieval-chat.git](https://github.com/Saakshi0508k/PDF-chatApp.git)
   cd response-retrieval-chat
   
   
2. Install dependencies:
   sh
   pip install -r requirements.txt
   
   
3. Set up the environment variable for the Gemini API key:
   sh
   export GEMINI_API_KEY=your_api_key_here
   

4. Start the application:
   sh
   streamlit run chatpdf1.py
   

5. Access the chat interface at [http://localhost:8501](http://localhost:8501)

## Future Enhancements
- Support for multi-document summarization.
- RAG (Retrieval-Augmented Generation) improvements.
- User feedback loop for better ranking.
- Role-based access control for document visibility.

## License
MIT License

---
Feel free to contribute by opening issues or pull requests!
