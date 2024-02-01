import re
from EnBed.logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger('my_application')


def clean_text(text):
    """
    Enhanced function to clean and format text extracted from a PDF file.
    1. Normalize whitespace.
    2. Correct punctuation spacing.
    3. Replace or remove problematic characters.
    4. (Optional) Correct common OCR text extraction errors.
    """

    # Convert multiple whitespace (excluding newlines and tabs) to a single space for inline text.
    text_single_space = re.sub(r"[^\S\n\t]+", " ", text)
    logger.debug(f"Text with single space: {text_single_space}[:1000]")
    text_newline = re.sub(r"\n+", "\n", text_single_space)      # Normalize multiple newlines to a single newline if needed.
    logger.debug(f"Text with single newline: {text_newline}[:1000]")
    text_tab = re.sub(r"\t+", " ", text_newline)                # Replace tabs with spaces.
    logger.debug(f"Text with single tab: {text_tab}[:1000]")
    text_punct = re.sub(r" +([.,;:!?])", r"\1", text_tab)       # Remove spaces before punctuation.
    logger.debug(f"Text with punctuation: {text_punct}[:1000]")

    # Remove or replace problematic characters (e.g., ligatures, non-standard quotes)
    replacements = {
        # Replace common ligatures
        'ﬀ': 'ff',
        'ﬁ': 'fi',
        'ﬂ': 'fl',
        'ﬃ': 'ffi',
        'ﬄ': 'ffl',
        '‘': "'",
        '’': "'",
        '“': '"',
        '”': '"',
        '\xa0': ' ',
        # More replacements can be added
    }

    for old, new in replacements.items():
        text_replacements_new = text_punct.replace(old, new)
        logger.debug(f"Text with replacements: {text_replacements_new}[:1000]")

    # # Correct common OCR errors (example placeholders, adjust based on actual observation)
    # ocr_corrections = {
    #     'l0ve': 'love',  # Example: OCR misreading 'love' as 'l0ve'
    #     'h0use': 'house',  # Example: OCR misreading 'house' as 'h0use'
    #     # Add more based on observed OCR errors
    # }
    #
    # for old, new in ocr_corrections.items():
    #     text = re.sub(old, new, text)

    # Remove leading and trailing spaces
    text_final = text_replacements_new.strip()
    logger.debug(f"Final text: {text_final}[:1000]")

    return text_final