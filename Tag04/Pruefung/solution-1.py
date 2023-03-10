#!/usr/bin/env python3
# coding: utf8

import os

print(f"cwd:   {os.getcwd()}")
print(f"Files: {os.listdir()}")

string = 'Panamakanal'
countOfA = 0;
for char in string:
    if (char == 'a'):
        countOfA += 1
print(f"Anzahl A's in Panamakanal: {countOfA}")