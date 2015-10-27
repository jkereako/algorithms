def binary_search(list, element, low, high):
    """
    Chop a list in half, inspect it.
    """

    # Account for cases in which the list is 0 or 1 element
    if high - low < 2:
        return list[low] == element or list[high] == element

    # Find the middle element
    mid = low + (high - low) // 2

    # We found the element
    if list[mid] == element:
        return True

    # If the middle element is greater than the subject, then search the lower
    # half of the list.
    if list[mid] > element:
        return binary_search(list, element, low, mid - 1)

    # Otherwise, search the upper half
    return binary_search(list, element, mid + 1, high)
