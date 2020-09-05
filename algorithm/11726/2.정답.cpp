#include <iostream>
using namespace std;

int main(void)
{
    int N;
    std::cin >> N;

    int *arr = new int[N];

    arr[N - 1] = 1;
    arr[N - 2] = 2;
    for (int i = N - 3; i >= 0; i--)
    {
        arr[i] = (arr[i + 1] + arr[i + 2]) % 10007;
    }
    // for(int i = N-1; i >= 0; i--){
    //     cout << arr[i] << endl;
    // }
    cout << arr[0] << endl;

    return 0;
}