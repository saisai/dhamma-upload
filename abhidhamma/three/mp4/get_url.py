from bs4 import BeautifulSoup as bs4
import re
text = """
									<tbody><tr>
										<td colspan="3">
										<p align="center">
										<span style="background-color: #FFCC00">
										<font size="4">တတိယအဆင္႔</font></span></p></td>
									</tr>
									<tr>
										<td width="285" bgcolor="#FFCC00">
										<p align="center"><font size="4">
										သမုပစၥည္းပိုင္း</font></p></td>
										<td width="301" bgcolor="#FFCC00" align="center">
										<font size="4">ပစၥည္းပိုင္း 
										(၂၀၁၂)</font></td>
										<td bgcolor="#FFCC00" align="center">
										<font size="4">ကမၼ႒ာန္းပိုင္း</font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/160-Dawkhinhlatin-Thamotesi-01.1.mp4">၁၆၀။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁) ဆိုရိုး</a></font></td>
										<td width="301"><font size="4">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/187-Dawkhinhlatin-187-Dawkhinhlatin-47-05-PyitSi-01-A-PaTateSa-Start.mp4">
										၁၈၇။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁) ဆိုရိုး</a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/230-Dawkhinhlatin-230-Dawkhinhlatin-52-01.mp4">
										<font size="4">၂၃၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										(ေခါင္းစဥ္)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/161-Dawkhinhlatin-Thamotesi-01.mp4">၁၆၁။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁)</a> </font>
										</td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/188-Dawkhinhlatin-188-Dawkhinhlatin-47-06-PyitSi-01-B.mp4">
										၁၈၈။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/231-Dawkhinhlatin-231-Dawkhinhlatin-52-02-KaMaHtan-A.mp4">
										<font size="4">၂၃၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁) </font><font size="4">
										ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/162-Dawkhinhlatin-Thamotesi-2.1.mp4">၁၆၂။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂) ဆိုရိုး</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/189-Dawkhinhlatin-189-Dawkhinhlatin-47-07-PyitSi-02-A.mp4">
										၁၈၉။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/232-Dawkhinhlatin-232-Dawkhinhlatin-52-03-KaMaHtan-B1.mp4">
										<font size="4">၂၃၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/163-Dawkhinhlatin-Thamotesi-2.mp4">၁၆၃။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂)</a> </font>
										</td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/190-Dawkhinhlatin-190-Dawkhinhlatin-47-08-PyitSi-02-B.mp4">
										၁၉၀။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/233-Dawkhinhlatin-233-Dawkhinhlatin-52-04KaMaHtan-B2.mp4">
										<font size="4">၂၃၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/164-Dawkhinhlatin-Thamotesi-3.1.mp4">၁၆၄။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃) ဆိုရိုး</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/191-Dawkhinhlatin-191-Dawkhinhlatin-48-01-PyitSi-03-A.mp4">
										၁၉၁။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃) ဆိုရိုး</a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/234-Dawkhinhlatin-234-Dawkhinhlatin-52-05.mp4">
										<font size="4">၂၃၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၂) </font><font size="4">
										ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/165-Dawkhinhlatin-Thamotesi-3.mp4">၁၆၅။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃)</a> </font>
										</td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/192-Dawkhinhlatin-192-Dawkhinhlatin-48-02-PyitSi-03-B1.mp4">
										၁၉၂။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/235-Dawkhinhlatin-235-Dawkhinhlatin-52-06.mp4">
										<font size="4">၂၃၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၂) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/166-Dawkhinhlatin-Thamotesi-4.mp4">၁၆၆။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄) ဆိုရိုး</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/193-Dawkhinhlatin-193-Dawkhinhlatin-48-03-PyitSi-03-B2.mp4">
										၁၉၃။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/236-Dawkhinhlatin-236-Dawkhinhlatin-52-07.mp4">
										<font size="4">၂၃၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၂) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/167-Dawkhinhlatin-Thamotesi-4(2).mp4">၁၆၇။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄)</a> </font>
										</td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/194-Dawkhinhlatin-194-Dawkhinhlatin-48-04-PyitSi-04-A.mp4">
										၁၉၄။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄) ဆိုရိုး</a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/237-Dawkhinhlatin-237-Dawkhinhlatin-52-08.mp4">
										<font size="4">၂၃၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၃) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/168-Dawkhinhlatin-Thamotesi-5.1.mp4">၁၆၈။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅) 
										ဆိုရိုး</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/195-Dawkhinhlatin-195-Dawkhinhlatin-48-05-PyitSi-04-B1.mp4">
										၁၉၅။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/238-Dawkhinhlatin-238-Dawkhinhlatin-52-09.mp4">
										<font size="4">၂၃၈</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၃) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/169-Dawkhinhlatin-Thamotesi-5.mp4">၁၆၉။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅)</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/196-Dawkhinhlatin-196-Dawkhinhlatin-48-06-PyitSi-04-B2.mp4">
										၁၉၆။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/239-Dawkhinhlatin-239-Dawkhinhlatin-52-10.mp4">
										<font size="4">၂၃၉</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၃) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/170-Dawkhinhlatin-Thamotesi-6.mp4">၁၇၀။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆)</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/197-Dawkhinhlatin-197-Dawkhinhlatin-48-07-PyitSi-05-A1.mp4">
										၁၉၇။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅) ဆိုရိုး</a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/240-Dawkhinhlatin-240-Dawkhinhlatin-52-11.mp4">
										<font size="4">၂၄၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၄)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/171-Dawkhinhlatin-Thamotesi-7.1.mp4">၁၇၁။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇) 
										ဆိုရိုး</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/198-Dawkhinhlatin-198-Dawkhinhlatin-48-08-PyitSi-05-A2.mp4">
										၁၉၈။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/241-Dawkhinhlatin-241-Dawkhinhlatin-52-12.mp4">
										<font size="4">၂၄၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၄)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/172-Dawkhinhlatin-Thamotesi-7.mp4">၁၇၂။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇)</a></font></td>
										<td width="301">
										<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/199-Dawkhinhlatin-199-Dawkhinhlatin-48-09-PyitSi-05-B.mp4">
										၁၉၉။ တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅) </a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/242-Dawkhinhlatin-242-Dawkhinhlatin-53-01.mp4">
										<font size="4">၂၄၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										(ေခါင္းစဥ္)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/173-Dawkhinhlatin-Thamotesi-8.1.mp4">၁၇၃။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၈) 
										ဆိုရိုး</a></font></td>
										<td width="301">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/200-Dawkhinhlatin-200-Dawkhinhlatin-48-10-PyitSi-06-A.mp4">
										<font size="4">၂၀၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆) ဆိုရိုး</font></a></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/243-Dawkhinhlatin-243-Dawkhinhlatin-53-02.mp4">
										<font size="4">၂၄၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၄) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/174-Dawkhinhlatin-Thamotesi-8.mp4">၁၇၄။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၈)</a></font></td>
										<td width="301">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/201-Dawkhinhlatin-201-Dawkhinhlatin-48-11-PyitSi-06-B1.mp4">
										<font size="4">၂၀၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆) </font></a></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/244-Dawkhinhlatin-244-Dawkhinhlatin-53-03.mp4">
										<font size="4">၂၄၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၅)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/175-Dawkhinhlatin-Thamotesi-9.mp4">၁၇၅။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၉) 
										ဆိုရိုး</a></font></td>
										<td width="301">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/202-Dawkhinhlatin-202-Dawkhinhlatin-48-12-PyitSi-06-B2.mp4">
										<font size="4">၂၀၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆) </font></a></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/245-Dawkhinhlatin-245-Dawkhinhlatin-53-04.mp4">
										<font size="4">၂၄၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၅)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/176-Dawkhinhlatin-Thamotesi-9(2).mp4">၁၇၆။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၉)</a></font></td>
										<td width="301">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/203-Dawkhinhlatin-203-Dawkhinhlatin-49-01-PyitSi-07-A-PaTateSa.mp4">
										<font size="4">၂၀၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇) </font></a></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/246-Dawkhinhlatin-246-Dawkhinhlatin-53-05.mp4">
										<font size="4">၂၄၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၅)</font></a><font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/243-Dawkhinhlatin-243-Dawkhinhlatin-53-02.mp4">
										ဆိုရိုး</a></font></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/177-Dawkhinhlatin-Thamotesi-10.1.mp4">၁၇၇။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၀) 
										ဆိုရိုး</a></font></td>
										<td width="301">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/204-Dawkhinhlatin-204-Dawkhinhlatin-49-02-PyitSi-07-B-PaTateSa.mp4">
										<font size="4">၂၀၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇) </font></a></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/247-Dawkhinhlatin-247-Dawkhinhlatin-53-06.mp4">
										<font size="4">၂၄၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၆)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/178-Dawkhinhlatin-Thamotesi-10.mp4">၁၇၈။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၀)</a></font></td>
										<td width="301">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/205-Dawkhinhlatin-205-Dawkhinhlatin-49-03-PyitSi-08-PaHtan-1A.mp4">
										<font size="4">၂၀၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၁) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၈) ဆိုရိုး</font></a></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/248-Dawkhinhlatin-248-Dawkhinhlatin-53-07.mp4">
										<font size="4">၂၄၈</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၆)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/179-Dawkhinhlatin-Thamotesi-11.1.mp4">၁၇၉။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၁) 
										ဆိုရိုး</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/206-Dawkhinhlatin-206-Dawkhinhlatin-49-04-PyitSi-08-PaHtan-1B.mp4">
										<font size="4">၂၀၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၁) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၈) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/249-Dawkhinhlatin-249-Dawkhinhlatin-53-08.mp4">
										<font size="4">၂၄၉</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၆) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/180-Dawkhinhlatin-Thamotesi-11.mp4">၁၈၀။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၁)</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/207-Dawkhinhlatin-207-Dawkhinhlatin-49-05-PyitSi-08-PaHtan-1C.mp4">
										<font size="4">၂၀၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၁) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၈) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/250-Dawkhinhlatin-250-Dawkhinhlatin-53-09.mp4">
										<font size="4">၂၅၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၇)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/181-Dawkhinhlatin-Thamotesi-12.1.mp4">၁၈၁။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၂) 
										ဆိုရိုး</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/208-Dawkhinhlatin-208-Dawkhinhlatin-49-06-PyitSi-09-PaHtan-2A.mp4">
										<font size="4">၂၀၈</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၂) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၉) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/251-Dawkhinhlatin-251-Dawkhinhlatin-53-10.mp4">
										<font size="4">၂၅၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၇)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/182-Dawkhinhlatin-Thamotesi-12.mp4">၁၈၂။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၂</a>)</font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/209-Dawkhinhlatin-209-Dawkhinhlatin-49-07-PyitSi-09-PaHtan-2B.mp4">
										<font size="4">၂၀၉</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၂) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၉) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/252-Dawkhinhlatin-252-Dawkhinhlatin-53-11.mp4">
										<font size="4">၂၅၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၇) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/183-Dawkhinhlatin-Thamotesi-13-1.mp4">၁၈၃။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၃) 
										ဆိုရိုး</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/210-Dawkhinhlatin-210-Dawkhinhlatin-49-08-PyitSi-10-PaHtan-3A.mp4">
										<font size="4">၂၁၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၃) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၀) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/253-Dawkhinhlatin-253-Dawkhinhlatin-53-12.mp4">
										<font size="4">၂၅၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၈)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/184-Dawkhinhlatin-Thamotesi-13.mp4">၁၈၄။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၃)</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/211-Dawkhinhlatin-211-Dawkhinhlatin-49-09-PyitSi-10-PaHtan-3B.mp4">
										<font size="4">၂၁၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၃) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၀) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/254-Dawkhinhlatin-254-Dawkhinhlatin-53-13.mp4">
										<font size="4">၂၅၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၈)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/185-Dawkhinhlatin-Thamotesi-14A.mp4">၁၈၅။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၄) 
										ပ</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/212-Dawkhinhlatin-212-Dawkhinhlatin-50-01-PyitSi-11-PaHtan-4A.mp4">
										<font size="4">၂၁၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၄) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၁) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/255-Dawkhinhlatin-255-Dawkhinhlatin-54-01.mp4">
										<font size="4">၂၅၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										(ေခါင္းစဥ္)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								<font size="4" face="Zawgyi-One">
										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/186-Dawkhinhlatin-Thamotesi-14B.mp4">၁၈၆။ တတိယအဆင္႔ပို႔ခ်ခ်က္ 
								သမုပစၥည္းပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၄) 
										ဒု</a></font></td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/213-Dawkhinhlatin-213-Dawkhinhlatin-50-02-PyitSi-11-PaHtan-4B.mp4">
										<font size="4">၂၁၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၄) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၁) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/256-Dawkhinhlatin-256-Dawkhinhlatin-54-02.mp4">
										<font size="4">၂၅၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၈) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/214-Dawkhinhlatin-214-Dawkhinhlatin-50-03-PyitSi-12-PaHtan-5A.mp4">
										<font size="4">၂၁၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၅) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၂) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/257-Dawkhinhlatin-257-Dawkhinhlatin-54-03.mp4">
										<font size="4">၂၅၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၉)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/215-Dawkhinhlatin-215-Dawkhinhlatin-50-04-PyitSi-12-PaHtan-5B.mp4">
										<font size="4">၂၁၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၅) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၂) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/258-Dawkhinhlatin-258-Dawkhinhlatin-54-04.mp4">
										<font size="4">၂၅၈</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၉)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/216-Dawkhinhlatin-216-Dawkhinhlatin-50-05-PyitSi-13-PaHtan--6A.mp4">
										<font size="4">၂၁၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၆) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၃) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/259-Dawkhinhlatin-259-Dawkhinhlatin-54-05.mp4">
										<font size="4">၂၅၉</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၉) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/217-Dawkhinhlatin-217-Dawkhinhlatin-50-06-PyitSi-13-PaHtan--6B.mp4">
										<font size="4">၂၁၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၆) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၃) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/260-Dawkhinhlatin-260-Dawkhinhlatin-54-06.mp4">
										<font size="4">၂၆၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၀) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/218-Dawkhinhlatin-218-Dawkhinhlatin-50-07-PyitSi-14-PaHtan--7A.mp4">
										<font size="4">၂၁၈</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၇) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၄) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/261-Dawkhinhlatin-261-Dawkhinhlatin-54-07.mp4">
										<font size="4">၂၆၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၀) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/219-Dawkhinhlatin-219-Dawkhinhlatin-50-08-PyitSi-14-PaHtan--7B.mp4">
										<font size="4">၂၁၉</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ 
										ပစၥည္းပိုင္း-ပ႒ာန္းပိုင္း(၇) ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၄) </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/262-Dawkhinhlatin-262-Dawkhinhlatin-54-08.mp4">
										<font size="4">၂၆၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၀) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/220-Dawkhinhlatin-220-Dawkhinhlatin-51-01.mp4">
										<font size="4">၂၂၀</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၁) 
										ပို႔ခ်ခ်က္</font></a></font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/263-Dawkhinhlatin-263-Dawkhinhlatin-54-09.mp4">
										<font size="4">၂၆၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၁) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/221-Dawkhinhlatin-221-Dawkhinhlatin-51-02.mp4">
										<font size="4">၂၂၁</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၂) 
										ပို႔ခ်ခ်က</font></a><font size="4" face="Zawgyi-One">္
										</font>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/264-Dawkhinhlatin-264-Dawkhinhlatin-54-10.mp4">
										<font size="4">၂၆၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၁) </font></a>
</font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/222-Dawkhinhlatin-222-Dawkhinhlatin-51-03.mp4">
										<font size="4">၂၂၂</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၃) 
										ပို႔ခ်ခ်က</font></a><font size="4" face="Zawgyi-One">္
										</font>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/265-Dawkhinhlatin-265-Dawkhinhlatin-54-11.mp4">
										<font size="4">၂၆၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၁) ဆိုရိုး</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/223-Dawkhinhlatin-223-Dawkhinhlatin-51-04.mp4">
										<font size="4">၂၂၃</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၄) 
										ပို႔ခ်ခ်က္ </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/266-Dawkhinhlatin-266-Dawkhinhlatin-54-12.mp4">
										<font size="4">၂၆၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၂)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/224-Dawkhinhlatin-224-Dawkhinhlatin-51-05.mp4">
										<font size="4">၂၂၄</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၅) 
										ပို႔ခ်ခ်က္ </font></a>
</font></td>
										<td>

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/267-Dawkhinhlatin-267-Dawkhinhlatin-54-13.mp4">
										<font size="4">၂၆၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ကမၼ႒ာန္း ပို႔ခ်ခ်က္ 
										အမွတ္စဥ္ (၁၂)</font></a></font></td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/225-Dawkhinhlatin-225-Dawkhinhlatin-51-06.mp4">
										<font size="4">၂၂၅</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၆) 
										ပို႔ခ်ခ်က</font></a><font size="4" face="Zawgyi-One">္
										</font>
</font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/226-Dawkhinhlatin-226-Dawkhinhlatin-51-07.mp4">
										<font size="4">၂၂၆</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၇) 
										ပို႔ခ်ခ်က္ </font></a>
</font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/227-Dawkhinhlatin-227-Dawkhinhlatin-51-08.mp4">
										<font size="4">၂၂၇</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၈) 
										ပို႔ခ်ခ်က</font></a><font size="4" face="Zawgyi-One">္
										</font>
</font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/228-Dawkhinhlatin-228-Dawkhinhlatin-51-09.mp4">
										<font size="4">၂၂၈</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၉) 
										ပို႔ခ်ခ်က္</font></a><font size="4" face="Zawgyi-One">
										</font>
</font></td>
										<td>&nbsp;</td>
									</tr>
									<tr>
										<td width="285">
								&nbsp;</td>
										<td width="301">

<font face="Zawgyi-One">






										<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/229-Dawkhinhlatin-229-Dawkhinhlatin-51-10.mp4">
										<font size="4">၂၂၉</font><font size="4" face="Zawgyi-One">။ 
										တတိယဆင္႔ပို႔ခ်ခ်က္ ပစၥည္းပိုင္း-ပညတ္(၁၀) 
										ပို႔ခ်ခ်က္ </font></a>
</font></td>
										<td>&nbsp;</td>
									</tr>
								</tbody>
"""

soup = bs4(text, 'html.parser')

p = re.compile(r'(?P<word>[^0-9]+)')

#print(p)
count = 160
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
        
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp4|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find('a').get('href'), 
        " ".join(key.find('td').find_next_sibling('td').find('a').get_text().strip().split()) 
            ))
        count += 1
    except AttributeError as err:
        pass
        
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
