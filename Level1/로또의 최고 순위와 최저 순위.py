def solution(lottos, win_nums):
    answer = []
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    max = 7-count
    if max == 7:
        max = 6
    answer.append(max)
    count = 0
    for j in range(6):
        if lottos[j] == 0:
            lottos[j] = win_nums[1]
    for i in lottos:
        if i in win_nums:
            count += 1
    min = 7-count
    if min == 7:
        min = 6
    answer. append(min)

    answer.sort()
    return answer
