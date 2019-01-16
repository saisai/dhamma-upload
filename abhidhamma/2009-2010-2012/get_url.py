from bs4 import BeautifulSoup as bs4
import re
one = """

									<tbody><tr>
										<td colspan="3" bgcolor="#0000CC" align="center">
								<font size="4" color="#FFFFFF">ပထမအဆင္႕</font></td>
									</tr>
									<tr>
										<td width="32%" bgcolor="#0000CC" align="center">
								<font size="4" color="#FFFFFF">စိတ္ပိုင္း (၂၀၀၉)</font></td>
										<td width="34%" bgcolor="#0000CC" align="center">
								<font size="4" color="#FFFFFF">ေစတသိက္ပိုင္း 
								(၂၀၀၉)</font></td>
										<td width="31%" bgcolor="#0000CC" align="center">
								<font size="4" color="#FFFFFF">ပကိဏ္းပိုင္း 
								(၂၀၀၉)</font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/001-DawKhinHlaTin-Abhidhamma-Sait-Lect-1.mp4">၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁) 
								</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/035-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect1(25)-4-8-2009.mp4">၃၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၅) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၁) ဆိုရိုး ၄-၈-၂၀၀၉</a></font></td>
										<td width="31%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/058-DawKhinHlaTin-Abhidhamma-PaKane-Lect1(48)-6-2-2010.mp4">၅၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၈) 
								ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁) ဆိုရိုး ၆-၂-၂၀၁၀
								</a>
								</font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/002-DawKhinHlaTin-Abhidhamma-Sait-Lect-2.mp4">၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂) 
								</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/036-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect1(26)-5-8-2009.mp4">၃၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၆) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၂) ဆိုရိုး ၅-၈-၂၀၀၉</a></font></td>
										<td width="31%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/059-DawKhinHlaTin-Abhidhamma-PaKane-Lect2(49)-6-2-2010.mp4">၅၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၉) 
								ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၂) ဆိုရိုး ၆-၂-၂၀၁၀
								</a>
								</font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/003-DawKhinHlaTin-Abhidhamma-Sait-Lect-3.mp4">၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃) အဓိပၸါယ္</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/037-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect3(27)-11-8-2009.mp4">၃၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၇) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၃) ဆိုရိုး ၁၁-၈-၂၀၀၉</a></font></td>
										<td width="31%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/060-DawKhinHlaTin-Abhidhamma-PaKane-Lect3(50)-7-2-2010.mp4">၆၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၀) 
								ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၃) ဆိုရိုး ၇-၂-၂၀၁၀
								</a>
								</font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/004-DawKhinHlaTin-Abhidhamma-Sait-Lect-4.mp4">၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄) ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/038-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect4(28)-12-8-2009.mp4">၃၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၈) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၄) အဓိပၸါယ္ ၁၂-၈-၂၀၀၉</a></font></td>
										<td width="31%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/061-DawKhinHlaTin-Abhidhamma-PaKane-Lect4(51)-7-2-2010.mp4">၆၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၁) 
								ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၄) ဆိုရိုး ၇-၂-၂၀၁၀
								</a>
								</font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/005-DawKhinHlaTin-Abhidhamma-Sait-5-1.mp4">၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅-၁) သရုပ္ခြဲ</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/039-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect5(29)-15-9-2009.mp4">၃၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၉) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၅) အဓိပၸါယ္ ၁၅-၉-၂၀၀၉</a></font></td>
										<td width="31%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/062-DawKhinHlaTin-Abhidhamma-PaKane-Lect5(52)-12-2-2010.mp4">၆၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၂) 
								ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၅) ဆိုရိုး ၁၂-၂-၂၀၁၀
								</a>
								</font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/006-DawKhinHlaTin-Abhidhamma-Sait-5-2.mp4">၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅-၂)&nbsp; အဓိပၸါယ္</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/040-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect6(30)-16-9-2009.mp4">၄၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၀) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၆) ဆိုရိုး ၁၆-၉-၂၀၀၉</a></font></td>
										<td width="31%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/063-DawKhinHlaTin-Abhidhamma-PaKane-Lect6(53)-12-2-2010.mp4">
<font size="4" face="Zawgyi-One">
										၆၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၃) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၆) အဓိပၸါယ္ 
၁၂-၂-၂၀၁၀</font></a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/007-DawKhinHlaTin-Abhidhamma-Sait-Lect-6-1.mp4">၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆-၁) ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/041-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect7(31)-22-9-2009.mp4">၄၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၁) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၇) အဓိပၸါယ္ ၂၂-၉-၂၀၀၉</a></font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/064-DawKhinHlaTin-Abhidhamma-PaKane-Lect6(53)-12-2-2010.mp4">၆၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၃) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၆) ဆိုရိုး 
၁၂-၂-၂၀၁၀ </a> </font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/008-DawKhinHlaTin-Abhidhamma-Sait-Lect-6-2.mp4">၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆-၂) သရုပ္ခြဲ</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/042-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect8(32)-23-9-2009.mp4">
										၄၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၂) 
										ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၈) ဆိုရိုး 
										၂၃-၉-၂၀၀၉</a></font></td>
										<td width="31%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/065-DawKhinHlaTin-Abhidhamma-PaKane-Lect7(54)-13-2-2010.mp4">
<font size="4" face="Zawgyi-One">
										၆၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၄) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၇) အဓိပၸါယ္ 
၁၃-၂-၂၀၁၀</font></a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/009-DawKhinHlaTin-Abhidhamma-Sait-Lect-6-3.mp4">၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆-၃) အဓိပၸါယ္</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/043-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect9(33)-29-9-2009.mp4">၄၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၃) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၉) ဆိုရိုး ၂၉-၉-၂၀၀၉</a></font></td>
										<td width="31%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/066-DawKhinHlaTin-Abhidhamma-PaKane-Lect8(55)-13-2-2010.mp4">
<font size="4" face="Zawgyi-One">
										၆၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၅) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၈) အဓိပၸါယ္ 
၁၃-၂-၂၀၁၀</font></a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/010-DawKhinHlaTin-Abhidhamma-Sait-Lect-7-1.mp4">၁၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၇-၁) ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/044-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect10(34)-30-9-2009.mp4">၄၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၄) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၁၀) အဓိပၸါယ္&nbsp; ၃၀-၉-၂၀၀၉</a></font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/067-DawKhinHlaTin-Abhidhamma-PaKane-Lect9(56)-14-2-2010.mp4">၆၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၆) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၉) ဆိုရိုး 
၁၄-၂-၂၀၁၀ </a> </font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/011-DawKhinHlaTin-Abhidhamma-Sait-Lect-7-2.mp4">၁၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၇-၂) သရုပ္ခြဲ</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/045-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect11(35)-6-10-2009.mp4">၄၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၅) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၁၁) အဓိပၸါယ္ ၆-၁၀-၂၀၀၉</a></font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/068-DawKhinHlaTin-Abhidhamma-PaKane-Lect10(57)-14-2-2010.mp4">

<font face="Zawgyi-One">






										၆၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၇) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၀) 
အဓိပၸါယ္ ၁၄-၂-၂၀၁၀</font></a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/012-DawKhinHlaTin-Abhidhamma-Sait-Lect-7-3.mp4">၁၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၇-၃) အဓိပၸါယ္</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/046-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect12(36)-7-10-2009.mp4">၄၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၆) ေစတသိက္ပိုင္း 
								ပို႕ခ်ခ်က္ (၁၂) ဆိုရိုး ၇-၁၀-၂၀၀၉</a></font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/069-DawKhinHlaTin-Abhidhamma-PaKane-Lect11(58)-20-2-2010.mp4">

<font face="Zawgyi-One">






										၆၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၈) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၁) 
အဓိပၸါယ္ ၂၀-၂-၂၀၁၀</font></a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/013-DawKhinHlaTin-Abhidhamma-Sait-Lect-8-1.mp4">၁၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၈-၁) ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/047-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect13(37)-13-10-2009.mp4">၄၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၇) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၃) ဆိုရိုး&nbsp; 
								၁၃-၁၀-၂၀၀၉
								</a> </font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/070-DawKhinHlaTin-Abhidhamma-PaKane-Lect12(59)-20-2-2010.mp4">

<font face="Zawgyi-One">






										၇၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅၉) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၂) 
အဓိပၸါယ္ ၂၀-၂-၂၀၁၀</font></a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/014-DawKhinHlaTin-Abhidhamma-Sait-Lect-8-2.mp4">၁၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၈-၂) သရုပ္ခြဲ</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/048-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect14(38)-14-10-2009.mp4">၄၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၈) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၄) ဆိုရိုး&nbsp; 
								၁၄-၁၀-၂၀၀၉ 
								</a> </font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/071-DawKhinHlaTin-Abhidhamma-PaKane-Lect13(60)-21-2-2010.mp4">၇၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၀) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၃) ဆိုရိုး 
၂၁-၂-၂၀၁၀ </a> </font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/015-DawKhinHlaTin-Abhidhamma-Sait-Lect-8-3.mp4">၁၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၈-၃) အဓိပၸါယ္</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/049-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect15(39)-20-10-2009.mp4">၄၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၉) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၅) အဓိပၸါယ္ 
								၂၀-၁၀-၂၀၀၉ 
								</a> </font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/072-DawKhinHlaTin-Abhidhamma-PaKane-Lect14(61)-21-2-2010.mp4">၇၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၁) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၄) 
အရမၼဏသဂၤဟ ၂၁-၂-၂၀၁၀</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/016-DawKhinHlaTin-Abhidhamma-Sait-Lect-9-1.mp4">၁၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၉-၁)&nbsp; ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/050-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect16(40)-21-10-2009.mp4">၅၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၀) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၆) အဓိပၸါယ္ 
								၂၁-၁၀-၂၀၀၉ 
								</a> </font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/073-DawKhinHlaTin-Abhidhamma-PaKane-Lect15(62)-28-2-2010.mp4">၇၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၂) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၅) ဆိုရိုး 
၂၈-၂-၂၀၁၀</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/017-DawKhinHlaTin-Abhidhamma-Sait-Lect-9-2.mp4">၁၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၉-၂) သရုပ္ခြဲ</a></font></td>
										<td width="34%">
										<font size="4" face="Zawgyi-One">
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/051-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect17(41)-27-10-2009.mp4">၅၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၁) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၇) သရုပ္ခြဲ 
								၂၇-၁၀-၂၀၀၉ 
								</a> </font></td>
										<td width="31%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/074-DawKhinHlaTin-Abhidhamma-PaKane-Lect16(63)-28-2-2010.mp4">၇၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၃) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၆) 
အဓိပၸါယ္ ၂၈-၂-၂၀၁၀</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/018-DawKhinHlaTin-Abhidhamma-Sait-Lect-10-1.mp4">၁၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၀-၁) ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/052-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect18(42)-28-10-2009.mp4">၅၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၂) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၈) သရုပ္ခြဲ 
								၂၈-၁၀-၂၀၀၉ 
								</a> </font></td>
										<td width="31%"><font size="4" face="Zawgyi-One"><a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/075-DawKhinHlaTin-Abhidhamma-PaKane-Lect17(64)-6-3-2010.mp4">၇၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၄) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၇) 
အဓိပၸါယ္ ၆-၃-၂၀၁၀</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/019-DawKhinHlaTin-Abhidhamma-Sait-Lect-10-2.mp4">၁၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၀-၂) သရုပ္ခြဲ</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/053-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect19(43)-3-11-2009.mp4">၅၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၃) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၁၉) သရုပ္ခြဲ ၃-၁၁-၂၀၀၉
								</a>
								</font></td>
										<td width="31%"><font size="4" face="Zawgyi-One">
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/063-DawKhinHlaTin-Abhidhamma-PaKane-Lect6(53)-12-2-2010.mp4">&nbsp;</a><a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/076-DawKhinHlaTin-Abhidhamma-PaKane-Lect18(65)-6-3-2010.mp4">၇၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၅) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၈) 
အဓိပၸါယ္ ၆-၃-၂၀၁၀</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/020-DawKhinHlaTin-Abhidhamma-Sait-Lect-11-1.mp4">၂၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၁-၁) ဆိုရိုး</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/054-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect20(44)-4-11-2009.mp4">၅၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၄) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၂၀) သရုပ္ခြဲ ၄-၁၁-၂၀၀၉
								</a>
								</font></td>
										<td width="31%"><font size="4" face="Zawgyi-One">
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/065-DawKhinHlaTin-Abhidhamma-PaKane-Lect7(54)-13-2-2010.mp4">&nbsp;</a><a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/077-DawKhinHlaTin-Abhidhamma-PaKane-Lect19(66)-7-3-2010.mp4">၇၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆၆) ပကိဏ္းပိုင္း ပို႕ခ်ခ်က္ (၁၉) 
ဝတၳဳသဂၤဟ ၇-၃-၂၀၁၀</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/021-DawKhinHlaTin-Abhidhamma-Sait-Lect-11-2.mp4">၂၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၁-၂) အဓိပၸါယ္</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/055-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect21(45)-10-11-2009.mp4">၅၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၅) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၂၁) အဓိပၸါယ္ 
								၁၀-၁၁-၂၀၀၉ 
								</a> </font></td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/022-DawKhinHlaTin-Abhidhamma-Sait-Lect-12-1.mp4">၂၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၂) အဓိပၸါယ္ ၁၇-၆-၂၀၀၉</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/056-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect22(46)-17-11-2009.mp4">၅၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၆) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၂၂) ဆိုရိုး ၁၇-၁၁-၂၀၀၉
								</a>
								</font></td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/023-DawKhinHlaTin-Abhidhamma-Sait-Lect-13.mp4">၂၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၃) အဓိပၸါယ္ ၂၃-၆-၂၀၀၉</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/057-DawKhinHlaTin-Abhidhamma-SayTaThaik-Lect23(47)-18-11-2009.mp4">၅၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄၇) 
								ေစတသိက္ပိုင္း ပို႕ခ်ခ်က္ (၂၃) ဆိုရိုး ၁၈-၁၁-၂၀၀၉
								</a>
								</font></td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/024-DawKhinHlaTin-Abhidhamma-Sait-Lect-14-24-6-2009.mp4">၂၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၄) အဓိပၸါယ္ ၂၄-၆-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/025-DawKhinHlaTin-Abhidhamma-Sait-Lect-15-30-6-2009.mp4">၂၅။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၅) သရုပ္ခြဲ ၃၀-၆-၂၀၀၉</a></font></td>
										<td width="34%">

<font face="Zawgyi-One">






								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
</font>

										</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/026-DawKhinHlaTin-Abhidhamma-Sait-Lect-16-1-7-2009.mp4">၂၆။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၆) သရုပ္ခြဲ ၁-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/027-DawKhinHlaTin-Abhidhamma-Sait-Lect17-7-7-2009.mp4">၂၇။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၇) အဓိပၸါယ္ ၇-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/028-DawKhinHlaTin-Abhidhamma-Sait-Lect18-8-7-2009.mp4">၂၈။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၈) အဓိပၸါယ္ ၈-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;<p>&nbsp;</p></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/029-DawKhinHlaTin-Abhidhamma-Sait-Lect19-14-7-2009.mp4">၂၉။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၉) အဓိပၸါယ္ ၁၄-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/030-DawKhinHlaTin-Abhidhamma-Sait-Lect20-15-7-2009.mp4">၃၀။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၀) အဓိပၸါယ္ ၁၅-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%"><font size="4" face="Zawgyi-One">
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/066-DawKhinHlaTin-Abhidhamma-PaKane-Lect8(55)-13-2-2010.mp4">&nbsp;</a></font></td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/031-DawKhinHlaTin-Abhidhamma-Sait-Lect21-21-7-2009.mp4">၃၁။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၁) အဓိပၸါယ္ ၂၁-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/032-DawKhinHlaTin-Abhidhamma-Sait-Lect22-22-7-2009.mp4">၃၂။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၂) သရုပ္ခြဲ ၂၂-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/033-DawKhinHlaTin-Abhidhamma-Sait-Lect23-28-7-2009.mp4">၃၃။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၃) အဓိပၸါယ္ ၂၈-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/034-DawKhinHlaTin-Abhidhamma-Sait-Lect24-29-7-2009.mp4">၃၄။ ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၄) အဓိပၸါယ္ ၂၉-၇-၂၀၀၉</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="31%">&nbsp;</td>
									</tr>
									</tbody>
"""
two = """									<tbody><tr>
										<td colspan="3">
										<p align="center">
										<font size="4" face="Zawgyi-One" color="#FFFFFF">
										<span style="background-color: #CC3399">
										ဒုတိယအဆင္႔ (၂၀၁၀)</span></font></p></td>
									</tr>
									<tr>
										<td width="32%" bgcolor="#CC3399" align="center">
										<p align="center">
										<font size="4" color="#FFFFFF">
										ဝီထိပိုင္း (၂၀၁၀)</font></p></td>
										<td width="34%" bgcolor="#CC3399" align="center">
										<p align="center">
										<font size="4" color="#FFFFFF">
										ဝီထိမုတ္ပိုင္း (၂၀၁၀)</font></p></td>
										<td width="32%" bgcolor="#CC3399" align="center">
										<font size="4" color="#FFFFFF">
										ရုပ္ပိုင္း (၂၀၁၀)</font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/079-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(1)-13-3-2010.mp4">၇၉။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁) 
ဆိုရိုး ၁၃-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/114-Dawkhinhlatin-Vihtimutta01-1.mp4">
								၁၁၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/145-Dawkhinhlatin-Rupa-01-1.mp4">၁၄၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/080-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(2)-13-3-2010.mp4">၈၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂) 
အဓိပၸါယ္ ၁၃-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/115-Dawkhinhlatin-Vihtimutta02-1.mp4">
								၁၁၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/146-Dawkhinhlatin-Rupa-02-1.mp4">၁၄၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/081-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(3)-14-3-2010.mp4">၈၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃) 
အဓိပၸါယ္ ၁၄-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/116-Dawkhinhlatin-Vihtimutta03-1.mp4">
								၁၁၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/147-Dawkhinhlatin-Rupa-03-1.mp4">၁၄၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/082-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(4)-14-3-2010.mp4">၈၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၄) 
အဓိပၸါယ္ ၁၄-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/117-Dawkhinhlatin-Vihtimutta04-1.mp4">
								၁၁၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/148-Dawkhinhlatin-Rupa-04-1.mp4">၁၄၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၄)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/083-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(5)-20-3-2010.mp4">၈၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၅) 
အဓိပၸါယ္ ၂၀-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/118-Dawkhinhlatin-Vihtimutta05-1.mp4">
								၁၁၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/149-Dawkhinhlatin-Rupa-05-1.mp4">၁၄၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၅)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/084-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(6)-20-3-2010.mp4">၈၄။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၆) 
ဆိုရိုး ၂၀-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/119-Dawkhinhlatin-Vihtimutta06-1.mp4">
								၁၁၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/150-Dawkhinhlatin-Rupa-06-1.mp4">၁၅၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၆)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/085-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(7)-21-3-2010.mp4">၈၅။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၇) 
ဆိုရိုး ၂၁-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/120-Dawkhinhlatin-Vihtimutta07-1.mp4">
								၁၂၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/151-Dawkhinhlatin-Rupa-07-1.mp4">၁၅၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၇)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/086-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(8)-21-3-2010.mp4">၈၆။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၈) 
ဆိုရိုး ၂၁-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/121-Dawkhinhlatin-Vihtimutta08-1.mp4">၁၂၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၈)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/152-Dawkhinhlatin-Rupa-08-1.mp4">၁၅၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၈)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/087-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(9)-27-3-2010.mp4">၈၇။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၉) 
အဓိပၸါယ္ ၂၇-၃-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/122-Dawkhinhlatin-Vihtimutta09-1.mp4">
								၁၂၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၉)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/153-Dawkhinhlatin-Rupa-09-1.mp4">၁၅၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၉)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/088-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(10)-10-5-2010.mp4">၈၈။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၀) 
ဆိုရိုး ၁၁-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/123-Dawkhinhlatin-Vihtimutta10-1.mp4">
								၁၂၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၀)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/154-Dawkhinhlatin-Rupa-10-1.mp4">၁၅၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၀)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/089-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(11)-12-5-2010.mp4">၈၉။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၁) 
အဓိပၸါယ္ ၁၂-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">၁၂၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ 
								ဝီထိမုတ္ပိုင္း ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၁)</font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/155-Dawkhinhlatin-Rupa-11-1.mp4">၁၅၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၁)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/090-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(12)-18-5-2010.mp4">၉၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၂) 
အဓိပၸါယ္ ၁၈-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/125-Dawkhinhlatin-Vihtimutta12-1.mp4">
								၁၂၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၂)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/156-Dawkhinhlatin-Rupa-12-1.mp4">၁၅၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၂)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/091-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(13)-19-5-2010.mp4">၉၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၃) 
ဆိုရိုး ၁၉-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/126-Dawkhinhlatin-Vihtimutta13-1.mp4">
								၁၂၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၃)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/157-Dawkhinhlatin-Rupa-13-1.mp4">၁၅၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၃)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/092-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(13)-25-5-2010.mp4">၉၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၄) 
အဓိပၸါယ္ ၂၅-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/127-Dawkhinhlatin-Vihtimutta14-1.mp4">
								၁၂၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၄)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/158-Dawkhinhlatin-Rupa-14-1.mp4">၁၅၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၄)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/093-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(15)-26-5-2010.mp4">၉၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၅) 
ဆိုရိုး ၂၆-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/128-Dawkhinhlatin-Vihtimutta15-1.mp4">
								၁၂၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၅)</a></font></td>
										<td width="32%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/159-Dawkhinhlatin-Rupa-15-1.mp4">၁၅၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ရုပ္္ပိုင္း 
										ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၅)</a></font></td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/094-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(16)-1-6-2010.mp4">၉၄။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၆) 
ဆိုရိုး ၂၆-၅-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/129-Dawkhinhlatin-Vihtimutta16-1.mp4">
								၁၂၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၆)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/095-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(17)-2-6-2010.mp4">၉၅<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၇) 
ဆိုရိုး ၆-၆-၂၀၁၀</font></a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/130-Dawkhinhlatin-Vihtimutta17-1.mp4">
								၁၃၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၇)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DawKhinHlaTin/abhidhamma-special-2009-2010/096-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(18)-8-6-2010.wmv">
၉၆။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၈) ဆိုရိုး ၈-၆-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/131-Dawkhinhlatin-Vihtimutta18-1.mp4">
								၁၃၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၈)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/097-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(19)-9-6-2010.mp4">၉၇။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၁၉) အဓိပၸါယ္ ၉-၆-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/132-Dawkhinhlatin-Vihtimutta19-1.mp4">
								၁၃၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၁၉)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/098-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(20)-15-6-2010.mp4">၉၈<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၀) 
ဆိုရိုး ၁၅-၆-၂၀၁၀</font></a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/133-Dawkhinhlatin-Vihtimutta20-1.mp4">
								၁၃၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၀)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/099-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(21)-16-6-2010.mp4">၉၉<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၁) 
အဓိပၸါယ္ ၁၆-၆-၂၀၁၀</font></a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/134-Dawkhinhlatin-Vihtimutta21-1.mp4">
								၁၃၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၁)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/100-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(22)-22-6-2010.mp4">၁၀၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၂) ဆိုရိုး ၂၂-၆-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/135-Dawkhinhlatin-Vihtimutta22-1.mp4">
								၁၃၅။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၂)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/101-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(23)-23-6-2010.mp4">၁၀၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၃) အဓိပၸါယ္ ၂၃-၆-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/136-Dawkhinhlatin-Vihtimutta23-1.mp4">
								၁၃၆။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၃)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/102-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(24)-29-6-2010.mp4">၁၀၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၄) ဆိုရိုး ၂၉-၆-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/137-Dawkhinhlatin-Vihtimutta24-1.mp4">
								၁၃၇။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၄)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/103-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(25)-30-6-2010.mp4">၁၀၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၅) အဓိပၸါယ္ ၃၀-၆-၂၀၁၀</a></font></td>
										<td width="34%">

<font face="Zawgyi-One">






								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/138-Dawkhinhlatin-Vihtimutta25-1.mp4">
								၁၃၈။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၅)</a></font></p>
</font>

										</td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/104-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(26)-6-7-2010.mp4">၁၀၄။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၆) ဆိုရိုး ၆-၇-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/139-Dawkhinhlatin-Vihtimutta26-1.mp4">
								၁၃၉။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၆)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/105-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(27)-7-7-2010.mp4">၁၀၅<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၇) 
ဆိုရိုး ၇-၇-၂၀၁၀</font></a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/140-Dawkhinhlatin-Vihtimutta27-1.mp4">
								၁၄၀။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၇)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">

<font face="Zawgyi-One">






<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/106-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(28)-13-7-2010.mp4">၁၀၆<font size="4">။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၈) 
အဓိပၸါယ္ ၁၃-၇-၂၀၁၀</font></a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/141-Dawkhinhlatin-Vihtimutta28-1.mp4">
								၁၄၁။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၈)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/107-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(29)-14-7-2010.mp4">၁၀၇။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၂၉) အဓိပၸါယ္ ၁၄-၇-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/142-Dawkhinhlatin-Vihtimutta29-1.mp4">
								၁၄၂။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၂၉)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/108-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(30)-20-7-2010.mp4">၁၀၈။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၀) အဓိပၸါယ္ ၂၀-၇-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/143-Dawkhinhlatin-Vihtimutta30-1.mp4">
								၁၄၃။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃၀)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/109-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(31)-21-7-2010.mp4">၁၀၉။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၁) အဓိပၸါယ္ ၂၁-၇-၂၀၁၀</a></font></td>
										<td width="34%">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/144-Dawkhinhlatin-Vihtimutta31-1.mp4">
								၁၄၄။ ဒုတိယအဆင္႔ပို႔ခ်ခ်က္ ဝီထိမုတ္ပိုင္း 
								ပို႔ခ်ခ်က္ အမွတ္စဥ္ (၃၁)</a></font></td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/110-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(32)-27-7-2010.mp4">၁၁၀။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၂) အဓိပၸါယ္ ၂၇-၇-၂၀၁၀</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/111-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(33)-28-7-2010.mp4">၁၁၁။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၃) အဓိပၸါယ္ ၂၈-၇-၂၀၁၀</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/112-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(34)-3-8-2010.mp4">၁၁၂။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၄) အဓိပၸါယ္၃-၈-၂၀၁၀</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="32%">&nbsp;</td>
									</tr>
									<tr>
										<td width="32%">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/abhidhamma-special-2009-2010/113-DawKhinHlaTin-Abhidhamma-WeHteet-Lect(35)-4-8-2010.mp4">၁၁၃။ ဒုတိယအဆင့္ပို႕ခ်ခ်က္ ဝီထိပိုင္း ပို႕ခ်ခ်က္ အမွတ္စဥ္ (၃၅) အဓိပၸါယ္ ၄-၈-၂၀၁၀</a></font></td>
										<td width="34%">&nbsp;</td>
										<td width="32%">&nbsp;</td>
									</tr>
									</tbody>
"""                                    
three = """
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

#soup = bs4(one, 'html.parser')
#soup = bs4(two, 'html.parser')
soup = bs4(three, 'html.parser')


with open('titles_links.txt', 'w') as f:

    count = 156
    for key in soup.find_all('tr'):
        try:
            counter = '{:03d}'.format(count)
            #print(" ".join(key.find('td').find('a').get_text().strip().split()))
            print('{}.mp4|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), 
                " ".join(key.find('td').find('a').get_text().strip().split())            
                ))
            f.write('{}.mp4|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), 
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
            f.write('{}.mp4|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find('a').get('href'), 
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
            f.write('{}.mp4|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get('href'), 
            " ".join(key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get_text().strip().split()) ))            
            count += 1
        except AttributeError as err:
            pass
