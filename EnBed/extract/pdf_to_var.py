import fitz  # PyMuPDF

def pdf_to_var(pdf_path):
    extracted_text = ""  # Initialize empty string to accumulate text from all pages
    with fitz.open(pdf_path) as doc:  # Open and manage the PDF document
        for page in doc:  # Iterate through each page in the document
            text = page.get_text().encode("utf8")  # Extract text from the current page
            extracted_text += text + "\f"  # Concatenate, adding form feed as a delimiter

    return extracted_text

# Example usage:
# pdf_path = "/Users/jdo/Desktop/Computer Organization and Design.pdf"
# entire_document_text = extract_text_from_pdf(pdf_path)
# # You can then print the first 1000 characters to check, or manipulate as needed.
# print(entire_document_text[:100000])