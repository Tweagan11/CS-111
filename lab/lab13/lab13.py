def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


def multiply(m, n):
    """ Takes two positive integers (including zero) and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if m == 0 or n == 0:
        return 0
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def is_prime(n):

    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    if n < 2:
        return False

    def is_prime_helper(m):
        if m == 1:
            return True
        elif n % m == 0:
            return False
        else:
            return is_prime_helper(m - 1)

    return is_prime_helper(n - 1)





is_prime(2)