import os
import sys
import collections
import json
import shutil
import subprocess
import glob

from bs4 import BeautifulSoup as bs4
import requests


from .helper import natural_keys

file = sys.argv[0]

pathname = os.path.dirname(file)
#print(pathname)
#print('running from %s' % os.path.abspath(pathname))
#print(file)

running_from_path = os.path.abspath(pathname) + '/'
print(running_from_path)


# read file 
# return list as result
def get_results(file_in):
    file_in = running_from_path + file_in
    #print(file_in, 'a')
    return [f.strip('\n') for f in open(file_in) ]
    

def breaker_in_order(list_result):

    #tmp = []
    
    def get_line_breaker(line):
        breaker = line.split('|')[0].strip() == 'breaker'
        ext_desc = ""
        if breaker == True:
            ext_desc = line.split('|')[1]
        return (breaker, ext_desc)
        
    def get_line_not_breaker(line):
        breaker = line.split('|')[0].strip() != 'breaker'
        ext_desc = ""
        if breaker != False:
            ext_desc = line
        return ext_desc
    
    for line in list_result:
        #print(get_line_breaker(line))
        tmp = ""
        
        if get_line_breaker(line)[0] == True:
            tmp = get_line_breaker(line)[1]
            extra_desc = tmp
        else:
            #print('{}'.format(line))
            #print('{}|{}'.format(line, extra_desc))
            print('{}|{}'.format(get_line_not_breaker(line).split('|')[2], extra_desc))

def change_order(list_result):

    tmp = []
    
    for line in list_result:
        if line.split('|')[0].strip() == 'breaker':
            
            cc = list(reversed(tmp))
            
            for dd in cc:
                yield dd + '|' + line.split('|')[1]
                
            tmp.clear() # make empty list
            
        else:            
            tmp.append(line)
            
def add_extra_description(list_result):

    tmp = []
    
    def get_line_breaker(line):
        breaker = line.split('|')[0].strip() == 'breaker'
        ext_desc = ""
        if breaker == True:
            ext_desc = line.split('|')[1]
        return (breaker, ext_desc)
        
    def get_line_not_breaker(line):
        breaker = line.split('|')[0].strip() != 'breaker'
        ext_desc = ""
        if breaker != False:
            ext_desc = line
        return ext_desc
    
    for line in list_result:
        #print(get_line_breaker(line))
        tmp = ""
        
        if get_line_breaker(line)[0] == True:
            tmp = get_line_breaker(line)[1]
            extra_desc = tmp
        else:
            print('{}|{}'.format(get_line_not_breaker(line).split('|')[2], extra_desc))
     

def copy_to_remote(copied_file, remote_username, remote_pass, remote_hostname, remote_port, escaped_remote):
    #remote_username = 'u0_a97'
    #remote_hostname = '192.168.1.36'
    #escaped_remote = '/storage/1527-15E5/Android/data/com.termux/files/youtube/ashin-zaw-ti-ka-nyaungdone/'
    copied_file = running_from_path + copied_file
    
    #print(glob.glob(copied_file))
    
    for copied_file in sorted(glob.glob(copied_file),   key=natural_keys):
        print(copied_file)
    
        if os.path.isfile(copied_file):
            cmd = "sshpass -p %s /usr/bin/rsync -P --partial -avzzz %s -e 'ssh -p %s' %s@%s:'%s'" % (remote_pass, copied_file, remote_port, remote_username, remote_hostname, escaped_remote)

            result = 1 
            while result != 0:
                result = subprocess.Popen(cmd,shell=True).wait()
                #text = result.communicate()[0]
                #returncode = result.returncode
            
                print(result)
            
            if result == 0:
                if os.path.isfile(copied_file):
                    print('Moving file...', copied_file)
                    shutil.move(copied_file, '%sfinished/' % (running_from_path))    


def get_line_from_file(file_in):
    file_in = running_from_path + file_in
    for f in open(file_in, 'r'):
        yield f.split('|')[1]


