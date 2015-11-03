def sort(L):
    """
    Insertion sort is a O(n^2) algorithm in the worst case which is when the
    array to be sorted is in reverse order. However, the space complexity of
    this algorithm is O(1) because the only auxiliary space required to perform
    an insertion sort is the temporary variable `val`. In other words, insertion
    sort is done "in place".
    """
    # Start from the second element so we can compare the current element with
    # the previous element.
    for i in range(1, len(L)):
        val = L[i]
        k = i

        # Start from the current position of the array and iterate backwards
        # toward the beginning of the array comparing adjascent values as you
        # go.
        while k > 0 and val < L[k - 1]:
            L[k] = L[k - 1]
            k -= 1

        L[k] = val

    return L

