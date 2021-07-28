def solution(nums):
    answer = 0
    total_num = len(nums)
    nums= list(set(nums))
    second_num = len(nums)
    if(total_num/2 < second_num):
        answer = int(total_num/2)
    else:
        answer = second_num
    return answer

nums = [1,2,3,3]
print(solution(nums))
