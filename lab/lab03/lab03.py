def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    x = []
    for i in range(len(s)):
        if i % 2 == 0:
            y = s[i] * i
            x.append(y)
    return x

K = [1, 2, 3, 4, 5, 6]
even_weighted(K)

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)

    v = [[s[i], t[i]] for i in range(len(s))]
    return v


def count_appearances(lst):
    """Returns a dictionary containing each integer's appearance count
    >>> lst = [0]
    >>> count_appearances(lst)
    {0: 1}
    >>> lst = [0, 0, 1, 2, 1, 1]
    >>> count_appearances(lst)
    {0: 2, 1: 3, 2: 1}
    >>> lst = [0, 0, 0, 0, 0, 3, 0, 0]
    >>> count_appearances(lst)
    {0: 7, 3: 1}
    """
    new_dict = {}
    for key in lst:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1

    return new_dict

def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    counter = 0
    with open(input_filename, 'r') as infile:
        with open(output_filename, 'w') as outfile:
            lines = infile.readlines()
            for line in lines:
                counter += 1
                print(f"{counter}: {line}", end="")
                outfile.write(f"{counter}: {line}")



########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    return [i for i in range(1,n) if n%i == 0]

def slice_and_multiplice(lst):
    """Return a new list where all values past the first are
    multiplied by the first value.

    >>> slice_and_multiplice([1,1,6])
    [1, 6]
    >>> slice_and_multiplice([9,1,5,2])
    [9, 45, 18]
    >>> slice_and_multiplice([4])
    []
    >>> slice_and_multiplice([0,4,9,18,20])
    [0, 0, 0, 0]
    """
    return [lst[i]*lst[0] for i in range(1,len(lst))]
