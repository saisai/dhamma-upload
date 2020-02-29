#!/usr/bin/env python
# coding=utf-8

time = [f.strip('\n').split(' ') for f in open('time.txt')]

time_duration = [f.strip('\n').split(' ') for f in open('time_duration.txt')]

not_equal = 0
not_equal_list = []
for t, td in zip(time, time_duration):
    if t[0] == td[0]:
        print("{}: {}".format(t[0], int(t[1]) - int(td[1])))
    else:
        not_equal += 1
        not_equal_list.append(t[0])
        
print("Not equal:", not_equal)
print("Not equal list:", not_equal_list)