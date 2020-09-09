#include<cstdio>

int max(int a, int b){
  return a > b ? a : b;
}

int main(void)
{
  int T, N;
  scanf("%d", &T);

  for (int t = 0; t < T; t++)
  {
    scanf("%d", &N);
    int sticker[2][N + 1];

    sticker[0][0] = 0;
    sticker[1][0] = 0;
    for (int i = 0; i < 2; ++i)
    {
      for (int j = 1; j < N + 1; j++)
      {
        scanf("%d", &sticker[i][j]);
      }
    }
    for (int n = 2; n < N + 1; n++)
    {
      sticker[0][n] += max(sticker[1][n - 2], sticker[1][n - 1]);
      sticker[1][n] += max(sticker[0][n - 2], sticker[0][n - 1]);
    }
    // cout << "테이블 입력 테스트----------" << endl;
    // for (int i = 0; i < 2; ++i)
    // {
    //   for (int j = 0; j < N+1; j++)
    //   {
    //     cout << sticker[i][j] << "\t\t";
    //   }
    //   cout << endl;
    // }
    // cout << "---------------------------" << endl;
    printf("%d\n", max(sticker[0][N], sticker[1][N]));
  }

  return 0;
}
