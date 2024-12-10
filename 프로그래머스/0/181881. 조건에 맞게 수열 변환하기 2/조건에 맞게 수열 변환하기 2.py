def solution(arr):
    answer = 0
    # arr(1) [1, 2, 3, 100, 99, 98]
    # arr(2) [3, 2, 7, 50, 99, 49]
    # ...
    # arr(5) [63, 2, 63, 51, 99, 99]
    # arr(6) [63, 2, 63, 51, 99, 99]
    old = arr
    while True:
        new = []
        for i in range(len(old)):
            if old[i] >= 50 and old[i] % 2 == 0:
                new.append(old[i] // 2)
            elif old[i] < 50 and old[i] % 2 != 0:
                new.append(old[i] * 2 + 1)
            else:
                new.append(old[i])
                
        if new == old:
            break
        else:
            old = new
            answer += 1
    return answer