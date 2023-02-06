def print_number(n):
    if n == 1:
        return n
    else:
        print_number(n-1)
        return n
print(print_number(50))