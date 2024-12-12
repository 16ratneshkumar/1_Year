# Compute Divergence of a vector field.

import sympy as sp

def compute_divergence(vector_field, variables):
    divergence = sum(sp.diff(comp, var) for comp, var in zip(vector_field, variables))
    return divergence

def main():
    x, y, z = sp.symbols('x y z')
    
    F1 = x**2 + y**2 
    F2 = y**3 + z    
    F3 = x * z**2     
    
    vector_field = [F1, F2, F3]
    
    divergence = compute_divergence(vector_field, [x, y, z])
    
    print(f"Vector field: F(x, y, z) = ({F1}, {F2}, {F3})")
    print("\nDivergence of the vector field:")
    print(divergence)
    
    divergence_at_point = divergence.evalf(subs={x: 1, y: 2, z: 3})
    print(f"\nDivergence at the point (1, 2, 3): {divergence_at_point}")

if __name__ == "__main__":
    main()
