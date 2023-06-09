# 2. 부품 찾기
def binarySearch(array, target, start, end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)
    

n = int(input()) # 전체 부품 수
arr = list(map(int, input().split())) # 부품 번호
arr.sort() # 이진 탐색은 이미 정렬된 리스트에서만 가능하기 때문에 정렬해준다.

m = int(input()) # 찾고자 하는 부품 수
find_arr = list(map(int, input().split())) # 찾고자 하는 부품 번호


for num in find_arr:
    print(binarySearch(arr, num, 0, len(arr) - 1), end = " ")



