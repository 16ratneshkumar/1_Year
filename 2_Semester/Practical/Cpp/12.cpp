/*12.. Copy the contents of one text file to another file, after removing all whitespaces*/

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string inputFile, outputFile;

    cout << "Enter the name of the input file: ";
    getline(cin, inputFile);

    cout << "Enter the name of the output file: ";
    getline(cin, outputFile);

    ifstream inFile(inputFile);
    if (!inFile) {
        cerr << "Failed to open input file." << endl;
        return 1;
    }

    ofstream outFile(outputFile);
    if (!outFile) {
        cerr << "Failed to open output file." << endl;
        inFile.close();
        return 1;
    }

    char ch;
    while (inFile.get(ch)) {
        if (!isspace(ch)) {
            outFile.put(ch);
        }
    }

    cout << "Contents copied to " << outputFile << " after removing whitespaces." << endl;

    inFile.close();
    outFile.close();

    return 0;
}

