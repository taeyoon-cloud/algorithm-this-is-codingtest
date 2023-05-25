n = int(input())

count_3 = 0
answer = 0
for i in range(60):
    for j in range(60):
        if '3' in str(i) + str(j):
            count_3 += 1

if n < 3:
    answer = count_3 * (n+1)
elif n < 13:
    answer = 3600 + count_3 * n
else:
    answer = 7200 + count_3 * (n-1)

print(answer)