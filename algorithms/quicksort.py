def sort(L):
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

