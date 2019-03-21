def sum_array(array):

    '''Return sum of all items in array'''

    total = 0

    for num in array:
        total= total + num

    return total

def fibonacci(n):
    """
    The first two terms are 0 and 1. All other terms are
    obtained by adding the preceding two terms. This means
    to say the nth term is the sum of (n-1)th and (n-2)th term.

    """
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):

    """
    The factorial function multiplies all whole numbers from the input n down to 1.
    Notice how the function does factorial(n-1) within factorial(n)!

    """
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    """
     The reverse functions traverses an array
     from end to start, one character at a time.

    """
    if len(word) == 1:
        return word

    return word[-1] + reverse(word[:-1])
