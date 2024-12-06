def solution(num_list):
    answer = 0
    for num in range(len(num_list)):
        if num_list[num] < 0:
            return num
    return -1