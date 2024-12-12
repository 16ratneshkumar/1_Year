# Solve A System Of Homogeneous And Non-Homogeneous Equations Using Gauss Elimination Method.

import numpy as np

def gauss_elimination(coeff_matrix, constants):
    n = len(constants)
    
    augmented_matrix = np.hstack((coeff_matrix, constants.reshape(-1, 1)))

    for i in range(n):
        if augmented_matrix[i, i] == 0:
            for k in range(i + 1, n):
                if augmented_matrix[k, i] != 0:
                    augmented_matrix[[i, k]] = augmented_matrix[[k, i]]
                    break

        for j in range(i + 1, n):
            ratio = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= ratio * augmented_matrix[i, i:]

    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solution[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], solution[i + 1:])) / augmented_matrix[i, i]
    
    return solution

def main():
    print("Solve a System of Equations Using Gauss Elimination Method")
    num_equations = int(input("Enter the number of equations: "))

    print("Enter the coefficients of the equations row by row:")
    coeff_matrix = []
    for i in range(num_equations):
        row = input(f"Row {i + 1}: ").split()
        coeff_matrix.append([float(num) for num in row])

    coeff_matrix = np.array(coeff_matrix)

    is_homogeneous = input("Is the system homogeneous? (yes/no): ").strip().lower()

    if is_homogeneous == 'yes':
        constants = np.zeros(num_equations)
    else:
        print("Enter the constant terms of the equations:")
        constants = np.array([float(input(f"Constant for equation {i + 1}: ")) for i in range(num_equations)])

    try:
        solution = gauss_elimination(coeff_matrix, constants)
        print("\nSolution to the System of Equations:")
        for i, sol in enumerate(solution, 1):
            print(f"x{i} = {sol}")
    except Exception as e:
        print("\nError: ", str(e))
        print("The system of equations may not have a unique solution.")

if __name__ == "__main__":
    main()
