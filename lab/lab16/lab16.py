from pair import *
import os


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    # lst = expression.split()
    # new_list = []
    # for token in lst:
    #     num = ""
    #     if token[0] == "(" or token[-1] == ")":
    #         for char in token:
    #             if char == "(":
    #                 open_par = True
    #             elif char == ")":
    #                 open_par = False
    #             else:
    #                 num = num + char
    #         if open_par:
    #             new_list.append("(")
    #             new_list.append(num)
    #         else:
    #             new_list.append(num)
    #             new_list.append(")")
    #     else:
    #         new_list.append(token)
    # return new_list
    # lst = []
    # num = ""
    # for char in [*expression]:
    #     if char == '(':
    #         lst.append('(')
    #     elif char == ')':
    #         lst.append(num)
    #         lst.append(')')
    #     else:
    #         if char == " ":
    #             lst.append(num)
    #             num = ""
    #         else:
    #             num += char
    # return lst
    # lst = []
    # num = ""
    # for char in expression:
    #     if char in '()':
    #         if num:
    #             lst.append(num)
    #             num = ""
    #         lst.append(char)
    #     elif char == ' ':
    #         if num:
    #             lst.append(num)
    #             num = ""
    #     else:
    #         num += char
    # if num:
    #     lst.append(num)
    # return lst
    line = expression.strip()
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    return line.split()



# OPTIONAL
def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    if tokens[index] == '(':
        oper = tokens[index + 1]
        if index != 0:
            sub, index = parse_tokens(tokens, index + 2)
            oper = Pair(oper, sub)
        if index == 0:
            index += 2
        new_pair, index = parse_tokens(tokens, index)
        return Pair(oper, new_pair), index
    if tokens[index] == ')':
        return nil, index + 1
    try:
        if '.' in tokens[index]:
            num = float(tokens[index])
        else:
            num = int(tokens[index])
        new_pair, index = parse_tokens(tokens, index + 1)
        return Pair(num, new_pair), index
    except TypeError:
        print("Invalid token")
        return



