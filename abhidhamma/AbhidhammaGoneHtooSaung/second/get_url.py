from bs4 import BeautifulSoup as bs4
import re
one = """

									<colgroup>
										<col style="width: 200pt" width="266">
										<col style="width: 214pt" width="285">
										<col style="width: 209pt" width="278">
									</colgroup>
									<tbody><tr style="height: 27.75pt" height="37">
										<td style="height: 27.75pt; width: 200pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="266" height="37">
										ဝီထိပိုင္း</td>
										<td style="width: 214pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="285">
										ဝီထိပိုင္း</td>
										<td style="width: 209pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="278">
										ဝီထိမုတ္ပိုင္း</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0224.mp3">
										၂၂၄။ intro</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										အဆက္…</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										အဆက္…</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0225.mp3">
										၂၂၅။ ဝီထိအဓိပၸါယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0325.mp3">
										၃၂၅။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0424.mp3">
										၄၂၄။ – ။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0226.mp3">
										၂၂၆။ ဝီထိအမည္သတ္မွတ္ပံု (၂)မ်ိဳး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0326.mp3">
										၃၂၆။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0425.mp3">
										၄၂၅။ မရဏာသႏၷေဇာ၏အာ႐ံုသည္ ပစၥဳပၸန္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0227.mp3">
										၂၂၇။ ဆ ဆကၠတရား (အဘိဓမၼာသရုပ္)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0327.mp3">
										၃၂၇။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0426.mp3">
										၄၂၆။ – ဂတိနိမိတ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0228.mp3">
										၂၂၈။ ဝိသယပၸဝတၱိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0328.mp3">
										၃၂၈။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0427.mp3">
										၄၂၇။ မရဏာသႏၷေဇာႏွင့္ စုတိက်ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0229.mp3">
										၂၂၉။ ဝီထိမုတ္စိတ္တို႔၏ ဝိသယပၸပတၱိ (၃)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0329.mp3">
										၃၂၉။ – မေနာဒြါရကာမေဇာဝါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0428.mp3">
										၄၂၈။ ပဋိသေႏၶစိတ္ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0230.mp3">
										၂၃၀။ ဝီထိစိတ္တို႔၏ ဝိသယပၸဝတၱိ (၆)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0330.mp3">
										၃၃၀။ – မေနာဒြါရကာမေဇာဝါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0429.mp3">
										၄၂၉။ – (၁)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0231.mp3">
										၂၃၁။ – ဝိသယပၸဝတၱိ (၄)ပါး / (၂)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0331.mp3">
										၃၃၁။ – မေနာဒြါရကာမေဇာဝါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0430.mp3">
										၄၃၀။ – (၂)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0232.mp3">
										၂၃၂။ စိတ္သက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0332.mp3">
										၃၃၂။ – တဒါရမၼဏနိယာမ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0431.mp3">
										၄၃၁။ အယူမွားမႈဒိဠိမျဖစ္ရန္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0233.mp3">
										၂၃၃။ စိတ္၏ ဌီခဏ ရွိ-မရွိ ျပႆနာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0333.mp3">
										၃၃၃။ – တဒါရမၼဏနိယာမ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0432.mp3">
										၄၃၂။ ပဋိသေႏၶစိတ္၏အာ႐ံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0234.mp3">
										၂၃၄။ ရုပ္သက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0334.mp3">
										၃၃၄။ – ဇဝနနိယာမ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0433.mp3">
										၄၃၃။ ပဋိသေႏၶ၊ ဘဝင္တို႔၏အာ႐ံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0235.mp3">
										၂၃၅။ စိတ္သက္တို၍ ရုပ္သက္ရွည္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0335.mp3">
										၃၃၅။ – ဇဝနနိယာမ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0434.mp3">
										၄၃၄။ ပဋိသေႏၶေနျခင္းအေၾကာင္း(၃)ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0236.mp3">
										၂၃၆။ စိတ္သက္ – ရုပ္သက္ျဖစ္ပံု ဥပမာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0336.mp3">
										၃၃၆။ – ဇဝနနိယာမ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0435.mp3">
										၄၃၅။ စုတိေနာင္ ပဋိသေႏၶေႏွာင္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0237.mp3">
										၂၃၇။ လကၡဏရုပ္ (၄)ပါး – ၾကဥ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0337.mp3">
										၃၃၇။ စံျပေမးေျဖမ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0436.mp3">
										၄၃၆။ ႐ူပစုတိေနာင္ အဟိတ္ပဋိ–မရ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0238.mp3">
										၂၃၈။ စကၡဳဒြါရအတိမဟႏၲာရံုဝီထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0338.mp3">
										၃၃၈။ ၁၉၈၄</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0437.mp3">
										၄၃၇။ ဘဝင္, စုတိျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0239.mp3">
										၂၃၉။ ပသာဒရုပ္ (၅)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0339.mp3">
										၃၃၉။ ၁၉၈၅-၈၆</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0438.mp3">
										၄၃၈။ သံသရာစက္ လည္ပံု ျပတ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0240.mp3">
										၂၄၀။ ပဥၥရံုတို႔ ပဥၥဒြါရ၌ထင္လာပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0340.mp3">
										၃၄၀။ ၁၉၈၇-၈၈</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0439.mp3">
										၄၃၉။ ေမးေျဖ-၁၉၇၈-၁၉၈၀</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0241.mp3">
										၂၄၁။ စိတ္အစဥ္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0341.mp3">
										၃၄၁။ ၁၉၈၉-၉၄</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0440.mp3">
										၄၄၀။ ၁၉၈၁-၁၉၈၈</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0242.mp3">
										၂၄၂။ ဘဝင္ႏွစ္ႀကိမ္လႈပ္ရျခင္းအေၾကာင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0342.mp3">
										၃၄၂။ ၁၉၉၅-၂၀၀၆</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0441.mp3">
										၄၄၁။ ၁၉၈၉-၁၉၉၂</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0243.mp3">
										၂၄၃။ ဘဝင္လႈပ္ရျခင္းအေၾကာင္း</a></td>
										<td style="font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										ဝီထိမုတ္ပိုင္း</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0442.mp3">
										၄၄၂။ ၁၉၉၃-၁၉၉၆</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0244.mp3">
										၂၄၄။ ပဥၥဒြါရာဝဇၨန္း စေသာ ဝီထိစိတ္မ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0343.mp3">
										၃၄၃။ Intro</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0443.mp3">
										၄၄၃။ ၁၉၉၇-၂၀၀၃</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0245.mp3">
										၂၄၅။ စကၡဳဝိညာဏ္စသည္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0344.mp3">
										၃၄၄။ ဘူမိစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0444.mp3">
										၄၄၄။ ၂၀၀၄-၂၀၀၆</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0246.mp3">
										၂၄၆။ ။ ေမးခြန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0345.mp3">
										၃၄၅။ – အပါယ္(၄)ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0445.mp3">
										၄၄၅။ ဋီကာ႐ွင္းတမ္း- ဘူမိစတုကၠ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0247.mp3">
										၂၄၇။ စကၡဳနာ ရူပံ ဒိသြာ .</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0346.mp3">
										၃၄၆။ – ကာမသုဂတိ(၇)ဘံု – လူ(မႏုႆ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0446.mp3">
										၄၄၆။ ကမၼစတုကၠ</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0248.mp3">
										၂၄၈။ ကာမေဇာျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0347.mp3">
										၃၄၇။ – စာတုမဟာရာဇ္..</a></td>
										<td style="font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										ရုပ္ပိုင္း</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0249.mp3">
										၂၄၉။ ကာမေဇာတို႔ ေစာရာအႀကိမ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0348.mp3">
										၃၄၈။ – ရူပါဝစရ (၁၆)ဘံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0447.mp3">
										၄၄၇။ ႐ူပသမုေဒၵသ-မဟာဘုတ္ျမည္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0250.mp3">
										၂၅၀။ တဒါရံုျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0349.mp3">
										၃၄၉။ – အရူပါဝစရ (၄)ဘံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0448.mp3">
										၄၄၈။ – မ်က္လွည့္ဆရာႏွင့္တူပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0251.mp3">
										၂၅၁။ ဘဝဂၤပါေတာ = ဘဝင္က်သည္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0350.mp3">
										၃၅၀။ – ဘံု၌ ပုဂၢဳိလ္ရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0449.mp3">
										၄၄၉။ – ပထဝီအဓိပၸါယ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0252.mp3">
										၂၅၂။ ဝိထိစိတ္ျဖစ္ပံု (သရက္သီးဥပမာ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0351.mp3">
										၃၅၁။ ပဋိသႏၶိစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0450.mp3">
										၄၅၀။ – အာေပါ – – – ။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0253.mp3">
										၂၅၃။ မဟႏၲာရံုဝီထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0352.mp3">
										၃၅၂။ – ဘုမၼသိတနတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0451.mp3">
										၄၅၁။ ဥပါဒါ႐ုပ္အဖြင့္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0254.mp3">
										၂၅၄။ မဟႏၲာရံုဝီထိ၌ တဒါရံုမက်ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0353.mp3">
										၃၅၃။ – ဇစၥႏၶ…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0452.mp3">
										၄၅၂။ ပသာဒ႐ုပ္ (၅) ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0255.mp3">
										၂၅၅။ တဒါရံု(၁)ႀကိမ္ မျဖစ္ျခင္းအေၾကာင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0354.mp3">
										၃၅၄။ – ဇစၥႏၶ…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0453.mp3">
										၄၅၃။ – စကၡဳပသာဒ . . .</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0256.mp3">
										၂၅၆။ – ။ – ေမးခြန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0355.mp3">
										၃၅၅။ – ဇစၥဗဓိရ…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0454.mp3">
										၄၅၄။ – ေဂါစရ႐ုပ္ (၇) ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0257.mp3">
										၂၅၇။ – ။ – ေမးခြန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0356.mp3">
										၃၅၆။ – ပ႑က…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0455.mp3">
										၄၅၅။ – ေမးခြန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0258.mp3">
										၂၅၈။ ပရိတၱာရံုဝီထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0357.mp3">
										၃၅၇။ မဟာဝိပါက္စိတ္(၈)ပါးျဖင့္ 
										ပဋိသေႏၶေနသူ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0456.mp3">
										၄၅၆။ – ဘာဝ႐ုပ္ ၂-ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0259.mp3">
										၂၅၉။ – ။ -၌ ေဇာမျဖစ္ျခင္းအေၾကာင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0358.mp3">
										၃၅၈။ စာတုမဟာရာဇ္နတ္သက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0457.mp3">
										၄၅၇။ ဟဒယ ဝတၳဳ႐ုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0260.mp3">
										၂၆၀။ အတိပရိတၱာရံုဝီထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0359.mp3">
										၃၅၉။ အထက္အထက္နတ္တို႔၏ အသက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0458.mp3">
										၄၅၈။ ။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0261.mp3">
										၂၆၁။ အတိပရိတၱာရံုဝီထိ၌ (န)ျဖစ္၍ 
										(ဒ)မျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0360.mp3">
										၃၆၀။ ရူပဋိသေႏၶ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0459.mp3">
										၄၅၉။ ။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0262.mp3">
										၂၆၂။ ပဥၥဒြါရဝီထိ၌ ျဖစ္ေသာ စိတ္သရုပ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0361.mp3">
										၃၆၁။ – ဒုတိယစ်ာန္ဘံုပဋိသေႏၶ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0460.mp3">
										၄၆၀။ – ဇီဝိတ႐ုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0263.mp3">
										၂၆၃။ မေနာဒြါရဝီထိ၊ မေနာဒြါရ ကာမေဇာဝါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0362.mp3">
										၃၆၂။ ‘ပ’စ်ာန္ ျဗဟၼာတို႔၏ သက္တမ္းကို</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0461.mp3">
										၄၆၁။ – အာဟာရ႐ုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0264.mp3">
										၂၆၄။ မေနာဒြါရ၌ ထင္ေသာအာရံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0363.mp3">
										၃၆၃။ – အသေခၤ်ယ်ကပ္ ပမာဏ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0462.mp3">
										၄၆၂။ သဘာဝ႐ုပ္ စသည္ျမည္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0265.mp3">
										၂၆၅။ မေနာဒြာရ၌ ထင္ေသာအာရံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0364.mp3">
										၃၆၄။ အရူပ ပဋိသေႏ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0463.mp3">
										၄၆၃။ အာကာသဓာတ္ပရိေစၧဒ႐ုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0266.mp3">
										၂၆၆။ – ။ – (ေမးခြန္း)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0365.mp3">
										၃၆၅။ ကမၼစတုကၠ – ကိစၥစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0464.mp3">
										၄၆၄။ ကာယဝိညတ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0267.mp3">
										၂၆၇။ – ။ – ျဖစ္ေသာစိတ္သရုပ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0366.mp3">
										၃၆၆။ – ဥပပီဠကကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0465.mp3">
										၄၆၅။ ဝဇီဝိညတ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0268.mp3">
										၂၆၈။ – ။ – အပၸနာေဇာဝါရ (ဘိ)သရုပ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0367.mp3">
										၃၆၇။ – ဇနကကံႏွင့္ ဥပဃာတက…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0466.mp3">
										၄၆၆။ လဟုတာဒိ႐ုပ္ ၃-ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0269.mp3">
										၂၆၉။ – ။ – အပၸနာေဇာဝါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0368.mp3">
										၃၆၈။ – ပါကဒါနပရိယာယစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0467.mp3">
										၄၆၇။ ။ ကြဲပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0270.mp3">
										၂၇၀။ – ။ – အပၸနာေဇာဝါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0369.mp3">
										၃၆၉။ – ပါကကာလစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0468.mp3">
										၄၆၈။ လကၡဏ႐ုပ္ ၄-ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0271.mp3">
										၂၇၁။ – ။ – ဝိဘူတာရံုသာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0370.mp3">
										၃၇၀။ – ဒိ႒ဓမၼေဝဒနီယကံ..</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0469.mp3">
										၄၆၉။ ဥပစယႏွင့္သႏၲတိအထူး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0272.mp3">
										၂၇၂။ – ။ – တဒါရံုမက်ျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0371.mp3">
										၃၇၁။ – ပါကကာလကံမည္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0470.mp3">
										၄၇၀။ စတိ႐ုပ္ကိုပင္ ။ ဟုေခၚဆိုရျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0273.mp3">
										၂၇၃။ အပၸနာဝီထိက်ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0372.mp3">
										၃၇၂။ – ပါကဌာနစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0471.mp3">
										၄၇၁။ ႐ုပ္ ၁၁ ပါးအျပား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0274.mp3">
										၂၇၄။ ပ ဥ ႏု ေဂါ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0373.mp3">
										၃၇၃။ – ကမၼဒြါရ(၃)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0472.mp3">
										၄၇၂။ ရူပဝိဘာဂ – ဧကဝိဓနည္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0275.mp3">
										၂၇၅။ အပၸနာေဇာတို႔ (၄-၅)ႀကိမ္၌သာ 
										ျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0374.mp3">
										၃၇၄။ အကုသိုလ္ကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0473.mp3">
										၄၇၃။ ဒိြဝိဓနည္း – အဇၩတၱိကရုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0276.mp3">
										၂၇၆။ အပၸနာေဇာတို႔ (၄-၅)ႀကိမ္၌သာ 
										ျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0375.mp3">
										၃၇၅။ – အဒိႏၷာဒါန</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0474.mp3">
										၄၇၄။ ေဂါစရဂၢါဟကရုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0277.mp3">
										၂၇၇။ အပၸနာေဇာတို႔ ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0376.mp3">
										၃၇၆။ – ကာေမသုမိစၧာစာရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0475.mp3">
										၄၇၅။ ဣၿႏၵိယရုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0278.mp3">
										၂၇၈။ အပၸနာေဇာတို႔ က်ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0377.mp3">
										၃၇၇။ – ကာယဝိညတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0476.mp3">
										၄၇၆။ – ဒြါရရုပ္…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0279.mp3">
										၂၇၉။ ဝိပါကနိယာမ (ဘိ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0378.mp3">
										၃၇၈။ – “ဗာဟုလႅ”သဒၵါထည့္ဆိုရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0477.mp3">
										၄၇၇။ – ၾသဠာရိကရုပ္…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0280.mp3">
										၂၈၀။ ဝိပါကနိယာမ (ဘိ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0379.mp3">
										၃၇၉။ – “ဗာဟုလႅ”သဒၵါထည့္ဆိုရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0478.mp3">
										၄၇၈။ – သပၸဋိဃရုပ္…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0281.mp3">
										၂၈၁။ ဝိပါက္အမွန္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0380.mp3">
										၃၈၀။ – ကာယကံသည္…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0479.mp3">
										၄၇၉။ – အဝိနိေဗာၻဂရုပ္…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0282.mp3">
										၂၈၂။ ေဇာအျပန္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0381.mp3">
										၃၈၁။ – အကုသိုလ္ဝစီကံ (၄)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0480.mp3">
										၄၈၀။ ရူပသမုဌာန – ရုပ္ျဖစ္ေၾကာင္းတရား(ဘိ)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0283.mp3">
										၂၈၃။ ေဇာအမွန္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0382.mp3">
										၃၈၂။ – ဝစီကံ (၄)ပါး အဆံုးအျဖတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0481.mp3">
										၄၈၁။ – ံကရုပ္ကိုျဖစ္ေစပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0284.mp3">
										၂၈၄။ ပုဂၢိဳလ္အလိုက္ တဒါရံုျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0383.mp3">
										၃၈၃။ – အကုသိုလ္မေနာကံ (၃)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0482.mp3">
										၄၈၂။ စိတ္ကရုပ္ကိုျဖစ္ေစပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0285.mp3">
										၂၈၅။ ေဇာေနာင္တဒါရံုက်ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0384.mp3">
										၃၈၄။ – ေဒါသမူလေၾကာင့္ျဖစ္ေသာကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0483.mp3">
										၄၈၃။ – ဣရိယာပုတ္ကိုျဖစ္ေစႏိုင္…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0286.mp3">
										၂၈၆။ ႀကိယာေဇာေနာင္တဒါရံုက်သင့္ မက်သင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0385.mp3">
										၃၈၅။ – ေလာဘမူလေၾကာင့္ျဖစ္ေသာကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0484.mp3">
										၄၈၄။ – ရယ္ရႊင္ျခင္းကို ..။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0287.mp3">
										၂၈၇။ ကု၊ အကု၊ ႀကိ . . . 
										တဒါရံုကိုမွတ္ျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0386.mp3">
										၃၈၆။ – ေလာဘ၊ ေဒါသေၾကာင့္ျဖစ္ေသာကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0485.mp3">
										၄၈၅။ – ဥတုက ရုပ္ကိုျဖစ္ေစပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0288.mp3">
										၂၈၈။ ဥာသံေဇာေနာင္ . . . တဒါရံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0387.mp3">
										၃၈၇။ – ကာမာဝစရ ကုသိုလ္ကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0486.mp3">
										၄၈၆။ – ေတေဇာဒာတုဌိတိပၸတၱာဝ…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0289.mp3">
										၂၈၉။ အာဂႏၲဳကဝီထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0388.mp3">
										၃၈၈။ ပုညႀတိဝတၳဳ (၁၀)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0487.mp3">
										၄၈၇။ – အာဟာရကရုပ္ကိုျဖစ္ေစပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0290.mp3">
										၂၉၀။ အာဂႏၲဳကဝီထိ ဘဝင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0389.mp3">
										၃၈၉။ – သီလ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0488.mp3">
										၄၈၈။ – ဧကဇ ၊ ဒိြဇ…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0291.mp3">
										၂၉၁။ အာဂႏၲဳကဝီထိ ဘဝင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0390.mp3">
										၃၉၀။ – ဘာဝနာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0489.mp3">
										၄၈၉။ – စတုဝိမုတ္ရုပ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0292.mp3">
										၂၉၂။ တဒါရံုျဖစ္ေၾကာင္းအဂၤါ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0391.mp3">
										၃၉၁။ – အပစာယန</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0490.mp3">
										၄၉၀။ ရူပကာလာပ – (အဘိဓမၼာ)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0293.mp3">
										၂၉၃။ ကာမေဇာ၏ အဆံုး၌သာ တဒါရံု ျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0392.mp3">
										၃၉၂။ – ပတၱိဒါန</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0491.mp3">
										၄၉၁။ ရူပကာလာပ – (အဘိဓမၼာ)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0294.mp3">
										၂၉၄။ ကာမေဇာ၏ အဆံုး၌သာ တဒါရံု ျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0393.mp3">
										၃၉၃။ – ဓတမၼႆဝန</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0492.mp3">
										၄၉၂။ ရူပကာလာပ – (အဘိဓမၼာ)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0295.mp3">
										၂၉၅။ ကာမေဇာ၏ အဆံုး၌သာ တဒါရံု ျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0394.mp3">
										၃၉၄။ – ဒိ႒ိဇုကမၼ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0493.mp3">
										၄၉၃။ ရူပ ပဝတၱိကၠမ – ကာမဘံု၌ရုပ္ျဖစ္စဥ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0296.mp3">
										၂၉၆။ ကာမအာရံု၌သာ တဒါရံုျဖစ္ရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0395.mp3">
										၃၉၅။ ပုည(၁၀)ပါးကို ဒါနသီလဘာဝနာ၌သြင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0494.mp3">
										၄၉၄။ – ကလလေရၾကည္ရုပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0297.mp3">
										၂၉၇။ ဇဝနနိယာမ၊ မရဏာသႏၷေဇာျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0396.mp3">
										၃၉၆။ – ဓမၼေဒသနာသည္ ဒါနမယျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0495.mp3">
										၄၉၅။ – ဂဗၻေသယ်ကုရုပ္ျဖစ္စဥ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0298.mp3">
										၂၉၈။ ။ ယမိုက္ျပာဋိဟာျပေသာအခါေဇာျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0397.mp3">
										၃၉၇။ ရူပါဝစရကုသိုလ္ကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0496.mp3">
										၄၉၆။ – ရုပ္(၄)ပါးတို႔ ေရွးဦးစြာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0299.mp3">
										၂၉၉။ မဟဂၢဳတ္ေဇာတို႔ေစာပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0398.mp3">
										၃၉၈။ အကုသိုလ္ကံ၏ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0497.mp3">
										၄၉၇။ – (အဘိ)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0300.mp3">
										၃၀၀။ မဂ္ေဇာ (၁)ႀကိမ္သာ ေစာရပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0399.mp3">
										၃၉၉။ အကုသိုလ္ကံ၏ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0498.mp3">
										၄၉၈။ – ပဋိသေႏၶစိတ္၏ ဌီကာလမွ –</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0301.mp3">
										၃၀၁။ နိေရာဓသမာပတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0400.mp3">
										၄၀၀။ အကုသိုလ္ကံ၏ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0499.mp3">
										၄၉၉။ – အာဟာရဇရုပ္ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0302.mp3">
										၃၀၂။ သမာပတၱိဝီထိ…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0401.mp3">
										၄၀၁။ အကုသိုလ္ပယ္စဥ္(၃)မ်ိဳး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0500.mp3">
										၅၀၀။ – ရုပ္ (၄)ပါးတို႔ ေနာက္ဆံုးခ်ဳပ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0303.mp3">
										၃၀၃။ ပုဂၢလေဘဒ၊ ဟိတ္ပုဂၢိဳလ္စသည္..</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0402.mp3">
										၄၀၂။ ပ႒ာန္းလာ သာဓက</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0501.mp3">
										၅၀၁။ – ေသျခင္းသတ္မွတ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0304.mp3">
										၃၀၄။ အဟိတ္ဝ ဒိြဟိတ္ မရႏိုင္ေသာေဇာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0403.mp3">
										၄၀၃။ ကာမကုသိုလ္အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0502.mp3">
										၅၀၂။ – ရံူပဘံု၌ ရုပ္ျဖစ္စဥ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0305.mp3">
										၃၀၅။ဝိပါကာဝရဏ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0404.mp3">
										၄၀၄။ တိဟိတ္ကုသိုလ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0504.mp3">
										၅၀၃။ – ဘံုအားျဖင့္ ရေသာရုပ္မ်ား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0306.mp3">
										၃၀၆။ သုဂတိအဟိတ္၊ ဒိြဟိတ္မရႏိုင္ေသာ 
										ဝိပါက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0405.mp3">
										၄၀၅။ ေစတနာ၏ ပဋိ၊ ပဝတၱိ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0504.mp3">
										၅၀၄။ – ေကစိဆရာတို႔အလို…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0307.mp3">
										၃၀၇။ သုဂတိအဟိတ္၊ ဒိြဟိတ္မရႏိုင္ေသာ 
										ဝိပါက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0406.mp3">
										၄၀၆။ ကံအက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0505.mp3">
										၅၀၅။ နိဗၺာန္အေၾကာင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0308.mp3">
										၃၀၈။ ေသကၡ၊ အေသကၡ ပုဂၢိဳလ္တို႔ မရေသာေဇာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0407.mp3">
										၄၀၇။ သမာနဝါဒ၊ ေကစိဝါဒ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0506.mp3">
										၅၀၆။ နိဗၺာန္အေၾကာင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0309.mp3">
										၃၀၉။ အရိယာမ်ားသာ ျဖစ္ေသာေဇာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0408.mp3">
										၄၀၈။ ရူပကုသိုလ္ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0507.mp3">
										၅၀၇။ – “အဘဝပညတ္”မွ်သည္-</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0310.mp3">
										၃၁၀။ ဋီကာရွင္းတမ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0409.mp3">
										၄၀၉။ ရူပကုသိုလ္ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0508.mp3">
										၅၀၈။ နိဗၺာန္အျပား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0311.mp3">
										၃၁၁။ ဋီကာရွင္းတမ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0410.mp3">
										၄၁၀။ အသညသတ္ဘံုသို႔ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0509.mp3">
										၅၀၉။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0312.mp3">
										၃၁၂။ ။ ပုဂၢလေဘဒဆိုင္ရာ ေမးေျဖမ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0411.mp3">
										၄၁၁။ သုဒၶဝါသ (၅)ဘံုသို႔ အက်ိဳးေပးပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0510.mp3">
										၅၁၀။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0313.mp3">
										၃၁၃။ ။ ပုဂၢလေဘဒဆိုင္ရာ ေမးေျဖမ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0412.mp3">
										၄၁၂။ အနာဂါမ္မွန္သမွ် ဗဟၼာျပည္အၿမဲေရာက္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0511.mp3">
										၅၁၁။ – ဥပါဒိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0314.mp3">
										၃၁၄။ ။ ပုဂၢလေဘဒဆိုင္ရာ ေမးေျဖမ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0413.mp3">
										၄၁၃။ –။ ကာမဘံု၌ ျပန္မျဖစ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0512.mp3">
										၅၁၂။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0315.mp3">
										၃၁၅။ ဘူမိဝိဘာဂ – ကာမာဝစရဘံု၌စိတ္ရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0414.mp3">
										၄၁၄။ မရဏုပၸတၱိစတုကၠ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0513.mp3">
										၅၁၃။ နိဗၺာန္၏ ဂုဏ္ရည္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0316.mp3">
										၃၁၆။ ။ ရူပါဝစရဘံု၌စိတ္ရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0415.mp3">
										၄၁၅။ –။ -ကံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0514.mp3">
										၅၁၄။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0317.mp3">
										၃၁၇။ ။ အရူပါဝစရဘံု၌စိတ္ရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0416.mp3">
										၄၁၆။ -။- ကမၼနိမိတ္၊ ဂတိနိမိတ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0515.mp3">
										၅၁၅။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0318.mp3">
										၃၁၈။ အသညသတ္ဘံု၌ စိတ္မျဖစ္ျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0417.mp3">
										၄၁၇။ -။- နိမိတ္မထင္ေသာ ပုဂၢိဳလ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0516.mp3">
										၅၁၆။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0319.mp3">
										၃၁၉။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္းအစ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0418.mp3">
										၄၁၈။ -။- စုေတခါနီး စိတ္အစဥ္ျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0516.mp3">
										၅၁၇။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0320.mp3">
										၃၂၀။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္းအစ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0419.mp3">
										၄၁၉။ မရဏာသႏၷဝီထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0518.mp3">
										၅၁၈။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0321.mp3">
										၃၂၁။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္းအစ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0420.mp3">
										၄၂၀။ မရဏာသႏၷဝီထိ၏ အာရံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0519.mp3">
										၅၁၉။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0322.mp3">
										၃၂၂။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္းအစ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0421.mp3">
										၄၂၁။ မရဏာသႏၷဝီထိ၏ အာရံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0520.mp3">
										၅၂၀။ ။ (ရွင္းတမ္း)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0323.mp3">
										၃၂၃။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္းအစ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0422.mp3">
										၄၂၂။ မွတ္ခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0521.mp3">
										၅၂၁။ ေမးေျဖ -၁၉၇၈ – ၁၉၈၈</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0324.mp3">
										၃၂၄။ ဋီကာရွင္းတမ္း – ဝီထိပိုင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0423.mp3">
										၄၂၃။ – ။</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0522.mp3">
										၅၂၂။ ၁၉၈၈ – ၂၀၀၆</a></td>
									</tr>
								</tbody>							                                
"""

#soup = bs4(one, 'html.parser')
#soup = bs4(two, 'html.parser')
soup = bs4(one, 'html.parser')


with open('titles_links.txt', 'w') as f:

    count = 224
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
