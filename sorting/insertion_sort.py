def sort(list):
    for i in range(1, len(list)):
        tmp = list[i]
        k = i

        while k > 0 and tmp < list[k - 1]:
            list[k] = list[k - 1]
            k -= 1

        list[k] = tmp

    return list
