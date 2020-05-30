T = int(input())

def same(w1, w2):
    count = 0
    for i in w2:
        if i in w1:
            count += 1
    return count

for i in range(1, T+1):
    N, M = map(int, input().split())
    word1 = [input() for _ in range(N)]
    word2 = [input() for _ in range(M)]
    count = same(word1, word2)
    print(f'#{i} {count}')