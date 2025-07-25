# 🏙️ Real Estate Research Tool

A powerful AI-powered research tool designed for real estate professionals and enthusiasts. This application uses Retrieval-Augmented Generation (RAG) to analyze real estate news articles and provide intelligent answers to your questions.

![Real Estate Research Tool](<Resources/image%20(24).png>)

## ✨ Features

- **📰 Multi-URL Processing**: Load and analyze up to 3 news articles simultaneously
- **🤖 AI-Powered Q&A**: Get intelligent answers using Llama-3 via Groq API
- **🔍 Advanced RAG System**: Uses HuggingFace embeddings and ChromaDB for efficient retrieval
- **📊 Source Attribution**: Every answer includes source URLs for transparency
- **🎨 Modern UI**: Clean, intuitive Streamlit interface with real-time feedback
- **⚡ Fast Processing**: Optimized text chunking and vector storage
- **🛡️ Error Handling**: Robust error handling and validation throughout

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key (get one at [groq.com](https://groq.com))

### Installation

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd Exercise_Solution
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   ```

4. **Run the application**

   ```bash
   streamlit run main.py
   ```

5. **Open your browser**

   The app will open at `http://localhost:8501`

## 📖 Usage Guide

### Step 1: Add News Articles

- Use the sidebar to enter up to 3 URLs of real estate news articles
- URLs must start with `http://` or `https://`
- Click "🚀 Process URLs" to begin analysis

### Step 2: Ask Questions

- Once URLs are processed, you can ask questions about the articles
- The AI will search through the content and provide relevant answers
- Sources are automatically cited for transparency

### Example URLs to Try

```
https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html
https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html
https://www.cnbc.com/2024/12/17/wall-street-sees-upside-in-2025-for-these-dividend-paying-real-estate-stocks.html
```

### Example Questions

- "What are the current mortgage rates?"
- "How does the Federal Reserve's policy affect mortgages?"
- "What are the predictions for real estate stocks in 2025?"
- "What factors influence mortgage rate changes?"

## 🏗️ Architecture

### Core Components

1. **Document Loader**: `UnstructuredURLLoader` extracts content from URLs
2. **Text Processing**: `RecursiveCharacterTextSplitter` chunks text optimally
3. **Embeddings**: HuggingFace's `sentence-transformers/all-MiniLM-L6-v2`
4. **Vector Store**: ChromaDB for efficient similarity search
5. **LLM**: Llama-3 via Groq API for answer generation
6. **UI**: Streamlit for the web interface

### File Structure

```
Exercise_Solution/
├── main.py              # Streamlit web application
├── rag.py               # Core RAG functionality
├── prompt.py            # AI prompt templates
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── test_setup.py        # Setup validation script
```

## ⚙️ Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)
- `GROQ_MODEL`: Model to use (default: `llama-3.3-70b-versatile`)

### Model Settings

- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters
- **Max Tokens**: 500 for responses
- **Temperature**: 0.9 for creativity
- **Retriever K**: 4 documents for context

## 🔧 Customization

### Adding New Models

Edit `config.py` to change model settings:

```python
GROQ_MODEL = "your-preferred-model"
TEMPERATURE = 0.7  # Adjust creativity
MAX_TOKENS = 1000  # Adjust response length
```

### Modifying Prompts

Edit `prompt.py` to customize AI behavior:

```python
# Add domain-specific instructions
updated_template = "You are an expert in [your domain]..."
```

### Changing Embeddings

Update `config.py`:

```python
EMBEDDING_MODEL = "your-preferred-embedding-model"
```

## 🐛 Troubleshooting

### Common Issues

1. **"GROQ_API_KEY environment variable is required"**

   - Ensure your `.env` file exists and contains the API key
   - Check that the key is valid and has sufficient credits

2. **"Error loading data from URLs"**

   - Verify URLs are accessible and contain text content
   - Some sites may block automated access

3. **"Vector database is not initialized"**

   - Process URLs first before asking questions
   - Check that the Resources/vectorstore directory exists

4. **Slow processing**
   - Large articles may take time to process
   - Consider using fewer URLs or shorter articles

### Performance Tips

- Use articles with clear, structured content
- Limit to 2-3 URLs for faster processing
- Ensure stable internet connection for URL loading

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/) and [Llama-3](https://llama.meta.com/)
- Uses [LangChain](https://langchain.com/) for RAG implementation
- Embeddings from [HuggingFace](https://huggingface.co/)
- Vector storage with [ChromaDB](https://www.trychroma.com/)

---

**Happy researching! 🏠📈**
