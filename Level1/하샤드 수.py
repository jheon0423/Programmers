def solution(x):
    answer = True
    num = 0
    y = str(x)
    length = len(y)
    for i in range(length):
        num += int(y[i])
    if (x%num != 0):
        return False
    return answer
