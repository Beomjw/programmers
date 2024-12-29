def solution(N, stages):
    answer = []
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    # N = 5 (스테이지의 개수)
    # [2, 1, 2, 6, 2, 4, 3, 3] 현재 멈춰있는 스테이지의 번호
    # 1 스테이지 실패율 1 / 8
    # 2 스테이지 실패율 3 / 7
    # 3 스테이지 실패율 2 / 4
    # 4 스테이지 실패율 1 / 2
    # 5 스테이지 실패율 0 / 1
    
    # 실패율 내림차순 [3, 4, 2, 1, 5]
    
    # N = 4 (스테이지의 개수)
    # [4,4,4,4,4]
    # 1 스테이지 실패율 5 / 5
    # 2 스테이지 실패율 5 / 5
    # 3 스테이지 실패율 5 / 5
    # 4 스테이지 실패율 0 / 5
    
    # 실패율 내림차순 [4, 1, 2, 3]
    
    fail_rate = []
    players = len(stages) # 8
    
    for stage in range(1, N+1): # 1 2 3 4 5
        count1 = stages.count(stage)
        
        if players > 0:
            rate = count1 / players
            fail_rate.append((stage, rate))
            players -= count1
        else:
            fail_rate.append((stage, 0))
            
    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    # 실패율을 내림차순 -> 실패율이 같으면 stage 번호 오름차순
    stage_list = list(map(lambda x: x[0], fail_rate))
    
    return stage_list