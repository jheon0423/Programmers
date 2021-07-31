def solution(d, budget):
    answer = 0
    i = 0
    d.sort()
    while(True):
        if(answer == len(d) or budget<d[i]):
            break
        budget -= d[i]
        answer += 1
        i += 1
    return answer
