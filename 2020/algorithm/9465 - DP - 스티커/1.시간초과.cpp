#include <iostream>
using namespace std;

int T, N, max_count;
int sticker[2][100000];

void countox(int n, int count);
void countxo(int n, int count);
void countxx(int n, int count);

int main(void)
{
  cin >> T;

  for (int t = 0; t < T; t++)
  {
    max_count = 0;

    cin >> N;

    for (int i = 0; i < 2; ++i)
    {
      for (int j = 0; j < N; j++)
      {
        cin >> sticker[i][j];
      }
    }
    // cout << "테이블 입력 테스트----------" << endl;
    // for (int i = 0; i < 2; ++i)
    // {
    //   for (int j = 0; j < N; j++)
    //   {
    //     cout << sticker[i][j] << "\t\t";
    //   }
    //   cout << endl;
    // }
    // cout << "---------------------------" << endl;

    countox(N - 1, 0);
    countxo(N - 1, 0);
    countxx(N - 1, 0);

    cout << max_count << endl;
  }

  return 0;
}

void countox(int n, int count)
{
  int ox, xo, xx;
  //cout << "ox n= " << n << "\t\tcount: " << count + sticker[0][n] << endl;
  if (n == 0)
  {
    if (max_count < (count + sticker[0][n]))
    {
      max_count = count + sticker[0][n];
      //cout << max_count << endl;
    }
  }
  else
  {
    countxo(n - 1, count + sticker[0][n]);
    countxx(n - 1, count + sticker[0][n]);
  }
}
void countxo(int n, int count)
{
  int ox, xo, xx;
  //cout << "xo n= " << n << "\t\tcount: " << count + sticker[1][n] << endl;
  if (n == 0)
  {
    if (max_count < (count + sticker[1][n]))
    {
      max_count = count + sticker[1][n];
      //cout << max_count << endl;
    }
  }
  else
  {
    countox(n - 1, count + sticker[1][n]);
    countxx(n - 1, count + sticker[1][n]);
  }
}
void countxx(int n, int count)
{
  int ox, xo, xx;
  //cout << "xx n= " << n << "\t\tcount: " << count << endl;
  if (n == 0)
  {
    return;
  }
  else
  {
    countox(n - 1, count);
    countxo(n - 1, count);
    countxx(n - 1, count);
  }
}