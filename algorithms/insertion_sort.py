def sort(L):
    """
    Insertion sort is a simple algorithm which builds the final sorted list 1
    item at a time.

    It compares the current element with it's neighbor to the left. If the
    current element is smaller than the neighbor, it then compares with the
    neighbor before that and so on until the beginning of the list is reached.

    Performance
    ===========
    Worst:      O(n^2)
    Average:    O(n^2)
    Best:       O(n)

    Space
    =====
    Worst:      O(1)
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

