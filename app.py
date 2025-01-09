import openai
import fitz  # PyMuPDF to read PDF

# OpenAI API Key
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your API Key

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    text = ""

    # Iterate through each page and extract text
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()

    return text

# Function to get an answer from ChatGPT
def ask_chatgpt(question, context):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Answer the following question based on the context:\n\nContext: {context}\n\nQuestion: {question}\nAnswer:",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Get the answer from the response
    return response.choices[0].text.strip()

# Example usage
def main():
    # Path to the PDF file
    pdf_path = "path_to_your_pdf_file.pdf"
    
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Example Question
    question = "What is the main topic of this document?"

    # Ask ChatGPT based on the extracted PDF text
    answer = ask_chatgpt(question, pdf_text)

    print(f"Question: {question}")
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
