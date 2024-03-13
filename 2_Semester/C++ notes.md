# **C ++**
C++ is a general-purpose programming language that was developed as an enhancement of the C language to include object-oriented paradigm. It is an imperative and a compiled language. 
## Why Learn C++?
- C++ is one of the most used and popular programming languages.
- C++ is used in making operating systems, embedded systems, and Graphical User Interfaces.
- It is an object-oriented programming language that implements all the OOPs concepts such as **Abstraction**, **Encapsulation**, and **Inheritance**, which gives a clear structure to programs and allows code to be reused, lowering development costs and providing security.
- It is portable and can be used to create applications that can be adapted to multiple platforms.
- C++ is easy to learn so that you can choose it as your first programming language.
- It makes programming easy for programmers to switch to C++ because its syntax is similar to C, Java, and C#.

## Features
- C++ is a high-level, general-purpose programming language designed for system and application programming. It was developed by Bjarne Stroustrup at Bell Labs in 1983 as an extension of the C programming language.
- One of the key features of C++ is its ability to support low-level, system-level programming, making it suitable for developing operating systems, device drivers, and other system software.
- C++ has a large, active community of developers and users, and a wealth of resources and tools available for learning and using the language. Some of the key features of C++ include:
- Object-Oriented Programming: C++ supports object-oriented programming, allowing developers to create classes and objects and to define methods and properties for these objects.
- Templates: C++ templates allow developers to write generic code that can work with any data type, making it easier to write reusable and flexible code.
- Standard Template Library (STL): The STL provides a wide range of containers and algorithms for working with data, making it easier to write efficient and effective code.
- Exception Handling: C++ provides robust exception handling capabilities, making it easier to write code that can handle errors and unexpected situations.

