from bs4 import BeautifulSoup as bs4
import re
one = """

									<colgroup>
										<col style="width: 194pt" width="258">
										<col style="width: 185pt" width="246">
										<col style="width: 183pt" width="244">
									</colgroup>
									<tbody><tr style="height: 23.25pt" height="31">
										<td style="height: 23.25pt; width: 194pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="258" height="31">
										<font size="2">သီလနိေဒၵသ</font></td>
										<td style="width: 185pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="246">
										<font size="2">ဓုတဂၤနိေဒၵ</font></td>
										<td style="width: 183pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="244">
										<font size="2">ပထဝီကသိဏနီေဒၵ</font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0001.mp3">၁။ 
										မိတ္ဆက္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0115.mp3">၁၁၅။ ဓုတဂၤနိေဒၵသ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0213.mp3">၂၁၃။ ပထဝီကသိဏနီေဒၵသ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0002.mp3">၂။&nbsp; မာတိကာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0116.mp3">၁၁၆။ အရိယဝံသတရား (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0214.mp3">၂၁၄။ မသင္႔ေလ်ာ္ေသာေက်ာင္း 
										(၁၈)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0003.mp3">၃။ နိဒါန္းသည္ ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0117.mp3">၁၁၇။ ဓုတင္ (၁၃) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0215.mp3">၂၁၅။ သင္႔ေလ်ာ္ေသာေက်ာင္း</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0004.mp3">၄။ – အေျဖ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0118.mp3">၁၁၈။ မာတိကာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0216.mp3">၂၁၆။ ပလိေဗာဓငယ္မ်ား</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0005.mp3">၅။ – က်မ္းျပဳဆရာ, 
										ဝိသုဒိၶမဂ္ပုဒ္အဖြင္႔</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0119.mp3">၁၁၉။ ဓုတင္မည္ပံု (၃) 
										မ်ိဳး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0217.mp3">၂၁၇။ 
										ဘာဝနာပြားျခင္းအစီအရင္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0006.mp3">၆။ ဝိသုဒၶိမဂ္မည္ေသာ 
										ေဒသနာအမ်ိဳးမ်ိဳး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0120.mp3">၁၂၀။ ဓုတင္ (၁၃) ပါး၏ အနက္ 
										(၁)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0218.mp3">၂၁၈။ ဘာဝနာ – 
										ကသိုဏ္းဝန္းကိုၾကည္႔နည္း…</a>.</font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0007.mp3">၇။ အေမးဂါထာ၏ 
										အက်ဥ္းခ်ဳပ္အဖြင္႔</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0121.mp3">၁၂၁။ ဓုတင္ (၂) ပါး၏ အနက္ 
										(၆)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0219.mp3">၂၁၉။ ဘာဝနာ – 
										ကသိုဏ္းဝန္းကိုၾကည္႔နည္း…</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0008.mp3">၈။ အေျဖဂါထာ၏ 
										အက်ဥ္းခ်ဳပ္အဖြင္႔</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0122.mp3">၁၂၂။ ဓုတင္ (၇) ပါး၏ အနက္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0220.mp3">၂၂၀။ 
										ပဋိဘာဂနိမိတ္ျဖစ္ေအာင္အားထုတ္ပံု</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0009.mp3">၉။ အေျဖဂါထာ၏ 
										အက်ဥ္းခ်ဳပ္အဖြင္႔</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0123.mp3">၁၂၃။ ဓုတင္ (၈) ပါး၏ အနက္ 
										(၁၃)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0221.mp3">၂၂၁။ 
										နိမိတ္ႏွစ္ပါးထူးျခားခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0010.mp3">၁၀။ သီလျဖင္႔ျပအပ္ေသာဂုဏ္ 
										(၉) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0124.mp3">၁၂၄။ ဓုတင္၏ လကၡဏ စသည္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0222.mp3">၂၂၂။ သမာဓိႏွစ္မ်ိဳး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0011.mp3">၁၁။ သီလျဖင္႔ျပအပ္ေသာဂုဏ္ 
										(၉) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0125.mp3">၁၂၅။ ဓုတင္ 
										ေဆာက္တည္ပံုႏွင္႔ က်င္႔ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0223.mp3">၂၂၃။ အလြန္ခက္ခဲေသာအရာ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0012.mp3">၁၂။ သီလျဖင္႔ျပအပ္ေသာဂုဏ္ 
										(၉) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0126.mp3">၁၂၆။ ေမးခြန္းနံပါတ္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0224.mp3">၂၂၄။ 
										ပဋိဘာဂနိမိတ္ကိုေစာင္႔ေရွာက္ပံု</a></font></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="29" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0013.mp3">၁၃။ သီလျဖင္႔ျပအပ္ေသာဂုဏ္ 
										(၉) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0127.mp3">၁၂၇။ (၁) ပံသုကူဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0225.mp3">၂၂၅။ 
										အပၸနာ၌ကြ်မ္းက်င္ေၾကာင္း (၁၀)ပါး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0014.mp3">၁၄။ သီလျဖင္႔ျပအပ္ေသာဂုဏ္ 
										(၉) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0128.mp3">၁၂၈။ (၁) ပံသုကူဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0226.mp3">၂၂၆။ နံပါတ္ (၂)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0015.mp3">၁၅။ သီလျဖင္႔ျပအပ္ေသာဂုဏ္ 
										(၉) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0129.mp3">၁၂၉။ (၁) ပံသုကူဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0227.mp3">၂၂၇။ နံပါတ္ (၂.၁)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0016.mp3">၁၆။ သီလနိေဒၵသ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0130.mp3">၁၃၀။ (၂) တိစီဝရိက္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0228.mp3">၂၂၈။ နံပါတ္ (၂.၂)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0017.mp3">၁၇။ သီလဟူသည္၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0131.mp3">၁၃၁။ (၂) တိစီဝရိက္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0229.mp3">၂၂၉။ နံပါတ္ (၂.၃)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0018.mp3">၁၈။ သီလဟူသည္၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0132.mp3">၁၃၂။ (၃) ပါ႑ိပါတ္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0230.mp3">၂၃၀။ နံပါတ္ (၃)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0019.mp3">၁၉။ သီလဟူသည္၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0133.mp3">၁၃၃။ (၃) ပါ႑ိပါတ္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0231.mp3">၂၃၁။ နံပါတ္ (၄)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0020.mp3">၂၀။ သီလ၏ အနက္၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0134.mp3">၁၃၄။ (၄) သပဒါနစာရိက ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0232.mp3">၂၃၂။ နံပါတ္ (၄)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0021.mp3">၂၁။ သီလ၏ လကၡ စသည္၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0135.mp3">၁၃၅။ (၄) သပဒါနစာရိက ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0233.mp3">၂၃၃။ နံပါတ္ (၄)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0022.mp3">၂၂။ သီလ၏ ရသ စသည္၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0136.mp3">၁၃၆။ (၅) ဧကာသနိက္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0234.mp3">၂၃၄။ နံပါတ္ (၅)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0023.mp3">၂၃။ သီလ၏ အက်ိဳး၊</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0137.mp3">၁၃၇။ (၆) ပတၱပိုဏ္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0235.mp3">၂၃၅။ နံပါတ္ (၅)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0024.mp3">၂၄။ သီလကို 
										ခ်ီးက်ဴးေသာစကားမ်ား</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0138.mp3">၁၃၈။ (၆) ပတၱပိုဏ္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0236.mp3">၂၃၆။ နံပါတ္ (၅)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0025.mp3">၂၅။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0139.mp3">၁၃၉။ (၇) ခလုပစၦာဘတ္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0237.mp3">၂၃၇။ နံပါတ္ (၆, ၇, ၈, ၉, 
										၁၀)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0026.mp3">၂၆။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0140.mp3">၁၄၀။ (၈) အာရညကင္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0238.mp3">၂၃၈။ နိမိတ္သို႔ 
										ေရွးရႈျဖစ္ေစျခင္း</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0027.mp3">၂၇။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0141.mp3">၁၄၁။ (၈) အာရညကင္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0239.mp3">၂၃၉။ ပထမစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 23px; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0028.mp3">၂၈။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="23" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0142.mp3">၁၄၂။ (၈) အာရညကင္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="23" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0240.mp3">၂၄၀။ ပထမစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 25px; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0029.mp3">၂၉။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="25" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0143.mp3">၁၄၃။ (၈) အာရညကင္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="25" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0241.mp3">၂၄၁။ ပထမစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0030.mp3">၃၀။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0144.mp3">၁၄၄။ (၈) အာရညကင္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0242.mp3">၂၄၂။ ပထမစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0031.mp3">၃၁။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0145.mp3">၁၄၅။ (၈) အာရညကင္ ဓုတင္ 
										contd</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0243.mp3">၂၄၃။ ပထမစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0032.mp3">၃၂။ သီလအျပားကို ျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0146.mp3">၁၄၆။ (၈) အာရညကင္ ဓုတင္ 
										contd</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0244.mp3">၂၄၄။ ပထမစ်ာနကထာအဖြင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0033.mp3">၃၃။ တိကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0147.mp3">၁၄၇။ (၈) အာရညကင္ ဓုတင္ 
										contd</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0245.mp3">၂၄၅။ ပထမစ်ာနကထာအဖြင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0034.mp3">၃၄။ တိကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0148.mp3">၁၄၈။ (၉) ရုကၡမူ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0246.mp3">၂၄၆။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0035.mp3">၃၅။ တိကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0149.mp3">၁၄၉။ (၁၀) အေဗၻာကာသိက 
										ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0247.mp3">၂၄၇။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0036.mp3">၃၆။ 
										ပဋိသမၻိဒါမဂ္၌ေဟာေသာသံုးပါးအစု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0150.mp3">၁၅၀။ (၁၀) အေဗၻာကာသိက 
										ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0248.mp3">၂၄၈။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0037.mp3">၃၇။ စတုကၠသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0151.mp3">၁၅၁။ (၁၀) အေဗၻာကာသိက 
										ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0249.mp3">၂၄၉။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0038.mp3">၃၈။ စတုကၠသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0152.mp3">၁၅၂။ (၁၁) သုႆာန္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0250.mp3">၂၅၀။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0039.mp3">၃၉။ စတုကၠသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0153.mp3">၁၅၃။ (၁၁) သုႆာန္ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0251.mp3">၂၅၁။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0040.mp3">၄၀။ ပါတိေမာကၡသံဝရသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0154.mp3">၁၅၄။ (၁၂) ယထာသႏၱတိ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0252.mp3">၂၅၂။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0041.mp3">၄၁။ ပါတိေမာကၡသံဝရသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0155.mp3">၁၅၅။ (၁၃) နိသဇၨီ ဓုတင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0253.mp3">၂၅၃။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0042.mp3">၄၂။ ရဟန္းဟူူသည္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0156.mp3">၁၅၆။ 
										ဓုတင္ၿပိဳးျပြမ္းျပဆိုခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0254.mp3">၂၅၄။ (၁) 
										ကာမတို႔မွကင္းဆိတ္၍</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0043.mp3">၄၃။ ပါတိေမာကၡသံဝရသံဝုတ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0157.mp3">၁၅၇။ ဓုတ စသည္တို႔ကို 
										ေဝဖန္ေသာနည္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0255.mp3">၂၅၅။ အကုသိုလ္တရားတို႔အရ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0044.mp3">၄၄။ အာစာရေဂါစရသမၼႏၷ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0158.mp3">၁၅၈။ ဓုတဓမၼတရား (၅) 
										ပါး….the end.</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0256.mp3">၂၅၆။ ဤသို႔ေသာနည္းျဖင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0045.mp3">၄၅။ အာစာရေဂါစရသမၼႏၷ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0159.mp3">၁၅၉။ လမ္းျပေျမပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0257.mp3">၂၅၇။ ဤသို႔ေသာနည္းျဖင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0046.mp3">၄၆။ မဟာနိေဒၵသပါဠိေတာ္လာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0258.mp3">၂၅၈။ (၂) “ဝိတက္ 
										ဝိစာရႏွင္႔တကြျဖစ္ေသာ”</a></font></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="29" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0047.mp3">၄၇။ မဟာနိေဒၵသအ႒ကထာလာ</a></font></td>
										<td style="font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										<font size="2">ကမၼဌာနဂၢဟဏနိေဒၵသ</font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0259.mp3">၂၅၉။ (၂) “ဝိတက္ 
										ဝိစာရႏွင္႔တကြျဖစ္ေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0048.mp3">၄၈။ မဟာအာရကၡေဂါစရ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0160.mp3">၁၆၀။ ကမၼဌာနဂၢဟဏနိေဒၵသ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0260.mp3">၂၆၀။ ဝိတက္ ႏွင္႔ ဝိစာရ 
										အထူး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0049.mp3">၄၉။ အဏုမေတၱသု ဝေဇၨသု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0161.mp3">၁၆၁။ သမာဓိဟူသည္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0261.mp3">၂၆၁။ (၃) 
										“ဝိေဝကေၾကာင္႔ျဖစ္ေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0050.mp3">၅၀။ သမာဒါယ သိကၡတိ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0162.mp3">၁၆၂။ သမာဓိအျပား</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0262.mp3">၂၆၂။ (၄) “ပီတိသုခရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0051.mp3">၅၁။ ဣၿႏၵိယ သံဝရသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0163.mp3">၁၆၃။ ေလာကီ + ေလာကုတၱရာ 
										သမာဓိ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0263.mp3">၂၆၃။ ပီတိမွ သမာဓိျဖစ္ပံု 
										အဆင္႔ဆင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0052.mp3">၅၂။ ဣၿႏၵိယ သံဝရသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0164.mp3">၁၆၄။ သမာဓိ (၃) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0264.mp3">၂၆၄။ ပီတီ ႏွင္႔ သုခ အထူး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0053.mp3">၅၃။ ဣၿႏၵိယ သံဝရသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0165.mp3">၁၆၅။ သမာဓိ (၃) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0265.mp3">၂၆၅။ (၆) “ဝိဟရတိ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0054.mp3">၅၄။ အႏုဗ်ဥၨ္နကို 
										မွတ္ယူေလ႔မရွိ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0166.mp3">၁၆၆။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0266.mp3">၂၆၆။ (၇) “အဂၤါ ၅-ပါးကို 
										ပယ္ၿပီးသည္…..”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0055.mp3">၅၅။ မဟာတိႆမေထရ္ဝတၳဳ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0167.mp3">၁၆၇။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0267.mp3">၂၆၇။ (၈) “အဂၤါ ၅-ပါးႏွင္႔ 
										ျပည္႔စံုျခင္း”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0056.mp3">၅၆။ 
										စကၡဳေျႏၵကိုေစာင္႔စည္းမႈမရွိ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0168.mp3">၁၆၈။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0268.mp3">၂၆၈။ ဈာန္အဂၤါ ၅-ပါး 
										ျပည္႔စံုပံု</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0057.mp3">၅၇။ စကၡဳေျႏၵ၌ – သံဝရ 
										ျဖစ္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0169.mp3">၁၆၉။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0269.mp3">၂၆၉။ 
										ဧကဂၢတာသရုပ္ကိုထုတ္မျပ….</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0058.mp3">၅၈။ စကၡဳေျႏၵ၌ – သံဝရ 
										ျဖစ္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0170.mp3">၁၇၀။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0270.mp3">၂၇၀။ (၉) “ေကာင္းျခင္း 
										၃-ပါး….”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0059.mp3">၅၉။ 
										အသံဝရဟုဆိုရျခင္းအေၾကာင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0171.mp3">၁၇၁။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0271.mp3">၂၇၁။ 
										အဘယဂိရိဝါသီဆရာတို႔အဆို</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0060.mp3">၆၀။ အာဇီဝပါရိသုဒၶိသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0172.mp3">၁၇၂။ သမာဓိ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0272.mp3">၂၇၂။ 
										အဘယဂိရိဝါသီဆရာတို႔အဆို</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0061.mp3">၆၁။ အာဇီဝပါရိသုဒၶိသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0173.mp3">၁၇၃။ သမာဓိပြားမ်ားပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0273.mp3">၂၇၃။ 
										အဘယဂိရိဝါသီဆရာတို႔အဆို</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0062.mp3">၆၂။ 
										ခုဒၵကဝတၳဳဝိဘင္းပါဠိေတာ္၌လာေသာနည္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0174.mp3">၁၇၄။ ပလိေဗာဓ (၁၀) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0274.mp3">၂၇၄။ 
										အဘယဂိရိဝါသီဆရာတို႔အဆို</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0063.mp3">၆၃။ မဟာနိေဒၵသပါဠိေတာ္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0175.mp3">၁၇၅။ (၂) ကုလပလိေဗာဓ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0275.mp3">၂၇၅။ (၁၀) 
										“ပထဝီကသိုဏ္းကို…..”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0064.mp3">၆၄။ လပနာ ၁၃-ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0176.mp3">၁၇၆။ (၃) လာဘပလိေဗာဓ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0276.mp3">၂၇၆။ 
										ၾကာျမင္႔စြာတည္ျခင္းကိုၿပီးေစျခင္း</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0065.mp3">၆၅။ မဟာနိေဒၵသပါဠိေတာ္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0177.mp3">၁၇၇။ (၄) ဃနပလိေဗာဒ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0277.mp3">၂၇၇။ ေလးသမား ဥပမာ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0066.mp3">၆၆။ ေနမိတၱိကထာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0178.mp3">၁၇၈။ (၅) ကမၼပလိေဗာဓ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0278.mp3">၂၇၈။ (ခ) 
										နီဝရဏတရားတုိ႔ကို….</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0067.mp3">၆၇။ နိေပၸသိကတာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0179.mp3">၁၇၉။ (၆) ဂႏၱပလိေဗာဓ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0279.mp3">၂၇၉။ နိမိတ္ကိုပြားေစျခင္း</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0068.mp3">၆၈။ 
										အာဇီဝပါရိသုဒၶိသီလဟူသည္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0180.mp3">၁၈၀။ (၁၀) ဣဒိၶပလိေဗာဓ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0280.mp3">၂၈၀။ နိမိတ္ကိုပြားေစျခင္း</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0069.mp3">၆၉။ ပစၥယသႏၷိႆိတသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0181.mp3">၁၈၁။ ကမၼ႒ာန္း (၂) မ်ိဳး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0281.mp3">၂၈၁။ နိမိတ္ကိုပြားေစျခင္း</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0070.mp3">၇၀။ 
										ဆြမ္း၌ပစၥေဝကၡဏာဆင္ျခင္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0182.mp3">၁၈၂။ မရဏႆတိကမၼ႒ာန္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0282.mp3">၂၈၂။ 
										စ်ာန္ဝင္စားျခင္းမ်ားသူျဖစ္ရာ၏</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0071.mp3">၇၁။ ဣမႆ ကာယႆ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0183.mp3">၁၈၃။ (ခ) ပါရိဟာရိကမၼ႒ာန္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0283.mp3">၂၈၃။ 
										စ်ာန္ဝင္စားျခင္းမ်ားသူျဖစ္ရာ၏</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0072.mp3">၇၂။ ျဗဟၼစရိယာႏုဂၢဟာယ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0184.mp3">၁၈၄။ မိတ္ေဆြေကာင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0284.mp3">၂၈၄။ 
										စ်ာန္ဝင္စားျခင္းမ်ားသူျဖစ္ရာ၏</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0073.mp3">၇၃။ ေဝဒနာေဟာင္းသစ္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0185.mp3">၁၈၅။ မိတ္ေဆြေကာင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0285.mp3">၂၈၅။ 
										စ်ာန္ဝင္စားျခင္းမ်ားသူျဖစ္ရာ၏</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0074.mp3">၇၄။ ယာၾတာစ …</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0186.mp3">၁၈၆။ ဆရာထံ သြားပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0286.mp3">၂၈၆။ ဝသီေဘာ္ (၅) ပါး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0075.mp3">၇၅။ 
										ေက်ာင္း၌ပစၥေဝကၡဏာဆင္ျခင္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0187.mp3">၁၈၇။ နိကာယ္တစ္ခုမွ်…..</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0287.mp3">၂၈၇။ ဝသီေဘာ္ (၅) ပါး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0076.mp3">၇၆။ ဥတုပရိႆယ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0188.mp3">၁၈၈။ ဆရာထံေရာက္လွွ်င္ 
										ျပဳရမည္႔က်င္႔ဝတ္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0288.mp3">၂၈၈။ ဒုတိယစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0077.mp3">၇၇။ ဥတုပရိႆယ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0189.mp3">၁၈၉။ စရိုက္ဖြင္႔ျပခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0289.mp3">၂၈၉။ ဒုတိယစ်ာနကထာအဖြင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0078.mp3">၇၈။ ဥတုပရိႆယ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0190.mp3">၁၉၀။ ရာဂ ႏွင္႔ သဒၵါ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0290.mp3">၂၉၀။ (၁) “ဝိတက္ဝိစာရတို႔ 
										ၿငိမ္းျခင္းေၾကာင္႔”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0079.mp3">၇၉။ ေဆး၌ 
										ပစၥဝကၡဏာဆင္ျခင္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0191.mp3">၁၉၁။ အပေရဆရာအယူ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0291.mp3">၂၉၁။ (၄) “ေစတေသာ 
										ဧေကာဒိဘာဝံ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0080.mp3">၈၀။ ဝိလာနပစၥယ …</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0192.mp3">၁၉၂။ စရိုက္ဆိုင္ရာ 
										ေမးခြန္း (၃) ရပ္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0292.mp3">၂၉၂။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0081.mp3">၈၁။ ဝိလာနပစၥယ …</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0193.mp3">၁၉၃။ 
										စရိုက္တို႔၏ျဖစ္ေၾကာင္းတရား (၁)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0293.mp3">၂၉၃။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0082.mp3">၈၂။ 
										စတုပါရိသုဒၶိသီလကိုျပည္႔စံုေစပံုအစီအရင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0194.mp3">၁၉၄။ 
										စရိုက္တို႔၏ျဖစ္ေၾကာင္းတရား (၂)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0294.mp3">၂၉၄။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0083.mp3">၈၃။ 
										ခိုးသူတို႔တုပ္ေႏွာင္မေထရ္ဝတၳဳ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0195.mp3">၁၉၅။ 
										စရိုက္တို႔၏ျဖစ္ေၾကာင္းတရား (၃)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0295.mp3">၂၉၅။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0084.mp3">၈၄။ 
										ဣၿႏၵိယသံဝရသီလကိုျပည္႔စံုေစပံုအစီအရင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0196.mp3">၁၉၆။ စရိုက္တို႔ကို 
										ထင္ရွားျပျခင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0296.mp3">၂၉၆။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0085.mp3">၈၅။ 
										ျပည္႔စံုေစျခင္း၏အက်ိဳး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0197.mp3">၁၉၇။ (၅) 
										တရားတို႔၏ျဖစ္ျခင္းသေဘာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0297.mp3">၂၉၇။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0086.mp3">၈၆။ 
										ျပည္႔စံုေစျခင္း၏အက်ိဳး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0198.mp3">၁၉၈။ (၅) 
										တရားတို႔၏ျဖစ္ျခင္းသေဘာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0298.mp3">၂၉၈။ (၅) “ဝိတက္ ဝိစာရ 
										မရွိေသာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0087.mp3">၈၇။ စိတၱဂုတၱမေထရ္ဝတၳဳ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0199.mp3">၁၉၉။ 
										စရိုက္ႏွင္႔သင္႔ေလ်ာ္ေသာအရာမ်ား</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0299.mp3">၂၉၉။ (၆) “သမာဓိဇံ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0088.mp3">၈၈။ 
										အာဇီဝပါရိသုဒၶိသီလကိုျပည္႔စံုေစပံုအစီအရင္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0200.mp3">၂၀၀။ ကမၼဌာန္း (၄၀) 
										ဖြင္႔ျပခ်က္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0300.mp3">၃၀၀။ (၇) 
										“ဤသို႔ေနေသာေယာဂီသည္….”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0089.mp3">၈၉။ ဓုတင္ ေဆာင္, မေဆာင္….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0201.mp3">၂၀၁။ (၄) အဂၤါႏွင္႔ 
										အာရံုကိုလြန္….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0301.mp3">၃၀၁။ တတိယစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0090.mp3">၉၀။ 
										အလြန္ေခါင္းပါးေသာအက်င္႔ရွိေသာ….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0202.mp3">၂၀၂။ (၅) 
										ပြားေစ….မပြားေစအပ္…</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0302.mp3">၃၀၂။ တတိယစ်ာနကထာအဖြင္႔</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0091.mp3">၉၁။ 
										အလြန္ေခါင္းပါးေသာအက်င္႔ – သာဓကဝတၳဳ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0203.mp3">၂၀၃။ ေစာဒနာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0303.mp3">၃၀၃။ (၁) “ပီတိယာ စ 
										ဝိရာဂါ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0092.mp3">၉၂။ 
										ပစၥယသႏၷႆိတသီလကိုျပည္႔စံုေစပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0204.mp3">၂၀၄။ (၂) အာနာပါနႆတိ….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0304.mp3">၃၀၄။ (၂) “ဥေပကၡေကာ စ 
										ဝိဟရတိ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0093.mp3">၉၃။ ပရိေဘာဂ (၄) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0205.mp3">၂၀၅။ (၂) အာနာပါနႆတိ….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0305.mp3">၃၀၅။ (၂) “ဥေပကၡေကာ စ 
										ဝိဟရတိ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0094.mp3">၉၄။ သီလ (၄) ပါးႏွင္႔ 
										သုဒၶိ (၄) ပါးတြဲစပ္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0206.mp3">၂၀၆။ (၇) ဘံုကိုေဝဖန္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0306.mp3">၃၀၆။ ဥေပကၡာ (၁၀) ပါး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0095.mp3">၉၅။ သီလ (၄) ပါးႏွင္႔ 
										သုဒၶိ (၄) ပါးတြဲစပ္ပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0207.mp3">၂၀၇။ (၈) ယူအပ္သည္ကို 
										ေဝဖန္….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0307.mp3">၃၀၇။ ဥေပကၡာ (၁၀) ပါး</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0096.mp3">၉၆။ ဒါယဇၨပရိေဘာဂ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0208.mp3">၂၀၈။ (၉) 
										အေၾကာင္းကိုေဝဖန္…</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0308.mp3">၃၀၈။ 
										တရားကိုယ္တူလ်က္အမည္ကြဲပံု</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0097.mp3">၉၇။ အလံုးစံုေသာ အရိယာ, 
										ပုထုဇဥ္….</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0209.mp3">၂၀၉။ 
										စရိုက္အားေလ်ာ္စြာေဝဖန္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0309.mp3">၃၀၉။ သခၤါရုေပကၡာ ႏွင္႔ 
										ဝိပႆႏုေပကၡာ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0098.mp3">၉၈။ ဂါထာအေပါင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0210.mp3">၂၁၀။ ကမၼဌာန္းကိုရယူပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0310.mp3">၃၁၀။ သခၤါရုေပကၡာ ႏွင္႔ 
										ဝိပႆႏုေပကၡာ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0099.mp3">၉၉။ ပထမပဥၥကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0211.mp3">၂၁၁။ (၃) ျပည္႔စံုေသာအလုိ…</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0311.mp3">၃၁၁။ သခၤါရုေပကၡာ ႏွင္႔ 
										ဝိပႆႏုေပကၡာ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0100.mp3">၁၀၀။ ပရိယႏၱပါရိသုဒၶိသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0212.mp3">၂၁၂။ 
										ကမၼဌာန္းဆရာေဟာၾကားပံု</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0312.mp3">၃၁၂။ ေစာဒနာ</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 23px; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0101.mp3">၁၀၁။ ပရိယႏၱပါရိသုဒၶိသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="23">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="23" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0313.mp3">၃၁၃။ (၃) “သေတာ စသမၸဇာေနာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 25px; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0102.mp3">၁၀၂။ 
										သီလကိုခ်ီးက်ဴးေသာဂါထာ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="25">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="25" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0314.mp3">၃၁၄။ (၃) “သေတာ စသမၸဇာေနာ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0103.mp3">၁၀၃။ အပရာမ႒ပါရိသုဒၶိသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0315.mp3">၃၁၅။ (၄) “သုခဥၥ ကာေယန 
										ပဋိသံေဝေဒတိ”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0104.mp3">၁၀၄။ ဒုတိယပဥၥကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0316.mp3">၃၁၆။ (၅) 
										“တတိယစ်ာန္ႏွင္႔ျပည္႔စံု….”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0105.mp3">၁၀၅။ ဒုတိယပဥၥကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0317.mp3">၃၁၇။ (၆) 
										“ဤသို႔ေနေသာေယာဂီ…”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0106.mp3">၁၀၆။ ဒုတိယပဥၥကသီလ</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0318.mp3">၃၁၈။ စတုတၳစ်ာန္ ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0107.mp3">၁၀၇။ ပယ္ျခင္းဟူသည္</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0319.mp3">၃၁၉။ စတုတၳစ်ာန္ ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0108.mp3">၁၀၈။ (၁၁) – (၁၅)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0320.mp3">၃၂၀။ ေစာဒနာ (၁)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0109.mp3">၁၀၉။ (၁၆) – (၂၅)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0321.mp3">၃၂၁။ ေစာဒနာ (၂)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0110.mp3">၁၁၀။ (၂၆) – (၄၇)</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0322.mp3">၃၂၂။ ေစာဒနာ (၂)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0111.mp3">၁၁၁။ သီလညစ္ႏြမ္းေၾကာင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0323.mp3">၃၂၃။ ေစာဒနာ (၂)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0112.mp3">၁၁၂။ သီလညစ္ႏြမ္းေၾကာင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0324.mp3">၃၂၄။ ေစာဒနာ (၃)</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0113.mp3">၁၁၃။ ေမထုန္ငယ္ (၇) ပါး</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0325.mp3">၃၂၅။ (၄) 
										“ဒုကၡလည္းမဟုတ္….”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0114.mp3">၁၁၄။ သီလျဖဴစင္ေၾကာင္း</a></font></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0326.mp3">၃၂၆။ (၅) 
										“ဥေပကၡာေၾကာင္႔….”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0327.mp3">၃၂၇။ (၅) “ဥေပကၡာေၾကာင္႔…”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0328.mp3">၃၂၈။ (၆) 
										“ဤသို႔ေနေသာေယာဂီ…”</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<font size="2">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0329.mp3">၃၂၉။ ပဥၥကစ်ာန္ျပဆိုခ်က္</a></font></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0330.mp3">၃၃၀။ ပဥၥကစ်ာန္ျပဆိုခ်က္</a></td>
									</tr>
								</tbody>				                                
"""

