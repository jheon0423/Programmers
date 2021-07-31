def solution(n):
    answer = 0
    if n**0.5 == int(n**0.5):
        answer = int(n**0.5)
    if answer == 0:
        return -1
    else:
        return (answer+1)**2
