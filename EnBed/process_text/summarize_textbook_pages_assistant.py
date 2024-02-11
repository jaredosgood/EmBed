import os
import openai
from EnBed.logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger('EnBed.process_text.punctuation_assistant')
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
def summarize_textbook_pages_assistant(punctuated_text):

    system_prompt = """You are a helpful assistant that summarizes textbook extracts.
    You have the following tasks:
    (1) Think step-by-step.
    (2) Use the context provided to summarize the text.
    (3) Preserve the original words, wording of technical terms, and proper nouns.
    (4) Summarize three pages of textbook content into a single paragraph.
    (5) Give added relevance to the most important information and information on the second of the three pages.
    (6) Remember to include the most important information from the first and third pages.
    (7) Understand that the summary should be coherent and well-structured.
    (8) Remember that the textbooks topic is Algorithm design in Java.
    (8) Examin the text three times before starting to generate the summary."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": punctuated_text
            }
        ]
    )
    summary_response = str(response.choices[0].message.content)
    logger.info(f"Response from 'summarize_textbook_pages_assistant': " + (summary_response[:1000]))
    return summary_response