two = """

									<colgroup>
										<col style="width: 170pt" width="227">
										<col style="width: 194pt" width="258">
										<col style="width: 233pt" width="310">
									</colgroup>
									<tbody><tr style="height: 23.25pt" height="31">
										<td style="height: 23.25pt; width: 249px; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" height="31">
										ေသသကသိဏနိေဒၵသ</td>
										<td style="width: 244px; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										ဆ-အႏုႆတိနိေဒၵသ</td>
										<td style="width: 257px; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA">
										ဆ-အႏုႆတိနိေဒၵသ</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0331.mp3">၃၃၁။ ေသသကသိဏနိေဒၵသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0372.mp3">၃၇၂။ ဆ-အႏုႆတိနိေဒၵသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257">
										&nbsp;</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0332.mp3">၃၃၂။ ေတေဇာကသိုဏ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0373.mp3">၃၇၃။ ဆ-အႏုႆတိနိေဒၵသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0421.mp3">၄၂၁။ ၂- ဥဇုပၸဋိပႏၷဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0333.mp3">၃၃၃။ ဝါေယာကသိုဏ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0374.mp3">၃၇၄။ (၁) ဗုဒၶါႏုႆတိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0422.mp3">၄၂၂။ ၃- ဉာယပၸဋိပႏၷဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0334.mp3">၃၃၄။ ဝါေယာကသိုဏ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0375.mp3">၃၇၅။ ၁- အရဟံဂုဏ္ေတာ္အဖြင္႔</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0423.mp3">၄၂၃။ ၄- သာမိစိပၸဋိပႏၷဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0335.mp3">၃၃၅။ ပီတကသိုဏ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0376.mp3">၃၇၆။ ၁- အရဟံဂုဏ္ေတာ္အဖြင္႔</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0424.mp3">၄၂၄။ ၅- အာဟုေနယ်ဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0336.mp3">၃၃၆။ အာေလာက ကသိုဏ္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0377.mp3">၃၇၇။ ၁- အရဟံဂုဏ္ေတာ္အဖြင္႔ (၄)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0425.mp3">၄၂၅။ ၆- ပါဟုေနယ်ဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0337.mp3">၃၃၇။ ၿပိဳးျပြမ္းျပဆိုခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0378.mp3">၃၇၈။ ၁- အရဟံဂုဏ္ေတာ္အဖြင္႔ (၅)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0426.mp3">၄၂၆။ ၇- ဒကၡိေဏယ်ဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0338.mp3">၃၃၈။ ၿပိဳးျပြမ္းျပဆိုခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0379.mp3">၃၇၉။ ၂- သမၼာသမၺဳဒၶဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0427.mp3">၄၂၇။ ၈ ႏွင္႔ ၉ ဂုဏ္ေတာ္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0339.mp3">၃၃၉။ ကသိုဏ္းတို႔၏ အထူးအျပား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0380.mp3">၃၈၀။ ၂- သမၼာသမၺဳဒၶဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0428.mp3">၄၂၈။ သီလာႏုႆတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0340.mp3">၃၄၀။ ကသိုဏ္းတို႔၏ အထူးအျပား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0381.mp3">၃၈၁။ ၃- ဝိဇၨာစရဏသမၸႏၷဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0429.mp3">၄၂၉။ စာဂါႏုႆတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0341.mp3">၃၄၁။ စ်ာန္မရႏိုင္ေသာပုဂၢိဳလ္မ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0382.mp3">၃၈၂။ ၃- ဝိဇၨာစရဏသမၸႏၷဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0430.mp3">၄၃၀။ စာဂါႏုႆတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0383.mp3">၃၈၃။ ၃- ဝိဇၨာစရဏသမၸႏၷဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0431.mp3">၄၃၁။ စာဂါႏုႆတိ</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="249" height="29">
										အသုဘကမၼဌာနနိေဒၵ</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0384.mp3">၃၈၄။ ၄- သုဂေတာဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0432.mp3">၄၃၂။ စာဂါႏုႆတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0342.mp3">၃၄၂။ အသုဘကမၼ႒ာနနိေဒၵသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0385.mp3">၃၈၅။ ၄- သုဂေတာဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0433.mp3">၄၃၃။ ဥပစာရစ်ာန္သို႔ေရာက္ပံု…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0343.mp3">၃၄၃။ အသုဘကမၼ႒ာနနိေဒၵသ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0386.mp3">၃၈၆။ ၄- သုဂေတာဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0434.mp3">၄၃၄။ ေဒဝတာႏုႆတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0344.mp3">၃၄၄။ ဥဒၶဳမာတက ကမၼ႒ာန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0387.mp3">၃၈၇။ ၄- သုဂေတာဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0435.mp3">၄၃၅။ ေဒဝတာႏုႆတိ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0345.mp3">၃၄၅။ ပန္ၾကား၍ သြားအပ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0388.mp3">၃၈၈။ ၅- ေလာကဝိဒူဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0436.mp3">၄၃၆။ ၿပိဳးျပြမ္းျပဆိုခ်က္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0346.mp3">၃၄၆။ အ႒ကထာတို႔၌ျပဆိုေသာအစီအရင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0389.mp3">၃၈၉။ ၅- ေလာကဝိဒူဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0437.mp3">၄၃၇။ မ်ားစြာေသာသုတ္တို႔၌ ေဟာေတာ္မူပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0347.mp3">၃၄၇။ အ႒ကထာတို႔၌ျပဆိုေသာအစီအရင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0390.mp3">၃၉၀။ ၅- ေလာကဝိဒူဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0438.mp3">၄၃၈။ ပုထုဇဥ္လည္း ႏွလံုးသြင္းထိုက္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0348.mp3">၃၄၈။ အက်ယ္ဖြင္႔ဆိုခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0391.mp3">၃၉၁။ ၅- ေလာကဝိဒူဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="258">&nbsp;</td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="29" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0349.mp3">၃၄၉။ (၁၁) ပါးေသာအျခင္းအရာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0392.mp3">၃၉၂။ ၾသကာသေလာကသိပံု</a></td>
										<td style="font-weight: 700; font-family: Zawgyi-One, sans-serif; text-align: center; vertical-align: middle; color: black; font-size: 11.0pt; font-style: normal; text-decoration: none; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: .5pt solid windowtext; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px; background: #ACB9CA" width="257">
										အႏုႆတိကမၼ႒ာနနိေဒၵသ</td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0350.mp3">၃၅၀။ (၁၁) ပါးေသာအျခင္းအရာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0393.mp3">၃၉၃။ ၆- အႏုတၱေရာပုရိသဒမၼသာရထိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0439.mp3">၄၃၉။ မရဏႆတိကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0351.mp3">၃၅၁။ (၁၁) ပါးေသာအျခင္းအရာ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0394.mp3">၃၉၄။ ၆- အႏုတၱေရာပုရိသဒမၼသာရထိ (၆-ခ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0440.mp3">၄၄၀။ ေသျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0352.mp3">၃၅၂။ နိမိတ္ထင္ေပၚေသာပုဂၢိဳလ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0395.mp3">၃၉၅။ ၆- အႏုတၱေရာပုရိသဒမၼသာရထိ (၆-ဂ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0441.mp3">၄၄၁။ မရဏႆတိပြားပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0353.mp3">၃၅၃။ ငါးပါးအျပားအားျဖင္႔ နိမိတ္ယူပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0396.mp3">၃၉၆။ ၇- သတၱာေဒဝမႏုႆာနံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0442.mp3">၄၄၂။ ရွစ္ပါးေသာအျခင္းအရာ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0354.mp3">၃၅၄။ ငါးပါးအျပားအားျဖင္႔ နိမိတ္ယူပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0397.mp3">၃၉၇။ ၇- သတၱာေဒဝမႏုႆာနံ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0443.mp3">၄၄၃။ (၁) သူသတ္သမားကဲ႔သို႔</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0355.mp3">၃၅၅။ အသြားအျပန္လမ္းကိုမွတ္သားျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0398.mp3">၃၉၈။ ၈- ဗုဒၶဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0444.mp3">၄၄၄။ (၁) သူသတ္သမားကဲ႔သို႔</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0356.mp3">၃၅၆။ အက်ိဳးအာနိသင္မ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0399.mp3">၃၉၉။ ၉- ဘဂဝါဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0445.mp3">၄၄၅။ (၂) ျပည္႔စံုျခင္း 
										ပ်က္စီးျခင္းအားျဖင္႔</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0357.mp3">၃၅၇။ အက်ိဳးအာနိသင္မ်ား</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0400.mp3">၄၀၀။ ဘဂဝါအနက္ (၉) ခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0446.mp3">၄၄၆။ (၃) အနီးသို႔ေဆာင္ေသာအားျဖင္႔</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0358.mp3">၃၅၈။ အက်ိဳးအာနိသင္ကို ေျမာ္ျမင္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0401.mp3">၄၀၁။ (၃) ဘဂ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0447.mp3">၄၄၇။ (၄) ရုပ္ကိုယ္၏..</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0359.mp3">၃၅၉။ အပၸနာအစီအရင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0402.mp3">၄၀၂။ ဘုန္းေတာ္ (၆) ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0448.mp3">၄၄၈။ (၈) ရွင္ဆဲခဏ၏…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0360.mp3">၃၆၀။ ဝိနီလက စေသာ ကမၼ႒ာန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0403.mp3">၄၀၃။ (၄) ဝိဘတၱဝါ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0449.mp3">၄၄၉။ ဥပစာရစ်ာန္သို႔ေရာက္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0361.mp3">၃၆၁။ ဝိပုဗၺက ကမၼ႒ာန္း…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0404.mp3">၄၀၄။ ဥပစာရစ်ာန္သို႔ေရာက္ပံု…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0450.mp3">၄၅၀။ အက်ိဳး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0362.mp3">၃၆၂။ ဝိကၡာယိတက ကမၼ႒ာန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0405.mp3">၄၀၅။ (၂) ဓမၼာႏုႆတိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0451.mp3">၄၅၁။ အက်ိဳး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0363.mp3">၃၆၃။ အ႒ိက ကမၼ႒ာန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0406.mp3">၄၀၆။ ၁- သြာကၡတဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0452.mp3">၄၅၂။ ကာယဂတာသတိကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0364.mp3">၃၆၄။ အ႒ိက ကမၼ႒ာန္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0407.mp3">၄၀၇။ ၁- သြာကၡတဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0453.mp3">၄၅၃။ ကာယဂတာသတိကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0365.mp3">၃၆၅။ ၿပိဳးျပြမ္းျပဆိုခ်က္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0408.mp3">၄၀၈။ ၁- သြာကၡတဂုဏ္ေတာ္ မည္ပံုတစ္နည္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0454.mp3">၄၅၄။ ဥဂၢဟေကာသလႅ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0366.mp3">၃၆၆။ ၿပိဳးျပြမ္းျပဆိုခ်က္ (ခ)</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0409.mp3">၄၀၉။ သႏၵိ႒ိကဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0455.mp3">၄၅၅။ စိတ္ျဖင္႔ရြတ္ဆိုပံု…</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0367.mp3">၃၆၇။ ပထမစ်ာန္မွ်သာရႏိုင္ျခင္း</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0410.mp3">၄၁၀။ ေလာကုတၱရာတရား (၉) ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0456.mp3">၄၅၆။ (၁) ဆံပင္</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0368.mp3">၃၆၈။ ရွင္ဆဲသူလည္း အသုဘသာျဖစ္ပံု</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0411.mp3">၄၁၁။ ေလာကုတၱရာတရား (၉) ပါး</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0457.mp3">၄၅၇။ ၾကြင္းေကာ႒ာသ – ႏွလံုး</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0369.mp3">၃၆၉။ ပညာမ်က္စိမရွိသူတို႔၏အျမင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0412.mp3">၄၁၂။ ၃- အကာလိကဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0458.mp3">၄၅၈။ (၁၂) အသည္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0370.mp3">၃၇၀။ ပညာမ်က္စိမရွိသူတို႔၏အျမင္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0413.mp3">၄၁၃။ ၄- ဧဟိပႆိကဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0459.mp3">၄၅၉။ (၂၁) သည္းေျခ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: medium none; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="249" height="24" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0371.mp3">၃၇၁။ ဂါထာ (၃) ပုဒ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0414.mp3">၄၁၄။ ၅- ၾသပေနယ်ိကဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0460.mp3">၄၆၀။ (၂၆) အဆီခဲ</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0415.mp3">၄၁၅။ ၅- ၾသပေနယ်ိကဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0461.mp3">၄၆၁။ အာနပါနႆတိကမၼ႒ာန္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0416.mp3">၄၁၆။ ၆- ပစၥတၱံေဝဒိတေဗၺာဝိညဴဟိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0462.mp3">၄၆၂။ အာနပါနကမၼ႒ာန္းအားထုတ္ပံု</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0417.mp3">၄၁၇။ တစ္နည္းအဖြင္႔</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0463.mp3">၄၆၃။ အားေကာင္းေသာသတိႏွင္႔ပညာ</a></td>
									</tr>
									<tr style="height:21.75pt" height="29">
										<td style="height: 21.75pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="29">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0418.mp3">၄၁၈။ ဥပစာရစ်ာန္သို႔ေရာက္ပံု…</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0464.mp3">၄၆၄။ စတုတၳစတုကၠအဖြင္႔</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0419.mp3">၄၁၉။ (၃) သံဃာႏုႆတိ</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0465.mp3">၄၆၅။ စာေမးပြဲဆိုင္ရာျပန္လွန္သင္ၾကားျခင္း</a></td>
									</tr>
									<tr style="height:18.0pt" height="24">
										<td style="height: 18.0pt; font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border: medium none; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="250" height="24">&nbsp;</td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="244" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0420.mp3">၄၂၀။ ၁- သုပၸဋိပႏၷဂုဏ္ေတာ္</a></td>
										<td style="font-size: 10.0pt; font-family: Zawgyi-One, sans-serif; color: black; font-weight: 400; font-style: normal; text-decoration: none; text-align: general; vertical-align: bottom; white-space: nowrap; border-left: medium none; border-right: .5pt solid windowtext; border-top: medium none; border-bottom: .5pt solid windowtext; padding-left: 1px; padding-right: 1px; padding-top: 1px" width="257" align="left">
										<a href="http://dhammadownload.com/MP3Library/DawKhinHlaTin/VisuddhiMagga/Dawkhinhlatin-VisuddhiMagga-0466.mp3">၄၆၆။ စာေမးပြဲဆိုင္ရာျပန္လွန္သင္ၾကားျခင္း</a></td>
									</tr>
								</tbody>
"""
#soup = bs4(one, 'html.parser')
soup = bs4(two, 'html.parser')



