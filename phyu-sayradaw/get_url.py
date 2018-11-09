from bs4 import BeautifulSoup as bs4

text = """<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0001-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁။ သူ႕အမည္က သုဒတၳ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0002-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂။ အလွဴရဲေသာ္လည္းမမြဲပါ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0003-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃။ ခက္ဆိုမွခက္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0004-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄။ ဘာေၾကာင့္အမွ်ေ၀ရတာလဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0005-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅။ မိဘေက်းဇူးကို အသသက္ေပးဆပ္သူ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0006-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆။ သစၥာေလးအင္ ျမတ္သဇင္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0007-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇။ အျမတ္ဆံုးပူေဇာ္ပြဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0008-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈။ ၀ိပႆနာအားထုတ္ရျခင္းအေၾကာင္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0009-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉။ ေအာင္ပြဲရေ၀ဒနာေယာဂီ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0010-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ အလုပ္ေပး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0011-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၁။ ကံၾကမၼာအေၾကြးေပးျဖတ္နည္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0012-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ လွဴကထိန္ျမတ္သကၤန္းးရယ္နဲ႕ မဂ္လမ္းကိုရြယ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0013-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ ဘာရသုတၱန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0014-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ အနီးအေ၀းသံုးနဲ႕ေလး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0015-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ ရွင္ရဟန္းနဲ႕သကၤန္းစြမ္းရည္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0016-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ လူငါးေယာက္နဲ႕ၾကီးေလးၾကီး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0017-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ သံဃဂုဏပကသက</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0018-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ အေၾကာင္းအက်ိဳးခ်စ္ျမတ္ႏိုး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0019-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၉။ အသက္ေသေသာ္လည္း မ်က္ရည္မက်</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0020-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၀။ အေမေက်းဇူးမေက် ငါမေသ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0021-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၁။ ရတနာထိုက္တဲ့ခ်စ္သမီး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0022-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၂။ စ-လယ္-ဆံုး &#8211; ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0023-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၃။ စ-လယ္-ဆံုး &#8211; ၂</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0024-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၄။ သီဟာေထရ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0025-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၅။ ဥပသကာဂုဏ္ရည္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0026-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၆။ အႏွစ္သံုးပါး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0027-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၇။ သာသနာအေမြခံ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0028-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၈။ ဘယ္ကုသလိုလ္အျမတ္ဆံုးပါလိမ့္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0029-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၂၉။ ေဘးလြတ္ရာသြား အိုလူသား</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0030-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၀။ ရင္မွာဆြဲရမည့္ ပုလဲရတနာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0031-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၁။ ခရီးသြားခရီးနား</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0032-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၂။ တရားဂုဏ္ေတာ္ရွိခိုးပူေဇာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0033-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၃။ အေရွ႕ကေန၀န္းထြက္သည့္ပမာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0034-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၄။ စာအံသံၾကားလို႕တရားရ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0035-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၅။ သင္ဘာတြက္ လုပ္တာလဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0036-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၆။ မဟာသတိပ႒ာန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0037-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၇။ ဒါရုကၡေႏၵာပမာသုတၱန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0038-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၈။ ကာမသုတၱန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0039-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၃၉။ စံျပကုသိုလ္ရွင္သူလိုျဖစ္ေစခ်င္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0040-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၀။ ပါေ၀ယ်ကဆင္တိုက္ပြဲ၀င္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0041-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၁။ လက္ငုတ္ေဖာ္ယူျပည္နိဗၺဴ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0042-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၂။ မဂၢင္ရွစ္တန္းရထားပ်ံ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0043-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၃။ ေမြးေန႕မွသည္ နိဗၺာန္ျပည္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0044-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၄။ သရဏဂုဏ္ရွင္းတမ္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0045-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၅။ ေသမင္းမေၾကာက္ရဲရဲေတာက္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0046-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၆။ အႏွစ္သံုးခုထုတ္စုသည့္ပြဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0047-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၇။ သံဃာဂုဏ္ရည္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0048-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၈။ ၾသကာသ၊ သရဏဂံု သီလရွင္းတန္း ႏွင့္ ေသြးျဖင့္ေရးေသာ ဓမၼကထာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0049-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၄၉။ ဘုရားအတြက္ အသက္စြန္႕၀ံ့သူ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0050-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၀။ အာေသာကမင္း၏နိဒါန္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0051-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၁။ မိုးေသာက္ၾကယ္ျဖဴ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0052-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၂။ သံုးပြင့္တစ္ခိုင္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0053-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၃။ ခင္ပြန္းၾကီးဆယ္ပါး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0054-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၄။ ခရီးသြားငါးေယာက္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0055-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၅။ သိမ္ေတာ္မဂၤလာသိေကာင္းစရာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0056-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၆။ ဘာသာေရးအေျခခံႏွင့္ ၀ိပႆနာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0057-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၇။ ၀ိပႆနာႏွင့္ စပ္သိမွတ္စဖြယ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0058-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၈။ ေဒ၀တာသုတၱန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0059-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၅၉။ မလြမ္းေပမယ့္မေမ့ပါ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0060-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၀။ လက္ေ၀ွ႕သမားရဲ႕ လက္ေတြ႕တရား</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0061-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၁။ ဇာတ္သိမ္းမတူတဲ့သူႏွစ္ဦး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0062-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၂။ သန္းကုေဋေက်ာ္တန္တဲ့ဒီေျခလွမ္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0063-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၃။ သာသနာေအာင္ပြဲအသက္ႏွင့္လဲ၍</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0064-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၄။ ဖိတ္ေခၚပါသည္အိုေယာဂီ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0065-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၅။ သရဏဂံုရွင္းတန္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0066-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၆။ သားလေရႊစင္နိဗၺာန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0067-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၇။ ေသမင္းကိုအႏိုင္ယူမယ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0068-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၈။ ေ၀လာမသုတၱန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0069-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၆၉။ ဆင္းရဲျငိမ္းရန္သတိပ႒ာန္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0070-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၀။ ၾသကာသကန္ေတာ့က်ိဳးရွင္းတမ္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0071-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၁။ ေကာင္းမွေကာင္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0072-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၂။ သီလရွင္းတန္းႏွင့္၀ိပႆနာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0073-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၃။ ကရုဏာရွင္ဗုဒၶ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0074-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၄။ သမထဘာ၀နာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0075-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၅။ နိဗၺာန္သြားမယ့္ရထား</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0076-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၆။ ေ၀ဒနာႏုပႆနာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0077-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၇။ ၀ိပႆနာအလုပ္ေပး &#8211; ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0078-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၈။ ၀ိပႆနာအလုပ္ေပး &#8211; ၂</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0079-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၇၉။ ၀ိပႆနာအလုပ္ေပး &#8211; ၃</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0080-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၀။ ေသြးနဲ႕ေရးတဲ့သာသနာ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0081-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၁။ တရားဂုဏ္ရွင္ &#8211; ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0082-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၂။ တရားဂုဏ္ရွင္ &#8211; ၂</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0083-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၃။ ဗာကုလဇာတ္ေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0084-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၄။ လူျခင္းမတူတာ ဘာေၾကာင့္လဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0085-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၅။ ေလးၾကိမ္ေျမာက္ ဘံုကထိန္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0086-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၆။ သိမ္အလွဴ &#8211; ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0087-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၇။ သိမ္အလွဴ &#8211; ၂</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0088-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၈။ ေက်ာင္းအလွဴ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0089-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၈၉။ ပန္ကာအလွဴ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0090-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၀။ ေရခဲေသတၱာအလွဴ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0091-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၁။ ဘာသာေရးအစ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0092-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၂။ ၀ါဆိုကိုးခ်က္လျပည့္ရက္၊ ေဆာင္ရြက္သံုးလူမင္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0093-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၃။ မီးေလာင္ျပင္မွပြင့္ေသာပန္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0094-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၄။ အျဖဴနဲ႕အမည္းတမူကြဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0095-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၅။ တရားနာေသာဖားကေလး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0096-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၆။ သင္ဘာအတြက္ လုပ္တာလဲ</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0097-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၇။ နတ္တို႕တမ္းတလူ႕ဘ၀</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0098-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၈။ သံဃာဂုဏ္ရည္ &#8211; ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0099-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၉၉။ သံဃာဂုဏ္ရည္ &#8211; ၂</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0100-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၀၀။ ၀ိပႆနာခ်စ္ျမတ္ႏိုး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0101-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၀၁။ သူမ်ားအလွဴ၀ယ္တဲ့ကိုရင္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0102-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၀၂။ သစ္တစ္ပင္ေကာငး္ ငွက္တစ္ေသာင္း</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0103-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၀၃။ စကၤာပူတြင္ေဟာၾကားေသာတရား &#8211; ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Phu-SayaDaw-U-Narapati-MP3/DVD%28104%29/0104-PHU.mp3" target="_blank"><span style="color: #ffcc00;">၁၀၄။ စကၤာပူတြင္ေဟာၾကားေသာတရား &#8211; ၂</span></a></span></p>
    </div>"""

soup = bs4(text, 'html.parser')

with open('titles_links.txt', 'w') as f:
    for key in soup.find_all('a'):
        f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        #f.write('{}\n'.format(key.get_text()))
        
with open('file.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get('href')))

with open('titles.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get_text()))        



