T = int(input())
import itertools

def battery(n, data):
    result = list(itertools.permutations(range(1, n)))
    min_energy = float('inf')
    for case_ in result:
        total = 0
        case = [0] + list(case_) + [0]
        for i in range(len(case)-1):
            total += data[case[i]][case[i+1]]
        if min_energy > total:
            min_energy = total
    return min_energy



for i in range(1, T+1):
    n = int(input())
    energy = [list(map(int, input().split())) for _ in range(n)]
    ans = battery(n, energy)
    print(f'#{i} {ans}')