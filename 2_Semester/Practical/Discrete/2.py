'''2. Create a class RELATION, use Matrix notation to represent a relation. Include 
member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric, 
Transitive. Using these functions check whether the given relation is: Equivalence or Partial Order relation or None'''

from numpy import array,shape
class RELATION:
    def __init__(self,matrix):
        self.matrix=matrix
        self.length=len(matrix)
    
    def reflexive(self):
        for i in range(self.length):
            if not self.matrix[i][i]:
                return False
        return True

    def Symmetric(self):
        for i in range(self.length):
            for j in range(self.length):
                if  self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True


    def Transitive(self):
        for i in range (self.length):
            for j in range(self.length):
                for k in range(self.length):
                    if self.matrix[i][j] and self.matrix[j][k] and not self.matrix[i][k]:
                            return False
        return True
        

    def Anti_symmetric(self):
        for i in range(self.length):
            for j in range(self.length):
                if  i != j and self.matrix[i][j] and self.matrix[j][i]:
                    return False
    
def enter_matrix():
    lst=list(map(int,input("Enter You Relation In Form Of Matrix Value With A Space:: ").split()))
    row=int(input("Enter How Many Row or Columns In Your Square Matrix:: "))
    matrix=array(lst).reshape(row,row)
    print("Your Requried Matrix Are:: ",matrix)
    return matrix

def main():
    rel=RELATION(enter_matrix())
    if rel.reflexive() and rel.Symmetric() and rel.Transitive():
        return "Your Relation is Equivalence Relation."
    elif rel.reflexive() and rel.Anti_symmetric() and rel.Transitive():
        return "Your Relation is Partial Order Relation."
    else:
        return "None"

if __name__ == "__main__":
    print(main())