//Josephus Problem
// It can be explained as
//There are N people standing in a circle numbered from 1 to N. Also given an integer K. 
//First, count the K-th number starting from the first one and delete it.
//Then K numbers are counted starting from the next one and the K-th one is removed again, and so on.
//The process stops when one number remains. The task is to find the last number.

#include<iostream>
#include<bits/stdc++.h>

#define vi vector<int>
#define vs vector<string>
#define vc vector<char>
#define vvi vector<vi>
#define pii pair<int,int>
#define rep(i,n) for(int i=0;i<n;i++)
#define repi(i,a,b) for(int i=a;i<b;i++)
#define ff first
#define ss second

using namespace std;
void Josh(vector < int > person, int k, int index) {
  if (person.size() == 1) {
    cout << person[0] << endl;
    return;
  }
  index = ((index + k) % person.size());
  person.erase(person.begin() + index);
  Josh(person, k, index);
}
int main(){
	int n ,k;
	cin>>n>>k;
	k--;
	int index=0;
  vector < int > person;
  for (int i = 1; i <= n; i++) {
    person.push_back(i);
  }
 
  Josh(person, k, index);
}


