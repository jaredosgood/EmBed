import re

def clean_text(text):
    """
    This function is used for cleaning a given text.
    Remove double spaces, newline and semicolon characters.
    """
    # Replace double spaces with single space.
    # text = text.replace("  ", " ")

    # Replace newline characters with "; ".
    text = text.replace("\n", "; ")

    # Replace more than one space with single space.
    text = re.sub(" +", " ", text)

    # Replace semicolons with single spaces.
    cleaned_text = text.replace(';', ' ')

    return cleaned_text