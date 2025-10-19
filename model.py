import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain

load_dotenv()  # Load GROQ_API_KEY
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

# Define Summary Prompt
prompt_template = """
Provide a clear and concise summary in 300 words of the following website content:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

def summarize_content(docs):
    """Summarize website documents."""
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
    return chain.run(docs)
