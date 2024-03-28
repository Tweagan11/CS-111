import sys


def print_args(lst):
    for arg in lst:
        print(arg)

def check_flags(lst):
    if lst[1] == '-p' or lst[1] == '-i' or lst[1] == '-h' or lst[1] == '-w' or lst[1] == '-r':
        return True
    else:
        return False

def flags(lst):
    if lst[1] == '-p':
        print_args(lst[2:])

    elif lst[1] == '-i':
        print("Hello World")

    elif lst[1] == '-h':
        print("Valid flags:")
        print("-p : prints out all the command line arguments after the -p")
        print("-i : prints \"Hello World\"")
        print("-h : prints out a help command")

    elif lst[1] == '-w':
        if len(lst) > 3:
            with open(lst[2], 'w') as infile:
                for line in lst[3:]:
                    infile.write(line + '\n')
        else:
            print("No Content Provided")

    elif lst[1] == '-r':
        with open(lst[2], 'r') as outfile:
            for line in outfile:
                print(line, end='')


if check_flags(sys.argv) :
    flags(sys.argv)
else:
    print_args(sys.argv)

