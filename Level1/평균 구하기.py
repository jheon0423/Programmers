def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
    answer /= float(len(arr))
    return answer
