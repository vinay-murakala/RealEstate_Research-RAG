import streamlit as st
from rag import process_urls, generate_answer
import re

# Page configuration
st.set_page_config(
    page_title="Real Estate Research Tool",
    page_icon="🏙️",
    layout="wide"
)

st.title("🏙️ Real Estate Research Tool")
st.markdown("Ask questions about real estate news articles and get AI-powered answers!")

# Sidebar for URL inputs
with st.sidebar:
    st.header("📰 Add News Articles")
    st.markdown("Enter up to 3 URLs to analyze:")
    
    url1 = st.text_input("URL 1", placeholder="https://example.com/article1")
    url2 = st.text_input("URL 2", placeholder="https://example.com/article2")
    url3 = st.text_input("URL 3", placeholder="https://example.com/article3")
    
    # URL validation
    def is_valid_url(url):
        if not url:
            return False
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url_pattern.match(url) is not None
    
    urls = [url for url in (url1, url2, url3) if url.strip()]
    valid_urls = [url for url in urls if is_valid_url(url)]
    
    if urls and not valid_urls:
        st.error("Please enter valid URLs starting with http:// or https://")
    
    process_url_button = st.button("🚀 Process URLs", type="primary")
    
    if process_url_button:
        if not valid_urls:
            st.error("Please provide at least one valid URL")
        else:
            st.info(f"Processing {len(valid_urls)} URL(s)...")
            
            # Create a progress container
            progress_container = st.container()
            with progress_container:
                for status in process_urls(valid_urls):
                    st.text(status)
                    st.rerun()  # Refresh to show progress
            
            st.success("✅ URLs processed successfully!")
            st.session_state.urls_processed = True

# Main content area
if 'urls_processed' not in st.session_state:
    st.session_state.urls_processed = False

if st.session_state.urls_processed:
    st.header("❓ Ask Questions")
    
    # Query input
    query = st.text_input(
        "Enter your question about the articles:",
        placeholder="What are the current mortgage rates?",
        key="query_input"
    )
    
    if query:
        try:
            with st.spinner("🤔 Generating answer..."):
                answer, sources = generate_answer(query)
            
            # Display answer
            st.header("💡 Answer:")
            st.write(answer)
            
            # Display sources
            if sources:
                st.subheader("📚 Sources:")
                for i, source in enumerate(sources, 1):
                    st.markdown(f"{i}. {source}")
                    
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            if "not initialized" in str(e).lower():
                st.info("💡 Please process URLs first using the sidebar")
else:
    st.info("👈 Use the sidebar to add URLs and start analyzing articles!")
    
    # Example section
    with st.expander("📖 Example URLs"):
        st.markdown("""
        Try these example URLs:
        - https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html
        - https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html
        - https://www.cnbc.com/2024/12/17/wall-street-sees-upside-in-2025-for-these-dividend-paying-real-estate-stocks.html
        """)
    
    # Example questions
    with st.expander("💭 Example Questions"):
        st.markdown("""
        Once you've processed URLs, try asking:
        - What are the current mortgage rates?
        - How does the Federal Reserve's policy affect mortgages?
        - What are the predictions for real estate stocks in 2025?
        - What factors influence mortgage rate changes?
        """)
