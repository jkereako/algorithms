def sort(L):
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
