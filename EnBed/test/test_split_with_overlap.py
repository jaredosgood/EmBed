from EnBed.processText.split_with_overlap import split_with_overlap
from EnBed.logging_config import setup_logging
import logging
import os

OUTPUT_FILE_PATH = "/Users/jdo/Downloads/EnBed/Test"
setup_logging()
logger = logging.getLogger('my_application')


def test_split_with_overlap():
    print("Testing split_with_overlap method...")
    with open('/Users/jdo/EnBed/EnBed/test/ipsum_01.txt', 'r') as file:
        text_01 = file.read()
        logger.info(f"Text 01: {text_01}")
    with open('/Users/jdo/EnBed/EnBed/test/ipsum_02.txt', 'r') as file:
        text_02 = file.read()
        logger.info(f"Text 02: {text_02}")
    with open('/Users/jdo/EnBed/EnBed/test/ipsum_03.txt', 'r') as file:
        text_03 = file.read()
        logger.info(f"Text 03: {text_03}")
    with open('/Users/jdo/EnBed/EnBed/test/ipsum_04.txt', 'r') as file:
        text_04 = file.read()
        logger.info(f"Text 04: {text_04}")
    with open('/Users/jdo/EnBed/EnBed/test/ipsum_05.txt', 'r') as file:
        text_05 = file.read()
        logger.info(f"Text 05: {text_05}")
    appended_ipsum = text_01 + text_02 + text_03 + text_04 + text_05
    try:
        chunked_ipsum = split_with_overlap(appended_ipsum, 10, 200)
        logging.info(f"Result: {chunked_ipsum}")
    except Exception as e:
        logging.error(f"Error: {e}")
        return
    i = 1
    chunk_array = []
    for chunk in chunked_ipsum:
        try:
            if not os.path.isdir(OUTPUT_FILE_PATH):
                os.makedirs(OUTPUT_FILE_PATH)
                logger.info(f"Directory {OUTPUT_FILE_PATH} was created.")
            with open(f'{OUTPUT_FILE_PATH}/chunk_{i:02}.txt', 'w') as file:
                file.write(chunked_ipsum[chunk])
                logger.info(f"Chunk {i} written to file.")
                i = i + 1
                logger.info(f"{i} has been iterated.")
                chunk_array.append(chunked_ipsum[chunk])
                logger.info(f"Chunk {i}: {chunked_ipsum[chunk]}")
        except:
            with open(f'{OUTPUT_FILE_PATH}/chunk_{i:02}.txt', 'w') as file:
                file.write(chunked_ipsum[chunk])
                logger.info(f"Chunk {i} written to file.")
                i = i + 1
                logger.info(f"{i} has been iterated.")
                chunk_array.append(chunked_ipsum[chunk])
                logger.info(f"Chunk {i}: {chunked_ipsum[chunk]}")
    return chunk_array


test_split_with_overlap()
