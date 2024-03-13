# Table Of Contents
- ## [Overview Of C]
   ```
   typecasting
   primitive data type

   ```
- ## [Scoping]
- ## [Parameter Passing Technioues]
- ## [Circuit switch]
- ## [Array]
   ```
   dereference
   ```
- ## [Pointer]
   ```
   type of point
      near
      far

   functional pointer
   ```
- ## [Recursion]
- ## [Structures(User Define Datatype)]
- ## [Linked List]
- ## [Double Linked List]
   - ## [Binary Tree]

## Overview Of C
   - ### declaration 
       - ### simple variable
            ``` c
            int a;
            ```
       - ### pointer variable
            ```c
            int *a;    /*a is a pointer variable*/
            ```
       - ### array
            ```c
            int a[9];  /*9 is the size of an array*/
            ```
   - ### initialization
       - ### simple variable
            ``` c
            int a=10;
            ```
       - ### pointer variable
            ```c
            int a=10;
            *b=&a;
            ```
       - ### array
            ```c
            int a[9]={1,2,3,4,5,6,7,8,9};
            ```
## Scoping 
   - ### static scoping
      
   - ### dynamic scoping
       
## Parameter Passing Technioues
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
      - There are different parameter passing techniques like -
        1. [Pass By Value]
        2. [Pass By Reference]
        3. [Pass By Pointer]
        4. [Pass By Result]
        5. [Pass By Value-Result(Copy-Restore)]
        6. [Pass By Name]
        7. [Pass By Need]

   - ### Pass By Value
      ```c
      int main(){
            int Num1=9;
            int Num2=5;
            printf("Before Swapping:: \nNum1 = %d\nNum2 = %d\n",Num1,Num2);
            swap(Num1,Num2);
            printf("After Swapping:: \nNum1 = %d\nNum2 = %d\n",Num1,Num2);
            return 0;
            }
      swap(num1,num2){
            int a=num1;
            num1=num2;
            num2=a;
            return num1,num2;
            }
      ```
      OUTPUT::- 
      ```c
      Before Swapping:: 
      Num1 = 9
      Num2 = 5
      After Swapping:: 
      Num1 = 9
      Num2 = 5
      ```
   - ### Pass By Reference
      ```c++
      int main(){
            int Num1=9;
            int Num2=5;
            printf("Before Swapping:: \nNum1 = %d\nNum2 = %d\n",Num1,Num2);
            swap(&Num1,&Num2);
            printf("After Swapping:: \nNum1 = %d\nNum2 = %d\n",Num1,Num2);
            return 0;
      }
      swap(int *num1,int *num2){
            int a=*num1;
            *num1=*num2;
            *num2=a;
            return num1,num2;
      }
      ```
      OUTPUT::- 
      ```c
      Before Swapping:: 
      Num1 = 9
      Num2 = 5
      After Swapping:: 
      Num1 = 5
      Num2 = 9
      ```

## Array
   - 1-D Array
   - 2-D Array
   - Multi-D Array
   - ## memory accessing for array
      - ### row major order 
      - ### column major order





garbage collector
type of matrix
spare
dense

why indexing is starts with 0 in place of 1

 
## Pointer
## Recursion
   - Tail Recursion
   - Non-Tail Recursion
   - Nested Recursion
   - Indirect Recursion

## User Define Datatype
## Linked List
