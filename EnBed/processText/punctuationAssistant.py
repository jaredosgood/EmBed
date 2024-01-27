import os
import openai

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
def punctuation_assistant(punctuated_transcripts):

    system_prompt = """You are a helpful assistant that adds punctuation to text and code in a textbook.
    Preserve the original words and only insert necessary punctuation such as periods, commas, capialization,
    symbols like dollar sings or percentage signs, backtick to format a small piece of code within a line of text,
    triple backticks for larger snippets of code that should be displayed as a separate block, and formatting
    consistent with the constraints of a '.txt' file. Preserve page numbers and format them as '<<<Page {#}>>>\n'.
    Remove unnecessary spacing, given that this information will be embedded and stored in a vector database.
    Use only the context provided. If there is no context provided say, 'No context provided'\n"""
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
                "content": punctuated_transcripts
            }
        ]
    )
    return response