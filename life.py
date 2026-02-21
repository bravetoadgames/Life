#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:51:36 2026

@author: arjeneke
"""
from classes.class_minion import Minion

minion = Minion()

print("Name: " + minion.sex.getFullName())
print("Gender: " + minion.sex.getGender())
print("Age expectancy: " + minion.health.getAgeExpectancy())


