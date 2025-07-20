from uuid import uuid4
from config import (
    GROQ_API_KEY, GROQ_MODEL, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP,
    VECTORSTORE_DIR, COLLECTION_NAME, MAX_TOKENS, TEMPERATURE,
    MAX_TOKENS_LIMIT, RETRIEVER_K, validate_config
)
from prompt import PROMPT, EXAMPLE_PROMPT
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

llm = None
vector_store = None


def initialize_components():
    global llm, vector_store

    # Validate configuration
    validate_config()

    if llm is None:
        llm = ChatGroq(
            model=GROQ_MODEL, 
            temperature=TEMPERATURE, 
            max_tokens=MAX_TOKENS,
            groq_api_key=GROQ_API_KEY
        )

    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=ef,
            persist_directory=str(VECTORSTORE_DIR)
        )


def process_urls(urls):
    """
    This function scraps data from a url and stores it in a vector db
    :param urls: input urls
    :return: generator yielding status messages
    """
    if not urls:
        yield "No URLs provided"
        return
        
    yield "Initializing Components"
    try:
        initialize_components()
    except Exception as e:
        yield f"Error initializing components: {str(e)}"
        return

    yield "Resetting vector store...✅"
    try:
        vector_store.reset_collection()
    except Exception as e:
        yield f"Error resetting vector store: {str(e)}"
        return

    yield "Loading data...✅"
    try:
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()
        
        if not data:
            yield "No data could be loaded from the provided URLs"
            return
            
    except Exception as e:
        yield f"Error loading data from URLs: {str(e)}"
        return

    yield "Splitting text into chunks...✅"
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", " "],
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP  # Add overlap for better context
        )
        docs = text_splitter.split_documents(data)
        
        if not docs:
            yield "No documents created after text splitting"
            return
            
    except Exception as e:
        yield f"Error splitting text: {str(e)}"
        return

    yield "Add chunks to vector database...✅"
    try:
        uuids = [str(uuid4()) for _ in range(len(docs))]
        vector_store.add_documents(docs, ids=uuids)
    except Exception as e:
        yield f"Error adding documents to vector store: {str(e)}"
        return

    yield f"Done adding {len(docs)} documents to vector database...✅"

def generate_answer(query):
    """
    Generate an answer for the given query using the RAG system
    :param query: The question to answer
    :return: tuple of (answer, sources)
    """
    if not query or not query.strip():
        raise ValueError("Query cannot be empty")
        
    if not vector_store:
        raise RuntimeError("Vector database is not initialized. Please process URLs first.")
    
    try:
        qa_chain = load_qa_with_sources_chain(
            llm, 
            chain_type="stuff",
            prompt=PROMPT,
            document_prompt=EXAMPLE_PROMPT
        )
        chain = RetrievalQAWithSourcesChain(
            combine_documents_chain=qa_chain, 
            retriever=vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K}),
            reduce_k_below_max_tokens=True, 
            max_tokens_limit=MAX_TOKENS_LIMIT,
            return_source_documents=True
        )
        result = chain.invoke({"question": query}, return_only_outputs=True)
        sources_docs = [doc.metadata['source'] for doc in result['source_documents']]

        return result['answer'], sources_docs
    except Exception as e:
        raise RuntimeError(f"Error generating answer: {str(e)}")


if __name__ == "__main__":
    urls = [
        "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
        "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
    ]

    process_urls(urls)
    answer, sources = generate_answer("Tell me what was the 30 year fixed mortagate rate along with the date?")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")