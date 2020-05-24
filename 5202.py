T = int(input())

def todo(work): 
    schedule = [work[0]]
    before = work[0]
    for w in work:
        if w[0] >= before[1]:
            schedule.append(w)
            before = w
    return len(schedule)

for i in range(1, T+1):
    n = int(input())
    work = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x :x[1])
    numberOfWork = todo(work)
    print(f'#{i} {numberOfWork}')
