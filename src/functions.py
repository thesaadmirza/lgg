def lgg(h, x):
    """Calculate the LGG of two concepts."""
    # Initialize the result to an empty list
    result = []
    # Iterate over the features in both concepts
    for f1, v1 in h:
        for f2, v2 in x:
            # If the feature and value are the same, add it to the result
            if f1 == f2 and v1 == v2:
                result.append((f1, v1))
    return result






