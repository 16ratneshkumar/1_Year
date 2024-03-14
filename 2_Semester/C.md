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
* Scope of a variable is the part of the program where the variable is visible. Variables have a limited scope. Two variables with the same name can be declared in different scopes. The scope of global variables is the entire program. The scope of local variables is limited to the function in which they are declared. The scope of a variable is determined by its location in the program text.

* lets understand with an example

    ```c++
    #include<iostream>
    using namespace std;
    int x = 10;
    int main(){
        int x = 20;
        {
            int x = 30;
            cout<<x<<endl;
        }
        cout<<x<<endl;
        cout<<::x<<endl;
        return 0;
    }
    ```

* The output of the above code is
    ```c++
    30
    20
    10
    ```
* The scope resolution operator (::) is used to refer to the global variable. It is used to tell the compiler that the variable that follows the operator (::) is a global variable.

* Lets take another example

    ```c++
    #include<iostream>
    using namespace std;
    int global = 10;
    void inner(){
        global++;
        cout<<global<<endl;
    }
    int local(){
        inner();
        int global = 20;
        global++;
        cout<<global<<endl;
    }
    int main(){
        cout<<global<<endl;
        local();
        cout<<global<<endl;
        return 0;
    }
    ```
* The output of the above code is
    ```c++
    10
    11
    21
    11
   ```
   - ### static scoping
        - Static scoping is also called lexical scoping. In this scoping, a variable always refers to its top-level environment. This is a property of the program text and is unrelated to the run-time call stack. Static scoping also makes it much easier to make a modular code as a programmer can figure out the scope just by looking at the code.
        ```c
        // A C program to demonstrate static scoping.
        #include<stdio.h>
        int x = 10;

        // Called by g()
        int f()
        {
        return x;
        }

        int g()
        {
        int x = 20;
        return f();
        }

        int main()
        {
        printf("%d", g());
        printf("\n");
        return 0;
        }
        
        ```
        - Output
        ```c
        10
        ```

   - ### dynamic scoping
        - dynamic scope requires the programmer to anticipate all possible dynamic contexts.
        ```c
        // Since dynamic scoping is not possible in c languages, we consider the 
        // following pseudo code as our example. It
        // prints 20 in a language that uses dynamic
        // scoping. 

        int x = 10;

        // Called by g()
        int f()
        {
        return x;
        }

        // g() has its own variable
        // named as x and calls f()
        int g()
        {
        int x = 20;
        return f();
        }

        main()
        {
        printf(g());
        }
        ```
       
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


- ## memory accessing for array
    - ### row major order 
    - ### column major order



why indexing is starts with 0 in place of 1

 
# Pointers

* A pointer is a variable that stores the address of another variable. Like any variable or constant, you must declare a pointer before using it to store any variable address. The general form of a pointer variable declaration is −

    ```c++
    type *var-name;
    ```
* Here, type is the pointer's base type; it must be a valid C++ type and var-name is the name of the pointer variable. The asterisk * used to declare a pointer is the same asterisk used for multiplication. However, in this statement the asterisk is being used to designate a variable as a pointer. Take a look at some of the valid pointer declarations −
    ```c
    int    *ip;
    ```
* The actual data type of the value of all pointers, whether integer, float, character, or otherwise, is the same, a long hexadecimal number that represents a memory address. The only difference between pointers of different data types is the data type of the variable or constant that the pointer points to.
* Null Pointers in C++

    * It is always a good practice to assign a NULL value to a pointer variable in case you do not have an exact address to be assigned. This is done at the time of variable declaration. A pointer that is assigned NULL is called a null pointer.
    * The NULL pointer is a constant with a value of zero defined in several standard libraries, including iostream. Consider the following program −

        ```c++
        #include <iostream>
        using namespace std;

        int main () {
            int  *ptr = NULL;

            cout << "The value of ptr is " << ptr ;

            return 0;
        }
        ```
    * When the above code is compiled and executed, it produces the following result −

        ```c++
        The value of ptr is 0
        ```
    * In most of the operating systems, programs are not permitted to access memory at address 0 because that memory is reserved by the operating system. However, the memory address 0 has special significance; it signals that the pointer is not intended to point to an accessible memory location. But by convention, if a pointer contains the null (zero) value, it is assumed to point to nothing.
    * To check for a null pointer, you can use an if statement as follows −

        ```c++
        if(ptr)     /* succeeds if p is not null */
        if(!ptr)    /* succeeds if p is null */
        ```
        - This type of if statement is used to check if a pointer is null or not. like if(ptr) will return true if ptr is not null and false if it is null.

