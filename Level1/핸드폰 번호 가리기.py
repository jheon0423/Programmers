def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    answer = phone_number
    a = len(phone_number)
    for i in range(0,a-4):
        answer[i] = '*'
    answer = ''.join(answer)
    return answer
