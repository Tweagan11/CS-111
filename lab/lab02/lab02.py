def falling(n, k):
    total = 1
    while k > 0:
        total = total * n
        n -= 1
        k -= 1

    return total


def sum_digits(y):
    sum = 0
    while y != 0:
        sum += y % 10
        y = y // 10
    return sum

##################################################
"""Code below here is for extra practice and doesn't count for or against
your grade on this lab.
def double_eights(n):
    Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
"*** YOUR CODE HERE ***"""

def double_eights(n):
    while n != 0:
        if (n % 10 == 8):
            n = n // 10
            if (n % 10 == 8):
                return True
        else:
            n = n // 10
            if(n < 10):
                return False

print(double_eights(80878))