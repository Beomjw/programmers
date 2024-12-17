def solution(board, k):
    answer = 0
    # [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if i + j <= k:
                answer += board[i][j]
    return answer