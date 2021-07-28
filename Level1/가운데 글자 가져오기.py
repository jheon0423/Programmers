def solution(s):
    answer = ''
    l = len(s)
    a = int(l/2)
    s = list(s)
    if(l%2==1):
        answer = s[a]
    else:
        answer = s[a-1] + s[a]
    answer = ''.join(answer)
    return answer
