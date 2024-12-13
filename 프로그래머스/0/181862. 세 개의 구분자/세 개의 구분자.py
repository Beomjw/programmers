def solution(myStr):
    # a b c가 아닌 문자만 출력
    answer = myStr.split('a')
    
    result = []
    for a in answer:
        b = a.split('b')
        result.extend(b)
    
    result2 = []
    for r in result:
        c = r.split('c')
        result2.extend(c)
    
    result3 = []
    for r in result2:
        if r:
            result3.append(r)
    
    if result3:
        return result3
    else:
        return ["EMPTY"]
