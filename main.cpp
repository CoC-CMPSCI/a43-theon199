// Make a program that finds the minimum value among three integer values.

#include <iostream>
using namespace std;
int main()
{
    int num1, num2, num3;
    int min;
    cin >> num1 >> num2 >> num3;

    // TODO: Find the smallest value among three values
    min = num1;
    if (num2 < min)
        min = num2;
    if (num3 < min)
        min = num3;
    // END TODO

    // Use the following statements to print output
    cout << "The smallest number is  " << min << endl;
}