## Arrays as Pointer

* Let us recall the concept of arrays and pointers. Consider the following array definition −

    ```c++
    double balance[50];
    ```
* Here, balance is a variable array which is sufficient to hold up to 50 double numbers. Here, we can think `balance` as a pointer pointing to the first element of the array `balance`. Therefore, *(balance + 4) is a valid expression which gives us the value of the 5th element stored in the array. Let us try to access array elements using pointer notation and array notation. The following program makes use of the concept −

    ```c++
    #include <iostream>
    using namespace std;

    int main () {
        double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};
        double *p;

        p = balance;

        // output each array element's value 
        cout << "Array values using pointer " << endl; 
        for ( int i = 0; i < 5; i++ ) {
            cout << "*(p + " << i << ") : ";
            cout << *(p + i) << endl;
        }

        cout << "Array values using balance as address " << endl;
        for ( int i = 0; i < 5; i++ ) {
            cout << "*(balance + " << i << ") : ";
            cout << *(balance + i) << endl;
        }

        return 0;
    }
    ```


* When the above code is compiled and executed, it produces the following result −

    ```c++
    Array values using pointer
    *(p + 0) : 1000
    *(p + 1) : 2
    *(p + 2) : 3.4
    *(p + 3) : 17
    *(p + 4) : 50
    Array values using balance as address
    *(balance + 0) : 1000
    *(balance + 1) : 2
    *(balance + 2) : 3.4
    *(balance + 3) : 17
    *(balance + 4) : 50
    ```
    ```c++
        cout<<bool(balance[1]==1[balance])<<endl;
        // will return 1 as both are same weahter we use balance[1] or 1[balance] as they are commutative in nature.

    ```
    * The size of element of array dipends on the type and compiler. For example in 32 bit compiler the size of int is 4 bytes and in 64 bit compiler the size of int is 8 bytes. So, the size of array will be 4* 5 = 20 bytes in 32 bit compiler and 8*5 = 40 bytes in 64 bit compiler.

    * Since Array is a continious block of memory so we can use pointer to access the array elements. so each element will take 4 bytes in 32 bit compiler and 8 bytes in 64 bit compiler. for example if array starts with address 1000 then the next element will be at 1002 in 16 bit compiler and 1004 in 32 bit compiler.

    
## Fucntion Pointers

```c++
#include<stdio.h>
int Add(int a, int b){
    return a+b;
}

int main(){
    int c;

    // making a funciton Pointer
    int (*p)(int,int);

    // Assigning to the variable
    p = &Add;
    c = (*p)(2,3); // de-refrencing and executing the function.
    printf("%d\n",c); 

    //or we can use
    p = Add;
    c = p(2,3);
    printf("%d",c);
    // both printf give same result
}
```

## Callbacks
when a refrence of  funciton is passed as an arguement to another function then that funciton is called as `callback` funciton
```c++
#include<stdio.h>

int A(){
    printf("hello world");
}
int B(void (*ptr)()){
    ptr();
}

int main(){
    
    B(A);
}
```

# 2D Array

A **two-dimensional array** is a collection of elements organized in rows and columns. It can be visualized as a table or a grid, where each element is accessed using two indices: one for the row and one for the column. Like a one-dimensional array, two-dimensional array indices also range from 0 to n-1 for both rows and columns  .

