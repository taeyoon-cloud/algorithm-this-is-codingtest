# 개미 전사
n = int(input()) # 식량 창고 개수
arr = list(map(int, input().split())) # 식량 창고 정보

dp = [0] * 100

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-1])

print(dp[n-1])
