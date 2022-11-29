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


def conjunction(x, y):
    """Calculate the conjunction of two conjunctions."""
    # Initialize the result to an empty list
    z = []
    # Iterate over the features in both conjunctions
    for f1, v1 in x:
        for f2, v2 in y:
            # If the feature and value are the same, add it to the result
            if f1 == f2 and v1 == v2:
                z.append((f1, v1))
    return z


def internal_disjunction(v1, v2):
    """Calculate the internal disjunction of two values. For Average"""
    return (v1 + v2) / 2


def lgcg(x, y):
    """Calculate the LGCG of two conjunctions."""
    # Initialize the result to an empty list
    z = []
    # Iterate over the features in both conjunctions
    for f1, v1 in x:
        found_match = False
        for f2, v2 in y:
            # If the feature is present in both conjunctions
            if f1 == f2:
                # Add the internal disjunction of the values to the result
                z.append((f1, internal_disjunction(v1, v2)))
                found_match = True
                break
        if not found_match:
            z.append((f1, v1))
    for f2, v2 in y:
        found_match = False
        for f1, v1 in x:
            if f1 == f2:
                found_match = True
                break
        if not found_match:
            z.append((f2, v2))
    return z
