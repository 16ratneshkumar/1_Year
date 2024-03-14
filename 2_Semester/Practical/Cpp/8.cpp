/*8. Create a Matrix class. Write a menu-driven program to perform following Matrix operations (exceptions should be thrown by the functions if matrices passed to them are incompatible and handled by the main() function):
a. Sum
b. Product
c. Transpose
*/
#include <iostream>
#include <vector>
using namespace std;

class Matrix {
private:
    int rows;
    int cols;
    vector<vector<int>> data;

public:
    Matrix(int r, int c) : rows(r), cols(c) {
        data.resize(rows, vector<int>(cols, 0));
    }

    void setElement(int i, int j, int value) {
        data[i][j] = value;
    }

    int getElement(int i, int j) const {
        return data[i][j];
    }

    int getRows() const {
        return rows;
    }

    int getCols() const {
        return cols;
    }

    Matrix sum(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw invalid_argument("Matrices are incompatible for sum operation");
        }

        Matrix result(rows, cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result.setElement(i, j, data[i][j] + other.getElement(i, j));
            }
        }
        return result;
    }

    Matrix product(const Matrix& other) const {
        if (cols != other.rows) {
            throw invalid_argument("Matrices are incompatible for product operation");
        }

        Matrix result(rows, other.cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < other.cols; ++j) {
                int sum = 0;
                for (int k = 0; k < cols; ++k) {
                    sum += data[i][k] * other.getElement(k, j);
                }
                result.setElement(i, j, sum);
            }
        }
        return result;
    }

    Matrix transpose() const {
        Matrix result(cols, rows);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result.setElement(j, i, data[i][j]);
            }
        }
        return result;
    }
};

int main() {
    int rows1, cols1, rows2, cols2;

    cout << "Enter the number of rows and columns for first matrix: ";
    cin >> rows1 >> cols1;
    Matrix mat1(rows1, cols1);
    cout << "Enter elements for first matrix:\n";
    for (int i = 0; i < rows1; ++i) {
        for (int j = 0; j < cols1; ++j) {
            int value;
            cin >> value;
            mat1.setElement(i, j, value);
        }
    }

    cout << "Enter the number of rows and columns for second matrix: ";
    cin >> rows2 >> cols2;
    Matrix mat2(rows2, cols2);
    cout << "Enter elements for second matrix:\n";
    for (int i = 0; i < rows2; ++i) {
        for (int j = 0; j < cols2; ++j) {
            int value;
            cin >> value;
            mat2.setElement(i, j, value);
        }
    }

    int choice;
    cout << "\nMenu:\n";
    cout << "1. Sum\n";
    cout << "2. Product\n";
    cout << "3. Transpose\n";
    cout << "Enter your choice: ";
    cin >> choice;

    try {
        switch (choice) {
            case 1: {
                Matrix result = mat1.sum(mat2);
                cout << "Sum of matrices:\n";
                for (int i = 0; i < result.getRows(); ++i) {
                    for (int j = 0; j < result.getCols(); ++j) {
                        cout << result.getElement(i, j) << " ";
                    }
                    cout << endl;
                }
                break;
            }
            case 2: {
                Matrix result = mat1.product(mat2);
                cout << "Product of matrices:\n";
                for (int i = 0; i < result.getRows(); ++i) {
                    for (int j = 0; j < result.getCols(); ++j) {
                        cout << result.getElement(i, j) << " ";
                    }
                    cout << endl;
                }
                break;
            }
            case 3: {
                Matrix result = mat1.transpose();
                cout << "Transpose of first matrix:\n";
                for (int i = 0; i < result.getRows(); ++i) {
                    for (int j = 0; j < result.getCols(); ++j) {
                        cout << result.getElement(i, j) << " ";
                    }
                    cout << endl;
                }
                break;
            }
            default:
                cout << "Invalid choice\n";
        }
    } catch (const invalid_argument& e) {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}
