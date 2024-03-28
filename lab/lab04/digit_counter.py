def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0

    while num > 0:
        print(f"Digits: {num}")
        if func(num % 10):
            print(f"DEBUG: Inside digit_counter function")
            counter += 1
            print(f"Counter: {counter}")
        num = num // 10
        print(f"Num after div: {num}")

    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


"""ADD_TESTING_CODE"""
print(digit_counter(is_even, 12334467))
