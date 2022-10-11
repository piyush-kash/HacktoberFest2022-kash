#include <iostream>
using namespace std;

int sum(int n){
	
// 4 = 4+3+2+1 = 10

if(n==0){
	return 0;
}

int presum = sum(n-1);
return n + presum;


}

int main(){
	int n;
	cin>>n;
	
	cout << sum(n) ;
	
}
