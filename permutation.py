"""3. Write a Program that generates all the permutations of a given set of digits, with or
without repetition."""
from itertools import permutations, product

def generate_permutations(digits, repeat=False):
    if repeat:
        return list(product(digits, repeat=len(digits)))
    else:
        return list(permutations(digits))

digits = input("Enter digits: ").split()
print("Without Repetition:", generate_permutations(digits))
print("With Repetition:", generate_permutations(digits, repeat=True))
