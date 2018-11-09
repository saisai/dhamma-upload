import os
import glob

files = """696944847356258
573948799727396
177179439869075
341656486606078
301827210412217
363050514237814
2247641922149208
884400958430205
298965134256707
297209544214629
331090984320020
247008469298935"""

tt = []
for mp4 in files.split('\n'):
    #print(mp4+'.mp4')
    tt.append(mp4+'.mp4')


for t in glob.glob('*.mp4'):
    if t not in tt:
        print(t)
        dest = 'finished/' + t
        os.rename(t, dest)

