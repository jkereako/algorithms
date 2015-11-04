def binary_search(L, key):
    """
    Chop a L in half, inspect it.
    """

    # The list is empty, hence, the key does not exist.
    if len(L) == 0:
        return False

    # The list only contains 1 element, test if it is the key
    if len(L) == 1:
        return L[0] == key

    # Find the middle key
    mid = len(L) // 2

    # We found the key
    if L[mid] == key:
        return True

    # If the middle element is greater than the key, then search the lower
    # half of L.
    if L[mid] > key:
        return binary_search(L[:mid], key)

    # Otherwise, search the upper half
    return binary_search(L[mid:], key)
