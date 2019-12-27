def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm
    
title = 'ပထမကြီးတန်းအတွက် ဆန်းဘာသာ ပို့ချလမ်းညွှန်မှုစာဝါမှတ်တမ်း'    

for i in range(1, 34):
    tt = '{} ({})'.format(title, change(i))
    print('{}|{}|{}'.format(i, 'test', tt))