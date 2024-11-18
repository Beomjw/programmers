import datetime

def solution(a, b):
    answer = ''
    date = datetime.date(2016, a, b)
    
    # 0:월 ~ 6:일 
    day_of_week = date.weekday()
    
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    answer = days[(day_of_week) % 7]
    
    return answer