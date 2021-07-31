def solution(s):
    answer = True
    p = 0
    y = 0
    
    a = len(s)
    for i in range (a):
        if s[i] == "p" or s[i] == "P":
            p += 1
        elif s[i]=="y" or s[i] =="Y":
            y += 1
    if p==y:
        return True
    else:
        return False
