
import collections


urls = [url.split('|')[1] for url in open('test.txt')]

#print(urls)


for key, val in collections.Counter(urls).items():
    if val > 1:
        print(key, val)
       
