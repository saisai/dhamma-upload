from bs4 import BeautifulSoup as bs4

text = """<div id="page-17149" class="elements-box post-17149 page type-page status-publish has-post-thumbnail hentry">
<h5><span style="color: #339966;">အဂၢမဟာကမၼ႒ာနာစရိယ၊ အဂၢမဟာသဒၶမေဇာတိကဓဇ</span></h5>
<h5><span style="color: #339966;">မဟာစည္နာယက၊ ျပည္တြင္းျပည္ပ သာသနာျပဳ ေရႊမင္းဝံဆရာေတာ္ဘုရားႀကီး ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား စုစည္းမႈ (MP3)</span></h5>
<h5><span style="color: #33cccc;">စုစည္းထားေသာ အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/203.mp3"><span style="color: #ffcc00;">၁။ ( ၃ )ပါးစံုမွ ပိုေကာင္းလွ (သာဓုသုတၱံ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/153.mp3"><span style="color: #ffcc00;">၂။ ( ၅၂၈ )သြယ္ ေမတၱာ (ေမတၱသုတၱံ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/222.mp3"><span style="color: #ffcc00;">၃။ ( ၆၆ ) ႏွစ္ေျမာက္ ေမြးေန႔ပူေဇာ္ပြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/64.mp3"><span style="color: #ffcc00;">၄။ (၁၁) မီးၿငိမ္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/166.mp3"><span style="color: #ffcc00;">၅။ (၃၈) ျဖာ မဂၤလာ (မာတာပိတုဥပ႒ာနံ) တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/158.mp3"><span style="color: #ffcc00;">၆။ ကဆုန္လျပည္႔ ဗုဒၶေန႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/85.mp3"><span style="color: #ffcc00;">၇။ ကာလသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/145.mp3"><span style="color: #ffcc00;">၈။ ကိုယ္႔ကိုခ်စ္ရင္ ကိုယ္ျပဳျပင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/191.mp3"><span style="color: #ffcc00;">၉။ ကိုယ္႔ကိုခ်စ္ရင္ ကိုယ္ျပဳျပင္ (၂ ၀၁၃ -သႀကၤန္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/140.mp3"><span style="color: #ffcc00;">၁၀။ ကိုယ္႔အားကိုယ္႔ကိုး လူ႔တန္ဘိုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/61.mp3"><span style="color: #ffcc00;">၁၁။ ကိုယ္႔အားကုိယ္ကိုး လူ႔တန္ဘိုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/141.mp3"><span style="color: #ffcc00;">၁၂။ ကုသိုလ္အျမတ္ယူတတ္ပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/149.mp3"><span style="color: #ffcc00;">၁၃။ က်ိဳး ( ၅ ) ပါးပိုင္ ဒါနကိုင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/121.mp3"><span style="color: #ffcc00;">၁၄။ ေကာင္းျခင္းေလးျဖာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/217.mp3"><span style="color: #ffcc00;">၁၅။ ေက်းဇူးဂုဏ္အင္ ဆပ္ေစခ်င္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/195.mp3"><span style="color: #ffcc00;">၁၆။ ေက်းဇူးရွိက ဆပ္ေပးရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/134.mp3"><span style="color: #ffcc00;">၁၇။ ခုေရာ ေနာင္ပါ ၿမဲဝမ္းသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/187.mp3"><span style="color: #ffcc00;">၁၈။ စိတ္ကိုဆံုးမ နိဗၺာန္ရ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/188.mp3"><span style="color: #ffcc00;">၁၉။ စိတ္ကိုဆံုးမ နိဗၺာန္ရ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/184.mp3"><span style="color: #ffcc00;">၂၀။ စိတ္ကိုျပဳျပင္ နိဗၺာန္ဝင္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/185.mp3"><span style="color: #ffcc00;">၂၁။ စိတ္ကိုျပဳျပင္ နိဗၺာန္ဝင္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/186.mp3"><span style="color: #ffcc00;">၂၂။ စိတ္ကိုျပဳျပင္ နိဗၺာန္ဝင္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/136.mp3"><span style="color: #ffcc00;">၂၃။ စူ႒သုတေသာမဇတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/135.mp3"><span style="color: #ffcc00;">၂၄။ ဆင္းရဲကင္းေဝး ခ်မ္းသာေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/220.mp3"><span style="color: #ffcc00;">၂၅။ ဆင္းရဲကင္းေဝး ခ်မ္းသာေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/86.mp3"><span style="color: #ffcc00;">၂၆။ ဆဆကၠသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/147.mp3"><span style="color: #ffcc00;">၂၇။ ဆရာ႔ေက်းဇူး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/67.mp3"><span style="color: #ffcc00;">၂၈။ တရားနဲ႔သာ ပူေဇာ္ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/81.mp3"><span style="color: #ffcc00;">၂၉။ တရားရျခင္း ( ၅ )ပါး -၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/82.mp3"><span style="color: #ffcc00;">၃၀။ တရားရျခင္း ( ၅ )ပါး -၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/83.mp3"><span style="color: #ffcc00;">၃၁။ တရားရျခင္း ( ၅ )ပါး -၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/84.mp3"><span style="color: #ffcc00;">၃၂။ တရားရျခင္း ( ၅ )ပါး -၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/180.mp3"><span style="color: #ffcc00;">၃၃။ တရားရႈနည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/182.mp3"><span style="color: #ffcc00;">၃၄။ တရားရႏိုင္တဲ႔ အခြင္႔အခါေကာင္း ( ၄ )မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/196.mp3"><span style="color: #ffcc00;">၃၅။ တရားအားထုတ္တဲ႔ ပုဂၢိဳလ္ဆိုတာ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/197.mp3"><span style="color: #ffcc00;">၃၆။ တရားအားထုတ္တဲ႔ ပုဂၢိဳလ္ဆိုတာ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/181.mp3"><span style="color: #ffcc00;">၃၇။ တရားအားထုတ္ရမယ္႔အခ်ိန္အခါ ( ၅ )မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/190.mp3"><span style="color: #ffcc00;">၃၈။ တရားအားထုတ္ရမယ္႔အခ်ိန္အခါ ( ၅ )မ်ိဳး ( ၂၀၁၃-သႀကၤန္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/127.mp3"><span style="color: #ffcc00;">၃၉။ တရားအားထုတ္သူ ျပည္႔စံုရမည္႔ အရည္အခ်င္း ( ၅ )မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/177.mp3"><span style="color: #ffcc00;">၄၀။ တရားေစာင္႔မွ ခ်မ္းသာရ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/178.mp3"><span style="color: #ffcc00;">၄၁။ တရားေစာင္႔မွ ခ်မ္းသာရ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/151.mp3"><span style="color: #ffcc00;">၄၂။ တားမရေသာ ေဘးႀကီး (၄)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/174.mp3"><span style="color: #ffcc00;">၄၃။ တိုက္ပြဲဝင္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/169.mp3"><span style="color: #ffcc00;">၄၄။ တေယာဇနဝတၳဳ (ကံတရားသည္သာ ကိုယ္ပိုင္ဥစၥာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/129.mp3"><span style="color: #ffcc00;">၄၅။ ဒါနကထာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/41.mp3"><span style="color: #ffcc00;">၄၆။ ဒါရုကၡေႏၶာပမသုတၱန္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/42.mp3"><span style="color: #ffcc00;">၄၇။ ဒါရုကၡေႏၶာပမသုတၱန္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/43.mp3"><span style="color: #ffcc00;">၄၈။ ဒါရုကၡေႏၶာပမသုတၱန္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/44.mp3"><span style="color: #ffcc00;">၄၉။ ဒါရုကၡေႏၶာပမသုတၱန္ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/194.mp3"><span style="color: #ffcc00;">၅၀။ ဒါရုဋိကပုတၱဝတၳဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/148.mp3"><span style="color: #ffcc00;">၅၁။ ဒိ႒ိပယ္ခြာေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/183.mp3"><span style="color: #ffcc00;">၅၂။ ဓမၼ အပၸမာဒမဂၤလာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/80.mp3"><span style="color: #ffcc00;">၅၃။ ဓမၼပီတိ / ဓမၼရသ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/167.mp3"><span style="color: #ffcc00;">၅၄။ နိဗၺာနသညာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/144.mp3"><span style="color: #ffcc00;">၅၅။ နႏၵေတၳရ ဝတၳဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/168.mp3"><span style="color: #ffcc00;">၅၆။ ႏွစ္သစ္မဂၤလာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/192.mp3"><span style="color: #ffcc00;">၅၇။ ႏွစ္သစ္မဂၤလာ ( အႏွစ္-၄ပါး )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/62.mp3"><span style="color: #ffcc00;">၅၈။ ႏွစ္သစ္မဂၤလာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/137.mp3"><span style="color: #ffcc00;">၅၉။ ပညာဘာဝနာျပည္႔စံုမွ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/122.mp3"><span style="color: #ffcc00;">၆၀။ ပဥၥဂၢဒါယကျဗဟၼဏဝတၳဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/253.mp3"><span style="color: #ffcc00;">၆၁။ ပဥၥဘိကၡဳဝတၳဳ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/254.mp3"><span style="color: #ffcc00;">၆၂။ ပဥၥဘိကၡဳဝတၳဳ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/255.mp3"><span style="color: #ffcc00;">၆၃။ ပဥၥဘိကၡဳဝတၳဳ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/116.mp3"><span style="color: #ffcc00;">၆၄။ ပါရမီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/202.mp3"><span style="color: #ffcc00;">၆၅။ ပုဂၢိဳလ္ ( ၃ )မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/179.mp3"><span style="color: #ffcc00;">၆၆။ ပုဂၢိဳလ္ ( ၄ ) မ်ိိဳး (ပုဂၢသုတၱံ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/78.mp3"><span style="color: #ffcc00;">၆၇။ ပုဂၢိဳလ္ ( ၄ ) မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/157.mp3"><span style="color: #ffcc00;">၆၈။ ေပသကာရေဒတုဝတၱဳ (ရက္ကန္းသည္ သမီး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/163.mp3"><span style="color: #ffcc00;">၆၉။ ဗဟုကာရသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/156.mp3"><span style="color: #ffcc00;">၆၀။ ဗဟုပုတၱိကေထရီ (သားသမီးမ်ားေသာ ေထရီ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/139.mp3"><span style="color: #ffcc00;">၇၀။ ဗိလာလပါဒကေသ႒ိဝတၱဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/162.mp3"><span style="color: #ffcc00;">၇၂။ ဘဝ တာဝန္ ေက်ပြန္ပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/218.mp3"><span style="color: #ffcc00;">၇၃။ ဘဝ တာဝန္ ေက်ပြန္ပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/219.mp3"><span style="color: #ffcc00;">၇၄။ ဘဝ တာဝန္ ေက်ပြန္ပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/161.mp3"><span style="color: #ffcc00;">၇၅။ ဘဝတန္ဘိုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/251.mp3"><span style="color: #ffcc00;">၇၆။ ဘာဝနာသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/200.mp3"><span style="color: #ffcc00;">၇၇။ ဘုရားရွင္၏ အာမခံခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/262.mp3"><span style="color: #ffcc00;">၇၈။ မဆုတ္ယုတ္ေၾကာင္း ( ၄ )ပါး-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/263.mp3"><span style="color: #ffcc00;">၇၉။ မဆုတ္ယုတ္ေၾကာင္း ( ၄ )ပါး-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/77.mp3"><span style="color: #ffcc00;">၈၀။ မဟာကပၸိဏေထရသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/165.mp3"><span style="color: #ffcc00;">၈၁။ မဟာဓနဝါဏိစၥ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/66.mp3"><span style="color: #ffcc00;">၈၂။ မဟာေဂါသဂၤသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/88.mp3"><span style="color: #ffcc00;">၈၃။ မအို မနာ မေသမႈတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/89.mp3"><span style="color: #ffcc00;">၈၄။ မာဂဏီယ သုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/143.mp3"><span style="color: #ffcc00;">၈၅။ မိမိသည္သာ အားကိုးရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/150.mp3"><span style="color: #ffcc00;">၈၆။ မိုးႏွင္႔တူေသာ ပုဂၢိဳလ္ ( ၄ )မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/22.mp3"><span style="color: #ffcc00;">၈၇။ ျဗဟၼာ႔ဝိဟာရ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/23.mp3"><span style="color: #ffcc00;">၈၈။ ျဗဟၼာ႔ဝိဟာရ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/154.mp3"><span style="color: #ffcc00;">၈၉။ ျမတ္ေသာေနထိုင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/260.mp3"><span style="color: #ffcc00;">၉၀။ ျမတ္ေသာေနထိုင္ျခင္း ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/261.mp3"><span style="color: #ffcc00;">၉၁။ ျမတ္ေသာေနထိုင္ျခင္း ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/249.mp3"><span style="color: #ffcc00;">၉၂။ ေမတၱသုတၱံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/250.mp3"><span style="color: #ffcc00;">၉၃။ ေမတၱာအခါေတာ္ေန႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/69.mp3"><span style="color: #ffcc00;">၉၄။ ေယာဂီက်င္႔ဖြယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/138.mp3"><span style="color: #ffcc00;">၉၅။ ရခဲျခင္းတရား ( ၄ ) ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/221.mp3"><span style="color: #ffcc00;">၉၆။ ရခဲျခင္းတရား ေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/146.mp3"><span style="color: #ffcc00;">၉၇။ ေရာဟိတႆသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/29.mp3"><span style="color: #ffcc00;">၉၈။ ေရႊမင္းဝံ ရိပ္သာမိသားစုမ်ားအေပၚေက်းဇူးဆပ္၊ တိုက္တြန္း တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/176.mp3"><span style="color: #ffcc00;">၉၉။ လံုၿခံဳေရးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/131.mp3"><span style="color: #ffcc00;">၁၀၀။ လွ်င္ျမန္တဲ႔ဟသၤာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/142.mp3"><span style="color: #ffcc00;">၁၀၁။ လိုတာလွဴက လိုျပည္႔ဝ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/252.mp3"><span style="color: #ffcc00;">၁၀၂။ လူ႔ဘဝဂုဏ္ရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/164.mp3"><span style="color: #ffcc00;">၁၀၃။ ေလးျဖာခ်မ္းသာ ေရြးခ်ယ္ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/65.mp3"><span style="color: #ffcc00;">၁၀၄။ ေလာကႀကီးဟာ သင္႔ဆရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/133.mp3"><span style="color: #ffcc00;">၁၀၅။ ဝန္ထုတ္ဝန္ပိုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/52.mp3"><span style="color: #ffcc00;">၁၀၆။ ဝမၼိကသုတ္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/53.mp3"><span style="color: #ffcc00;">၁၀၇။ ဝမၼိကသုတ္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/54.mp3"><span style="color: #ffcc00;">၁၀၈။ ဝမၼိကသုတ္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/55.mp3"><span style="color: #ffcc00;">၁၀၉။ ဝမၼိကသုတ္ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/119.mp3"><span style="color: #ffcc00;">၁၁၀။ ဝါဆိုလျပည္႔ ဓမၼစၾကာအခါေတာ္ေန႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/24.mp3"><span style="color: #ffcc00;">၁၁၁။ ဝိပႆနာဂုဏ္ရည္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/25.mp3"><span style="color: #ffcc00;">၁၁၂။ ဝိပႆနာဂုဏ္ရည္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/26.mp3"><span style="color: #ffcc00;">၁၁၃။ ဝိပႆနာဂုဏ္ရည္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/27.mp3"><span style="color: #ffcc00;">၁၁၄။ ဝိပႆနာဂုဏ္ရည္ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/128.mp3"><span style="color: #ffcc00;">၁၁၅။ ဝိပႆနာညစ္ညဴးေၾကာင္း ( ၁၀ )ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/264.mp3"><span style="color: #ffcc00;">၁၁၆။ ဝိပႆနာရႈနည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/199.mp3"><span style="color: #ffcc00;">၁၁၇။ ဝိပႆနာသမၼဒိ႒ိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/68.mp3"><span style="color: #ffcc00;">၁၁၈။ သကၠပဥၥသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/204.mp3"><span style="color: #ffcc00;">၁၁၉။ သကၤန္းလွဴက်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/90.mp3"><span style="color: #ffcc00;">၁၂၀။ သကၤန္းလွဴက်ိဳး အမ်ိဳးမ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/87.mp3"><span style="color: #ffcc00;">၁၂၁။ သတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/30.mp3"><span style="color: #ffcc00;">၁၂၂။ သတိပ႒ာန္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/31.mp3"><span style="color: #ffcc00;">၁၂၃။ သတိပ႒ာန္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/32.mp3"><span style="color: #ffcc00;">၁၂၄။ သတိပ႒ာန္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/33.mp3"><span style="color: #ffcc00;">၁၂၅။ သတိပ႒ာန္ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/265.mp3"><span style="color: #ffcc00;">၁၂၆။ သတိပ႒ာန္ဂုဏ္ရည္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/126.mp3"><span style="color: #ffcc00;">၁၂၇။ သတိပ႒ာန္ရႈတာ ဘယ္သူ႔အတြက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/125.mp3"><span style="color: #ffcc00;">၁၂၈။ သတိပ႒ာန္ရႈနည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/123.mp3"><span style="color: #ffcc00;">၁၂၉။ သတိပ႒ာန္အက်ဥ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/124.mp3"><span style="color: #ffcc00;">၁၃၀။ သတိပ႒ာန္အက်ိဳး ( ၇ )မ်ိဳးအက်ဥ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/117.mp3"><span style="color: #ffcc00;">၁၃၁။ သတိပ႒ာန္ေလးပါး ရႈပြားပံု ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/118.mp3"><span style="color: #ffcc00;">၁၃၂။ သတိပ႒ာန္ေလးပါး ရႈပြားပံု ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/257.mp3"><span style="color: #ffcc00;">၁၃၃။ သတိပ႒ာန္ေလးပါးရႈမွတ္ၿပီး ရရွိႏိုင္ေသာဥာဏ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/258.mp3"><span style="color: #ffcc00;">၁၃၄။ သတိပ႒ာန္ေလးပါးရႈမွတ္ၿပီး ရရွိႏိုင္ေသာဥာဏ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/259.mp3"><span style="color: #ffcc00;">၁၃၅။ သတိပ႒ာန္ေလးပါးရႈမွတ္ၿပီး ရရွိႏိုင္ေသာဥာဏ္ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/152.mp3"><span style="color: #ffcc00;">၁၃၆။ သတိပ႒ာန္ေဟာၾကားရာေနရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/170.mp3"><span style="color: #ffcc00;">၁၃၇။ သတိေပးတိုက္တြန္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/38.mp3"><span style="color: #ffcc00;">၁၃၈။ သပၸဇဥ္ရႈမွတ္ပံု ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/39.mp3"><span style="color: #ffcc00;">၁၃၉။ သပၸဇဥ္ရႈမွတ္ပံု ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/40.mp3"><span style="color: #ffcc00;">၁၄၀။ သပၸဇဥ္ရႈမွတ္ပံု ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/159.mp3"><span style="color: #ffcc00;">၁၄၁။ သမထ ႏွင္႔ ဝိပႆနာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/189.mp3"><span style="color: #ffcc00;">၁၄၂။ သမထႏွင္႔ ဝိပႆနာ ( ၂၀၁၃ – သႀကၤန္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/175.mp3"><span style="color: #ffcc00;">၁၄၃။ သမယသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/79.mp3"><span style="color: #ffcc00;">၁၄၄။ သာသနာ႔ႏုဂၢဟ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/256.mp3"><span style="color: #ffcc00;">၁၄၅။ သီလဝႏၱသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/201.mp3"><span style="color: #ffcc00;">၁၄၆။ သူေတာ္ဥစၥာ ( ၇ )ျဖာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/63.mp3"><span style="color: #ffcc00;">၁၄၇။ သူေတာ္ေကာင္း လကၡဏာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/130.mp3"><span style="color: #ffcc00;">၁၄၈။ ေသမင္းကိုမေၾကာက္ရန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/58.mp3"><span style="color: #ffcc00;">၁၄၉။ ေသာတာပန္ ပယ္ရမည္႔ ကိေလသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/28.mp3"><span style="color: #ffcc00;">၁၅၀။ ေသာတာပန္ ပယ္ရမည္႔သံေယာဇဥ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/56.mp3"><span style="color: #ffcc00;">၁၅၁။ ေသာတာပန္ျဖစ္ျခင္း အေၾကာင္း ( ၄ )ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/171.mp3"><span style="color: #ffcc00;">၁၅၂။ ေသာတာပန္ျဖစ္ရန္ ေၾကာင္းေလးတန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/172.mp3"><span style="color: #ffcc00;">၁၅၃။ ေသာတာပန္ျဖစ္ရန္ ေၾကာင္းေလးတန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/57.mp3"><span style="color: #ffcc00;">၁၅၄။ ေသာတာပန္အဂၤါ ( ၄ )ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/160.mp3"><span style="color: #ffcc00;">၁၅၅။ အခ်ိန္ရွိခိုက္ လံု႔လစိုက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/173.mp3"><span style="color: #ffcc00;">၁၅၆။ အဂၢိဒတၱပုဏၰားဝတၳဳ (အားေပးစကား)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/216.mp3"><span style="color: #ffcc00;">၁၅၇။ အမွန္တရား ( ၄ )ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/198.mp3"><span style="color: #ffcc00;">၁၅၈။ အျမင္႔ျမတ္ဆံုး တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/132.mp3"><span style="color: #ffcc00;">၁၅၉။ အရြယ္ ( ၁၀ )ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/155.mp3"><span style="color: #ffcc00;">၁၆၀။ အရိပ္ခ်မ္းသာ (ေလာကနီတိ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/120.mp3"><span style="color: #ffcc00;">၁၆၁။ အားထုတ္နည္းေလးရသြားပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/110.mp3"><span style="color: #ffcc00;">၁၆၂။ အႏုဂၢဟိတသုတၱံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/34.mp3"><span style="color: #ffcc00;">၁၆၃။ ဣရိယာပထ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/59.mp3"><span style="color: #ffcc00;">၁၆၄။ ဣရိယာပထ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/35.mp3"><span style="color: #ffcc00;">၁၆၅။ ဣရိယာပထ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/60.mp3"><span style="color: #ffcc00;">၁၆၆။ ဣရိယာပထ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/36.mp3"><span style="color: #ffcc00;">၁၆၇။ ဣရိယာပထ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/37.mp3"><span style="color: #ffcc00;">၁၆၈။ ဣရိယာပထ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/193.mp3"><span style="color: #ffcc00;">၁၆၉။ ဥပါသကာဂုဏ္ရည္</span></a></p>
<h5><span style="color: #33cccc;">မ်က္ေမွာက္ခ်မ္းသာေရး တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/210.mp3"><span style="color: #ffcc00;">၁၇၀။ မ်က္ေမွာက္ခ်မ္းသာေရး ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/211.mp3"><span style="color: #ffcc00;">၁၇၁။ မ်က္ေမွာက္ခ်မ္းသာေရး ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/212.mp3"><span style="color: #ffcc00;">၁၇၂။ မ်က္ေမွာက္ခ်မ္းသာေရး ( ၃ ) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/213.mp3"><span style="color: #ffcc00;">၁၇၃။ မ်က္ေမွာက္ခ်မ္းသာေရး ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/214.mp3"><span style="color: #ffcc00;">၁၇၄။ မ်က္ေမွာက္ခ်မ္းသာေရး ( ၅ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/215.mp3"><span style="color: #ffcc00;">၁၇၅။ မ်က္ေမွာက္ခ်မ္းသာေရး ( ၆ )</span></a></p>
<h5><span style="color: #33cccc;">သတိပ႒ာန္အက်ိဳး တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/91.mp3"><span style="color: #ffcc00;">၁၇၆။ သတိပ႒ာန္အက်ိဳး ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/92.mp3"><span style="color: #ffcc00;">၁၇၇။ သတိပ႒ာန္အက်ိဳး ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/93.mp3"><span style="color: #ffcc00;">၁၇၈။ သတိပ႒ာန္အက်ိဳး ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/94.mp3"><span style="color: #ffcc00;">၁၇၉။ သတိပ႒ာန္အက်ိဳး ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/95.mp3"><span style="color: #ffcc00;">၁၈၀။ သတိပ႒ာန္အက်ိဳး ( ၅ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/96.mp3"><span style="color: #ffcc00;">၁၈၁။ သတိပ႒ာန္အက်ိဳး ( ၆ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/97.mp3"><span style="color: #ffcc00;">၁၈၂။ သတိပ႒ာန္အက်ိဳး ( ၇ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/98.mp3"><span style="color: #ffcc00;">၁၈၃။ သတိပ႒ာန္အက်ိဳး ( ၈ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/99.mp3"><span style="color: #ffcc00;">၁၈၄။ သတိပ႒ာန္အက်ိဳး ( ၉ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/100.mp3"><span style="color: #ffcc00;">၁၈၅။ သတိပ႒ာန္အက်ိဳး ( ၁၀ )</span></a></p>
<h5><span style="color: #33cccc;">သတိပ႒ာန္ ေၾကြးေၾကာ္သံ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/223.mp3"><span style="color: #ffcc00;">၁၈၆။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/224.mp3"><span style="color: #ffcc00;">၁၈၇။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/225.mp3"><span style="color: #ffcc00;">၁၈၈။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/226.mp3"><span style="color: #ffcc00;">၁၈၉။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/227.mp3"><span style="color: #ffcc00;">၁၉၀။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/228.mp3"><span style="color: #ffcc00;">၁၉၁။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/229.mp3"><span style="color: #ffcc00;">၁၉၂။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/230.mp3"><span style="color: #ffcc00;">၁၉၃။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/231.mp3"><span style="color: #ffcc00;">၁၉၄။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/232.mp3"><span style="color: #ffcc00;">၁၉၅။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/233.mp3"><span style="color: #ffcc00;">၁၉၆။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/234.mp3"><span style="color: #ffcc00;">၁၉၇။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/235.mp3"><span style="color: #ffcc00;">၁၉၈။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/236.mp3"><span style="color: #ffcc00;">၁၉၉။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/237.mp3"><span style="color: #ffcc00;">၂၀၀။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/238.mp3"><span style="color: #ffcc00;">၂၀၁။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/239.mp3"><span style="color: #ffcc00;">၂၀၂။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/240.mp3"><span style="color: #ffcc00;">၂၀၃။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/241.mp3"><span style="color: #ffcc00;">၂၀၄။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၁၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/242.mp3"><span style="color: #ffcc00;">၂၀၅။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/243.mp3"><span style="color: #ffcc00;">၂၀၆။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/244.mp3"><span style="color: #ffcc00;">၂၀၇။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/245.mp3"><span style="color: #ffcc00;">၂၀၈။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/246.mp3"><span style="color: #ffcc00;">၂၀၉။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/247.mp3"><span style="color: #ffcc00;">၂၁၀။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/248.mp3"><span style="color: #ffcc00;">၂၁၁။ သတိပ႒ာန္ ေၾကြးေၾကာ္သံ (၂၆)</span></a></p>
<h5><span style="color: #33cccc;">အရိယာတို႔၏ စံအိမ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/205.mp3"><span style="color: #ffcc00;">၂၁၂။ အရိယာတို႔၏ စံအိမ္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/206.mp3"><span style="color: #ffcc00;">၂၁၃။ အရိယာတို႔၏ စံအိမ္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/207.mp3"><span style="color: #ffcc00;">၂၁၄။ အရိယာတို႔၏ စံအိမ္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/208.mp3"><span style="color: #ffcc00;">၂၁၅။ အရိယာတို႔၏ စံအိမ္ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/209.mp3"><span style="color: #ffcc00;">၂၁၆။ အရိယာတို႔၏ စံအိမ္ ( ၅ )</span></a></p>
<h5><span style="color: #33cccc;">အေျခခံဘာသာေရး</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/70.mp3"><span style="color: #ffcc00;">၂၁၇။ အေျခခံဘာသာေရး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/71.mp3"><span style="color: #ffcc00;">၂၁၈။ အေျခခံဘာသာေရး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/72.mp3"><span style="color: #ffcc00;">၂၁၉။ အေျခခံဘာသာေရး (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/73.mp3"><span style="color: #ffcc00;">၂၂၀။ အေျခခံဘာသာေရး (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/74.mp3"><span style="color: #ffcc00;">၂၂၁။ အေျခခံဘာသာေရး (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/75.mp3"><span style="color: #ffcc00;">၂၂၂။ အေျခခံဘာသာေရး (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/76.mp3"><span style="color: #ffcc00;">၂၂၃။ အေျခခံဘာသာေရး (၇)</span></a></p>
<h5><span style="color: #33cccc;">အရိယာဝါသတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/45.mp3"><span style="color: #ffcc00;">၂၂၄။ အရိယာဝါသတရား ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/46.mp3"><span style="color: #ffcc00;">၂၂၅။ အရိယာဝါသတရား ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/47.mp3"><span style="color: #ffcc00;">၂၂၆။ အရိယာဝါသတရား ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/48.mp3"><span style="color: #ffcc00;">၂၂၇။ အရိယာဝါသတရား ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/49.mp3"><span style="color: #ffcc00;">၂၂၈။ အရိယာဝါသတရား ( ၅ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/50.mp3"><span style="color: #ffcc00;">၂၂၉။ အရိယာဝါသတရား ( ၆ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/51.mp3"><span style="color: #ffcc00;">၂၃၀။ အရိယာဝါသတရား ( ၇ )</span></a></p>
<h5><span style="color: #33cccc;">ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/101.mp3"><span style="color: #ffcc00;">၂၃၁။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/102.mp3"><span style="color: #ffcc00;">၂၃၂။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/103.mp3"><span style="color: #ffcc00;">၂၃၃။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/104.mp3"><span style="color: #ffcc00;">၂၃၄။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/105.mp3"><span style="color: #ffcc00;">၂၃၅။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၅</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/106.mp3"><span style="color: #ffcc00;">၂၃၆။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၆</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/107.mp3"><span style="color: #ffcc00;">၂၃၇။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၇</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/108.mp3"><span style="color: #ffcc00;">၂၃၈။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၈</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/109.mp3"><span style="color: #ffcc00;">၂၃၉။ ဣေျႏၵထက္ေၾကာင္း ( ၉ )ပါး-၉</span></a></p>
<h5><span style="color: #33cccc;">ဣရိယာပထပိုင္း တရားတေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/111.mp3"><span style="color: #ffcc00;">၂၄၀။ ဣရိယာပထပိုင္း ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/112.mp3"><span style="color: #ffcc00;">၂၄၁။ ဣရိယာပထပိုင္း ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/113.mp3"><span style="color: #ffcc00;">၂၄၂။ ဣရိယာပထပိုင္း ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/114.mp3"><span style="color: #ffcc00;">၂၄၃။ ဣရိယာပထပိုင္း ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/115.mp3"><span style="color: #ffcc00;">၂၄၄။ ဣရိယာပထပိုင္း ( ၅ )</span></a></p>
<h5><span style="color: #33cccc;">(၇.၇.၂၀၁၃)အေမရိကန္၊ ကယ္လီဖိုးနီးယား၊ ဆန္ဖရန္စစၥကို ဟတ္မြန္ေဘးၿမိဳ႕၊ မဟာသတိပ႒ာန္ (၇) တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/266.mp3"><span style="color: #ffcc00;">၂၄၅။ (၇) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/267.mp3"><span style="color: #ffcc00;">၂၄၆။ (၇) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/268.mp3"><span style="color: #ffcc00;">၂၄၇။ (၇) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/269.mp3"><span style="color: #ffcc00;">၂၄၈။ (၇) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/270.mp3"><span style="color: #ffcc00;">၂၄၉။ (၇) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/271.mp3"><span style="color: #ffcc00;">၂၅၀။ (၇) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/272.mp3"><span style="color: #ffcc00;">၂၅၁။ (၇) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/273.mp3"><span style="color: #ffcc00;">၂၅၂။ (၇) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/274.mp3"><span style="color: #ffcc00;">၂၅၃။ (၇) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/275.mp3"><span style="color: #ffcc00;">၂၅၄။ (၇) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/276.mp3"><span style="color: #ffcc00;">၂၅၅။ (၇) တရားစခန္း အပိုင္း (၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/277.mp3"><span style="color: #ffcc00;">၂၅၆။ (၇) တရားစခန္း အပိုင္း (၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/278.mp3"><span style="color: #ffcc00;">၂၅၇။ (၇) တရားစခန္း အပိုင္း (၁၃)</span></a></p>
<h5><span style="color: #33cccc;">(၁၄.၇.၂၀၁၃) အေမရိကန္၊ ေမရီလန္းျပည္နယ္ (၁၀)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/14.mp3"><span style="color: #ffcc00;">၂၅၈။ ( ၈ )ပါးသီလေပး၊ သတိပ႒ာနသုတၱန္ ( ၁ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/15.mp3"><span style="color: #ffcc00;">၂၅၉။ သတိပ႒ာနသုတၱန္ ( ၂ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/16.mp3"><span style="color: #ffcc00;">၂၆၀။ သတိပ႒ာနသုတၱန္ ( ၃ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/17.mp3"><span style="color: #ffcc00;">၂၆၁။ သတိပ႒ာနသုတၱန္ ( ၄ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/18.mp3"><span style="color: #ffcc00;">၂၆၂။ သတိပ႒ာနသုတၱန္ ( ၅ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/19.mp3"><span style="color: #ffcc00;">၂၆၃။ သတိပ႒ာနသုတၱန္ ( ၆ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/20.mp3"><span style="color: #ffcc00;">၂၆၄။ သတိပ႒ာနသုတၱန္ ( ၇ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/21.mp3"><span style="color: #ffcc00;">၂၆၅။ သမထ ႏွင့္ ဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/1.mp3"><span style="color: #ffcc00;">၂၆၆။ ဓမၼဂုဏ္ရည္ျပ ခရီးစဥ္ တရားေတာ္ (ဆန္ဖရန္စစၥကို)</span></a></p>
<h5><span style="color: #33cccc;">(၁၃.၆.၂၀၁၄) အေမရိကန္ႏိုင္ငံ၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/290.mp3"><span style="color: #ffcc00;">၂၆၇။ (၁၀) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/291.mp3"><span style="color: #ffcc00;">၂၆၈။ (၁၀) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/292.mp3"><span style="color: #ffcc00;">၂၆၉။ (၁၀) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/293.mp3"><span style="color: #ffcc00;">၂၇၀။ (၁၀) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/294.mp3"><span style="color: #ffcc00;">၂၇၁။ (၁၀) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/295.mp3"><span style="color: #ffcc00;">၂၇၂။ (၁၀) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/296.mp3"><span style="color: #ffcc00;">၂၇၃။ (၁၀) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/297.mp3"><span style="color: #ffcc00;">၂၇၄။ (၁၀) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/298.mp3"><span style="color: #ffcc00;">၂၇၅။ (၁၀) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/299.mp3"><span style="color: #ffcc00;">၂၇၆။ (၁၀) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<h5><span style="color: #33cccc;">(၂၁.၅.၂၀၁၄) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား၊ LA ဓမၼစကၡဳဓမၼာရံု မဟာသတိပ႒ာန္ (၆)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/279.mp3"><span style="color: #ffcc00;">၂၇၇။ (၆) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/280.mp3"><span style="color: #ffcc00;">၂၇၈။ (၆) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/281.mp3"><span style="color: #ffcc00;">၂၇၉။ (၆) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/282.mp3"><span style="color: #ffcc00;">၂၈၀။ (၆) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/283.mp3"><span style="color: #ffcc00;">၂၈၁။ (၆) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/284.mp3"><span style="color: #ffcc00;">၂၈၂။ (၆) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/285.mp3"><span style="color: #ffcc00;">၂၈၃။ (၆) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/286.mp3"><span style="color: #ffcc00;">၂၈၄။ (၆) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/287.mp3"><span style="color: #ffcc00;">၂၈၅။ (၆) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/288.mp3"><span style="color: #ffcc00;">၂၈၆။ (၆) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/289.mp3"><span style="color: #ffcc00;">၂၈၇။ (၆) တရားစခန္း အပိုင္း (၁၁)</span></a></p>
<h5><span style="color: #33cccc;">(၁၄.၇.၂၀၁၅) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား LA ေကာင္တီ၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/343.mp3"><span style="color: #ffcc00;">၂၈၈။ (၅) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/344.mp3"><span style="color: #ffcc00;">၂၈၉။ ၅) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/345.mp3"><span style="color: #ffcc00;">၂၉၀။ (၅) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/346.mp3"><span style="color: #ffcc00;">၂၉၁။ (၅) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/347.mp3"><span style="color: #ffcc00;">၂၉၂။ (၅) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/348.mp3"><span style="color: #ffcc00;">၂၉၃။ (၅) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/349.mp3"><span style="color: #ffcc00;">၂၉၄။ (၅) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/350.mp3"><span style="color: #ffcc00;">၂၉၅။ (၅) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/351.mp3"><span style="color: #ffcc00;">၂၉၆။ (၅) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/352.mp3"><span style="color: #ffcc00;">၂၉၇။ (၅) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/353.mp3"><span style="color: #ffcc00;">၂၉၈။ (၅) တရားစခန္း အပိုင္း (၁၁)</span></a></p>
<h5><span style="color: #33cccc;">(၁၂.၆.၂၀၁၅) အေမရိကန္ႏိုင္ငံ၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/300.mp3"><span style="color: #ffcc00;">၂၉၉။ (၁၀) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/301.mp3"><span style="color: #ffcc00;">၃၀၀။ (၁၀) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/302.mp3"><span style="color: #ffcc00;">၃၀၁။ (၁၀) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/303.mp3"><span style="color: #ffcc00;">၃၀၂။ (၁၀) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/304.mp3"><span style="color: #ffcc00;">၃၀၃။ (၁၀) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/305.mp3"><span style="color: #ffcc00;">၃၀၄။ (၁၀) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/306.mp3"><span style="color: #ffcc00;">၃၀၅။ (၁၀) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/307.mp3"><span style="color: #ffcc00;">၃၀၆။ (၁၀) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/308.mp3"><span style="color: #ffcc00;">၃၀၇။ (၁၀) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/309.mp3"><span style="color: #ffcc00;">၃၀၈။ (၁၀) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/310.mp3"><span style="color: #ffcc00;">၃၀၉။ (၁၀) တရားစခန္း အပိုင္း (၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/311.mp3"><span style="color: #ffcc00;">၃၁၀။ (၁၀) တရားစခန္း အပိုင္း (၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/312.mp3"><span style="color: #ffcc00;">၃၁၁။ (၁၀) တရားစခန္း အပိုင္း (၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/313.mp3"><span style="color: #ffcc00;">၃၁၂။ (၁၀) တရားစခန္း အပိုင္း (၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/314.mp3"><span style="color: #ffcc00;">၃၁၃။ (၁၀) တရားစခန္း အပိုင္း (၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/315.mp3"><span style="color: #ffcc00;">၃၁၄။ (၁၀) တရားစခန္း အပိုင္း (၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/316.mp3"><span style="color: #ffcc00;">၃၁၅။ (၁၀) တရားစခန္း အပိုင္း (၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/317.mp3"><span style="color: #ffcc00;">၃၁၆။ (၁၀) တရားစခန္း အပိုင္း (၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/318.mp3"><span style="color: #ffcc00;">၃၁၇။ (၁၀) တရားစခန္း အပိုင္း (၁၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/319.mp3"><span style="color: #ffcc00;">၃၁၈။ (၁၀) တရားစခန္း အပိုင္း (၂၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/320.mp3"><span style="color: #ffcc00;">၃၁၉။ (၁၀) တရားစခန္း အပိုင္း (၂၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/321.mp3"><span style="color: #ffcc00;">၃၂၀။ (၁၀) တရားစခန္း အပိုင္း (၂၂)</span></a></p>
<h5><span style="color: #33cccc;">(၂၃.၅.၂၀၁၆) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား၊ ဆန္ဖရန္စစၥကို ဟတ္မြန္ေဘးၿမိဳ႕၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/354.mp3"><span style="color: #ffcc00;">၃၂၁။ (၅) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/355.mp3"><span style="color: #ffcc00;">၃၂၂။ (၅) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/356.mp3"><span style="color: #ffcc00;">၃၂၃။ (၅) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/357.mp3"><span style="color: #ffcc00;">၃၂၄။ (၅) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/358.mp3"><span style="color: #ffcc00;">၃၂၅။ (၅) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/359.mp3"><span style="color: #ffcc00;">၃၂၆။ (၅) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/360.mp3"><span style="color: #ffcc00;">၃၂၇။ (၅) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/361.mp3"><span style="color: #ffcc00;">၃၂၈။ (၅) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/362.mp3"><span style="color: #ffcc00;">၃၂၉။ (၅) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/363.mp3"><span style="color: #ffcc00;">၃၃၀။ (၅) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/364.mp3"><span style="color: #ffcc00;">၃၃၁။ (၅) တရားစခန္း အပိုင္း (၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/365.mp3"><span style="color: #ffcc00;">၃၃၂။ (၅) တရားစခန္း အပိုင္း (၁၂)</span></a></p>
<h5><span style="color: #33cccc;">(၃.၆.၂၀၁၆) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယား LA ေကာင္တီ၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/322.mp3"><span style="color: #ffcc00;">၃၃၃။ (၅) တရားစခန္း အပိုင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/323.mp3"><span style="color: #ffcc00;">၃၃၄။ (၅) တရားစခန္း အပိုင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/324.mp3"><span style="color: #ffcc00;">၃၃၅။ (၅) တရားစခန္း အပိုင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/325.mp3"><span style="color: #ffcc00;">၃၃၆။ (၅) တရားစခန္း အပိုင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/326.mp3"><span style="color: #ffcc00;">၃၃၇။ (၅) တရားစခန္း အပိုင္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/327.mp3"><span style="color: #ffcc00;">၃၃၈။ (၅) တရားစခန္း အပိုင္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/328.mp3"><span style="color: #ffcc00;">၃၃၉။ (၅) တရားစခန္း အပိုင္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/329.mp3"><span style="color: #ffcc00;">၃၄၀။ (၅) တရားစခန္း အပိုင္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/330.mp3"><span style="color: #ffcc00;">၃၄၁။ (၅) တရားစခန္း အပိုင္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/331.mp3"><span style="color: #ffcc00;">၃၄၂။ (၅) တရားစခန္း အပိုင္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/332.mp3"><span style="color: #ffcc00;">၃၄၃။ (၅) တရားစခန္း အပိုင္း (၁၁)</span></a></p>
<h5><span style="color: #33cccc;">(၁၁.၆.၂၀၁၆) အေမရိကန္၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/415.mp3"><span style="color: #ffcc00;">၃၄၄။ ရႈမွတ္နည္း အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/416.mp3"><span style="color: #ffcc00;">၃၄၅။ ဝန္ခံျခင္း ႏွင္႔ ေဟာခဲ႔သည္ (၁၁-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/417.mp3"><span style="color: #ffcc00;">၃၄၆။ အက်ိဳး ရွိေအာင္ေနပါ (၁၂-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/418.mp3"><span style="color: #ffcc00;">၃၄၇။ အရိယာစံအိမ္ (၁၃-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/419.mp3"><span style="color: #ffcc00;">၃၄၈။ အရိယာစံအိမ္ (၁၄-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/420.mp3"><span style="color: #ffcc00;">၃၄၉။ အရိယာစံအိမ္ (၁၅-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/421.mp3"><span style="color: #ffcc00;">၃၅၀။ အရိယာစံအိမ္ (၁၆-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/422.mp3"><span style="color: #ffcc00;">၃၅၁။ အရိယာစံအိမ္ (၁၇-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/423.mp3"><span style="color: #ffcc00;">၃၅၂။ အရိယာစံအိမ္ (၁၈-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/424.mp3"><span style="color: #ffcc00;">၃၅၃။ ၾသဝါဒပါတိေမာက္ (၁၉-၆-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/425.mp3"><span style="color: #ffcc00;">၃၅၄။ English လိုေဟာ</span></a></p>
<h5><span style="color: #33cccc;">(၁၀.၆.၂၀၁၇) အေမရိကန္ႏိုင္၊ ေမရီလင္းျပည္နယ္၊ မဟာသတိပ႒ာန္ (၁၀)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/394.mp3"><span style="color: #ffcc00;">၃၅၅။ ( ၈ )ပါး သီလေပး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/395.mp3"><span style="color: #ffcc00;">၃၅၆။ ေယာဂီလိုက္နာရမည္႔ တရား ( ၄ )ပါး တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/396.mp3"><span style="color: #ffcc00;">၃၅၇။ သတိပ႒ာန္တရား ( ၄ )ပါး တရားေတာ္ (၁၀-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/397.mp3"><span style="color: #ffcc00;">၃၅၈။ အခြင္႔ေကာင္း ( ၄ ) ပါး တရားေတာ္ (၁၁-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/398.mp3"><span style="color: #ffcc00;">၃၅၉။ ဣရိယာပထပိုင္း (၁၂-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/399.mp3"><span style="color: #ffcc00;">၃၆၀။ တရားအားထုတ္သူမ်ား ျပည္႔စံုရမည္႔အေၾကာင္း အဂၤါ ( ၅ )ပါး -၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/400.mp3"><span style="color: #ffcc00;">၃၆၁။ တရားအားထုတ္သူမ်ား ျပည္႔စံုရမည္႔အေၾကာင္း အဂၤါ ( ၅ )ပါး -၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/401.mp3"><span style="color: #ffcc00;">၃၆၂။ ဝိပႆနာ ဂုဏ္ရည္ျပတရားေတာ္ (၁၃-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/402.mp3"><span style="color: #ffcc00;">၃၆၃။ ဝိပႆနာ ဂုဏ္ရည္ျပတရားေတာ္ (၁၄-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/403.mp3"><span style="color: #ffcc00;">၃၆၄။ ဝိပႆနာ ဂုဏ္ရည္ျပတရားေတာ္ (၁၅-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/404.mp3"><span style="color: #ffcc00;">၃၆၅။ ဝိပႆနာ ဂုဏ္ရည္ျပတရားေတာ္ (၁၆-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/405.mp3"><span style="color: #ffcc00;">၃၆၆။ ဓမၼခ်မ္းသာ ရေအာင္ရွာ (၁၇-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/406.mp3"><span style="color: #ffcc00;">၃၆၇။ တရားစခန္းေအာင္ပြဲ ၾသဝါဒ (၁၈-၆-၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/407.mp3"><span style="color: #ffcc00;">၃၆၈။ စိတၱာႏုပႆနာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/408.mp3"><span style="color: #ffcc00;">၃၆၉။ ေဝဒနာႏုပႆနာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/409.mp3"><span style="color: #ffcc00;">၃၇၀။ ဓမၼာႏုပႆနာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/410.mp3"><span style="color: #ffcc00;">၃၇၁။ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/411.mp3"><span style="color: #ffcc00;">၃၇၂။ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/412.mp3"><span style="color: #ffcc00;">၃၇၃။ ေမြးေန႔အလွဴေတာ္ – ေဒၚေမရီခ်စ္တီး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/413.mp3"><span style="color: #ffcc00;">၃၇၄။ ( ၅ )ပါးသီလေပး / ကိုယ္ေစာင္႔တရား ( ၄ )ပါး၊ ဓမၼအလင္းေရာင္ေက်ာင္းတိုက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/414.mp3"><span style="color: #ffcc00;">၃၇၅။ ဆြမ္းအႏုေမာဒနာ ဦးေဝၿဖိဳးေအာင္ + မေအးမြန္၊ ေဒၚေမသန္း (မႏၱေလး ထမင္းဆိုင္)</span></a></p>
<h5><span style="color: #33cccc;">(၁၁.၅.၂၀၁၇) အေမရိကန္၊ ကယ္လီဖိုးနီးယား၊ ဆန္ဖရန္စစၥကို၊ ဟတ္မြန္ေဘးၿမိဳ႕၊ မဟာသတိပ႒ာန္ (၅)ရက္ တရားစခန္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/366.mp3"><span style="color: #ffcc00;">၃၇၆။ ၁၁.၅.၂၀၁၇ (နံနက္ပိုင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/367.mp3"><span style="color: #ffcc00;">၃၇၇။ ၁၂-၅-၂၀၁၇ (နံနက္ပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/368.mp3"><span style="color: #ffcc00;">၃၇၈။ ၁၃-၅-၂၀၁၇ (နံနက္ပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/369.mp3"><span style="color: #ffcc00;">၃၇၉။ ၁၄-၅-၂၀၁၇ (နံနက္ပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/370.mp3"><span style="color: #ffcc00;">၃၈၀။ ၁၅-၅-၂၀၁၇ (နံနက္ပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/371.mp3"><span style="color: #ffcc00;">၃၈၁။ ၁၁-၅-၂၀၁၇ (ညေနပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/372.mp3"><span style="color: #ffcc00;">၃၈၂။ ၁၂-၅-၂၀၁၇ (ညေနပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/373.mp3"><span style="color: #ffcc00;">၃၈၃။ ၁၃-၅-၂၀၁၇ (ညေနပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/374.mp3"><span style="color: #ffcc00;">၃၁၄။ ၁၄-၅-၂၀၁၇ (ညေနပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/375.mp3"><span style="color: #ffcc00;">၃၈၅။ ၁၅-၅-၂၀၁၇ (ညေနပို္င္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/376.mp3"><span style="color: #ffcc00;">၃၈၆။ ၁၆-၅-၂၀၁၇ တရားစခန္းပိတ္ပြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/377.mp3"><span style="color: #ffcc00;">၃၈၇။ ၁၇-၅-၂၀၁၇ ရႈမွတ္နည္း အလုပ္ေပးတရား (မဟာစည္ ဆရာေတာ္ႀကီး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/378.mp3"><span style="color: #ffcc00;">၃၈၈။ ၁၈-၅-၂၀၁၇ ရႈမွတ္နည္း အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/379.mp3"><span style="color: #ffcc00;">၃၈၉။ ၁၉-၅-၂၀၁၇ ရႈမွတ္နည္း အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/380.mp3"><span style="color: #ffcc00;">၃၉၀။ ၂၀-၅-၂၀၁၇ ရႈမွတ္နည္း အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/381.mp3"><span style="color: #ffcc00;">၃၉၁။ ၂၁-၅-၂၀၁၇ ရႈမွတ္နည္း အလုပ္ေပးတရား</span></a></p>
<h5><span style="color: #33cccc;">(၂၂.၅.၂၀၁၇) အေမရိကန္ႏိုင္ငံ၊ ကယ္လီဖိုးနီးယားျပည္နယ္၊ ဆန္ဖရန္စစၥကို၊ မတ္မြန္ေဘးၿမိဳ႕၊ အခ်ိန္ျပည္႔ ( ၇ ) ရက္ တရားစခန္း </span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/382.mp3"><span style="color: #ffcc00;">၃၉၂။(၂၂-၅-၂၀၁၇) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/383.mp3"><span style="color: #ffcc00;">၃၉၃။ ၂၂-၅-၂၀၁၇ (ညေနပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/384.mp3"><span style="color: #ffcc00;">၃၉၄။ ၂၃-၅-၂၀၁၇ (နံနက္ပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/385.mp3"><span style="color: #ffcc00;">၃၉၅။ ၂၃-၅-၂၀၁၇ (ညေနပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/386.mp3"><span style="color: #ffcc00;">၃၉၆။ ၂၄-၅-၂၀၁၇ (နံနက္ပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/387.mp3"><span style="color: #ffcc00;">၃၉၇။ ၂၄-၅-၂၀၁၇ (ညေနပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/388.mp3"><span style="color: #ffcc00;">၃၉၈။ ၂၅-၅-၂၀၁၇ (နံနက္ပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/389.mp3"><span style="color: #ffcc00;">၃၉၉။ ၂၅-၅-၂၀၁၇ (ညေနပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/390.mp3"><span style="color: #ffcc00;">၄၀၀။ ၂၆-၅-၂၀၁၇ (နံနက္ပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/391.mp3"><span style="color: #ffcc00;">၄၀၁။ ၂၆-၅-၂၀၁၇ (ညေနပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/392.mp3"><span style="color: #ffcc00;">၄၀၂။ ၂၇-၅-၂၀၁၇ (နံနက္ပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/shwe_min_won_sayardaw/1/393.mp3"><span style="color: #ffcc00;">၄၀၃။ ၂၇-၅-၂၀၁၇ (ညေနပိုင္း) လုပ္ငန္းစဥ္ျပ အလုပ္ေပးတရား</span></a></p>
</div>
"""

soup = bs4(text, 'html.parser')

'''
with open('titles_links.txt', 'w') as f:
    for key in soup.find_all('a'):
        f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        #f.write('{}\n'.format(key.get_text()))
'''        
count = 1
with open('titles_links.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        counter = '{:03d}'.format(count)
        f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
        count += 1

'''        
with open('titles.txt', 'w') as f:
    for key in soup.find_all('a'):
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        f.write('{}\n'.format(key.get_text()))        
'''


