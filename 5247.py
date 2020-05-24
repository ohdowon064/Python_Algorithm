T = int(input())

for i in range(1, T+1):
    pass

def bfs(Q, v):
    visited = [False] * n
    Q = []
    Q.append(v)
    visited[v]
    visit(v)
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(W)
                visited[w] = True
                visit(w)
