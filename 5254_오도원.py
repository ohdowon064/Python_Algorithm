T = int(input())

def suffix(text):
    text = text[::-1]
    suf = []
    for i in range(len(text)):
        suf.append(text[:i+1][::-1])
    return sorted(suf)

def substring(text, N):
    suf = suffix(text)
    LCP = [0 for _ in range(len(text))]
    for i in range(1, len(text)):
        prev = suf[i-1]
        cur = suf[i]
        j = 0
        while j < len(prev) and j < len(cur) and prev[j] == cur[j]: 
            j += 1
        LCP[i] = j
    
    subcount = 0
    for i in range(len(text)):
        subcount += len(suf[i]) - LCP[i]
        if subcount >= N:
            return suf[i][:len(suf[i])-(subcount - N)]



for i in range(1, T+1):
    N, text = input().split()
    sub = substring(text, int(N))
    print(f'#{i} {sub[0]} {len(sub)}')