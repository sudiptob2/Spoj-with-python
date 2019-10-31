dp = dict()
def coins(n):  
    if n == 0:
        return 0
    elif n not in dp:
        dp[n] = max(n,coins(n//2) + coins(n//3) + coins(n//4))
    return dp[n]
    
n = int(input())

print(coins(n))

