/*7. Write a program to calculate GCD of two numbers (i) with recursion (ii) without
recursion.*/
#include <iostream>
using namespace std;

int gcdRecursive(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcdRecursive(b, a % b);
    }
}

int gcdIterative(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int num1, num2;

    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    int gcdRec = gcdRecursive(num1, num2);
    cout << "GCD of " << num1 << " and " << num2 << " (with recursion): " << gcdRec << endl;

    int gcdIter = gcdIterative(num1, num2);
    cout << "GCD of " << num1 << " and " << num2 << " (without recursion): " << gcdIter << endl;

    return 0;
}

