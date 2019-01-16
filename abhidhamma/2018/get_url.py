from bs4 import BeautifulSoup as bs4
import re
text = """

									<tbody><tr>
										<td width="288" bgcolor="#CC3399" align="center">

<font face="Zawgyi-One">






										<p align="center">
								<font size="4" face="Zawgyi-One" color="#FFFFFF">ပထမအဆင္႔</font></p></font><p align="center"><font face="Zawgyi-One">
								<font size="4" color="#FFFFFF">အနီးကပ္ သင္တန္း 
								၂၀၁၈</font></font></p><p>&nbsp;</p></td>
										<td width="292" bgcolor="#CC3399" align="center">

<font face="Zawgyi-One">






										<font size="4" color="#FFFFFF">ဒုတိယအဆင္႔</font></font><p><font face="Zawgyi-One">
										<font size="4" face="Zawgyi-One" color="#FFFFFF">
										အနီးကပ္ သင္တန္း ၂၀၁၈</font></font></p><p>&nbsp;</p></td>
										<td bgcolor="#CC3399" align="center">

<font face="Zawgyi-One">






										<font size="4" color="#FFFFFF">
										တတိယအဆင္႕</font></font><p><font face="Zawgyi-One">
										<font size="4" face="Zawgyi-One" color="#FFFFFF">
										အနီးကပ္ သင္တန္း ၂၀၁၈</font></font></p><p>&nbsp;</p></td>
									</tr>
									<tr>
										<td width="288" align="center">
										<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">စိတ္ - ၁၀နာရီ၊ 
								၄၉မိနစ္</font></p><p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ေစတသိက္ - ၁၃နာရီ၊ 
								၂၆မိနစ္</font></p><p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ပကိဏ္း - ၈နာရီ၊ 
								၂၃မိနစ္</font></p><p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">စုစုေပါင္း - ၃၃ နာရီ ၃၈မိနစ္</font></p></td>
										<td width="292" align="center">
										&nbsp;</td>
										<td align="center">
										&nbsp;</td>
									</tr>
									<tr>
										<td width="288" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-16.mp4">
								၁) ၁၆-၁၀-၂၀၁၈ ပကိဏ္းအနီးကပ္ (၁)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-27-23to330.mp4">၁) 
										၂၇-၁၀-၂၀၁၈ ၀ီထိအနီးကပ္ (၁)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-21-200to330.mp4">
								၁) ၂၁-၁၀-၂၀၁၈ ပစၥည္းအနီးကပ္ (၁)</a></font></td>
									</tr>
									<tr>
										<td width="288" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-17.mp4">
								၂) ၁၇-၁၀-၂၀၁၈ ပကိဏ္းအနီးကပ္ (၂)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-28-200to330.mp4">၂) 
										၂၈-၁၀-၂၀၁၈ ၀ီထိအနီးကပ္ (၂)</a></font></td>
										<td>

<font face="Zawgyi-One">






								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-10-21-345To515.mp4">
								၂) <font size="4">၂၁-၁၀-၂၀၁၈ 
								ပစၥည္းအနီးကပ္ (၂)</font></a></font></td>
									</tr>
									<tr>
										<td width="288" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-18.mp4">
								၃) ၁၈-၁၀-၂၀၁၈ ပကိဏ္းအနီးကပ္ (၃)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-3-2to330.mp4">၃) 
										၃-၁၁-၂၀၁၈ ၀ီထိအနီးကပ္ (၃)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-27-345to515.mp4">၃) ၂၇-၁၀-၂၀၁၈ 
										ပစၥည္းအနီးကပ္ (၃)</a></font></td>
									</tr>
									<tr>
										<td width="288" height="49" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-20.mp4">
								၄) ၂၀-၁၀-၂၀၁၈ ပကိဏ္းအနီးကပ္ (၄)</a></font></td>
										<td width="292" height="49">
										<font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-04-2-1.mp4">၄) ၄-၁၁-၂၀၁၈ ၀ီထိအနီးကပ္ 
										(၄)</a></font></td>
										<td height="49"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-28-345to515.mp4">၄) 
										၂၈-၁၀-၂၀၁၈ ပစၥည္းအနီးကပ္ (၄)</a></font></td>
									</tr>
									<tr>
										<td width="288" height="41" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-21-12to130.mp4">၅) ၂၁-၁၀-၂၀၁၈ ပကိဏ္းအနီးကပ္ (၅)</a></font></td>
										<td width="292" height="41">
										<font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-10-2to330.mp4">၅) ၁၀-၁၁-၂၀၁၈ ၀ီထိအနီးကပ္ 
										(၄)</a></font></td>
										<td height="41"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-3-345to515.mp4">၅) 
										၃-၁၁-၂၀၁၈ ပစၥည္းအနီးကပ္ (၅)</a></font></td>
									</tr>
									<tr>
										<td width="288"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-27-12to130.mp4">၆) 
										၂၇-၁၀-၂၀၁၈ ေစတသိက္အနီးကပ္ (၁)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-11-200To330.mp4">
										၆) ၁၁-၁၁-၂၀၁၈ ဘုံပိုင္းအနီးကပ္ (၁) </a>
										</font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-04-3.mp4">၆) ၄-၁၁-၂၀၁၈ 
										ပစၥည္းအနီးကပ္ (၆)</a></font></td>
									</tr>
									<tr>
										<td width="288"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-28-12to130.mp4">၇) 
										၂၈-၁၀-၂၀၁၈ ေစတသိက္အနီးကပ္ (၂)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-17-12To130.mp4">
										၇) ၁၇-၁၁-၂၀၁၈ ဘုံပိုင္းအနီးကပ္ (၂)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-10-345To5.mp4">၇) ၁၀-၁၁-၂၀၁၈ 
										သမုစၥည္း အနီးကပ္ (၁)</a></font></td>
									</tr>
									<tr>
										<td width="288"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-30.mp4">၈) 
										၃၀-၁၀-၂၀၁၈ ေစတသိက္အနီးကပ္ (၃)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-17-2to330.mp4">
										၈) ၁၇-၁၁-၂၀၁၈ ဘုံပိုင္းအနီးကပ္ (၃)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-11-345To500.mp4">
										၈) ၁၁-၁၁-၂၀၁၈ သမုစၥည္း အနီးကပ္ (၂)</a></font></td>
									</tr>
									<tr>
										<td width="288"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-10-31.mp4">၉) 
										၃၁-၁၀-၂၀၁၈ ေစတသိက္အနီးကပ္ (၄)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-18-12To130.mp4">
										၉) ၁၈-၁၁-၂၀၁၈ ဘုံပိုင္းအနီးကပ္ (၄)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-17-345To500.mp4">
										၉) ၁၇-၁၁-၂၀၁၈ သမုစၥည္း အနီးကပ္ (၃)</a></font></td>
									</tr>
									<tr>
										<td width="288"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-1-1.mp4">၁၀) 
										၁-၁၁-၂၀၁၈ ေစတသိက္အနီးကပ္ (၅)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-18-2To330.mp4">
										၁၀) ၁၈-၁၁-၂၀၁၈ ဘုံပိုင္းအနီးကပ္ (၅)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-18-345To515.mp4">
										၁၀) ၁၈-၁၁-၂၀၁၈ သမုစၥည္း အနီးကပ္ (၄)</a></font></td>
									</tr>
									<tr>
										<td width="288">
										<p style="line-height: 100%">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-3-12to130.mp4">
										<font size="4">၁၁) 
										၃-၁၁-၂၀၁၈ စိတ္အနီးကပ္ (၁)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										</font></a></p></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-24-12To130.mp4">
										၁၁) ၂၄-၁၁-၂၀၁၈ ရုပ္္ပိုင္းအနီးကပ္ (၁)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-24-345to500.mp4">
										၁၁) ၂၄-၁၁-၂၀၁၈ ကမၼ႒ာန္းအနီးကပ္ (၁)</a></font></td>
									</tr>
									<tr>
										<td width="288"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-04-1-1.mp4">၁၂) 
										၄-၁၁-၂၀၁၈ စိတ္အနီးကပ္ (၂)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-24-2to330.mp4">
										၁၂) ၂၄-၁၁-၂၀၁၈ ရုပ္္ပိုင္းအနီးကပ္ (၂)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-25-345to500.mp4">
										၁၂) ၂၅-၁၁-၂၀၁၈ ကမၼ႒ာန္းအနီးကပ္ (၂)</a></font></td>
									</tr>
									<tr>
										<td width="288">
										<font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-08.mp4">
										၁၃) ၈-၁၁-၂၀၁၈စိတ္အနီးကပ္ (၃)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-25-12to130.mp4">
										၁၃) ၂၅-၁၁-၂၀၁၈ ရုပ္္ပိုင္းအနီးကပ္ (၃)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-12-01-2to330.mp4">
										၁၃) ၁-၁၂-၂၀၁၈ ကမၼ႒ာန္းအနီးကပ္ (၃)</a></font></td>
									</tr>
									<tr>
										<td width="288">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-10-12To130-1.mp4">






										<font size="4">၁၄) ၁၀-၁၁-၂၀၁၈ </font>
										<font size="4" face="Zawgyi-One">
										စိတ္အနီးကပ္ </font></a></font>
<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-10-12To130-1.mp4">
<font size="4">(၄)</font></a></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-11-25-2to330.mp4">
										၁၄) ၂၅-၁၁-၂၀၁၈ ရုပ္္ပိုင္းအနီးကပ္ (၄)</a></font></td>
										<td><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-12-01-345to5.mp4">
										၁၄) ၁-၁၂-၂၀၁၈ ကမၼ႒ာန္းအနီးကပ္ (၄)</a></font></td>
									</tr>
									<tr>
										<td width="288">

<font size="4">
<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-Revision-2018-11-11-12To130.mp4">
၁၅) ၁၁-၁၁-၂၀၁၈ စိတ္အနီးကပ္ (၅)</a></font></td>
										<td width="292"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/Revision/Dawkhinhlatin-Abhidhamma-revision-2018-12-01-12to130.mp4">
										၁၅) ၁-၁၂-၂၀၁၈ ရုပ္္ပိုင္းအနီးကပ္ (၅)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="288">&nbsp;</td>
										<td width="292">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
								</tbody>
"""

