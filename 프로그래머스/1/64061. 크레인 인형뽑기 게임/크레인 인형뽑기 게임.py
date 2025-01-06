def solution(board, moves):
    answer = 0
    # [[0,0,0,0,0],
    # [0,0,1,0,3],
    # [0,2,5,0,1],
    # [4,2,4,4,2],
    # [3,5,1,3,1]]
    
    # [1,5,3,5,1,2,1,4]
    
    # basket = [4, 3, 1, 1, 3, 2, 4]
    basket = []
    x = len(board) # 5
    # y = len(board[0]) # 5
    
    for m in moves: # [1,5,3,5,1,2,1,4]
        for i in range(x): 
            if board[i][m - 1] != 0:
                basket.append(board[i][m - 1])
                board[i][m -1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
            
    return answer