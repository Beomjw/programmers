def solution(board, h, w):
    answer = 0
    # [["blue", "red", "orange", "red"], 
    # ["red", "red", "blue", "orange"], 
    # ["blue", "orange", "red", "red"], 
    # ["orange", "orange", "red", "blue"]]
    
    color = board[h][w]
    rows = len(board) # 4
    cols = len(board[0]) # 4
    # 위
    if h > 0 and board[h-1][w] == color:
        answer += 1
    # 아래
    if h < rows - 1 and board[h+1][w] == color:
        answer += 1
    # 왼쪽
    if w > 0 and board[h][w-1] == color:
        answer += 1
    # 오른쪽
    if w < cols - 1 and board[h][w+1] == color:
        answer += 1
        
    return answer