
import re 
import datetime

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):

    return [ atoi(c) for c in re.split('(\d+)', text)]

arrange_results = [f.strip('\n') for f in open('duration_edited.txt')]

#print(arrange_results)

for result in sorted(arrange_results, key=natural_keys):
    #print(result.split('|')[0], result.split('|')[2].replace('-', ''))
    if(len(result.split('|')[2].replace('-', '').split(':'))) != 3:
        results = result.split('|')[2].replace('-', '').split(':')
        print(result.split('|')[0], datetime.timedelta(hours=0, minutes=int(results[0]), seconds=int(results[1])).seconds)
    else:
        results = result.split('|')[2].replace('-', '').split(':')
        print(result.split('|')[0], datetime.timedelta(hours=int(results[0]), minutes=int(results[1]), seconds=int(results[2])).seconds)    
        