soup = bs4(text, 'html.parser')

p = re.compile(r'(?P<word>[^0-9]+)')

#print(p)
count = 1
for key in soup.find_all('tr'):
    try:
        counter = '{:03d}'.format(count)
        #print(" ".join(key.find('td').find('a').get_text().strip().split()))
        print('{}.mp4|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), 
            " ".join(key.find('td').find('a').get_text().strip().split())            
            ))
        count += 1
    except AttributeError as err:
        pass
for key in soup.find_all('tr'):        
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp4|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find('a').get('href'), 
        " ".join(key.find('td').find_next_sibling('td').find('a').get_text().strip().split()) 
            ))
        count += 1
    except AttributeError as err:
        pass
for key in soup.find_all('tr'):        
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp4|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get('href'), 
        " ".join(key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get_text().strip().split()) ))
        count += 1
    except AttributeError as err:
        pass    
        
    
        


    
    '''
    if not key.find('td', attrs={'width':"243"}):
        continue
    elif not key.find('td', attrs={'width':"238"}):
        #print(key.find('td', attrs={'width':"238"}))
        try:
            if count == 124:
                count += 1
                pass
            else:
                if ".mp4" in key.find('td', attrs={'width':"238"}).find('a').get('href'):
                    key = key.find('td', attrs={'width':"238"}).find('a')
                    #print(key)
                    counter = '{:03d}'.format(count)
                    print('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text().strip().rstrip()))
                    count += 1
    
        except AttributeError as err:
            pass
            
    else:
        print(key)
    '''
    #print(key.find('td', attrs={'':""}))
    

'''
with open('titles_links.txt', 'w') as f:
    count = 1
    for key in soup.find_all('a'):
        if ".mp4" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text().strip().rstrip()))
            #f.write('{}\n'.format(key.get_text()))
            count += 1
'''      
            
"""        
with open('file.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get('href')))

with open('titles.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get_text()))        
"""
