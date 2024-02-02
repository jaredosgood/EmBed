import fitz
import pandas as pd
# import polars as pl

def extract_text_to_csv(pdf_path, csv_path, additional_columns=None):
    """
    Extracts text from each page of a PDF and saves it to a CSV file.

    Parameters:
    - pdf_path: Path to the PDF file to be processed
    - csv_path: Path where the CSV file will be saved
    - additional_columns: A dictionary where keys are column names and values are lists
                          containing the values for these columns. The length of each
                          list should match the number of pages in the PDF.
    """
    doc = fitz.open(pdf_path)  # Open the document.
    data = {"index": [],
            "id": [],
            "page_number": [],
            "page_contents": []}

    # Add additional columns if provided
    if additional_columns:
        for col in additional_columns:
            data[col] = additional_columns[col]

    for i, page in enumerate(doc, start=1):
        text = page.get_text().encode("utf8").decode("utf8")
        data["page_number"].append(i)
        data["page_contents"].append(text)

        # If additional columns are provided but not for this page, add a default value.
        if additional_columns:
            for col in additional_columns:
                if len(data[col]) < i:  # Assuming missing data implies len(column) < current page number
                    data[col].append('')  # Default value for missing data

    # Create a DataFrame
    df = pd.DataFrame(data)
    # For Polars, use the following line instead of the above one.
    # df = pl.DataFrame(data)

    # Save to a CSV file
    df.to_csv(csv_path, index=False)

# Example Usage
pdf_path = "/path/to/your/document.pdf"
csv_path = "/path/to/save/document.csv"
additional_columns = {
    "author": ["Author Name"] * 5  # Example for adding 5 pages of additional data
}
extract_text_to_csv(pdf_path, csv_path, additional_columns)