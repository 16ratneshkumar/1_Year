# Table Of Contents
- ## [Overview Of C]
- ## [Parameter passing technioues]


## Overview Of C
   - ### declaration 
       - ### simple variable
             int a;
       - ### pointer variable
             int *a;    \\ a is a pointer variable
       - ### array
             int a[9];  \\9 is the size of an array
   - ### initialization
       - ### simple variable
             int a=10;
       - ### pointer variable
             int a=10;
              *b=&a;
       - ### array
             int a[9]={1,2,3,4,5,6,7,8,9};

## Pointer
    - 
## memory accessing for array
   - ### row major order 
   - ### column major order
## scoping 
   - ### static scoping
         -
   - ### dynamic scoping
         - 
## Parameter passing technioues
   - Caller Function (A): The caller function, also known as the calling function or the client function, is the function that initiates the call to another function.
   - Called Function or Callee Function (B): The called function, also known as the callee function or the target function, is the function that is invoked or executed when called by another function.
   - Terminology
      - Formal Parameter: A formal parameter is like a variable declaration within the function or method’s prototype or definition. It specifies the name of the parameter and its data type. It serves as a placeholder for the actual value that will be passed when the function or method is called.
      - Actual arguments, also referred to as arguments or parameters
      - Actual Parameter: An actual parameter, on the other hand, is the real value or expression provided in the function or method call, which corresponds to a formal parameter. It is the concrete data that gets passed into the function or method when it is invoked.
      - Modes:
        - IN Mode: When a parameter is passed as IN, it means the caller is providing information to the callee. The callee can use this information but cannot modify the original value in the caller.
        - OUT Mode: When a parameter is passed as OUT, it means the callee can write or modify the value of this parameter, and those modifications will be reflected in the caller’s environment.
        - IN/OUT Mode: This combines both IN and OUT modes. The caller provides an initial value to the callee, and the callee can both use and modify the value, which will then be visible to the caller after the function or method call.

   - ### call by value
         - 
   - ### call by reference
         - 




garbage collector
type of matrix
spare
dense

why indexing is starts with 0 in place of 1