![image](https://github.com/Shantanu2911/Notes/assets/143939657/bd03ca38-c069-4ca1-8067-711acd4924ac)

## Advantages of C++ :
- Simple
- Machine Independent (Platform dependant)
- Mid-level language
- Rich library support
- Speed of execution
- Case-sensitive
- Dynamic Memory Allocation
- Memory Management
- Multi-threading
- Pointer and direct memory-access
- Object oriented
- Compiled Language

## Disadvantages of C++ :
- Steep Learning Curve
- Verbose Syntax
- Error-Prone

![image](https://github.com/Shantanu2911/Notes/assets/143939657/65c3f32f-cedb-446e-8e48-afb79d38bf7c)

## INSTALLATION
![image](https://github.com/Shantanu2911/Notes/assets/143939657/6f4b7cbb-dbbd-4a1a-92ea-4371567cc15a)

## First-Code in C++

```C++
// C++ Program to display "Hello, World!"
#include <iostream>
using namespace std;

int main()
{
   cout << "Hello, World!";

   return 0;
}

```
### **Output**

![image](https://github.com/Shantanu2911/Notes/assets/143939657/e399a4c4-f3f2-4609-a937-72a05ef4294d)

- **// C++ program to display “Hello World”** : This line is a comment line.
- **#include** : This is a preprocessor directive. #include<iostream> tells the compiler to include the standard iostream file which contains declarations of all the standard input/output library functions
- **using namespace std** : This is used to import the entity of the std namespace into the current namespace of the program. The statement using namespace std is generally considered a bad practice. When we import a namespace we are essentially pulling all type definitions into the current scope.The std namespace is huge. The alternative to this statement is to specify the namespace to which the identifier belongs using the scope operator(::) each time we declare a type. For example, std::cout.
- **int main() { }** : A function is a group of statements that are designed to perform a specific task. The main() function is the entry point of every C++ program, no matter where the function is located in the program.
- **cout<<“Hello World”;** : std::cout is an instance of the std::ostream class, that is used to display output on the screen. Everything followed by the character << in double quotes ” ” is displayed on the output device. The semi-colon character at the end of the statement is used to indicate that the statement is ending there.
- **return 0** : This statement is used to return a value from a function and indicates the finishing of a function. This statement is basically used in functions to return the results of the operations performed by a function.
- **Indentation** : We must always use indentations and comments to make the code more readable. 

## Basic of Syntax

![image](https://github.com/Shantanu2911/Notes/assets/143939657/646728ca-157c-4539-a75d-df6d015c7d6c)

- __Header File__ : The header files contain the definition of the functions and macros we are using in our program. They are defined on the top of the C++ program.

  Syntax :
  ```C++
  #include <library_name>
  ```

- **Namespace** : A namespace in C++ is used to provide a scope or a region where we define identifiers. It is used to avoid name conflicts between two identifiers as only unique names can be used as identifiers.

  Syntax :
  ```C++
  using namespace std;
  ```

- **Main Function** : The main function is the most important part of any C++ program. The program execution always starts from the main function. All the other functions are called from the main function. In C++, the main function is required to return some value indicating the execution status.

  Syntax :
  ```C++
  int main() {

    ... code ....
    return 0;
  }
  ```
- **Blocks** :  Blocks are the group of statements that are enclosed within { } braces. They define the scope of the identifiers and are generally used to enclose the body of functions and control statements.

  Syntax :
  ```C++
  {
      
  // Body of the Function
  
    return 0;
  }
  ```
  
 - **Semicolons** : It is used to terminate each line of the statement of the program. When the compiler sees this semicolon, it terminates the operation of that line and moves to the next line.

  Syntax :
  ```C++
 any_statement ;
  ```
## __DATATYPES__ :
- **PRIMITIVE**
    - __Integer__
        - Size - 4 bytes 
        - Eg : 1, 4, 100
        - Range [unsigned] (0 to 2<sup>32</sup> - 1)
        - Range [signed] (- 2<sup>31</sup> to 2<sup>31</sup> - 1) (using MSB(mosy significant bit) as sign)
          
          ![image](https://github.com/Shantanu2911/Notes/assets/143939657/358d8de3-0f2f-4f39-8b26-9be26616beb6)
          ![image](https://github.com/Shantanu2911/Notes/assets/143939657/0248531d-fcc0-43ee-a284-d9ddda62226d)

    - __Float__       Eg : 3.14, 6.5, 1.00
       -   Size - 4 byte
       -   __DOUBLE__ - Size 8 byte
          ![image](https://github.com/Shantanu2911/Notes/assets/143939657/69f0e715-270b-43c2-bffb-b4dc92291380)

    - __Character__
       - Size - 1 byte
       - Eg : c, f, @, %
         
           ![image](https://github.com/Shantanu2911/Notes/assets/143939657/bd17c299-bc10-42ee-a2d9-a70d3786623c)

    - __Booleam__
        - Eg : 0, 1
        - Size 1 byte

          ![image](https://github.com/Shantanu2911/Notes/assets/143939657/baed3ee7-47b3-43df-a7bd-6f8bf875660a)

_LETS TRY IT OUT :_
   ![image](https://github.com/Shantanu2911/Notes/assets/143939657/426f59b3-2445-451d-9700-8d4804971ced)
_OUTPUT :_
   ![image](https://github.com/Shantanu2911/Notes/assets/143939657/271745ec-f365-4ed5-a8da-f4a069b5344f)

### Type Modifiers : 
![image](https://github.com/Shantanu2911/Notes/assets/143939657/36df7c42-8f54-4e42-942d-4c6c0aea19ca)

- **DERIVED**
    - Function
    - Array
    - Pointer
    - Reference
- **USER-DEFINED**
    - Class
    - Structure
    - Union
    - Enum

## IF-ELSE Statement :
![image](https://github.com/Shantanu2911/Notes/assets/143939657/70ac596d-6a69-4cfb-a612-7383ff1c192d)

## LOOPS IN C++ :

### **For Loop :**
![image](https://github.com/Shantanu2911/Notes/assets/143939657/bfe55d05-daeb-46a7-b974-f48719c681df)

### **While Loop :**
![image](https://github.com/Shantanu2911/Notes/assets/143939657/0de6963b-cead-4dd7-8b95-0d8238ad7476)

### **Do While Loop :**
![image](https://github.com/Shantanu2911/Notes/assets/143939657/bfb74a3b-5447-4de7-8626-5600f43d7385)

### **Do While Loop V/s While Loop:**
![image](https://github.com/Shantanu2911/Notes/assets/143939657/d30cff12-45ec-4886-8902-750e4c85cb4a)

**Do while loop don't apply condition on the first count while, while loop does so**

## Break and Continue Statements in loops :

```C++
// To understancd the concept

#include <iostream>
using namespace std;

int main(){
    
   int pocketMoney = 3000; 
   for(int date=1;date<=30;date++){
    
    if(date%2==0){
        continue;
    }
    if (pocketMoney==0){
        break;
    }
    cout<<"Go out Today"<<endl;
    pocketMoney-=300;

   }
    return 0;
}
```

```C++
// To print prime numbers between two given numbers

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    for (int num = a; num <= b; num++) {
        int i;
        for (i = 2; i < num; i++) {
            if (num % i == 0) {
                break;
            }
        }
        if (i == num) {
            cout << num << endl;
        }
    }
    return 0;
}

```
## Switch-Case Statement

```C++
// multiple language robot
#include <iostream>
using namespace std;

int main() {

    char button;
    cout<<"Input a character";
    cin>>button;

    // if (button=='a'){
    //     cout<<"hello"<<endl;
    // }

    // else if (button=='b'){
    //     cout<<"namaste"<<endl;
    // }
    
    // else if (button=='c'){
    //     cout<<"hola amigo"<<endl;
    // }
    
    // else if (button=='d'){
    //     cout<<"salut"<<endl;
    // }
    
    // else if (button=='e'){
    //     cout<<"Ciao"<<endl;
    // }
    
    // else{
    //     cout<<"I am still learning more..."<<endl;
    // }

    switch(button){
        
        case 'a':
           cout<<"Hello"<<endl;
           break;

        case 'b':
           cout<<"Namaste"<<endl;
           break;
        
        case 'c':
           cout<<"Hola amigo"<<endl;
           break;
        
        case 'd':
           cout<<"Ciao"<<endl;
           break;
        
        case 'e':
           cout<<"Salut"<<endl;
           break;
        
        default:
        cout<<"I am still learning more!"<<endl;
           break;
    }

    return 0;
}
```

## __Operators in C++__
Operators are symbols that tell the computer to perform some specific operations.

- **Arithematic Operators** :
    - Binary Operators : (Done on two operands) +, -, *, /, %
    - Unary operator : (Done on only one operands) ++, --
       - Pre Incrementer (++a)
       - Post Incrementer (a++)
         ![image](https://github.com/Shantanu2911/Notes/assets/143939657/8722e684-af0f-45fe-bf2f-785826c1c8a5)
         ![image](https://github.com/Shantanu2911/Notes/assets/143939657/8a628026-657c-47d4-891f-93a4011694d0)

- **Relational Operators** :

  Defines a relation between 2 operands
  
  Returns a boolean Value
   (== , != , > , < , >= , <=)

- **Logical Operators** :
  
  && AND (works similar like gate operations)
  
  || OR (All values are true except **0**)

  ! NOT

- **Bitwise Operators** :
![image](https://github.com/Shantanu2911/Notes/assets/143939657/42a6a0bd-7f26-4229-ac0a-2139419b5f71)

- **Assignment Operators** :
   - (= , += , -= , *= , /=)
- **Miscellaneous Operators** :
   - Sizeof() : returns size of variable
   - __Condition?X:Y__ : also called (*Ternary Condtional Operator*)returns value of X if condition is true or else value of Y
   - cast : convert one datatype to another
   - Comma(,) : Causes a sequence of operations to be performed
   - & : (*Reference Operator*) Returns address of of a variable
   - \* : pointer to a variable

### Operators Precedence
![image](https://github.com/Shantanu2911/Notes/assets/143939657/c0f191d3-2f3b-4010-812d-549cea4e9288)

## Patterns In C++
```C++
//Reactangle pattern
#include <iostream>
using namespace std;

int main(){
    int rows,cols;
    cout<<"Enter the rows and columns"<<endl;
    cin>>rows>>cols;

    for(int i=1;i<=rows;i++){
        cout<<endl;
        for(int j=1;j<=cols;j++){
            cout<<"*";
        }
    }

    return 0;
}
```
```C++
//Hollow Reactangle pattern
#include <iostream>
using namespace std;

int main(){
    int rows,cols;
    cout<<"Enter the rows and columns"<<endl;
    cin>>rows>>cols;

    for(int i=1;i<=rows;i++){
        cout<<endl;
        for(int j=1;j<=cols;j++){
            if(i==1 || i==rows){
                cout<<"*";
            }
            else if(j==1 || j==cols){
                cout<<"*";
            }
            else{
                cout<<" ";
            }
        }
    } 

    return 0;
}

```
## **Functions in C++**:
Syntax
```C++
returnType functionName(parameter1,parameter2,....){
   //function body
}
```
![image](https://github.com/Shantanu2911/Notes/assets/143939657/dd6f338a-5a64-4dfc-be88-c968ec5c20c0)

## Array
Array is a list of similar datatypes.

<img src="https://github.com/Shantanu2911/Notes/assets/143939657/223656f5-545b-4df4-aeb9-36c209f0bdf2" width="75%" height="75%">

Syntax :
```C++
#include <iostream>
using namespace std;

int main(){

    int n;
    cin>>n;

    int array[n];
    for(int i=0;i<n;i++){
        cin>>array[i];
    }

    for(int i=0;i<n;i++){
        cout<<array[i]<<" ";
    }

    return 0;
}
```
## Pointers 
Pointers are variables that store the address of other variables.
<img src="https://github.com/Shantanu2911/Notes/assets/143939657/e010be4f-cab1-401e-960f-b28222b54339" width="75%" height="75%">
<img src="https://github.com/Shantanu2911/Notes/assets/143939657/a55978d9-cef0-4b9d-bad7-e6775b29fce6" width="75%" height="75%">

## Pointers and Arrays
```C++
#include <iostream>
using namespace std;

int main(){

    int arr[]={10,30,50};
    cout<<*arr<<endl;

    int* ptr = arr;
    for(int i=0;i<3;i++){
        cout<<*(arr+i)<<endl;
    }

}
```
## Pointers to Pointer
```C++
#include <iostream>
using namespace std;

int main(){

    int a=10;
    int* p;
    p = &a;
    cout << *p << endl;
    int**q = &p;
    cout << *q << endl;
    cout << **q << endl;

    return 0;

}
```
## Pointers Uses in Function
```C++
#include <iostream>
using namespace std;

void swap(int *a,int *b){
    int temp=*a;
    *a = *b;
    *b = temp;
}


int main(){

    int a=10;
    int b=5;

    swap(&a,&b);
    cout<<a<<" "<<b<<endl;

    return 0;

}
```
## __Strings__
<img src="https://github.com/Shantanu2911/Notes/assets/143939657/a910c6a7-4fd3-40d4-8fae-30e546d26fb2" width="70%" height="70%">

- String Declaration
```C++
#include <iostream>
#include <string>
using namespace std;

int main(){

    string str;
    getline(cin,str);
    cout<<str;
    string str1(5,'n');
    string str2 = "IamGay";

    cout<<str2;
    return 0;

}
```
- Concatenation of Strings
```C++
  #include <iostream>
#include <string>
using namespace std;

int main(){

    string str1 = "fam";
    string str2 = "ily";

    //str1.append(str2);
    cout<<str1 + str2<<endl;

    return 0;

}
```
- Indexing of Strings
```C++
#include <iostream>
#include <string>
using namespace std;

int main(){

    string str1 = "fam";
    string str2 = "ily";

    cout<<str1[2] + str2[0]<<endl;

    return 0;

}
```
- Functions of Strings
   - .clear( ) - clears the string
   - .compare( ) - show the difference between string
   - .empty( ) - check whether string is empty or not
   - .erase(start_index,characters to erase) - erase a specific part of string
   - .find( ) - finds a substring in a string
   - .insert(index, substring) - insert a substring in a string
   - .size( ) - finds size of string
   - .substr(startindex,no. of characters) - get a substring from a string
   - stoi( ) - changes string to integer
   - to_string( ) - changes integer to string
- Sorting in String
```C++
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(){

    string s1 = "qwertyuioasdfghjklzxcvbnm";
    
    sort(s1.begin(), s1.end());

    cout<<s1<<endl;

    return 0;

}
```

## Recursion
It is when a fuction call itself to make the problem smaller.
<img src="https://github.com/Shantanu2911/Notes/assets/143939657/ee53693a-391c-4a20-ae40-088579ee5a35" width="70%" height="70%">

```C++
#include <iostream>
using namespace std;

int factorial(int n){
    if(n==0){
        return 1;
    }

    int prevfact = factorial(n-1);
    return n*prevfact;

}

int main(){

    int n;
    cin>>n;

    cout<<factorial(n)<<endl;

    return 0;

}
```



