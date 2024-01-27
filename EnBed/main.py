from processText import processChunks as pc
from extract import extractText as ext
from processText import splitWithOverlap as swo
from export import writeFileTXT as wf
from processText import cleanText as clt

import os

PDF_PATH = '/Users/jdo/Library/CloudStorage/OneDrive-Personal/ASU Courses/CSE 230/Computer Organization and Design.pdf'
API_KEY = os.environ.get("OPENAI_API_KEY")
OUTPUT_FILE_PATH = '/Users/jdo/Downloads/Computer Organization and Design.txt'

def main():
    text = clt(ext(PDF_PATH))
    print(text[0:10000])
    chunks_dict = swo(text, 40, 2400)
    processed_text = pc(chunks_dict, API_KEY)
    wf(OUTPUT_FILE_PATH = processed_text)
    print(processed_text[0:10000])
    print(f"File written to {OUTPUT_FILE_PATH}")
    print(f"Number of chunks: {len(chunks_dict)}")
    return


if __name__ == '__main__':
    main()