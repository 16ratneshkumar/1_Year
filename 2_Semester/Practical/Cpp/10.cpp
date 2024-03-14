/*10. Create a Triangle class. Add exception handling statements to ensure the following conditions: all sides are greater than 0 and sum of any two sides are greater than the third side. The class should also have overloaded functions for calculating the area of a right angled triangle as well as using Heron's formula to calculate the area of any type of triangle.*/
#include <iostream>
#include <cmath>
#include <stdexcept>
using namespace std;

class Triangle {
private:
    double side1, side2, side3;

public:
    Triangle(double s1, double s2, double s3) : side1(s1), side2(s2), side3(s3) {
        if (side1 <= 0 || side2 <= 0 || side3 <= 0) {
            throw invalid_argument("All sides of the triangle must be greater than 0.");
        }
        if (side1 + side2 <= side3 || side1 + side3 <= side2 || side2 + side3 <= side1) {
            throw invalid_argument("Sum of any two sides must be greater than the third side.");
        }
    }

    double calculateArea() const {
        double s = (side1 + side2 + side3) / 2;
        return sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    double calculateArea(double base, double height) const {
        return 0.5 * base * height;
    }
};

int main() {
    try {
        double s1, s2, s3;
        cout << "Enter the lengths of the three sides of the triangle: ";
        cin >> s1 >> s2 >> s3;

        Triangle triangle(s1, s2, s3);

        double area;
        if (s1 * s1 + s2 * s2 == s3 * s3 || s1 * s1 + s3 * s3 == s2 * s2 || s2 * s2 + s3 * s3 == s1 * s1) {
            area = triangle.calculateArea(s1, s2);
            cout << "Area of the right-angled triangle: " << area << endl;
        } else {
            area = triangle.calculateArea();
            cout << "Area of the triangle using Heron's formula: " << area << endl;
        }
    } catch (const invalid_argument& e) {
        cerr << "Invalid triangle: " << e.what() << endl;
    }

    return 0;
}
