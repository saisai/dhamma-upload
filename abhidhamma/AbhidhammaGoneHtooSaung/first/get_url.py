from bs4 import BeautifulSoup as bs4
import re
one = """

									
									<tbody><tr style="height: 25.5pt" height="34">
										<td style="height: 25.5pt; width: 266px; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" height="34">
										စိတ္ပိုင္း</td>
										<td style="width: 271px; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										စိတ္ပိုင္း</td>
										<td style="width: 299px; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										ေစတသိက္ပိုင္း</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0001.mp3">
										၁။ ဋီကာေက်ာ္က်မ္း သမိုင္းအက်ဥ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										အဆက္….</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										အဆက္….</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0002.mp3">
										၂။ ပရမတၳတရား (၄)ပါး အဖြင့္ – စိတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0078.mp3">
										၇၈။ ဝိပါတ္စိတ္ခ်င္းကြဲျပားပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0152.mp3">
										၁၅၂။ ဖြင့္ဆိုပံု အစီအစဥ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0003.mp3">
										၃။ ေစတသိတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0079.mp3">
										၇၉။ ေလာကုတ္အက်ဥ္း (၈)မွ (၄၀)ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0153.mp3">
										၁၅၃။ ေလာကုတ္စိတ္ သဂၤဟနည္းအဖြင့္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0004.mp3">
										၄။ ရုပ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0080.mp3">
										၈၀။ ပါဒကစ်ာန္ႏွင့္တူစြာ မဂ္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0154.mp3">
										၁၅၄။ ေလာကုတ္စိတ္ သဂၤဟနည္းအဖြင့္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0005.mp3">
										၅။ နိဗၺာန္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0081.mp3">
										၈၁။ ပုဂၢလဇၥ်ာသယ ေလ်ာစြာမဂ္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0155.mp3">
										၁၅၅။ မဟဂၢဳတ္စိတ္ သဂၤဟနည္းအဖြင့္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0006.mp3">
										၆။ စိတ္ပိုင္းအဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0082.mp3">
										၈၂။ စ်ာန္ရပုဂၢိဳလ္အား ပဥၥဂႌကမဂၤျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0156.mp3">
										၁၅၆။ ကာမေသာနစိတ သဂၤဟနည္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0007.mp3">
										၇။ ကာမာဝစရပုဒါ၏ ဝစနတၳ . . .</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0083.mp3">
										၈၃။ ရတနတၱယပဏာမအဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0157.mp3">
										၁၅၇။ ကာမကုသိုလ္ႏွင့္ ဝိပါက္စိတ္တို႔ 
										အာရံုမတူ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0008.mp3">
										၈။ ။ ရူပါစရပုဒ္၏ . . .</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0084.mp3">
										၈၄။ “အဘိဓမၼတၱသဂၤဟ” ပါဌ္ျဖင့္ ..</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0158.mp3">
										၁၅၈။ ကာမကုသိုလ္ႏွင့္ ဝိပါက္စိတ္တို႔ 
										အာရံုမတူ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0009.mp3">
										၉။ ။ ေကာကုတၱရံပုဒ္၏ . . .</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0085.mp3">
										၈၅။ က်မ္းအစ၌ ရတနတၱယပဏာမျပဳျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0159.mp3">
										၁၅၉။ အကုသိလ္စိတ္ သဂၤဟနည္းအဖြင့္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0010.mp3">
										၁၀။ ။</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0086.mp3">
										၈၆။ “သမၼာသမၺဳဒၶ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0160.mp3">
										၁၆၀။ အဟိတ္စိတ္ သဂၤဟနည္းအဖြင့္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0011.mp3">
										၁၁။ -(၁)ကာမာဝစရစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0087.mp3">
										၈၇။ ပုဒ္ႏွစ္ပါးျဖင့္ ခ်ီးမႊမ္းေသာဂုဏ္…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0161.mp3">
										၁၆၁။ ဝိသသက ေစတသိက္မ်ား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0012.mp3">
										၁၂။ – ေလာဘမူစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0088.mp3">
										၈၈။ “သဒၶမၼ”ပုဒ္အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0162.mp3">
										၁၆၂။ စိတ္ႏွင့္အမွ် ေစတသိက္ျပားပံု</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0013.mp3">
										၁၃။ “ဒိ႒ိ” ပုဒ္ . . .</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0089.mp3">
										၈၉။ ေမး-ေျဖ (ရတနတၱယပဏာမဆိုင္ရာ)</a></td>
										<td style="font-weight: 400; font-family: Zawgyi-One, sans-serif; text-align: general; vertical-align: bottom; color: black; font-size: 10.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										&nbsp;</td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0014.mp3">
										၁၄။ သခၤါရ ပုဒ္၏</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0090.mp3">
										၉၀။ ၁၉၇၈ မွ ၂၀၀၅ အထိ</a></td>
										<td style="font-weight: 400; font-family: Zawgyi-One, sans-serif; text-align: general; vertical-align: bottom; color: black; font-size: 10.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										&nbsp;</td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0015.mp3">
										၁၅။ ဥေပကၡာ ပုဒ္၏</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0091.mp3">
										၉၁။ ၁၉၇၈ မွ ၂၀၀၅ အထိ</a></td>
										<td style="font-weight: 400; font-family: Zawgyi-One, sans-serif; text-align: general; vertical-align: bottom; color: black; font-size: 10.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										&nbsp;</td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0016.mp3">
										၁၆။ ဒိ႒ိျဖစ္ေၾကာင္း (၂)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0092.mp3">
										၉၂။ ၁၉၇၈ မွ ၂၀၀၅ အထိ</a></td>
										<td style="font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="299">
										ပကိဏ္းပိုင္း</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0017.mp3">
										၁၇။ ေသာမနႆယ ဥေပကၡာ သတၱိအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0093.mp3">
										၉၃။ ၁၉၇၈ မွ ၂၀၀၅ အထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0163.mp3">
										၁၆၃။ intro</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0018.mp3">
										၁၈။ အျပစ္မရွိယူဆ၍ လြန္က်ဴးျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0094.mp3">
										၉၄။ ၁၉၇၈ မွ ၂၀၀၅ အထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0164.mp3">
										၁၆၄။ ပကိဏ္းပိုင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0019.mp3">
										၁၉။ ပညတ္ေတာ္ဥပေဒကိုသိလွ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271">
										&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0165.mp3">
										၁၆၅။ ေဝဒနသဂၤဟ…</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0020.mp3">
										၂၀။ ေလာဘဟိတ္သာမက</a></td>
										<td style="font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="271">
										ေစတသိက္ပိုင္း</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0166.mp3">
										၁၆၆။ သုခဒုကၡေဝဒနာကို ခြဲျခမ္းေဟာရပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0021.mp3">
										၂၁။ ေလာဘမူစိတ္(၈)ပါးျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0095.mp3">
										၉၅။ ေစတသိက္ပိုင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0167.mp3">
										၁၆၇။ ေဟတုသဂၤဟ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0022.mp3">
										၂၂။ ျပန္ရွင္းျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0096.mp3">
										၉၆။ ေစသိက္လကၡဏာ (၄)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0168.mp3">
										၁၆၈။ ဟိတ္(၆)ပါးတို႔ကို “မူလ”ေခၚရျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0023.mp3">
										၂၃။ ေဒါသမူစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0097.mp3">
										၉၇။ ေစသိက္လကၡဏာ (၄)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0169.mp3">
										၁၆၉။ ကိစၥသဂၤဟ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0024.mp3">
										၂၄။ ေဒါသသည္ နာမ္တရားျဖစ္ပါလွ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0098.mp3">
										၉၈။ အညသမာန္းရာသီ အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0170.mp3">
										၁၇၀။ ဌာန</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0025.mp3">
										၂၅။ ေဒါမနႆ ပဋိဃအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										၉<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0099.mp3">၉။ 
										သဗၺစိတၱ ေစတသိက္ (၇)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0171.mp3">
										၁၇၁။ ကိစၥႏွင့္ ဌာန အထူး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0026.mp3">
										၂၆။ ေဒါမနႆ ျဖစ္ေၾကာင္းမ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0100.mp3">
										၁၀၀။ — ။– ေဝဒနာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0172.mp3">
										၁၇၂။ ဥ-တီ(၂)ပါးသာ ပဋိသေႏၶကိစၥတပ္ရျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0027.mp3">
										၂၇။ ေမာဟမူစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0101.mp3">
										၁၀၁။ — ။– သညာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0173.mp3">
										၁၇၃။ မဂၤ စသည္တို႔ ေဇာကိစၥတပ္ရျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0028.mp3">
										၂၈။ အလံုးစံုေသာ အာရံုတို႔၌</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0102.mp3">
										၁၀၂။ — ။– ေစတနာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0174.mp3">
										၁၇၄။ ဒြါရသဂၤဟ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0029.mp3">
										၂၉။ “ေမာမူဟ” ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0103.mp3">
										၁၀၃။ — ။– ဧကဂၢတာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0175.mp3">
										၁၇၅။ စကကၡဳဒြါရိကစိတ္ (၄၆)ပါးတို႔ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0030.mp3">
										၃၀။ မာတိကာျဖင့္ ရွင္းျပခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0104.mp3">
										၁၀၄။ — ။– ဇီဝိတိေျႏၵ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0176.mp3">
										၁၇၆။ သီလအဓိ႒ာန္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0031.mp3">
										၃၁။ “အကုသလ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0105.mp3">
										၁၀၅။ — ။– မနသိကာရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0177.mp3">
										၁၇၇။ ပဥၥဒြါရိကစိတတတတ္ 
										(၃)ပါးျဖစ္ရျခင္းးးး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0032.mp3">
										၃၂။ အဟိတ္စိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0106.mp3">
										၁၀၆။ ပကိဏ္းေစတသိက္ (၆)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0178.mp3">
										၁၇၈။ ဝတၳဳသဂၤဟ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0033.mp3">
										၃၃။ “စကၡဳ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0107.mp3">
										၁၀၇။ အကုသိုလ္ေစတသိက္ – ဒိ႒ိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0179.mp3">
										၁၇၉။ ရူပဘံု၌ ဃာ-ဇိ-ကာ မရွိျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0034.mp3">
										၃၄။ “ကာယ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0108.mp3">
										၁၀၈။ ဒ႒ိႏွင့္ ညာဏ္အထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0180.mp3">
										၁၈၀။ ပဥၥဝိညာဏဓာတ္ – မရျခင္းအေၾကာင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0035.mp3">
										၃၅။ “ဒုကၡ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0109.mp3">
										၁၀၉။ ညာဏ္ႏွင့္တူေသာ တရားမ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0181.mp3">
										၁၈၁။ ဓာတ္(၃)ပါးအထူး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0036.mp3">
										၃၆။ “ဝိပါက”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0110.mp3">
										၁၁၀။ ။ မာန</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0182.mp3">
										၁၈၂။ ဝတၳဳရုပ္၌ မွီ၍ ျဖစ္ေသာစိတ္ (၄၃)ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0037.mp3">
										၃၇။ “သုခ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0111.mp3">
										၁၁၁။ ။ ေဒါသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0183.mp3">
										၁၈၃။ ရူပကု-ႀကိတို႔ အရူပဘံု၌ မျဖစ္ျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0038.mp3">
										၃၈။ အဟိတ္ကုဝိ သႏၲီရဏ(၂)ပါး ဆိုရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0112.mp3">
										၁၁၂။ ။ ဣႆာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0184.mp3">
										၁၈၄။ အာရမၼဏသဂၤဟ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0039.mp3">
										၃၉။ အကုဝိ သႏၲီရဏ ဥေပကၡာျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0113.mp3">
										၁၁၃။ ။ ထိနမိဒၶ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0185.mp3">
										၁၈၅။ စကၡဳဒါြရ၌ျဖစ္ေသာ စိတ္တို႔၏ အာရံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0040.mp3">
										၄၀။ ပဋိဃကို အဗ်ာကတတို႔၌ မရႏိုင္ျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0114.mp3">
										၁၁၄။ ။ ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0186.mp3">
										၁၈၆။ ဒြါရဝိမုတ္စိတ္၏ အာရံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0041.mp3">
										၄၁။ စကၡဳဝိညာဏ္၏ စေသာ (၄)ပါးတို႔၏</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0115.mp3">
										၁၁၅။ ေသာဘနရာသီ အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0187.mp3">
										၁၈၇။ ေမးခြန္း – ကာမဘံုမွ စုေတေသာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0042.mp3">
										၄၂။ ကာယဝိညာဥ္၏ ဒုကၡသဟဂုတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0116.mp3">
										၁၁၆။ – သဒၶါ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0188.mp3">
										၁၈၈။ ကာမဧကန္ (၂၅)ပါး၏ အာရံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0043.mp3">
										၄၃။ သမၸဋိစၧိဳင္းေဒြ၏ ဒုကၡသဟဂုတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0117.mp3">
										၁၁၇။ – အေလာဘ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0189.mp3">
										၁၈၉။ ကာမ၊ မဟဂၢဳတ္ ၊ နိဗၺာန္ ၊ ပညတ္ 
										အေနကန္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0044.mp3">
										၄၄။ အဟိတ္ကုဝိ ဥတီ၏ ေသာမႆ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0118.mp3">
										၁၁၈။ – အေလာဘ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0190.mp3">
										၁၉၀။ ဥာသံ – ကာမကုသိုလ္ႏွင့္ ကုဘိ ံ၏ 
										အာရံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0045.mp3">
										၄၅။ – ။ – (၈)ပါးတို႔ အေဟတုက</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0119.mp3">
										၁၁၉။ အေဒါသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0191.mp3">
										၁၉၁။ အားလံုးစံုေသာအာရံုကို 
										အာရံုျပဳေသာစိတ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0046.mp3">
										၄၆။ အကုဝိ၌ သဟိတ္မျဖစ္သင့္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0120.mp3">
										၁၂၀။ စံုတြဲေစတသိက္မ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0192.mp3">
										၁၉၂။ (၆)ပါးေသာ စိတ္တို႔…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0047.mp3">
										၄၇။ “ပဥၥဒြါရာဝဇၨန” ပုဒ္၏ အဓိပၸါယ္ …</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0121.mp3">
										၁၂၁။ ယုဂဠ ေစတသိက္မ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0193.mp3">
										၁၉၃။ ဧကန္အာရံုမ်ား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0048.mp3">
										၄၈။ ပဥၥဒြါရာဝဇၨန္း၏ ပုဒ္၌ မေနာဒြာရအရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0122.mp3">
										၁၂၂။ ဝိရတီေစတသိက္ (၃)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0194.mp3">
										၁၉၄။ ၁၉၇၈ ခုႏွစ္၊ နံပတ္ (၁)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0049.mp3">
										၄၉။ “မေနာဒြါရာဝဇၨန” ပုဒ္၌ မေနာဒြာရအရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0123.mp3">
										၁၂၃။ – ဝိရတီအျပား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0195.mp3">
										၁၉၅။ ၁၉၇၈ ခုႏွစ္၊ နံပတ္ (၂)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0050.mp3">
										၅၀။ “မေနာဒြါရာဝဇၨန” ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0124.mp3">
										၁၂၄။ အပၸမညာေစတသိက္ (၂)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0196.mp3">
										၁၉၆။ ၁၉၇၈ ခုႏွစ္၊ နံပတ္ (၃)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0051.mp3">
										၅၁။ မေနာဒြါရာဝဇၨန္း၏ ဥေပကၡာ သဟဂုတ</a>္</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0125.mp3">
										၁၂၅။ အပၸမညာေစတသိက္ (၂)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0197.mp3">
										၁၉၇။ ၁၉၇၉ ခုႏွစ္၊ နံပတ္ (၁)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0052.mp3">
										၅၂။ အဟိတ္စိတ္အေၾကာင္း (ဇနကဟိတ္…)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0126.mp3">
										၁၂၆။ – ကရုဏာေစတသိက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0198.mp3">
										၁၉၈။ ၁၉၇၉ ခုႏွစ္၊ နံပတ္ (၂)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0053.mp3">
										၅၃။ ေသာဘနစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0127.mp3">
										၁၂၇။ ပညိေျႏၵ ေစတသိက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0199.mp3">
										၁၉၉။ ၁၉၇၉ ခုႏွစ္၊ နံပတ္ (၄)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0054.mp3">
										၅၄။ ကာမေသာဘနစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0128.mp3">
										၁၂၈။ သမၸေယာဂနည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0200.mp3">
										၂၀၀။ ၁၉၈၀ ခုႏွစ္၊ နံပတ္ (၁)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0055.mp3">
										၅၅။ “ဥာဏ”ပုဒ္၏ အဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0129.mp3">
										၁၂၉။ ပဏိဏ္းေစတသိက္ သမၸေယာဂနည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0201.mp3">
										၂၀၁။ ၁၉၈၀ ခုႏွစ္၊ နံပတ္ (၂)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0056.mp3">
										၅၆။ မဟာကုသိုလ္ ဥေပကၡာျဖစ္ေၾကာင္း…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0130.mp3">
										၁၃၀။ – ဝိတက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0202.mp3">
										၂၀၂။ ၁၉၈၀ ခုႏွစ္၊ နံပတ္ (၃)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0057.mp3">
										၅၇။ – ။ – စိတ္(၈)ပါး ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0131.mp3">
										၁၃၁။ – ဝိတက</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0203.mp3">
										၂၀၃။ ၁၉၈၀ ခုႏွစ္၊ နံပတ္ (၃)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0058.mp3">
										၅၈။ – ။ – စိတ္အျပား . .</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0132.mp3">
										၁၃၂။ – ဝိစာရ ၊ ပီတိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0204.mp3">
										၂၀၄။ ၁၉၈၃ – ၁၉၉၁ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0059.mp3">
										၅၉။ “ကုသလ”ကုသလပုဒ္အရေကာက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0133.mp3">
										၁၃၃။ – အဓိေမကၡ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0205.mp3">
										၂၀၅။ ပံ့သကူစိတ္ထား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0060.mp3">
										၆၀။ မဟာဝိပါတ္စိတ္ ေသာမနႆ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0134.mp3">
										၁၃၄။ အကု-ေစ သမၸေယာဂနည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0206.mp3">
										၂၀၆။ ၁၉၈၈ – ၁၉၉၅ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0061.mp3">
										၆၁။ ။ ဥာဏသမၸယုတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0135.mp3">
										၁၃၅။ – ေဒါသ၊ ဣႆာယွဥ္ေသာစိတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0207.mp3">
										၂၀၇။ ၁၉၈၁ – ၂၀၀၄ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0062.mp3">
										၆၂။ ။ အသခၤါရိက . ..</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0136.mp3">
										၁၃၆။ ေသာဘန – ေစ သမၸေယာဂနည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0208.mp3">
										၂၀၈။ ၁၉၈၂ – ၂၀၀၁ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0063.mp3">
										၆၃။ ရူပါဝစရစိတ္အဖြင့္ (ဝိတက္)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0137.mp3">
										၁၃၇။ – ဝိရတီ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0209.mp3">
										၂၀၉။ ေဟတုသဂၤဟဆိုင္ရာ အေမးအေျဖမ်ား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0064.mp3">
										၆၄။ ရုပါဝစရစိတ္အဖြင့္ (ဝိတက္)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0138.mp3">
										၁၃၈။ ။ ဝိသံု ဝိသုံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0210.mp3">
										၂၁၀။ ကိစၥသဂၤဟဆုိင္ရာ အေမးအေျဖမ်ား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0065.mp3">
										၆၅။ ။ (ဝိစာရ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0139.mp3">
										၁၃၉။ – ။ နိယတ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0211.mp3">
										၂၁၁။ ေစတသိက္ပိုင္း ဆိုင္ရာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0066.mp3">
										၆၆။ ။ (ဧကဂၢတာ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0140.mp3">
										၁၄၀။ – ။ ဧကေတာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0212.mp3">
										၂၁၂။ ၁၉၇၈ – ၁၉၇၉ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0067.mp3">
										၆၇။ ဝိတက္စေသာ (၅)ပါး အေပါင္းကိုသာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0141.mp3">
										၁၄၁။ – ။ ဧကေတာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0213.mp3">
										၂၁၃။ ၁၉၈၀ – ၁၉၈၁ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0068.mp3">
										၆၈။ ရူပ၊ အရူပ၊ ေလာကုတ္စိတ္တို႔ 
										ကြဲျပားပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0142.mp3">
										၁၄၂။ ေလာကီႏွင့္ ေလာကုတ္ ဝိရတီအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0214.mp3">
										၂၁၄။ ၁၉၈၂ – ၁၉၈၃ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0069.mp3">
										၆၉။ ရူပဝိပါတ္စိတ္ကို စ်ာန္ႏွင့္တူစြာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0143.mp3">
										၁၄၃။ အပၸမညာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0215.mp3">
										၂၁၅။ ၁၉၈၄ – ၁၉၈၅ – ၁၉၈၆ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0070.mp3">
										၇၀။ အရူပါဝစရစိတ္ အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0144.mp3">
										၁၄၄။ အပၸမညာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0216.mp3">
										၂၁၆။ ၁၉၈၇ – ၁၉၈၈ – ၉၁၈၉ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0071.mp3">
										၇၁။ နိဒႆနနည္းမွ်သာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0145.mp3">
										၁၄၅။ – မယွဥ္ေသာစိတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0217.mp3">
										၂၁၇။ ၁၉၉၀ – ၁၉၉၇ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0072.mp3">
										၇၂။ အရူပစိတ္၏ အာရမၼဏေဘဒျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0146.mp3">
										၁၄၆။ – ။ – ဝီထိျဖင့္ရွင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0218.mp3">
										၂၁၈။ ၁၉၉၃ – ၁၉၉၄ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0073.mp3">
										၇၃။ ေလာကုတၱရာစိတ္အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0147.mp3">
										၁၄၇။ ဧကန္ေသာမနႆစိတ္၌သာ ယွဥ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0219.mp3">
										၂၁၉။ ၁၉၉၅ ခုႏွစ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0074.mp3">
										၇၄။ ။ သကဒါဂါမိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0148.mp3">
										၁၄၈။ – ေကစိဝါဒ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0220.mp3">
										၂၂၀။ ၁၉၉၆ – ၂၀၀၀ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0075.mp3">
										၇၅။ ။ အနာဂါမိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0149.mp3">
										၁၄၉။ အနယတေယာဂီေစတသိက္ (၁၁)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0221.mp3">
										၂၂၁။ ၂၀၀၁ -၂၀၀၅ ခုႏွစ္ထိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0076.mp3">
										၇၆။ သံေယာဇဥ္တို႔ ပယ္ျခင္းကိစၥအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0150.mp3">
										၁၅၀။ သဂၤဟနည္းအဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0222.mp3">
										၂၂၂။ ေစတသိက္ပိုင္းဆိုင္ရာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="266" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0077.mp3">
										၇၇။ မဂ္စိတ္ (၁)ႀကိမ္သာ ျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="271" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0151.mp3">
										၁၅၁။ – သဂၤဟနည္းအသံုးခ်ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="299" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0223.mp3">
										၂၂၃။ ပကိဏ္းပိုင္ဆိုင္ရာ ေမး/ေျဖမ်ား</a></td>
									</tr>
								</tbody>									                                
"""

#soup = bs4(one, 'html.parser')
#soup = bs4(two, 'html.parser')
soup = bs4(one, 'html.parser')


with open('titles_links.txt', 'w') as f:

    count = 1
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
