def solution(array, commands):
    answer = []
    result = []
    i, j, k = 0, 0, 0
    for c in range(len(commands)):
        i = commands[c][0] # [2 5 3] [4 4 1] [1 7 3]
        j = commands[c][1]
        k = commands[c][2]
              
        answer = array[i-1:j]
        answer.sort()
        result.append(answer[k-1])
    
    return result

# def solution(array, commands):
#     answer = []
#     result = []
#     for command in commands:
#         i, j, k = command
        
#         answer = sorted(array[i-1:j])
#         result.append(answer[k-1])
    
#     return result