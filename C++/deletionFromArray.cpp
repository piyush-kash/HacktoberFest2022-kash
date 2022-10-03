// This is a program to delete an element after finding it. If no number found then it deletes the last element in the array.
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define ll long long
#define sc ;
#define tc ll t sc cin >> t sc while (t--)
#define ritik ios::sync_with_stdio(false)
#define spyder cin.tie(NULL)

int delet(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            int find = i;
            for (int j = find; j < n; j++)
                arr[j] = arr[j + 1];
        }
    }
    for (int i = 0; i < n - 1; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    ritik;
    spyder;
    int arr[] = {5, 6, 7, 8, 9};
    delet(arr, 5, 19);
    return 0;
}