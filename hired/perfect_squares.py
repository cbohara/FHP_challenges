import math

def solution(A,B):
    count = 0
    for x in range(A,B+1):
        if x < 0:
            continue
        if math.sqrt(x) % 1 == 0:
            count +=1
    return count

print(solution(4,17))
