// Given an integer array of coins[ ] of size N representing different types of currency and an integer sum, 
// The task is to find the number of ways to make sum by using different combinations from coins[].  

#include<bits/stdc++.h>
using namespace std;
const int N = 1e3+1;
int t[N+1][N+1];
void knapsack(int arr[] , int n , int sum)
{
    for(int i=0 ; i<=n ; i++)
    {
        for(int j=0 ; j<=sum ; j++)
        {
            if(i==0 && j==0)
            {
                t[i][j] = 1;
            }
            else if(i==0)
            {
                t[i][j]=0;
            }
            else if(j==0)
            {
                t[i][j]=1;
            }
            else{
                if(arr[i-1]<=j)
                t[i][j] = t[i][j-arr[i-1]]+t[i-1][j];
                else{
                t[i][j] = t[i-1][j];
                }
            }
        }
    }
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    int sum = 0;
    for(int i=0 ; i<n ; i++){ cin>>arr[i];
    }
    cin>>sum;
    knapsack(arr,n,sum);
    cout<<t[n][sum];
}