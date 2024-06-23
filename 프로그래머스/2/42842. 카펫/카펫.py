def solution(brown, yellow):
#    if yellow == 1:
#        return [3,3]
    for i in range(1, yellow+1):
        if (yellow % i) == 0:
            y2 = yellow // i
            if brown == (y2+2)*2 + 2*i:
                w = y2 + 2 # y2는 노란격자 가로 수 이므로 +2
                h = i + 2 # i는 노란격자 세로 수이므로 +2
                return [w, h]
                
# 반복문과 조건문이 모든 경우를 일반적으로 처리하기 때문에 yellow == 1인 경우 따로 정의해주지 않아도 됨.
