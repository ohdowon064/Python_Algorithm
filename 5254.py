def sol(N,word):
    subset=[]
    for i in range(0,len(word)+1):
        for j in range(i+1,len(word)+1):
            subset.append(word[i:j])
    
    result_list=[]
    for v in subset:
        if v not in result_list:
            result_list.append(v)
    result_list = sorted(result_list)

    result_index = result_list[int(N)-1]
    
    return result_index


T = int(input())
for test_case in range(1, T+1):
    N,word = input().split()
    result = sol(N, word)
    print('#{} {} {}'.format(test_case,result[0], len(result)))