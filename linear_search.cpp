#include <iostream>
using namespace std;
int main()
{
    int arr[20], n, find;
    bool ans;
    cout << "Enter no of elements in array : " << endl;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << "enter " << n << " elements : " << endl;
        cin >> arr[i];
    }
    cout << "Enter no which you want to search : " << endl;
    cin >> find;
    for (int j = 0; j < n; j++)
    {
        if (arr[j] == find)
        {
            ans = true;
            break;
        }
    }
    if (ans == true)
    {
        cout << find << " is present " << endl;
    }
    else
    {
        cout << find << " is not present there " << endl;
    }

    return 0;
}