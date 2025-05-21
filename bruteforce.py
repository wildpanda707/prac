"""4.For any number n, write a program to list all the solutions of the equation x₁ + x₂ + x₃ + ... + xₙ = C, where C is a constant (C ≤ 10) and x₁, x₂, x₃, ..., xₙ are nonnegative integers, using brute force strategy.."""
def find_solutions(n, C):
    def helper(current, total):
        if len(current) == n:
            if total == C:
                results.append(current[:])
            return
        for i in range(C + 1):
            if total + i <= C:
                current.append(i)
                helper(current, total + i)
                current.pop()
    
    results = []
    helper([], 0)
    return results

n = int(input("Enter number of variables (n): "))
C = int(input("Enter constant C (<=10): "))
solutions = find_solutions(n, C)

print(f"\nAll non-negative integer solutions to x1 + x2 + ... + x{n} = {C}:\n")
for s in solutions:
    print(s)
