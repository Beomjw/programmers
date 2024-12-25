def solution(number, limit, power):
    answer = 0
    # 15의 약소 1, 3, 5, 15 (4개) -> 공격력이 4인 무기 구매
    # number = 5
    # limit = 3
    # power = 2
    # number = 5
    # 1부터 5까지의 약수의 개수
    # [1, 2, 2, 3, 2] 
    # limit = 3
    # power = 2
    # result 10
    
    result = []
    for n in range(1, number+1): # 1 2 3 4 5
        count = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        result.append(count)
    
    for i in range(len(result)):
        if result[i] > limit:
            result[i] = power
            
    return sum(result)