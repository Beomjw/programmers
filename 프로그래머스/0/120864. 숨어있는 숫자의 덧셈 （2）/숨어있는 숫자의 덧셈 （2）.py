import re

def solution(my_string):
    # 정규 표현식을 사용하여 숫자를 모두 추출합니다.
    numbers = re.findall(r'\d+', my_string)
    
    # 추출된 숫자 문자열들을 정수로 변환한 뒤, 그 합을 반환합니다.
    return sum(map(int, numbers))
