count = 0
def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global count
    result = [0 for _ in range(len(left) + len(right))]
    if left[-1] > right[-1] : count += 1
    li = 0
    ri = 0
    k = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            result[k] = left[li]
            li += 1
        else:
            result[k] = right[ri]
            ri += 1
        k += 1
    
    if li < len(left):
        for i in range(li, len(left)):
            result[k] = left[i]
            k += 1
    if ri < len(right):
        for i in range(ri, len(right)):
            result[k] = right[i]
            k += 1
    
    return result

T = int(input())
for i in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    data = merge_sort(data)
    print(f'#{i} {data[n//2]} {count}')
    count = 0