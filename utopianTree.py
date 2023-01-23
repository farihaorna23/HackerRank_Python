def utopianTree(n):
    answer = 1
    if n == 0:
        return 1
    
    for i in range(1,n+1):
        if i % 2 != 0:
            answer *= 2
        else:
            answer += 1
    return answer