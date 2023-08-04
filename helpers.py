
import PyPDF2
import tiktoken

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pages = pdf_reader.pages

        content = []
        for page in pages:
            
            text = page.extract_text()
            content.append(text)

    return '\n'.join(content)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

