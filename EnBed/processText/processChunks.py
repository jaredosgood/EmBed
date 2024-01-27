from .punctuationAssistant import punctuation_assistant
def process_chunks(chunks_dict, api_key):
    appended_chunks = ""
    for _, chunk_text in chunks_dict.items():
        processed_text = punctuation_assistant(chunk_text, api_key)
        appended_chunks += processed_text
    return appended_chunks