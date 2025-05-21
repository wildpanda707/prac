"""Create a class SET. Create member functions to perform the following SET
operations:
1) ismember: check whether an element belongs to the set or not and return value
as true/false.
2) powerset: list all the elements of the power set of a set .
3) subset: Check whether one set is a subset of the other or not.
4) union and Intersection of two Sets.
5) complement: Assume Universal Set as per the input elements from the user.
6) set Difference and Symmetric Difference between two sets.
7) cartesian Product of Sets.
Write a menu driven program to perform the above functions on an instance of the
SET class."""
from itertools import chain, combinations, product

class SET:
    def __init__(self, elements):
        self.set = set(elements)

    def ismember(self, x):
        return x in self.set

    def powerset(self):
        s = list(self.set)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

    def subset(self, other):
        return self.set.issubset(other.set)

    def union(self, other):
        return self.set.union(other.set)

    def intersection(self, other):
        return self.set.intersection(other.set)

    def complement(self, universal):
        return universal.set.difference(self.set)

    def difference(self, other):
        return self.set.difference(other.set)

    def symmetric_difference(self, other):
        return self.set.symmetric_difference(other.set)

    def cartesian_product(self, other):
        return list(product(self.set, other.set))

# Menu
def menu():
    A = SET(input("Enter elements of Set A separated by space: ").split())
    B = SET(input("Enter elements of Set B separated by space: ").split())
    U = SET(input("Enter elements of Universal Set separated by space: ").split())
    
    while True:
        print("\n1. ismember\n2. powerset\n3. subset\n4. union\n5. intersection\n6. complement\n7. difference\n8. symmetric difference\n9. cartesian product\n0. Exit")
        choice = input("Choose operation: ")

        if choice == "1":
            x = input("Enter element to check in A: ")
            print(A.ismember(x))
        elif choice == "2":
            print(A.powerset())
        elif choice == "3":
            print("A subset of B?", A.subset(B))
        elif choice == "4":
            print("A ∪ B:", A.union(B))
        elif choice == "5":
            print("A ∩ B:", A.intersection(B))
        elif choice == "6":
            print("Complement of A:", A.complement(U))
        elif choice == "7":
            print("A - B:", A.difference(B))
        elif choice == "8":
            print("Symmetric Difference A △ B:", A.symmetric_difference(B))
        elif choice == "9":
            print("A × B:", A.cartesian_product(B))
        elif choice == "0":
            break
        else:
            print("Invalid option")

menu()
