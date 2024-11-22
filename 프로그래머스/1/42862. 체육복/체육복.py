def solution(n, lost, reserve):
    # 바로 앞번호의 학생 or 바로 뒷번호의 학생에게만 체육복을 빌려 줄 수 있다.
    # 4번 학생은 -> 3번 학생 or 5번 학생
    
    # 전체 학생의 수 : 5
    # 잃어버린 학생 2, 4
    # 여벌 체육복 1, 3, 5
    # 빌려줄 수 있는 1->2 / 3->4 or 5->4
    # 5명이 수업을 들을 수 있다. (1, 2, 3, 4, 5)
    
    # 전체 학생의 수 : 5
    # 잃어버린 학생 2, 4
    # 여벌 체육복 3
    # 빌려줄 수 있는 3->2 or 3->4
    # 3명이 수업을 들을 수 있다. (1, 2, 3, 5 or 1, 3, 4, 5)
    
    # 전체 학생의 수 : 3
    # 잃어버린 학생 3
    # 여벌 체육복 1
    # 빌려줄 수 있는 학생 없다.
    # 2명이 수업을 들을 수 있다.(1번이랑 2번)
    
    # 전체 학생의 수 : 5
    # 잃어버린 학생 : 2, 4, 5
    # 여벌 체육복 : 2, 4
    # 빌려줄 수 있는 학생 없다.
    # 4명이 수업을 들을 수 있다. (1번 2번 3번 4번) 
    common = set(lost) & set(reserve)
    actual_lost = set(lost) - common
    actual_reserve = set(reserve) - common
    
    for student in sorted(actual_reserve):
        if student - 1 in actual_lost:
            actual_lost.remove(student - 1)
        elif student + 1 in actual_lost:
            actual_lost.remove(student + 1)
    
    return n - len(actual_lost)


    