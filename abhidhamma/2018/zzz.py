
def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm
    
files = [f.strip('\n') for f in open('c.txt', 'r') if len(f) > 2 ]

count = 1
title_one = "အဘိဓမၼာအေျခခံ တတိယအဆင့္  သမုစၥည္းပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ ("
title_two = "အဘိဓမၼာအေျခခံ တတိယအဆင့္  ပစၥည္းပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ ("
title_three = "အဘိဓမၼာအေျခခံ တတိယအဆင့္  ကမၼ႒ာန္းပိုင္း  ပို႕ခ်ခ်က္ အမွတ္စဥ္ ("
mp3 = 400
for f in files:

    if count <= 57:        
        print('{}{}.mp3|{}|{}{}){}'.format(f.split('|')[0], mp3, f.split('|')[1], title_one, change(count), f.split('။')[1]))
        count += 1
        mp3 += 1
    elif 57 <= count <= 140:
        print('{}{}.mp3|{}|{}{}){}'.format(f.split('|')[0], mp3, f.split('|')[1], title_two, change(count), f.split('။')[1]))
        count += 1
        mp3 += 1
    elif count > 140:
        print('{}{}.mp3|{}|{}{}){}'.format(f.split('|')[0], mp3, f.split('|')[1], title_three, change(count), f.split('။')[1]))
        count += 1
        mp3 += 1
