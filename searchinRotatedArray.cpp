#include <iostream>
using namespace std;
int binarySearch(int arr[], int s, int e, int key)
{
    int start = s;
    int end = e;
    int mid = start + (end - start) / 2;
    while (start <= end)
    {
        if (arr[mid] == key)
        {
            return mid;
        }
        if (key > arr[mid])
        {
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
        mid = start + (end - start) / 2;
    }
    return -1;
}
int pivotElement(int arr[], int n)
{
    int s = 0, e = n - 1;
    int mid = s + (e - s) / 2;
    while (s < e)
    {
        if (arr[mid] >= arr[0])
        {
            s = mid + 1;
        }
        else
        {
            e = mid;
        }
        mid = s + (e - s) / 2;
    }
    return s;
}
int main()
{
    int arr[7] = {2, 2, 2, 3, 2, 2, 2};
    int n = 7;
    int key = 3;
    int pivot = pivotElement(arr, n);
    cout << pivot << endl;
    if (arr[pivot] <= key && key <= arr[n - 1])
    {
        cout << binarySearch(arr, pivot, n - 1, key);
    }
    else
    {
        cout << binarySearch(arr, 0, pivot - 1, key);
    }

    return 0;
}
