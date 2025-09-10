def square_root(x, precision=2):
    if x < 0:
        raise ValueError ("Error: Cannot compute the square root of a negative number.")
    return x ** 0.5

num = float(input("Enter a number: "))
result = square_root(num)
print(f"The square root of {num} is {result}")
