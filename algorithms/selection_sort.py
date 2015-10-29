def sort(list):
    """Assumes that L is a list of elements that can be compared
       using >.  Sorts L in ascending order"""
    for i in range(len(list) - 1):
        #Invariant: list[:i] is sorted
        min_idx = i
        min_val= list[i]
        j = i + 1

        while j < len(list):
            if min_val > list[j]:
                min_idx = j
                min_val= list[j]
            j += 1

        temp = list[i]
        list[i] = list[min_idx]
        list[min_idx] = temp

    return list
