# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:48:56 2020

@author: 이승익
"""

T = int(input())
for test_case in range(1, 1 + T):
    N, *M = map(int, input().split())
    
    count = 0 
    bus_stop = 0
    bus_battery = M[bus_stop]
    
    while bus_stop + bus_battery < N - 1:
        max_charge = 0
        next_bus_stop = 0
        for i in range(bus_battery, 0, -1):
            charge = M[bus_stop + i] - (bus_battery - i)
            if charge > max_charge:
                max_charge = charge
                next_bus_stop = bus_stop + i
                
        bus_stop = next_bus_stop
        bus_battery = M[bus_stop]
        count += 1
        
    print('#{} {}'.format(test_case, count))