# Compute Curl Of A Vector Field.

import sympy as sp

def compute_curl(vector_field, variables):
    curl = [
        sp.diff(vector_field[2], variables[1]) - sp.diff(vector_field[1], variables[2]),
        sp.diff(vector_field[0], variables[2]) - sp.diff(vector_field[2], variables[0]),
        sp.diff(vector_field[1], variables[0]) - sp.diff(vector_field[0], variables[1])
    ]
    return curl

def main():
    x, y, z = sp.symbols('x y z')
    
    F1 = x**2 + y**2 
    F2 = y**3 + z    
    F3 = x * z**2    
    
    vector_field = [F1, F2, F3]
    
    curl = compute_curl(vector_field, [x, y, z])
    
    print(f"Vector field: F(x, y, z) = ({F1}, {F2}, {F3})")
    print("\nCurl of the vector field:")
    print(curl)
    
    curl_at_point = [comp.evalf(subs={x: 1, y: 2, z: 3}) for comp in curl]
    print(f"\nCurl at the point (1, 2, 3): {curl_at_point}")

if __name__ == "__main__":
    main()
