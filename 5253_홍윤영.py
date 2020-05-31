for t in range(1, int(input())+1):
    N,M=map(int,input().split())
    words_A=[]
    for i in range(N):
        data = input()
        words_A.append(data)
    words_B=[]
    for j in range(M):
        data  = input()
        words_B.append(data)
    cnt=0
    for j in range(M):
        obj=words_B[j]
        for i in range(N):
            sbj=words_A[i]
            if len(sbj)>=len(obj):
                sbj_proc=sbj[0:len(obj)]
                if obj==sbj_proc:
                    cnt+=1
                    break
    print('#{} {}'.format(t,cnt))
