def split_text(text, max_length=400):

    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:

        current_chunk.append(word)

        if len(current_chunk) >= max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks