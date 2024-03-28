import sys

def merge(left, right):
    """
    merge two sorted lists
    >>>merge([1,3,5],[2,4,6])
    [1,2,3,4,5,6]
    >>> merge([1,1,9],[7,7,7])
    [1,1,7,7,7,9]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] <= right[0]:
        return [left[0]] + merge(left[1:], right[0:])
    else:
        return [right[0]] + merge(left[0:], right[1:])

def sort(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        mid = length // 2
        left = sort(list[:mid])
        right = sort(list[mid:])
        return merge(left, right)




if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile, 'r') as file:
        file_list = [int(line) for line in file]

    with open(outfile, 'w') as outfile:
        sorted_list = sort(file_list)
        for i in sorted_list:
            outfile.write(f"{i:03d}\n")

