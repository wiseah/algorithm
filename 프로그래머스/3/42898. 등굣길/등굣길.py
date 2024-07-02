def solution(m, n, puddles):  # m, n이 열, 행으로 주어짐
    dp = [[0]*(m+1) for i in range(n+1)] # dp 테이블을 n+1 x m+1 크기로 초기화(행x열)
    dp[1][1] = 1 # 시작점 초기화
    
    for puddle in puddles: # 웅덩이 표시(puddle 좌표가 열,행으로 주어져서 행, 열로 좌표 변환)
        dp[puddle[1]][puddle[0]] = -1 # puddle[1] = 행, puddle[0] = 열
        
    for i in range(1, n+1): # 행
        for j in range(1, m+1): # 열
            if dp[i][j] == -1: # 물이 고여있는 위치
                dp[i][j] = 0 # 경로 수를 0으로 설정
            else:
                if i > 1:
                    dp[i][j] += dp[i-1][j] # 위쪽에서 오는 경우(행의 숫자가 커지므로)
                if j >1:
                    dp[i][j] += dp[i][j-1] # 왼쪽에서 오는 경우(열의 숫자가 커지므로)
                dp[i][j] %= 1000000007
        
        
    return dp[n][m]