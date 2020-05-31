# -*- coding: utf-8 -*-
"""
Created on Sun May 31 02:48:21 2020

@author: 이승익
"""

for t in range(1, int(input())+1):
    N,M=map(int,input().split())
    dictionary_A=set()
    for i in range(N):
        dictionary_A.add(input())
    cnt=0
    for j in range(M):
        obj=input()
        if obj in dictionary_A:
            cnt+=1
    print('#{} {}'.format(t,cnt))