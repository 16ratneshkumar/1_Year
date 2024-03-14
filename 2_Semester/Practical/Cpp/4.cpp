/*4. Write a menu driven program to perform string manipulation (without using inbuilt string functions):
a. Show address of each character in string
b. Concatenate two strings.
c. Compare two strings
d. Calculate length of the string (use pointers)
e. Convert all lowercase characters to uppercase
f. Reverse the string
g. Insert a string in another string at a user specified position*/
#include <iostream>
#include <cstring>
using namespace std;

void showAddress(const char* str) {
    cout << "Address of each character in the string:\n";
    for (int i = 0; str[i] != '\0'; ++i) {
        cout << "Character: " << str[i] << ", Address: " << static_cast<const void*>(&str[i]) << endl;
    }
}

void concatenateStrings(char* str1, const char* str2) {
    strcat(str1, str2);
    cout << "Concatenated string: " << str1 << endl;
}

int compareStrings(const char* str1, const char* str2) {
    return strcmp(str1, str2);
}

int stringLength(const char* str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return length;
}

void convertToLowercase(char* str) {
    for (int i = 0; str[i] != '\0'; ++i) {
        if (isupper(str[i])) {
            str[i] = tolower(str[i]);
        }
    }
    cout << "String in lowercase: " << str << endl;
}

void reverseString(char* str) {
    int length = strlen(str);
    for (int i = 0; i < length / 2; ++i) {
        char temp = str[i];
        str[i] = str[length - 1 - i];
        str[length - 1 - i] = temp;
    }
    cout << "Reversed string: " << str << endl;
}

void insertString(char* str, const char* insertStr, int position) {
    int length = strlen(str);
    int insertLength = strlen(insertStr);
    if (position < 0 || position > length) {
        cout << "Invalid position!\n";
        return;
    }

    // Make space for insertion
    for (int i = length; i >= position; --i) {
        str[i + insertLength] = str[i];
    }

    // Insert the string
    for (int i = 0; i < insertLength; ++i) {
        str[position + i] = insertStr[i];
    }

    cout << "String after insertion: " << str << endl;
}

int main() {
    char str1[100], str2[50], insertStr[50];
    int choice, position;

    cout << "Enter a string: ";
    cin.getline(str1, 100);

    do {
        cout << "\nMenu:\n";
        cout << "1. Show address of each character in string\n";
        cout << "2. Concatenate two strings\n";
        cout << "3. Compare two strings\n";
        cout << "4. Calculate length of the string\n";
        cout << "5. Convert all lowercase characters to uppercase\n";
        cout << "6. Reverse the string\n";
        cout << "7. Insert a string in another string at a user specified position\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                showAddress(str1);
                break;
            case 2:
                cout << "Enter second string to concatenate: ";
                cin.ignore(); // Clear input buffer
                cin.getline(str2, 50);
                concatenateStrings(str1, str2);
                break;
            case 3:
                cout << "Enter second string to compare: ";
                cin.ignore();
                cin.getline(str2, 50);
                if (compareStrings(str1, str2) == 0) {
                    cout << "Strings are equal\n";
                } else {
                    cout << "Strings are not equal\n";
                }
                break;
            case 4:
                cout << "Length of the string: " << stringLength(str1) << endl;
                break;
            case 5:
                convertToLowercase(str1);
                break;
            case 6:
                reverseString(str1);
                break;
            case 7:
                cout << "Enter string to insert: ";
                cin.ignore();
                cin.getline(insertStr, 50);
                cout << "Enter position to insert: ";
                cin >> position;
                insertString(str1, insertStr, position);
                break;
            case 8:
                cout << "Exiting program\n";
                break;
            default:
                cout << "Invalid choice! Please enter again.\n";
        }
    } while (choice != 8);

    return 0;
}
