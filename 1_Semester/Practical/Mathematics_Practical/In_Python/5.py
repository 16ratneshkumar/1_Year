# Solve A System Of Homogeneous Equations Using The Gauss Jordan Method.

import numpy as np

def gauss_jordan(matrix):
    rows, cols = matrix.shape

    for i in range(rows):
        if matrix[i, i] != 0:
            matrix[i] = matrix[i] / matrix[i, i]
        else:
            for k in range(i + 1, rows):
                if matrix[k, i] != 0:
                    matrix[[i, k]] = matrix[[k, i]]
                    matrix[i] = matrix[i] / matrix[i, i]
                    break

        for j in range(rows):
            if i != j:
                factor = matrix[j, i]
                matrix[j] -= factor * matrix[i]

    return matrix

def get_homogeneous_solution(augmented_matrix):
    rows, cols = augmented_matrix.shape
    solution_space = []

    if rows < cols - 1:
        print("\nThe system has infinitely many solutions:")
        for i in range(rows, cols - 1):
            solution_space.append(f"x{i + 1} = free variable")
    else:
        print("\nThe system has a unique or trivial solution:")

    solutions = augmented_matrix[:, -1]
    for i, sol in enumerate(solutions):
        solution_space.append(f"x{i + 1} = {sol}")

    return solution_space

def main():
    print("Solve a System of Homogeneous Equations Using Gauss-Jordan Method")
    num_equations = int(input("Enter the number of equations: "))

    print("Enter the coefficients of the equations row by row:")
    coeff_matrix = []
    for i in range(num_equations):
        row = input(f"Row {i + 1}: ").split()
        coeff_matrix.append([float(num) for num in row])

    coeff_matrix = np.array(coeff_matrix)

    zero_column = np.zeros((num_equations, 1))
    augmented_matrix = np.hstack((coeff_matrix, zero_column))

    reduced_matrix = gauss_jordan(augmented_matrix)

    print("\nRow Reduced Echelon Form (RREF):")
    print(reduced_matrix)

    solution_space = get_homogeneous_solution(reduced_matrix)
    print("\nSolution:")
    for sol in solution_space:
        print(sol)

if __name__ == "__main__":
    main()
