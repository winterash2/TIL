
# 정수들의 리스트가 입력으로 들어옵니다. 이 정수들의 리스트를 일부분만 잘라내어 모두 더했을 때의 값을 부분합이라 부릅니다. 이때 가장 큰 부분합을 구해봅시다.
# 예를 들어, [-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]이 입력으로 들어왔다면 [10, 5, -2, 17]을 모두 더한 30이 정답이 됩니다.
# ※입력에는 최소 하나 이상의 양수가 존재합니다.
# ※이 문제에는 여러 종류의 풀이법이 존재합니다. 각 풀이법의 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.

# def maxSubArray(nums): # 시간 초과됨
#     i = 0
#     sums = []
#     maxs = []
#     while i < len(nums):
#         sums.append(0)
#         maxs.append(0)
#         i += 1
#     i = 0
#     while i < len(nums):
#         j = 0
#         while j <= i:
#             sums[j] += nums[i]
#             if sums[j] > maxs[j]:
#                 maxs[j] = sums[j]
#             j += 1
#         i += 1
#     print(sums)
#     print(maxs)
#     max_sub = max(maxs)
#     return max_sub

def maxSubArray(nums):
    max_val = 0
    sum_val = 0
    for num in nums:
        sum_val = max(sum_val + num, num)
        if sum_val > max_val:
            max_val = sum_val
    return max_val

def main():
    # 30이 리턴되어야 합니다
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]))

main()
