"""2. Create a class RELATION, use Matrix notation to represent a relation. Include
member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric,
Transitive. Using these functions check whether the given relation is: Equivalence or
Partial Order relation or None"""
class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def is_reflexive(self):
        return all(self.matrix[i][i] == 1 for i in range(self.n))

    def is_symmetric(self):
        return all(self.matrix[i][j] == self.matrix[j][i] for i in range(self.n) for j in range(self.n))

    def is_antisymmetric(self):
        return all(self.matrix[i][j] == 0 or self.matrix[j][i] == 0 or i == j for i in range(self.n) for j in range(self.n))

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j]:
                    for k in range(self.n):
                        if self.matrix[j][k] and not self.matrix[i][k]:
                            return False
        return True

    def relation_type(self):
        r = self.is_reflexive()
        s = self.is_symmetric()
        a = self.is_antisymmetric()
        t = self.is_transitive()
        if r and s and t:
            return "Equivalence Relation"
        elif r and a and t:
            return "Partial Order Relation"
        else:
            return "None"

# Example
matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
R = RELATION(matrix)
print("Reflexive:", R.is_reflexive())
print("Symmetric:", R.is_symmetric())
print("Antisymmetric:", R.is_antisymmetric())
print("Transitive:", R.is_transitive())
print("Relation type:", R.relation_type())
