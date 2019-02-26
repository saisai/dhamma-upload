#!/usr/bin/env python
# coding=utf-8

files = [f.strip('\n') for f in open('test.txt', 'r') if len(f) > 2]

def splited_lines_generator(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i: i + n]

for index, lines in enumerate(splited_lines_generator(files, 10)):
    with open(str(index) + '.txt', 'w') as f:
        f.write('\n'.join(lines))
