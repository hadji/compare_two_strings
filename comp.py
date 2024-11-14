# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:32:56 2024

@author: boris
"""

import sys

if len(sys.argv) < 3:
    print('Enter parameters!')
    sys.exit(1)

str1 = sys.argv[1]
str2 = sys.argv[2]

# Modify check to accept and return `str2`
def check(char, str2):
    found = True
    ind = str2.find(char)
    if ind != -1:
        if ind == 0:
            str2 = str2[1:]
        else:
            str2 = str2[:ind] + str2[ind + 1:]
    else:
        found = False
    return found, str2

# Loop through each character in `str1` without modifying it
for ch in str1:
    found, str2 = check(ch, str2)  # Update `str2` after each check
    if not found:
        break
if not found:
    print("Two strings are different!")
else:
    print("Two strings are equals!")