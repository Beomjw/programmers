def solution(num_list):
    even = 0
    odd = 0
    # 첫 번째 원소를 1번 원소라고 할 때,
    # 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
    
    if even > odd:
        return even
    else:
        return odd
    