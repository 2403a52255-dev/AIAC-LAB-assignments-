def normalize(scores):
    """
    Normalizes a list of numerical scores to the range [0, 1].

    Args:
        scores (list): List of numerical values to normalize.

    Returns:
        list: List of normalized values. Returns an empty list if input is empty.
              If all values are the same, returns a list of zeroes.
    """
    if not scores:
        return []
    m = max(scores)
    n = min(scores)
    if m == n:
        return [0 for _ in scores]
    return [(x - n) / (m - n) for x in scores]
print(normalize([ ])) # Example usage
print(normalize([10,20,30])) # Example usage
print(normalize([1,1,1,1 ])) # Example usage