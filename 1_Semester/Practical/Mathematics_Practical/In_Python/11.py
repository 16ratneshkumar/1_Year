# Compute Gradient Of A Scalar Field.

import sympy as sp

def compute_gradient(function, variables):
    gradient = [sp.diff(function, var) for var in variables]
    return gradient

def main():
    x, y, z = sp.symbols('x y z')
    
    function = x**2 + y**2 + z**2 
    
    gradient = compute_gradient(function, [x, y, z])
    
    print(f"Scalar field: f(x, y, z) = {function}")
    print("\nGradient of the scalar field:")
    for i, grad in enumerate(gradient, 1):
        print(f"∂f/∂{['x', 'y', 'z'][i-1]} = {grad}")
    
    gradient_at_point = [grad.evalf(subs={x: 1, y: 2, z: 3}) for grad in gradient]
    print("\nGradient at the point (1, 2, 3):")
    for i, grad_value in enumerate(gradient_at_point, 1):
        print(f"∂f/∂{['x', 'y', 'z'][i-1]} at (1, 2, 3) = {grad_value}")

if __name__ == "__main__":
    main()
