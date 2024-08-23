def solution(rsp):
    answer = ''
    mode = {
        '2' : '0', '0' : '5', '5' : '2'
    }
    answer = ''.join(mode[m] for m in rsp)
    return answer