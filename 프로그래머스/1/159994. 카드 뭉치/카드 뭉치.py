def solution(cards1, cards2, goal):
#     answer = ''
#     # goal ["i", "want", "to", "drink", "water"]
#     # cards1 ["i", "drink", "water"]
#     # cards2 ["want", "to"]
#     result1 = []
#     result2 = []
#     for i, s in enumerate(goal): # ["i", "want", "to", "drink", "water"] 0 1 2 3 4 
#         for j, c1 in enumerate(cards1): # ["i", "drink", "water"] 0 1 2
#             if c1 == s:
#                 result1.append(j)
#         for z, c2 in enumerate(cards2): # ["want", "to"] 0 1
#             if c2 == s:
#                 result2.append(z)
    
#     result1_sort = sorted(result1, reverse=True)
#     result2_sort = sorted(result2, reverse=True)
    
#     if result1 == result1_sort and result2 == result2_sort:
#         return "Yes"
#     else:
#         return "No"

    i = 0
    j = 0
    for word in goal: # ["i", "want", "to", "drink", "water"]
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            return "No"
    
    return "Yes"
        