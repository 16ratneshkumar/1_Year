/*11. Create a class Student containing fields for Roll No., Name, Class, Year and Total Marks. Write a program to store 5 objects of Student class in a file. Retrieve these records from the file and display them.*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Student {
private:
    int rollNo;
    string name;
    string className;
    int year;
    int totalMarks;

public:
    Student() {}
    Student(int r, const string& n, const string& c, int y, int tm) : rollNo(r), name(n), className(c), year(y), totalMarks(tm) {}

    friend ostream& operator<<(ostream& os, const Student& student) {
        os << "Roll No.: " << student.rollNo << endl;
        os << "Name: " << student.name << endl;
        os << "Class: " << student.className << endl;
        os << "Year: " << student.year << endl;
        os << "Total Marks: " << student.totalMarks << endl;
        return os;
    }

    friend istream& operator>>(istream& is, Student& student) {
        is >> student.rollNo;
        is >> ws;
        getline(is, student.name);
        is >> ws;
        getline(is, student.className);
        is >> student.year;
        is >> student.totalMarks;
        return is;
    }
};

int main() {
    ofstream outFile("students.txt", ios::out | ios::binary);
    if (!outFile) {
        cerr << "Failed to open file for writing." << endl;
        return 1;
    }

    for (int i = 0; i < 5; ++i) {
        Student student;
        cin >> student;
        outFile.write(reinterpret_cast<const char*>(&student), sizeof(Student));
    }
    outFile.close();

    ifstream inFile("students.txt", ios::in | ios::binary);
    if (!inFile) {
        cerr << "Failed to open file for reading." << endl;
        return 1;
    }

    Student student;
    while (inFile.read(reinterpret_cast<char*>(&student), sizeof(Student))) {
        cout << student << endl;
    }
    inFile.close();

    return 0;
}
