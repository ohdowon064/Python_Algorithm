t = int(input())
import itertools

def min_sum(n, data):
    m = [1 for _ in range(n-1)]
    m.extend([-1 for _ in range(n-1)])
    result = list(itertools.permutations(m))
    min = float('inf')

    for case in result:
        total = data[0][0]
        i, j = 0, 0
        for direct in case:
            if direct == 1:
                j += 1
            elif direct == -1:
                i += 1
            total += data[i][j]
        if min > total:
            min = total
    return min


for i in range(1, t+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = min_sum(n, data)
    print(f'#{i} {ans}')