def check_link(url):
    r = requests.get(url)
    return r.status_code
    


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
        
def get_json_option(file_in_1, file_in_2, file_out, playlist, description_title, source=''):

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
                         "playlist" : playlist.strip(),
                         "title": "{}".format(title.split('|')[2]),
                          "description": "{}\n{}{}".format(description_title, description, source), 
                           "id": "{}".format( title.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title.split('|')[2]))
            results.append(dict_title)
        else:
            dict_title = {
                          "playlist" : playlist.strip(),
                         "title": "{}".format(title.split('|')[2]),
                          "description": "{}\n{} {}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format(title.split('|')[0].split('.')[0])
                        }       

            results.append(dict_title)        
            '''
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
                              "description": "{}\n{} {}".format(description_title, description.split('|')[2], source), 
                               "id": "{}".format(title.split('|')[0].split('.')[0])
                            }       

                results.append(dict_title)            
            '''
        
    data = json.dumps(results, indent=4)        
    with open(file_out, encoding='utf-8', mode='w') as f:
        json.dump(data, f)  

def get_json_files_in_same(file_in_1, file_in_2, file_out, playlist, description_title, source=''):

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
                         "playlist" : playlist.strip(),
                         "title": "{}".format(title.split('|')[2]),
                          "description": "{}\n{}{}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format( title.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title.split('|')[2]))
            results.append(dict_title)
        else:
            dict_title = {
                          "playlist" : playlist.strip(),
                         "title": "{}".format(title.split('|')[2]),
                          "description": "{}\n{} {}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format(title.split('|')[0].split('.')[0])
                        }       

            results.append(dict_title) 
        
    data = json.dumps(results, indent=4)        
    with open(file_out, encoding='utf-8', mode='w') as f:
        json.dump(data, f) 


