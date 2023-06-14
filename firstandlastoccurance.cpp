#include <iostream>
using namespace std;
int firstOccurance(int arr[], int n, int k)
{
    int s = 0, e = n;
    int m = s + (e - s) / 2;
    int ans = -1;
    while (s <= e)
    {

        if (k == arr[m])
        {
            ans = m;
            m = s + 1;
        }
        else if (k < arr[m])
        {
            e = m - 1;
        }
        else
        {
            s = m + 1;
        }
        m = s + (e - s) / 2;
    }
    return ans;
}
int lastOccurance(int arr[], int n, int k)
{
    int s = 0, e = n;
    int m = s + (e - s) / 2;
    int ans = -1;
    while (s <= e)
    {

        if (k == arr[m])
        {
            ans = m;
            s = m + 1;
        }
        else if (k < arr[m])
        {
            e = m - 1;
        }
        else
        {
            s = m + 1;
        }
        m = s + (e - s) / 2;
    }
    return ans;
}
int main()
{
    int arr[5] = {1, 3, 3, 4, 5};
    cout << "first occurance is at index  : " << firstOccurance(arr, 5, 3) << endl;
    cout << "last occurance is at index  : " << lastOccurance(arr, 5, 3) << endl;
    return 0;
}