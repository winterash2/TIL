#include <iostream>
#include <string>
#include <vector>

using namespace std;

void gotodestination(int n, int prev, int present, int dest, int value, int arr[201][201], int result[201])
{
  result[present] = value + arr[prev][present];
  if (present == dest)
  {
    return;
  }
  else
  {
    value += arr[prev][present];
    for (int next = 1; next < n + 1; next++)
    {
      if (arr[present][next] != 0)
      {
        if ( ( (arr[present][next] + value) < result[next] ) || ( result[next] == 0) ){
          cout << "present: " << present << " next: " << next << endl;
          gotodestination(n, present, next, dest, value, arr, result);
        }
      }
    }
  }
}
void gotostart(int n, int start, int dest, int arr[201][201], int result[201]){
  for(int next; next < n+1; next++){
    if(arr[start][next] != 0){
      cout << "start: " << start << " next: " << next << endl;
      gotodestination(n, start, next, dest, 0, arr, result);
    }
  }
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares)
{
  int answer = 0;
  int result[201];
  int arr[201][201];
  for (int i = 0; i < n + 1; i++)
    for (int j = 0; j < n + 1; j++)
      arr[i][j] = 0;
  vector<vector<int>>::iterator it_i;
  vector<int>::iterator it_j;

  for (it_i = fares.begin(); it_i <= fares.end() && it_i != fares.end(); it_i++)
  {
    vector<int> fare = *it_i;
    int i = fare[0];
    int j = fare[1];
    int v = fare[2];
    arr[i][j] = v;
    arr[j][i] = v;
  }
  ///*
  for (int i = 0; i < n + 1; i++)
  {
    for (int j = 0; j < n + 1; j++)
    {
      cout << arr[i][j] << "\t";
    }
    cout << endl;
  }
  //*/

  for (int i = 0; i < n + 1; i++)
  {
    result[i] = 0;
  }
  gotostart(n, s, a, arr, result);
  int min_stoa = result[a];

  for (int i = 0; i < n + 1; i++)
  {
    result[i] = 0;
  }
  gotostart(n, s, b, arr, result);
  int min_stob = result[b];

  for (int i = 0; i < n + 1; i++)
  {
    result[i] = 0;
  }
  gotostart(n, a, b, arr, result);
  int min_atob = result[b];

  cout << "stoa" << min_stoa << endl;
  cout << "stob" << min_stob << endl;
  cout << "atob" << min_atob << endl;

  return answer;
}