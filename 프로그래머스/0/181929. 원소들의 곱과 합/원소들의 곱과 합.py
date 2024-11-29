def solution(num_list):
    answer = 0
    sum = 0
    multi = 1
    for num in num_list:
        sum += num
        multi *= num
    
    if (sum*sum) > multi:
        return 1
    else:
        return 0