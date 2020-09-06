#include <iostream>
using namespace std;

int main(void)
{
  int T, N;
  cin >> T;

  for (int t = 0; t < T; t++)
  {
    cin >> N;
    int arr[N];

    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 4;
    for (int i = 3; i < N; i++)
    {
      arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1];
    }
    cout << arr[N - 1] << endl;
  }

  return 0;
}