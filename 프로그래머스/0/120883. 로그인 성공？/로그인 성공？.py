def solution(id_pw, db):
    answer = ''
    for ip in db:
        if id_pw[0] == ip[0] and id_pw[1] == ip[1]:
                return "login"
        elif id_pw[0] == ip[0] and id_pw[1] != ip[1]:
                return "wrong pw"
    
    return "fail"
                