def get_json_title(file_in_1, file_in_2, file_out, playlist, description_title, source=''):

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
        if len(title) > 100:
            dict_title = {
                         "playlist" : playlist.strip(),
                         "title": "{}".format(title),
                          "description": "{}\n{}{}".format(description_title, description, source), 
                           "id": "{}".format( title.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title.split('|')[2]))
            results.append(dict_title)
        else:
            dict_title = {
                          "playlist" : playlist.strip(),
                         "title": "{}".format(title.split('|')[2]),
                          "description": "{}\n{} {}".format(description_title, description.split('|')[2], source), 
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
        
        if len(title.strip()) > 100:
            dict_title = {
                         "playlist" : playlist.strip(),
                         "title": "{}".format(title),
                          "description": "{}\n{}{}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format( description.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title))
            results.append(dict_title)
        else:
       
            dict_title = {
                          "playlist" : playlist.strip(),
                         "title": "{}".format(title.split('|')[2].strip()),
                          "description": "{}\n{} {}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format(description.split('|')[0].split('.')[0])
                        }       

            results.append(dict_title)            
        
        
    data = json.dumps(results, indent=4)        
    with open(file_out, encoding='utf-8', mode='w') as f:
        json.dump(data, f)  

# convert result to json        
def get_json_fb_2(file_in_1, file_in_2, file_out, playlist, description_title, source=''):

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
        
        if len(title.strip()) > 100:
            dict_title = {
                         "playlist" : playlist.strip(),
                         "title": "{}".format(title),
                          "description": "{}\n{}{}".format(description_title, description.split('|')[2], source), 
                           "id": "{}".format( description.split('|')[0].split('.')[0] )
                        }       

            #print('{}။{} greater than 100'.format(change(counter), title.split('။')[1]))
            print('{} greater than 100'.format(title))
            results.append(dict_title)
        else:
       
            dict_title = {
                          "playlist" : playlist.strip(),
                         "title": "{}".format(title.strip()),
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
                    extra = '|%s' % (title.split('|')[3] if len(title.split('|')) > 0 else '')
                    f.write( '{}။{}{}\n'.format(change(counter), title.split('|')[2].split('။')[1], extra))
                else:
                    extra = '|%s' % (title.split('|')[3] if len(title.split('|')) > 0 else '')
                    f.write( '{}။{}{}\n'.format(change(counter), title.split('|')[2], extra ) ) 
                
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

def convert_myanmar_number_option(file_in, file_out, count=1, desc=None):

    file_in = running_from_path+file_in
    
    file_out = running_from_path+file_out
    
    titles = [title.strip('\n\n\n') for title in open(file_in)]
    
    
    if desc is None:
    
        with open(file_out, 'w') as f:
        
            def get_mp3_ext(file_mp3):
                return file_mp3.split('.')[1] # may be .mp3 of .MP3
                
            counter = count   
            #get_mp3_ext = title.split('|')[0].split('.')[1] 
            
            for title in titles:                       
                print(title)
                mp3_fomat = '{:03d}.{}'.format(counter, get_mp3_ext(title.split('|')[0])) 
                if title.split('|')[2].find('။') > 0: # found
                    #extra = '|%s' % (title.split('|')[3] if len(title.split('|')) > 0 else '')
                    f.write( '{}|{}|{}။{}\n'.format(mp3_fomat, title.split('|')[1], change(counter), title.split('|')[2].split('။')[1]))
                else:
                    #extra = '|%s' % (title.split('|')[3] if len(title.split('|')) > 0 else '')
                    f.write( '{}|{}|{}။{}\n'.format(mp3_fomat, title.split('|')[1], change(counter), title.split('|')[2]) ) 
                
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
                            #print('Error', err)
                            f.write('{}။{}|\n'.format(change(counter), title.split('|')[2]))
                            #print('{}။{}|\n'.format(change(counter), title.split('|')[2]))
                            
                        
                        #print('{}။{}'.format(change(counter), title))
                        
                        counter += 1                        
    

def check_duplicate(file_in):

    file_in = running_from_path+file_in
    
    
    urls = [url.split('|')[1] for url in open(file_in, encoding='utf8')]
    
    total = 0
    for key, val in collections.Counter(urls).items():
        if val > 1:
            total += 1 
            print(key, val)
            
    print('\ntotal duplicates ', total)
            
# check duplicate and do not add the latter            
def check_duplicate_option(file_in):

    file_in = running_from_path+file_in
    
    
    urls = [url.split('|')[1] for url in open(file_in)]
    new_urls = set()
    
    for key, val in collections.Counter(urls).items():        
        if val > 1:
            print(key, val)
    
    urls = [url.strip('\n') for url in open(file_in)]
    new_urls = set()    
    print('unique')
    for url in urls:
        new_url = url.split('|')[1]
        if new_url not in new_urls:
            new_urls.add(new_url)
            print(url)
            
def update_raw_titles_links(file_in, file_out, count=1):

    file_in = running_from_path+file_in
    #print(file_in)
    file_out = running_from_path+file_out
    
    lines = [f.strip('\n') for f in open(file_in)]
    
    with open(file_out, 'w') as f:
        counter = count
        for line in lines:
            #print(line)
            #print(line.split('|')[1])
            #media = line.split('|')[0]
            url = line.split('|')[1]
            ext = url.split('.')[-1]
            media = '{:03d}'.format(counter)
            title = line.split('|')[2]
            print(line)
            if title.find('။') > 0: # found
                extra = '|%s' % (line.split('|')[3] if len(line.split('|')) > 0 else '')
                f.write( '{}.{}|{}|{}။{}{}\n'.format(media, ext, url, change(counter), title.split('။')[1], extra))
            else:
                extra = '|%s' % (line.split('|')[3] if len(line.split('|')) > 0 else '')
                f.write( '{}.{}|{}|{}။{}{}\n'.format(media, ext, url, change(counter), title, extra ) ) 
    
            counter += 1
            
def update_raw_titles_links_option(file_in, file_out, count=1):

    file_in = running_from_path+file_in
    #print(file_in)
    file_out = running_from_path+file_out
    
    lines = [f.strip('\n') for f in open(file_in)]
    
    with open(file_out, 'w') as f:
        counter = count
        for line in lines:
            #print(line)
            #print(line.split('|')[1])
            #media = line.split('|')[0]
            url = line.split('|')[1]
            ext = url.split('.')[-1]
            media = '{:03d}'.format(counter)
            title = line.split('|')[2]
            print(line)
            if title.find('။') > 0: # found
                #extra = '|%s' % (line.split('|')[2] if len(line.split('|')) > 0 else '')
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title.split('။')[1]))
            else:
                #extra = '|%s' % (line.split('|')[2] if len(line.split('|')) > 0 else '')
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title) ) 
    
            counter += 1 

