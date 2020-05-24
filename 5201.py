T = int(input())

def transport(truck, container):
    container.sort(reverse=True)
    truck.sort(reverse=True)
    load = []
    while truck:
        if truck[0] >= container[0]:
            load.append(container[0])
            truck.pop(0)
        container.pop(0)
        if not container: break
    return sum(load)

for i in range(T):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    load = transport(truck, container)
    print(f'#{i+1} {load}')