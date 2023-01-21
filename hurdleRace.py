def hurdleRace(k, height):
    max_value = max(height)
    diff = max_value - k
    
    if diff <= 0:
        return 0
    else:
        return diff