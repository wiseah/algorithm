def solution(money):
    answer = 0
    if len(money) == 1: # 집이 한 개인 경우
        return money.pop()
    
    size = len(money)
    dp1 = [0] + money[:-1] # 첫 번쩨 집 터는 경우(마지막 인덱스 집 불가능)
    for i in range(2, size):
        dp1[i] = max(dp1[i-1], dp1[i] + dp1[i-2])
    
    dp2 = [0] + money[1:] # 첫 번째 집 안터는 경우(마지막 인덱스 집 가능)
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i] + dp2[i-2])
        
    return max(dp1[-1], dp2[-1])