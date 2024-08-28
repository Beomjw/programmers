def solution(sides):
    # 두 변을 오름차순으로 정렬
    a, b = sorted(sides)
    
    # 나머지 한 변이 될 수 있는 범위
    min_x = b - a + 1  # x > b - a 인 경우
    max_x = a + b - 1  # x < a + b 인 경우
    
    # 가능한 정수의 개수는 max_x - min_x + 1
    return max_x - min_x + 1
