def make_set(x):
    global p, rank
    p[x] = x
    rank[x] = 0

def find_set(x):
    global p, rank
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    global p, rank
    link(find_set(x), find_set(y))

def link(x, y):
    global p, rank
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1

def kruskal(G, V):
    global p, rank
    mst = []
    for i in range(V+1):
        make_set(i)
    G.sort(key=lambda x: x[2])
    mst_cost = 0

    while len(mst) < V:
        u, v, val = G.pop(0)
        if find_set(u) != find_set(v):
            union(u, v)
            mst.append((u, v))
            mst_cost += val
    return mst_cost

T = int(input())
for i in range(1, T+1):
    V, E = map(int, input().split())
    G = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G.append((n1, n2, w))
    rank = [0 for _ in range(V+1)]
    p = [0 for _ in range(V+1)]
    ans = kruskal(G, V)
    print(f'#{i} {ans}')