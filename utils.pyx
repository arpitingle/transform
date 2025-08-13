def normalize_and_join(list input_texts):
    """
    Cython implementation: takes a list of strings, lowercases, strips, 
    collapses whitespace, joins into one string
    """
    cdef int i, n = len(input_texts)
    cdef list output_parts = []
    cdef str part
    
    for i in range(n):
        part = input_texts[i]
        if part:
            # Normalize: lowercase, strip, collapse whitespace
            normalized_part = " ".join(part.lower().strip().split())
            output_parts.append(normalized_part)
    
    return " ".join(output_parts)