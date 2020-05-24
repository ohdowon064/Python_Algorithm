def dijkstra(G, r, V):
    D = [float('inf')] * (V + 1)
    P = [None] * (V + 1)
    visited = [False] * (V + 1)
    D[r] = 0

    for _ in range(V+1):
        minIndex = -1
        min_val = float('inf')
        for i in range(V+1):
            if not visited[i] and D[i] < min_val:
                min_val = D[i]
                minIndex = i
        visited[minIndex] = True
        if minIndex in G:
            for v, val in G[minIndex]:
                if not visited[v] and D[minIndex] + val < D[v]:
                    D[v] = D[minIndex] + val
                    P[v] = minIndex
    return D[V]

T = int(input())
for i in range(1, T+1):
    N, E = map(int, input().split())
    G = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        if s not in G:
            G[s] = [(e, w)]
        else: G[s].append((e, w))
    ans = dijkstra(G, 0, N)
    print(f'#{i} {ans}') 
    