#include <iostream>
using namespace std;

int main(void)
{
  int N;
  int arr[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  cin >> N;

  for (int i = 0; i < N; i++)
  {
    for (int j = 1; j < 10; j++)
    {
      arr[j] = (arr[j] + arr[j - 1]) % 10007;
    }
  }
  cout << arr[9] << endl;
  return 0;
}