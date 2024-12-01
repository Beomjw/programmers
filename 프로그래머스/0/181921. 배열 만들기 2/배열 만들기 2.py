def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(ch in '05' for ch in str(i)): 
            # str(i) 문자열 변환 505 -> '505'
            # str(505)의 경우 ch는 순차적으로 '5', '0', '5'
            # ch in '05' 현재 문자인 ch가 '0' 또는 '5' 중 하나인지 확인
            # ch in '05'는 True 또는 False를 반환
            # ch = '5'일때 True
            # ch = '1'일때 False
            # all str(505)인 경우 all([True, True, True]) True 반환
            # 하나라도 False인 경우 False 반환
            answer.append(i)
    
    if answer:
        return answer
    else:
        return [-1]