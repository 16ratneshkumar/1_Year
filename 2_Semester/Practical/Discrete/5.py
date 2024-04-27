"""5. Write a Program to evaluate a polynomial function. (For example store f(x) = 4n2 + 
2n + 9 in an array and for a given value of n, say n = 5, compute the value of f(n))."""

def solve_polynomial():
    func = list(map(int, input("Enter Your polynomial coefficient Seperated With Space::").split()))
    num = int(input("Enter Value Of Your Variable::"))
    value = 0
    for i in range(-1, -len(func)-1, -1):
        value += func[i]*num**(-i-1)
    return value
print(solve_polynomial())
