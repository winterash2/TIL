#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

string solution(string play_time, string adv_time, vector<string> logs)
{
  int adv_time_int;
  int total[370001] = {0,};
  //string answer = "";
  cout << "----------------------" << endl;
  {
    vector<string> adv_time_vector;
    stringstream ss(adv_time);
    string temp;
    int i = 0;
    while (getline(ss, temp, ':'))
    {
      i++;
      if (i == 3)
      {
        stringstream sss(temp);
        string ttemp;
        while (getline(sss, ttemp, '-'))
        {
          adv_time_vector.push_back(ttemp);
        }
      }
      else
      {
        adv_time_vector.push_back(temp);
      }
    }
    adv_time_int = stoi(adv_time_vector[0]) * 3600 + stoi(adv_time_vector[1]) * 60 + stoi(adv_time_vector[2]);
  }
  
  vector<string>::iterator it;
  for (it = logs.begin(); it != logs.end(); it++)
  {
    string log = *it;
    vector<string> log_vector;

    { // 로그 :이랑 -로 떼기
      stringstream ss(log);
      string temp;
      int i = 0;
      while (getline(ss, temp, ':'))
      {
        i++;
        if (i == 3)
        {
          stringstream sss(temp);
          string ttemp;
          while (getline(sss, ttemp, '-'))
          {
            log_vector.push_back(ttemp);
          }
        }
        else
        {
          log_vector.push_back(temp);
        }
      }
    }
    int start = stoi(log_vector[0]) * 3600 + stoi(log_vector[1]) * 60 + stoi(log_vector[2]);
    int end = stoi(log_vector[3]) * 3600 + stoi(log_vector[4]) * 60 + stoi(log_vector[5]);
    for (int i = start; i <= end; i++)
    {
      total[i] += 1;
    }
  }

  cout << "----------------------" << endl;
  
  int sum = 0;
  int sum_arr[370001] = {0,};
  int max = sum;
  for (int i = 0; i < adv_time_int; i++)
  {
    sum = sum + total[i];
  }
  sum_arr[0] = sum;
  for (int i = 1; i < 360000; i++)
  {
    sum_arr[i] = sum_arr[i - 1] + total[adv_time_int + i - 1];
    if (sum_arr[i] > max)
      max = sum_arr[i];
  }
  string answer = "";
  answer += to_string(max / 3600);
  answer += ':';
  answer += to_string((max % 3600) / 60);
  answer += ':';
  answer += to_string((max % 3600) % 60);
  cout << answer << endl;

  return answer;
}


// int main(void){
//   string play_time = "02:03:55";
//   string adv_time = "00:14:15";
//   vector<string> logs;
//   logs.push_back("01:20:15-01:45:14");
//   logs.push_back("00:40:31-01:00:00");
//   logs.push_back("00:25:50-00:48:29");
//   logs.push_back("01:30:59-01:53:29");
//   logs.push_back("01:37:44-02:02:30");

//   solution(play_time, adv_time, logs);
// }