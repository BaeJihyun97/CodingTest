def solution(n):
    answer = 0
    if n % 2 == 1:
        answer = 0
    else:
        n //= 2
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 3
        for i in range(2, n+1):
            dp[i] = (dp[i-1]*4 - dp[i-2]) % 1000000007

        answer = dp[n]
    return answer