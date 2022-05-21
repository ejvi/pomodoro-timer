#!/usr/bin/env python
import time, sys, os
from tqdm import tqdm

iteration = 0


def pomodoro():
    t = 1500
    pbar = tqdm(total=t)
    for i in range(t):
        pbar.update(n=1)
        time.sleep(1)

if iteration == 0:
    input ("Press ENTER to POMODORO")
    pomodoro()
    iteration = 1
    
    
    
if iteration == 1:
    while True:
        print('''
Time for a little break''')
        input ("Press ENTER to continue")
        pomodoro()