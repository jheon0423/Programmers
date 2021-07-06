def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    left_flag=0 
    right_flag = 0

    for i in range(len(numbers)):
        if numbers[i]==0:
            numbers[i] = 11
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            left_flag = 0
            left = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            right_flag = 0
            right = numbers[i]
        else:
            if left_flag == 0 and right_flag == 0:
                if abs(numbers[i]+1 - right) > abs(numbers[i]-1 - left):
                    answer += 'L'
                    left_flag = 1
                    left = numbers[i]
                elif abs(numbers[i]+1 - right) < abs(numbers[i]-1 - left):
                    answer += 'R'
                    right_flag = 1
                    right = numbers[i]
                else:
                    if(hand == "right"):
                        answer += "R"
                        right_flag = 1
                        right = numbers[i]
                    else:
                        answer += "L"
                        left_flag = 1
                        left = numbers[i]
            elif left_flag == 0 and right_flag == 1:
                if abs(numbers[i] - right)/3 > abs(numbers[i]-1 - left)/3+1:
                    answer += 'L'
                    left_flag = 1
                    left = numbers[i]
                elif abs(numbers[i] - right)/3 < abs(numbers[i]-1 - left)/3+1:
                    answer += 'R'
                    right_flag = 1
                    right = numbers[i]
                else:
                    if(hand == "right"):
                        answer += "R"
                        right_flag = 1
                        right = numbers[i]
                    else:
                        answer += "L"
                        left_flag = 1
                        left = numbers[i]
            elif left_flag == 1 and right_flag == 0:
                if abs(numbers[i]+1 - right)/3+1 > abs(numbers[i] - left)/3:
                    answer += 'L'
                    left_flag = 1
                    left = numbers[i]
                elif abs(numbers[i]+1 - right)/3+1 < abs(numbers[i] - left)/3:
                    answer += 'R'
                    right_flag = 1
                    right = numbers[i]
                else:
                    if(hand == "right"):
                        answer += "R"
                        right_flag = 1
                        right = numbers[i]
                    else:
                        answer += "L"
                        left_flag = 1
                        left = numbers[i]
            else:
                if abs(numbers[i] - right) > abs(numbers[i] - left):
                    answer += 'L'
                    left_flag = 1
                    left = numbers[i]
                elif abs(numbers[i] - right) < abs(numbers[i] - left):
                    answer += 'R'
                    right_flag = 1
                    right = numbers[i]
                else:
                    if(hand == "right"):
                        answer += "R"
                        right_flag = 1
                        right = numbers[i]
                    else:
                        answer += "L"
                        left_flag = 1
                        left = numbers[i]
    return answer
