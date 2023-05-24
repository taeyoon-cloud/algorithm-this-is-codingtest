# 1이 될 때까지
n, k = map(int,input().split())

count = 0
while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        temp = n % k
        n -= temp
        if n == 0:
            count += (temp - 1)
            break
        else:
            count += temp
    print(n, count)

print(count)