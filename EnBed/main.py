from processText import processChunks as pc
from extract import extractAndCleanText as ect
from processText import splitWithOverlap as swo
from export import writeFileTXT as wf

import os

PDF_PATH = '/your/pdf/path.pdf'
API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    clean_text = ect(PDF_PATH)
    chunks_dict = swo(clean_text, 40, 2400)
    processed_text = pc(chunks_dict, API_KEY)
    wf(processed_text)
    return


if __name__ == '__main__':
    main()