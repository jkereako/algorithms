def sort(list, lt = lambda x, y: x < y):
    """Returns a new sorted list containing the same elements as L"""
    if len(list) < 2:
        return list[:]

    # Divide and conquer!
    middle = int(len(list)/2)
    left = sort(list[:middle], lt)
    right = sort(list[middle:], lt)

    return merge(left, right, lt)

def merge(left, right, lt):
    """Assumes left and right are sorted lists.
     lt defines an ordering on the elements of the lists.
     Returns a new sorted(by lt) list containing the same elements
     as (left + right) would contain."""
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):
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

