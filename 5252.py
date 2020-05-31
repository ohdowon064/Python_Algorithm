def sol(N,M):
    ar=[]
    for i in range(N):
        ar.append(input())
    
    count = 0
    for j in range(M):
        word = input()
        if word in ar:
        
            count +=1;
    return count



T = int(input())
for test_case in range(1, T+1):
    N,M = map(int, input().split())
    print('#{} {}'.format(test_case,sol(N,M)))