def solution(keyinput, board):
    answer = [0, 0]
    
    a = (board[0] - 1) // 2
    b = (board[1] - 1) // 2
    
    for key in keyinput:
        if key == "left":
            if -a < answer[0]: 
                answer[0] -= 1
        elif key == "right":
            if a > answer[0]:
                answer[0] += 1
        elif key == "up":
            if b > answer[1]:
                answer[1] += 1
        elif key == "down":
            if -b < answer[1]:
                answer[1] -= 1
    
    return answer