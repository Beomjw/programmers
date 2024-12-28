def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for b in babbling: # ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	
        for w in word: # ["aya", "ye", "woo", "ma"]
            if w * 2 not in b: # ["ayaaya", "yeye", "woowoo", "mama"]
                # ["ayaye", "uuu", "yemawoo"]	
                b = b.replace(w, ' ') 
                # [" ye", "uuu", " mawoo"]
                # ["   ", "uuu", "   woo"]
                # ["   ", "uuu", "      "]
        if b.isspace(): 
            answer += 1
    
    return answer
    