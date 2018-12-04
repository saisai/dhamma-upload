#!/usr/bin/env python
# coding=utf-8



files = [f.strip('\n') for f in open('2018.txt', 'r') if len(f) > 2]

for f in reversed(files):
    print(f)
