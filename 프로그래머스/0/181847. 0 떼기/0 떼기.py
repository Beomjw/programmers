def solution(n_str):
    answer = ''
    # "0010"
    # 0
    # 0
    # 1
    # 0
    for n in n_str:
        if n != '0' or answer:
            answer += n
            
    return answer