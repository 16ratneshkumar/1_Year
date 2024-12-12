# Find The Orthonormal Basis Of Given Vectorspace Using The Gram-Schmidt Orthogonalization Process.

import numpy as np

def gram_schmidt(vectors):
    """
    Perform the Gram-Schmidt process to compute an orthonormal basis.
    
    Parameters:
    vectors (list of lists or np.ndarray): List of vectors in the vector space.

    Returns:
    orthonormal_basis (list of np.ndarray): Orthonormal basis of the vector space.
    """
    orthonormal_basis = []
    
    for v in vectors:
        v = np.array(v, dtype=float) 
        for u in orthonormal_basis:
            v -= np.dot(v, u) * u
        norm = np.linalg.norm(v)
        if norm > 1e-10: 
            orthonormal_basis.append(v / norm)
    
    return orthonormal_basis

def main():
    print("Find the Orthonormal Basis of a Vector Space Using Gram-Schmidt Orthogonalization")
    num_vectors = int(input("Enter the number of vectors in the space: "))
    dimension = int(input("Enter the dimension of the vectors: "))
    
    print("Enter each vector as space-separated numbers:")
    vectors = []
    for i in range(num_vectors):
        vec = list(map(float, input(f"Vector {i + 1}: ").split()))
        vectors.append(vec)
    
    orthonormal_basis = gram_schmidt(vectors)
    
    print("\nOrthonormal Basis:")
    if len(orthonormal_basis) == 0:
        print("The given set of vectors does not span a vector space.")
    else:
        for i, vec in enumerate(orthonormal_basis, 1):
            print(f"Vector {i}: {vec}")

if __name__ == "__main__":
    main()
