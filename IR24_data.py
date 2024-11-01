# Functions for gathering data

import requests
import html2text
import wikipediaapi
from pathlib import Path

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Adapted from: https://github.com/pixegami/langchain-rag-tutorial/blob/main/create_database.py
def load_docs(dir):
    loader = DirectoryLoader(dir, glob="*.md")
    documents = loader.load()
    return documents

# Adapted from: https://github.com/pixegami/langchain-rag-tutorial/blob/main/create_database.py
def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks

# Function to convert HTML to Markdown and save to a file
converter = html2text.HTML2Text()
def html_to_markdown(url, output_file):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Convert the HTML content to Markdown
    markdown_content = converter.handle(html_content)

    # Write the Markdown content to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f'Markdown content saved to {output_file}')



# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('IR24 (henrik.bongers@t-online.de)','en')
def wiki_to_text(article, output_file):
    # Get the Wikipedia page
    page = wiki_wiki.page(article)

    if page.exists():
        html_content = page.text

        # Convert HTML to Markdown
        markdown_content = converter.handle(html_content)

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        print(article + '\'s content saved successfully!')
    else:
        print("Article " + article + " not found!")


# Taken from RetrievalTutorial.
def download_file(url): 
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Write the content to the file
        file_path = url.split("/")[-1]
        if not Path(file_path).exists():
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        print(f"File downloaded successfully: {file_path}")
        return file_path

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        raise
    except IOError as e:
        print(f"Error saving file: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise



