/*2.Write a program to remove the duplicates from an array.*/
#include <iostream>
#include <unordered_set>
using namespace std;

void removeDuplicates(int arr[], int& size) {
    unordered_set<int> unique;
    int index = 0;

    for (int i = 0; i < size; ++i) {
        if (unique.insert(arr[i]).second) {
            arr[index++] = arr[i];
        }
    }

    size = index;
}

int main() {
    int arr[] = {1, 2, 3, 4, 3, 2, 1, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    removeDuplicates(arr, size);

    cout << "Array after removing duplicates: ";
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
