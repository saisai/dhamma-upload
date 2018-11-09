from bs4 import BeautifulSoup as bs4


text = """
<p>၁။ အသုဘကမၼဌာန္း(၁) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-1.mp3">Download</a><br />၂။ အသုဘကမၼဌာန္း(၂) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-2.mp3">Download</a><br />၃။ ကံတရားႏွင့္၀ိပႆနာတရားေတာ္ <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-3.mp3">Download</a><br />၄။ မိုးအဆံုးေျမအဆံုးရွာသူ (ျမင္းမုိရ္ေတာင္ႏွင့္စၾကာၤ၀ဠာတည္ေနပံု) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-4.mp3">Download </a><br />၅။ ေမတၱာတရားႏွင့္ပရိတ္တရား(၁) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-5.mp3">Download</a><br />၆။ ေမတၱာတရားႏွင့္ပရိတ္တရား(၂) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-6.mp3">Download</a><br />၇။ ပရိတ္ႏွင့္သိမွတ္စရာမ်ား(၁) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-7.mp3">Download</a><br />၈။ ပရိတ္ႏွင့္သိမွတ္စရာမ်ား(၂) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-8.mp3">Download</a><br />၉။ ပရိတ္ႏွင့္သိမွတ္စရာမ်ား(၃) <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-9.mp3">Download</a><br />၁၀။ ေရေမတၱာႏွင့္ပရိတ္တရားေတာ္ <a href="http://www.dhammaransi.info/Audio/Dhamma2/UOttamasara-DhammaTalk-10.mp3">Download</a></p>
<p>၁။ ကံတရားႏွင့္ မီးကြင္းပရိတ္ (၁) <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-21.mp3">Download</a><br />၂။ ကံတရားႏွင့္ မီးကြင္းပရိတ္ (၂) <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-22.mp3">Download</a><br />၃။ မိဘေက်းဇူးတရားေဒသနာေတာ္ (၁) <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-23.mp3">Download</a><br />၄။ မိဘေက်းဇူးတရားေဒသနာေတာ္ (၂) <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-24.mp3">Download</a><br />၅။ ႏြားေမတၱာစာတရားေတာ္ <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-25.mp3">Download</a><br />၆။ သံသရာက်င္လည္ေနနည္း (၁) <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-26.mp3">Download</a><br />၇။ သံသရာက်င္လည္ေနနည္း (၂) <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-27.mp3">Download</a><br />၈။ သာဓိကမင္းၾကီးတရားေတာ္ <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-28.mp3">Download</a><br />၉။ ၀ိပႆနာအလုပ္ေပးတရားေတာ္ <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-29.mp3">Download</a><br />၁၀။ ေရဆူပရိတ္၊ ဂုဏ္ေတာ္ကြန္ျခာ၊ ကမၼ၀ါ <a href="http://www.dhammaransi.net/Audio/Dhamma2/UOttamasara-DhammaTalk-30.mp3">Download</a></p></div></div></article></div>
"""
'''
soup = bs4(text, 'html.parser')
import json
#for key in soup:
cc = 1
for key in soup:
    #print(type(key))
    #if cc < 100:
    if not list(key) == ['\n']:        
        for kk in list(key):
            print(kk)
'''

'''
not being used
soup = bs4(text, 'html.parser')
with open('titles_links.txt', 'w') as f:
    count = 1
    for key in soup.find_all('a'):
        #print(key)
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
            #f.write('{}\n'.format(key.get_text()))
            count += 1
'''

'''
titles = [c for c in open('cc.txt')]
for line in titles:
    if line != "":
        #if 'mp3' in line and len(line) > 1:
        if 'mp3' not in line and len(line) > 1:
        #if len(line) > 2:
            print(line, end='')
            #print(len(line))
            #print(line, end='')
'''


mm = [mm.strip('\n') for mm in open('new_title_links_mm.txt')]            
links = [link.strip('\n') for link in open('new_title_links_link.txt')]     

count = 11
with open('titles_links.txt', 'w') as out:
    for m, l in zip(mm, links):
        
        out.write('{:03}.mp3|{}|{}\n'.format(count, l, m))
        
        count += 1 
