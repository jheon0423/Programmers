def solution(numbers):
    a = len(numbers)
    answer = []
    for i in range(a):
        for j in range(i+1,a):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
