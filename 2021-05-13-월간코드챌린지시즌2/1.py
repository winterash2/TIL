def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer


print(solution(13, 17))

# n = 60;
# i =1;
# arr = []
# while(i*i <n):
#     if(n%i ==0):
#         arr.append(i);
#         arr.append(n/i);
#     i+=1
# n_arr = list(map(int, sorted(arr)))
