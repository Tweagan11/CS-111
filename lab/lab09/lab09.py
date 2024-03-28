from random import randint


def in_range1(n):
    """Write a function that checks to see if n is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    if 1 <= n <= 100:
        return True
    else:
        return False


def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    for n in range(1001):
        try:
            num = randint(1, 102)
            in_range2(num)
        except ValueError:
            print(num)



def in_range2(num):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    if 1 > num or num > 100:
        raise ValueError('Number Out of Range')
    else:
        return None


if __name__ == "__main__":
    main()
