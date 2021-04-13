import sys
input = sys.stdin.readline

N = int(input())
peoples = []
for i in range(N):
    age, name = input().split()
    peoples.append((int(age), i, name))
peoples.sort()
for person in peoples:
    print(person[0], person[2])
