import datetime

#minutes =   [f.strip('\n') for f in open('zz_titles.txt', 'r')]
'''
minutes =   [f.strip('\n') for f in open('duration.txt', 'r')]

count = 1
for f in minutes:
    #print(f.split(':'))
    data = f.split(':')
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=30, seconds=0).seconds = 5400
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    # datetime.timedelta(hours=1, minutes=10, seconds=0).seconds = 4200
    if len(data) > 2:
        #print(f.split(':'))
        #print(len(data))
        if datetime.timedelta(hours=int(data[0]), minutes=int(data[1]), seconds=int(data[2])).seconds > 4200:
            print(count)
    
    count += 1
'''

files = [f.strip('\n') for f in open('file.txt')]
minutes =   [f.strip('\n') for f in open('no_time_id_title.txt', 'r')]

count = 1
for result in minutes:
    f = result.split('|||')[1]
    data = f.split(':')
    if len(data) > 2:
        if datetime.timedelta(hours=int(data[0]), minutes=int(data[1]), seconds=int(data[2])).seconds > 4500:
            print(result.split('|||')[0])
    
    '''
    #print(f.split(':'))
    data = f.split(':')
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    # datetime.timedelta(hours=1, minutes=10, seconds=0).seconds = 4200
    if len(data) > 2:
        #print(f.split(':'))
        #print(len(data))
        if datetime.timedelta(hours=int(data[0]), minutes=int(data[1]), seconds=int(data[2])).seconds > 4200:
            print(count)
    
    count += 1
    '''
            

