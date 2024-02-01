import fitz
import pandas as pd

def get_text_from_page(doc, start_idx, end_idx):
    """
    Helper function to extract texts from a range of pages.

    Parameters:
    - doc: The opened PDF document (PyMuPDF document object).
    - start_idx: The starting index (0-based inclusive).
    - end_idx: The ending index (non-inclusive).

    Returns:
    - A concatenated string of texts from the specified range of pages.
    """
    text_from_page = ""
    for i in range(start_idx, min(end_idx, len(doc))):

        page = doc.load_page(i)
        text_from_page += page.get_text().encode("utf8").decode("utf8") + "\f"
    return text_from_page

def pdf_to_df(pdf_path):
    """
    Function to load a PDF, extract text from each page with overlapping, and save into a DataFrame.

    Parameters:
    - pdf_path: Path to the PDF file to be processed.

    Returns:
    - A DataFrame containing the extracted text and associated pages information.
    """
    # Open the PDF document
    with fitz.open(pdf_path) as doc:
        entries = []

        # Iterate through the document, overlapping as described
        for i in range(len(doc) - 2):
            # Calculate page range for extraction (with overlap)
            start_idx = i
            end_idx = i + 3

            # Extract texts
            text = get_text_from_page(doc, start_idx, end_idx)

            # Determine target_page and page_range
            target_page = start_idx + 1
            page_range = f"{start_idx},{target_page},{end_idx - 1}"

            # Append to entries
            entries.append({"target_page": target_page, "page_range": page_range, "text": text})

        # Creating DataFrame
        df = pd.DataFrame(entries)

        # Assigning column names
        df.columns = ["target_page", "page_range", "text"]

    return df

# Example usage
pdf_path = "/Users/jdo/Library/CloudStorage/OneDrive-Personal/ASU Courses/CSE 240/Syllabus - CSE 240.pdf"
df = pdf_to_df(pdf_path)
print(df.head())