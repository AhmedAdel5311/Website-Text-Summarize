import streamlit as st
import validators
from langchain_community.document_loaders import UnstructuredURLLoader
from model import summarize_content

st.set_page_config(page_title="Website Summarizer", page_icon="🌐")
st.title("🌐 Website Text Summarizer")
st.subheader("Enter a website URL to summarize")

# Input field for website URL only
generic_url = st.text_input("Website URL", label_visibility="visible")

if st.button("Summarize Website"):
    if not generic_url.strip():
        st.error("Please enter a website URL.")
    elif not validators.url(generic_url):
        st.error("Invalid URL. Please enter a valid website URL.")
    else:
        try:
            with st.spinner("Fetching and summarizing content..."):
                loader = UnstructuredURLLoader(
                    urls=[generic_url],
                    ssl_verify=False,
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                docs = loader.load()
                summary = summarize_content(docs)
                st.success(summary)
        except Exception as e:
            st.exception(f"An error occurred: {e}")