def update_raw_titles_links_mp3_and_title(file_in, file_out, count=1):

    file_in = running_from_path+file_in
    #print(file_in)
    file_out = running_from_path+file_out
    
    lines = [f.strip('\n') for f in open(file_in)]
    
    with open(file_out, 'w') as f:
        counter = count
        for line in lines:
            #print(line)
            #print(line.split('|')[1])
            #media = line.split('|')[0]
            url = line.split('|')[1]
            ext = url.split('.')[-1]
            media = '{:03d}'.format(counter)
            title = line.split('|')[2]
            print(line)
            if title.find('။') > 0: # found
                #extra = '|%s' % (line.split('|')[2] if len(line.split('|')) > 0 else '')
                f.write( '{}.{}|{}|{}။{}\n'.format(media, ext, url, change(counter), title.split('။')[1]))
            else:
                #extra = '|%s' % (line.split('|')[2] if len(line.split('|')) > 0 else '')
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
            #if ['.mp3', '.MP3'] in key.get('href'):
            if '.mp3' in key.get('href') or '.MP3' in key.get('href') or '.wma' in key.get('href'):
                mp3_type = key.get('href').split('/')[-1].split('.')[-1]
                counter = '{:03d}'.format(count)
                fd.write('{}.{}|{}|{}\n'.format(counter, mp3_type, ''.join(key.get('href').split()), ' '.join(key.get_text().split())))

                count += 1
                
def get_html_mp3_option(file_in, file_out, url, count=1):

    file_in = running_from_path+file_in
    
    file_out = running_from_path+file_out

    text = open(file_in, 'r').read()

    soup = bs4(text, 'html.parser')
    
        
    count = count
    
    with open(file_out, 'w') as fd:

        for key in soup.find_all('a'):
            
            #if ['.mp3', '.MP3'] in key.get('href'):
            if '.mp3' in key.get('href') or '.MP3' in key.get('href'):
                #print(type(key.findChild()))
                '''
                try:
                    # string = string.replace('\r', '').replace('\n', '')
                    ss = ' '.join(key.findChild().get_text().splitlines())
                    ss_two = ss.replace('\r', '').replace('\n', '')
                    #print(key.findChild())
                    #print(key)
                    mp3_type = key.get('href').split('/')[-1].split('.')[-1]
                    counter = '{:03d}'.format(count)
                    fd.write('{}.{}|{}{}|{}\n'.format(counter, mp3_type, url,''.join(key.get('href').split()), ss_two))                 
                    #fd.write('{}.{}|{}{}|{}\n'.format(counter, mp3_type, url,''.join(key.get('href').split()), ' '.join(key.get_text().split())))   
                    #count += 1  
                except AttributeError as err:
                    pass
                '''
                mp3_type = key.get('href').split('/')[-1].split('.')[-1]
                counter = '{:03d}'.format(count)
                fd.write('{}.{}|{}{}|{}\n'.format(counter, mp3_type, url,''.join(key.get('href').split()), ' '.join(key.get_text().split())))

                count += 1                
                
                
'''
if __name__ == '__main__':
    get_html_mp4('get_url.txt', 3)
'''
                



