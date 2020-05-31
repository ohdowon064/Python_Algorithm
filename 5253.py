def sol(N,M):
    ar_n=[]
    for i in range(N):
        ar_n.append(input())
    
    ar_m = []
    for j in range(M):
        ar_m.append(input())

    count = 0
    match_list=[]
    for x in range(N):
        word = ar_n[x]

        for y in range(M):
            prefix = ar_m[y]

            if len(prefix) <= len(word):
                word_slice = word[:len(prefix)]
                if word_slice == prefix:
                    count += 1
                    match_list.append(prefix)
    
    result_list=[]
    for v in match_list:
        if v not in result_list:
            result_list.append(v)
    
    result = len(result_list)

       
    return result



T = int(input())
for test_case in range(1, T+1):
    N,M = map(int, input().split())
    print('#{} {}'.format(test_case,sol(N,M)))