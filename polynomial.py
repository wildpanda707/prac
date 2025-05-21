""" Write a Program to evaluate a polynomial function. (For example store f(x) = 4n2 +
2n + 9 in an array and for a given value of n, say n = 5, compute the value of f(n))."""
def evaluate_polynomial(coeffs, n):
    return sum(coeff * (n ** i) for i, coeff in enumerate(coeffs))

# Example: f(n) = 4n^2 + 2n + 9 --> coeffs = [9, 2, 4]
coeffs = [9, 2, 4]
n = int(input("Enter value of n: "))
print("Value of polynomial:", evaluate_polynomial(coeffs, n))
