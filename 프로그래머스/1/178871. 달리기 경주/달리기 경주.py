def solution(players, callings):
    answer = []
    player_positions = {}
    
    for idx, player in enumerate(players):
        player_positions[player] = idx
        # {"mumu":0,"soe":1,"poe":2,"kai":3,"mine":4}
    
    for c in callings:
        idx = player_positions[c]
        
        if idx > 0:
            front_player = players[idx - 1]
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
        player_positions[c] = idx - 1
        player_positions[front_player] = idx
        
    return players