Here is an example of how to declare a 2D array in C++:

```c++
int arr[3][4];
```

This declares a 2D array `arr` with 3 rows and 4 columns. The size of the array is equal to the size of the data type multiplied by the total number of elements that can be stored in an array . We can calculate the total number of elements in an array by multiplying the size of each dimension of a multidimensional array . For example, the array `arr` can store a total of (3 x 4) = 12 elements.

We can initialize a 2D array using an initializer list in two ways. Below is the first method of initializing a 2D array using an initializer list:

```c++
int arr[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
```

This initializes the 2D array `arr` with the values 1 to 12. The first set of braces `{}` represents the rows, and the second set of braces `{}` represents the columns .
 
Sure, here is an example of a 2D array in tabular format:

| **Index** | **0** | **1** | **2** | **3** |
|-------|-----|-----|-----|-----|
| **0** | 1   | 2   | 3   | 4   |
| **1** | 5   | 6   | 7   | 8   |
| **2** | 9   | 10  | 11  | 12  |

This table represents a 2D array `arr` with 3 rows and 4 columns. The first row contains the values 1 to 4, the second row contains the values 5 to 8, and the third row contains the values 9 to 12. We can access any element of the array using its row and column indices. For example, $$arr_{1,2}$$ would return the value 7.

* Here is the same information in C++ code:

    ```c++
    #include <iostream>
    using namespace std;

    int main() {
        int arr[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

        // Accessing elements of the array
        cout << "The element at arr[1][2] is: " << arr[1][2] << endl;

        // Printing the array in tabular format
        cout << "\nTable representation of the array:\n";
        cout << "| **Index** | **0** | **1** | **2** | **3** |\n";
        cout << "|-------|-----|-----|-----|-----|\n";
        for (int i = 0; i < 3; i++) {
            cout << "| **" << i << "** |";
            for (int j = 0; j < 4; j++) {
                cout << " " << arr[i][j] << " |";
            }
            cout << "\n";
        }

        return 0;
    }
    ```

* Here is the Spyral travercing of the matrix

    ```c++
    #include<iostream>
    using namespace std;
    int main(){
    int n = 5,m =5;
    int arr[5][5] = {{1, 2, 3, 4, 5},
                {6, 7, 8, 9, 10},
                {11, 12, 13, 14, 15},
                {16, 17, 18, 19, 20},
                {21, 22, 23, 24, 25}};
                
    int row_start = 0, row_end = n-1, column_start = 0, column_end = m-1;
    while (row_start<=row_end && column_start<=column_end){

        // form left to right
        for(int i=column_start;i<=row_end;i++){
            cout<<arr[row_start][i]<<" ";
        }  
        row_start++;

        // from top to bottom
        for(int i = row_start; i<=column_end;i++){
            cout<<arr[i][column_end]<<" ";
        } 
        column_end--;

        // from right to left
        for(int i = column_end; i>=column_start;i--){
            cout<<arr[row_end][i]<<" ";
        }
        row_end--;

        // from bottom to top
        for (int i=row_end; i>=row_start;i--){
            cout<<arr[i][column_start]<<" ";
        }
        column_start++;
        
        }
        return 0;
    }

    ```

# Row Major Order

* In row-major order, the consecutive elements of a row reside next to each other, whereas the consecutive elements of a column reside far apart. This is because the elements of a row are stored in consecutive memory locations, whereas the elements of a column are stored in locations that are far apart. This is illustrated in the following figure:

![order](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Row_and_column_major_order.svg/300px-Row_and_column_major_order.svg.png)


