def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        a = min(arr)
        arr.remove(a)
    return arr
