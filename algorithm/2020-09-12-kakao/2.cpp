#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string new_id)
{
  //string answer = "";
  vector<char> new_id_vector(new_id.begin(), new_id.end());
  vector<char>::iterator it;

  // 1단계
  for (it = new_id_vector.begin(); it != new_id_vector.end(); it++)
  {
    if (*it >= 65 && *it <= 90)
    {
      *it += 32;
    }
  }
  // 2단계
  for (it = new_id_vector.begin(); it <= new_id_vector.end() && it != new_id_vector.end();)
  {
    if (*it != 45 && *it != 46 && *it != 95)
    {
      if (*it <= 47 || (*it >= 58 && *it <= 96) || *it >= 123)
      {
        new_id_vector.erase(it);
        continue;
      }
    }
    it++;
  }
  //3단계
  bool check = false;
  if (!new_id_vector.empty())
  {
    for (it = new_id_vector.begin(); it <= new_id_vector.end() && it != new_id_vector.end();)
    {
      if (*it == '.')
      {
        if (!check)
          check = true;
        else
        {
          new_id_vector.erase(it);
          continue;
        }
      }
      else
        check = false;
      it++;
    }
  }
  //4단계
  if (!new_id_vector.empty())
  {
    if (new_id_vector.front() == '.')
      new_id_vector.erase(new_id_vector.begin());
    if (new_id_vector.back() == '.')
      new_id_vector.pop_back();
  }
  // 5단계
  if (new_id_vector.empty())
    new_id_vector.push_back('a');
  //6단계
  for (int i = new_id_vector.size(); i > 15; i--)
  {
    new_id_vector.pop_back();
  }
  if (new_id_vector.back() == '.')
    new_id_vector.pop_back();
  //7단계
  for (int i = new_id_vector.size(); i < 3; i++)
  {
    new_id_vector.push_back(new_id_vector.back());
  }

  string answer(new_id_vector.begin(), new_id_vector.end());
  cout << answer << endl;

  return answer;
}

int main(void)
{
  solution("...!@BaT#*..y.abcdefghijklm");
  solution("z-+.^.");
  solution("=.=");
  solution("123_.def");
  solution("abcdefghijklmn.p");

  return 0;
}