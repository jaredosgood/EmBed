

def split_with_overlap(text_tokens, num_chunks, overlap):
    """
    Splits the text tokens into specified number of chunks with specified overlap with adjacent chunks
    and assigns each chunk to a key in a dictionary that mimics the variable name 'chunk_##'.

    :param text_tokens: List of tokens to be split
    :param num_chunks: Number of chunks to split into
    :param overlap: Number of tokens each chunk needs to overlap with adjacent chunks
    :return: Dictionary with keys as 'chunk_##' and values as chunks (each chunk is a list of tokens)
    """
    total_length = len(text_tokens)
    # base_chunk_size = total_length // num_chunks
    overlap_total = (num_chunks - 1) * overlap * 2  # Overlap for both sides for all but first and last chunk
    adjusted_chunk_size_with_overlap = (total_length + overlap_total) // num_chunks

    # The first and last chunk are adjusted by removing one overlap because they only overlap on one side
    first_last_chunk_size = adjusted_chunk_size_with_overlap - overlap

    chunks_dict = {}
    start_index = 0

    for i in range(num_chunks):
        chunk_name = 'chunk_{:02}'.format(i + 1)  # Formatting chunk name with two-digit index

        if i == 0:  # First chunk
            end_index = start_index + first_last_chunk_size
        elif i == num_chunks - 1:  # Last chunk
            start_index -= overlap  # Adjust for overlap
            end_index = total_length
        else:
            start_index -= overlap  # Adjust for overlap
            end_index = start_index + adjusted_chunk_size_with_overlap

        chunks_dict[chunk_name] = text_tokens[start_index:end_index]

        start_index = end_index  # Set start for next chunk

    return chunks_dict
