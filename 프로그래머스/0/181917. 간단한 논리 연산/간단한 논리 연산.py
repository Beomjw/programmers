# V 연산자는 하나라도 T면 T다.
# ^ 연산자는 하나라도 F면 F다.

def solution(x1, x2, x3, x4):
    answer = True
    answer = (x1 or x2) and (x3 or x4)
    return answer