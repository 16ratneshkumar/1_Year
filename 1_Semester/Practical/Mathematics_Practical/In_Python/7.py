# Check The Linear Dependence Of Vectors. Generate A Linear Combination Of Given Vectors Of Rn/ Matrices Of The Same Size And Find The Transition Matrix Of Given Matrix Space.

import numpy as np
from sympy import Matrix

def check_linear_dependence(vectors):
    matrix = Matrix(vectors).T
    rank = matrix.rank()
    if rank < len(vectors):
        return True, rank 
    return False, rank

def generate_linear_combination(vectors, coefficients):
    result = np.zeros_like(vectors[0], dtype=float)
    for coef, vec in zip(coefficients, vectors):
        result += coef * np.array(vec)
    return result

def compute_transition_matrix(basis_from, basis_to):
    basis_from_matrix = Matrix(basis_from).T
    basis_to_matrix = Matrix(basis_to).T

    transition_matrix = basis_to_matrix.inv() * basis_from_matrix
    return np.array(transition_matrix).astype(float)

def main():
    print("Linear Dependence, Linear Combination, and Transition Matrix")

    print("\nEnter the number of vectors or matrices: ")
    num_vectors = int(input())
    print("Enter the dimension (size) of each vector or matrix (e.g., 3 for R^3 or 2x2): ")
    dimension = int(input())

    vectors = []
    for i in range(num_vectors):
        print(f"Enter vector/matrix {i + 1} as space-separated numbers:")
        vec = list(map(float, input().split()))
        vectors.append(vec)

    is_dependent, rank = check_linear_dependence(vectors)
    print("\nLinear Dependence Check:")
    if is_dependent:
        print("The vectors are linearly dependent.")
    else:
        print("The vectors are linearly independent.")
    print(f"Rank of the matrix: {rank}")

    print("\nEnter coefficients for linear combination (space-separated):")
    coefficients = list(map(float, input().split()))
    linear_combination = generate_linear_combination(vectors, coefficients)
    print(f"Linear combination result: {linear_combination}")

    print("\nEnter another basis (same dimension) for transition matrix computation:")
    basis_to = []
    for i in range(dimension):
        print(f"Enter vector {i + 1} of the new basis as space-separated numbers:")
        vec = list(map(float, input().split()))
        basis_to.append(vec)

    transition_matrix = compute_transition_matrix(vectors[:dimension], basis_to)
    print("\nTransition Matrix:")
    print(transition_matrix)

if __name__ == "__main__":
    main()
