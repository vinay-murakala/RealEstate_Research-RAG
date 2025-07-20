#!/usr/bin/env python3
"""
Test script to validate the Real Estate Research Tool setup
"""
import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import streamlit
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        from langchain_groq import ChatGroq
        print("✅ LangChain Groq imported successfully")
    except ImportError as e:
        print(f"❌ LangChain Groq import failed: {e}")
        return False
    
    try:
        from langchain_huggingface.embeddings import HuggingFaceEmbeddings
        print("✅ HuggingFace embeddings imported successfully")
    except ImportError as e:
        print(f"❌ HuggingFace embeddings import failed: {e}")
        return False
    
    try:
        from langchain_chroma import Chroma
        print("✅ ChromaDB imported successfully")
    except ImportError as e:
        print(f"❌ ChromaDB import failed: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading"""
    print("\n🔧 Testing configuration...")
    
    try:
        from config import validate_config, GROQ_API_KEY
        print("✅ Configuration module imported successfully")
        
        if GROQ_API_KEY:
            print("✅ GROQ_API_KEY found in environment")
        else:
            print("⚠️  GROQ_API_KEY not found - you'll need to set it in .env file")
            
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False
    
    return True

def test_directories():
    """Test if required directories exist"""
    print("\n📁 Testing directories...")
    
    base_dir = Path(__file__).parent
    resources_dir = base_dir / "Resources"
    vectorstore_dir = resources_dir / "vectorstore"
    
    if resources_dir.exists():
        print("✅ Resources directory exists")
    else:
        print("⚠️  Resources directory doesn't exist - will be created automatically")
    
    if vectorstore_dir.exists():
        print("✅ Vectorstore directory exists")
    else:
        print("⚠️  Vectorstore directory doesn't exist - will be created automatically")
    
    return True

def test_modules():
    """Test if project modules can be imported"""
    print("\n📦 Testing project modules...")
    
    try:
        from rag import process_urls, generate_answer
        print("✅ RAG module imported successfully")
    except Exception as e:
        print(f"❌ RAG module import failed: {e}")
        return False
    
    try:
        from prompt import PROMPT, EXAMPLE_PROMPT
        print("✅ Prompt module imported successfully")
    except Exception as e:
        print(f"❌ Prompt module import failed: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("🚀 Real Estate Research Tool - Setup Validation")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_directories,
        test_modules
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Create a .env file with your GROQ_API_KEY")
        print("2. Run: streamlit run main.py")
        print("3. Open your browser to http://localhost:8501")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\nTroubleshooting:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Check your Python version (3.8+ required)")
        print("3. Ensure all files are in the correct locations")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 