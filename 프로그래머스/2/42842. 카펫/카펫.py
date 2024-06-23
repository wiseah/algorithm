def solution(brown, yellow):
    if yellow == 1:
        return [3,3]
    for i in range(1, yellow+1):
        if (yellow % i) == 0:
            y2 = yellow // i
            if brown == (y2+2)*2 + 2*i:
                w = y2 + 2
                h = i + 2
                return [w, h]