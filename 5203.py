T = int(input())

def babygin(cards):
    if len(cards) < 3:
        return False
    counting = [0 for _ in range(10)]
    baby = {'triplete' : 0, 'run' : 0}
    for c in cards:
        if counting[c] != 0: continue
        else: counting[c] = cards.count(c)
    
    for i in range(len(counting)):
        if counting[i] != 0 and counting[i+1] != 0 and counting[i+2] != 0 and i+2 <= len(counting)-1:
            baby['run'] += 1
            counting[i] -= 1
            counting[i+1] -= 1
            counting[i+2] -= 1
            return True
        if counting[i] >= 0:
            baby['triplete'] += 1
            counting[i] -= 3
            return True
    return False
        
def game(cards):
    even, odd = [], []
    even_score = 0
    odd_score = 0
    for i in range(len(cards)):
        if i & 1 == 0: even.append(cards[i])
        else: odd.append(cards[i])
        if babygin(even):
            even_score += 1
        if babygin(odd):
            odd_score += 1
        if even_score > odd_score:
            return 1
        elif even_score < odd_score:
            return 2
    return 0

for i in range(1, T+1):
    cards = list(map(int, input().split()))
    win = game(cards)
    print(f'#{i} {win}')
