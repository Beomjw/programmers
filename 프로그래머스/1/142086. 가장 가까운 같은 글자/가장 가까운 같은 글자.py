def solution(s):
    answer = []
    last_seen = {}
    # "banana"
    # b 처음 -1
    # a 처음 -1
    # n 처음 -1
    # a 자신보다 두 칸 앞에 2
    # n 자신보다 두 칸 앞에 2
    # a 자신보다 두 칸 네 칸 앞에 있는데 그 중 가까운 거 2
    result = []
    for i, char in enumerate(s): # 012345 "banana" 
        if char not in last_seen:
            result.append(-1)
        else:
            result.append(i - last_seen[char]) # a는 3번째 last_seen[a]는 1번쨰 = 3 - 1 
        
        last_seen[char] = i # last_seen[a]에 3으로 갱신 {"b":0,"a":5,"n":4}
    
    return result