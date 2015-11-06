def sort(L, compare = lambda x, y: x < y):
    """
    Mergesort is a famous example of a divide and conquer algorithm invented in
    1945. It divides a list into 2 parts, sorts each part individually and then
    merges the 2 lists.

    Performance
    ===========
    Worst:      O(n log n)
    Avereage:   O(n log n)
    Best:       O(n log n)
    """

    # If L is fewer than 2 elements, then return a copy of the list
    if len(L) < 2:
        return list(L)

    # Divide and conquer!
    mid = len(L) // 2
    left = sort(L[:mid], compare)
    right = sort(L[mid:], compare)

    return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i,j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1

    return result

