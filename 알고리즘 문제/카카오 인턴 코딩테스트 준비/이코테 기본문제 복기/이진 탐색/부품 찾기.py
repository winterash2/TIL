import bisect

N = int(input())
stocks = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

stocks.sort()
orders.sort()

for order in orders:
    idx = bisect.bisect_left(stocks, order)
    # print(stocks, order, idx, end=" ")
    if stocks[idx] != order:
        print("no", end=" ")
    else:
        print("yes", end=" ")

"""
5
8 3 7 9 2
3 
5 7 9
"""
