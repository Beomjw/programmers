def solution(n):
    if n == 1:
        return [[1]]
    answer = [[0 for j in range(n)] for i in range(n)]
    # [[1, 2, 3, 4],  
    # [12, 13, 14, 5], 
    # [11, 16, 15, 6], 
    # [10, 9, 8, 7]]
    x = 0
    y = 0
    dir = 'right'
    for i in range(n*n): # 4*4 = 16 (0 ~ 16)
        answer[x][y] = i + 1 # answer[0][0] = 1
        if dir == 'right':
            y += 1 # answer[0][1]
            if y == n - 1 or answer[x][y+1] != 0:
                dir = 'down'
        elif dir == 'down':
            x += 1 # answer[1][3]
            if x == n - 1 or answer[x+1][y] != 0:
                dir = 'left'
        elif dir == 'left':
            y -= 1 # answer[3][3]
            if y == 0 or answer[x][y-1] != 0:
                dir ='up'
        elif dir == 'up':
            x -= 1
            if x == 0 or answer[x-1][y] != 0:
                dir = 'right'
    return answer