T = int(input())


def team(n, m, vote):
    global p, rank
    for i in range(1, n+1):
        make_set(i)
    for i in range(0, len(vote), 2):
        p1, p2 = vote[i:i+2]
        union(p1, p2)
    teams = set()
    for i in range(1, n+1):
        teams.add(find_set(i))
    return len(teams)

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


for i in range(1, T+1):
    n, m = map(int, input().split())
    vote = list(map(int, input().split()))
    p = [0 for _ in range(n+1)]
    rank = [0 for _ in range(n+1)]
    ans = team(n, m, vote)
    print(f'#{i} {ans}')


# T = int(input())

# def team(n, m, vote):
#     p = [set({i}) for i in range(1, n+1)]
#     for i in range(0, len(vote), 2):
#         p[vote[i]-1].union(p[vote[i+1]-1])
#     print(p)
#     return len(p)

# for i in range(1, T+1):
#     n, m = map(int, input().split())
#     vote = list(map(int, input().split()))
#     ans = team(n, m, vote)
#     print(f'#{i} {ans}')

