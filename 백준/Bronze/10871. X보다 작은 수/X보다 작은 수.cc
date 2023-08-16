#include <iostream>
#include <string>
using namespace std;

int main(void){
    int n;
    int x;

    cin >> n >> x;
    int* ls = new int[n];
    for (int i =0; i < n; i++){
        cin >> ls[i];
    }

    for (int i=0; i < n;i++){
        if (ls[i] < x){
            cout << ls[i] << ' ';
        }
    }
    delete[] ls;
}