#with open('titles_links.txt', 'w') as f:
with open('titles_links.txt', 'a') as f:

    #count = 1
    count = 331
    for key in soup.find_all('tr'):
        try:
            counter = '{:03d}'.format(count)
            #print(" ".join(key.find('td').find('a').get_text().strip().split()))
            print('{}.mp3|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), 
                " ".join(key.find('td').find('a').get_text().strip().split())            
                ))
            f.write('{}.mp3|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), 
                " ".join(key.find('td').find('a').get_text().strip().split())            
                ))
            count += 1
        except AttributeError as err:
            pass
    for key in soup.find_all('tr'):        
        try:
            counter = '{:03d}'.format(count)
            print('{}..mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find('a').get('href'), 
            " ".join(key.find('td').find_next_sibling('td').find('a').get_text().strip().split()) 
                ))
            f.write('{}..mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find('a').get('href'), 
            " ".join(key.find('td').find_next_sibling('td').find('a').get_text().strip().split()) 
                ))                
            count += 1
        except AttributeError as err:
            pass
    for key in soup.find_all('tr'):        
        try:
            counter = '{:03d}'.format(count)
            print('{}..mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get('href'), 
            " ".join(key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get_text().strip().split()) ))
            f.write('{}..mp3|{}|{}\n'.format(counter, key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get('href'), 
            " ".join(key.find('td').find_next_sibling('td').find_next_sibling('td').find('a').get_text().strip().split()) ))            
            count += 1
        except AttributeError as err:
            pass
