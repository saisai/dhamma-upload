from bs4 import BeautifulSoup as bs4
import re
text = """
									<tbody><tr>
										<td colspan="3">
										<p align="center">
										<font size="4" face="Zawgyi-One" color="#FFFFFF">
										<span style="background-color: #CC3399">
										ဒုတိယအဆင္႔ (၂၀၁၀)</span></font></p></td>
									</tr>
									<tr>
										<td width="243" bgcolor="#CC3399" align="center">
										<p align="center">
										<font size="4" color="#FFFFFF">
										ဝီထိပိုင္း (၂၀၁၀)</font></p></td>
										<td width="238" bgcolor="#CC3399" align="center">
										<p align="center">
										<font size="4" color="#FFFFFF">
										ဝီထိမုတ္ပိုင္း (၂၀၁၀)</font></p></td>
										<td bgcolor="#CC3399" align="center">
										<font size="4" color="#FFFFFF">
										ရုပ္ပိုင္း (၂၀၁၀)</font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/079-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(1)-13-3-2010.mp4">၇၉။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁) 
ဆိုရိုး ၁၃-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/114-Dawkhinhlatin-Vihtimutta01-1.mp4">
								၁၁၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/145-Dawkhinhlatin-%20Rupa%2001-1.mp4">
										၁၄၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/080-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(2)-13-3-2010.mp4">၈၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂) 
အဓိပၸါယ္ ၁၃-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/115-Dawkhinhlatin-Vihtimutta02-1.mp4">
								၁၁၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/146-Dawkhinhlatin-%20Rupa%2002-1.mp4">
										၁၄၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/081-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(3)-14-3-2010.mp4">၈၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃) 
အဓိပၸါယ္ ၁၄-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/116-Dawkhinhlatin-Vihtimutta03-1.mp4">
								၁၁၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/147-Dawkhinhlatin-%20Rupa%2003-1.mp4">
										၁၄၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/082-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(4)-14-3-2010.mp4">၈၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄) 
အဓိပၸါယ္ ၁၄-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/117-Dawkhinhlatin-Vihtimutta04-1.mp4">
								၁၁၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/148-Dawkhinhlatin-%20Rupa%2004-1.mp4">
										၁၄၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/083-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(5)-20-3-2010.mp4">၈၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅) 
အဓိပၸါယ္ ၂၀-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/118-Dawkhinhlatin-Vihtimutta05-1.mp4">
								၁၁၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/149-Dawkhinhlatin-%20Rupa%2005-1.mp4">
										၁၄၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/084-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(6)-20-3-2010.mp4">၈၄။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆) 
ဆိုရိုး ၂၀-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/119-Dawkhinhlatin-Vihtimutta06-1.mp4">
								၁၁၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/150-Dawkhinhlatin-%20Rupa%2006-1.mp4">
										၁၅၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/085-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(7)-21-3-2010.mp4">၈၅။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၇) 
ဆိုရိုး ၂၁-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/120-Dawkhinhlatin-Vihtimutta07-1.mp4">
								၁၂၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/151-Dawkhinhlatin-%20Rupa%2007-1.mp4">
										၁၅၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/086-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(8)-21-3-2010.mp4">၈၆။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၈) 
ဆိုရိုး ၂၁-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/120-Dawkhinhlatin-Vihtimutta07-1.mp4">
								၁၂၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၈)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/152-Dawkhinhlatin-%20Rupa%2008-1.mp4">
										၁၅၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၈)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/087-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(9)-27-3-2010.mp4">၈၇။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၉) 
အဓိပၸါယ္ ၂၇-၃-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/122-Dawkhinhlatin-Vihtimutta09-1.mp4">
								၁၂၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၉)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/153-Dawkhinhlatin-%20Rupa%2009-1.mp4">
										၁၅၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၉)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/088-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(10)-10-5-2010.mp4">၈၈။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၀) 
ဆိုရိုး ၁၁-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/123-Dawkhinhlatin-Vihtimutta10-1.mp4">
								၁၂၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၀)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/154-Dawkhinhlatin-%20Rupa%2010-1.mp4">
										၁၅၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၀)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/089-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(11)-12-5-2010.mp4">၈၉။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၁) 
အဓိပၸါယ္ ၁၂-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">၁၂၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ 
								ဝီထိမုတ္ပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၁)</font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/155-Dawkhinhlatin-%20Rupa%2011-1.mp4">
										၁၅၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၁)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/090-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(12)-18-5-2010.mp4">၉၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၂) 
အဓိပၸါယ္ ၁၈-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/125-Dawkhinhlatin-Vihtimutta12-1.mp4">
								၁၂၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၂)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/156-Dawkhinhlatin-%20Rupa%2012-1.mp4">
										၁၅၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၂)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/091-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(13)-19-5-2010.mp4">၉၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၃) 
ဆိုရိုး ၁၉-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/126-Dawkhinhlatin-Vihtimutta13-1.mp4">
								၁၂၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၃)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/157-Dawkhinhlatin-%20Rupa%2013-1.mp4">
										၁၅၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၃)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/092-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(13)-25-5-2010.mp4">၉၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၄) 
အဓိပၸါယ္ ၂၅-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/127-Dawkhinhlatin-Vihtimutta14-1.mp4">
								၁၂၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၄)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/158-Dawkhinhlatin-%20Rupa%2014-1.mp4">
										၁၅၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၄)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/093-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(15)-26-5-2010.mp4">၉၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၅) 
ဆိုရိုး ၂၆-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/128-Dawkhinhlatin-Vihtimutta15-1.mp4">
								၁၂၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၅)</a></font></td>
										<td>
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/159-Dawkhinhlatin-%20Rupa%2015-1.mp4">
										၁၅၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၅)</a></font></td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/094-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(16)-1-6-2010.mp4">၉၄။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၆) 
ဆိုရိုး ၂၆-၅-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/129-Dawkhinhlatin-Vihtimutta16-1.mp4">
								၁၂၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၆)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/095-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(17)-2-6-2010.mp4">၉၅<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၇) 
ဆိုရိုး ၆-၆-၂၀၁၀</font></a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/130-Dawkhinhlatin-Vihtimutta17-1.mp4">
								၁၃၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၇)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DawKhinHlaTin/abhidhamma-special-2009-2010/096-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(18)-8-6-2010.wmv">
၉၆။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၈) ဆိုရိုး ၈-၆-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/131-Dawkhinhlatin-Vihtimutta18-1.mp4">
								၁၃၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၈)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/097-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(19)-9-6-2010.mp4">၉၇။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၉) အဓိပၸါယ္ ၉-၆-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/132-Dawkhinhlatin-Vihtimutta19-1.mp4">
								၁၃၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၉)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/098-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(20)-15-6-2010.mp4">၉၈<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၀) 
ဆိုရိုး ၁၅-၆-၂၀၁၀</font></a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/133-Dawkhinhlatin-Vihtimutta20-1.mp4">
								၁၃၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၀)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/099-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(21)-16-6-2010.mp4">၉၉<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၁) 
အဓိပၸါယ္ ၁၆-၆-၂၀၁၀</font></a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/134-Dawkhinhlatin-Vihtimutta21-1.mp4">
								၁၃၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၁)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/100-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(22)-22-6-2010.mp4">၁၀၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၂) ဆိုရိုး ၂၂-၆-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/135-Dawkhinhlatin-Vihtimutta22-1.mp4">
								၁၃၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၂)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/101-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(23)-23-6-2010.mp4">၁၀၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၃) အဓိပၸါယ္ ၂၃-၆-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/136-Dawkhinhlatin-Vihtimutta23-1.mp4">
								၁၃၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၃)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/102-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(24)-29-6-2010.mp4">၁၀၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၄) ဆိုရိုး ၂၉-၆-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/137-Dawkhinhlatin-Vihtimutta24-1.mp4">
								၁၃၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၄)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/103-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(25)-30-6-2010.mp4">၁၀၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၅) အဓိပၸါယ္ ၃၀-၆-၂၀၁၀</a></font></td>
										<td width="238">

<font face="Zawgyi-One">






								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/138-Dawkhinhlatin-Vihtimutta25-1.mp4">
								၁၃၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၅)</a></font></p>
</font>

										<p>&nbsp;</p></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/104-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(26)-6-7-2010.mp4">၁၀၄။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၆) ဆိုရိုး ၆-၇-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/139-Dawkhinhlatin-Vihtimutta26-1.mp4">
								၁၃၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၆)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/105-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(27)-7-7-2010.mp4">၁၀၅<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၇) 
ဆိုရိုး ၇-၇-၂၀၁၀</font></a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/140-Dawkhinhlatin-Vihtimutta27-1.mp4">
								၁၄၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၇)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/106-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(28)-13-7-2010.mp4">၁၀၆<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၈) 
အဓိပၸါယ္ ၁၃-၇-၂၀၁၀</font></a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/141-Dawkhinhlatin-Vihtimutta28-1.mp4">
								၁၄၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၈)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/107-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(29)-14-7-2010.mp4">၁၀၇။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၉) အဓိပၸါယ္ ၁၄-၇-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/142-Dawkhinhlatin-Vihtimutta29-1.mp4">
								၁၄၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၉)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/108-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(30)-20-7-2010.mp4">၁၀၈။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၀) အဓိပၸါယ္ ၂၀-၇-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/143-Dawkhinhlatin-Vihtimutta30-1.mp4">
								၁၄၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃၀)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/109-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(31)-21-7-2010.mp4">၁၀၉။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၁) အဓိပၸါယ္ ၂၁-၇-၂၀၁၀</a></font></td>
										<td width="238">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/144-Dawkhinhlatin-Vihtimutta31-1.mp4">
								၁၄၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃၁)</a></font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/110-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(32)-27-7-2010.mp4">၁၁၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၂) အဓိပၸါယ္ ၂၇-၇-၂၀၁၀</a></font></td>
										<td width="238">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/111-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(33)-28-7-2010.mp4">၁၁၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၃) အဓိပၸါယ္ ၂၈-၇-၂၀၁၀</a></font></td>
										<td width="238">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/112-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(34)-3-8-2010.mp4">၁၁၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၄) အဓိပၸါယ္၃-၈-၂၀၁၀</a></font></td>
										<td width="238">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/113-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(35)-4-8-2010.mp4">၁၁၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၅) အဓိပၸါယ္ ၄-၈-၂၀၁၀</a></font></td>
										<td width="238">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">&nbsp;</td>
										<td width="238">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="243">&nbsp;</td>
										<td width="238">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
								</tbody>
"""

soup = bs4(text, 'html.parser')

p = re.compile(r'(?P<word>[^0-9]+)')

#print(p)
count = 145
for key in soup.find_all('tr'):
    try:
        if key.find('td').find_next_sibling('td').find_next_sibling('td'):
            key = key.find('td').find_next_sibling('td').find_next_sibling('td')
            try:
                if ".mp4" in key.find('a').get('href'):
                    key = key.find('a')
                    #print(key)
                    counter = '{:03d}'.format(count)
                    print('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text().strip().rstrip()))
                    count += 1

            except AttributeError as err:
                pass    
                
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
