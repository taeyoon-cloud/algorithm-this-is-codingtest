# 3. 성적이 낮은 순서대로 학생 출력하기
n = int(input())
arr = []
for i in range(n):
    line = input().split()
    name = line[0]
    grade = int(line[1])
    arr.append((name, grade))

arr.sort(key = lambda x: x[1])

for p in arr:
    print(p[0], end = ' ')