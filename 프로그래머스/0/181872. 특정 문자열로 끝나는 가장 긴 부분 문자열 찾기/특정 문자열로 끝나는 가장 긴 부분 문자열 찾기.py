def solution(myString, pat):
    # "AbCdEFG"
    # "dE"
    end = myString.rfind(pat) # 3
            
    return myString[:end+len(pat)]