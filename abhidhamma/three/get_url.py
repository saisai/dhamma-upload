from bs4 import BeautifulSoup as bs4
import re
text = """<table border="1" width="100%">
									<tbody><tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/001-DawKhinHlaTin-Samucca.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁။ သမုစၥည္းပိုင္း ဟူသည္</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/002-DawKhinHlaTin-.mp3">
										၂။ သမုသဟသဂၤဟ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/003-DawKhinHlaTin-.mp3">
										၃။ သမုသဟသဂၤဟ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/004-DawKhinHlaTin-.mp3">
										၄။ (၁) -အာသေဝါတရား ၄-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/005-DawKhinHlaTin-.mp3">
										၅။ (၂) -ၾသဃတရား ၄-ပါး</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/006-DawKhinHlaTin-.mp3">
										၆။ (၃) -ေယာဂတရား ၄-ပါး</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/007-DawKhinHlaTin-.mp3">
										၇။ (၄) -ဂႏ ၱတရား ၄-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/008-DawKhinHlaTin-.mp3">
										၈။ (၅) -ဥပါဒါန္တရား ၄-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/009-DawKhinHlaTin-.mp3">
										၉။ (၆) -နိဝရဏတရား ၆-ပါး</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/010-DawKhinHlaTin-.mp3">
										၁၀။ (၇) -အႏုသယတရား ၇-ပါး</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/011-DawKhinHlaTin-.mp3">
										၁၁။ (၇) -အႏုသယတရား ၇-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/012-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၂။ (၈) -သံေယာဇဥ္ ၁၀-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/013-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၃။ (၈) -သံေယာဇဥ္ ၁၀-ပါး</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/014-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၄။ (၉) -ကိေလသာတရား ၁၀-ပါး</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/015-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၅။ (၉) -ကိေလသာတရား ၁၀-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/016-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၆။ (၉) -ကိေလသာတရား ၁၀-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/017-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၇။ အကုသလ သဂၤဟျပန္ၿခဳံေျပာျခင္း</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/018-DawKhinHlaTin-.mp3">
										၁၈။ မိႆကသဂၤဟ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/019-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၉။ (၁) ဟိတ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/020-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၀။ (၂) စ်ာနင္</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/021-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၁။ (၃) မဂၢင္</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/022-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၂။ (၄) ဣေႃႏၵ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/023-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၃။ (၄) ဣေႃႏၵ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/024-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၄။ (၄) ဣေႃႏၵ</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/025-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၅။ (၄) ဣေႃႏၵ</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/026-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၆။ (၄) ဣေႃႏၵ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/027-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၇။ (၄) ဣေႃႏၵ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/028-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၈။ (၅) ဗိုလ္</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/029-DawKhinHlaTin-.mp3">
										၂၉။ (၆) အဓိပတိ</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/030-DawKhinHlaTin-.mp3">
										၃၀။ (၇) အဟာရ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/031-DawKhinHlaTin-.mp3">
										၃၁။ (၇) အဟာရ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/032-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၂။ မိႆကသဂၤဟျပန္ၿခဳံေျပာျခင္း</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/033-DawKhinHlaTin-.mp3">
										၃၃။ ေဗာဓိကၡယသဂၤဟ</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/034-DawKhinHlaTin-.mp3">
										၃၄။ ေဗာဓိကၡယသဂၤဟ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/035-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၅။ (၁) သတိပ႒ာန္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/036-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၆။ (၂) သမၸပၸ႒ာန္</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/037-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၇။ (၃) ဣဒၶိပၸါဒ္ (၄) ဣေႃႏၵ(၅) ဗိုလ္</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/038-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၈။ (၆) ေဗာဇၥ်င္</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/039-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၉။ (၇) မဂၢင္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/040-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၀။ သမုစၥည္းပိုင္း စာေမးပြဲဆိုင္ရာ</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/041-DawKhinHlaTin-.mp3">
										၄၁။ သဗၺသဂၤဟ</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/042-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၂။ (၁) ခႏၶာ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/043-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၃။ (၂) ဥပါဒါနကၡႏၶာ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/044-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၄။ (၂) ဥပါဒါနကၡႏၶာ</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/045-DawKhinHlaTin-.mp3">
										၄၅။ (၃) အာယတန</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/046-DawKhinHlaTin-.mp3">
										၄၆။ (၃) အာယတန</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/047-DawKhinHlaTin-.mp3">
										၄၇။ (၃) အာယတန</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/048-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၈။ (၄) ဓာတ္</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/049-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၉။ (၄) ဓာတ္</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/050-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၀။ (၄) ဓာတ္</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/051-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၁။ (၄) ဓာတ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/052-DawKhinHlaTin-.mp3">
										၅၂။ (၅) သစၥာ</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/053-DawKhinHlaTin-.mp3">
										၅၃။ (၅) သစၥာ</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/054-DawKhinHlaTin-.mp3">
										၅၄။ (၅) သစၥာ</a></font></td>
										<td width="184">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/055-DawKhinHlaTin-.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၅။ (၅) သစၥာ - သစၥာဝိမုတ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/056-DawKhinHlaTin-Samucca.mp3">
										၅၆။ (၅) သစၥာ - တဏွာ ၁၀၈</a></font></td>
									</tr>
									<tr>
										<td width="195">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/ThamuPyitSee/057-DawKhinHlaTin-Samucca.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၇။ - ျပန္ၿခဳံေျပာျခင္း</a></font></td>
										<td width="210">&nbsp;</td>
										<td width="184">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="194">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/001-DawKhinHlaTin-Paccaya.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁။ ပစၥည္းပိုင္း</a></font></td>
										<td width="210">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/002-DawKhinHlaTin-Paccaya.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂။ ပစၥည္းပိုင္း</a></font></td>
										<td width="185">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/003-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃။ ပဋိစၥသမုပၸါဒ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/004-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၄။ ပဋိစၥသမုပၸါဒ္ - အဝိဇၨာ</a></font></td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="199">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/005-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၅။ ပဋိစၥသမုပၸါဒ္ - အဝိဇၨာ</a></font></td>
										<td width="203">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/006-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၆။ ပဋိစၥသမုပၸါဒ္ - သခၤါရ</a></font></td>
										<td width="199">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/007-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၇။ ပဋိစၥသမုပၸါဒ္ - ဝိညာဏံ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/008-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၈။ ပဋိစၥသမုပၸါဒ္ - နာမရူပံ</a></font></td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="268">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/009-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၉။ ျပန္ၿခဳံေျပာျခင္း</a></font></td>
										<td width="296">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/010-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၀။ နာမရူပံ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/011-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၁။ သဠာယတန</a></font></td>
									</tr>
									<tr>
										<td width="268">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/012-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၂။ ဖႆ</a></font></td>
										<td width="296">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/013-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၃။ ေဝဒနာ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/014-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၄။ တဏွာ</a></font></td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="269">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/015-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၅။ ဥပါဒါန္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/016-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၆။ ဘဝ</a></font></td>
										<td width="265">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/017-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၁၇။ ဘဝ - ကမၼဘဝ၊ ဥပပတၱိဘဝ</a></font></td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="273">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/018-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၈။ စာေမးပြဲရူေထာင့္ျဖင့္ရွင္းျပ</a></font></td>
										<td width="293">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/019-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁၉။ စာေမးပြဲရူေထာင့္ျဖင့္ရွင္းျပ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/020-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၀။ ဇာတိ</a></font></td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="271">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/021-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၁။ ဇာတိပစၥယာ ဇရာ၊ မရဏ</a></font></td>
										<td width="293">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/022-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၂။ မွတ္စု စာမ်က္ႏွာ-၁၉</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/023-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၃။ ဘဝစက္အဂၤါစသည္</a></font></td>
									</tr>
									<tr>
										<td width="271">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/024-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၄။ ဘဝစက္အဂၤါစသည္ - ကာလ ၃-ပါး</a></font></td>
										<td width="293">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/025-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၅။ ဘဝစက္အဂၤါစသည္ - အလႊာ ၄-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/026-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၆။ ဘဝစက္အဂၤါစသည္ - အဂၤါ ၁၂-ပါး</a></font></td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="191">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/027-DawKhinHlaTin-PatticcaSamuppada.mp3">
										၂၇။ ဘဝစက္အဂၤါစသည္ - အဂၤါ ၁၂-ပါး</a></font></td>
										<td width="244">

<font face="Zawgyi-One">






								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/028-DawKhinHlaTin-PatticcaSamuppada.mp3">
၂၈။ ဘဝစက္အဂၤါစသည္ -&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; အဂၤါ ၁၂-ပါး</a></font></p>
</font>

										</td>
										<td width="191">
										<font size="4" face="Zawgyi-One">
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/029-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂၉။ စာေမးပြဲရူေထာင့္ျဖင ့္ရွင္းျပ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/030-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၀။ စာေမးပြဲရူေထာင့္ျဖင ့္ရွင္းျပ - အစပ္ 
										၃-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="191">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/031-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၁။ စာေမးပြဲရူေထာင့္ျဖင့္ ရွင္းျပ - ဝဋ္ 
										၃-ပါး</a></font></td>
										<td width="244">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/032-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၂။ စာေမးပြဲရူေထာင့္ျဖင္႔ </a>&nbsp;&nbsp;&nbsp;&nbsp;
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/032-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										ရွင္းျပ - ဝဋ္ ၃-ပါး</a></font></td>
										<td width="191">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/033-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၃။ ျပန္ၿခဳံေျပာ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/034-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၄။ ျပန္ၿခဳံေျပာ -ျခင္းရာ ၂၀</a></font></td>
									</tr>
									<tr>
										<td width="191">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/035-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၅။ ျပန္ၿခဳံေျပာ -ျခင္းရာ ၂၀</a></font></td>
										<td width="244">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/036-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၆။ စာေမးပြဲရူေထာင့္ျဖင့္&nbsp;&nbsp;&nbsp;&nbsp; 
										ရွင္းျပ 
</a> </font></td>
										<td width="191">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/037-DawKhinHlaTin-PatticcaSamuppada.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၇။ စာေမးပြဲရူေထာင့္ျဖင့္&nbsp; ရွင္းျပ 
</a> </font></td>
										<td>&nbsp;</td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/038-DawKhinHlaTin-Patthana-1.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၈။ ပ႒ာန္းပိုင္း - ပ႒ာန္းနည္း</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/039-DawKhinHlaTin-Patthana-2.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃၉။ ပ႒ာန္းပိုင္း - ပ႒ာန္းနည္း</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/040-DawKhinHlaTin-Patthana-3.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၀။ ေဟတုပစၥည္း</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/041-DawKhinHlaTin-Patthana-4.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၁။ အာရမၼဏပစၥည္း - အဓိပတိပစၥည္း</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/042-DawKhinHlaTin-Patthana-5.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၂။ အနႏ ၱရပစၥည္း - သမနႏ ၱရပစၥည္း</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/043-DawKhinHlaTin-Patthana-6.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၃။ သဟဇာတပစၥည္း - အညမညပစၥည္း</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/044-DawKhinHlaTin-Patthana-7.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၄။ နိႆယပစၥည္း- ဥပနိႆယပစၥည္း</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/045-DawKhinHlaTin-Patthana-8.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၅။ ပုေရဇာတပစၥည္း - ပစာၦဇာတပစၥည္း</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/046-DawKhinHlaTin-Patthana-9.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၆။ အာေသဝနပစၥည္း ---</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/047-DawKhinHlaTin-Patthana-10.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၇။ အာဟာရပစၥည္း ---</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/048-DawKhinHlaTin-Patthana-11.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄၈။ ၆-ရာသီေဝဖန္ခန္း</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/049-DawKhinHlaTin-Patthana-12.mp3">
										၄၉။ ေတကာလိက စသည္---</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/050-DawKhinHlaTin-Panatti-1.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၀။ ပညတ္</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/051-DawKhinHlaTin-Panatti-2.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၁။ ပညတ္</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/052-DawKhinHlaTin-Panatti-3.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၂။ ပညတ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/053-DawKhinHlaTin-Panatti-4.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၃။ ပညတ္</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/054-DawKhinHlaTin-Panatti-5.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၄။ ပညတ္</a></font></td>
										<td width="214">

<font face="Zawgyi-One">






								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/055-DawKhinHlaTin-Panatti-6.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၅။ ပညတ္</a></font></p>
</font>

										</td>
										<td width="193">
										<font size="4" face="Zawgyi-One">
										<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/056-DawKhinHlaTin-Q-A.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၆။ ေမးေျဖ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/057-DawKhinHlaTin-1977.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၇။ ေမးေျဖ - ၁၉၇၇</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/058-DawKhinHlaTin-1980.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၈။ ေမးေျဖ - ၁၉၈၀</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/059-DawKhinHlaTin-1981.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅၉။ ေမးေျဖ - ၁၉၈၁</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/060-DawKhinHlaTin-1982.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၀။ ေမးေျဖ - ၁၉၈၂</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/061-DawKhinHlaTin-1983.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၁။ ေမးေျဖ - ၁၉၈၃</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/062-DawKhinHlaTin-1984.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၂။ ေမးေျဖ - ၁၉၈၄</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/063-DawKhinHlaTin-1985.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၃။ ေမးေျဖ - ၁၉၈၅</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/064-DawKhinHlaTin-1986.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၄။ ေမးေျဖ - ၁၉၈၆</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/065-DawKhinHlaTin-1987.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၅။ ေမးေျဖ - ၁၉၈၇</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/066-DawKhinHlaTin-1988.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၆။ ေမးေျဖ - ၁၉၈၈</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/067-DawKhinHlaTin-1989.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၇။ ေမးေျဖ - ၁၉၈၉</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/068-DawKhinHlaTin-1990.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၈။ ေမးေျဖ - ၁၉၉၀</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/069-DawKhinHlaTin-1991.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၆၉။ ေမးေျဖ - ၁၉၉၁</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/070-DawKhinHlaTin-1992.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၀။ ေမးေျဖ - ၁၉၉၂</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/071-DawKhinHlaTin-1993.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၁။ ေမးေျဖ - ၁၉၉၃</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/072-DawKhinHlaTin-1994.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၂။ ေမးေျဖ - ၁၉၉၄</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/073-DawKhinHlaTin-1995.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၃။ ေမးေျဖ - ၁၉၉၅</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/074-DawKhinHlaTin-1996.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၄။ ေမးေျဖ - ၁၉၉၆</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/075-DawKhinHlaTin-1997.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၅။ ေမးေျဖ - ၁၉၉၇</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/076-DawKhinHlaTin-1998.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၆။ ေမးေျဖ - ၁၉၉၈</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/077-DawKhinHlaTin-1999.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၇။ ေမးေျဖ - ၁၉၉၉</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/078-DawKhinHlaTin-2000.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၈။ ေမးေျဖ - ၂၀၀၀</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/079-DawKhinHlaTin-2001.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၇၉။ ေမးေျဖ - ၂၀၀၁</a></font></td>
										<td width="193">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/080-DawKhinHlaTin-2002.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၈၀။ ေမးေျဖ - ၂၀၀၂</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/081-DawKhinHlaTin-2003.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၈၁။ ေမးေျဖ - ၂၀၀၃</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/082-DawKhinHlaTin-2004.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၈၂။ ေမးေျဖ - ၂၀၀၄</a></font></td>
										<td width="214">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/PyitSee/083-DawKhinHlaTin-2005.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၈၃။ ေမးေျဖ - ၂၀၀၅</a></font></td>
										<td width="193">&nbsp;</td>
										<td>&nbsp;</td>
									</tr>
								</tbody></table>
<table border="1" width="100%">
									<tbody><tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/001-DawKhinHlaTin-History.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၁။ အဘိဓမၼာ သမိုင္းေၾကာင္း</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/002-DawKhinHlaTin-Kammathana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၂။ ကမၼ႒ာန္းပိုင္း</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/003-DawKhinHlaTin-Kilesa-35.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၃။ - ကိေလသာ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/004-DawKhinHlaTin-Pahana-35.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၄။ -ကိေလသာပယ္ပုံ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/005-DawKhinHlaTin-Sasana-35.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
										၅။ သာသနာ ၃-ရပ္</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/006-DawKhinHlaTin-Sa-Si-Ki-36.mp3">
										၆။ သာသနာ - သိကၡာ ၃-ပါး</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/007-DawKhinHlaTin-Bhavana-36.mp3">
၇။ ဘာဝနာ ၃-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/008-DawKhinHlaTin-Sila-1.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၈။ သီလပိုင္း</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/009-DawKhinHlaTin-Sila-2.mp3">
၉။ - ၈ပါးသီလ</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/010-DawKhinHlaTin-Sila-3.mp3">
၁၀။ -စတုပါရိသုဒၶိသီလ</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/011-DawKhinHlaTin-Samadhi-1.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၁၁။ သမာဓိပိုင္း</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/012-DawKhinHlaTin-Samadhi-2.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၁၂။ သမာဓိပိုင္း</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/013-DawKhinHlaTin-Kammathana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၁၃။ စာေမးပြဲရူေထာင့္ျဖင့္ ရွင္းျပ 
</a> </font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/014-DawKhinHlaTin-Samatha-37.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၁၄။ စာေမးပြဲရူေထာင့္ျဖင့္ ရွင္းျပ 
</a> </font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/015-DawKhinHlaTin-Kasina-37.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၁၅။ ကသိုဏ္း ၁၀-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/016-DawKhinHlaTin-Asubha-37.mp3">
၁၆။ အသုဘ ၁၀-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/017-DawKhinHlaTin-Anussati-38.mp3">
၁၇။ အႏုႆတိ ၁၀-ပါး</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/018-DawKhinHlaTin-Anussati-38.mp3">
၁၈။ အႏုႆတိ ၁၀-ပါး</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/019-DawKhinHlaTin-Appamana-39.mp3">
၁၉။ အပၸမညာ ၄-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/020-DawKhinHlaTin-Brahmavihara.mp3">
၂၀။ ျဗဟၼဝိဟာရ ၄-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/021-DawKhinHlaTin-Aharepatikula.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၂၁။ အာဟာေရပဋိကူလ သညာ</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/022-DawKhinHlaTin-Catudhatu40.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၂၂။ စတုဓာတုဝဝတၳာန္</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/023-DawKhinHlaTin-Arupa-40.mp3">
၂၃။ အာရုပၸ ၄-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/024-DawKhinHlaTin-Carita-40.mp3">
၂၄။ စရိုက္ ၆-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/025-DawKhinHlaTin-CaritaKamma.mp3">
၂၅။ စရိုက္ ၆-ပါး</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/026-DawKhinHlaTin-Raga-41.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၂၆။ -ရာဂ စရိုက္</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/027-DawKhinHlaTin-Dosa-41.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၂၇။ - ေဒါသ စိတ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/028-DawKhinHlaTin-Moha-41.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၂၈။ - ေမာဟ စိတ္</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/029-DawKhinHlaTin-Carita-42.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၂၉။ စရိုက္ ၆-ပါးလုံးႏွင့္ သင့္ေလ်ာ္ေသာ ကမၼ႒ာန္း</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/030-DawKhinHlaTin-Carita-42.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၃၀။ စရိုက္ႏွင့္ ကမၼ႒ာန္း တြဲစပ္ပုံ</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/031-DawKhinHlaTin-JhanaKamma.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၃၁။ စ်ာန္ႏွင့္ ကမၼ႒ာန္း တြဲစပ္ပုံ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/032-DawKhinHlaTin-JhanaKamma.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၃၂။ စ်ာန္ႏွင့္ ကမၼ႒ာန္း တြဲစပ္ပုံ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/033-DawKhinHlaTin-JhanaKamma.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၃၃။ စ်ာန္ႏွင့္ ကမၼ႒ာန္း တြဲစပ္ပုံ</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/034-DawKhinHlaTin-Bhavana-42.mp3">
၃၄။ ဘာဝနာ ၃-ပါး</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/035-DawKhinHlaTin-Bhavana-43.mp3">
၃၅။ ဘာဝနာ ၃-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/036-DawKhinHlaTin-Bhavana-43.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၃၆။ ဘာဝနာႏွင့္ ကမၼ႒ာန္း တြဲစပ္ပုံ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/037-DawKhinHlaTin-Jhana-44.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၃၇။ ဘာဝနာႏွင့္ ကမၼ႒ာန္း တြဲစပ္ပုံ</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/038-DawKhinHlaTin-Nimitta-45.mp3">
၃၈။ နိမိတ္ ၃-ပါး</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/039-DawKhinHlaTin-Nimitta-45.mp3">
၃၉။ နိမိတ္ ၃-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/040-DawKhinHlaTin-Nimitta-45.mp3">
၄၀။ နိမိတ္ ၃-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/041-DawKhinHlaTin-Paramattha.mp3">
၄၁။ နိမိတ္ ၃-ပါး</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/042-DawKhinHlaTin-Nimitta-46.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၂။ နိမိတ္ႏွင့္ ဘာဝနာ တြဲစပ္ပုံ</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/043-DawKhinHlaTin-Vasibho.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၃။ ဝသီေဘာ္ ၅-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/044-DawKhinHlaTin-Avajjana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၄။ ဝသီေဘာ္ ၅-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/045-DawKhinHlaTin-Paccavekkhana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၅။ ဝသီေဘာ္ ၅-ပါး</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/046-DawKhinHlaTin-Vutthana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၆။ ဝသီေဘာ္ ၅-ပါး</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/047-DawKhinHlaTin-Samapajjana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၇။ ဝသီေဘာ္ ၅-ပါး</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/048-DawKhinHlaTin-Du%20Jhana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၈။ ဒုတိယစ်ာန္စသည္ ရပုံ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/049-DawKhinHlaTin-Ta%20Jhana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၄၉။ ဒုတိယစ်ာန္စသည္ ရပုံ</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/050-DawKhinHlaTin-JhanaSamapat.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၀။ စ်ာနသမာပတ္</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/051-DawKhinHlaTin-ArupaJhana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၁။ အရူပစ်ာန္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/052-DawKhinHlaTin-Abhinana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၂။ အဘိညာဥ္ခန္း</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/053-DawKhinHlaTin-Abhinana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၃။ အဘိညာဥ္ခန္း</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/054-DawKhinHlaTin-Abhinana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၄။ အဘိညာဥ္ခန္း</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/055-DawKhinHlaTin-Abhinana.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၅။ အဘိညာဥ္ခန္း</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/056-DawKhinHlaTin-Vipassana51.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၆။ ဝိပႆနာပိုင္း</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/057-DawKhinHlaTin-Vipassana51.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၇။ ဝိပႆနာပိုင္း</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/058-DawKhinHlaTin-DitthiVisuddhi.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၅၈။ ဒိ႒ိဝိသုဒၶိ</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/059-DawKhinHlaTin-SilaVisuddhi.mp3">
၅၉။ သီလဝိသုဒၶိ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/060-DawKhinHlaTin-CittaVisuddhi.mp3">
၆၀။ စိတၱဝိသုဒၶိ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/061-DawKhinHlaTin-DitthiVisuddhi.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၆၁။ ဒိ႒ိဝိသုဒၶိ</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/062-DawKhinHlaTin-Vipassana53.mp3">
၆၂။ ကခၤါဝိတရဏဝိသုဒၶိ</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/063-DawKhinHlaTin-Gotrabhu.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၆၃။ ေဂါၾတဘုဥာဏ္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/064-DawKhinHlaTin-Antraya-54.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၆၄။ ဥပကၠိေလသာ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/065-DawKhinHlaTin-Magga-53.mp3">
၆၅။ မဂၢါမဂၢ --</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/066-DawKhinHlaTin-Visuddhi-52.mp3">
၆၆။ မဂၢါမဂၢ --</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/067-DawKhinHlaTin-CulaSotapan.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၆၇။ စူဠေသာတာပန္</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/068-DawKhinHlaTin-Vipassana53.mp3">
၆၈။ ဝိပႆနာဉာဏ္ ၁၀-ပါး</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/069-DawKhinHlaTin-Vipassana53.mp3">
၆၉။ ဝိပႆနာဉာဏ္ ၁၀-ပါး</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/070-DawKhinHlaTin-Visuddhi.mp3">
၇၀။ ဉာဏဒႆန ဝိသုဒၶိ</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/071-DawKhinHlaTin-Pahana.mp3">
၇၁။ ဉာဏဒႆန ဝိသုဒၶိ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/072-DawKhinHlaTin-MagKicca59.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၇၂။ မဂ္ကိစၥ ၄-ခ်က္</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/073-DawKhinHlaTin-MagKicca59.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၇၃။ မဂ္ကိစၥ ၄-ခ်က္</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/074-DawKhinHlaTin-MagKicca59.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၇၄။ မဂ္ကိစၥ ၄-ခ်က္</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/075-DawKhinHlaTin-MaggaVithi60.mp3">
၇၅။ မဂၢဝီထိ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/076-DawKhinHlaTin-Sotapatti60.mp3">
၇၆။ ပစၥဝကၡဏာဝီထိ</a></font></td>
									</tr>
									<tr>
										<td width="219">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/077-DawKhinHlaTin-Sotapan60.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၇၇။ ေသာတာပန္</a></font></td>
										<td width="217">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/078-DawKhinHlaTin-Sakadagam65.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၇၈။ သကဒါဂါမ္</a></font></td>
										<td width="187">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/079-DawKhinHlaTin-Vimokkha62.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၇၉။ ဝိေမာကၡ</a></font></td>
										<td>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Abhidhamma-Level-03/KaMaHtan/080-DawKhinHlaTin-ForTutorial.mp3" class=" __zg" style="font-family: ZawGyi-One !important;">
၈၀။ အစမ္းစာေမးပြဲရွင္း ျပခ်က္</a></font></td>
									</tr>
								</tbody></table>
"""

soup = bs4(text, 'html.parser')

p = re.compile(r'(?P<word>[^0-9]+)')

#print(p)
count = 1
for key in soup.find_all('tr'):
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp3|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), key.find('td').find('a').get_text().strip()))
        count += 1
    except AttributeError as err:
        pass
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find('a').get('href'), key.find('td').find_next_sibling('td').find('a').get_text().strip()))
        count += 1
    except AttributeError as err:
        pass
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get('href'), key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get_text().strip()))
        count += 1
    except AttributeError as err:
        pass    
    try:
        counter = '{:03d}'.format(count)
        print('{}.mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find('a').get('href'), key.find('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find('a').get_text().strip()))
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
