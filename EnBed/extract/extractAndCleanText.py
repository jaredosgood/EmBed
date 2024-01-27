import textract

def extract_and_clean_text(pdf_path):
    """
    This function is used to extract and clean the text from a PDF file at the specified path.
    The text is cleaned by removing double spaces, newline and semicolon characters.
    """

    # Extract raw text from PDF using 'pdfminer' method from 'textract' library.
    # This library provides simple method to extract plain text from multiple file types like pdf, word etc.
    # 'decode('utf-8')' is used to ensure proper conversion of extracted characters to human readable format.
    raw_text = textract.process(pdf_path, method='pdfminer').decode('utf-8')

    # Replace double spaces, newline characters and semicolons with single space.
    # This is done to clean up the extracted text and bring it to a standardized format.
    clean_text = raw_text.replace("  ", " ").replace("\n", "; ").replace(';', ' ')

    # Return the cleaned text from the function.
    return clean_text