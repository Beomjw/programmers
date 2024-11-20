def solution(lottos, win_nums):
    answer = []
    # 인덱스 = 순위
    # [0, 1, 2, 3, 4, 5, 6]
    # 값 = 맞춘 개수
    rank = [6, 6, 5, 4, 3, 2, 1] 
    
    # 1 : 6개 번호가 모두 일치
    # 2 : 5개 번호 일치
    # 3 : 4개 번호 일치
    # 4 : 3개 번호 일치
    # 5 : 2개 번호 일치
    # 6 : 낙점
    
    matches = len(set(lottos) & set(win_nums))
    
    zeros = lottos.count(0)
    
    best_rank = rank[matches + zeros]
    worst_rank = rank[matches]
    
    return [best_rank, worst_rank]