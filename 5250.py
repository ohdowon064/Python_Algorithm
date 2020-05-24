T = int(input())

def move(G, r, n):
    D = [float('inf')] * (n*n)
    P = [None] * (n*n)
    visited = [False] * (n*n)
    D[r] = 0

    for _ in range(n*n):
        minIndex = -1
        min_val = float('inf')
        for i in range(n*n):
            if not visited[i] and D[i] < min_val:
                min_val = D[i]
                minIndex = i
        visited[minIndex] = True
        if len(G[minIndex]) > 0:
            for v, val in G[minIndex]:
                if not visited[v] and D[minIndex] + val < D[v]:
                    D[v] = D[minIndex] + val
                    P[v] = minIndex
    return D[n*n-1]

for i in range(1, T+1):
    n = int(input())
    tmap = [list(map(int, input().split())) for _ in range(n)]
    G = {}
    p = 0
    for row in range(n):
        for col in range(n):
            G[p] = []
            if col != n - 1:
                h = tmap[row][col] - tmap[row][col+1]
                if h >= 0:
                    G[p].append((p+1, 1))
                else:
                    G[p].append((p+1, 1 - h))
            if row != n-1:
                h = tmap[row][col] - tmap[row+1][col]
                if h >= 0:
                    G[p].append((p+n, 1))
                else:
                    G[p].append((p+n, 1-h))
            p += 1

    ans = move(G, 0, n)
    print(f'#{i} {ans}')
