def solution(n):
    answer = 0
    n = str(n)
    a = len(n)
    
    for i in range(a):
        answer += int(n[i])

    return answer
