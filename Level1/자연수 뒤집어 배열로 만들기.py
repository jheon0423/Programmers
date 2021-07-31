def solution(n):
    answer = []
    n = str(n)
    a = len(str(n))
    for i in range(a-1,-1,-1):
        answer.append(int(n[i]))
    return answer
