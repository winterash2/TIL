#include <iostream>
using namespace std;

int main(void)
{
  int N;
  cin >> N;
  int arr[N][2];

  arr[0][0] = 0;
  arr[0][1] = 1;
  for (int i = 1; i < N; i++)
  {
    arr[i][0] = arr[i - 1][0] + arr[i - 1][1];
    arr[i][1] = arr[i - 1][0];
  }
  // for (int i = 0; i < N; i++)
  // {
  //   cout << arr[i][0] << "\t\t" << arr[i][1] << "\t\t" << arr[i][0] + arr[i][1] << endl;
  // }
  cout << arr[N - 1][0] + arr[N - 1][1] << endl;

  return 0;
}