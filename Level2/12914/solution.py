def solution(n):
    answer = 0
    dp = [0] * (n+1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    answer = (dp[-1]) % 1234567
    
    return answer