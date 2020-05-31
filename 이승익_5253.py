# -*- coding: utf-8 -*-
"""
Created on Sun May 31 02:48:38 2020

@author: 이승익
"""

for t in range(1, int(input())+1):
    N,M=map(int,input().split())
    words_A=[None]*N
    for i in range(N):
        words_A[i]=input()
    words_B=[None]*M
    for j in range(M):
        words_B[j]=input()
    cnt=0
    for j in range(M):
        obj=words_B[j]
        for i in range(N):
            sbj=words_A[i]
            if len(sbj)<len(obj):
                continue
            else:
                sbj_proc=sbj[0:len(obj)]
                if obj==sbj_proc:
                    cnt+=1
                    break
    print('#{} {}'.format(t,cnt))