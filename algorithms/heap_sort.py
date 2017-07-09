
def sort(A):
    heapify(A)
    end = len(A) - 1

    while end > 0:
        A[end], A[0] = A[0], A[end]
        sift_down(A, 0, end - 1)
        end -= 1

    return A

def heapify(A):
    start = (len(A) - 2) // 2
    while start >= 0:
        sift_down(A, start, len(A) - 1)
        start -= 1

def sift_down(A, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and A[child] < A[child + 1]:
            child += 1
        if child <= end and A[root] < A[child]:
            A[root], A[child] = A[child], A[root]
            root = child
        else:
            return
