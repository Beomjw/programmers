def solution(k, m, score):
    answer = 0
    # 최상품 사과 = k점
    # 한 상자에 담길 사과의 개수 = m
    # k = 3
    # m = 4
    # score = [1,2,3,1,2,3,1]
    # [2, 3, 2, 3]
    # 최저 사과 점수 * 한 상자에 담긴 사과 개수 * 상자의 개수
    # 2 * 4 * 1 = 8
    
    # k = 4
    # m = 3
    # score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
    # [4, 4, 4], [4, 4, 4], [2, 2, 2], [1, 1, 2]
    # 최저 사과 점수 * 한 상자에 담긴 사과 개수 * 상자의 개수
    # (4 * 3) + (4 * 3) + (2 * 3) + (1 * 3) = 33
    l = len(score) # 7
    score.sort(reverse=True) # [3, 3, 2, 2, 1, 1, 1]
    box_count = l // m
    box = [score[i:i+m] for i in range(0, len(score), m)] # index = [[0, 1, 2, 3]], [4, 5, 6]]
    b = box[:box_count]
    s = 0
    for j in b:
        s += min(j) * m
    return s