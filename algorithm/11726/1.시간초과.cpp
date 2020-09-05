#include<iostream>
using namespace std;

int count(int N){
    int term1, term2;
    if(N == 0)
        return 1;
    else if(N <= 0)
        return 0;
    term1 = count(N-1);
    term2 = count(N-2);
    return term1 + term2;
}

int main(void){
    int N;
    std::cin >> N;
    
    cout<< count(N) << endl;

    return 0;
}