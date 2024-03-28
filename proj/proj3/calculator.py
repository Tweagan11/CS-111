from pair import Pair, nil
from operator import add, sub, mul, truediv

def parse(tokens):
    p_tokens = parse_tokens(tokens, 0)[0]
    return p_tokens


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
    except ValueError as e:
        raise TypeError(f"Error converting token '{tokens[index]}' to number: {e}")
    new_pair, index = parse_tokens(tokens, index + 1)
    return Pair(num, new_pair), index


def tokenize(expression):
    line = expression.strip()
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    return line.split()


def reduce(func, operands, initial):
    while operands != nil:
        initial = func(initial,operands.first)
        operands = operands.rest
    return initial

def apply(operator, operands):
    if operator == '+':
        return reduce(add, operands.rest, operands.first)
    elif operator == '*':
        return reduce(mul, operands.rest, operands.first)
    elif operator == '-':
        return reduce(sub, operands.rest, operands.first)
    elif operator == '/':
        return reduce(truediv, operands.rest, operands.first)
    else:
        raise TypeError("Operator invalid")

def identity(x):
    return x

def eval(syntax_tree):
    if isinstance(syntax_tree, int) or isinstance(syntax_tree, float):
        return syntax_tree
    elif isinstance(syntax_tree, Pair):
        if isinstance(syntax_tree.first, Pair):
            val = eval(syntax_tree.first)
            rest = syntax_tree.rest.map(eval)
            return Pair(val, rest)
        elif syntax_tree.first in ['+', '-', '/', '*']:
            rest = syntax_tree.rest.map(eval)
            return apply(syntax_tree.first, rest)
    else:
        raise TypeError("Something went wrong")



if __name__ == "__main__":
    print("Welcome to the CS 111 Calculator Interpreter.")
    inp = ""
    while inp != "exit":
        inp = input("calc >> ")
        if inp == "exit":
            break
        try:
            inp = tokenize(inp)
            parse_inp = parse(inp)
            print(eval(parse_inp))
        except Exception as exception:
            print(exception)

    print("Goodbye!")