'''
가장 큰 두 수의 차
0보다 큰 정수들의 배열이 주어졌다고 합시다. 여기서 가능한 모든 서로 다른 두 숫자의 차이를 고려 해 보고, 이중 가장 큰 차이를 반환하는 함수를 적어봅시다. 예를 들어서, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 가 입력으로 주어졌을 경우 가장 큰 차이를 내는 숫자쌍은 50-1 = 49 입니다.

두 수의 차에 해당하는 값을 반환하면 됩니다. 위 예시의 경우, 49를 반환합니다.
양의 값을 반환해야 합니다. 위 예시의 경우 -49가 아니라 49를 반환해야 합니다.
배열의 길이는 2보다 크거나 같다고 가정합니다.
이 문제에는 여러 종류의 풀이법이 존재합니다. 각 풀이법의 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.
'''
# TODO sort는 시간복잡도가 높음


# def maxTwoDiff(nums):
#     nums.sort()
#     min = nums[0]
#     max = nums[len(nums)-1]
#     return max - min
    
# def maxTwoDiff(nums):
#     max=min=nums[0]
#     for num in nums:
#         if num < min:
#             min = num
#         elif num > max:
#             max = num
#     return max - min

def maxTwoDiff(nums):
    return max(nums) - min(nums)

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
