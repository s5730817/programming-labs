from math import sqrt

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    output = True
    right_border = int(sqrt(num)) + 1
    for i in range(2, right_border):
        if num % i == 0:
            output = False
            break


    return output


# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
  