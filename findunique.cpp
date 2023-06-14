#include <iostream>
using namespace std;

int uniqueFind(int arr[], int size)
{
    int ans = 0;
    for (int i = 0; i < size; i++)
    {
        ans = ans ^ arr[i]; // XOR 0 WITH ALL VALUES
    }
    return ans;
}
int main()
{
    int arr[5] = {1, 2, 1, 2, 3};
    int s = 5;
    cout << uniqueFind(arr, s);
    return 0;
}
