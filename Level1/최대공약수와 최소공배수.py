def solution(n, m):
    answer = []
    #최대공약수
    num = 0
    for i in range(1,max(n,m)+1):
        if n%i==0 and m%i==0:
            num = i
    answer.append(num)
    num = 0
    #최소공배수
    for i in range(m*n,min(n,m),-1):
        if(i%n == 0) and (i%m == 0):
            num = i
    answer.append(num)
    return answer
