n, m = map(int, input().split())

answer = 0
for i in range(n):
    temp_arr = list(map(int, input().split()))
    answer = max(answer, min(temp_arr))

print(answer)