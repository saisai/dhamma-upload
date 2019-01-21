from bs4 import BeautifulSoup as bs4
import re
one = """

									<colgroup>
										<col style="width: 193pt" width="257">
										<col style="width: 218pt" width="290">
										<col style="width: 217pt" width="289">
									</colgroup>
									<tbody><tr style="height: 22.5pt" height="30">
										<td style="height: 22.5pt; width: 193pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="257" height="30">
										သမုစၥည္းပိုင္း</td>
										<td style="width: 218pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="290">
										ပစၥည္းပိုင္း</td>
										<td style="width: 217pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="289">
										ကမဌာန္းပိုင္း</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">
										&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										အဆက္…</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0653.mp3">
										၆၅၃။ အဘိဓမၼာ ျပန္႐ွင္းျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0523.mp3">
										၅၂၃။ အာသဝ (၄)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0584.mp3">
										၅၈၄။ အဝိဇၨာ သခၤါရတို႔ကိုယူသျဖင့္..</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0654.mp3">
										၆၅၄။ မာတိကာ ႐ွင္လင္းခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0524.mp3">
										၅၂၄။ မာန စသည္- အာသဝမမည္ျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0585.mp3">
										၅၈၅။ အေၾကာင္းအျခင္းအရာ -၂၀</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0655.mp3">
										၆၅၅။ ကမၼ႒ာန္းပိုင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0525.mp3">
										၅၂၅။ ဥပါဒါန္–</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0586.mp3">
										၅၈၆။ အတိတ္အေၾကာင္း-၅ပါးျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0656.mp3">
										၆၅၆။ ကမၼ႒ာန္းပိုင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0526.mp3">
										၅၂၆။ ဥဒၶစၥ ကုကၠစၥ တူညီပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0587.mp3">
										၅၈၇။ အာကာရမည္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0657.mp3">
										၆၅၇။ သမထကမၼ႒ာန္းပိုင္း-ကသိုဏ္း ၁၀ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0527.mp3">
										၅၂၇။ ပဋိဃသံေယာဇဥ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0588.mp3">
										၅၈၈။ သခၤါရႏွင့္ ကမၼဘဝအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0658.mp3">
										၆၅၈။ အသုဘ ၁၀ပါး၊ အႏုႆ တိ ၁၀ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0528.mp3">
										၅၂၈။ အႏုသယ၊ သံေယာဇဥ္၊ ကိေလသာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0589.mp3">
										၅၈၉။ သခၤါရႏွင့္ ကမၼဘဝအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0659.mp3">
										၆၅၉။ မရဏာႏုႆ တိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0529.mp3">
										၅၂၉။ မိႆ ကသဂၤဟ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0590.mp3">
										၅၉၀။ အစပ္ -(၃)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0660.mp3">
										၆၆၀။ ကာယဂတာဂတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0530.mp3">
										၅၃၀။ မိႆ ကသဂၤဟ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0591.mp3">
										၅၉၁။ အစပ္ -(၃)ပါးအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0661.mp3">
										၆၆၁။ အပၸမညာ ၄ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0531.mp3">
										၅၃၁။ ဣေျႏၵတို႔အစိုးရပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0592.mp3">
										၅၉၂။ သေခၤပ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0662.mp3">
										၆၆၂။ အပၸမညာ ေမတၱာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0532.mp3">
										၅၃၂။ ဣေျႏၵတို႔အစိုးရပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0593.mp3">
										၅၉၃။ ဝဋ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0663.mp3">
										၆၆၃။ အာဟာေရပဋိကူလသညာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0533.mp3">
										၅၃၃။ ဣေျႏၵ ၂၂-ပါးေဟာစဥ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0594.mp3">
										၅၉၄။ ကမၼဘဝႏွင့္ သခၤါရအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0664.mp3">
										၆၆၄။ အာရံုကမၼ႒ာန္းႏွင့္ အာရမၼဏိကကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0534.mp3">
										၅၃၄။ ဣေျႏၵ ၂၂-ပါးေဟာစဥ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0595.mp3">
										၅၉၅။ ဘဝတစ္စိတ္(ဘေဝကေဒေသာ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0665.mp3">
										၆၆၅။ စ႐ိုက္ ၆-ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0535.mp3">
										၅၃၅။ ဗိုလ္၊ အဓိပတိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0596.mp3">
										၅၉၆။ ဝဋ္ျမစ္ (၂)ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0666.mp3">
										၆၆၆။ သပၸါယေဘဒ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0536.mp3">
										၅၃၆။ အာဟာရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0597.mp3">
										၅၉၇။ အဝိဇၨာမူလကို အရင္ဆိုရျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0667.mp3">
										၆၆၇။ ဘာဝနာေဘဒ-ပရိကမၼဘာဝနာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0537.mp3">
										၅၃၇။ ေဗာဓိပကၡိယသဂၤဟ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0598.mp3">
										၅၉၈။ ဝဋ္ျပတ္ပံု ဝဋ္လည္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0668.mp3">
										၆၆၈။ — ဥပစာရဘာဝနာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0538.mp3">
										၅၃၈။ ေဗာဓိပကၡိယသဂၤဟ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0599.mp3">
										၅၉၉။ အာသဝါနံ သမုပၸါဒါ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0669.mp3">
										၆၆၉။ — အပၸနာဘာဝနာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0539.mp3">
										၅၃၉။ မဂၢင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0600.mp3">
										၆၀၀။ ပ႒ာန္းနည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0670.mp3">
										၆၇၀။ ဘာဝနာ ၃ပါးလံုးရေသာ ကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0540.mp3">
										၅၄၀။ သဗၺသဂၤဟ-ခႏၶာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0601.mp3">
										၆၀၁။ ေဟတုပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0671.mp3">
										၆၇၁။ ဒုတိယာ႐ုပၸႏွင့္ အပၸနာရႏိုင္ျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0541.mp3">
										၅၄၁။ သဗၺသဂၤဟ-ခႏၶာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0602.mp3">
										၆၀၂။ ဟိတ္ႏွင့္ ပစၥည္းအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0672.mp3">
										၆၇၂။ စ်ာန္ျဖင့္ ကမၼ႒ာန္းကို ေဝဖန္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0542.mp3">
										၅၄၂။ ဥပါဒါနကၡႏၶာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0603.mp3">
										၆၀၃။ အာရမၼဏပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0673.mp3">
										၆၇၃။ အပၸနာစ်ာန္ရႏိုင္ေသာ ကမၼ႒ာန္း (၃၀)</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0543.mp3">
										၅၄၃။ အာယတန ၁၂-ပါး စဥ္ထားပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0604.mp3">
										၆၀၄။ အဓိပတိပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0674.mp3">
										၆၇၄။ နိမိတၱေဘဒ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0544.mp3">
										၅၄၄။ အာယတန ၁၂-ပါး စဥ္ထားပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0605.mp3">
										၆၀၅။ အနႏၱရ၊ သမနႏၱရပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0675.mp3">
										၆၇၅။ ပရိကမၼနမတိ၊ဥဂၢတနမတိရႏိုင္ေသာ…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0545.mp3">
										၅၄၅။ အာယတန ၁၂-ပါး စဥ္ထားပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0606.mp3">
										၆၀၆။ ေကစီဝါဒ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0676.mp3">
										၆၇၆။ ဘာဝနာႏွင့္နမိတ္ တြဲစပ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0546.mp3">
										၅၄၆။ အာယတန ၁၂-ပါး စဥ္ထားပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0607.mp3">
										၆၀၇။ သဟဇာတ အညမညပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0677.mp3">
										၆၇၇။ ဘာဝနာႏွင့္နမိတ္ တြဲစပ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0547.mp3">
										၅၄၇။ အရိယသစၥာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0608.mp3">
										၆၀၈။ သဟဇာတ အညမညပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0678.mp3">
										၆၇၈။ ဗုဒၶႏုႆ သတိပြားမ်ားပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0548.mp3">
										၅၄၈။ အရိယသစၥာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0609.mp3">
										၆၀၉။ နိႆ ယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0679.mp3">
										၆၇၉။ ဝသီေဘာ(၅) ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0549.mp3">
										၅၄၉။ အရိယသစၥာ+သတၱဝါႏွင့္ ေဒသနာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0610.mp3">
										၆၁၀။ ဥပနိႆ ယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0680.mp3">
										၆၈၀။ အာ႐ူပစ်ာန္ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0550.mp3">
										၅၅၀။ အရိယသစၥာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0611.mp3">
										၆၁၁။ ပုေရဇာတ၊ ပစၦာဇာတပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0681.mp3">
										၆၈၁။ အာ႐ူပစ်ာန္ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0551.mp3">
										၅၅၁။ အေမးအေျဖ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0612.mp3">
										၆၁၂။ အာေသဝနပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0682.mp3">
										၆၈၂။ အဘိညာဏ္ခန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0552.mp3">
										၅၅၂။ အေမးအေျဖ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0613.mp3">
										၆၁၃။ ကမၼပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0683.mp3">
										၆၈၃။ အဘိညာဏ္အစြမ္းျဖင့္ ျဖစ္ေသာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0553.mp3">
										၅၅၃။ အေမးအေျဖ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0614.mp3">
										၆၁၄။ ဝိပါကပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0684.mp3">
										၆၈၄။ အဘိညာဏ္ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">
										&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0615.mp3">
										၆၁၅။ အာဟာရပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0685.mp3">
										၆၈၅။ ေလာကီအဘိဉာဏ္(၇) ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">
										&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0616.mp3">
										၆၁၆။ အာဟာရပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0686.mp3">
										၆၈၆။ ဒိဗၺစကၡဳ ကို စုတူပပါတဉာဏ္ဟု 
										ဆိုရျခင္း</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" height="29">
										ပစၥည္းပိုင္း</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0617.mp3">
										၆၁၇။ ဣၿႏိၵယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0687.mp3">
										၆၈၇။ အဘိဉာဏ္မဝင္စားမီ ပရိကံျပဳပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">
										&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0618.mp3">
										၆၁၈။ စ်ာနပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0688.mp3">
										၆၈၈။ အဘိဉာဏ္တို႔၏ အာရံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0554.mp3">
										၅၅၄။ ပစၥည္းပိုင္းမည္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0619.mp3">
										၆၁၉။ မဂၢပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0689.mp3">
										၆၈၉။ အဘိဉာဏ္တို႔၏ အာရံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0555.mp3">
										၅၅၅။ ပစၥည္းတရား-ပစၥယုပၸန္တရား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0620.mp3">
										၆၂၀။ မဂၢပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0690.mp3">
										၆၉၀။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0556.mp3">
										၅၅၆။ နည္း ၂ပါး အဖြင့္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0621.mp3">
										၆၂၁။ သမၸယုတၱပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0691.mp3">
										၆၉၁။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0557.mp3">
										၅၅၇။ နည္း ၂ပါး အဖြင့္ အထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0622.mp3">
										၆၂၂။ ဝိပၸယုတၱပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0692.mp3">
										၆၉၂။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0558.mp3">
										၅၅၈။ ပဋိစၥသမုပၸာဒ္ အႏုေလာမ ပါ႒ိေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0623.mp3">
										၆၂၃။ အတၳိပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0693.mp3">
										၆၉၃။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0559.mp3">
										၅၅၉။ အဝိဇၨာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0624.mp3">
										၆၂၄။ အဝိဂတပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0694.mp3">
										၆၉၄။ ဝိပၸႆ နာဘာဝနာ ကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0560.mp3">
										၅၆၀။ အဝိဇၨာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0625.mp3">
										၆၂၅။ အတၳိ၊ အဝိဂတ အထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0695.mp3">
										၆၉၅။ ဝိပၸႆ နာဉာဏ္ (၁၀)ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0561.mp3">
										၅၆၁။ သခၤါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0626.mp3">
										၆၂၆။ နတၳိပစၥည္း၊ ဝိဂတပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0696.mp3">
										၆၉၆။ ဥဒယဗၺယဉာဏ္ျဖင့္ သံုးသပ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0562.mp3">
										၅၆၂။ အက်ိဳးသခၤါရ ႏွင့္ အေၾကာင္းသခၤါရ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0627.mp3">
										၆၂၇။ ပ႒ာန္းနည္းအဖြင့္ အက်ယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0697.mp3">
										၆၉၇။ ဝိသုဒၶိေဘဒ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0563.mp3">
										၅၆၃။ ဝိဥာဏ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0628.mp3">
										၆၂၈။ ပ႒ာန္းနည္းအဖြင့္ အက်ယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0698.mp3">
										၆၉၈။ (၁)သီလဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0564.mp3">
										၅၆၄။ ဝိဥာဏ္ အဘိဓမၼာျပန္႐ွင္းျပ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0629.mp3">
										၆၂၉။ ပ႒ာန္းနည္းအဖြင့္ အက်ယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0699.mp3">
										၆၉၉။ (၁)သီလဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0565.mp3">
										၅၆၅။ ဝိဥာဏ္ အဘိဓမၼာျပန္႐ွင္းျပ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0630.mp3">
										၆၃၀။ နာမ္သည္နာမ္အား-၆ပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0700.mp3">
										၇၀၀။ (၂)စိတၱာဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0566.mp3">
										၅၆၆။ ဝိဥာဏ္ အဘိဓမၼာျပန္႐ွင္းျပ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0631.mp3">
										၆၃၁။ အာေသဝနပစၥည္ဆိုင္ရာ သိဖြယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0701.mp3">
										၇၀၁။ (၃)ဒိ႒ိဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0567.mp3">
										၅၆၇။ နာမ္႐ုပ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0632.mp3">
										၆၃၂။ အာေသဝနပစၥည္ဆိုင္ရာ သိဖြယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0702.mp3">
										၇၀၂။ (၄)ကခၤါဝိတရဏဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0568.mp3">
										၅၆၈။ နာမ္႐ုပ္-၂မ်ိဳး အထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0633.mp3">
										၆၃၃။ အာေသဝနပစၥည္ဆိုင္ရာ သိဖြယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0703.mp3">
										၇၀၃။ (၅)မဂၢါ ဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0569.mp3">
										၅၆၉။ သဠာယတန</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0634.mp3">
										၆၃၄။ သမၸယုတၱပစၥည္းဆိုင္ရာ သိဖြယ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0704.mp3">
										၇၀၄။ (၅)မဂၢါ ဥပကိၠေလသာ ၁၀-ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0570.mp3">
										၅၇၀။ ဖႆ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0635.mp3">
										၆၃၅။ နာမ္သည္နာမ္႐ုပ္အား- ၅ပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0705.mp3">
										၇၀၅။ (၆)ပဋိပဒါ ဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0571.mp3">
										၅၇၁။ ေဝဒနာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0636.mp3">
										၆၃၆။ ကမၼပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0706.mp3">
										၇၀၆။ (၇)ဥာဏဒႆ န ဝိသုဒၶိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0572.mp3">
										၅၇၂။ မွတ္ရန္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0637.mp3">
										၆၃၇။ ဝိပါကပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0707.mp3">
										၇၀၇။ စူဠေသာတာပန္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0573.mp3">
										၅၇၃။ တဏွာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0638.mp3">
										၆၃၈။ ဝိပါကပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0708.mp3">
										၇၀၈။ ဝိပၸႆ နာ၏ေဘးရန္ အစစ္ႏွင့္ အတု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0574.mp3">
										၅၇၄။ ဥပါဒါန္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0639.mp3">
										၆၃၉။ နာမ္သည္႐ုပ္အား-၁ပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0709.mp3">
										၇၀၉။ ေဂါၾတဘုစိတ္ျဖစ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0575.mp3">
										၅၇၅။ ဘဝ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0640.mp3">
										၆၄၀။ ႐ုပ္သည္နာမ္အား-ပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0710.mp3">
										၇၁၀။ ဝိေမာကၡေဘဒ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0576.mp3">
										၅၇၆။ ဘဝ-၂မ်ိဳးအထူး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0641.mp3">
										၆၄၁။ ပညတ္၊ နာမ္၊ ရုပ္သည္ နာမ္အား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0711.mp3">
										၇၁၁။ ဝိေမာကၡမုခ ၃-ပါး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0577.mp3">
										၅၇၇။ ဇာတိ၊ ဇရာ စသည္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0642.mp3">
										၆၄၂။ ဥပနိႆ ယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0712.mp3">
										၇၁၂။ မဂ္ (၄) ပါးတို႔ အကုသိုလ္ပယ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0578.mp3">
										၅၇၈။ အဝိဇၨာစသည္တို႔ အေၾကာင္းအျဖစ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0643.mp3">
										၆၄၃။ အနႏၱ႐ူပနိႆ ယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0713.mp3">
										၇၁၃။ ဝိေမာကၡ အမည္ရပံုမ်ား ၁။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0579.mp3">
										၅၇၉။ တဏွာ၏ အေၾကာင္းပစၥည္းျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0644.mp3">
										၆၄၄။ ပကတူပနိႆ ယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0714.mp3">
										၇၁၄။ ဝိေမာကၡ အမည္ရပံုမ်ား ၂။ ၃။</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0580.mp3">
										၅၈၀။ ဥပါဒါန္၏ အေၾကာင္းပစၥည္းျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0645.mp3">
										၆၄၅။ နာမ္႐ုပ္သည္ နာမ္႐ုပ္အား- ၉ပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0715.mp3">
										၇၁၅။ ပုဂၢလေဘဒ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0581.mp3">
										၅၈၁။ ဧဝေမတႆ ။ပ။ သမုဒေယာေဟာတိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0646.mp3">
										၆၄၆။ နာမ္႐ုပ္သည္ နာမ္႐ုပ္အား အာဟာရပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0716.mp3">
										၇၁၆။ သမၼာပတၱိေဘဒ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0582.mp3">
										၅၈၂။ အဓြန္႔ (၃) ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0647.mp3">
										၆၄၇။ ဣျႏၵိယပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0717.mp3">
										၇၁၇။ ေမး/ေျဖမ်ား</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0583.mp3">
										၅၈၃။ ေသာကစေသာ စကားရပ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0648.mp3">
										၆၄၈။ ဝိပၸယုတၱပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0718.mp3">
										၇၁၈။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0649.mp3">
										၆၄၉။ ဝိပၸယုတၱပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0719.mp3">
										၇၁၉။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0650.mp3">
										၆၅၀။ အတၳိႏွင့္ အဝိဂတပစၥည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0720.mp3">
										၇၂၀။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0651.mp3">
										၆၅၁။ နိဗၺာန္မွာ အတၳိႏွင့္ အဝိဂတမရိွပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0721.mp3">
										၇၂၁။ ဋီကာ႐ွင္းတမ္းျဖင့္ ေလ့လာခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0652.mp3">
										၆၅၂။ ၂၄-ပစၥည္း အက်ဥ္းခ်ဳပ္ၿပီး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/Tikakyaw/Dawkhinhlatin-Tikakyaw-0722.mp3">
										၇၂၂။ ေမး/ေျဖမ်ား</a></td>
									</tr>
								</tbody>					                                
"""

#soup = bs4(one, 'html.parser')
#soup = bs4(two, 'html.parser')
soup = bs4(one, 'html.parser')


with open('titles_links.txt', 'w') as f:

    count = 523
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
