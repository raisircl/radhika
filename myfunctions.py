"""
This module contains utility functions for basic arithmetic operations and printing multiplication tables.
"""
def sum(n1, n2):
    """Returns the sum of n1 and n2."""
    return n1 + n2

def biggest(n1,n2):
    """Returns the bigger of n1 and n2."""
    if n1 > n2:
        return n1
    else:
        return n2

def table(num):
    """Prints the multiplication table of the given number."""
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
