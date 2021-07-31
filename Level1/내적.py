def solution(a, b):
    answer = 0
    q = len(a)
    for i in range (q):
        answer += a[i] * b[i]
    return answer
