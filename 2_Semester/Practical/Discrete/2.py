"""2. Create a class RELATION, use Matrix notation to represent a relation. Include
member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric, 
Transitive. Using these functions check whether the given relation is: Equivalence or Partial Order relation or None"""

from numpy import array
class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.length = len(matrix)
    
    def reflexive(self):
        for i in range(self.length):
            if not self.matrix[i][i]:
                return False
        return True

    def symmetric(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def transitive(self):
        for i in range(self.length):
            for j in range(self.length):
                for k in range(self.length):
                    if self.matrix[i][j] and self.matrix[j][k] and not self.matrix[i][k]:
                        return False
        return True

    def anti_symmetric(self):
        for i in range(self.length):
            for j in range(self.length):
                if i != j and self.matrix[i][j] and self.matrix[j][i]:
                    return False
        return True
    
def enter_matrix():
    lst = list(map(int, input("Enter All Relation In Form Of Matrix Value With A Space:: ").split()))
    row = int(input("Enter How Many Row or Columns In Your Square Matrix:: "))
    matrix = array(lst).reshape(row, row)
    print("Your Required Matrix Are:: \n", matrix)
    return matrix

def main():
    rel = RELATION(enter_matrix())
    if rel.reflexive() and rel.symmetric() and rel.transitive():
        return "Your Relation is Equivalence Relation."
    elif rel.reflexive() and rel.anti_symmetric() and rel.transitive():
        return "Your Relation is Partial Order Relation."
    else:
        return "None"
if __name__ == "__main__":
    print(main())