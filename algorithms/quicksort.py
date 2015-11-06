def sort(L):
    """
    Developed in 1959 by Tony Hoare, quicksort is still a commonly used
    algorithm.

    Performance
    ===========
    Worst:      O(n^2)
    Average:    O(n log n)
    Best:       O(n log n)

    Space
    =====
    Worst:      O(n)
    Average:    O(n log n)
    """

    if len(L) <= 1:
        return L

    lesser = []
    greater = []
    pivots = []

    pivot = L[0]

    for val in L:
        if val < pivot:
            lesser.append(val)
        elif val > pivot:
            greater.append(val)
        else:
            pivots.append(val)

    lesser = sort(lesser)
    greater = sort(greater)

    return lesser + pivots + greater

