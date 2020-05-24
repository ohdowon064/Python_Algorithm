def binarySearch(data, key):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key == data[mid]:
            return mid
        elif key < data[mid] :
            end = mid - 1
        else:
            start = mid + 1
    return -1
0
T = int(input())
for i in range(1, i+1):

