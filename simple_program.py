def factorial(dp,n):
    if n == 0 or n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = n*factorial(dp,n-1)
    return dp[n]
    
n = int(input("enter n value:"))
dp = [0] * (n+1)

print(factorial(dp,n))