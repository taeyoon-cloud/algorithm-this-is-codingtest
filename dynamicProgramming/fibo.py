def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


# print(fibo(100))


dp = [0] * 101

# 재귀(top-down)
def fibo_dp_1(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo_dp_1(30))

# 반복문(bottom-up)
def fibo_dp_2(x):
    dp[1] = 1
    dp[2] = 1
    for i in range(3, x+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[x]


print(fibo_dp_2(30))
    