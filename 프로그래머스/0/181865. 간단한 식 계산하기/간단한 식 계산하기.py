def solution(binomial):
    answer = 0
    calculator = []
    if '+' in binomial:
        calculator = binomial.split(' + ')
        return int(calculator[0]) + int(calculator[1])
    elif '-' in binomial:
        calculator = binomial.split(' - ')
        return int(calculator[0]) - int(calculator[1])
    elif '*' in binomial:
        calculator = binomial.split(' * ')
        return int(calculator[0]) * int(calculator[1])
    return calculator