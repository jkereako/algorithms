def sort(L):
    """
    Selection sort is an in-place comparison sort. The algorithm divides the
    input list into 2 parts: the sublist of items already sorted, which is built
    from the front of the list toward the tail, and the sublist of items yet to
    be sorted. See the example below:

    [64, 25, 12, 22, 11]    # Initial state
    [11, 25, 12, 22, 64]    # sorted sublist = [11]
    [11, 12, 25, 22, 64]    # sorted sublist = [11, 12]
    [11, 12, 22, 25, 64]    # sorted sublist = [11, 12, 22]
    [11, 12, 22, 25, 64]    # sorted sublist = [11, 12, 22, 25]
    [11, 12, 22, 25, 64]    # sorted sublist = [11, 12, 22, 25, 64]
    """

    for i in range(len(L) - 1):
        #Invariant: L[:i] is sorted
        min_idx = i
        min_val= L[i]
        j = i + 1

        while j < len(L):
            if min_val > L[j]:
                min_idx = j
                min_val= L[j]
            j += 1

        temp = L[i]
        L[i] = list[min_idx]
        L[min_idx] = temp