* lets understand with an example

    ```c++
    #include<iostream>
    using namespace std;
    int main(){
        int arr[2][3] = {{1,2,3},{4,5,6}};
        cout<<arr<<endl;
        cout<<&arr[0][0]<<endl;
        cout<<arr[0]<<endl;
        cout<<&arr[0]<<endl;
        cout<<arr[1]<<endl;
        cout<<&arr[1]<<endl;
        cout<<arr[0]+1<<endl;
        cout<<&arr[0]+1<<endl;
        cout<<arr[1]+1<<endl;
        cout<<&arr[1]+1<<endl;
        return 0;
    }
    ```
    * The output of the
    ```c++
        0x61fef8
        0x61fef8
        0x61fef8
        0x61fef8
        0x61ff04
        0x61ff04
        0x61fefc
        0x61ff04
        0x61ff08
        0x61ff10
    ```
    * The output of the above code is the address of the first element of the array. The address of the first element of the array is the same as the address of the array itself.

* Address calculation in general
    * Fro `1D` Array

        * The address of an element in a `1D array` is calculated as follows:

            `address = base_address + (index - start_index * size_of_data_type)`

        * For example, the address of the 3rd element of an integer array with base address 1000 is calculated as follows:

            ```c++
            address = 1000 + (2 * 2) = 1004 //  for 16 bit compiler
            address = 1000 + (2 * 4) = 1008 //  for 32 bit compiler
            address = 1000 + (2 * 8) = 1016 //  for 64 bit compiler
            // i take 2 because it will be 3rd element.
            ```

        * another example: an array starts with index -5 to 5 and size of int is 10 bytes. then find the address of arr[2].
        
            ```c++
            address = 1000 + ((2 - (-5 ) * 10)) = 1070

        * another example: an array starts with index -10 to 10 and size of int is 8 bytes. then find the address of arr[3].
        
            ```c++
            address = 1000 + ((3 - (-10 ) * 8)) = 1104
            // by solving it we get 1000 +(3+10)*8 = 1000 + 13*8 = 1000 + 104 = 1104
            ```

    * For `2D` Array
    
        * The address of an element in a `2D array` is calculated as follows:

            `address = Base_Address + (((row_index - start_index) * number_of_columns) + column_index - start_index) * size_of_data_type`
            
        * For example, the address of the element $arr_{2,3}$ of a 2D array with base address 1000 is calculated as follows: (starting index assumed to be 0)

            ```c++ 
            address = 1000 + ((2 * 4) + 3) * 2 = 1018 //  for 16 bit compiler
            address = 1000 + ((2 * 4) + 3) * 4 = 1026 //  for 32 bit compiler
            address = 1000 + ((2 * 4) + 3) * 8 = 1042 //  for 64 bit compiler
            ```
        * another example: an array starts with index -5 to 5 and size of int is 10 bytes. then find the address of arr[2][3]. and dimension of array is 5*5.
        
            ```c++
            int address = 1000 + (((2 - (-5)) * 5) + 3 - (-5)) * 10 
            cout<<address<<endl;
            ```

        * it will give output:
            ```c++
            1070

            // explaination: 1000 + ((2+5)*5 + 3+5)*10 = 1000 + (7*5 + 8)*10 = 1000 + (35 + 8)*10 = 1000 + 43*10 = 1000 + 430 = 1430
            ```
<br>

## Recursion
   - Recursion is the technique of making a function call itself. This technique provides a way to break complicated problems down into simple problems which are easier to solve.
    ```c
    // C Program to calculate the sum of first N natural numbers using recursion
    #include <stdio.h> 

    int nSum(int n) 
    { 
        if (n == 0) { 
            return 0; 
        } 
        int res = n + nSum(n - 1); 

        return res; 
    } 

    int main() 
    { 
        int n = 5; 
        int sum = nSum(n); 

        printf("Sum of First %d Natural Numbers: %d", n, sum); 
        return 0; 
    }
    ```
   - 4 type are recursion are given below:
        - Tail Recursion
        - Non-Tail Recursion
        - Direct Recursion
        - Indirect Recursion
   - ## Tail Recursion
        - A recursive function is called the tail-recursive if the function makes recursive calling itself, and that recursive call is the last statement executes by the function. After that, there is no function or statement is left to call the recursive function.
        ```c
        #include <stdio.h>  
        void fun1( int num)  
        {  
            if (num == 0)  
                return;  
            else  
                printf ("\n Number is: %d", num);
            return fun1 (num - 1);     
        }  
        int main ()  
        {  
            fun1(7); 
            return 0;  
        }  
        ```
   - ## Non-Tail
        - A function is called the non-tail or head recursive if a function makes a recursive call itself, the recursive call will be the first statement in the function. It means there should be no statement or operation is called before the recursive calls. Furthermore, the head recursive does not perform any operation at the time of recursive calling. Instead, all operations are done at the return time.
        ```c
        #include <stdio.h>  
        void head_fun (int num)  
        {  
        if ( num > 0 )  
        {  
        head_fun (num -1);  
        printf (" %d", num);  
        }  
        }  
        int main ()  
        {  
        int a = 5;  
        printf (" Use of Non-Tail/Head Recursive function \n");  
        head_fun (a); 
        return 0;  
        }  
        ```

   - ## Direct Recursion
        - When a function calls itself within the same function repeatedly, it is called the direct recursion.
        ```c
        #include<stdio.h>  
        int fibo_num (int i)  
        {  
        if ( i == 0)  
        {  
        return 0;  
        }  
        if ( i == 1)  
        {  
        return 1;  
        }  
        return fibo_num (i - 1) + fibonacci (i -2);  
        }  
        int main ()  
        {  
        int i;  
        for ( i = 0; i < 10; i++)  
        {  
        printf (" %d \t ", fibo_num (i));  
        }  
        return 0;  
        }  
        ```
   - ## Indirect Recursion
        - When a function is mutually called by another function in a circular manner, the function is called an indirect recursion function.
        ```c
        #include <stdio.h>  
        void odd();  
        void even(); 
        int num = 1;   
        void odd ()  
        {     
            if (num <= 10)  
            {  
                printf (" %d ", num + 1);   
                num++;
                even();  
            }  
            return;  
        }  
        void even ()  
        {  
            if ( num <= 10)  
            {  
                printf (" %d ", num - 1); 
                num++;  
                odd(); 
            }  
            return;  
        }  
        int main ()  
        {  
            odd();
            return 0;  
        }  
        ```









# Object-Oriented Programming (OOP) Explained with C++
   - Object-Oriented Programming (OOP) is a programming paradigm centered around the concept of "objects" which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). In C++, OOP is implemented using classes and objects, with support for various features like overriding, overloading, runtime polymorphism, and compile-time polymorphism. Let's explore these concepts in detail:

## Classes and Objects
   - A class is a blueprint for creating objects. It defines the properties and behaviors that objects of that class will have. For example:
   ```cpp
    class Car {
        string brand;
        int year;

    public:
        void setBrand(string b) {
            brand = b;
        }

        void setYear(int y) {
            year = y;
        }
    };
   ```
   - An object is an instance of a class. It represents a specific instance of the class and can store data and perform operations defined by the class.

   ```cpp
    Car myCar; // Creating an object of type Car
    myCar.setBrand("Toyota");
    myCar.setYear(2022);
   ```

## Encapsulation
   - Encapsulation is the bundling of data and methods that operate on the data into a single unit, called a class. It hides the internal state of an object from the outside world and only exposes a public interface to interact with the object.

   ```cpp
    class Example {
    private:
        int x;

    public:
        void setX(int value) {
            x = value;
        }

        int getX() {
            return x;
        }
    };
   ```
## Inheritance
   - Inheritance is a mechanism in which a new class (derived class) is created from an existing class (base class). The derived class inherits properties and behaviors from the base class.

   ```cpp
    class Animal {
    public:
        void eat() {
            cout << "Eating...\n";
        }
    };

    class Dog : public Animal {
    public:
        void bark() {
            cout << "Barking...\n";
        }
    };
   ```
## Polymorphism
### Compile-Time Polymorphism (Function Overloading)
   - Compile-time polymorphism allows different functions to be called based on the number or types of arguments. This is achieved through function overloading.

   ```cpp
    class Math {
    public:
        int add(int a, int b) {
            return a + b;
        }

        float add(float a, float b) {
            return a + b;
        }
    };
   ```
### Runtime Polymorphism (Function Overriding)
   - Runtime polymorphism allows a function to behave differently based on the object that invokes it. This is achieved through virtual functions and function overriding.
   ```cpp
    class Shape {
    public:
        virtual void draw() {
            cout << "Drawing a shape\n";
        }
    };

    class Circle : public Shape {
    public:
        void draw() override {
            cout << "Drawing a circle\n";
        }
    };

    class Square : public Shape {
    public:
        void draw() override {
            cout << "Drawing a square\n";
        }
    };
   ```
## Operator Overloading
   - Operator overloading allows operators to be redefined for custom classes. This enables intuitive usage of operators with user-defined types.

   ```cpp
    class Complex {
        float real;
        float imag;

    public:
        Complex(float r, float i) : real(r), imag(i) {}

        Complex operator+(const Complex &other) {
            return Complex(real + other.real, imag + other.imag);
        }

        void display() {
            cout << real << " + " << imag << "i" << endl;
        }
    };
   ```

# File Handling in C++
   - File handling in C++ allows you to work with files on the system. It enables reading data from files, writing data to files, and performing various operations like opening, closing, deleting, and modifying files. Here's a detailed explanation of file handling in C++:

## File Streams
C++ provides three types of file streams:
- **ifstream**: Used for reading input from files.
- **ofstream**: Used for writing output to files.
- **fstream**: Can be used for both reading and writing.

- To use file streams, you need to include the `<fstream>` header file.

```cpp
#include <fstream>
```
## Opening and Closing Files
   - You can open files using the open() method of file streams. The open() method takes the file name and the mode in which you want to open the file (e.g., ios::in for input, ios::out for output, ios::app for appending, etc.).

   ```cpp
    ofstream outFile;
    outFile.open("example.txt", ios::out);

    if (!outFile.is_open()) {
        cout << "Error opening file!";
        return 1;
    }

    // Perform operations on the file

    outFile.close();
   ```
## Reading from Files
   - To read data from files, you can use the >> or getline() functions for formatted or line-based input, respectively.

   ```cpp
    ifstream inFile;
    inFile.open("input.txt", ios::in);

    if (!inFile.is_open()) {
        cout << "Error opening file!";
        return 1;
    }

    int num;
    inFile >> num; // Read an integer from the file

    string line;
    getline(inFile, line); // Read a line from the file

    // Perform operations with the read data

    inFile.close();
   ```
## Writing to Files
   - To write data to files, you can use the << operator for formatted output.

   ```cpp
    ofstream outFile;
    outFile.open("output.txt", ios::out);

    if (!outFile.is_open()) {
        cout << "Error opening file!";
        return 1;
    }

    int num = 10;
    outFile << num; // Write an integer to the file

    string text = "Hello, world!";
    outFile << text; // Write a string to the file

    // Perform other write operations

    outFile.close();
   ```
## Checking End-of-File (EOF)
   - You can use the eof() function to check whether you've reached the end of the file while reading.

   ```cpp
    ifstream inFile;
    inFile.open("data.txt", ios::in);

    if (!inFile.is_open()) {
        cout << "Error opening file!";
        return 1;
    }

    int num;
    while (!inFile.eof()) {
        inFile >> num;
        cout << num << " ";
    }

    inFile.close();
   ```
## Error Handling
   - Always check if the file operations (like opening or closing) were successful to avoid runtime errors.
