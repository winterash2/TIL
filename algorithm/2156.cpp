#include <iostream>

using namespace std;

void accumlate(int N, int *arr, int *result, int present){
  if()
}

int main(void)
{
  int N;
  cin >> N;
  int arr[N];
  int result[N+2];

  for (int i = 0; i < N; i++)
    cin >> arr[i];
  
  result[0] = arr[0];
  result[1] = arr[0] > arr[1] ? arr[0] : arr[1];

  return 0;
}