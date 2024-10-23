def solution(polynomial):
    number = 0  # 상수 항을 저장
    number_x = 0  # x 항의 계수를 저장
    result = []  # 최종 결과를 저장할 리스트
    
    # 다항식을 '+'로 분리하고 각 항목의 앞뒤 공백을 제거
    answer = polynomial.split('+')
    for i in answer:
        i = i.strip()  # 공백 제거
        if 'x' in i:
            # 'x'만 있는 경우 계수는 1로 처리
            if i == 'x':
                number_x += 1
            else:
                # '3x'와 같은 형식에서 숫자 부분을 추출하여 계수를 더함
                number_x += int(i.replace('x', ''))
        else:
            # 'x'가 없는 경우 상수 항으로 처리
            number += int(i)
    
    # 결과 리스트에 x 항 먼저 추가
    if number_x == 1:
        result.append('x')  # 계수가 1이면 'x'만 추가
    elif number_x != 0:
        result.append(f'{number_x}x')  # 계수가 1이 아니면 숫자와 함께 추가
    
    # 상수 항이 0이 아니면 상수 항을 추가
    if number != 0:
        result.append(str(number))
    
    # x 항이 있는 경우 숫자 뒤에 상수 항을 추가하고, 없는 경우 숫자만 반환
    return ' + '.join(result)

# 테스트 케이스
print(solution("3x + 7 + x"))  # 예상 결과: "4x + 7"
print(solution("x + x + x"))   # 예상 결과: "3x"
print(solution("7 + 3x"))      # 예상 결과: "3x + 7"
print(solution("x + 5"))       # 예상 결과: "x + 5"
