def solution(wallet, bill):
    answer = 0
    # 지갑의 크기 30 * 15
    # 지폐의 크기 26 * 17 -> 반으로 접으면 13 * 17
    
    while min(bill) > min(wallet) or max(bill) > max(wallet): 
        if bill[0] > bill[1]:  
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
            
    return answer