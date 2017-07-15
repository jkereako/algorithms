
def max_subarray(A):
        """
        Kadane's algorithm.

        The problem was first posed by Ulf Grenander of Brown University in
        1977. A linear time algorithm was found soon afterwards by Jay Kadane
        of Carnegie Mellon University.

        Performance
        ===========
        O(n)
        """
    max_ending_here = max_so_far = A[0]

    for x in A[1:]:
        # `max_ending_here` keeps a running total of the maximum subarray.
        max_ending_here = max(x, max_ending_here + x)

        # `max_so_far` changes only twice; once at the beginning of the maximum
        # subarray and once at the end.
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
