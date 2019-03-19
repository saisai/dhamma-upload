import os
import sys
import collections
import json

from bs4 import BeautifulSoup as bs4

file = sys.argv[0]

pathname = os.path.dirname(file)
#print(pathname)
#print('running from %s' % os.path.abspath(pathname))
#print(file)

running_from_path = os.path.abspath(pathname) + '/'
#print(running_from_path)




def splited_lines_generator(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i: i + n]

def get_splited_lines(file_in, line_num):
    
    file_in = running_from_path + file_in
    files = [f.strip('\n') for f in open(file_in, 'r') if len(f) > 2]
    
    
    for index, lines in enumerate(splited_lines_generator(files, line_num)):
        with open('{}{}.txt'.format(running_from_path, str(index)), 'w') as f:
            f.write('\n'.join(lines))
            

def change(num):
    mm = ['၀','၁','၂','၃', '၄', '၅', '၆','၇','၈','၉']
    strmm = ''
    mmlist = list(map(int, str(num)))
    
    for i in mmlist:
        strmm += mm[i]

    return strmm
    
def get_json(file_in_1, file_in_2, file_out, playlist, description_title, source=''):

    file_in_1 = running_from_path+file_in_1
    file_in_2 = running_from_path+file_in_2
    
    file_out = running_from_path+file_out
    
    titles = [title.strip('\n') for title in open(file_in_1)]
    #get_count = len(titles)
    #print(get_count)


    descriptions = [title.strip('\n') for title in open(file_in_2)]
    #get_count_descriptions = len(descriptions)
    #print(get_count_descriptions)

    description_title = description_title
    source = source


    results = []    
    playlist = playlist

    for title, description in zip(titles, descriptions):
      
        #print(title)
        if len(title.split('|')[2]) > 100:
            dict_title = {
                         "playlist" : playlist,
                         "title": "{}".format(title.split('|')[2]),
                          "description": "{}\n{}{}".format(description_title, description, source), 
                           "id": "{}".format( title.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title.split('|')[2]))
            results.append(dict_title)
        else:
            if len(description.split('|')[1]) > 0:
            
                dict_title = {
                              "playlist" : playlist,
                             "title": "{}".format(title.split('|')[2]),
                              "description": "{}\n{} ({}){}".format(description_title, description.split('|')[0], description.split('|')[1], source), 
                               "id": "{}".format(title.split('|')[0].split('.')[0])
                            }       

                results.append(dict_title)
            else:
                dict_title = {
                              "playlist" : playlist,
                             "title": "{}".format(title.split('|')[2]),
                              "description": "{}\n{} {}".format(description_title, description.split('|')[0], source), 
                               "id": "{}".format(title.split('|')[0].split('.')[0])
                            }       

                results.append(dict_title)            
        
        
    data = json.dumps(results, indent=4)        
    with open(file_out, encoding='utf-8', mode='w') as f:
        json.dump(data, f)  
        
# convert result to json        
def get_json_fb(file_in_1, file_in_2, file_out, playlist, description_title, source=''):

    file_in_1 = running_from_path+file_in_1
    file_in_2 = running_from_path+file_in_2
    
    file_out = running_from_path+file_out
    
    titles = [title.strip('\n') for title in open(file_in_1)]
    #get_count = len(titles)
    #print(get_count)


    descriptions = [title.strip('\n') for title in open(file_in_2)]
    #get_count_descriptions = len(descriptions)
    #print(get_count_descriptions)

    description_title = description_title
    source = source


    results = []    
    playlist = playlist

    for title, description in zip(titles, descriptions):
      
        #print(title)
        
        if len("{}\n{} {}".format(description_title, description.split('|')[2], source)) > 5000:
            print(len("{}\n{} {}".format(description_title, description.split('|')[2], source)))
            print("{}\n{}\n{} {}".format(description.split('|')[0].split('.')[0],description_title, description.split('|')[2], source))
        
        if len(title) > 100:
            dict_title = {
                         "playlist" : playlist,
                         "title": "{}".format(title),
                          "description": "{}\n{}{}".format(description_title, description, source), 
                           "id": "{}".format( description.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title))
            results.append(dict_title)
        else:
       
            dict_title = {
                          "playlist" : playlist,
                         "title": "{}".format(title),
                          "description": "{}\n{} {}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format(description.split('|')[0].split('.')[0])
                        }       

            results.append(dict_title)            
        
        
    data = json.dumps(results, indent=4)        
    with open(file_out, encoding='utf-8', mode='w') as f:
        json.dump(data, f)        
        
    
