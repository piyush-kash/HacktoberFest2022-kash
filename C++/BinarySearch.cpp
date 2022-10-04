#include<bits/stdc++.h>
using namespace std;
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
void bubble(int arr[], int n)
{
    for(int i =0;i<n;i++)
    {
        for(int j = 0;j<n-i-1;j++)
        {
            if(arr[j]>arr[j+1])
                swap(arr[j],arr[j+1]);
        }
    }
}
int binary(int arr[], int l, int r, int x)
{
    while (l<=r)
    {
        int mid = (l+r)/2;
        if (arr[mid]==x)
            return mid;
        if(arr[mid]<x)
            l = mid +1;
        else 
            r = mid -1;
    }
    return -1;
}
int main()
{
    int n;
    cout <<"Enter the size of the array:";
    cin >>n;
    int arr[n];
    cout <<"Enter the elements of the array:";
    for(int i =0;i<n;i++)
    {
        cin>>arr[i];
    }
    cout<<"The elements of the array is:";
    for(int i =0;i<n;i++)
    {
        cout <<arr[i]<<" ";
    }
    bubble(arr, n);
    
    cout <<"\nArray after sorting:";
    for(int i =0;i<n;i++)
    {
        cout <<arr[i]<<" ";
    }
    int x;
    int r;
    cout <<endl;
    cout <<"Enter the value of the key:";
    cin >>x;
    int res = binary(arr, 0, n-1, x);
    if(res == -1)
        cout <<"Element is not present in array";
    else    
        cout<<"Element is present at "<<res<<" index in the array";
        
    return 0;
}
