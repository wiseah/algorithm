def solution(triangle):
    dp = triangle
    
    for i in range(1, len(dp)): 
        for j in range(i+1): # 가장 왼쪽
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j ==i: # 가장 오른쪽
                dp[i][j] += dp[i-1][-1]
            else: # 중간인 경우 윗줄의 왼쪽 대각선 원소와 윗줄의 바로 위 원소 중 더 큰 값을 더함
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
    
    return max(dp[-1]) # 가장 마지막 줄에서 최대값 찾아서 반환