#include<iostream>
using namespace std;
int dividex(int x){
    if(x <= 1) return 0;
    int a = dividex(x/2) + x%2 + 1;
    int b = dividex(x/3) + x%3 + 1;
    return a < b ? a : b;
}
int main(){
    int N;
    cin >> N;
    cout << dividex(N);
    return 0;
}