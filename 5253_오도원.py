T = int(input())

def prefix(text, pattern):
    count = 0
    for p in pattern:
        for t in text:
            if len(p) > len(t):
                continue
            if p == t[:len(p)]:
                count += 1
                break
    return count

for i in range(1, T+1):
    N, M = map(int, input().split())
    text = [input() for _ in range(N)]
    pattern = [input() for _ in range(M)]
    count = prefix(text, pattern)
    print(f'#{i} {count}')