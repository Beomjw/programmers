def solution(n, m, section):
    answer = 0
    # 페인트가 칠해진 길이 = n미터
    # 롤러의 길이 = m미터
    # n = 8
    # m = 4
    # [2, 3, 6]
    # 1234 5678 -> 2번
    
    # n = 5
    # m = 4
    # [1, 3]
    # 12345
    # 1234 -> 1번
    
    # n = 4
    # m = 1
    # [1, 2, 3, 4]
    # 4번
    current = 0
    
    for s in section: #[2, 3, 6]
        if s > current:
            answer += 1
            current = s + m - 1 # 2 + 4 - 1 = 5
    
    return answer