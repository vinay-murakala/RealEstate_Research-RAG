from langchain.prompts import PromptTemplate
from langchain.chains.qa_with_sources.stuff_prompt import template

# Enhanced prompt for real estate research
updated_template = """You are an expert real estate research assistant with deep knowledge of market trends, mortgage rates, property values, and real estate investment strategies.

Your task is to provide accurate, well-researched answers based on the provided real estate news articles and documents. Always:
1. Base your answers on the provided sources
2. Be specific with numbers, dates, and facts when available
3. Provide context and explanations for real estate concepts
4. If information is not available in the sources, clearly state that
5. Use professional real estate terminology appropriately

{template}"""

PROMPT = PromptTemplate(template=updated_template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)