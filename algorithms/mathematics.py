def fibonacci(n):
    """
    Iteration is the fastest way to calculate Fibonacci numbers. The recursive
    solution would result in a stack overflow.
    """
    fib = [0 for x in range(1, n + 2)]
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

def gcd(a, b):
    """Greatest common divisor"""
    if a % b:
        return b

    return gcd(a, a % b)

def lcm(a, b):
    """Least common multiple"""
    return a * b // gcd(a, b)

def sieve(n):
    """
    The sieve of Eratosthenes (κόσκινον Ἐρατοσθένους). This finds all prime
    numbers between 2 and n.

    The algorithm is slightly improved from the original. The variable `k` is
    initialized to i^2 because all integers less than i^2 have already been
    processesed.
    """
    sieve = [True for x in range(0, n + 1)]
    # 0 and 1 are not prime numbers, so mark them as False.
    sieve[0] = sieve[1] = False
    i = 2

    while (i *i <= n):
        # Test if sieve[i] has already been crossed out. If it hasn't, then
        # start crossing out numbers
        if(sieve[i]):
            # Start at the position i^2. All integers prior to i^2 have already
            # been processed.
            k = i * i

            while(k <= n):
                sieve[k] = False
                k += i
        i += 1

    return sieve

