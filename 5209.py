# T = int(input())

# best = float('inf')
# def product(costs, min_set, current_cost, k, check):
#     global best
#     if best <= current_cost:
#         return
#     if k == len(costs):
#         best = sum(min_set)
#         return

#     for m in range(k, len(costs)):
#         for company in range(len(costs[m])):
#             if not check[company]:
#                 min_set.append(costs[m][company])
#                 check[company] = True
#                 product(costs, min_set, current_cost+costs[m][company], k+1, check)
#                 check[company] = False
#                 min_set.pop()
    

# for i in range(1, T+1):
#     n = int(input())
#     costs = [list(map(int, input().split())) for _ in range(n)]
#     min_set = []
#     check = [False for _ in range(n)]
#     product(costs, min_set, 0, 0, check)
#     print(f'#{i} {best}')
#     best = float('inf')

T = int(input())

def product(G, cost, rank):
    global visited, min_cost
    if min_cost <= cost:
        return
    if rank == len(G):
        min_cost = cost
    else:
        for company in range(len(G[rank])):
            if not visited[company]:
                visited[company] = True
                product(G, cost + G[rank][company], rank+1)
                visited[company] = False
    

for i in range(1, T+1):
    n = int(input())
    G = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_cost = float('inf')
    product(G, 0, 0)
    print(f'#{i} {min_cost}')


# T = int(input())

# def product(G, cost, rank):
#     global min_cost
#     if min_cost <= cost:
#         return
#     if rank == len(G):
#         min_cost = cost
#     else:
#         for company in range(len(G[rank])):
#             product(G, cost + G[rank][company], rank+1)
    

# for i in range(1, T+1):
#     n = int(input())
#     G = [list(map(int, input().split())) for _ in range(n)]
#     min_cost = float('inf')
#     product(G, 0, 0)
#     print(f'#{i} {min_cost}')
