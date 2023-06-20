# 바닥 공사
n = int(input()) # 가로 길이 n
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796

print(dp[n])
