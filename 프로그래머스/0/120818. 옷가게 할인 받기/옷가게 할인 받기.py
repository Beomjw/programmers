def solution(price):
    answer = 0
    if price < 100000:
        return price
    elif price >= 100000 and price < 300000:
        return int(price * 0.95)
    elif price >= 300000 and price < 500000:
        return int(price * 0.9)
    else:
        return int(price * 0.8)