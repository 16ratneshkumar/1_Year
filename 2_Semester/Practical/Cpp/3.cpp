/*3. Write a program that prints a table indicating the number of occurrences of each alphabet in the text entered as command line arguments.*/
#include <iostream>
#include <unordered_map>
#include <cctype> // For isalpha
using namespace std;

void printAlphabetFrequency(const string& text) {
    unordered_map<char, int> frequencyMap;

    // Count frequency of each alphabet
    for (char ch : text) {
        if (isalpha(ch)) {
            frequencyMap[tolower(ch)]++;
        }
    }

    // Print the table
    cout << "Alphabet Frequency Table:\n";
    for (char ch = 'a'; ch <= 'z'; ++ch) {
        cout << ch << ": " << frequencyMap[ch] << endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "Usage: " << argv[0] << " <text>" << endl;
        return 1;
    }

    string text = argv[1];
    printAlphabetFrequency(text);

    return 0;
}
