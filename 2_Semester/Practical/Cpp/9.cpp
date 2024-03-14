/*9. Define a class Person having name as a data member. Inherit two classes Student and Employee from Person. Student has additional attributes as course, marks and year and Employee has department and salary. Write display() method in all the three classes to display the corresponding attributes.Provide the necessary methods to show runtime polymorphism.*/

#include <iostream>
#include <string>
using namespace std;

class Person {
protected:
    string name;

public:
    Person(const string& n) : name(n) {}

    virtual void display() const {
        cout << "Name: " << name << endl;
    }
};

class Student : public Person {
private:
    string course;
    int marks;
    int year;

public:
    Student(const string& n, const string& c, int m, int y) : Person(n), course(c), marks(m), year(y) {}

    void display() const override {
        Person::display();
        cout << "Course: " << course << endl;
        cout << "Marks: " << marks << endl;
        cout << "Year: " << year << endl;
    }
};

class Employee : public Person {
private:
    string department;
    double salary;

public:
    Employee(const string& n, const string& d, double s) : Person(n), department(d), salary(s) {}

    void display() const override {
        Person::display();
        cout << "Department: " << department << endl;
        cout << "Salary: $" << salary << endl;
    }
};

int main() {
    Person* person1 = new Student("Alice", "Computer Science", 85, 2023);
    Person* person2 = new Employee("Bob", "Human Resources", 50000.0);

    cout << "Details of Person 1 (Student):\n";
    person1->display();

    cout << "\nDetails of Person 2 (Employee):\n";
    person2->display();

    delete person1;
    delete person2;

    return 0;
}
