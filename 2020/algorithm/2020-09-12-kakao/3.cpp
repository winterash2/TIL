#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<int> solution(vector<string> info, vector<string> query)
{
  vector<int> answer;
  vector<string>::iterator it;
  string arr_info[5][info.size()];
  string arr_query[8][query.size()];
  int size = 0;
  for (it = info.begin(), size = 0; it != info.end(); it++, size++)
  {
    stringstream ss(*it);
    string temp;
    int i = 0;
    while (getline(ss, temp, ' '))
    {
      arr_info[i][size] = temp;
      i++;
    }
    // cout << arr_info[0][size] << "\t" << arr_info[1][size] << "\t" << arr_info[2][size] << "\t" << arr_info[3][size] << "\t" << arr_info[4][size] << endl;
  }
  for (it = query.begin(), size = 0; it != query.end(); it++, size++)
  {
    stringstream ss(*it);
    string temp;
    int i = 0;
    while (getline(ss, temp, ' '))
    {
      arr_query[i][size] = temp;
      i++;
    }
    // cout << arr_query[0][size] << "\t" << arr_query[2][size] << "\t" << arr_query[4][size] << "\t" << arr_query[6][size] << "\t" << arr_query[7][size] << endl;
  }

  for(int i = 0; i < size; i++){
    
  }

  return answer;
}

int main(void)
{
  vector<string>::iterator it;
  vector<string> info;
  info.push_back("java backend junior pizza 150");
  info.push_back("python frontend senior chicken 210");
  info.push_back("python frontend senior chicken 150");
  info.push_back("cpp backend senior pizza 260");
  info.push_back("java backend junior chicken 80");
  info.push_back("python backend senior chicken 50");

  vector<string> query;
  query.push_back("java and backend and junior and pizza 100");
  query.push_back("python and frontend and senior and chicken 200");
  query.push_back("cpp and - and senior and pizza 250");
  query.push_back("- and backend and senior and - 150");
  query.push_back("- and - and - and chicken 100");
  query.push_back("- and - and - and - 150");

  solution(info, query);

  return 0;
}