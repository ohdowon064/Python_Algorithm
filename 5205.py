T = int(input())

def qs(data, start, end):
    if start < end:
        pivot = partition(data, start, end)
        qs(data, start, pivot-1)
        qs(data, pivot+1, end)

def partition(data, start, end):
    x = data[end]
    i = start - 1
    for j in range(start, end):
        if data[j] <= x:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[end] = data[end], data[i+1]
    return i+1

for i in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    qs(data, 0, n-1)
    print(f'#{i} {data[int(n/2)]}')
    