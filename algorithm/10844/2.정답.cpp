#include <iostream>
using namespace std;

int main(void)
{
  int N;
  int arr1[10] = {0, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  int arr2[10] = {0, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  int result = 0;

  // for (int l = 0; l <= 9; l++)
  // {
  //   cout << arr1[l] << "\t";
  // }
  // cout << endl;

  cin >> N;
  for (int i = 1; i < N; i++)
  {
    arr2[0] = arr1[1];
    arr2[9] = arr1[8];
    for (int j = 1; j <= 8; j++)
    {
      arr2[j] = (arr1[j - 1] + arr1[j + 1]) % 1000000000;
    }
    for (int j = 0; j <= 9; j++)
    {
      arr1[j] = arr2[j];
    }
    // for (int l = 0; l <= 9; l++)
    // {
    //   cout << arr1[l] << "\t";
    // }
    // cout << endl;
  }
  for (int i = 0; i < 10; i++)
  {
    result = (result + arr1[i]) % 1000000000;
  }
  cout << result;

  return 0;
}