import datetime

minutes =   [f.strip('\n') for f in open('zz_titles.txt', 'r')]

count = 1
for f in minutes:
    #print(f.split(':'))
    data = f.split(':')
    # datetime.timedelta(hours=1, minutes=40, seconds=0).seconds = 6000
    # datetime.timedelta(hours=1, minutes=15, seconds=0).seconds = 4500
    if len(data) > 2:
        #print(f.split(':'))
        #print(len(data))
        if datetime.timedelta(hours=int(data[0]), minutes=int(data[1]), seconds=int(data[2])).seconds > 4500:
            print(count)
    
    count += 1
            

