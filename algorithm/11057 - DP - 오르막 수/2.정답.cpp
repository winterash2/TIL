#include <iostream>
using namespace std;

int main(void)
{
  int N;
  int arr[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  int result = 0;
  cin >> N;

  for (int i = 1; i < N; i++)
  {
    for (int j = 1; j < 10; j++)
    {
      arr[j] = (arr[j] + arr[j - 1]) % 10007;
    }
  }

  result = 0;
  for (int i = 0; i < 10; i++)
  {
    result = (result + arr[i]) % 10007;
  }
  cout << result << endl;
  return 0;
}