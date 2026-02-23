#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:51:36 2026

@author: arjeneke
"""

from classes.class_minion import Minion

import os
import time

os.system('clear')
minion = Minion()


# -------------------------------------------------------------------------
# Game loop
# -------------------------------------------------------------------------
delta_time = 0
last_time = time.time()
fps=30

while True:
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time



    # Game logic (e.g., movement: position += speed * dt)
    #print(f"Update with delta_time: {delta_time:.4f}s")
    if not minion.health.isDead():
        minion.lifePulse()
    else:
        minion = Minion()



    # Maintain target FPS
    frame_time = 1 / fps
    sleep_time = frame_time - (time.time() - current_time)
    if sleep_time > 0:
        time.sleep(sleep_time)

