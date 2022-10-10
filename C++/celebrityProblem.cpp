#include <bits/stdc++.h>
#include <list>
using namespace std;
#define N 4

bool MATRIX[N][N] = { { 0, 0, 1, 0 },{ 0, 0, 1, 0 },{ 0, 0, 0, 0 },{ 0, 0, 1, 0 } };

bool knows(int A, int B)
{
    return MATRIX[A][B];
   
}

int findCelebrity(int n) {
   
    int celebrity = -1;
    for(int i = 0; i < n; i++) {
        bool knowAny = false, knownToAll = true;
        for(int j = 0; j < n; j++) {
            if(knows(i, j)) {
                knowAny = true;
                break;
            }
        }

        for(int j = 0; j < n; j++) {
            if(i != j and !knows(j, i)) {
                knownToAll = false;
                break;
            }
        }

        if(!knowAny && knownToAll) {
            celebrity = i;
            break;
        }
    }

    return celebrity;
}
int main()
{
int n = 4;
int id = findCelebrity(n);
id == -1 ? cout << "No celebrity" : cout << "Celebrity ID " << id;
return 0;
}
