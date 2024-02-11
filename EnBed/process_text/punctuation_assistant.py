import os
import openai
from EnBed.logging_config import setup_logging
import logging



setup_logging()
logger = logging.getLogger('EnBed.process_text.punctuation_assistant')
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
def punctuation_assistant(raw_text):

    system_prompt = """You are a helpful assistant that corrects text and code extracted from a textbook.
    You have the following tasks:
    (1) Remove misplaced spaces within words. For example, the word "soft ware" should be "software".
    (2) Replace double or triple spaces with single spaces. For example, "off  the" should be "off the".
    (3) Alter line endings so that each paragraph is on the same line. For example, 
        "This is the first sentence.\nThis is the second sentence." should be "This is the first sentence. This is the second sentence."
    (4) Preserve the original words.
    (5) Insert a single backtick, "`", before and after to format a small piece of code within a line of text.
    (6) Insert triple backticks for long single-line snippets of code and all multi-line code blocks.
    (7) Preserve page numbers and format them as '\n<<<Page {#}>>>\n'.
    (8) Use only the context provided."""
    response = client.chat.completions.create(
        # model="gpt-4",
        model="gpt-4-0125-preview",
        # model="gpt-3.5-turbo-0125",
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
    string_response = str(response.choices[0].message.content)
    logger.info(f"Response from 'punctuation_assistant': " + (string_response[:1000]))
    return string_response
