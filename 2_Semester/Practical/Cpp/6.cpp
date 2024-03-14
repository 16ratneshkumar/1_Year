/*6. Write a program to search a given element in a set of N numbers using Binary search
 (i) with recursion (ii) without recursion.*/
#include <iostream>
using namespace std;

int binarySearchRecursive(int arr[], int low, int high, int target) {
    if (low > high) {
        return -1;
    }

    int mid = low + (high - low) / 2;
    if (arr[mid] == target) {
        return mid; 
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, mid + 1, high, target);
    } else {
        return binarySearchRecursive(arr, low, mid - 1, target);
    }
}

// Binary search without recursion
int binarySearchIterative(int arr[], int size, int target) {
    int low = 0, high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid; 
        } else if (arr[mid] < target) {
            low = mid + 1; 
        } else {
            high = mid - 1; 
        }
    }

    return -1;
}

int main() {
    int N, target;

    cout << "Enter the number of elements in the array: ";
    cin >> N;

    int arr[N];
    cout << "Enter " << N << " sorted elements:\n";
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    cout << "Enter the element to search: ";
    cin >> target;

    int indexRec = binarySearchRecursive(arr, 0, N - 1, target);
    if (indexRec != -1) {
        cout << "Element found at index (with recursion): " << indexRec << endl;
    } else {
        cout << "Element not found (with recursion)\n";
    }

    int indexIter = binarySearchIterative(arr, N, target);
    if (indexIter != -1) {
        cout << "Element found at index (without recursion): " << indexIter << endl;
    } else {
        cout << "Element not found (without recursion)\n";
    }

    return 0;
}
