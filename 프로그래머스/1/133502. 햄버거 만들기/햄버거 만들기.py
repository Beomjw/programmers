def solution(ingredient):
    answer = 0
    # 빵 야채 고기 빵
    # 1 2 3 1
    
    hamburger = [1, 2, 3, 1]
    stack = []
    for i in ingredient: # [2, 1, 1, 2, 3, 1, 2, 3, 1]
        stack.append(i)
        
        if stack[-4:] == hamburger:
            for _ in range(4): # 4번 반복
                stack.pop()
            answer += 1
    return answer