def solution(sticker):
    answer = 0
    if len(sticker) == 1: # 스티커 1개인 경우
        return sticker.pop()
    
    size = len(sticker)
    dp1 = [0] + sticker[:-1] # 0번 인덱스의 스티커를 떼는 경우
    for i in range(2, size): # 1번 인덱스와 마지막 인덱스의 스티커 사용불가
        dp1[i] = max(dp1[i-1], dp1[i] + dp1[i-2]) # 현재 스티커를 선택하지 않은 경우 vs 현재 스티커를 선택하고 두 칸 전의 최대 점수를 더하는 경우
    
    dp2 = [0] + sticker[1:]  # 1번 인덱스의 스티커를 떼는 경우(첫 번째 스티커를 선택하지 않는 경우이므로 마지막 스티커 선택 가능)
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i] + dp2[i-2])
        
    answer = max(dp1[-1], dp2[-1]) # 첫 번째 스티커를 선택한 경우 vs 첫 번째 스티커 선택 안한 경우 중 더 큰 값
    

    return answer