"""4. For any number n, write a program to list all the solutions of the equation x1 + x2 + 
x3 + ...+ xn = C, where C is a constant (C<=10) and x1, x2,x3,...,xn are non-negative 
integers, using brute force strategy."""
def find_solutions(C, n):
    def generate_solutions(current_sum, current_solution, remaining_terms):
        if current_sum == C:
            solutions.append(current_solution[:])
            return
        if not remaining_terms:
            return
        for i in range(remaining_terms[0], C - current_sum + 1):
            current_solution.append(i)
            generate_solutions(current_sum + i, current_solution, remaining_terms[1:])
            current_solution.pop()

    solutions = []
    generate_solutions(0, [], list(range(C + 1)))
    return solutions

if __name__ == "__main__":
    n = int(input("Enter number of terms::"))
    C = int(input("Enter value of constant::"))
    all_solutions = find_solutions(C, n)
    print(f"All solutions for {n} terms equation which sum is {C}")
    for solution in all_solutions:
        print(solution)
