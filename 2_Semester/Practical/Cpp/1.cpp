/*Write a program to compute the sum of the first n terms of the following series:
Sum=1-1/2²+1/3³-
The number of terms n is to be taken from the user through the command line. If the command line argument is not found then prompt the user to enter the value of n.*/
#include <iostream>
#include <cmath>
using namespace std;
int Sum(int n)
{
    float sum;
    for (int i=1;i<n+1;i++)
    {
        sum+=pow(-1,i+1)/pow(i,i);
    }
    cout<<"Your Output Is:: "<<sum<<endl;
}
int main()
{
	int x;
	cout<<"Enter Your Number:: ";
	cin>>x;
	Sum(x);
	return 0;
}