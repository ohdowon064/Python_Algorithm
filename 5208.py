import sys
read = sys.stdin.readline
T = int(input())

min_charge = float('inf')
def come(stops, v, charge):
    global min_charge
    if v + stops[v] >= len(stops):
        min_charge = min(min_charge, charge)
        return

    if charge >= min_charge:
        return

    for i in range(v+1, v + stops[v] + 1 if v + stops[v] <= len(stops) else len(stops)):
        come(stops, i, charge+1)

for i in range(1, T+1):
    stops = list(map(int, read().split()))
    come(stops[1:], 0, 0)
    print(f'#{i} {min_charge}')
    min_charge = float('inf')
