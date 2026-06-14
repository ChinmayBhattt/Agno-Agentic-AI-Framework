# Agno-Agentic-AI-Framework

An Agentic AI framework built using Agno, Gemini, LanceDB, and Streamlit to create intelligent AI agents with memory, search capabilities, document processing, and real-time data access.

## Features

* Agentic AI workflows powered by Agno
* Gemini LLM integration
* Web search using DuckDuckGo
* PDF document processing
* Vector database support with LanceDB
* Interactive Streamlit interface
* Financial data retrieval with Yahoo Finance
* Data analysis using Pandas
* Fast full-text search with Tantivy

## Tech Stack

* Python
* Agno
* Gemini
* LanceDB
* Streamlit
* Pandas
* DuckDuckGo Search
* PyPDF
* Tantivy
* Yahoo Finance

## Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/Agno-Agentic-AI-Framework.git
cd Agno-Agentic-AI-Framework
```

### Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

## Run the Application

```bash
streamlit run app.py
```

## Project Structure

```text
Agno-Agentic-AI-Framework/
├── app.py
├── requirements.txt
├── .env
├── README.md
├── data/
├── agents/
├── knowledge/
└── vector_db/
```

## Requirements

* Python 3.12+
* Gemini API Key

## License

MIT License

## Author

Chinmay Bhatt
Hacker's Unity
