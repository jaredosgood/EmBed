import os
import openai
from EnBed.logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger('my_application')
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
def punctuation_assistant(raw_text):

    system_prompt = """You are a helpful assistant that corrects text and code extracted from a textbook.
    You have the following tasks:
    (1) Remove misplaced spaces within words. For example, the word "soft ware" should be "software".
    (2) Replace double or triple spaces with single spaces. For example, "off  the" should be "off the".
    (3) Alter line endings so that 
    Preserve the original words and only insert necessary punctuation such as periods, commas, capialization,
    symbols like dollar sings or percentage signs, backtick to format a small piece of code within a line of text,
    triple backticks for larger snippets of code that should be displayed as a separate block, and formatting
    consistent with the constraints of a '.txt' file. Preserve page numbers and format them as '\n<<<Page {#}>>>\n'.
    Remove unnecessary spacing, given that this information will be embedded and stored in a vector database.
    Use only the context provided."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": raw_text
            }
        ]
    )
    string_response = str(response)
    logger.info(f"Response from 'punctuation_assistant': {string_response}[:1000]")
    return string_response