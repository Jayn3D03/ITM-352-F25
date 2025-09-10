# create a module with handy math functions
# name: chloecornforth
# date: 9/10/2025

# function to compute the midpoint between two numbers
def midpoint(num1, num2):
    mid = (num1 + num2) / 2
    return mid

# function to compute the square root of a number
def square_root(x):
    if x < 0:
        raise ValueError ("Error: Cannot compute the square root of a negative number.")
    return x ** 0.5

def exponent(base, exp):
    return base ** exp

# function to find the maximum of two numbers
def maximum(a, b):
    return a if a > b else b

# function to find the minimum of two numbers
def minimum(a, b):
    return a if a < b else b