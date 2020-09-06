#include <iostream>
using namespace std;

int main(void)
{
  int N;
  int arr1[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  int arr2[10];
  int result = 0;
  cin >> N;

  // for (int j = 0; j < 10; j++)
  // {
  //   cout << arr1[j] << "\t";
  // }
  // cout << endl;

  for (int i = 1; i < N; i++)
  {
    for (int j = 0; j < 10; j++)
    {
      arr2[j] = 0;
      for (int l = 0; l <= j; l++)
      {
        arr2[j] = (arr2[j] + arr1[l]) % 10007;
      }
    }
    for (int j = 0; j < 10; j++)
    {
      arr1[j] = arr2[j];
    }
    // for (int j = 0; j < 10; j++)
    // {
    //   cout << arr1[j] << "\t";
    // }
    // cout << endl;
  }

  result = 0;
  for (int i = 0; i < 10; i++)
  {
    result = (result + arr1[i]) % 10007;
  }
  cout << result << endl;
  return 0;
}