def convert_myanmar_number(file_in, file_out, count=1, desc=None):

    file_in = running_from_path+file_in
    
    file_out = running_from_path+file_out
    
    titles = [title.strip('\n\n\n') for title in open(file_in)]
    
    
    if desc is None:
    
        with open(file_out, 'w') as f:
            counter = count            
            for title in titles:                       
                
                if title.find('။') > 0: # found
                    f.write( '{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]) )
                else:
                    f.write( '{}။{}|\n'.format(change(counter), title.split('|')[2]) ) 
                
                counter += 1    
    else:
    
        with open(file_out, 'w') as f:
            counter = count
            for dd in desc.items():
                
                for title in titles:
                            
                    number = int(title.split('|')[0].split('.')[0])
                    #print(type(number))
                    if dd[1][1] <= number  <= dd[1][2]:
                        print(dd[1][0])
                        print(title.split('|')[2])            
                            
                        try:
                            
                            f.write('{}။{}|{}\n'.format(change(counter), title.split('|')[2].split('။')[1], dd[1][0]))
                            #print('{}။{}|\n'.format(change(counter), title.split('|')[2].split('။')[1]))
                            #print(title.split('|')[2])
                            
                        except IndexError as err:
                            f.write('{}။{}|\n'.format(change(counter), title.split('|')[2]))
                            #print('{}။{}|\n'.format(change(counter), title.split('|')[2]))
                            
                        
                        #print('{}။{}'.format(change(counter), title))
                        
                        counter += 1        
    

def check_duplicate(file_in):

    file_in = running_from_path+file_in
    
    
    urls = [url.split('|')[1] for url in open(file_in)]
    
    for key, val in collections.Counter(urls).items():
        if val > 1:
            print(key, val)
            
def update_raw_titles_links(file_in, file_out, count=1):

    file_in = running_from_path+file_in
    #print(file_in)
    file_out = running_from_path+file_out
    
    lines = [f.strip('\n') for f in open(file_in)]
    
    with open(file_out, 'w') as f:
        counter = count
        for line in lines:
            #print(line.split('|')[1])
            #media = line.split('|')[0]
            url = line.split('|')[1]
            ext = url.split('.')[-1]
            media = '{:03d}'.format(counter)
            title = line.split('|')[2]
            if title.find('။') > 0: # found
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title.split('။')[1]) )
            else:
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title) ) 
    
            counter += 1
            
def update_raw_reversed_titles_links(file_in, file_out, count=1):

    file_in = running_from_path+file_in
    #print(file_in)
    file_out = running_from_path+file_out
    
    lines = [f.strip('\n') for f in open(file_in)]
    
    with open(file_out, 'w') as f:
        counter = count
        for line in reversed(lines):
            #media = line.split('|')[0]
            url = line.split('|')[1]
            ext = url.split('.')[-1]
            media = '{:03d}'.format(counter)
            title = line.split('|')[2]
            if title.find('။') > 0: # found
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title.split('။')[1]) )
            else:
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title) ) 
    
            counter += 1            
    
            

'''
param -> get_url.txt
'''
def get_html_mp4(file_in, file_out, count=1):
    
    file_in = running_from_path+file_in
    #print(file_in)
    file_out = running_from_path+file_out
    
    text = open(file_in, 'r').read()

    soup = bs4(text, 'html.parser')
    
    #files = param_folder + 'titles_links.txt'
    #files = 'titles_links.txt'

    count = count
    with open(file_out, 'w') as fd:

        for key in soup.find_all('a'):
            ext = key.get('href').split('.')[-1]
            #print(ext)
            if ext in ['mp4', 'wmv']:
                #print(ext)
                #print(key.get('href'))
                counter = '{:03d}'.format(count)
                fd.write('{}.{}|{}|{}\n'.format(counter, ext, ''.join(key.get('href').split()), ' '.join(key.get_text().split())))

                count += 1
            
'''
param -> get_url.txt
'''
def get_html_mp3(file_in, file_out, count=1):

    file_in = running_from_path+file_in
    
    file_out = running_from_path+file_out

    text = open(file_in, 'r').read()

    soup = bs4(text, 'html.parser')
    
        
    count = count
    
    with open(file_out, 'w') as fd:

        for key in soup.find_all('a'):
            if '.mp3' in key.get('href'):
                counter = '{:03d}'.format(count)
                fd.write('{}.mp3|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split())))

                count += 1        
'''
if __name__ == '__main__':
    get_html_mp4('get_url.txt', 3)
'''
                



