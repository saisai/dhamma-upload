from bs4 import BeautifulSoup as bs4

text = """

        <p><span style="color: #00ffff;"><a title="တရားေတာ္မ်ားအား ေဒါင္းလုပ္ဆြဲနည္း" href="https://www.thitsarparamisociety.com/download/"><span style="color: #00ffff;">MP3 တရားေတာ္မ်ား မိမိအသံုးျပဳသည့္ Mobile သို႔ PC(Desktop)မ်ားအတြက္ ေဒါင္းလုပ္ဆြဲပံု အဆင့္ဆင့္ <span style="color: #ffcc00;">Click Here</span></span></a></span></p>
<h5><span style="color: #339966;">သစၥာေရႊစည္ ဆရာေတာ္ အရွင္ ဥတၱမ ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား စုစည္းမွု (MP3)</span></h5>
<h5><span style="color: #339966;"><a style="font-weight: bold; color: #3366ff;" href="https://www.thitsarparamisociety.com/ahshinottama-ebook/" target="_blank">သစၥာေရႊစည္ ဆရာေတာ္ အရွင္ ဥတၱမ<strong> တရားစာအုပ္မ်ား</strong> Click Here</a></span></h5>
<p>&nbsp;</p>
<h5><span style="color: #339966;">၂၀၁၈ ဝါတြင္းကာလ လွည္းကူး တရားစခန္းတြင္ ေဟာၾကားေတာ္မူခဲ့ေသာ တရားေတာ္မ်ား</span></h5>
<p><span style="color: #ff9900;"><a style="color: #ff9900;" href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-031118PM2.mp3">ဘုရားရွိခိုး (၃)ပုဒ္ တရားေတာ္ &nbsp;အပိုင္း (၁) (3.11.10)</a></span></p>
<p><span style="color: #ff9900;"><a style="color: #ff9900;" href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-041118PM2.mp3">ဘုရားရွိခိုး (၃)ပုဒ္ တရားေတာ္ &nbsp;အပိုင္း (၂)</a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-051118PM2.mp3"><span style="color: #ff9900;">ဘုရားရွိခိုး (၃)ပုဒ္ တရားေတာ္&nbsp; အပိုင္း (၃)</span></a></p>
<p><span style="color: #ff9900;"><a style="color: #ff9900;" href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-041118AM10.mp3">ကထိန္အႏုေမာဒနာတရားေတာ္</a> (၁၁)ျကိမ္ေျမာက္ စုေပါင္းမဟာဘံုကထိန္သကၤန္း ကပ္လွဳဒါန္းပြဲ</span></p>
<p><span style="color: #ff9900;"><a style="color: #ff9900;" href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-031118PM7.mp3">ဂဂၤမာလဇာတ္ တရားေတာ္</a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-041118PM7.mp3"><span style="color: #ff9900;">သကၠပဥွ သုတၱန္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/sunday-talk/418-THITSARSHWESI/418-051118PM7.mp3"><span style="color: #ff9900;">မဟာသုဒႆနသုတၱန္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Oct/24.10.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၂၄.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Oct/25.10.2018.mp3"><span style="color: #ffcc00;">အလြယ္မက္ရင္ အခက္ၾကံဳမယ္တရားေတာ္ (၂၅.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Oct/26.10.2018.mp3"><span style="color: #ffcc00;">ပညာရိွသူေတာ္ေကာင္း (၂၆.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Oct/27.10.2018.mp3"><span style="color: #ffcc00;">ကိေလသာေတြမ၀င္ေအာင္ ဘယ္လိုေစာင့္ေရွာက္ရမလဲ (၂၇.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Oct/28.10.2018.mp3"><span style="color: #ffcc00;">ကုသိုလ္ေကာင္းမႈေတြတိုးပြားလာေအာင္ ဘယ္လိုေဆာင္ရြက္ၾကမလဲ (၂၈.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Oct/304.10.2018.mp3"><span style="color: #ffcc00;">ဂိရိမာနႏၵသုတၱံအႏွစ္ခ်ဳပ္တရားေတာ္ (၃၀.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/336.mp3"><span style="color: #ffcc00;">တရားအားထုတ္ၿခင္း၏ အက်ိဳးမ်ား (၇.၈.၂၀၁၈ / ညေန)</span></a><br>
<a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/337.mp3"><span style="color: #ffcc00;">အားေပးစကား (၁) (၈.၈.၂၀၁၈ / မနက္ခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/338.mp3"><span style="color: #ffcc00;">ဓနဥၥာနိသုတၱန္ (၈.၈.၂၀၁၈ / ညခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/339.mp3"><span style="color: #ffcc00;">အားေပးစကား (၂) (၉.၈.၂၀၁၈ / မနက္ခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/342.mp3"><span style="color: #ffcc00;">ရူပါရာမသုတၱန္ (၉.၈.၂၀၁၈ / ညခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/343.mp3"><span style="color: #ffcc00;">အားေပးစကား (၃) (၁၀.၈.၂၀၁၈ / မနက္ခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/344.mp3"><span style="color: #ffcc00;">တထာဂတ အစၦရိယ သုတၱန္ (၁၀.၈.၂၀၁၈ / ညခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/345.mp3"><span style="color: #ffcc00;">အားေပးစကား (၄) (၁၁.၈.၂၀၁၈ / မနက္ခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/August/346.mp3"><span style="color: #ffcc00;">ၾကားရရုံပင္ အပူစင္၍ (၁၁.၈.၂၀၁၈ ညခင္း)</span></a></p>
<h5><span style="color: #339966;">၂၀၁၈ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္အသစ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/17.6.2018_6pm.mp3"><span style="color: #ffcc00;">စိတၱသမၻဴတဇာတ္ တရားေတာ္ (၁၇.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/16.6.2018_7pm.mp3"><span style="color: #ffcc00;">မဟာသုတေသာမဇာတ္ တရားေတာ္ (၁၆.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/15.6.2018_7pm.mp3"><span style="color: #ffcc00;">အကိတၱိဇာတ္ တရားေတာ္ (၁၅.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/15.6.2018_10am.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း အပိုင္း (၁) (၁၅.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/15.6.2018_3pm.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း အပိုင္း (၂) (၁၅.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/16.6.2018_2pm.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း အပိုင္း (၃) (၁၆.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/17.6.2018_10am.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း အပိုင္း (၄) (၁၇.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/June/17.6.2018_3pm.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း အပိုင္း (၅) (၁၇.၆.၂၀၁၈ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/May/14.05.2018.mp3"><span style="color: #ffcc00;">ပုဗၺသုတၱံ၊ နာကုလပိတာသုတၱံ – လူငယ္လူၾကီးတရားေတာ္ (၁၄.၅.၂၀၁၈ ထိုင္၀မ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/May/13.05.2018.mp3"><span style="color: #ffcc00;">ဇရာသုတၱံ (၁၃.၅.၂၀၁၈ ထိုင္၀မ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/May/12.05.2018.mp3"><span style="color: #ffcc00;">နာဂသုတၱံ (၁၂.၅.၂၀၁၈ ထိုင္၀မ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/27.4.2018.mp3"><span style="color: #ffcc00;">လူငယ္လူၾကီးတရားေတာ္ (၂၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/18.4.2018.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုးႀကီးပြါးျခင္း (၁၈.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/17.4.2018.mp3"><span style="color: #ffcc00;">တစ္ဘ၀ျပီးတစ္ဘ၀ (၁၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/16.4.018.mp3"><span style="color: #ffcc00;">တရား(၄)မ်ိဳးႏွင့္ ဂုဏ္သတၱိ (၁၆.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/15.4.2018.mp3"><span style="color: #ffcc00;">ကိုရင္တိႆ (၁၅.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/14.4.2018.mp3"><span style="color: #ffcc00;">စစ္မွန္ေသာ ေအာင္ျမင္မႈ (၁၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/13.4.2018.mp3"><span style="color: #ffcc00;">ရ႒ပါလသုတၱံ (၁၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/April/07.4.2018.mp3"><span style="color: #ffcc00;">ဇရာသုတၱံ (၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/2018/Mar/10.3.2018.mp3"><span style="color: #ffcc00;">ဒုကၡၿငိမ္းေၾကာင္း နည္းလမ္းေကာင္း (၁၀.၃.၂၀၁၈)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">၂၀၁၇ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္အသစ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Dec/29.12.2017.mp3"><span style="color: #ffcc00;">သံေယာဇဥ္ (၂၉.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Dec/28.12.107.mp3"><span style="color: #ffcc00;">ဓမၼပဒဂါထာတရားေတာ္ (၂) – (၂၈.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Dec/27.12.2017.mp3"><span style="color: #ffcc00;">ဓမၼပဒဂါထာတရားေတာ္ (၁) – (၂၇.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Dec/26.12.2017.mp3"><span style="color: #ffcc00;">ဥဒယဘဒၵဇာတ္ (၂၆.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Dec/25.12.2017.mp3"><span style="color: #ffcc00;">စာလာေထရီ ၊ ဥပစာလာေထရီ၊ သီသူပစာလာေထရီ (၂၅.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Dec/24.12.2017.mp3"><span style="color: #ffcc00;">၀ဇိရာေထရီ ႏွင့္ ေသလာေထရီ (၂၄.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/25.11.2017.mp3"><span style="color: #ffcc00;">နာကုလပိတုသုတၱံ ႏွင့္ ဥဂၢသုတၱံ တရားေတာ္ (၂၅.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/24.11.2017.mp3"><span style="color: #ffcc00;">ဆပၸါဏေကာပမသုတၱံ တရားေတာ္ (၂၄.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/23.11.2017.mp3"><span style="color: #ffcc00;">၀မၼိကသုတၱံ တရားေတာ္ (၂၃.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/22.11.2017.mp3"><span style="color: #ffcc00;">အာသီ၀ိေသာပမသုတၱံ တရားေတာ္ (၂၂.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/21.11.2017.mp3"><span style="color: #ffcc00;">ဒါ႐ုကၡေႏၶာပမသုတၱံ တရားေတာ္ (၂၁.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/20.11.2017.mp3"><span style="color: #ffcc00;">ျဖဴေအာင္စိတ္ကိုထား တရားေတာ္ (၂၀.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/19.11.2017.mp3"><span style="color: #ffcc00;">ေကာင္းမႈေဆာင္ တရားေတာ္ (၁၉.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/18.11.2017.mp3"><span style="color: #ffcc00;">မေကာင္းမႈေရွာင္ တရားေတာ္ (၁၈.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Nov/17.11.2017.mp3"><span style="color: #ffcc00;">ေယာနိေသာမနသိကာရ – ႏုလံုးသြင္းမွန္ျခင္းတရားေတာ္ (၁၇.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Oct/9.10.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၉.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Oct/8.10.2017.mp3"><span style="color: #ffcc00;">ပါတရာသီသုတၱံ (၈.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Oct/7.10.2017.mp3"><span style="color: #ffcc00;">ပါရာယနသုတၱံ (၇.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Oct/6.10.2017.mp3"><span style="color: #ffcc00;">ေဂါပါလကသုတ္ (၆.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Oct/5.10.2017.mp3"><span style="color: #ffcc00;">ပုတၱမံသူပမသုတၱံ (၅.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Oct/4.10.2017.mp3"><span style="color: #ffcc00;">နာဂေရာပမသုတၱံ (၄.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/24.9.2017.mp3"><span style="color: #ffcc00;">စိတ္ကိုဘယ္လိုဆံုးမလဲတရားေတာ္ (၂၄.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/17.9.2017_5PM.mp3"><span style="color: #ffcc00;">အရဏ၀ိဘဂၤသုတၱန္ – ဘ၀ေနနည္းတရားေတာ္ (၁၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/17.9.2017_2PM.mp3"><span style="color: #ffcc00;">ကႎသုေကာပမသုတၱန္တရားေတာ္ (၁၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/17.9.2017_10AM.mp3"><span style="color: #ffcc00;">ကိုယ့္ကုိယ္ကိုေကာင္းသထက္ေကာင္းေအာင္ၾကိဳးစားပါ (၁၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/16.9.2017_7PM.mp3"><span style="color: #ffcc00;">မာဂ႑ိယသုတၱန္ – ကာမႏွင့္ဘ၀တရားေတာ္ (၁၆.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/16.9.2017_2PM.mp3"><span style="color: #ffcc00;">အာသီ၀ိေသာပမသုတၱန္ (၁၆.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/14.9.2017.mp3"><span style="color: #ffcc00;">ဥပမာ(၃)မ်ိဳးတရားေတာ္ (၁၄.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/UOttama%20ThitSarShweSi/281.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ (သို႔) လမ္းခရီး၌ကၽြမ္းက်င္လိမၼာသူ (၁၁.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/Sep/10.9.2017.mp3"><span style="color: #ffcc00;">ဆင္ျခင္ရမည့္တရားမ်ား (၁၀.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/August/29.8.2017.mp3"><span style="color: #ffcc00;">ဥပုသ္သီလေပး တရားေတာ္ (၂၉.၈.၂၀၁၇)</span></a></p>
<h5><span style="color: #339966;">မေထရ္ျမတ္ၾကီးမ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/May/26.5.2017.mp3"><span style="color: #ffcc00;">အရွင္သာရိပုတၱရာမေထရ္ျမတ္အေၾကာင္း(၁) (၂၆.၅.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/May/27.5.2017.mp3"><span style="color: #ffcc00;">အရွင္သာရိပုတၱရာမေထရ္ျမတ္အေၾကာင္း(၂) (၂၇.၅.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/May/28.5.2017.mp3"><span style="color: #ffcc00;">အရွင္မဟာေမဂၢလန္မေထရ္ျမတ္အေၾကာင္း (၂၈.၅.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/May/29.5.2017.mp3"><span style="color: #ffcc00;">အရွင္မဟာကႆပမေထရ္ျမတ္အေၾကာင္း (၂၉.၅.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/May/30.5.2017.mp3"><span style="color: #ffcc00;">အရွင္အာနႏၵာမေထရ္ျမတ္အေၾကာင္း (၃၀.၅.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/May/31.5.2017.mp3"><span style="color: #ffcc00;">အရွင္အႏုရုဒၶါမေထရ္ျမတ္အေၾကာင္း (၃၁.၅.၂၀၁၇)</span></a></p>
<h5><span style="color: #339966;">ဒါန၊ သီလ၊ ဘာ၀နာ တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/116.mp3"><span style="color: #ffcc00;">ဒါန တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/117.mp3"><span style="color: #ffcc00;">သီလ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/118.mp3"><span style="color: #ffcc00;">ဘာဝနာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/290417PM2EDIT.mp3"><span style="color: #ffcc00;">ဗုဒၶါႏုႆတိဘဝနာ တရားေတာ္ (၂၉.၄.၂၀၁၇) ေန႔ခင္း (၂:၀၀) နာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/290417PM7EDIT.mp3"><span style="color: #ffcc00;">ပဟာတဗၺ တရားေတာ္ (၂၉.၄.၂၀၁၇) ည (၇:၀၀) နာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/300417AM10EDIT.mp3"><span style="color: #ffcc00;">ေမတၱာဘာဝနာ တရားေတာ္ (၃၀.၄.၂၀၁၇) နံနက္ (၁၀:၀၀) နာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/300417PM2EDIT.mp3"><span style="color: #ffcc00;">အသုဘ ဘာဝနာ တရားေတာ္ (၃၀.၄.၂၀၁၇) ေန႔ခင္း (၂:၀၀) နာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/300417PM7EDIT.mp3"><span style="color: #ffcc00;">ဘာေဝတဗၺ တရားေတာ္ (၃၀.၄.၂၀၁၇) ည (၇:၀၀) နာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/10517AM10EDIT.mp3"><span style="color: #ffcc00;">မရဏာႏုႆတိ ဘာဝနာ တရားေတာ္ (၁.၅.၂၀၁၇) နံနက္ (၁၀:၀၀) နာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/10517PM2EDIT.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္ ဘာဝနာတရားေတာ္ (၁.၅.၂၀၁၇) ေန႔ခင္း (၂:၀၀) နာရီ</span></a></p>
<h5><span style="color: #339966;">သစၥာေလးပါး တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/singapore-3-10-2015/Thitsar-Lay-Par-1.mp3"><span style="color: #ffcc00;">သစၥာေလးပါး တရားေတာ္ (ဒုကၡသစၥာ) (၃.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/singapore-3-10-2015/Thitsar-Lay-Par-2.mp3"><span style="color: #ffcc00;">သစၥာေလးပါး တရားေတာ္ (သမုဒယသစၥာ) (၃.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/singapore-3-10-2015/151004_0010.MP3"><span style="color: #ffcc00;">သစၥာေလးပါး တရားေတာ္ (နိေယာဓသစၥာ) (၄.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/singapore-3-10-2015/151004_0011.MP3"><span style="color: #ffcc00;">သစၥာေလးပါး တရားေတာ္ (မဂၢသစၥာ) (၄.၁၀.၂၀၁၅)</span></a></p>
<h5><span style="color: #339966;">ေဗာဓိပကၡိရတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/06%20Bawdi%20Pakeiya%201.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/07%20Bawdi%20Pakeiya%202.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/08%20Bawdi%20Pakeiya%203.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/09%20Bawdi%20Pakeiya%204.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/10%20Bawdi%20Pakeiya%205.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/11%20Bawdi%20Pakeiya%206.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/12%20Bawdi%20Pakeiya%207.MP3"><span style="color: #ffcc00;">ေဗာဓိပကၡိရ (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/094.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္ (၄)ပါး – စကၤာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/095.MP3"><span style="color: #ffcc00;">သမၼပၸဒါန္ (၄)ပါး – စကၤာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/096.mp3"><span style="color: #ffcc00;">ကၠဒၶိပါဒ္(၄)ပါး – စကၤာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/097.MP3"><span style="color: #ffcc00;">ဣေျႏၵ(၅)ပါး – စကၤာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/098.MP3"><span style="color: #ffcc00;">ဗိုလ္ (၅)ပါး – စကၤာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/099.MP3"><span style="color: #ffcc00;">ေဗာဇၥ်င္(၇)ပါး – စကၤာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/100.mp3"><span style="color: #ffcc00;">မဂၢင္(၈)ပါး – စကၤာပူ</span></a></p>
<h5><span style="color: #339966;">ပါရမီ(၁၀)ပါးတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/10.mp3"><span style="color: #ffcc00;">ဥေပကၡာပါရမီ (၃၁.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/9.mp3"><span style="color: #ffcc00;">ေမတၱာပါရမီ (၃၀.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/8.mp3"><span style="color: #ffcc00;">အဓိ႒ာန္ပါရမီ (၂၉.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/7.mp3"><span style="color: #ffcc00;">သစၥာပါရမီ (၂၈.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/6.mp3"><span style="color: #ffcc00;">ခႏၲီပါမီ (၂၇.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/5.mp3"><span style="color: #ffcc00;">ဝီရိယပါရမီ (၂၆.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/4.mp3"><span style="color: #ffcc00;">ပညာပါရမီ (၂၅.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/3.mp3"><span style="color: #ffcc00;">ေနကၡမပါရမီ (၂၄.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/2.mp3"><span style="color: #ffcc00;">သီလပါရမီ (၂၃.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Parami-10-par/1.mp3"><span style="color: #ffcc00;">ဒါနပါရမီ (၂၂.၅.၂၀၁၆)</span></a></p>
<h5><span style="color: #339966;">အလုပ္ေပးတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/111.mp3"><span style="color: #ffcc00;">ပထမေန႔ အလုပ္ေပးတရားေတာ္ – (၂၅.၁၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/01%2026-12-2016%20Aloatpay%201.mp3"><span style="color: #ffcc00;">ဒုတိယေန႔ အလုပ္ေပးတရားေတာ္ – (၂၆.၁၂.၂၀၁၆) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/02%2027-12-2016%20Aloatpay%202.mp3"><span style="color: #ffcc00;">တတိယေန႔ အလုပ္ေပးတရားေတာ္ – (၂၇.၁၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/03%2028-12-2016%20Aloatpay%203.mp3"><span style="color: #ffcc00;">စတုတၳေန႔ အလုပ္ေပးတရားေတာ္ -(၂၈.၁၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/04%2029-12-2016%20Aloatpay%204.mp3"><span style="color: #ffcc00;">ပဥၥမေန႔ အလုပ္ေပးတရားေတာ္ – (၂၉.၁၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Alote-Pay-tayartaw/05%2030-12-2016%20Aloatpay%205.mp3"><span style="color: #ffcc00;">ဆ႒မေေန႔ အလုပ္ေပးတရားေတာ္ – (၃၀.၁၂.၂၀၁၆) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/02_07082016.mp3"><span style="color: #ffcc00;">အလုပ္ေပးတရားေတာ္ (၂၀၁၆ စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-9.mp3"><span style="color: #ffcc00;">အလုပ္ေပးတရားေတာ္ (၂၀၁၆ သၾကၤန္)</span></a></p>
<h5><span style="color: #339966;">တစ္ေၾကာင္းတည္းေသာလမ္းတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/135.mp3"><span style="color: #ffcc00;">တစ္ေၾကာင္းတည္းေသာလမ္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/136.mp3"><span style="color: #ffcc00;">တစ္ေၾကာင္းတည္းေသာလမ္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/137.mp3"><span style="color: #ffcc00;">တစ္ေၾကာင္းတည္းေသာလမ္း(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/138.mp3"><span style="color: #ffcc00;">တစ္ေၾကာင္းတည္းေသာလမ္း(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/139.mp3"><span style="color: #ffcc00;">တစ္ေၾကာင္းတည္းေသာလမ္း(၅)</span></a></p>
<h5><span style="color: #339966;">မဂၤလာတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/141.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/142.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/143.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/144.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/145.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/146.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/147.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/148.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/149.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/150.mp3"><span style="color: #ffcc00;">မဂၤလာတရားေတာ္ (၁၀)</span></a></p>
<h5><span style="color: #339966;">သာသနာေတာ္၏ ရတနာမ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/14-7-2015.mp3"><span style="color: #ffcc00;">သာသနာေတာ္၏ ရတနာမ်ား – ၁ (၁၄.၇.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/15-7-2015.mp3"><span style="color: #ffcc00;">သာသနာေတာ္၏ ရတနာမ်ား – ၂ (၁၅.၇.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/16-7-2015.mp3"><span style="color: #ffcc00;">သာသနာေတာ္၏ ရတနာမ်ား – ၃ (၁၆.၇.၂၀၁၅)</span></a></p>
<h5><span style="color: #339966;">ကလ်ာဏပုထုစဥ္တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/1A_06082016.mp3"><span style="color: #ffcc00;">ကလ်ာဏပုထုစဥ္ အပိုင္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/01_07082016.mp3"><span style="color: #ffcc00;">ကလ်ာဏပုထုစဥ္ အပိုင္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/03_07082016.mp3"><span style="color: #ffcc00;">ကလ်ာဏပုထုစဥ္ အပိုင္း(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/01_09082016.mp3"><span style="color: #ffcc00;">ကလ်ာဏပုထုစဥ္ အပိုင္း(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/02_09082016.mp3"><span style="color: #ffcc00;">ကလ်ာဏပုထုစဥ္ အပိုင္း(၅)</span></a></p>
<h5><span style="color: #339966;">သူေတာ္ေကာင္းတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/164.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းဆုိသည္မွာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/190.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းဆုိသည္မွာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/009.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတုိ႔၏သေဘာထား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/082.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတုိ႔သေဘာထား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/088.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတုိ႔သေဘာထား (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/133.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းဥစၥာ(၇)ပါး</span></a></p>
<h5><span style="color: #339966;">၂၀၁၇ – သႀကၤန္တြင္း တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/12.4.2017.mp3"><span style="color: #ffcc00;">(၁၂.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/13.4.2017.mp3"><span style="color: #ffcc00;">(၁၃.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/14.4.2017.mp3"><span style="color: #ffcc00;">(၁၄.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/15.4.2017.mp3"><span style="color: #ffcc00;">(၁၅.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/16.4.2017.mp3"><span style="color: #ffcc00;">(၁၆.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/17.4.2017.mp3"><span style="color: #ffcc00;">(၁၇.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/18.4.2017.mp3"><span style="color: #ffcc00;">(၁၈.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2017/April/19.4.2017.mp3"><span style="color: #ffcc00;">(၁၉.၄.၂၀၁၇) ေန႔တြင္ ေဟာၾကားေတာ္မူေသာ တရားေတာ္</span></a></p>
<h5><span style="color: #339966;">၂၀၁၆ – သႀကၤန္တြင္း တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-1.mp3"><span style="color: #ffcc00;">ပထမေန႔&nbsp; တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-2.mp3"><span style="color: #ffcc00;">ဒုတိယေန႔ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-3.mp3"><span style="color: #ffcc00;">တတိယေန႔ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-4.mp3"><span style="color: #ffcc00;">စတုတၳေန႔ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-5.mp3"><span style="color: #ffcc00;">ပဥၥမေန႔ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-6.mp3"><span style="color: #ffcc00;">ဆ႒မေန႔ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-7.mp3"><span style="color: #ffcc00;">သတၱမေန႔ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/thitgyan-8.mp3"><span style="color: #ffcc00;">သတၱမေန႔ ႏႈတ္ဆက္ တရားေတာ္</span></a></p>
<h5><span style="color: #339966;">စုစည္းထားေသာအကၡရာစဥ္တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/129.mp3"><span style="color: #ffcc00;">ကံသုံးပါးကုိျဖဴစင္ေအာင္ႀကိဳးစားပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/NO142/01%20A%202014%2012/20140224%20KanHnaZat%20ZayYaWaDi.mp3"><span style="color: #ffcc00;">ကဏဌာဇာတ္ (၂၄.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/6-4-2016.mp3"><span style="color: #ffcc00;">ကိုယ့္စိတ္ကိုစစ္ေဆးပါ (၆.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/166.mp3"><span style="color: #ffcc00;">ကုသုိလ္ႏွင့္အကုသုိလ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/31-8-2015.mp3"><span style="color: #ffcc00;">ခြန္အားေလးမ်ဳိး (၃၁.၈.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/049.mp3"><span style="color: #ffcc00;">ေကာင္းတာေတြထက္ေကာင္းတဲ့အရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/161.mp3"><span style="color: #ffcc00;">ေကာင္းမႈေဆာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/18-2-2016.mp3"><span style="color: #ffcc00;">ေကာင္းျမတ္ေသာ ေနျခင္းေလးမ်ဳိး (၁၈.၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/007.mp3"><span style="color: #ffcc00;">ေကာင္းေသာည</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/155.mp3"><span style="color: #ffcc00;">ေကာင္းေသာတရားဆုိသည္မွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/196.mp3"><span style="color: #ffcc00;">ေက်ာင္းေဆာင္အလွဴ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/199.mp3"><span style="color: #ffcc00;">ေက်ာင္းေဆာင္ေရစက္ခ်</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/039.mp3"><span style="color: #ffcc00;">ႀကီးပြားေၾကာင္းတရား(၇)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/064.mp3"><span style="color: #ffcc00;">ခုေရာေနာင္ပါခ်မ္းသာေစဖုိ႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/171.mp3"><span style="color: #ffcc00;">ခ်စ္ျခင္းမုန္းျခင္းလြတ္ေျမာက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/055.mp3"><span style="color: #ffcc00;">ခ်မ္းသာခ်င္ရင္စိတ္ကုိျပင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/028.mp3"><span style="color: #ffcc00;">ခ်မ္းသာေၾကာင္းတရား(၁၂)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/026.mp3"><span style="color: #ffcc00;">ခႏၶာေျမအုိး ကုသုိလ္ေရႊအုိး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/21-6-2016.mp3"><span style="color: #ffcc00;">ခႏၲီ (သို႔မဟုတ္) ျမင့္ျမတ္ေသာ အက်င့္ (၂၁.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/035.mp3"><span style="color: #ffcc00;">ေခါင္းေဆာင္ႀကီးႏွစ္ဦး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/02%20A%202012%208/A%2020121103%20ChaungNayThawYanThu%20ANuThaYa%20KyaikHto.mp3"><span style="color: #ffcc00;">ေျခာင္းေနေသာ ရန္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/132.mp3"><span style="color: #ffcc00;">ငါးပါး၌တည္ေလးပါးကုိပြား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/036.mp3"><span style="color: #ffcc00;">စကားတုိ႔၏အစြမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/184.mp3"><span style="color: #ffcc00;">စစ္မွန္ေသာ အားကုိးရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/033.mp3"><span style="color: #ffcc00;">စြန္႔နိင္သေလာက္ခ်မ္းသာမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/104.mp3"><span style="color: #ffcc00;">စိတၱသူႀကြယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/158.mp3"><span style="color: #ffcc00;">စိတ္၏ရန္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/03_09082016.mp3"><span style="color: #ffcc00;">စိတ္၏အစြမ္းႏွင့္သတိ၏အစြမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/06%20A%204/A%20SateToeEiThaBaw.mp3"><span style="color: #ffcc00;">စိတ္တို႔၏ သေဘာထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/037.mp3"><span style="color: #ffcc00;">စိတ္တုိ႔၏အစြမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/038.mp3"><span style="color: #ffcc00;">စိတ္ထားလွမွျမတ္နိးႀကသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/154.mp3"><span style="color: #ffcc00;">စိတ္မနာေအာင္ေနတက္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/107.mp3"><span style="color: #ffcc00;">စိတ္သာလွ်င္ပဓာန</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/054.mp3"><span style="color: #ffcc00;">စိတ္ေကာင္းထားမွခ်မ္းသာရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/050.mp3"><span style="color: #ffcc00;">ေစာင့္စည္းျခင္းသည္ေကာင္း၏</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/04_07082016.mp3"><span style="color: #ffcc00;">ဆင္းရဲအစခ်စ္ျခင္းက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/197.mp3"><span style="color: #ffcc00;">ဆြမ္းအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/18.mp3"><span style="color: #ffcc00;">ဆိုးသည္ျဖစ္ေစ ေကာင္းသည္ျဖစ္ေစ (ရန္ကုန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/153.mp3"><span style="color: #ffcc00;">ဆီခြက္(သုိ႔မဟုတ္)ကာယဂတာသတိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/113.mp3"><span style="color: #ffcc00;">ဆုတ္ယုတ္ေၾကာင္းႏွင့္ႀကီးပြားေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/018.mp3"><span style="color: #ffcc00;">ဆုိးသည္ျဖစ္ေစေကာင္းသည္ျဖစ္ေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/075.mp3"><span style="color: #ffcc00;">ေစ်းသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/053.mp3"><span style="color: #ffcc00;">ညီညြတ္မွခ်မ္းသာမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/112.mp3"><span style="color: #ffcc00;">တစ္ခုေသာတရား၏ဂုဏ္ေက်းဇူးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/172.mp3"><span style="color: #ffcc00;">တစ္ခုေသာတရားကုိေစာင့္ေရွာက္ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/021.mp3"><span style="color: #ffcc00;">တန္းဖုိးရွိတဲ့လူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/131.mp3"><span style="color: #ffcc00;">တန္းဖုိးရွိေသာတရားႏွင့္တန္းဖုိးမရွိေသာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/187.mp3"><span style="color: #ffcc00;">တရားအက်ဥ္း(၄)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/121.mp3"><span style="color: #ffcc00;">ေတာင္ထိပ္ေပၚကလူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/21-11-2015.mp3"><span style="color: #ffcc00;">ဒီတရားေတြကို ေျပာေပးပါ (၂၁.၁၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/027.mp3"><span style="color: #ffcc00;">ဒီဘက္ကမ္းႏွင့္ဟုိဘက္ကမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/084.mp3"><span style="color: #ffcc00;">ေဒါသပယ္ေၾကာင္းနည္းလမ္းေကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/179.mp3"><span style="color: #ffcc00;">ေဒါသမီးႏွင့္ေမတၱာေရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/10-6-2015.mp3"><span style="color: #ffcc00;">ဓနဥၨာနိသုတၱန္ (၁၀.၆.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/023.mp3"><span style="color: #ffcc00;">ဓမၼစြမ္းရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/060.mp3"><span style="color: #ffcc00;">နခသီခသုတၱဳန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/17.mp3"><span style="color: #ffcc00;">နိဗၺာန္ခရီးႏွင့္ အတားဆီးမ်ား (ရန္ကုန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/singapore-3-10-2015/151004_0012.MP3"><span style="color: #ffcc00;">နိဗၺာန္ပို႔မည့္ သညာမ်ား (၄.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/076.mp3"><span style="color: #ffcc00;">နႏၵေကာ၀ါဒသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/052.mp3"><span style="color: #ffcc00;">ေနာင္တေ၀း၍ေအးပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/173.mp3"><span style="color: #ffcc00;">ပညာဆုိတာရတနာပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/163.mp3"><span style="color: #ffcc00;">ပညာရွိဆုိသည္မွာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/189.mp3"><span style="color: #ffcc00;">ပညာရွိဆုိသည္မွာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/6-2015/19-6-2015.mp3"><span style="color: #ffcc00;">ပညာရွိတို႔၏ အရည္အခ်င္း (၃)မ်ဳိး (၁၉.၆.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/075.mp3"><span style="color: #ffcc00;">ပါပဏိကသုတၱန္ (ေစ်းသည္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/20-6-2016.mp3"><span style="color: #ffcc00;">ပါရမီ (သို႔မဟုတ္) ျမင့္ျမတ္ေသာ လုပ္ငန္း (၂၀.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/157.mp3"><span style="color: #ffcc00;">ပုေဏၰာ၀ါဒသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/125.mp3"><span style="color: #ffcc00;">ပူေသာမီးကုိၿငိမ္း၍လင္းေသာမီးကုိရွာပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/No-33/DVD%20Title%204.mp3"><span style="color: #ffcc00;">ေျပာမယံု ႀကံဳမွသိ (၁၆.၉.၂၀၁၄) မံုရြာၿမိဳ႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/159.mp3"><span style="color: #ffcc00;">ေျပာမယုံ ႀကံဳမွသိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/031.mp3"><span style="color: #ffcc00;">ဗကျဗဟၼာ၏ အတိတ္ဇာတ္လမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/6-2015/16-8-2015.mp3"><span style="color: #ffcc00;">ဗလသုတၱန္ (၁၆.၈.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/025.mp3"><span style="color: #ffcc00;">မ်ားစြားအက်ိဳးေက်းဇူးတရား(၄)ပါးတရားေတာ္ (ဗဟုကာရ သုတၱံ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/08%20B%202012%208/B%2020120722%20BuddhaCheeMoonKhanHtikeThu%20KyaukSe.mp3"><span style="color: #ffcc00;">ဗုဒၶခ်ီးမြန္းခံထိုက္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/09%20B%202011%205/B%2020110308%20BozZin%20Taunggoo.mp3"><span style="color: #ffcc00;">ေဗာဇၥ်င္သုတ္ (ေတာင္ငူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/192.mp3"><span style="color: #ffcc00;">ၿငိမ္းေအးစြာေနနည္းမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/057.mp3"><span style="color: #ffcc00;">ဘယ္လုိတုံ႔ျပန္ႀကမွာလဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/118.mp3"><span style="color: #ffcc00;">ဘာ၀နာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/128.mp3"><span style="color: #ffcc00;">ဘာ၀နာသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/074.mp3"><span style="color: #ffcc00;">ဘာကုိရွာေနႀကတာလဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/128.mp3"><span style="color: #ffcc00;">ဘာဝနာသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2016-SG/1B_06082016.mp3"><span style="color: #ffcc00;">ဘုရားသာသနာဆိုသည္မွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/030.mp3"><span style="color: #ffcc00;">ဘုရားေပးေသာဥပမာမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/089.mp3"><span style="color: #ffcc00;">ဘုရားေပးေသာဥပမာမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/101.mp3"><span style="color: #ffcc00;">ဘုရားႏွင့္နီးသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/10-7-2016.mp3"><span style="color: #ffcc00;">ေဘးကင္းရာ နယ္ေျမ (၁၀.၇.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/069.mp3"><span style="color: #ffcc00;">ေဘးမျဖစ္ေအာင္ေနပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/168.mp3"><span style="color: #ffcc00;">ေဘးမျဖစ္ေအာင္ေနပါ (ျမစ္ငယ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/NO142/01%20A%202014%2012/20140429%20MinGaLar%206%20YanKin.mp3"><span style="color: #ffcc00;">မဂၤသုတၱန္ (မဂၤလာတရားေတာ္) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/111.mp3"><span style="color: #ffcc00;">မထူးဇာတ္ခင္းသူမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/056.mp3"><span style="color: #ffcc00;">မၿငိမ္းခ်မ္းတာဘာေႀကာင့္လည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/174.mp3"><span style="color: #ffcc00;">မရဏႆတိကထာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/175.mp3"><span style="color: #ffcc00;">မဟာဒုကၡကၡႏၶသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/134.mp3"><span style="color: #ffcc00;">မဟာရာဟုေလာ၀ါဒသုတၱန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/085.mp3"><span style="color: #ffcc00;">မဟာသုတေသာမဇာတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/020.mp3"><span style="color: #ffcc00;">မဟာသုဒႆနသုတၱံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/103.mp3"><span style="color: #ffcc00;">မာဂ႑ိယသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/077.mp3"><span style="color: #ffcc00;">မိဘေက်းဇူးအထူးသိပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/123.mp3"><span style="color: #ffcc00;">မီး(၇)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/160.mp3"><span style="color: #ffcc00;">မေကာင္းမႈေရွာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/058.mp3"><span style="color: #ffcc00;">မွန္ႀကည့့္လုိက္ပါဦး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/029.mp3"><span style="color: #ffcc00;">ယဥ္ေက်းေသာစိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/162.mp3"><span style="color: #ffcc00;">ျဖဴေအာင္စိတ္ကုိထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/115.mp3"><span style="color: #ffcc00;">ျမင့္ျမတ္သူတုိ႔၏အေတြး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/singapore-3-10-2015/1-3.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးအမႏွင့္ သတိ၏ အစြမ္း (၃.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/043.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏၀ါဒႏွင့္ခ်ီးမြမ္းျခင္း(၂)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/044.mp3"><span style="color: #ffcc00;">ျမတ္ဘုရား၏စကား(၃)ခြန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/167.mp3"><span style="color: #ffcc00;">ေမတၱာရွိ၍သစၥာသိပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/198.mp3"><span style="color: #ffcc00;">ေမြးေန႔အလွဴ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/070.mp3"><span style="color: #ffcc00;">ေမဃိယသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/13.mp3"><span style="color: #ffcc00;">ရတနာထိုက္ေသာ စကား(၄)ခြန္း (ေမၿမိဳ႕)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/20091202%20YadanarHtikeThawSaGar4Khun%20TaungTwinGyi.mp3"><span style="color: #ffcc00;">ရတနာထိုက္ေသာ စကားေလးခြန္း (ေတာင္တြင္းႀကီး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/20091225%20YadanarHtikeThawSagar4Khun%20ShwePyiThar.mp3"><span style="color: #ffcc00;">ရတနာထိုက္ေသာ စကားေလးခြန္း (ေရႊျပည္သာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/57.mp3"><span style="color: #ffcc00;">ရတနာထို္က္ေသာ စကား(၄)ခြန္း (လမ္းမေတာ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/034.mp3"><span style="color: #ffcc00;">ရန္သူ႕အႀကိဳက္လုိက္ႀကမွာလား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/140.mp3"><span style="color: #ffcc00;">ရဟန္းပ်င္းႏွင့္ ရြဲကုန္သည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/185.mp3"><span style="color: #ffcc00;">ရူပနႏၵာေထရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/170.mp3"><span style="color: #ffcc00;">ရဲရင့္ေသာျမတ္ဘုရား၏အံ့ဖြယ္ေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/059.mp3"><span style="color: #ffcc00;">ရႏုိင္ခဲေသာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/08%20B%202012%208/B%2020120321%20ShinSuLaPan%20North%20Okkalapa.mp3"><span style="color: #ffcc00;">ရွင္စူဠပန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/09%20B%202011%205/B%2020111124%20ShinRaHtaParLa%20North%20Okkalapa.mp3"><span style="color: #ffcc00;">ရွင္ရဠပါလ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/040.mp3"><span style="color: #ffcc00;">ရွင္ရာဟုလာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/019.mp3"><span style="color: #ffcc00;">ရွိဖုိ႔ထက္သိဖုိ႔ကအေရးႀကီးသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/152.mp3"><span style="color: #ffcc00;">ေရေသာက္ျမစ္ </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/180.mp3"><span style="color: #ffcc00;">ေရွာင္လႊဲ၍မရေသာအရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/No-33/DVD%20Title%201.mp3"><span style="color: #ffcc00;">လံု႔လဟူသည္ (၁၄.၉.၂၀၁၄) မံုရြာၿမိဳ႕</span></a></p>
<p><a href="https://https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/060.mp3"><span style="color: #ffcc00;">လက္သည္းေပၚမွေျမမုန္႔မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/12-6-2015.mp3"><span style="color: #ffcc00;">လြတ္ေျမာက္မွ ခ်မ္းသာရ (၁၂.၆.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/061.mp3"><span style="color: #ffcc00;">လြန္ကဲေသာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/156.mp3"><span style="color: #ffcc00;">လုံးလဟူသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/188.mp3"><span style="color: #ffcc00;">လူဆင္းရဲႏွင့္လူခ်မ္းသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/182.mp3"><span style="color: #ffcc00;">လူမုိက္ႏွင့္ပညာရွိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/079.mp3"><span style="color: #ffcc00;">လႊ – ဥပမာ (ဇမၺဴသီရိ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/03%20A%202011%2039/A%2020111123%20LayParChanTharYaAungShar%20MaYanGone.mp3"><span style="color: #ffcc00;">ေလးပါးခ်မ္းသာရေအာင္ရွာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/08%20B%202012%208/B%2020120829%204ParChanTharYaAungShar%20TharZi.mp3"><span style="color: #ffcc00;">ေလးပါးခ်မ္းသာရေအာင္ရွာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/071.mp3"><span style="color: #ffcc00;">ေလာကကုိတင့္တယ္ေစသူမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/102.mp3"><span style="color: #ffcc00;">ေလာကဓံတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/015.mp3"><span style="color: #ffcc00;">ေလာဘသေဘာႏွင့္ေကာင္းမွုအက်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/062.mp3"><span style="color: #ffcc00;">၀ိပလႅာသသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/022.mp3"><span style="color: #ffcc00;">၀ု႒ိသုတၱံတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/048.mp3"><span style="color: #ffcc00;">ေ၀လာမသုတၱံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/20-4-2015.mp3"><span style="color: #ffcc00;">သံသရာခရီးသြား လမ္းမမွားဖို႔လိုသည္ (၂၀.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/056.mp3"><span style="color: #ffcc00;">သကၠပညာ့သုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/126.mp3"><span style="color: #ffcc00;">သခၤါရတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/22-4-2015.mp3"><span style="color: #ffcc00;">သင္မွတတ္မည္ က်င့္မွျမတ္မည္ (၂၂.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/20110906%20Parami%204.mp3"><span style="color: #ffcc00;">သစၥာ ႏွင့္ အဓိဌာန္ပါရမီ (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/080.mp3"><span style="color: #ffcc00;">သစၥာသိဘုိ႔အေရးႀကီးဆုံံး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/081.mp3"><span style="color: #ffcc00;">သစၥာေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/186.mp3"><span style="color: #ffcc00;">သတိ(သုိ႔)စိတ္၏အေစာင့္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/20090902%20ThaDiNeltPyawSateKoSauntLutAungYone.mp3"><span style="color: #ffcc00;">သတိနဲ႔ေျပာ စိတ္ကိုေစာင့္ လြတ္ေအာင္ရံုး တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/21-4-2015.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္ (သို႔မဟုတ္) တစ္ေၾကာင္းတည္းေသာလမ္း (၂၁.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/032.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္ဂုဏ္ရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/010.mp3"><span style="color: #ffcc00;">သတိႏွင့္ေပ်ာ္ စိတ္ကုိေစာင့္ လြတ္ေအာင္ရုန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/016.mp3"><span style="color: #ffcc00;">သန္႔ရွင္းေသာစိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/19-6-2016.mp3"><span style="color: #ffcc00;">သမၼာဒိ႒ိ (သို႔မဟုတ္) မွန္ကန္ေသာ အျမင္ (၁၉.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/063.mp3"><span style="color: #ffcc00;">သမုဒၵရာမ်ားကုိကူးၿပီးသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/200.mp3"><span style="color: #ffcc00;">သိမ္ေရစက္ခ်</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/117.mp3"><span style="color: #ffcc00;">သီလ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/011.mp3"><span style="color: #ffcc00;">သီဟနာဒသုတၱံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Z%2020090402%20ThuKha12Par%20AungLan.mp3"><span style="color: #ffcc00;">သုခ (၁၂)ပါး (ေအာင္လံ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/006.mp3"><span style="color: #ffcc00;">သူ႕အေၾကာင္း ကုိယ့္အေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/073.mp3"><span style="color: #ffcc00;">ေသခ်ာေသာလမ္းကုိေလွ်ာက္ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/22-6-2016.mp3"><span style="color: #ffcc00;">ေသျခင္း (သို႔မဟုတ္) အၿမဲမျပတ္ ေအာက္ေမ့အပ္ေသာ အရာ (၂၂.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/124.mp3"><span style="color: #ffcc00;">ေသာတပန္ဂုဏ္ရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/181.mp3"><span style="color: #ffcc00;">အကာအကြယ္အေစာင့္အေရွာက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/176.mp3"><span style="color: #ffcc00;">အက်ိဳးမဲ့ျခင္းႏွင့္ အက်ိဳးရွိျခင္း၏အေၾကာင္းတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/193.mp3"><span style="color: #ffcc00;">အက်ိဳးမ်ားေသာ သတိ(၁၀)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/105.mp3"><span style="color: #ffcc00;">အခြင့္သာတုန္းလြတ္ေအာင္ရုန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/08%20B%202012%208/B%2020121130%20AKhuYawNaungParChanTharSayPhoe%20MaYanGone.mp3"><span style="color: #ffcc00;">အခုေရာ ေနာင္ပါ ခ်မ္းသာေစဖို႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/177.mp3"><span style="color: #ffcc00;">အဂၢိသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/114.mp3"><span style="color: #ffcc00;">အစြမ္းထက္ေသာအေတြးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/130.mp3"><span style="color: #ffcc00;">အဆုံးမရွိေသာရွာေဖြျခင္းမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/014.mp3"><span style="color: #ffcc00;">အဆုိးဆုံးရန္သူႏွင့္အေကာင္းဆုံးမိတ္ေဆြ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/087.mp3"><span style="color: #ffcc00;">အဆုိးဆုံးရန္သူႏွင့္အေကာင္းဆုံးမိတ္ေဆြ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/091.mp3"><span style="color: #ffcc00;">အဆုိးဆုံးရန္သူႏွင့္အေကာင္းဆုံးမိတ္ေဆြ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/127.mp3"><span style="color: #ffcc00;">အတြင္းအျပင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/045.mp3"><span style="color: #ffcc00;">အနာထပိဏ္ႏွင့္ကံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/165.mp3"><span style="color: #ffcc00;">အပူဆုံးမီးႏွင့္အႀကီးဆုံးအျပစ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/065.mp3"><span style="color: #ffcc00;">အဘိဏၰသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/29-6-2016.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုး ကုသိုလ္ (၂၉.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/057.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုး တရားအလွဴ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/119.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုးေသာ ရွင္သန္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/120.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံး(၄)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/122.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံး(၆)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/072.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးစကားႏွင့္အျမတ္ဆုံးေအာင္နိင့့္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/169.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/119.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးေသာရွင္သန္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/083.mp3"><span style="color: #ffcc00;">အရုိးဆုံးႏွင့္အေကာင္းဆုံးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/042.mp3"><span style="color: #ffcc00;">အရွင္စူဠပန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/041.mp3"><span style="color: #ffcc00;">အရွင္ရ႒ပါလ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/012.mp3"><span style="color: #ffcc00;">အလြယ္မက္ရင္ အခက္ႀကံဳမယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/20110124%20AThiNeltNayTarAKaungSone%20SouthOkkalapa.mp3"><span style="color: #ffcc00;">အသိနဲ႔ေနတာ အေကာင္းဆံုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/066.mp3"><span style="color: #ffcc00;">အသိဥာဏ္၏ဂုဏ္ေက်းဇူး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/6-2015/21-6-2015.mp3"><span style="color: #ffcc00;">အားကိုးရာအမွတ္ သတိပ႒ာန္ (၂၁.၆.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/109.mp3"><span style="color: #ffcc00;">အားကုိးရာကိုဘယ္လုိရွာမလဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/008.mp3"><span style="color: #ffcc00;">အားကုိးရာလားရန္သူလား (ရန္ကုန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/090.mp3"><span style="color: #ffcc00;">အားကုိးရာလားရန္သူလား (ဇလြန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/110.mp3"><span style="color: #ffcc00;">အားရွိမွေဘးလြတ္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/151.mp3"><span style="color: #ffcc00;">အားလုံးကုိလႊတ္လုိက္ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/066.mp3"><span style="color: #ffcc00;">အားေပးစကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/183.mp3"><span style="color: #ffcc00;">အာရကၡသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/078.mp3"><span style="color: #ffcc00;">အာသ၀သုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/12%20C%203/C%20ArThaWaPalKyaungNeeLanKaungMyar%20ThanLyin.mp3"><span style="color: #ffcc00;">အာသဝပယ္ေၾကာင္းနည္းလမ္းေကာင္းမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/191.mp3"><span style="color: #ffcc00;">အုိသည့္တုိင္ေအာင္ေကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/108.mp3"><span style="color: #ffcc00;">အေကာင္းဆုံးေဆး အေကာင္းဆုံးေရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/046.mp3"><span style="color: #ffcc00;">အေမးေလးေထြအေျဖေလးပါး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/093.mp3"><span style="color: #ffcc00;">အေမးေလးေထြအေျဖေလးပါး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/067.mp3"><span style="color: #ffcc00;">အေျခအေနမွန္ကုိမေမ့ပါနဲ႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/6-2015/20-6-2015.mp3"><span style="color: #ffcc00;">အေသေကာင္းဖို႔ အေသလြတ္ဖို႔ (၂၀.၆.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/2015_2016/11-6-2015.mp3"><span style="color: #ffcc00;">အေသေကာင္းဖို႔ႏွင့္ အေသလြတ္ဖို႔ (၁၁.၆.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/11%20B%203/B%20ANuMarNaSutta%2020121216%20LanMaDaw.mp3"><span style="color: #ffcc00;">အႏုမာန သုတၱန္ (မံုရြာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/058.mp3"><span style="color: #ffcc00;">အႏုမာန သုတၱန္ (ရန္ကုန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/068.mp3"><span style="color: #ffcc00;">အႏုသယ(သုိ႔မဟုတ္)ေခ်ာင္းေနေသာရန္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/RADIOEDIT.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (သစၥာပါရမီ online ေရဒီယို (၂) ျပည့္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/3DAY441THITSARSHWESI2017EDIT/MP3/THITSARSHWESISAYARDAW.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၃-ရက္တရားစခန္း -စကၤာပူ စခန္းသိမ္းပြဲ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/194.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/195.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/03%20A%202011%2039/A%2020110129%20ANuMawDaNar%20PaBeDan.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ပန္ပဲတန္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayartaw%20%283%29/03%20A%202011%2039/A%2020111127%20ANuMawDaNar%20Taunggoo.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေတာင္ငူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/106.mp3"><span style="color: #ffcc00;">အႏွစ္(၃)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/NO142/01%20A%202014%2012/20140105%20AHnit3Par%20Insein.mp3"><span style="color: #ffcc00;">အႏွစ္သံုးပါး (၅.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/178.mp3"><span style="color: #ffcc00;">အႏွစ္သုံးပါးႏွင့္ဆႏၵေျခာက္ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/Tayarwaw%20%282%29/P2/059.mp3"><span style="color: #ffcc00;">ဣထဓမၼသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/024.mp3"><span style="color: #ffcc00;">ဥပမာ(၉)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/051.mp3"><span style="color: #ffcc00;">ဧည့္သည္ႏွင့္တူေသာအရာမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/UOttama%20ThitSarShweSi/200/092.mp3"><span style="color: #ffcc00;">ဧည့္သည္ႏွင့္တူေသာအရာမ်ား (၂)</span></a></p>
    
"""

soup = bs4(text, 'html.parser')


with open('titles_links.txt', 'w') as f:
    count = 1
    for key in soup.find_all('a'):
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
            #f.write('{}\n'.format(key.get_text()))
            count += 1
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