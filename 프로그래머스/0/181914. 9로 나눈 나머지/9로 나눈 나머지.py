
def solution(number):
    # answer = 0
    # answer = int(number) % 9
    sum = 0
    for i in number:
        sum += int(i)
    return sum % 9