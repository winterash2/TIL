#include <iostream>

using namespace std;

// void print(int * arr){
//   for(int i = 0; i < len(arr); )
// }

void accumlate(int N, int *arr, int *result, int present){
  if(present >= N){
    return ;
  }
  
}

int main(void)
{
  int N;
  cin >> N;
  int arr[N];
  int result[N+2] = {0,};

  for (int i = 0; i < N; i++)
    cin >> arr[i];
  
  return 0;
}