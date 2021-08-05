#python3 code

def solution(banana_list):
    def gcd(x, y):
        if x < y:
            x, y = y, x
        while (y):
            x, y = y, x % y
        return x

    def forever(x, y):
        quotient = (x+y)/gcd(x, y)
        if int(quotient) != quotient:
            return True
        quotient = int(quotient)
        return (quotient & (quotient-1)) != 0  
   
    def pair(u, match, seen):
        for v in range(l):
            if M[u][v] and seen[v] == False:
                seen[v] = True
                
                # if a has been matched to b, retrieve a from match[b]
                # check if it can be matched to another number given the 
                # current seen list. If so, updated match[b] to c (current)
                if match[v] == -1 or pair(match[v], match, seen):
                    match[v] = u
                    return True
        return False
           
    # build graph
    l = len(banana_list)
    M = [[None] * l for _ in range(l)]
    
    for i in range(l):
        for j in range(i, l):
            M[i][j] = forever(banana_list[i], banana_list[j])
            M[j][i] = M[i][j]  
    
    match = [-1] * l
    result = 0
    for i in range(l):
        seen = [False] * l
        if pair(i, match, seen):
            result += 1
    return l - 2 * (result//2)
