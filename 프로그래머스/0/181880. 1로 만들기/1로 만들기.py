def solution(num_list):
    answer = 0

    for n in num_list:
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = (n - 1) // 2
        answer += count
        
    return answer