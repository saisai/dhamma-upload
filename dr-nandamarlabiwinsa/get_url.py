from bs4 import BeautifulSoup as bs4

text = """<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0860-ndml(9).mp3"><span style="color: #ffcc00;">ဆရာေတာ္ၾကီး ခ်ီးျမွင့္ေပးေသာ ဗုဒၶါနုႆတိဘာဝနာပြားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0858-ndml(5).mp3"><span style="color: #ffcc00;">ဆရာေတာ္ၾကီး၏ ငါးပါးသီလေပးနွင့္ခ်ီးျမွင့္ေပးေသာပရိတ္တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0859-ndml(8).mp3"><span style="color: #ffcc00;">ဆရာေတာ္ၾကီး၏ ရွစ္ပါးသီလေပးနွင့္ခ်ီးျမွင့္ေပးေသာပရိတ္တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0829-ndml.mp3"><span style="color: #ffcc00;">ဆရာေတာ္ၾကီးရြတ္ဖတ္ပူေဇာ္ေသာ ေမတၱာသုတ္</span></a></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/528-myitta-po.mp3" target="_blank"><span style="color: #ffcc00;">(၅၂၈)သြယ္ေမတၱာပို႔ </span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/17-04-2017.mp3"><span style="color: #ffcc00;">ျမန္မာတို႔မဂၤလာႏွစ္သစ္ကိုၾကိဳဆိုပါ (၁၇.၄.၂၀၁၇ &#8211; ႏွစ္ဆန္းတစ္ရက္ေန႔)</span></a></p>
<h6><a href="https://www.thitsarparamisociety.com/dr-nandamarlabiwinsa-dhamma-lecture/" target="_blank"><span style="color: #3366ff;">ဓမၼသင္တန္းတရားေတာ္မ်ား နာယူရန္္</span> &gt;&gt;&gt;Click Here</a></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/12.8.2018.mp3"><span style="color: #ffcc00;">ဘ၀ခ်မ္းသာရေၾကာာင္းရွာ (၁၂.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/10.8.2018.mp3"><span style="color: #ffcc00;">စာၾကည့္တုိက္လွဴဒါန္းျခင္း အနဳေမာဒနာ ဩဝါဒတရားေတာ္ (၁၀.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/09.8.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒတရားေတာ္ (၉.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/08.8.2018.mp3"><span style="color: #ffcc00;">ခ်ီးမြမ္းထိုက္ေသာ လူသား တရားေတာ္ (၈.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/06.8.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၆.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/05.8.2018.mp3"><span style="color: #ffcc00;">သစ္တစ္ပင္ေကာင္း လူေကာင္းတစ္ေယာက္ (၅.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/04.8.2018_dhammalecture_SitaguSagaing.mp3"><span style="color: #ffcc00;">စာ၀ါပို႔ခ်ျခင္း (သီတဂူဗုဒၶတကၠသိုလ္ စစ္ကိုငး္) (၅.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/05.8.2018_anumawdanar.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၅.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/04.8.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၄.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/03.8.2018_warso_awwwarda.mp3"><span style="color: #ffcc00;">၀ါတြင္းကာလ အဖိတ္ေန႔ ၾသ၀ါဒ  (၃.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/03.8.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၃.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Aug/01.8.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၁.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/31.7.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၃၁.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/30.7.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၃၀.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/29.7.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆုံးအမ ႏွစ္ဘဝခ်မ္းသာေရး (၂၉.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/28.7.2018.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာဝင္ေကာင္းတို႔၏ အရည္အခ်င္းေကာင္းမ်ား (၂၈.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/28.7.2018_warso.mp3"><span style="color: #ffcc00;">ဝါဆို ဝါကပ္ အခမ္းအနား (၂၈.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/28.7.2018_warso_awwwarda.mp3"><span style="color: #ffcc00;">ဝါဆိုပြဲ ၾသဝါဒ (၂၈.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/27.7.2018.mp3"><span style="color: #ffcc00;">၂၆၀၇ႏွစ္ျပည့္ ဓမၼစၾကာေန႔ (၂၇.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/27.7.2018_anumawdanar.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၂၇.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/26.7.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆုံးအမႏွင့္ မိသားစုဘဝ (၂၆.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/24.7.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၂၄.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/21.7.2018.mp3"><span style="color: #ffcc00;">ဝိသာခါဆႏၵျပည့္ဝေသာအခါ တရားေတာ္ (၂၁.၀၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/20.7.2018.mp3"><span style="color: #ffcc00;">ဥစၥာစီးပြားႏွင့္ ကိုယ္က်င့္တရား တရားေတာ္ (၂၀.၀၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/14.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါးတရားေတာ္ (၁၄.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/12.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါးတရားေတာ္ (၁၂.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/11.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါးတရားေတာ္ (၁၁.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/10.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါးတရားေတာ္ (၁၀.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/05.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါးတရားေတာ္ (၅.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/03.7.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ သမၼဳတိေဒသနာ ႏွင့္ ပရမတၳေဒသနာ (၃.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/02.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါးတရားေတာ္ (ဆရာၾကီေဒၚကဥၥနာ ေမြးေန႔ပူဇာ အထူဓမၼဘသင္ ၂.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/01.7.2018.mp3"><span style="color: #ffcc00;">ဘာသာတရားႏွင့္ အမွန္အမွား (၁.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/30.6.2018.mp3"><span style="color: #ffcc00;">ဓမၼဒိႏၷသုတ္မွ ျမတ္ဗုဒၶ၏ဆံုးမစကား (၃၀.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/28.6.2018_pm.mp3"><span style="color: #ffcc00;">ေလာကကိုလွန္၍ဆန္တက္သူ (၂၈.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/28.6.2018_am.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာကိုယ္က်င့္တရားႏွင့္အညီေနထိုင္ျခင္း (၂၈.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/27.6.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ၾသ၀ါဒတရားေတာ္(၂၇.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/22.6.2018.mp3"><span style="color: #ffcc00;"> အႏုေမာဒနာ ၾသ၀ါဒတရားေတာ္(၂၂.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/20.6.2018.mp3"><span style="color: #ffcc00;"> အႏုေမာဒနာ ၾသ၀ါဒတရားေတာ္(၂၀.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/19.6.2018.mp3"><span style="color: #ffcc00;"> အႏုေမာဒနာ ၾသ၀ါဒတရားေတာ္(၁၉.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/06.6.2018.mp3"><span style="color: #ffcc00;">စရဏတရားျဖင့္ ေအာင္ျမင္မႈကိုရယူၾက တရားေတာ္ (၆.၆.၂၀၁၈)</span></a><br />
(အသံပိုင္းဆိုင္ရာအားနည္းမႈေၾကာင့္ တရားအေရွ႕ပိုင္း အနည္းငယ္မပါ၀င္ပါ။)</p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/03.6.2018.mp3"><span style="color: #ffcc00;">မိတ္ေဆြစစ္ကို ႐ွာေဖြျခင္း(၃.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/02.6.2018.mp3"><span style="color: #ffcc00;">ဘဝမွာေနထိုင္သမွ် အေရးပါသည့္ ကိုယ္က်င့္တရားႏွစ္ပါး (၂.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/June/01.6.2018.mp3"><span style="color: #ffcc00;">သတိထားရမည့္ မမွန္မကန္ေျပာဆိုမႈမ်ား (၁.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/31.5.2018-awwwarda-sitagubuddhauni-mdy.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ &#8211; သီတဂူကမာၻ႔ဗုဒၶတကၠသိုလ္ မႏၲေလး ေက်ာင္းသားသစ္ၾကိဳဆိုပြဲ(၃၁.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/30.5.2018-pm.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆုံးအမႏွင့္အညီအားကိုးရာ႐ွာျခင္း (၃၀.၅.၂၀၁၈ မႏၲေလးသာသနာ႔တကၠသိုလ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/30.5.2018-awwwarda-sitagubuddhauni.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ &#8211; သီတဂူကမာၻ႔ဗုဒၶတကၠသိုလ္ စစ္ကိုင္း (၃၀.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/30.5.2018-am.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒအႏုေမာဒနာတရားေတာ္ (၃၀.၅.၂၀၁၈ မႏၲေလး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/29.5.2018.mp3"><span style="color: #ffcc00;">႐ွင္ဥပါလိမေထရ္ျမတ္၏ အသိေပးဆုံးမစကား (၂၉.၅.၂၀၁၈ မႏၲေလးသာသနာ႔တကၠသိုလ္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/29.5.2018-awwwarda-and-anumawdanar.mp3"><span style="color: #ffcc00;"> အႏုေမာဒနာ ၾသ၀ါဒတရားေတာ္ မဟာသုေဗာဓာရုံေက်ာင္းတိုက္ ႏွစ္-၆၀ျပည့္(၂၉.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/28.5.2018-awwwarda.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ &#8211; မဟာသုေဗာဓာရုံေက်ာင္းတိုက္ ႏွစ္-၆၀ ျပည့္(၂၈.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/28.5.2018-anumawdanar.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ &#8211; မဟာသုေဗာဓာရုံေက်ာင္းတိုက္ ႏွစ္-၆၀ ျပည့္(၂၈.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/28.5.2018.mp3"><span style="color: #ffcc00;">အျမင္ကြဲျပား ပုဂၢိဳလ္မ်ား၏ ထူးျခားေသာဘဝ (၂၈.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/27.5.2018-pm.mp3"><span style="color: #ffcc00;">တဏွာဆင့္ပြား အဆိုးတရားမ်ား (၂၇.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/27.5.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္(၂၇.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/22.5.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂၂.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/17.5.2018.mp3"><span style="color: #ffcc00;"> ျမတ္ဗုဒၶ၏ ဓမၼအသံ (၁၇.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/17.5.2018-anumawdanar.mp3"><span style="color: #ffcc00;"> အႏုေမာဒနာတရားေတာ္(၁၇.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/15.5.2018.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔ ျမတ္နိဳးေသာဆု (၁၅.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/07.5.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ဒြယ ဝိပႆနာ (၇.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/05.5.2018.mp3"><span style="color: #ffcc00;">ဝိပႆနာ သမၼာဒိ႒ိ (၅.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Apr/30.4.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ပါရမီဘဝမွ မဃေဒဝမင္းႏွင့္ေနမိမင္းတရားေတာ္ အပိုင္း(၁) &#8211; (၃၀.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/01.5.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ပါရမီဘဝမွ မဃေဒဝမင္းႏွင့္ေနမိမင္း တရားေတာ္ အပိုင္း(၂) &#8211; (၁.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/03.5.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ပါရမီဘဝမွ မဃေဒဝမင္းႏွင့္ေနမိမင္း တရားေတာ္ အပိုင္း(၃) &#8211; (၃.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/06.5.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ပါရမီဘဝမွ မဃေဒဝမင္းႏွင့္ေနမိမင္း တရားေတာ္ အပိုင္း(၄) &#8211; (၆.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/May/02.5.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Apr/29.4.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶဖြားေတာ္မူေသာ (၂၆၄၁)ႏွစ္ေျမာက္ေမြးေန႔အခမ္းအနားတြင္ ပူေဇာ္ေသာ တရားေတာ္ (၂၉.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Apr/28.4.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ပါရမီဘဝမွ သုဝဏၰသာမ တရားေတာ္(၂၈.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/Apr/29.4.2018-pm.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ပါရမီဘဝမွ သုဝဏၰသာမ တရားေတာ္ အပိုင္း (၂) &#8211; (၂၉.၄.၂၀၁၈)</span></a><br />
(တရားေနာက္ပိုင္းတြင္ အသံျပတ္ေတာင္းမႈရိွပါသည္။)</p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/24.4.2018.mp3"><span style="color: #ffcc00;">ေမတၱသုတ္ပရိတ္တရားေတာ္ႏွင့္အႏုေမာဒနာတရားေတာ္ (၂၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/21.4.2018.mp3"><span style="color: #ffcc00;">ကုသိုလ္တရားႏွင့္စိတ္စြမ္းအား (၂၁.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/20.4.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂၀.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/18.4.2018-am.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၁၈.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/13.4.2018.mp3"><span style="color: #ffcc00;">သုတေသာမႏွင့္ လူဘီလူး တရားေတာ္ (၁) (၁၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/14.4.2018.mp3"><span style="color: #ffcc00;">သုတေသာမႏွင့္ လူဘီလူး တရားေတာ္ (၂) (၁၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/15.4.2018.mp3"><span style="color: #ffcc00;">သုတေသာမႏွင့္ လူဘီလူး တရားေတာ္ (၃) (၁၅.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/16.4.2018.mp3"><span style="color: #ffcc00;">သုတေသာမႏွင့္ လူဘီလူး တရားေတာ္ (၄) (၁၆.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/17.4.2018.mp3"><span style="color: #ffcc00;">သုတေသာမႏွင့္ လူဘီလူး တရားေတာ္ (၅) (၁၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/13.4.2018-am.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၁၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018-POL/01_08.4.2018.mp3"><span style="color: #ffcc00;">မဟာဇနကဇာတ္ေတာ္ႏွင့္ ဘဝသင္ခန္းစာမ်ား (၁) (၈.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018-POL/02_09.4.2018.mp3"><span style="color: #ffcc00;">မဟာဇနကဇာတ္ေတာ္ႏွင့္ ဘဝသင္ခန္းစာမ်ား (၂) (၉.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018-POL/03_10.4.2018.mp3"><span style="color: #ffcc00;">မဟာဇနကဇာတ္ေတာ္ႏွင့္ ဘဝသင္ခန္းစာမ်ား (၃) (၁၀.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018-POL/04_11.4.2018.mp3"><span style="color: #ffcc00;">မဟာဇနကဇာတ္ေတာ္ႏွင့္ ဘဝသင္ခန္းစာမ်ား (၄) (၁၁.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/05_12.4.2018.mp3"><span style="color: #ffcc00;">မဟာဇနကဇာတ္ေတာ္ႏွင့္ ဘဝသင္ခန္းစာမ်ား (၅) (၁၂.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Apr/05.4.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၅.၄.၂၀၁၈ ျပင္ဦးလြင္ ဓမၼသဟာယ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Apr/03.4.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၃.၄.၂၀၁၈ မႏၲေလး မဟာေအာင္ေျမ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/29.3.2018.mp3"><span style="color: #ffcc00;">ပရဟိတစြမ္းအားနဲ႔ ပါရမီဆယ္ပါး (၂၉.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/28.3.2018.mp3"><span style="color: #ffcc00;">ဘဝကိုအနိဳင္ယူျခင္း (၂၈.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/25.3.2018-pm.mp3"><span style="color: #ffcc00;">ေမးခြန္းပုစၧာျဖင့္ အေျဖ႐ွာျခင္း တရားေတာ္ (၂၅.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/25.3.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂၅.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/24.3.2018-pm.mp3"><span style="color: #ffcc00;">ဆင္းရဲသူ ႏွင့္ ခ်မ္းသာသူ (၂၄.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/24.3.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂၄.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/19.3.2018.mp3"><span style="color: #ffcc00;">ရတနာကို ႐ွာေဖြျခင္း တရားေတာ္ (၂) (၁၉.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/18.3.2018.mp3"><span style="color: #ffcc00;">ရတနာကို ႐ွာေဖြျခင္း တရားေတာ္ (၁) (၁၈.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/17.3.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၁၇.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Mar/01.3.2018.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ (၁.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/23.2.2018.mp3"><span style="color: #ffcc00;">သတိသမၸဇဥ္ည ႏွင့္ ေန႔စဥ္ဘဝ (၂၃.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/22.2.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာႏွင့္ ျမတ္ေသာအလွဴမဂၤလာ (၂၂.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/22.02.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၂၂.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/20.02.2018.mp3"><span style="color: #ffcc00;">ကံေကာင္းခ်င္လ်ွင္ စိတ္ထားျပင္ (၂၀.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/19.02.2018.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာ ႏွင့္ က်န္းမာေရး (၁၉.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/16.2.2018.mp3"><span style="color: #ffcc00;">အဆိုးထဲမွာ အေကာင္း႐ွာ (၁၆.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/15.2.2018.mp3"><span style="color: #ffcc00;">ျမန္မာနိဳင္ငံ၏ ဂုဏ္ယူဖြယ္ရာ ရတနာမ်ား (၁၅.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/14.2.2018.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာ အျမတ္ရတနာ (၁၄.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/14.2.2018-1.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၁၄.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/13.2.2018.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာလူငယ္မ်ား၏ အက်ိဳးစီးပြား (၁၃.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/12.2.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာ ဩဝါဒ (၁၂.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/11.2.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အာဏာေဒသနာ (၁၁.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/10.2.2018.mp3"><span style="color: #ffcc00;">ငါးဆူဗုဒၶ ဘဒၵဤကမာၻ (၁၀.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/09.2.2018.mp3"><span style="color: #ffcc00;">စိတ္အေျခအေနႏွင့္ ေရာက္ရမည့္ ဘုံဘဝ ၉.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/06.02.2018.mp3"><span style="color: #ffcc00;">ကိုယ္က်င့္တရားပ်က္ျပားျခင္း၏ အျပစ္မ်ား (၆.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/04.2.2018.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ လြတ္ေျမာက္ေရး လမ္းစဥ္ (၄.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Feb/01.2.2018.mp3"><span style="color: #ffcc00;">လွပေသာဘဝကို ျမတ္ဗုဒၶ၏ အဆုံးအမျဖင့္ ပုံေဖာ္ျခင္း (၁.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Jan/31.1.2018.mp3"><span style="color: #ffcc00;">လူ႔ဘ၀ႏွင့္သူေတာ္ေကာင္းတရား (၃၁.၀၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Jan/30.1.2018.mp3"><span style="color: #ffcc00;">တိုးတက္ႀကီးပြား အရည္အခ်င္းမ်ား (၃၀.၀၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Jan/28.1.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂၈.၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Jan/22.1.2018.mp3"><span style="color: #ffcc00;">ေလာကအက်ိဳးျပဳ လုပ္ငန္းႏွစ္ခု (၂၂.၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Jan/4.1.2018.mp3"><span style="color: #ffcc00;">ဘဝအဆင့္ကိုတိုးျမႇင့္ေရး (၄.၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2018/Jan/1.1.2018.mp3"><span style="color: #ffcc00;">မဂၤလာတရားႏွင့္အညီ ႏိုင္ငံသစ္ကိုတည္ (၁.၁.၂၀၁၈)</span></a></p>
<h5><span style="color: #339966;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/001_22.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁) &#8211; (၂၂.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/002_23.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂) &#8211; (၂၃.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/003_24.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃) &#8211; (၂၄.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/004_24.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄) &#8211; (၂၅.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/005_26.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅) &#8211; (၂၆.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/006_29.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆) &#8211; (၂၉.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/007_30.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇) &#8211; (၃၀.၈.၂၀၁၇)</span></a><br />
(Live Video အပိုင္းငယ္မ်ားကို ေပါင္းစုထားရေသာေၾကာင့္ တရားအလယ္တို႔တြင္ ျပတ္ေတာက္မႈအနည္းငယ္ရိွပါသည္။)</p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/008_31.8.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈) &#8211; (၃၁.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/009_1.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၉) &#8211; (၁.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/010_8.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၀) &#8211; (၈.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/011_9.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၁) &#8211; (၉.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/012_10.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၂) &#8211; (၁၀.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/013_11.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၃) &#8211; (၁၁.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/014_12.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၄) &#8211; (၁၂.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/015_13.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၅) &#8211; (၁၃.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/016_14.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၆) &#8211; (၁၄.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/017_15.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၇) &#8211; (၁၅.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/018_16.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၈) &#8211; (၁၆.၉.၂၀၁၇)</span></a><br />
(တရားေတာ္အစပိုင္း မပါရိွေသးပါ။)</p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/019_17.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၁၉) &#8211; (၁၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/020_19.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၀) &#8211; (၁၉.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/021_20.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၁) &#8211; (၂၀.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/022_21.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၂) &#8211; (၂၁.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/023_22.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၃) &#8211; (၂၂.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/024_23.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၄) &#8211; (၂၃.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/025_24.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၅) &#8211; (၂၄.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/026_25.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၆) &#8211; (၂၅.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/027_26.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၇) &#8211; (၂၆.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/028_27.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၈) &#8211; (၂၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/029_28.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၂၉) &#8211; (၂၈.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/030_29.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၀) &#8211; (၂၉.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/031_30.9.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၁) &#8211; (၃၀.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/32_3.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၂) &#8211; (၃.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/033_4.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၃) &#8211; (၄.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/034_5.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၄) &#8211; (၅.၁၀၂၀၁၇- သီတင္းကၽြတ္လျပည့္ေန႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/038_10.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၈) &#8211; (၁၀.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/039_13.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၃၉) &#8211; (၁၃.၁၀၂၀၁၇)</span></a><br />
(တရားေတာ္ အစပိုင္းေလးတြင္ အနည္းငယ္ျပတ္ေတာက္မႈရိွပါသည္။)</p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/040_21.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၀) &#8211; (၂၁.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/041_24.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၁) &#8211; (၂၄.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/042_25.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၂) &#8211; (၂၅.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/043_26.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၃) &#8211; (၂၆.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/044_27.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၄) &#8211; (၂၇.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/045_28.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၅) &#8211; (၂၈.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/048_31.10.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၈) &#8211; (၃၁.၁၀၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/049_4.11.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၄၉) &#8211; (၄.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/050_8.11.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၀) &#8211; (၈.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/053_18.11.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၃) &#8211; (၁၈.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/054_11.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၄) &#8211; (၁၁.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/055_12.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၅) &#8211; (၁၂.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/056_13.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၆) – (၁၃.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/057_14.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၇) – (၁၄.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/058_15.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၈) – (၁၅.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/059_15.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၅၉) – (၁၆.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/060_17.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၀) – (၁၇.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/061_18.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၁) – (၁၈.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/062_20.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၂) – (၂၀.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/063_21.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၃) – (၂၁.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/064_22.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၄) – (၂၂.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/065_23.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၅) – (၂၃.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/066_24.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၆) – (၂၄.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/067_26.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၇) – (၂၆.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/068_27.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၈) – (၂၇.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/069_28.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၆၉) – (၂၈.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/070_31.12.2017.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၀) – (၃၁.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/071_2.1.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၁) – (၂.၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/072_17.3.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၂) – (၁၇.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/073_31.3.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၃) – (၃၁.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/074_23.4.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၄) (၂၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/075_25.4.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၅) (၂၅.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/076_07.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၆) (၇.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/077_08.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၇) (၈.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/078_09.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၈) (၉.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/079_10.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၇၉) (၁၀.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/080_11.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၀) (၁၁.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/081_12.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၁) (၁၂.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/082_13.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၂) (၁၃.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/083_14.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၃) (၁၄.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/084_15.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၄) (၁၅.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/086_24.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၆) (၂၄.၆.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/087_25.6.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၇) (၂၅.၆.၂၀၁၈)</span></a><br />
(တရားေတာ္အစပိုင္းမပါရိွေသးပါ။)</p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/088_07.7.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၈) (၇.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/089_08.7.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၈၉) (၈.၇.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/MaHtayMyat-Great-Talk/090_14.7.2018.mp3"><span style="color: #ffcc00;">မေထရ္ျမတ္တို႔၏ အမွတ္တရ စကားမ်ား အပိုင္း (၉၀) (၁၄.၇.၂၀၁၈)</span></a></p>
<h5><span style="color: #339966;">၂၀၁၇ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္အသစ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Dec/30.12.2017.mp3"><span style="color: #ffcc00;">ပညာ ဥစၥာ ႀကိဳးစား႐ွာ (၃၀.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Dec/29.12.2017.mp3"><span style="color: #ffcc00;">ပညာ႐ွိသူေတာ္ေကာင္းတို႔၏ အဆုံးအမျဖင့္ ဘဝကိုပုံေဖာ္ျခင္း (၂၉.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Dec/20.12.2017.mp3"><span style="color: #ffcc00;">ကိုယ္က်င့္တရားႏွင့္ပညာစြမ္းအား (၂၀.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Dec/16.12.2017.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးပုဂၢိဳလ္ (၁၆.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Dec/10.12.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၁၀.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Dec/9.12.2017.mp3"><span style="color: #ffcc00;">သံသရာဘ၀ရိွၾကရျခင္းအေၾကာင္းတရားေတာ္ (၉.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Nov/26.11.2017.mp3"><span style="color: #ffcc00;">ကမာၻတည္သေရြ႕အေၾကာင္း (၂၆.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/29.10.2017.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးျဖစ္ေအာင္ၾကိဳးစားျခင္း (၂၉.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/27.10.2017.mp3"><span style="color: #ffcc00;">ကထိန္အလွဴ အႏုေမာဒနာတရားေတာ္ (၂၇.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/25.10.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂၅.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/18.10.2017.mp3"><span style="color: #ffcc00;">တရား႐ွိေနသမွ် ဘုရား႐ွိေနသည္ (၁၈.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/14.10.2017.mp3"><span style="color: #ffcc00;">သာသနာ မကြယ္မွီ ႀကိဳးစားၾက (၁၄.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/13.10.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၁၃.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/12.10.2017.mp3"><span style="color: #ffcc00;">ကထိန္အႏုေမာဒနာတရားေတာ္ &#8211; ယကၠန္းစင္ေတာင္ (၁၂.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/5.10.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ &#8211; ဓမၼဒီပ ဗုဒၶစာေပသင္တန္း (၅.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/4.10.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ &#8211; ျမိဳ႕ေတာ္ေဆးရုံ(၄.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/2.10.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၂.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/1.10.2017-5pm.mp3"><span style="color: #ffcc00;">ေရႊက်င္ဂိုဏ္း သံဃာေတာ္မ်ားအား ေဟာၾကားေပးအပ္ေသာ ၾသ၀ါဒတရားေတာ္(၁.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/Oct/1.10.2017.mp3"><span style="color: #ffcc00;">ေမတၱသုတ္ပရိတ္တရားေတာ္ ႏွင့္ အႏုေမာဒနာတရားေတာ္ (၁.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/30.9.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၃၀.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/28.9.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ &#8211; မႏၱေလးတကၠသိုလ္(၂၈.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/27.9.2017.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ &#8211; မႏၱေလးေဆးရုံၾကီး (၂၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/21.8.2017.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏စီးပြားေရးၾသ၀ါဒ (၂၁.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/19.8.2017.mp3"><span style="color: #ffcc00;">ေမြးေန႔အႏုေမာဒနာတရားေတာ္ (၁၉.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/18.8.2017.mp3"><span style="color: #ffcc00;">အသိတရားရိွသူႏွင့္အသိတရားမရိွသူ (၁၈.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/5.8.2017.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းဆက္ကပ္လႉဒါန္းပြဲ အႏုေမာဒနာတရား (၅.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/4.8.2017.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းဆက္ကပ္လႉဒါန္းပြဲ အႏုေမာဒနာတရား (၄.၈.၂၀၁၇)</span></a></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/31.07.2017.mp3">ကုသိုလ္ေကာင္းမႈျပဳၾကရာ၀ယ္ (၃၁.၇.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/29.07.2017.mp3">ေျပာတဲ့အတိုငး္လုပ္ျခင္းနွင့္လုပ္တဲ့အတိုင္းေျပာျခင္း(၂၉.၇.၂၀၁၇)</a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/26.07.2017.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းဆက္ကပ္လႉဒါန္းပြဲ အႏုေမာဒနာတရား (၂၆.၇.၂၀၁၇)</span></a></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/12.07.2017.mp3">ကာမသုတ္ႏွင့္ျမတ္ဗုဒၶ၏အဆံုးအမ (၁၂.၇.၂၀၁ရ)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/11.07.2017.mp3">ဖႏၵနဇာတ္ႏွင့္ျမတ္ဗုဒၶ၏အဆံုးအမ (၁၁.၇.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/10.07.2017.mp3">ဘ၀သုတ္ကိုေလ့လာသံုးသပ္ျခင္း ( ၁၀.၇.၂၀၁ရ)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/8-7-2017.mp3">သစၥာတရားႏွင့္ေမတၱာစြမ္းအား (၈.၇.၂၀၁ရ) (၀ါဆိုလျပည့္ေန႔)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/26-6-2017.mp3">အႏုေမာဒနာတရား (၂၆.၆.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/18-6-2017.mp3">လူ႔အရည္အခ်င္း (၁၈.၆.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/11-6-2017.mp3">ေဖ်ာက္ႏုိင္ခဲသည့္စိတ္စြဲမ်ား (၁၁.၆.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/10-5-2017.mp3">ကဆုန္လျပည့္ေန႔ ျမတ္ဗုဒၶ၏ ေအာင္ပြဲမ်ား (၁၀.၅.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/9-5-2017.mp3">ျမတ္ဗုဒၶသည္သာလွ်င္တစ္ဆူတည္းေသာဘုရား (၉.၅.၂၀၁၇)</a></span></p>
<p><span style="color: #ffcc00;"><a style="color: #ffcc00;" href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/8.5.2017.mp3">အနဳေမာဒနာ တရားေတာ္ (၈.၅.၂၀၁၇)</a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/24-03-2017.mp3"><span style="color: #ffcc00;">ကရုဏာကမၻာ ျမတ္ခ်မ္းသာအေၾကာင္းတရားေတာ္ (၂၄.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/19-03-2017.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမ သာသနာရွည္ၾကတည္တံ့ေရးအေၾကာင္းတရားေတာ္ (၁၉.၀၃.၂၀၁ရ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/6thday-parchoke-sayardawpayargyi.mp3"><span style="color: #ffcc00;">ဒိေ႒ဒိ႒မတၱံ ၀ိပႆနာက်င့္စဥ္ႏွင့္ အဓိပၸါယ္ရွင္းလင္းခ်က္မ်ား အေၾကာင္းတရားေတာ္ (၁၈.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/17-03-2017.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏သာသနာေတာ္ႏွင့္ အလွဴေတာ္မဂၤလာအေၾကာင္းတရားေတာ္ (၁၇.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/15-03-2017.mp3"><span style="color: #ffcc00;">ႏုလံုးစိတ္၀မ္းေအးခ်မ္းေစႏိုင္သည့္ ျမတ္ဗုဒၶ၏အဆံုးအမ်ား (၁၅.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/12-03-2017.mp3"><span style="color: #ffcc00;">အ႐ွံဴးႏွင့္အျမတ္ (၁၂.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/12-03-2016-Birthday-Anumawdanar.mp3"><span style="color: #ffcc00;">ပါခ်ဳပ္ဆရာေတာ္ဘုရားႀကီးေမြးေန႔ အႏုေမာဒနာတရား (၁၂.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/11-03-2017.mp3"><span style="color: #ffcc00;">ေမြးေန႔ပြဲ၏ အႏွစ္သာရအေၾကာင္း (၁၁.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/10-03-2017.mp3"><span style="color: #ffcc00;">ေျဖာင့္မတ္သည့္ စိတ္ထားအေၾကာင္း (၁၀.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/09-03-2017.mp3"><span style="color: #ffcc00;">အမ်ားေကာင္းက်ိဳး သယ္ပိုးရြက္ေဆာင္ျခင္း (၀၉.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/6-03-2017.mp3"><span style="color: #ffcc00;">ကံၾကမၼာႏွင့္သံသရာအေၾကာင္း (၆.၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/5-03-2017.mp3"><span style="color: #ffcc00;">ဗာဟိယသုတ္ႏွင့္ဝိပႆနာအလုပ္ေပးတရား (၅.၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/04-03-2017.mp3"><span style="color: #ffcc00;">ဝကၠလိမေထရ္ျမတ္၏ ဘဝႏွင့္ဓမၼမ်ား (၀၄.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/01-03-2017.mp3"><span style="color: #ffcc00;">ရခဲေသာလူဘဝႏွင့္ ရယူရမည့္အႏွစ္သာရ (၀၁.၀၃.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/26-02-2017.mp3"><span style="color: #ffcc00;">အ႐ွင္အာနႏၵာ၏ အဆုံးအမစကား (၂၆.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/022-15-02-2017-thinkharya.mp3"><span style="color: #ffcc00;">သခၤါရဟူသမွ် မတည္ျမဲျခင္း အေၾကာင္းရိွၾက၏ (၁၅.၀၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/021-13-02-2017-human-basic-ethic.mp3"><span style="color: #ffcc00;">လူတို႔၏အေျခခံကိုယ္က်င့္တရား (၁၃.၀၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/020-12-2-2017.mp3"><span style="color: #ffcc00;">အႏိုင္ယူျခင္းႏွင့္ညႇာတာျခင္း (၁၂.၀၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/019-06-02-2017-QandA.mp3"><span style="color: #ffcc00;">အထက္တန္းေက်ာင္းသူ/ေက်ာင္းသားေလးမ်ား၏ ေမးခြန္းမ်ားေျဖၾကားျခင္း &#8211; ၃ (၀၆.၀၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/018-05-02-2017-QandA.mp3"><span style="color: #ffcc00;">အထက္တန္းေက်ာင္းသူ/ေက်ာင္းသားေလးမ်ား၏ ေမးခြန္းမ်ားေျဖၾကားျခင္း &#8211; ၂ (၀၅.၀၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/017-04-02-2017-QandA.mp3"><span style="color: #ffcc00;">အထက္တန္းေက်ာင္းသူ/ေက်ာင္းသားေလးမ်ား၏ ေမးခြန္းမ်ားေျဖၾကားျခင္း &#8211; ၁ (၀၄.၀၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/016-30-01-2017-dhamma-ko-tanphoe-htarchin.mp3"><span style="color: #ffcc00;">ဓမၼကို တန္ဖိုးထားျခင္းတရားေတာ္ (၃၀.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/1-02-2017.mp3"><span style="color: #ffcc00;">ပုဏၰားအိုႀကီးကို ကယ္တင္ျခင္း (၁.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/015-29-01-2017-piti-aphityasone-kutho.mp3"><span style="color: #ffcc00;">ပီတိအျဖစ္ရဆုံး ကုသိုလ္အေၾကာင္းတရားေတာ္ (၂၉.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/014-28-01-2017.mp3"><span style="color: #ffcc00;">သံသရာဘ၀မွာ ႏွစ္ႀကိမ္သာဆံုေတြ႔ၾကသူမ်ားအေၾကာင္းတရားေတာ္ (၂၈.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/25.1.2017.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာမွာ ျဗဟၼယာနအေၾကာင္းတရားေဒသနာေတာ္(၂၅.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/012-11-1-2-17-waymarlathote.mp3"><span style="color: #ffcc00;">ေ၀လာမသုတ္ အႏွစ္ခ်ဳပ္ (၁၁.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/011-10-1-2017-lupyikatayarpwe.mp3"><span style="color: #ffcc00;">လူ႔ျပည္ကတရားပြဲမ်ားႏွင့္နတ္မ်ားအေၾကာင္း (၁၀.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/010-10-1-2017-batdarlithote-lecture.mp3"><span style="color: #ffcc00;">ဘဒၵါလိသုတ္ ပို႔ခ်ခ်က္ (၁၀.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/009-9-1-2017-kilargiyithote-lecture.mp3"><span style="color: #ffcc00;">ကီဋာဂီရိသုတ္ ပို႔ခ်ခ်က္ (၉.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/008-9-1-2017-htarwayakaungmu.mp3"><span style="color: #ffcc00;">ထာ၀ရေကာင္းမူျဖင့္ ေလာကကိုအက်ိဳးျပဳသူ (၉.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/007-8-1-2017-aikpyawchin-and-noekyarchin.mp3"><span style="color: #ffcc00;">အိပ္ေပ်ာ္ျခင္းႏွင့္ႏိွဳးၾကားျခင္း (၈.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/006-8-1-2017-chanthar4par.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ခ်မ္းသာေလးပါးအေၾကာင္း (၈.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/005-7-1-2017-satethawkako-phalsharchin.mp3"><span style="color: #ffcc00;">စိတ္ေသာကကိုဖယ္ရွားျခင္း (၇.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/004-6-1-2017-myatbuddhaei-asoneama.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမတရား (၆.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/003-6-1-2017-kantayar.mp3"><span style="color: #ffcc00;">ကံတရား၏တံု႔ျပန္မူသဘာ၀ (၆.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/002-5-1-2017-QandA.mp3"><span style="color: #ffcc00;">ဓမၼေမးခြန္းႏွင့္အေျဖမ်ား (၅.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/013-04-01-2017.mp3"><span style="color: #ffcc00;">အၾကင္နာတရား ပညာစြမ္းအားျဖင့္ ေလာကသားတို႔ကိုကယ္တင္သူ(၄.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/001-2017newyearspeak.mp3"><span style="color: #ffcc00;">၂၀၁ရခုႏွစ္ ႏွစ္သစ္မဂၤလာၾသ၀ါဒကထာ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;"> မိလိႏၵမင္းႏွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶ၀ါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ားတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/001.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁) (၉.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/002.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂) (၁၀.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/003.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၃) (၁၁.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/004.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၄) (၁၂.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/005.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၅) (၁၃.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/006.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၆) (၁၄.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/007.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၇) (၁၅.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/008.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၈) (၁၆.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/009.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၉) (၁၇.၆.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/010.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၀) (၁.၇.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/011.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၁) (၂.၇.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/012.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၂) (၄.၇.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/013.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၃) (၅.၇.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/014.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၄) (၂၂.၁၁.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/015.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၅) (၁၂.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/016.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၆) (၁၄.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/017.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၇) (၁၆.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/018.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၈) (၂၁.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/019.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၁၉) (၂၂.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/020.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၀) (၂၃.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/021.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၁) (၂၈.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/022.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၂) (၃၀.၁၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/023.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၃) (၁၂.၁.၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/024.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၄) (၁၅.၁.၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/025.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၅) (၂၂.၁.၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Milainda-QandA/026.mp3"><span style="color: #ffcc00;">မိလိႏၵမင္းနွင့္ရွင္နာဂေသနတို႔၏ ဗုဒၶဝါဒေရးရာ အေျခအတင္ေျပာဆိုခ်က္မ်ား အပိုင္း (၂၆) (၂၃.၁.၁၇)</span></a></p>
<p>&nbsp;</p>

<p>&nbsp;</p>
<h5><span style="color: #339966;"> ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/14-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၁) &#8211; (၁၄.၄.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/15-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၂) &#8211; (၁၅.၄.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/16-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၃) &#8211; (၁၆.၄.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/18-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၄) &#8211; (၁၈.၄.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/19-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၅) &#8211; (၁၉.၄.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/20-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၆) &#8211; (၂၀.၄.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017/21-04-2017.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အလုပ္အေကၽြး ရဟန္းေတာ္မ်ား အပိုင္း(၇) &#8211; (၂၁.၄.၂၀၁၇)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;"> ျမတ္ဗုဒၶ၏ ဂုဏ္ေတာ္တရားေတာ္မ်ား</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/083.mp3"><span style="color: #ffcc00;">၁။ ျမတ္ဗုဒၶ၏ အရဟံဂုဏ္ေတာ္ (၁၃.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/084.mp3"><span style="color: #ffcc00;">၂။ ျမတ္ဗုဒၶ၏ သမၼာသမၺဳဒၶဂုဏ္ေတာ္ (၁၄.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/085.mp3"><span style="color: #ffcc00;">၃။ ျမတ္ဗုဒၶ၏ ဝိဇၨာစရဏသမၺႏၷဂုဏ္ေတာ္ (၁၅.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/086.mp3"><span style="color: #ffcc00;">၄။ ျမတ္ဗုဒၶ၏ သုဂေတာ္ဂုဏ္ေတာ္ (၁၆.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/087.mp3"><span style="color: #ffcc00;">၅။ ျမတ္ဗုဒၶ၏ ေလာကဝိဒူဂုဏ္ေတာ္ (၁၇.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/088.mp3"><span style="color: #ffcc00;">၆။ ျမတ္ဗုဒၶ၏ အႏုတၱေရာပုရိသဒမၼသာရထိဂုဏ္ေတာ္ (၂၃.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/089.mp3"><span style="color: #ffcc00;">၇။ ျမတ္ဗုဒၶ၏ သတၱာေဒဝမႏုႆနံဂုဏ္ေတာ္ (၂၇.၄.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/090.mp3"><span style="color: #ffcc00;">၈။ ျမတ္ဗုဒၶ၏ ဗုဒၶဂုဏ္ေတာ္ (၁၈.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/091.mp3"><span style="color: #ffcc00;">၉။ ျမတ္ဗုဒၶ၏ ဘဂဝါဂုဏ္ေတာ္ (၁၆.၈.၂၀၁၄)</span></a></span></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ပရိတ္ႀကီး (၁၁)သုတ္အႏွစ္ခ်ဳပ္ တရားေတာ္မ်ား </span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/268-ndml.mp3"><span style="color: #ffcc00;">၁။ မဂၤလသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/333.mp3"><span style="color: #ffcc00;">၂။ ရတနသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/334.mp3"><span style="color: #ffcc00;">၃။ ရတနသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/335.mp3"><span style="color: #ffcc00;">၄။ ရတနသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/267-ndml.mp3"><span style="color: #ffcc00;">၅။ ေမတၱသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/296-ndml.mp3"><span style="color: #ffcc00;">၆။ ခႏၶသုတ္အႏွစ္ခ်ဳပ္ (အႏၱရယ္ကာကြယ္ျခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/maw-ya-thote.mp3"><span style="color: #ffcc00;">၇။ ေမာရသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/wit-ta-thote.mp3"><span style="color: #ffcc00;">၈။ ၀႗သုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/dazatka-thote.mp3"><span style="color: #ffcc00;">၉။ ဓဇဂၢသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/803.mp3"><span style="color: #ffcc00;">၁၀။ အာဋာနာဋိယသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/804.mp3"><span style="color: #ffcc00;">၁၁။ အာဋာနာဋိယသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/805.mp3"><span style="color: #ffcc00;">၁၂။ အာဋာနာဋိယသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/806.mp3"><span style="color: #ffcc00;">၁၃။ အာဋာနာဋိယသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/807.mp3"><span style="color: #ffcc00;">၁၄။ အာဋာနာဋိယသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/009.mp3"><span style="color: #ffcc00;">၁၅။ အဂၤုလိမာလသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/368.mp3"><span style="color: #ffcc00;">၁၆။ ေဗာဇၥ်ဂၤသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/634.mp3"><span style="color: #ffcc00;">၁၇။ ပုဗၺဏွသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<h5><span style="color: #339966;">မဟာသတိပ႒ာနသုတ္အႏွစ္ခ်ဳပ္ တရားေတာ္မ်ား</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.06/067-ndml.mp3"><span style="color: #ffcc00;">၁။ မဟာသတိပ႒ာနသုတ္အႏွစ္ခ်ဳပ္ (နိဒါန္း)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.06/068-ndml.mp3"><span style="color: #ffcc00;">၂။ မဟာသတိပ႒ာနသုတ္အႏွစ္ခ်ဳပ္ (ကာယာႏုပႆနာ)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.06/069-ndml.mp3"><span style="color: #ffcc00;">၃။ မဟာသတိပ႒ာႏုသုတ္အႏွစ္ခ်ဳပ္ (ေ၀ဒနာႏုပႆနာ)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.06/070-ndml.mp3"><span style="color: #ffcc00;">၄။ မဟာသတိပ႒ာႏုသုတ္အႏွစ္ခ်ဳပ္ (စိတၱာႏုပႆနာ)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.06/071-ndml.mp3"><span style="color: #ffcc00;">၅။ မဟာသတိပ႒ာႏုသုတ္အႏွစ္ခ်ဳပ္ (ဓမၼာႏုပႆနာ)</span></a></span></p>
<h5><span style="color: #339966;"> ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ တရားေတာ္မ်ား</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/092.mp3"><span style="color: #ffcc00;">၁။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၁ (၃.၁၀.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/093.mp3"><span style="color: #ffcc00;">၂။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၂ (၄.၁၀.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/094.mp3"><span style="color: #ffcc00;">၃။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၃ (၅.၁၀.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/095.mp3"><span style="color: #ffcc00;">၄။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၄ (၆.၁၀.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/096.mp3"><span style="color: #ffcc00;">၅။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၅ (၇.၁၀.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/097.mp3"><span style="color: #ffcc00;">၆။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၆ (၈.၁၀.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/098.mp3"><span style="color: #ffcc00;">၇။ ဝိပႆနာရႈဖြယ္ ေတာေလးဆယ္ &#8211; ၇ (၉.၁၀.၂၀၁၃)</span></a></span></p>
<h5><span style="color: #339966;"> ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/001.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/002.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/003.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/004.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/005.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/006.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၆။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/007.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၇။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/008.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၈။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/009.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၉။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/010.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၀။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/011.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၁။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/012.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၂။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/013.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၃။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/014.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၄။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/015.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၅။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/016.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၆။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/017.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၇။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/018.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၈။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/019.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၉။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၁၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/020.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၀။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/021.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၁။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/022.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၂။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/023.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၃။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/024.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၄။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/025.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၅။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/026.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၆။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/027.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၇။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/028.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၈။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/029.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၉။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၂၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/030.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၀။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/031.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၁။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/032.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၂။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/033.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၃။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/034.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၄။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/035.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၅။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/036.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၆။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/037.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၇။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/038.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၈။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/039.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၉။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၃၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/040.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၀။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/041.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၁။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/042.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၂။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/043.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၃။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/044.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၄။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/045.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၅။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/046.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၆။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/047.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၇။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/048.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၈။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/049.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၉။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၄၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/050.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅၀။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/051.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅၁။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/052.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅၂။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/053.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅၃။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/054.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅၄။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/BuddhaThaMeeTaw/055.mp3" target="_blank&quot;"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅၅။ ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား တရားေဒသနာေတာ္ (၅၅)</span></span></a></p>
<p>&nbsp;</p>
<h4><span style="color: #339966;">ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ႀကိဳးပမ္းခ်က္ ေဒသနာေတာ္ တရားေတာ္မ်ား စ/ဆံုး</span></h4>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/01.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁) (၁၁.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/02.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂) (၁၂.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/03.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃) (၁၃.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/04.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄) (၁၄.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/05.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅) (၁၅.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/6-Dr-Nandamalabhivamsa-DVD4.mp3"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆) (၁၆.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/07.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇) (၁၇.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/08.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၈) (၁၈.၇.၂၀၁၃) (ဇမၺဴသီရိဗိမာန္ေတာ္)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/09.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/10.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/11.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/12.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/13.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/14.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/15.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/16.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/17.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/18.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/19.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၁၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/20.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/21.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/22.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/23.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/24.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/25.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/26.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/27.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/28.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/29.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၂၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၂၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/30.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/31.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/32.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/33.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/34.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/35.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၅)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/36.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၆)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/37.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/38.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/39.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၃၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၃၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/40.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/41.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/42.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၂)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/43.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၃)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/44.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၄၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၄)</span></span></a></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/45.mp3" target="_blank"><span style="color: #ffcc00;">၄၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၅) (၁၉.၆.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/46.mp3" target="_blank"><span style="color: #ffcc00;">၄၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၆) (၂၀.၆.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/47.mp3" target="_blank"><span style="color: #ffcc00;">၄၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၇) (၁၅.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/48.mp3" target="_blank"><span style="color: #ffcc00;">၄၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၈) )</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/49.mp3" target="_blank"><span style="color: #ffcc00;">၄၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၄၉)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/50.mp3" target="_blank"><span style="color: #ffcc00;">၅၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၀)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/51.mp3" target="_blank"><span style="color: #ffcc00;">၅၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၁)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/52.mp3" target="_blank"><span style="color: #ffcc00;">၅၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၂)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/53.mp3" target="_blank"><span style="color: #ffcc00;">၅၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/54.mp3" target="_blank"><span style="color: #ffcc00;">၅၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/55.mp3" target="_blank"><span style="color: #ffcc00;">၅၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၅)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/56.mp3" target="_blank"><span style="color: #ffcc00;">၅၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၆)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/57.mp3" target="_blank"><span style="color: #ffcc00;">၅၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၇)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/58.mp3" target="_blank"><span style="color: #ffcc00;">၅၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၈)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/59.mp3" target="_blank"><span style="color: #ffcc00;">၅၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၅၉)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/60.mp3" target="_blank"><span style="color: #ffcc00;">၆၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၀)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/61.mp3" target="_blank"><span style="color: #ffcc00;">၆၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၁)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/62.mp3" target="_blank"><span style="color: #ffcc00;">၆၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၂)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/63.mp3" target="_blank"><span style="color: #ffcc00;">၆၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/64.mp3" target="_blank"><span style="color: #ffcc00;">၆၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/65.mp3"><span style="color: #ffcc00;">၆၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၅)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/66.mp3"><span style="color: #ffcc00;">၆၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၆)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/67.mp3"><span style="color: #ffcc00;">၆၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၇)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/068.mp3" target="_blank"><span style="color: #ffcc00;">၆၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၈) </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/069.mp3" target="_blank"><span style="color: #ffcc00;">၆၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၆၉)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/70.mp3"><span style="color: #ffcc00;">၇၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၀)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/71.mp3" target="_blank"><span style="color: #ffcc00;">၇၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၁)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/72.mp3" target="_blank"><span style="color: #ffcc00;">၇၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၂)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/73.mp3" target="_blank"><span style="color: #ffcc00;">၇၃။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/74.mp3" target="_blank"><span style="color: #ffcc00;">၇၄။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/75.mp3" target="_blank"><span style="color: #ffcc00;">၇၅။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၅) (၁.၁၂.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/76.mp3" target="_blank"><span style="color: #ffcc00;">၇၆။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၆) (၂.၁၂.၂၀၁၄)</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/077.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၇၇။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၇)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/078.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၇၈။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၈)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/079.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၇၉။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၇၉)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/080.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၈၀။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၈၀)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/081.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၈၁။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၈၁)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/LawKaTharToAtwat/082.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၈၂။ ေလာကသားတို႔အတြက္ ျမတ္ဗုဒၶ၏ ႀကိဳးပမ္းခ်က္ (အပိုင္း-၈၂)</span></span></a></p>
<h5><span style="color: #339966;">သစၥာေဒသနာ ဓမၼစၾကာတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.08/076-ndml.mp3"><span style="color: #ffcc00;">သစၥာေဒသနာ ဓမၼစၾကာ-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.08/077-ndml.mp3"><span style="color: #ffcc00;">သစၥာေဒသနာ ဓမၼစၾကာ-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.08/078-ndml.mp3"><span style="color: #ffcc00;">သစၥာေဒသနာ ဓမၼစၾကာ-၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.08/079-ndml.mp3"><span style="color: #ffcc00;">သစၥာေဒသနာ ဓမၼစၾကာ-၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.08/080-ndml.mp3" target="_blank"><span style="color: #ffcc00;">အနတၱလကၡဏာသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<h6><a title="&quot;အနတၱလကၡဏသုတ္ အႏွစ္ခ်ဳပ္ တရားေဒသနာေတာ္&quot;" href="https://www.thitsarparamisociety.com/wp-content/uploads/Books/DrNandamalabhivamsa/anatta.pdf" target="_blank"><span style="color: #33cccc;">&#8220;အနတၱလကၡဏသုတ္ အႏွစ္ခ်ဳပ္ တရားေဒသနာေတာ္&#8221; PDF </span></a></h6>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ပ႒ာန္းျမတ္ေဒသနာတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/036-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/037-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/038-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/039-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/040-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/041-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/042-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/043-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/044-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/045-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/046-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/047-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/048-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/049-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/050-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/051-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/052-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.04/053-ndml.mp3"><span style="color: #ffcc00;">ပ႒ာန္းျမတ္ေဒသနာေတာ္ၾကီး အပိုင္း(၁၈)</span></a></p>
<h5><span style="color: #339966;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္းတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/054-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/055-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/056-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/057-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/058-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/059-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/060-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/061-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/062-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/063-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/064-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/065-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.05/066-ndml.mp3"><span style="color: #ffcc00;">ပ႗ိစၥသမုပၸါဒ္ကို ပဌာန္းနည္းျဖင့္ေလ့လာသံုးသပ္ျခင္း အပို္င္း (၁၃)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ေဗာဓိပကိၡယတရားကို ေလ့လာသံုးသပ္ျခင္းတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/084.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/085.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/086.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/087.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/088.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၅</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/089.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၆</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/090.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၇</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/091.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၈</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/092.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၉</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/093.ndml%202.mp3"><span style="color: #ffcc00;">ေဗာဓိပကၡိယတရားကို ေလ့လာသံုးသပ္ျခင္း – ၁၀</span></a></p>
<h5><span style="color: #339966;">နိဗၺာန္တံခါးႀကီးဖြင္႔ေတာ္မူပါတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0059-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္တံခါးႀကီးဖြင္႔ေတာ္မူပါ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0060-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္တံခါးႀကီးဖြင္႔ေတာ္မူပါ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0061-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္တံခါးႀကီးဖြင္႔ေတာ္မူပါ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0062-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္တံခါးႀကီးဖြင္႔ေတာ္မူပါ (၄)</span></a></p>
<h5><span style="color: #339966;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/026-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/027-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/028-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/029-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/030-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/031-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/032-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/033-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/034-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.03/035-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရားကို အစုလိုက္ေလ့လာျခင္း အပိုင္း(၁၀)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ေဝဒနာတရားကို ေလ့လာသံုးသပ္ျခင္း</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/053.ndml%202.mp3"><span style="color: #ffcc00;">ေဝဒနာတရားကို ေလ့လာသံုးသပ္ျခင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/054.ndml%202.mp3"><span style="color: #ffcc00;">ေဝဒနာတရားကို ေလ့လာသံုးသပ္ျခင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/055.ndml%202.mp3"><span style="color: #ffcc00;">ေဝဒနာတရားကို ေလ့လာသံုးသပ္ျခင္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/056.ndml%202.mp3"><span style="color: #ffcc00;">ေဝဒနာတရားကို ေလ့လာသံုးသပ္ျခင္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/057.ndml%202.mp3"><span style="color: #ffcc00;">ေဝဒနာတရားကို ေလ့လာသံုးသပ္ျခင္း (၅)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ပါရမီ (၁၀)ပါး ျမတ္တရား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/175.ndml%202.mp3"><span style="color: #ffcc00;">ပါရမီ (၁၀)ပါး ျမတ္တရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/176.ndml%202.mp3"><span style="color: #ffcc00;">ပါရမီ (၁၀)ပါး ျမတ္တရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/177.ndml%202.mp3"><span style="color: #ffcc00;">ပါရမီ (၁၀)ပါး ျမတ္တရား (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/178.ndml%202.mp3"><span style="color: #ffcc00;">ပါရမီ (၁၀)ပါး ျမတ္တရား (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/179.ndml%202.mp3"><span style="color: #ffcc00;">ပါရမီ (၁၀)ပါး ျမတ္တရား (၅)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">စင္ၾကယ္မွု(၇)ပါးတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/770.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မွု(၇)ပါး (အပိုင္း -၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/771.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မွု(၇)ပါး (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/772.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မွု(၇)ပါး (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/773.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မွု(၇)ပါး (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/774.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မွု(၇)ပါး (အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/775.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မွု(၇)ပါး (အပိုင္း-၆)</span></a></p>
<h5><span style="color: #339966;">ဝိဓူရပညာရွိအေၾကာင္း တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016-thingyan/April-12.mp3"><span style="color: #ffcc00;">ဝိဓူရပညာရွိအေၾကာင္း တရားေဒသနာေတာ္ အပိုင္း(၁) (၁၂.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016-thingyan/April-13.mp3"><span style="color: #ffcc00;">ဝိဓူရပညာရွိအေၾကာင္း တရားေဒသနာေတာ္ အပိုင္း(၂) (၁၃.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016-thingyan/April-14.mp3"><span style="color: #ffcc00;">ဝိဓူရပညာရွိအေၾကာင္း တရားေဒသနာေတာ္ အပိုင္း(၃) (၁၄.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016-thingyan/April-15.mp3"><span style="color: #ffcc00;">ဝိဓူရပညာရွိအေၾကာင္း တရားေဒသနာေတာ္ အပိုင္း(၄) (၁၅.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016-thingyan/April-16.mp3"><span style="color: #ffcc00;">ဝိဓူရပညာရွိအေၾကာင္း တရားေဒသနာေတာ္ အပိုင္း(၅) (၁၆.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016-thingyan/April-17.mp3"><span style="color: #ffcc00;">ဝိဓူရပညာရွိအေၾကာင္း တရားေဒသနာေတာ္ အပိုင္း(၆) (၁၇.၄.၂၀၁၆)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ားတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/651.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ား (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/652.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ား (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/653.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ား (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/654.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ား (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/655.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ား (အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/656.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အလုပ္အေကြ်းရဟန္းမ်ား (အပိုင္း-၆)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ပေစၥကဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/868.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ဓမၼအျမင္(အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/869.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/870.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/871.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/872.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/873.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/874.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/875.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/876.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/877.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/878.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/879.mp3"><span style="color: #ffcc00;">ပေစၥက ဗုဒၶအရွင္ျမတ္တုိ႕၏ ဘ၀ႏွင့္ ဓမၼအျမင္(အပိုင္း-၁၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ရွင္ရာဟုလာ၏ဘ၀ႏွင့္ ျမတ္ဗုဒၶ၏အဆံုးအမ</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/014.ndml%202.mp3"><span style="color: #ffcc00;">ရွင္ရာဟုလာ၏ဘဝႏွင့္ျမတ္ဗုဒၶ၏အဆံုးအမ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/015.ndml%202.mp3"><span style="color: #ffcc00;">ရွင္ရာဟုလာ၏ဘဝႏွင့္ ျမတ္ဗုဒၶ၏အဆံုးအမ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/016.ndml%202.mp3"><span style="color: #ffcc00;">ရွင္ရာဟုလာ၏ဘဝႏွင့္ ျမတ္ဗုဒၶ၏အဆံုးအမ (၃)</span></a></p>
<h5><span style="color: #339966;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/109.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၁ (၂.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/110.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၂ (၃.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/111.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၃ (၁၇.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/112.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၄ (၁၈.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/113.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၅ (၁၉.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/114.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၆ (၂၀.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/115.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၇ (၂၂.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/116.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၈ (၂၃.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/117.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၉ (၂၄.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/118.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၁၀ (၂၅.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/119.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသားမ်ား – ၁၁ (၂၆.၃.၂၀၁၄)</span></a></p>
<h5><span style="color: #339966;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/921.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး(၁၀)ဦး(အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/922.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး(၁၀)ဦး(အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/923.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး(၁၀)ဦး(အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/924.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး(၁၀)ဦး(အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/925.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး(၁၀)ဦး(အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/926.mp3"><span style="color: #ffcc00;">ဘာသာေရးထူးခြ်န္သူ အမ်ိဳးသမီး(၁၀)ဦး(အပိုင္း-၆)</span></a></p>
<h5><span style="color: #339966;">ေကာသလအိပ္မက္ႏွင္႔ ယေန႔ကမၻာတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/138.mp3"><span style="color: #ffcc00;">ေကာသလအိပ္မက္ႏွင္႔ ယေန႔ကမၻာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/139.mp3"><span style="color: #ffcc00;">ေကာသလအိပ္မက္ႏွင္႔ ယေန႔ကမၻာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/140.mp3"><span style="color: #ffcc00;">ေကာသလအိပ္မက္ႏွင္႔ ယေန႔ကမၻာ (၃)</span></a></p>
<h5><span style="color: #339966;">ခုပါလိသုတ္မွ ဗုဒၶနွင့္ နိဂဏၰတို႔၏ မတူညီေသာ ကမၼဝါဒမ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/421-ndml(27.9.16).mp3"><span style="color: #ffcc00;">ခုပါလိသုတ္မွ ဗုဒၶနွင့္ နိဂဏၰတို႔၏ မတူညီေသာ ကမၼဝါဒမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/422-ndml(28.9.16).mp3"><span style="color: #ffcc00;">ခုပါလိသုတ္မွ ဗုဒၶနွင့္ နိဂဏၰတို႔၏ မတူညီေသာ ကမၼဝါဒမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/423-ndml(29.9.16).mp3"><span style="color: #ffcc00;">ခုပါလိသုတ္မွ ဗုဒၶနွင့္ နိဂဏၰတို႔၏ မတူညီေသာ ကမၼဝါဒမ်ား (၃)</span></a></p>
<h5><span style="color: #339966;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/739.mp3"><span style="color: #ffcc00;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ား (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/740.mp3"><span style="color: #ffcc00;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ား(အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/741.mp3"><span style="color: #ffcc00;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ား(အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/742.mp3"><span style="color: #ffcc00;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ား(အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/743.mp3"><span style="color: #ffcc00;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ား(အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/744.mp3"><span style="color: #ffcc00;">စိတ္၌ျဖစ္ပြားအဆိုးတရားတို႔၏လွည္႔စားမႈမ်ား(အပိုင္း-၆)</span></a></p>
<h5><span style="color: #339966;">ဇာတကေဒသနာမွ ျမတ္ဗုဒၶ၏အဆံုးအမမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/120.mp3"><span style="color: #ffcc00;">ဇာတကေဒသနာမွ ျမတ္ဗုဒၶ၏အဆံုးအမမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/121.mp3"><span style="color: #ffcc00;">ဇာတကေဒသနာမွ ျမတ္ဗုဒၶ၏အဆံုးအမမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/122.mp3"><span style="color: #ffcc00;">ဇာတကေဒသနာမွ ျမတ္ဗုဒၶ၏အဆံုးအမမ်ား (၃)</span></a></p>
<h5><span style="color: #339966;">ေတမိကုမၼာရ ဇာတ္ေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0002-NDML.mp3"><span style="color: #ffcc00;">ေတမိကုမၼာရ ဇာတ္ေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0003-NDML.mp3"><span style="color: #ffcc00;">ေတမိကုမၼာရ ဇာတ္ေတာ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0001-NDML.mp3"><span style="color: #ffcc00;">ေတမိကုမၼာရ ဇာတ္ေတာ္ (၃)</span></a></p>
<h5><span style="color: #339966;">ဒုဂၢတိဘုံသားတုိ႕၏ အမွာစကားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/793.mp3"><span style="color: #ffcc00;">ဒုဂၢတိဘုံသားတုိ႕၏ အမွာစကား (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/794.mp3"><span style="color: #ffcc00;">ဒုဂၢတိဘုံသားတုိ႕၏ အမွာစကား (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/795.mp3"><span style="color: #ffcc00;">ဒုဂၢတိဘုံသားတုိ႕၏ အမွာစကား (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/796.mp3"><span style="color: #ffcc00;">ဒုဂၢတိဘုံသားတုိ႕၏ အမွာစကား (အပိုင္း-၄)</span></a></p>
<h5><span style="color: #339966;">ဒေလႅခသုတ္ အႏွစ္ခ်ဳပ္ တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/910.mp3"><span style="color: #ffcc00;">ဒေလႅခသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/911.mp3"><span style="color: #ffcc00;">ဒေလႅခသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/912.mp3"><span style="color: #ffcc00;">ဒေလႅခသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/913.mp3"><span style="color: #ffcc00;">ဒေလႅခသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/914.mp3"><span style="color: #ffcc00;">ဒေလႅခသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၅)</span></a></p>
<h5><span style="color: #339966;">ဓမၼအေမးႏွင္႔အေျဖမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/342-ndml.mp3"><span style="color: #ffcc00;">ဓမၼအေမးႏွင္႔အေျဖမ်ား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/343-ndml.mp3"><span style="color: #ffcc00;">ဓမၼအေမးႏွင္႔အေျဖမ်ား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/344-ndml.mp3"><span style="color: #ffcc00;">ဓမၼအေမးႏွင္႔အေျဖမ်ား(၃)</span></a></p>
<h5><span style="color: #339966;">ဓမၼသဂၤဏီက်မ္းတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.01/001-ndml.mp3"><span style="color: #ffcc00;">ဓမၼသဂၤဏီက်မ္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.01/002-ndml.mp3"><span style="color: #ffcc00;">ဓမၼသဂၤဏီက်မ္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.01/003-ndml.mp3"><span style="color: #ffcc00;">ဓမၼသဂၤဏီက်မ္း (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.01/004-ndml.mp3"><span style="color: #ffcc00;">ဓမၼသဂၤဏီက်မ္း (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.01/005-ndml.mp3"><span style="color: #ffcc00;">ဓမၼသဂၤဏီက်မ္း (၅)</span></a></p>
<h5><span style="color: #339966;">ပဋိစၥသမုပၸါဒ ဝိဘဂၤက်မ္း သုတၱႏၱဘာဇနိယတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/141.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ ဝိဘဂၤက်မ္း သုတၱႏၱဘာဇနိယ – ၁ (၁၇.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/142.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ ဝိဘဂၤက်မ္း သုတၱႏၱဘာဇနိယ – ၂ (၁၈.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/143.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ ဝိဘဂၤက်မ္း သုတၱႏၱဘာဇနိယ – ၃ (၂၄.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/144.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ ဝိဘဂၤက်မ္း သုတၱႏၱဘာဇနိယ – ၄ (၂၅.၁.၂၀၁၅)</span></a></p>
<h5><span style="color: #339966;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္မ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/732.mp3"><span style="color: #ffcc00;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္မ်ား (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/733.mp3"><span style="color: #ffcc00;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္မ်ား (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/734.mp3"><span style="color: #ffcc00;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္မ်ား (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/735.mp3"><span style="color: #ffcc00;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္မ်ား (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/736.mp3"><span style="color: #ffcc00;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္မ်ား (အပိုင္း-၅)</span></a></p>
<h5><span style="color: #339966;">ပါရာယနေဒသနာ</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/026.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/027.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/028.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/029.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/030.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/031.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/032.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/033.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/034.ndml%202.mp3"><span style="color: #ffcc00;">ပါရာယနေဒသနာ (၉)</span></a></p>
<h5><span style="color: #339966;"> ဗိမာန္ရွင္တို႔၏ ျပန္ၾကားခ်က္မ်ား တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/104.mp3"><span style="color: #ffcc00;">ဗိမာန္ရွင္တို႔၏ ျပန္ၾကားခ်က္မ်ား &#8211; ၁ (၂.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/105.mp3"><span style="color: #ffcc00;">ဗိမာန္ရွင္တို႔၏ ျပန္ၾကားခ်က္မ်ား &#8211; ၂ (၃.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/106.mp3"><span style="color: #ffcc00;">ဗိမာန္ရွင္တို႔၏ ျပန္ၾကားခ်က္မ်ား &#8211; ၃ (၄.၂.၂၀၁၄)</span></a></p>
<h5><span style="color: #339966;">ျဗဟၼဇာလသုတ္ အႏွစ္ခ်ဳပ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/660.mp3"><span style="color: #ffcc00;">ျဗဟၼဇာလသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/661.mp3"><span style="color: #ffcc00;">ျဗဟၼဇာလသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/662.mp3"><span style="color: #ffcc00;">ျဗဟၼဇာလသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/663.mp3"><span style="color: #ffcc00;">ျဗဟၼဇာလသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၄)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဘဝခရီးဝယ္ လမ္းႏွစ္သြယ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/099.mp3"><span style="color: #ffcc00;">ဘဝခရီးဝယ္ လမ္းႏွစ္သြယ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/100.mp3"><span style="color: #ffcc00;">ဘဝခရီးဝယ္ လမ္းႏွစ္သြယ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/101.mp3"><span style="color: #ffcc00;">ဘဝခရီးဝယ္ လမ္းႏွစ္သြယ္ (၃)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">မဟာေ၀ဒလႅသုတ္ အႏွစ္ခ်ဳပ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/788.mp3"><span style="color: #ffcc00;">မဟာေ၀ဒလႅသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/789.mp3"><span style="color: #ffcc00;">မဟာေ၀ဒလႅသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/790.mp3"><span style="color: #ffcc00;">မဟာေ၀ဒလႅသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/791.mp3"><span style="color: #ffcc00;">မဟာေ၀ဒလႅသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/792.mp3"><span style="color: #ffcc00;">မဟာေ၀ဒလႅသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၅)</span></a></p>
<h5><span style="color: #339966;">မာရ္နတ္သို႕တုန္႕ျပန္ေျပာၾကားသည့္ ဘိကၡဳနီတို႕၏ဓမၼစကား တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/062.ndml%202.mp3"><span style="color: #ffcc00;">မာရ္နတ္သို႕တုန္႕ျပန္ေျပာၾကားသည့္ ဘိကၡဳနီတို႕၏ဓမၼစကား – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/063.ndml%202.mp3"><span style="color: #ffcc00;">မာရ္နတ္သို႕တုန္႕ျပန္ေျပာၾကားသည့္ ဘိကၡဳနီတို႕၏ဓမၼစကား – ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/064.ndml%202.mp3"><span style="color: #ffcc00;">မာရ္နတ္သို႕တုန္႕ျပန္ေျပာၾကားသည့္ ဘိကၡဳနီတို႕၏ဓမၼစကား – ၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/065.ndml%202.mp3"><span style="color: #ffcc00;">မာရ္နတ္သို႕တုန္႕ျပန္ေျပာၾကားသည့္ ဘိကၡဳနီတို႕၏ဓမၼစကား – ၄</span></a></p>
<h5><span style="color: #339966;">ျမတ္ဆုနိဗၺာန္အက်င္႔မွန္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/585.mp3"><span style="color: #ffcc00;">ျမတ္ဆုနိဗၺာန္အက်င္႔မွန္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/586.mp3"><span style="color: #ffcc00;">ျမတ္ဆုနိဗၺာန္အက်င္႔မွန္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/587.mp3"><span style="color: #ffcc00;">ျမတ္ဆုနိဗၺာန္အက်င္႔မွန္ (အပိုင္း-၃)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ျမတ္ဗုဒၶ၏ အႏုတၱရိယဂုဏ္(၁၆)ပါးတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/797.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အႏုတၱရိယဂုဏ္(၁၆)ပါး (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/798.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အႏုတၱရိယဂုဏ္(၁၆)ပါး (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/799.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အႏုတၱရိယဂုဏ္(၁၆)ပါး (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/800.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အႏုတၱရိယဂုဏ္(၁၆)ပါး (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/801.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အႏုတၱရိယဂုဏ္(၁၆)ပါး (အပိုင္း-၅)</span></a></p>
<h5><span style="color: #339966;">ျမတ္ဗုဒၶ၏ ေလာကဝိဇယလမ္းစဥ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/944.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ေလာကဝိဇယလမ္းစဥ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/945.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ေလာကဝိဇယလမ္းစဥ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/946.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ေလာကဝိဇယလမ္းစဥ္ (အပိုင္း-၃)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ျမတ္ဗုဒၶႏွင္႔ေကာသလမင္းတို႔ ေတြ႔ဆံုျခင္းမွတ္တမ္းမ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/135.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶႏွင္႔ေကာသလမင္းတို႔ ေတြ႔ဆံုျခင္းမွတ္တမ္းမ်ား – ၁ (၇.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/136.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶႏွင္႔ေကာသလမင္းတို႔ ေတြ႔ဆံုျခင္းမွတ္တမ္းမ်ား – ၂ (၈.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/137.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶႏွင္႔ေကာသလမင္းတို႔ ေတြ႔ဆံုျခင္းမွတ္တမ္းမ်ား – ၃ (၉.၁.၂၀၁၅)</span></a></p>
<h5><span style="color: #339966;">သကၠပဥၥသုတ္လာ ဓမၼေမးခြန္းႏွင့္ အေျဖမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/156.ndml%202.mp3"><span style="color: #ffcc00;">သကၠပဥၥသုတ္လာ ဓမၼေမးခြန္းႏွင့္ အေျဖမ်ား – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/157.ndml%202.mp3"><span style="color: #ffcc00;">သကၠပဥၥသုတ္လာ ဓမၼေမးခြန္းႏွင့္ အေျဖမ်ား -၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/158.ndml%202.mp3"><span style="color: #ffcc00;">သကၠပဥၥသုတ္လာ ဓမၼေမးခြန္းႏွင့္ အေျဖမ်ား – ၃</span></a></p>
<h5><span style="color: #339966;">သဠာယတနာဝိဘဂၤသုတ္ အႏွစ္ခ်ဳပ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/615.mp3"><span style="color: #ffcc00;">သဠာယတနာဝိဘဂၤသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/616.mp3"><span style="color: #ffcc00;">သဠာယတနာဝိဘဂၤသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/617.mp3"><span style="color: #ffcc00;">သဠာယတနာဝိဘဂၤသုတ္ အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<h5><span style="color: #339966;">သုညကမၻာ၏သရုပ္ေဆာင္မႈမ်ားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/626.mp3"><span style="color: #ffcc00;">သုညကမၻာ၏သရုပ္ေဆာင္မႈမ်ား (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/628.mp3"><span style="color: #ffcc00;">သုညကမၻာ၏သရုပ္ေဆာင္မႈမ်ား (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/629.mp3"><span style="color: #ffcc00;">သုညကမၻာ၏သရုပ္ေဆာင္မႈမ်ား (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/630.mp3"><span style="color: #ffcc00;">သုညကမၻာ၏သရုပ္ေဆာင္မႈမ်ား (အပိုင္း-၄)</span></a></p>
<h5><span style="color: #339966;">အရိယသစၥာကိုေလ႔လာသံုးသပ္ျခင္းတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/602.mp3"><span style="color: #ffcc00;">အရိယသစၥာကိုေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၁)</span></a>&gt;</p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/603.mp3"><span style="color: #ffcc00;">အရိယသစၥာကိုေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/604.mp3"><span style="color: #ffcc00;">အရိယသစၥာကိုေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၃)</span></a></p>
<h5><span style="color: #339966;">အမ်ားေကာင္းက်ိဳးရြက္သယ္ပိုးတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/667.mp3"><span style="color: #ffcc00;">အမ်ားေကာင္းက်ိဳးရြက္သယ္ပိုး (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/668.mp3"><span style="color: #ffcc00;">အမ်ားေကာင္းက်ိဳးရြက္သယ္ပိုး (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/669.mp3"><span style="color: #ffcc00;">အမ်ားေကာင္းက်ိဳးရြက္သယ္ပိုး (အပိုင္း-၃)</span></a></p>
<h5><span style="color: #339966;">အာမဂႏၶသုတ္အႏွစ္ခ်ဳပ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/936.mp3"><span style="color: #ffcc00;">အာမဂႏၶသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/937.mp3"><span style="color: #ffcc00;">အာမဂႏၶသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/938.mp3"><span style="color: #ffcc00;">အာမဂႏၶသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<h5><span style="color: #339966;">အာသဝကၡယက်င့္စဥ္တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/137.ndml%202.mp3"><span style="color: #ffcc00;">အာသဝကၡယက်င့္စဥ္ &#8211; ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/138.ndml%202.mp3"><span style="color: #ffcc00;">အာသဝကၡယက်င့္စဥ္ &#8211; ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/139.ndml%202.mp3"><span style="color: #ffcc00;">အာသဝကၡယက်င့္စဥ္ &#8211; ၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/140.ndml%202.mp3"><span style="color: #ffcc00;">အာသဝကၡယက်င့္စဥ္ &#8211; ၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/141.ndml%202.mp3"><span style="color: #ffcc00;">အာသဝကၡယက်င့္စဥ္ &#8211; ၅</span></a></p>
<h5><span style="color: #339966;"> အာနာပါနႆတိသုတ္အႏွစ္ခ်ဳပ္ တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/720.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/721.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/722.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/723.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/724.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိသုတ္အႏွစ္ခ်ဳပ္ (အပိုင္း-၅)</span></a></p>
<h5><span style="color: #339966;">ေအာင္ျမင္ၾကီးပြား လူ႕စြမ္းအားတရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/759.mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ၾကီးပြား လူ႕စြမ္းအား(အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/760.mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ၾကီးပြား လူ႕စြမ္းအား(အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/761.mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ၾကီးပြား လူ႕စြမ္းအား(အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/762.mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ၾကီးပြား လူ႕စြမ္းအား(အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/763.mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ၾကီးပြား လူ႕စြမ္းအား(အပိုင္း-၅)</span></a></p>
<h5><span style="color: #339966;">ဥပနိႆယပစၥည္းကို ေလ႔လာသံုးသပ္ျခင္း တရားေတာ္</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/553.mp3"><span style="color: #ffcc00;">ဥပနိႆယပစၥည္းကို ေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/554.mp3"><span style="color: #ffcc00;">ဥပနိႆယပစၥည္းကို ေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/555.mp3"><span style="color: #ffcc00;">ဥပနိႆယပစၥည္းကို ေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/556.mp3"><span style="color: #ffcc00;">ဥပနိႆယပစၥည္းကို ေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/557.mp3"><span style="color: #ffcc00;">ဥပနိႆယပစၥည္းကို ေလ႔လာသံုးသပ္ျခင္း (အပိုင္း-၅)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;က&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/029.mp3"><span style="color: #ffcc00;">ကံကိုဖယ္႐ွား နိဗၺာန္သြား တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/401-ndml(17.8.16).mp3"><span style="color: #ffcc00;">ကံတရားတို႔၏ သာေကတမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/411-ndml(8.9.16).mp3"><span style="color: #ffcc00;">ကံတရားနွင့္ သံသရာဘဝမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/020.mp3"><span style="color: #ffcc00;">ကံထပ္အလွဴေတာ္မဂၤလာ အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/398-ndml(10.8.16).mp3"><span style="color: #ffcc00;">ကံေကာင္းျခင္းနွင့္ ကံမေကာင္းျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0854-ndml(22.6.16).mp3"><span style="color: #ffcc00;">ကြယ္လြန္ျခင္း(၁)လျပည့္ အနုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/333-ndml(15.1.16).mp3"><span style="color: #ffcc00;">ကိုယ့္တိုင္းျပည္ ကိုယ့္လူမ်ိဳးနွင့္ ကိုယ့္သာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/414-ndml(12.9.16).mp3"><span style="color: #ffcc00;">ကီဋာဂီရိသုတ္ အနွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/385-ndml(26.7.16).mp3"><span style="color: #ffcc00;">ကုသိုလ္ျဖစ္ပြား ျမတ္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/387-ndml(31.7.16).mp3"><span style="color: #ffcc00;">ကုသိုလ္သည္သာ ဘဝရိကၡာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0857-ndml(1.2.16).mp3"><span style="color: #ffcc00;">ကႎတိသုတ္လာ ျမတ္ဗုဒၶ၏မိန္႔မွာခ်က္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/386-ndml(28.7.16).mp3"><span style="color: #ffcc00;">ေကာင္းစြာေျပာၾကား လူ႔စကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/040.mp3"><span style="color: #ffcc00;">ေကာသမၺီသုတ္လာ မေထရ္ျမတ္တုိ႔၏ ဓမၼသာကစၦာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/350-ndml(25.3.16).mp3"><span style="color: #ffcc00;">ေကာသလမင္း၏ ျမတ္ဗုဒၶအေပၚ ၾကည္ညိဳေလးစားမွု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/045.mp3"><span style="color: #ffcc00;">ေက်နပ္စရာ လူ႔ဘဝ အေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/380-ndml(14.7.16).mp3"><span style="color: #ffcc00;">ေၾကာက္ရြံ႕ျခင္းနွင့္ ရဲရင့္ျခင္း</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုႏွစ္ထိ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/107.mp3"><span style="color: #ffcc00;">ကဆုန္လျပည္႔ ဗ်ာဒိတ္ေတာ္ပြဲႏွင္႔အမွတ္တရပံုရိပ္မ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/108.mp3"><span style="color: #ffcc00;">ကဆုန္လျပည္႔ ဗ်ာဒိတ္ေတာ္ပြဲႏွင္႔အမွတ္တရပံုရိပ္မ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/029-DrNandamalabhivamsa-KaTeatKaLaEatBawaTaSateThaMinePoneYate.mp3"><span style="color: #ffcc00;">ကတိကလ၏ ဘဝတစိတ္သမိုင္းပံုရိပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/089-ndml.mp3"><span style="color: #ffcc00;">ကတၱာရုဇာတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/103-ndml.mp3"><span style="color: #ffcc00;">ကာလာမသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0158-NDML.mp3"><span style="color: #ffcc00;">ကံကိုဖယ္ရွားကံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/58.mp3"><span style="color: #ffcc00;">ကံထပ္ အလွဴေတာ္မဂၤလာအခမ္းအနား အႏုေမာဒနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/105.ndml%202.mp3"><span style="color: #ffcc00;">ကံရွိလို႕ဘံုဘဝရွိရသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/083.mp3"><span style="color: #ffcc00;">ကံႏွင္႔ ကိေလသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/146.mp3"><span style="color: #ffcc00;">ကံႏွင္႔ဘဝ အလုပ္ႏွင္႔လုပ္အားခ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0125-NDML.mp3"><span style="color: #ffcc00;">ကံၾကမၼာ၏ရုပ္ပံုလႊာမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/308-ndml.mp3"><span style="color: #ffcc00;">ကံၾကမၼာ၏လွည္႔စားမႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0017-NDML.mp3"><span style="color: #ffcc00;">ကကၠာရုဇာတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/049.mp3"><span style="color: #ffcc00;">ကစၥာနေဂါတၱသုတၱန</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/621.mp3"><span style="color: #ffcc00;">ကပ္ႀကီးသံုးပါး ေက်ာ္လႊားေရး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/622.mp3"><span style="color: #ffcc00;">ကပ္ႀကီးသံုးပါး ေက်ာ္လႊားေရး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/73.mp3"><span style="color: #ffcc00;">ကမဌာန္းဘာဝနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/209-ndml.mp3"><span style="color: #ffcc00;">ကမၻာဦးကလူသားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0157-NDML.mp3"><span style="color: #ffcc00;">ကမၻာဦးကလူသားမ်ားအေၾကာင္း (စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/289-ndml.mp3"><span style="color: #ffcc00;">ကမၼဌာန္းအလုပ္ႏွင္႔အိပ္ငိုက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/614.mp3"><span style="color: #ffcc00;">ကမၼဌာန္းေက်ာင္းႏွင္႔ေယာဂီအဂၤါညီလွ်င္ တရားထူးရႏိုင္သည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/077.ndml%202.mp3"><span style="color: #ffcc00;">ကမၼနိယာမ ႏွင့္ ေလာကသဘာဝ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/059.ndml%202.mp3"><span style="color: #ffcc00;">ကမၼဝဋ္မွ လြတ္ေျမာက္ေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/111.ndml%202.mp3"><span style="color: #ffcc00;">ကမၼဝိပါေကာအစိေႏ ၱေယ်ာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/011.ndml%202.mp3"><span style="color: #ffcc00;">ကမၼဝိဘဂၤသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/098.ndml%202.mp3"><span style="color: #ffcc00;">ကယ္တင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/332-ndml.mp3"><span style="color: #ffcc00;">ကြန္ဗ်ဴတာတကၠသိုလ္၀ါဆိုသကၤန္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/112.mp3"><span style="color: #ffcc00;">ကာမနိယာမသေဘာတရားႏွင္႔ ကံကိုကုန္ေစတတ္ေသာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/012.ndml%202.mp3"><span style="color: #ffcc00;">ကာယဘာဝနာႏွင့္ စိတၱဘာဝနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/650.mp3"><span style="color: #ffcc00;">ကာလာမသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/058.mp3"><span style="color: #ffcc00;">ကာေမသုမိစၦာစာရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/222-ndml.mp3"><span style="color: #ffcc00;">ကိုးကြယ္မႈ၏အဓိပၸါယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/122.mp3"><span style="color: #ffcc00;">ကိုးကြယ္ျခင္း၏ အျမင္႔ဆံုးရည္မွန္းခ်က</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/187.mp3"><span style="color: #ffcc00;">ကိုးကြယ္ရာဘာသာတရားကိုေရြးခ်ယ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0039-NDML.mp3"><span style="color: #ffcc00;">ကိုးကြယ္ရာအမွန္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/074.ndml%202.mp3"><span style="color: #ffcc00;">ကိုယ့္ဘဝ ကိုယ္ျပင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0113-NDML.mp3"><span style="color: #ffcc00;">ကိုယ္႔က်င္႔တရားသည္သာလွ်င္လူအဆင္႔အတန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0022-NDML.mp3"><span style="color: #ffcc00;">ကိုယ္႔္ေနရာကိုယ္ေနၾက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/168-ndml.mp3"><span style="color: #ffcc00;">ကိုယ္က်င္႔တရားသည္သာလူ႔အဆင္႔အတန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0126-NDML.mp3"><span style="color: #ffcc00;">ကိုယ္ခံစြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/316-ndml.mp3"><span style="color: #ffcc00;">ကိုယ္စိတ္ပံုသြင္ၿမဲဆင္ျခင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/047.mp3"><span style="color: #ffcc00;">ကိုယ္လုပ္တာ ကိုယ္ရမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/564.mp3"><span style="color: #ffcc00;">ကိုယ္ေရြးတဲ႔လမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/148.ndml%202.mp3"><span style="color: #ffcc00;">ကုသိုလ္ဆိုတာခ်မ္းသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/042.ndml%202.mp3"><span style="color: #ffcc00;">ကုသိုလ္တစ္ပဲ ငရဲတစ္ပိႆာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/643.mp3"><span style="color: #ffcc00;">ကုသိုလ္ပင္မ်ိဳး စိုက္ပ်ိဳးၾကျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/322-ndml.mp3"><span style="color: #ffcc00;">ကုသိုလ္ေကာင္းမႈအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/857.mp3"><span style="color: #ffcc00;">ကုသုိလ္မဂၤလာၾသ၀ါဒ (ဦးေရ၀တ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/26.6.2015.mp3"><span style="color: #ffcc00;">ကုသုိလ္ျမစ္ႀကီးေတြစီးေနပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/758.mp3"><span style="color: #ffcc00;">ကုိးပါးသီလျဖင့္ ဥပုသ္ေစာင့္သုံးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/826.mp3"><span style="color: #ffcc00;">ကုိယ္ခ်င္းစာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/649.mp3"><span style="color: #ffcc00;">ကဲ႔ရဲ႕ေသာစကားလံဳးမ်ားျဖင္႔ ခ်ီးမြမ္းအပ္ေသာ ျမတ္ဗုဒၶ၏ဂုဏ္ရည္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/183.mp3"><span style="color: #ffcc00;">က်က္သေရရွိေသာ လူ႔ဘဝ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/160.ndml%202.mp3"><span style="color: #ffcc00;">က်င့္ပံု႕ထူးျခား ဉာဏ္စြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/006.ndml%202.mp3"><span style="color: #ffcc00;">ေကာင္းက်ိဳးျပည့္၀ ျမတ္သီလ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/161.mp3"><span style="color: #ffcc00;">ေကာင္းက်ိဳးဟူသမွ်ႏွင္႔ အပၸမာဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0129-NDML.mp3"><span style="color: #ffcc00;">ေကာင္းတာကိုသာေရြးခ်ယ္ၾကပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/169.mp3"><span style="color: #ffcc00;">ေကာင္းမႈစြမ္းအားႏွင္႔ လူ႔အရည္အခ်င္းမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0106-NDML.mp3"><span style="color: #ffcc00;">ေက်းဇူးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/084.mp3"><span style="color: #ffcc00;">ေက်းဇူးတရားအႀကီးမားဆံုးေသာ ပုဂၢိဳလ္သံုးဦး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/190.mp3"><span style="color: #ffcc00;">ေက်းဇူးရွင္တို႔အားေက်းဇူးဆပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/619.mp3"><span style="color: #ffcc00;">ေက်းဇူးသိျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/005.mp3"><span style="color: #ffcc00;">ေက်းလက္ေဒသ ျမန္မာအေမြအႏွစ္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/905.mp3"><span style="color: #ffcc00;">ေက်နပ္စရာအေတြး ေရာဂါေပ်ာက္ေဆး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/787.mp3"><span style="color: #ffcc00;">ေက်ာင္းဖြင့္ပြဲၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/111-ndml.mp3"><span style="color: #ffcc00;">ကိုးကြယ္ရာအမွန္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/094-ndml.mp3"><span style="color: #ffcc00;">ကိုယ္႔ေနရာကိုယ္ေနၾက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/822.mp3"><span style="color: #ffcc00;">ၾကီးသူငယ္သူ သတ္မွတ္ခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/013.mp3"><span style="color: #ffcc00;">ႀကိဳတင္ေကာင္းမႈ ႀကိဳးစားျပဳ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ခ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/031.mp3"><span style="color: #ffcc00;">ခ်မ္းသာအတုကိုစြန္႔ႏိုင္မွ ခ်မ္းသာအစစ္ကိုရမည္တရားေတာ္</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုႏွစ္ထိ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/685.mp3"><span style="color: #ffcc00;">ခဏိကသမာဓိကို ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/931.mp3"><span style="color: #ffcc00;">ခိုင္မာစိတ္ထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/120.ndml%202.mp3"><span style="color: #ffcc00;">ခိုင္မာေသာ ကိုယ္က်င့္တရားႏွင့္ၾကံ႕ခိုင္သည့္စိတ္ထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/271-ndml.mp3"><span style="color: #ffcc00;">ခုခံစြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/188.mp3"><span style="color: #ffcc00;">ခ်စ္ၾကည္ေရးႏွင္႔ စည္းလံုးညီညြတ္ေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/298-ndml.mp3"><span style="color: #ffcc00;">ခ်မ္းသာစြာအိပ္စက္ရျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/131.mp3"><span style="color: #ffcc00;">ခ်မ္းသာသုခမ်ားႏွင္႔ ဓမၼဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/750.mp3"><span style="color: #ffcc00;">ခ်မ္းသာႏွစ္ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/598.mp3"><span style="color: #ffcc00;">ခ်ဳပ္ေႏွာင္ထားေသာ စိတ္ရွိသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/599.mp3"><span style="color: #ffcc00;">ခႏၶာကို ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/037.ndml%202.mp3"><span style="color: #ffcc00;">ခႏၡာႏွင့္ ဥပါဒါနကၡႏၶာ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဂ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/134.mp3"><span style="color: #ffcc00;">ဂါရဝႏွင္႔ အဂါရဝ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/133.ndml%202.mp3"><span style="color: #ffcc00;">ဂီရိမာနႏၵသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဃ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0038-NDML.mp3"><span style="color: #ffcc00;">ဃ႑ိကာရ၏ဘ၀တစ္စိတ္သမိုင္းပံုရိပ္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0024-NDML.mp3"><span style="color: #ffcc00;">ဃဋိကာရသုတၱန</span></a></p>
<h5><span style="color: #00ffff;">&#8220;င&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/079.ndml%202.mp3"><span style="color: #ffcc00;">ငါမရွိလွ်င္ ငါ့ဟာမရွိ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;စ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/399-ndml(11.8.16).mp3"><span style="color: #ffcc00;">စီးပြားရွာ အကိ်ဳးရွိရာသံုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/417-ndml(19.9.16).mp3"><span style="color: #ffcc00;">ေစတနာေကာင္းလွ်င္ ကံေကာင္းသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/049.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ ျမတ္မဂၤလာ</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုႏွစ္ထိ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/751.mp3"><span style="color: #ffcc00;">စံထားရမည္႔ ယဥ္ေက်းမႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/256-ndml.mp3"><span style="color: #ffcc00;">စံထားရမည္႔ကိုယ္႔က်င္႔တရားရွိသူမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/219-ndml.mp3"><span style="color: #ffcc00;">စံနမူနာယူရမည္႔သူ႔လိုလူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/112.ndml%202.mp3"><span style="color: #ffcc00;">စံုဆင္းယူ ႏွင့္ဆန္တက္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/255-ndml.mp3"><span style="color: #ffcc00;">စင္ၾကယ္မႈျဖင္႔စိတ္ဖိစီးမႈကိုေလွ်ာ႔ခ်ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/834.mp3"><span style="color: #ffcc00;">စင္ၾကယ္ေအာင္အားထုတ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/331-ndml.mp3"><span style="color: #ffcc00;">စစ္ကိုင္းၿမိဳ႕မဟာသုေဗာဓာရံု(၅၂)ႏွစ္ျပည္႔ ေက်ာင္းတိုက္ေန႔ၾသ၀ါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/328-ndml.mp3"><span style="color: #ffcc00;">စစ္ကိုင္းၿမိဳ႕မဟာသုေဗာဓာရံုေက်ာင္းေဆာင္သစ္ ေရစက္ခ်အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/184.mp3"><span style="color: #ffcc00;">စရိုက္ဆုိးမ်ားကို ျမတ္ဗုဒၶ၏အဆံုးအမျဖင္႔ဖယ္ရွားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/130.ndml%202.mp3"><span style="color: #ffcc00;">စရိုက္ႏွင့္ဝါသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/294-ndml.mp3"><span style="color: #ffcc00;">စြန္႔လႊတ္ျခင္းႏွင္႔ရယူျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0112-NDML.mp3"><span style="color: #ffcc00;">စြမ္းအားျပည္႔စိတ္ႏွင္႔စြမ္းအားမဲ႔စိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/559.mp3"><span style="color: #ffcc00;">စြမ္းအားရွိေသာစိတ္ႏွင္႔ စြမ္းအားျပည္႔ေသာစိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/133.mp3"><span style="color: #ffcc00;">စြမ္းအားႀကီးမားျမတ္ဗုဒၶ၏ မ်က္လံုးမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/134.mp3"><span style="color: #ffcc00;">စြမ္းအားႀကီးမားျမတ္ဗုဒၶ၏ မ်က္လံုးမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/632.mp3"><span style="color: #ffcc00;">စြမ္းအားႀကီးမားလူ႔ခြန္အား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/193.mp3"><span style="color: #ffcc00;">စြမ္းအားႀကီးမားသာသနာမ်က္လံုးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/355.mp3"><span style="color: #ffcc00;">စြယ္ေတာ္ျမတ္ႏွင္႔သစၥာတရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/001.ndml%202.mp3"><span style="color: #ffcc00;">စြယ္ေတာ္ေလးဆူ ဘုရားရွိခုိး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/593.mp3"><span style="color: #ffcc00;">စြဲလန္းစိတ္ႏွင္႔ ပူပန္စိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/648.mp3"><span style="color: #ffcc00;">စဥ္းစားဥာဏ္ႏွင္႔ အက်င္႔မွန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/809.mp3"><span style="color: #ffcc00;">စာနာစိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/689.mp3"><span style="color: #ffcc00;">စိတၱဘာဝနာျဖင္႔သာ စိတ္ျဖဴစင္ႏိုင္သည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0046-NDML.mp3"><span style="color: #ffcc00;">စိတၱာႏုပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/889.mp3"><span style="color: #ffcc00;">စိတ္၏က်က္စားရာ အာရံုမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/242-ndml.mp3"><span style="color: #ffcc00;">စိတ္၏ထြက္ေပါက္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0162-NDML.mp3"><span style="color: #ffcc00;">စိတ္၏ျဖစ္စဥ္ကိုေလ႔လာျခင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0163-NDML.mp3"><span style="color: #ffcc00;">စိတ္၏ျဖစ္စဥ္ကိုေလ႔လာျခင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0093-NDML.mp3"><span style="color: #ffcc00;">စိတ္၏အညစ္အေၾကးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/097.ndml%202.mp3"><span style="color: #ffcc00;">စိတ္၏အညစ္အေၾကးမ်ားကိုဖယ္ရွားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0161-NDML.mp3"><span style="color: #ffcc00;">စိတ္၏အာရံုမ်ားႏွင္႔ေဆာင္ရြက္မႈကိစၥမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/214-ndml.mp3"><span style="color: #ffcc00;">စိတ္၏အေတြးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/162.ndml%202.mp3"><span style="color: #ffcc00;">စိတ္၏အေႏွာင္အဖြဲ႕မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/179.mp3"><span style="color: #ffcc00;">စိတ္ကိုသတိျဖင္႔ ေစာင္႔ၾကည္႔ရမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0092-NDML.mp3"><span style="color: #ffcc00;">စိတ္ကိုအမွီျပဳအင္အားစုမ်ာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0164-NDML.mp3"><span style="color: #ffcc00;">စိတ္ကိုအာရံုႏွင္႔ေလ႔လာျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/164.ndml%202.mp3"><span style="color: #ffcc00;">စိတ္ကိုေစာင့္ထိန္းျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/717.mp3"><span style="color: #ffcc00;">စိတ္ကိုေစာင္႔ၾကည္႔ၿမဲသတိထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0091-NDML.mp3"><span style="color: #ffcc00;">စိတ္ကိုေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/040.mp3"><span style="color: #ffcc00;">စိတ္ကူးယဥ္ျခင္းႏွင္႔ အေျမာ္အျမ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/143.ndml%202.mp3"><span style="color: #ffcc00;">စိတ္ခ်မ္းသာမွ ကိုယ္က်န္းမာမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/173.mp3"><span style="color: #ffcc00;">စိတ္စြမ္းအားမ်ားႏွင္႔ စြမ္းေဆာင္ရာဌာနမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/021.mp3"><span style="color: #ffcc00;">စိတ္ဆင္ရိုင္းႏွင္႔ ပညာခြ်န္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/22.11.2014/9%20%2827.11.2014%20pm%29.mp3"><span style="color: #ffcc00;">စိတ္ဆႏၵျဖင့္ ဘဝကိုပံုေဖာ္သူမ်ားအေၾကာင္း တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/284-ndml.mp3"><span style="color: #ffcc00;">စိတ္ထားျမင္႔ျမတ္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/715.mp3"><span style="color: #ffcc00;">စိတ္ထိန္းႏိုင္မွ ခ်မ္းသာရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0033-NDML.mp3"><span style="color: #ffcc00;">စိတ္ဓါတ္ခြန္အားျမွင္႔တင္ထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/135.mp3"><span style="color: #ffcc00;">စိတ္ဓါတ္ေပ်ာ႔ည႔ံသူႏွင္႔ စိတ္ဓါတ္ႀကံ႕ခိုင္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/748.mp3"><span style="color: #ffcc00;">စိတ္ပူပန္မႈကင္းေအာင္ က်င္႔ေဆာင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/200.mp3"><span style="color: #ffcc00;">စိတ္ၿငိမ္းခ်မ္းမႈ ရသူႏွင္႔မရသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/014.mp3"><span style="color: #ffcc00;">စိတ္ျဖစ္စဥ္ကို ကဌာန္းနည္း ျဖင္႔ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0094-NDML.mp3"><span style="color: #ffcc00;">စိတ္ျဖဴစင္မႈအင္အားစုမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0095-NDML.mp3"><span style="color: #ffcc00;">စိတ္ျဖဴစင္မႈအင္အားစုမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0028-NDML.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/045.mp3"><span style="color: #ffcc00;">စိတ္ေကာင္းရွိဖို႔က ပထမ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0152-NDML.mp3"><span style="color: #ffcc00;">စိတ္ေနစိတ္ထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.4.2.PM.mp3"><span style="color: #ffcc00;">စိတ္ၿငိမ္းခ်မ္းမႈ ရသူ ႏွင့္ မရသူ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/018-ndml.mp3"><span style="color: #ffcc00;">စိတ္၏ အာရုံႏွင့္ ေဆာင္ရြက္မွုကိစၥမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/012-ndml.mp3"><span style="color: #ffcc00;">စိတ္ကို အမွီျပဳအင္အားစုမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/021-ndml.mp3"><span style="color: #ffcc00;">စိတ္ကို အာရုံႏွင့္ ေလ့က်င့္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/011-ndml.mp3"><span style="color: #ffcc00;">စိတ္ကိုေလ့လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/105-ndml.mp3"><span style="color: #ffcc00;">စိတ္ဓါတ္ခြန္အားျမင္႕တင္ထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/013-ndml.mp3"><span style="color: #ffcc00;">စိတ္အညစ္အေၾကးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/100-ndml.mp3"><span style="color: #ffcc00;">စိတ္အေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/126.mp3"><span style="color: #ffcc00;">စိုးရိမ္စိတ္ကို ဖယ္ရွားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0119-NDML.mp3"><span style="color: #ffcc00;">စိေတၱန နိယေတေလာေကာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/175.mp3"><span style="color: #ffcc00;">စီးပြားဥစၥာရွာေဖြျခင္းႏွင္႔ အသုံးျပဳျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/234-ndml.mp3"><span style="color: #ffcc00;">စုေဆာင္းျခင္းႏွစ္ရပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/941.mp3"><span style="color: #ffcc00;">စၾကာဝေတးမင္းဘဝကိုေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.2.25.PM.mp3"><span style="color: #ffcc00;">စြမ္းအားႀကီးမား ျမတ္ဗုဒၶ၏ မ်က္လံုးမ်ား တရားေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.2.26.PM.mp3"><span style="color: #ffcc00;">စြမ္းအားႀကီးမား ျမတ္ဗုဒၶ၏ မ်က္လံုးမ်ား တရားေတာ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/118-ndml.mp3"><span style="color: #ffcc00;">စိတၱာႏုပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/085.mp3"><span style="color: #ffcc00;">ေစာင္႔စည္းမွေကာင္းမည္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဆ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/336-ndml(8.2.16).mp3"><span style="color: #ffcc00;">ဆရာျမတ္တို႔၏ ဆႏၵ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0827-ndml.mp3"><span style="color: #ffcc00;">ဆႏၵျပည့္ေၾကာင္းတရားငါးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/038.mp3"><span style="color: #ffcc00;">ဆက္ဆံေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0081-NDML.mp3"><span style="color: #ffcc00;">ဆင္းရဲတြင္းမွလြတ္ကင္းျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/618.mp3"><span style="color: #ffcc00;">ဆင္းရဲမြဲေတမႈ ေလ်ာ႔ခ်ေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/009.ndml%202.mp3"><span style="color: #ffcc00;">ဆဆကၠေဒသနာ ႏွင့္ ဓမၼဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0047-NDML.mp3"><span style="color: #ffcc00;">ဆပ္ကပ္ပြဲမွရေသာတရားတစ္ပုဒ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/002.ndml%202.mp3"><span style="color: #ffcc00;">ဆရာ ႏွင့္ တပည့္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/756.mp3"><span style="color: #ffcc00;">ဆရာရွိမွအမွန္သိႏိုင္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/353.mp3"><span style="color: #ffcc00;">ဆြမ္းလွဴဒါန္းမႈအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/728.mp3"><span style="color: #ffcc00;">ဆြမ္းအလွဴအႏုေမာဒနာ (ကိုရဲမင္းထြန္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/024.ndml%202.mp3"><span style="color: #ffcc00;">ဆြမ္းအႏုေမာဒနာ (ျဖဳးမိသာစု)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/832.mp3"><span style="color: #ffcc00;">ဆြမ္းအႏုေမာဒနာ (ဦးေတဇေစာဦး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/108.ndml%202.mp3"><span style="color: #ffcc00;">ဆုတ္ယုတ္ျခင္းႏွင့္ၾကီးပြားတိုးတက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/114.ndml%202.mp3"><span style="color: #ffcc00;">ဆုပ္ကိုင္ျခင္းႏွင့္စြန္႕လြတ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0149-NDML.mp3"><span style="color: #ffcc00;">ဆုျမတ္(၆)ျဖာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/230-ndml.mp3"><span style="color: #ffcc00;">ဆုေတာင္းျပည္႔၀ျမတ္ဓမၼ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/301-ndml.mp3"><span style="color: #ffcc00;">ဆေႏၷာ၀ါဒသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0055-NDML.mp3"><span style="color: #ffcc00;">ဆႏၵာဓိပတိ (၆-၉-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/119-ndml.mp3"><span style="color: #ffcc00;">ဆပ္ကပြဲမွရေသာတရားတစ္ပုဒ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/007-DrNandamalabhivamsa-SanDaDeetPaTeat.mp3"><span style="color: #ffcc00;">ဆႏၵအဓိပတိ တရားေတာ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဇ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0841-ndml(23.4.16).mp3"><span style="color: #ffcc00;">ဇာတကမွ ျပည္သူ႔နီတိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/367-ndml(1.5.16).mp3"><span style="color: #ffcc00;">ဇာတကလာ သုရာပါန သမိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/133.mp3"><span style="color: #ffcc00;">ဇာတကမွ အဏၰဝါဗဟုသုတ (၂၈.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/003.mp3"><span style="color: #ffcc00;">ဇာတိေျမမွ သာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/013-DrNandamalabhivamsa-ZatPaweMhaYaThawTaYarTaPoak.mp3"><span style="color: #ffcc00;">ဇာတ္ပြဲမွရေသာ တရားတစ္ပုဒ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ည&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/035.mp3"><span style="color: #ffcc00;">ဉာတပရိညာ ဝိပႆနာအေၾကာင္းတရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/072.mp3"><span style="color: #ffcc00;">ဉာဏဒႆန၏ အေၾကာင္းတရားကိုရွာေဖြျခင္း (၂၉.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/121.ndml%202.mp3"><span style="color: #ffcc00;">ဉာတပရိညာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/281-ndml.mp3"><span style="color: #ffcc00;">ညီညြတ္မႈသည္အင္အား</span></a></p>
<h5><span style="color: #00ffff;">&#8220;တ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/405-ndml(22.8.16).mp3"><span style="color: #ffcc00;">တရားနာပရိတ္သတ္တြင္ အေတာ္ဆံုးလူ (၂၂.၈.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/047.mp3"><span style="color: #ffcc00;">တရားႏွင့္ေ၀းလွ်င္ ဘုရားႏွင့္ေ၀းမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/036.mp3"><span style="color: #ffcc00;">တီရဏပရိညာ ဝိပႆနာအေၾကာင္းတရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/684.mp3"><span style="color: #ffcc00;">တစ္ရာတန္းလူသား၏ ဆယ္စုႏွစ္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/43.mp3"><span style="color: #ffcc00;">တစ္ေန႔တာအဟာရအလွဴ အလွဴေတာ္ မဂၤလာေရစက္ခ်အႏုေမာဒနာ (၁၈.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/919.mp3"><span style="color: #ffcc00;">တဏွာသည္ ဘဝသစ္ကိုျဖစ္ေစႏိုင္သည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/022.mp3"><span style="color: #ffcc00;">တန္ခိုးရွင္ျဖစ္ရံုႏွင္႔ အသိဥာဏ္မရွိႏိုင္ပံု (၄.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/745.mp3"><span style="color: #ffcc00;">တပည္႔မ်ား ေလးစာျမတ္ႏိုးတဲ႔ဆရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/283-ndml.mp3"><span style="color: #ffcc00;">တမလြန္ဘ၀ကေဆြမ်ိဳးမ်ားအေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/048.mp3"><span style="color: #ffcc00;">တမလြန္ဘဝအတြက္ ႀကိဳတင္ျပင္ဆင္မႈမ်ား (၁၉.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/566.mp3"><span style="color: #ffcc00;">တမလြန္ဘဝႏွင္႔ ကံအေၾကာင္းေဆြးေႏြးျခင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/567.mp3"><span style="color: #ffcc00;">တမလြန္ဘဝႏွင္႔ ကံအေၾကာင္းေဆြးေႏြးျခင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/35.mp3"><span style="color: #ffcc00;">တရား(၆)မ်ဳိး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/701.mp3"><span style="color: #ffcc00;">တရားကိုျမတ္ႏိုးသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/291-ndml.mp3"><span style="color: #ffcc00;">တရားကိုသိလွ်က္အက်င္႔ခက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/248-ndml.mp3"><span style="color: #ffcc00;">တရားက်င္႔သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/829.mp3"><span style="color: #ffcc00;">တရားဆုိသည္မွာ ပညာျဖင့္သာသိႏုိင္သည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/241-ndml.mp3"><span style="color: #ffcc00;">တရားထူးရႏိုင္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/161.ndml%202.mp3"><span style="color: #ffcc00;">တရားနာျငား ဉာဏ္စြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/061.mp3"><span style="color: #ffcc00;">တရားပြဲမွရရွိေသာ အက်ိဳးအျမတ္ (၁၈.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/022.ndml%202.mp3"><span style="color: #ffcc00;">တရားမ်က္စိကိုပိုင္ဆိုင္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0045-NDML.mp3"><span style="color: #ffcc00;">တရားျမင္မွဘုရားျမင္မည္ (၁၀-၂-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/865.mp3"><span style="color: #ffcc00;">တရားရွာ ကုိယ္မွာေတြ႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/765.mp3"><span style="color: #ffcc00;">တရားသိလွ်င္ စိတ္ေပ်ာ္ရႊင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/927.mp3"><span style="color: #ffcc00;">တရားသူႀကီး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/764.mp3"><span style="color: #ffcc00;">တရားအသိမကြာ စီးပြားရွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/700.mp3"><span style="color: #ffcc00;">တိတ္ဆိတ္ၿငိမ္သက္မႈကိုျမတ္ႏိုးသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/330-ndml.mp3"><span style="color: #ffcc00;">တိပိဋိကပူေဇာ္ပြဲၾသ၀ါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/610.mp3"><span style="color: #ffcc00;">တိုးတက္ျခင္းႏွင္႔ ဆုတ္ယုတ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0132-NDML.mp3"><span style="color: #ffcc00;">တို႔မွာေခါင္းေဆာင္ရွိတယ္ (၂၂-၁-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/348.mp3"><span style="color: #ffcc00;">တိုင္းမႈးဆြမ္းဆပ္ကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/900.mp3"><span style="color: #ffcc00;">တိုင္ပင္ေဆြး ႀကီးပြားေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/197.mp3"><span style="color: #ffcc00;">တေပါင္းလရာသီႏွင္႔ ရွင္ကာဠဳဒါယီ (၃.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/198.mp3"><span style="color: #ffcc00;">တေပါင္းလရာသီႏွင္႔ သဲပံုေစတီပြဲေတာ္ (၅.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/117-ndml.mp3"><span style="color: #ffcc00;">တရားျမင္မွဘုရားျမင္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/370.mp3"><span style="color: #ffcc00;">ေတာင္စြန္းသီလရွင္ေက်ာင္းၾသဝါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0110-NDML.mp3"><span style="color: #ffcc00;">ေတာင္ပို႔ထဲကရတနာ (၇-၁၂-၂၀၀၈)</span></a></p>
<h5><span style="color: #00ffff;">&#8220;ထ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/416-ndml(18.9.16).mp3"><span style="color: #ffcc00;">ထာဝရလႊင့္ထူရမည့္ သာသနာေအာင္လံေတာ္ (၁၈.၉.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0835.mp3"><span style="color: #ffcc00;">ေထရဝါဒဓမၼရတနာ (ၾသဝါဒ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0070-NDML.mp3"><span style="color: #ffcc00;">ထာ၀ရေတြးထားရမယ္႔ဘ၀အေရးမ်ား (၁၀-၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/159.mp3"><span style="color: #ffcc00;">ထူးခြ်န္သူ (၁၁.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/779.mp3"><span style="color: #ffcc00;">ထူးဆန္းေသာ သတၱ၀ါၾကီးမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/780.mp3"><span style="color: #ffcc00;">ထူးဆန္းေသာ သတၱ၀ါၾကီးမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/293-ndml.mp3"><span style="color: #ffcc00;">ထူပႏွင္႔ေစတိယ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဒ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/364-ndml(19.4.16).mp3"><span style="color: #ffcc00;">ဒုကၡလြတ္ကင္းေအာင္စြမ္းေဆာင္နိုင္သည့္ အရည္အခ်င္းမ်ား (၁၉.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/342.mp3"><span style="color: #ffcc00;">ဒကၡိဏဝိဘဂၤသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0030-NDML.mp3"><span style="color: #ffcc00;">ဒကာရင္းကိုကယ္တင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/837.mp3"><span style="color: #ffcc00;">ဒြယ၀ိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/940.mp3"><span style="color: #ffcc00;">ဒါနတရားႏွင္႔ ျမတ္ဗုဒၶ၏သေဘာထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/077.mp3"><span style="color: #ffcc00;">ဒါနအရာ ျမတ္ဗုဒၶ၏မိန္႔မွာခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/199.mp3"><span style="color: #ffcc00;">ဒါနအေျခခံျမတ္နိဗၺာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/74.mp3"><span style="color: #ffcc00;">ဒါနာ၊ သီလ၊ ဘာဝနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/901.mp3"><span style="color: #ffcc00;">ဒါနေကာင္းမႈေတာင္းဆုရွစ္ျဖာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/221-ndml.mp3"><span style="color: #ffcc00;">ဒိဌိသမၼႏၷပုဂၢိဳလ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/190-ndml.mp3"><span style="color: #ffcc00;">ဒို႔မွာေခါင္းေဆာင္ရွိတယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0077-NDML.mp3"><span style="color: #ffcc00;">ဒိေဌ ဒိဌ မိတၱံ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/203.mp3"><span style="color: #ffcc00;">ဒိေဌဒိဌမတၱံ ဝိပႆနာ (၁၅.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/204.mp3"><span style="color: #ffcc00;">ဒိေဌဒိဌမတၱံ ဝိပႆနာ (၁၆.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/708.mp3"><span style="color: #ffcc00;">ဒီဃနခသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/088.mp3"><span style="color: #ffcc00;">ဒီဘက္ကမ္းမွ ဟုိဘက္ကမ္းသို႔ (၂၄.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/297-ndml.mp3"><span style="color: #ffcc00;">ဒုကၡအဆံုးသတ္ေရးႀကိဳးပမ္းခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/136.ndml%202.mp3"><span style="color: #ffcc00;">ဒုလႅဘရဟန္းဘဝ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/270-ndml.mp3"><span style="color: #ffcc00;">ဒႆန၀ိသဒၶိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/102-ndml.mp3"><span style="color: #ffcc00;">ဒကာရင္းကိုကယ္တင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/279-ndml.mp3"><span style="color: #ffcc00;">ေဒ၀ဒဟသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဓ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0851-ndml(5.6.16).mp3"><span style="color: #ffcc00;">ဓမၼစာေပသင္ယူျခင္း၏ အကိ်ဳးေက်းဇူးမ်ား (၅.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/343-ndml(8.3.16).mp3"><span style="color: #ffcc00;">ဓမၼအသိျဖင့္ ေနထိုင္ျခင္း (၈.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/410-ndml(6.9.16).mp3"><span style="color: #ffcc00;">ဓမၼေခါင္းေဆာင္၏ ေလးစားထိုက္ေသာ အရည္အခ်င္းမ်ား (၆.၉.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/365-ndml(19.4.16).mp3"><span style="color: #ffcc00;">ဓမၼေသနာပတိမေထရ္ျမတ္၏သံဃာက်င့္သံုး ထံုးနည္းဥပေဒ (၁၉.၄.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Singapore/2.mp3"><span style="color: #ffcc00;">ဓမၼ အေမး/အေျဖ (၈.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0124-NDML.mp3"><span style="color: #ffcc00;">ဓမၼံ သရဏံ ကစၦာမိ (၁၃-၁-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/725.mp3"><span style="color: #ffcc00;">ဓမၼကိုအေဖာ္ျပဳမွ ထာဝရခ်မ္းသာမည္</span></a><br />
<a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/225-ndml.mp3"><span style="color: #ffcc00;">ဓမၼစာရီႏွင္႔အဓမၼစာရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/115.ndml%202.mp3"><span style="color: #ffcc00;">ဓမၼစာေပသင္ယူျခင္းႏွင့္ မွန္ကန္ေသာအျမင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/045.ndml%202.mp3"><span style="color: #ffcc00;">ဓမၼစၾကာည၏ အမွတ္တရေဒသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/180.mp3"><span style="color: #ffcc00;">ဓမၼတာဝန္ (၂၃.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/231-ndml.mp3"><span style="color: #ffcc00;">ဓမၼဒိႏၷေထရီမ၏ဓမၼအေျဖမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/682.mp3"><span style="color: #ffcc00;">ဓမၼဗ်ဴဟာသင္တန္း တရားအေမးအေျဖမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/683.mp3"><span style="color: #ffcc00;">ဓမၼဗ်ဴဟာသင္တန္း တရားအေမးအေျဖမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/223-ndml.mp3"><span style="color: #ffcc00;">ဓမၼမွတ္ေက်ာက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/252-ndml.mp3"><span style="color: #ffcc00;">ဓမၼလမ္းမွေလွ်ာက္လွမ္းပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/942.mp3"><span style="color: #ffcc00;">ဓမၼလမ္းေၾကာင္းေပၚတင္ေပးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/8.mp3"><span style="color: #ffcc00;">ဓမၼသင္တန္းဖြင့္ပြဲႏွင့္ ဆရာေတာ္ဘုရားႀကီး၏ (၇၄)ႏွစ္ျပည့္ ေမြးေန႔အလွဴေတာ္မဂၤလာ အခမ္းအနား အႏုေမာဒနာ ၾသဝါဒ တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/001.mp3"><span style="color: #ffcc00;">ဓမၼသည္သာ ဘဝ၏အလင္းေရာင္ (၃၀.၁၀.၂၀၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0026-NDML.mp3"><span style="color: #ffcc00;">ဓမၼသည္သာကိုးကြယ္ရာ (၂၈-၁၀-၂၀၀၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/069.ndml%202.mp3"><span style="color: #ffcc00;">ဓမၼသမာဒါန</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/126.ndml%202.mp3"><span style="color: #ffcc00;">ဓမၼသာကစ ၦာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0105-NDML.mp3"><span style="color: #ffcc00;">ဓမၼအသိျဖင္႔အက်ိဳးရွိရွိေနမည္ (၁၈-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/947.mp3"><span style="color: #ffcc00;">ဓမၼအေမးအေျဖ (စကၤာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/948.mp3"><span style="color: #ffcc00;">ဓမၼအေမးအေျဖ (စကၤာပူ) (Eng)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/677.mp3"><span style="color: #ffcc00;">ဓမၼေရးရာ ဖြံ႔ၿဖိဳးတိုးတက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/124.ndml%202.mp3"><span style="color: #ffcc00;">ဓမၼႏုဓမၼပဋိပဒါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0041-NDML.mp3"><span style="color: #ffcc00;">ဓမၼႏုပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0054-NDML.mp3"><span style="color: #ffcc00;">ဓါတု၀ိဘဂၤသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/601.mp3"><span style="color: #ffcc00;">ဓါတ္(၁၈)ပါးကို ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/098-ndml.mp3"><span style="color: #ffcc00;">ဓမၼသည္သာကိုးကြယ္ရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/113-ndml.mp3"><span style="color: #ffcc00;">ဓမၼႏုပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/006-DrNandamalabhivamsa-DarTuWeiBinGaThout.mp3"><span style="color: #ffcc00;">ဓာတုဝိဘဂၤဂသုတ္ အႏွစ္ခ်ဳပ္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/148-ndml.mp3"><span style="color: #ffcc00;">ဓမၼစၾကၤာအခါေတာ္ေန႔-(၂၅၉၇)ႀကိမ္ေျမာက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/125-ndml.mp3"><span style="color: #ffcc00;">ဓါတုဝိဘဂၤသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;န&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/408-ndml(28.8.16).mp3"><span style="color: #ffcc00;">နတ္ျဗဟၼာပရိတ္သတ္မ်ား အမ်ားဆံုးတက္ေရာက္သည့္ ရွင္သာရိပုတၱရာ၏ တရားပြဲ (၁) (၂၈.၈.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/409-ndml(29.8.16).mp3"><span style="color: #ffcc00;">နတ္ျဗဟၼာပရိတ္သတ္မ်ား အမ်ားဆံုးတက္ေရာက္သည့္ ရွင္သာရိပုတၱရာ၏ တရားပြဲ (၂) (၂၉.၈.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/346-ndml(18.3.16).mp3"><span style="color: #ffcc00;">နာယူမွတ္သား သူေတာ္ေကာင္းတရား (၁၈.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/341-ndml(8.3.16).mp3"><span style="color: #ffcc00;">နွစ္ဘဝ ေကာင္းက်ိဳးပြားတိုးေစရမည္ (၈.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/384-ndml(25.7.16).mp3"><span style="color: #ffcc00;">ေနာင္တပူပန္ျခင္း အေၾကာင္းအရင္း (၂၅.၇.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/406-ndml(26.8.16).mp3"><span style="color: #ffcc00;">ႏွလံုးလွသူ(၂၆.၈.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0131-NDML.mp3"><span style="color: #ffcc00;">န စ ေသာ န စ အ ေညာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/171.mp3"><span style="color: #ffcc00;">နဂေရာပမသုတ္ကို ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0029-NDML.mp3"><span style="color: #ffcc00;">နတ္ျပည္မွအမွာစကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/642.mp3"><span style="color: #ffcc00;">နတ္လူတို႔၏ဆရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/147.ndml%202.mp3"><span style="color: #ffcc00;">နတ္ေတြစံုစမ္းတဲ့ လူ႕ျပည္သတင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/592.mp3"><span style="color: #ffcc00;">နယဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/359.mp3"><span style="color: #ffcc00;">နဝရတ္ရတနာပဲခြဲစက္လွဴဒါန္းမႈအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0090-NDML.mp3"><span style="color: #ffcc00;">နာမ္တရားကိုသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/890.mp3"><span style="color: #ffcc00;">နိဗၺာန သပၸါယ ပဋိပဒါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0168-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္ကိုမ်က္ေမွာက္ျပဳျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0099-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္တံခါးဖြင္႔ႏိုင္မွအပါယ္တံခါးပိတ္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0021-NDML.mp3"><span style="color: #ffcc00;">နိဗၺာန္လမ္းေပၚမွအဆီးအတားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/607.mp3"><span style="color: #ffcc00;">နိဗၺာန္ဝင္ေရာက္ တံခါးေပါက္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/046.ndml%202.mp3"><span style="color: #ffcc00;">နိဗၺာန္သည္ အားလံုးအတြက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/309-ndml.mp3"><span style="color: #ffcc00;">နိဗၺာန္သို႔ဦးတည္သြားေနသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/025-ndml.mp3"><span style="color: #ffcc00;">နိဗၺန္ကို မ်က္ေမွာက္ျပဳျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/093-ndml.mp3"><span style="color: #ffcc00;">နိဗၺာန္လမ္းေပၚမွအဆီးအတားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/623.mp3"><span style="color: #ffcc00;">နိယတမိစၦာဒိဌိကို ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/048.ndml%202.mp3"><span style="color: #ffcc00;">နိယ်ာနိက သာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/269-ndml.mp3"><span style="color: #ffcc00;">နႏၵီဒုကၡႆမူလံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com//wp-content/uploads/mp3/DrNandamalabhivamsa/disc1/ndml.02/010-ndml.mp3"><span style="color: #ffcc00;">နာမ္တရားကုိ ေလ့လာသံုုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/299-ndml.mp3"><span style="color: #ffcc00;">ႏိုင္သူႏွင္႔ရႈံုးသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/051.mp3"><span style="color: #ffcc00;">ႏွစ္မ်ိဳးလံုးေကာင္းတဲ႔ မလုပ္တာနဲ႔လုပ္တာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/186.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္မဂၤလာကို ေမတၱာျဖင္႔ႀကိဳဆိုျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0006-NDML.mp3"><span style="color: #ffcc00;">ႏွစ္ဦးကာလဓမၼလက္ေဆာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/687.mp3"><span style="color: #ffcc00;">ႏွစ္ဦးေမတၱာ လူတိုင္းမွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/216-ndml.mp3"><span style="color: #ffcc00;">ႏွလံုးသား၏ၿငိမ္းေအးမႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/157.mp3"><span style="color: #ffcc00;">ႏွလံုးသားမွအဆိုးတရားမ်ားကို ဖယ္ရွားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/101-ndml.mp3"><span style="color: #ffcc00;">နတ္ျပည္မွအမွာစကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/755.mp3"><span style="color: #ffcc00;">ေန႔တိုင္းဆင္ျခင္ စိတ္ကိုျပင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0130-NDML.mp3"><span style="color: #ffcc00;">ေနတံ၊ မမ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/026.mp3"><span style="color: #ffcc00;">ေနာက္ဆံုးလူ မျဖစ္ေစနဲ႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/049.ndml%202.mp3"><span style="color: #ffcc00;">ေနာင္တရျခင္းႏွင့္ေနာင္တပူပန္ျခင္း</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ပ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0832-ndml(24.1.16).mp3"><span style="color: #ffcc00;">ပရဟိတသမားနွင့္ပါရမီတရား (၂၄.၁.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/050.mp3"><span style="color: #ffcc00;">ျပည့္စုံေသာႀကီးပြားတိုးတက္ျခင္းတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/037.mp3"><span style="color: #ffcc00;">ပဟာန ပရိညာ ဝိပႆနာအေၾကာင္းတရားေဒသနာေတာ္ </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/034.mp3"><span style="color: #ffcc00;">ပိုင္႐ွင္မဲ့ပစၥည္းမ်ားအေၾကာင္းတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/400-ndml(16.8.16).mp3"><span style="color: #ffcc00;">ပုညႏွင့္ သုခ (၁၆.၈.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/412-ndml(9.9.16).mp3"><span style="color: #ffcc00;">ပတ္ဝတ္က်င္ကိုရွုျမင္၍ မိမိတို့ဘဝကို ျပဳျပင္ျခင္း (၉.၉.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0825-ndml(30.9.15).mp3"><span style="color: #ffcc00;">ပညာရိွတို႔ တန္ဖိုးထားအပ္ေသာကုသိုလ္(၃)မိ်ဳး (၃၀.၉.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/215-ndml.mp3"><span style="color: #ffcc00;">ပင္လယ္ျဖတ္ကူးလူႏွစ္ဦး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/339-ndml.mp3"><span style="color: #ffcc00;">ပညာ၀ိမုတၱရဟႏၱာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/145-ndml.mp3"><span style="color: #ffcc00;">ပညာမဲ့ ဒါန (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/146-ndml.mp3"><span style="color: #ffcc00;">ပညာမဲ့ ဒါန (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0079-NDML.mp3"><span style="color: #ffcc00;">ပညာမဲ႔သဒၶါ-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0080-NDML.mp3"><span style="color: #ffcc00;">ပညာမဲ႔သဒၶါ-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/099.mp3"><span style="color: #ffcc00;">ပညာျဖင္႔အသက္ေမြးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/015.mp3"><span style="color: #ffcc00;">ပညာရွင္မ်ားသာ သိႏိုင္သည္႔တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/029.mp3"><span style="color: #ffcc00;">ပညာရွိ စကားဝိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/930.mp3"><span style="color: #ffcc00;">ပညာရွိမွ အမွန္သိမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/104.mp3"><span style="color: #ffcc00;">ပညာရွိမွသာ သိႏိုင္မည္႔တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/340.mp3"><span style="color: #ffcc00;">ပညာဝိမုတိၱ ရဟႏၱာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/678.mp3"><span style="color: #ffcc00;">ပဋိပဒါေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/151.ndml%202.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ္ႏွင့္ ဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/038.ndml%202.mp3"><span style="color: #ffcc00;">ပဋိသမၻိဒါ ဉာဏ္ကိုေလ့လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/363.mp3"><span style="color: #ffcc00;">ပန္းကန္႔ေကာ္အလွဴအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0027-NDML.mp3"><span style="color: #ffcc00;">ပမာဒႏွင္႔အပမာဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/055.mp3"><span style="color: #ffcc00;">ပရဟိတဒါနႏွင္႔ ျမတ္ပုည</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/053.mp3"><span style="color: #ffcc00;">ပရဟိတသမား စိတ္ခြန္အား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/019.mp3"><span style="color: #ffcc00;">ပရာဘဝသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/590.mp3"><span style="color: #ffcc00;">ပရိညာသံုးျဖာ ဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/664.mp3"><span style="color: #ffcc00;">ပရိသတ္ၾကားမွ ျမတ္ဘုရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/142.ndml%202.mp3"><span style="color: #ffcc00;">ပါခ်ဳပ္ဆရာေတာ္၏ (၅၂)ဝါေျမာက္ ဥပသမၸဒါအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/290-ndml.mp3"><span style="color: #ffcc00;">ပါရမီကုသိုလ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0111-NDML.mp3"><span style="color: #ffcc00;">ပါရမီပံုရိပ္အမွတ္တံဆိပ္ (၈-၁၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/354.mp3"><span style="color: #ffcc00;">ပါရမီမိသားစုဆြမ္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/228-ndml.mp3"><span style="color: #ffcc00;">ပါရမီရွင္တို႔၏ဘ၀(ကိသာေဂါတမီ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/227-ndml.mp3"><span style="color: #ffcc00;">ပါရမီရွင္တို႔၏ဘ၀(ကု႑လေကသာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/681.mp3"><span style="color: #ffcc00;">ပါရမီသမၻာရျမတ္သုည</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/068.mp3"><span style="color: #ffcc00;">ပိဋိကစာေပအရ တဖုႆႏွင္႔ဘလိႅကတို႔ဘဝအေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/168.mp3"><span style="color: #ffcc00;">ပိုင္ဆုိင္မႈႏွစ္မ်ိဳး တန္ဖုိးျဖတ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/068.ndml%202.mp3"><span style="color: #ffcc00;">ပုဂိၢဳလ္ေလးဆင့္ ၾကာေလးပြင့္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/257-ndml.mp3"><span style="color: #ffcc00;">ပုဂၢိဳလ္ထူးပုဂၢိဳလ္ျမတ္မ်ား၏အမွတ္တရမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/237-ndml.mp3"><span style="color: #ffcc00;">ပုဂၢိဳလ္ျမတ္တို႔၏ႏွလံုးအိမ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/226-ndml.mp3"><span style="color: #ffcc00;">ပုညသဟာယမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/107.mp3"><span style="color: #ffcc00;">ပုထုဇဥ္ဘဝႏွင္႔ အရိယာဘဝ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/071.mp3"><span style="color: #ffcc00;">ပုထုဇဥ္မ်ား၏ ဘဝပန္းခ်ီကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/153.mp3"><span style="color: #ffcc00;">ပ်က္စီးမႈကိုေရွာင္ ျပည္႔စံုေအာင္ႀကိဳးစား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/645.mp3"><span style="color: #ffcc00;">ပႆဒနိယတရား ျမတ္(၁၀)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/105.mp3"><span style="color: #ffcc00;">ျပင္ရခက္တဲ႔အမွား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/047.ndml%202.mp3"><span style="color: #ffcc00;">ျပစ္မွားျခင္း ႏွင့္ ဒဏ္သင့္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/099-ndml.mp3"><span style="color: #ffcc00;">ပမာဒႏွင့္ အပၸမာဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/177.mp3"><span style="color: #ffcc00;">ေပါင္းသင္းဆက္ဆံေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/608.mp3"><span style="color: #ffcc00;">ေျပာင္းလဲျခင္းႏွင္႔ လံုးဝေျပာင္းလဲျခင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/609.mp3"><span style="color: #ffcc00;">ေျပာင္းလဲျခင္းႏွင္႔ လံုးဝေျပာင္းလဲျခင္း (၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဖ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/676.mp3"><span style="color: #ffcc00;">ဖန္ဆင္းရွင္ဝါဒျဖစ္ေပၚလာပံု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/dr-nandamarlabiwinsa/thitsarparamisociety.com/wp-content/uploads/mp3/DrNandamalabhivamsa/Part-3&#038;4/710.mp3"><span style="color: #ffcc00;">ဖယ္ရွားျခင္း (၃)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/709.mp3"><span style="color: #ffcc00;">ဖြ႔ံၿဖိဳးတိုးတက္ျခင္းကိုေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/362.mp3"><span style="color: #ffcc00;">ဖားကန္႔အဖြဲ႔ဆြမ္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/245-ndml.mp3"><span style="color: #ffcc00;">ျဖစ္ႏိုင္တာႏွင္႔မျဖစ္ႏိုင္တာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/132.ndml%202.mp3"><span style="color: #ffcc00;">ျဖဴစင္စိတ္ထားအလုပ္ၾကိဳးစား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/372.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမသုတ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဗ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/044.mp3"><span style="color: #ffcc00;">ဗလငါးပါး စိတ္စြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/331-ndml(2.1.16).mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာ၀င္တို႔၏ ယံုၾကည္ခ်က္ႏွင့္ ခံယူခ်က္ (၂.၁.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/352-ndml(29.3.16).mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာဝင္တစ္ေယာက္၏ အေကာင္းဆံုးအရည္အခ်င္းမ်ား(၂၉.၃.၂၀၁၆) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/340-ndml(6.3.16).mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာဝင္မ်ား၏ ယံုၾကည္ခ်က္နွင့္ ကိုယ္က်င့္တရား (၆.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/096.mp3"><span style="color: #ffcc00;">ဗုဒၶ ဘာသာ နွင္ နိုင္ ငံ ျခား သား မ်ား အ ေျကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/766.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏ အဆုံးအမကုိ လက္ဆင့္ကမ္းျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/076.mp3"><span style="color: #ffcc00;">ဗုဒၶ၏အဆံုးအမျဖင္႔ ေနထိုင္ျခင္း (၅.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/035.ndml%202.mp3"><span style="color: #ffcc00;">ဗုဒၶၶစြမ္းအား ဉာဏ္ (၁၀) ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/828.mp3"><span style="color: #ffcc00;">ဗုဒၶတုိက္ေၾကြး တရားေဆး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/154.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာတို႔၏ လူေနမႈဘဝ (၄.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/050.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာပီသေသာ ေနထိုင္ျခင္း (၂၆.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/082.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာျဖစ္ရန္ အေျခခံတရား (၁၆.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/66.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာျဖစ္ရန္ အေျခခံတရားအေၾကာင္း တရားေဒသနာေတာ္ (၂၉.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/117.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာဝင္တစ္ဦး၏ ဓမၼအျမင္ (၃၀.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/147.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာဝင္တို႔၏ တာဝန္ဝတၱရားမ်ား (၂၈.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/156.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာဝင္အမ်ိဳးသမီးမ်ား၏ ဘဝေအာင္ျမင္ေရး (၆.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/55.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာႏွင့္ ႏိုင္ငံျခားသားမ်ားအေၾကာင္း တရားေဒသနာေတာ္ (၁၃.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/907.mp3"><span style="color: #ffcc00;">ဗုဒၶသည္ ဓမၼကိုအေလးျပဳသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/101.mp3"><span style="color: #ffcc00;">ဗုဒၶသမီးေတာ္မ်ား၏ ရင္တြင္းစကား (၂၇.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/675.mp3"><span style="color: #ffcc00;">ဗုဒၶသာဝကမ်ား၏ တာဝန္ႀကီး (၄)ရပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/367.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာ၏ဝိေသသလကၡဏာမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/128.mp3"><span style="color: #ffcc00;">ဗုဒၶသီဟနာဒသုတၱန္ အႏွစ္ခ်ဳပ္ (၃.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/098.mp3"><span style="color: #ffcc00;">ဗုဒၶဟုဝန္ခံျခင္း (၁၆.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/012.mp3"><span style="color: #ffcc00;">ဗုဒၶအလိုေတာ္က် လူ႔ဘဝေဖာ္ေဆာင္ေရး (၂၀.၉.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0023-NDML.mp3"><span style="color: #ffcc00;">ဗုဒၶအလုိက်ေနထိုင္နည္း (၂၃-၁၂-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/094.mp3"><span style="color: #ffcc00;">ဗုဒၶေခတ္သူေဌးႀကီးႏွင္႔ ၾကြယ္ဝခ်မ္းသာမႈ (၁၀.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/123.mp3"><span style="color: #ffcc00;">ဗုဒၶေဟာၾကား သစၥာတရား – ၁ (၂၀.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/124.mp3"><span style="color: #ffcc00;">ဗုဒၶေဟာၾကား သစၥာတရား – ၂ (၂၁.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/080.ndml%202.mp3"><span style="color: #ffcc00;">ဗုဒၶေဟာၾကားတရားသံုးဆယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/095-ndml.mp3"><span style="color: #ffcc00;">ဗုဒၶအလိုက်ေနထိုင္နည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Singapore/1.mp3"><span style="color: #ffcc00;">ဗုဒၶေဟာၾကား စိတ္ဖိစီးမႈကို ေလ်ာ့ခ်ျခင္း နည္းမ်ားအေၾကာင္း (၈.၁၀.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/236-ndml.mp3"><span style="color: #ffcc00;">ဗ်ာကတႏွင္႔အဗ်ာကတ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/776.mp3"><span style="color: #ffcc00;">ဗ်ာဒိတ္ေတာ္ၾကား ဘုရား (၂၄)ဆူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/928.mp3"><span style="color: #ffcc00;">ဗိမၼိသာရမင္း၏ ဘဝႏွင္႔သင္ခန္းစာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/640.mp3"><span style="color: #ffcc00;">ေဗာဓိသတၱဒ ဝိပႆနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.5.2.PM.mp3"><span style="color: #ffcc00;">ျဗမၼာ့နိမႏၲနိကသုတ္ အႏွစ္ခ်ဳပ္ တရားေတာ္- အပိုင္း ၁ (၀၂.၀၅.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.5.3.PM.mp3"><span style="color: #ffcc00;">ျဗမၼာ့နိမႏၲနိကသုတ္ အႏွစ္ခ်ဳပ္ တရားေတာ္- အပိုင္း ၂ (၀၃.၀၅.၂၀၁၅)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဘ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/415-ndml(16.9.16).mp3"><span style="color: #ffcc00;">ဘဝခရီးအတြက္ ၾကိဳတင္ျပင္ဆင္ျခင္း (၁၆.၉.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/381-ndml(15.7.16).mp3"><span style="color: #ffcc00;">ဘဝေမးခြန္းနွင့္ အေျဖမ်ား(၁၅.၇.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/372-ndml(21.5.16).mp3"><span style="color: #ffcc00;">ဘုရားပြင့္ျခင္းေၾကာင့္ ေကာင္းမ်ိဳး(၁၂)မ်ိဳး ေပၚထြင္းျခင္း (၂၁.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/165.mp3"><span style="color: #ffcc00;">ဘံုဆြမ္းေလာင္းလွဴ စိတ္ထားျဖဴ (၄.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/896.mp3"><span style="color: #ffcc00;">ဘံုဘဝမွာ ဆံုမိျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0083-NDML.mp3"><span style="color: #ffcc00;">ဘ၀၏၀န္ထုပ္၀န္ပိုးမ်ား (၂၅-၇-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0032-NDML.mp3"><span style="color: #ffcc00;">ဘ၀ကိုအလွဆင္မည္႔သူ (၂၇-၁၂-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/213-ndml.mp3"><span style="color: #ffcc00;">ဘ၀ကိုအလွဆင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0051-NDML.mp3"><span style="color: #ffcc00;">ဘ၀ခရီး၀ယ္ေရြးခ်ယ္ရမယ္႔လမ္း (၂၅-၇-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/307-ndml.mp3"><span style="color: #ffcc00;">ဘ၀ခရီးသည္အနည္းအမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/239-ndml.mp3"><span style="color: #ffcc00;">ဘ၀ဆည္းဆာႏွင္႔ကရုဏာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/313-ndml.mp3"><span style="color: #ffcc00;">ဘ၀တဏွာကိုေလ႔လာျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0085-NDML.mp3"><span style="color: #ffcc00;">ဘ၀သံသရာအေၾကာင္း (၁၂-၈-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0036-NDML.mp3"><span style="color: #ffcc00;">ဘ၀အသြင္ကိုဓမၼအျမင္ျဖင္႔ၾကည္႔ရႈုျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/193-ndml.mp3"><span style="color: #ffcc00;">ဘ၀အေရးစိတ္ေအားရေလေအာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/275-ndml.mp3"><span style="color: #ffcc00;">ဘ၀ႏွင္႔ဆက္စပ္၍ပဌာန္းျမတ္ေဒသနာကို ေလ႔လာသံုးသပ္ျခင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/276-ndml.mp3"><span style="color: #ffcc00;">ဘ၀ႏွင္႔ဆက္စပ္၍ပဌာန္းျမတ္ေဒသနာကို ေလ႔လာသံုးသပ္ျခင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0066-NDML.mp3"><span style="color: #ffcc00;">ဘ၀ႏွင္႔နိဗၺာန္ (၄-၁-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0098-NDML.mp3"><span style="color: #ffcc00;">ဘ၀ႏွင္႔ဘ၀နိေရာဓအေၾကာင္း (၄-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/42.mp3"><span style="color: #ffcc00;">ဘဒၵႏၱသုႏၵရ မဟာေထျမတ္ႀကီးအား ရည္စူး၍ ေက်းဇူးဆပ္ျခင္း အလွဴေတာ္မဂၤလာ အႏုေမာဒနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0156-NDML.mp3"><span style="color: #ffcc00;">ဘဒၵႏၱနႏၵမာလာဘိဝံသသက္ေတာ္ (၆၉)ႏွစ္ ျပည္႔ၾသဝါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/149-ndml.mp3"><span style="color: #ffcc00;">ဘဝ၏ ထုတ္ဝန္ပိုးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/118.mp3"><span style="color: #ffcc00;">ဘဝကိုရႈျမင္သံုးသပ္ျခင္း (၇.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0171-NDML.mp3"><span style="color: #ffcc00;">ဘဝကိုအလွဆင္ျခင္း (၂၁-၄-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/034.mp3"><span style="color: #ffcc00;">ဘဝကိုေရြးခ်ယ္ျခင္းႏွင္႔ ျမတ္ဗုဒၶ၏အဆံုးအမ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/561.mp3"><span style="color: #ffcc00;">ဘဝကူးေကာင္းေရး က်င္႔ေဆာင္ေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/127.ndml%202.mp3"><span style="color: #ffcc00;">ဘဝတဏွာႏွင့္သံသရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/563.mp3"><span style="color: #ffcc00;">ဘဝဒုကၡကိုရႈျမင္သံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/50.mp3"><span style="color: #ffcc00;">ဘဝနာ (၂)ပါး စိတ္ခြန္အား အေၾကာင္း တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0166-NDML.mp3"><span style="color: #ffcc00;">ဘဝနိဂံုးေသဆံုးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/558.mp3"><span style="color: #ffcc00;">ဘဝမွာအေကာင္းဆံုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/151-ndml.mp3"><span style="color: #ffcc00;">ဘဝသံသရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0167-NDML.mp3"><span style="color: #ffcc00;">ဘဝသစ္ ၌ျပန္လည္ေမြးဖြားျခင္း (၃၀-၃-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0135-NDML.mp3"><span style="color: #ffcc00;">ဘဝအေရးစိတ္ေအးရေလေအာင္ (၁၃-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/018.ndml%202.mp3"><span style="color: #ffcc00;">ဘဝေရးရာအေျဖရွာျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/153-ndml.mp3"><span style="color: #ffcc00;">ဘဝႏွင့္ ဘဝနိေရာဓ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/042.mp3"><span style="color: #ffcc00;">ဘာဝနာႏွစ္ပါး စိတ္ခြန္အား (၁၀.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/637.mp3"><span style="color: #ffcc00;">ဘာသာတရားကို လိုက္နာက်င္႔သံုးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/636.mp3"><span style="color: #ffcc00;">ဘာသာတရားကို ေရြးခ်ယ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/859.mp3"><span style="color: #ffcc00;">ဘာသာတရားဆုိတုိင္း လုိက္နာသင့္သလား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/631.mp3"><span style="color: #ffcc00;">ဘာသာတရားလိုက္နာက်င္႔သံုးျခင္း၏ ရည္ရြယ္ခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/067.ndml%202.mp3"><span style="color: #ffcc00;">ဘာသာတရားႏွင့္ ကိုးကြယ္မႈသရဏဂံု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Dr-Nandanarlar-22-10-11-singapore.mp3"><span style="color: #ffcc00;">ဘာသာတရားကို ေရြးခ်ယ္ျခင္းအေၾကာင္းတရားေဒသနာေတာ္ (စင္ကာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Dr-Nandanarlar-23-10-11-singapore.mp3"><span style="color: #ffcc00;">ဘာသာတရားကို လိုက္နာက်င့္သံုးျခင္းအေၾကာင္း တရားေဒသနာေတာ္ (စင္ကာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/025.ndml%202.mp3"><span style="color: #ffcc00;">ဘိကၡဳနီသာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/707.mp3"><span style="color: #ffcc00;">ဘိကၡဴနီငါးရာႏွင္႔ အရွင္နႏၵက၏ ဝိပႆနာအလုပ္ေပး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/150.ndml%202.mp3"><span style="color: #ffcc00;">ဘိုးဘြားမ်ားႏွင့္ အပစာယနာကုသိုလ္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/103.ndml%202.mp3"><span style="color: #ffcc00;">ဘုရားပြင့္မွ ၾကားရသည့္အေျဖ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/339.mp3"><span style="color: #ffcc00;">ဘုရားအေလာင္းတို႔၏ ဘဝအေပၚရႈျမင္သံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/338-ndml.mp3"><span style="color: #ffcc00;">ဘုရားအေလာင္းတို႔အေပၚတြင္ရႈျမင္သံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/371.mp3"><span style="color: #ffcc00;">ဘုရားေသာ္မွေပးဆပ္ရသည္႔ ကံၾကမၼာဝဋ္ေၾကြးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/008.mp3"><span style="color: #ffcc00;">ဘုရားႏွင္႔ေတြ႕ေအာင္ ႀကိဳးစားပါ (၁.၉.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/818.mp3"><span style="color: #ffcc00;">ဘုရားၾကည္ညဳိက အပါယ္မက်</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/007.mp3"><span style="color: #ffcc00;">ဘေဒၵကသုတ္ အႏွစ္ခ်ဳပ္ (၂၉.၇.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/45.mp3"><span style="color: #ffcc00;">ဘဝကို ရႈျမင္သံုးသပ္ျခင္းအေၾကာင္း တရားေဒသနာေတာ္ (၇.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/023-ndml.mp3"><span style="color: #ffcc00;">ဘ၀နိဂံုးေသဆံုးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/024-ndml.mp3"><span style="color: #ffcc00;">ဘ၀သစ္ ၌ ျပန္လည္ေမြးဖြားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/104ndml.mp3"><span style="color: #ffcc00;">ဘဝကိုအလွဆင္မည္႕သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/123-ndml.mp3"><span style="color: #ffcc00;">ဘဝခရီးဝယ္ေရြးခ်ယ္ရမည္႔လမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/108-ndml.mp3"><span style="color: #ffcc00;">ဘဝအသြင္ကိုိုဓမၼအျမင္ျဖင္႔ေလ႔လာျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/132-ndml.mp3"><span style="color: #ffcc00;">ဘဝႏွင္႔နိဗၺာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/102.ndml%202.mp3"><span style="color: #ffcc00;">ေဘးကင္းရာသို႕ထြက္ခြါျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/159.ndml%202.mp3"><span style="color: #ffcc00;">ေဘးေလးပါးႏွင့္ဆင္ျခင္မႈ႕စြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/143.mp3"><span style="color: #ffcc00;">ေဘးေလးမ်ိဳးကိုေရွာင္၍ စင္ၾကယ္ေအာင္ေနထိုင္ျခင္း (၂၄.၁၀၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/076.ndml%202.mp3"><span style="color: #ffcc00;">ေဘသဇၨဂုရု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0127-NDML.mp3"><span style="color: #ffcc00;">ေဘာဂတဏွာ (၁၇-၁၂-၂၀၀၉)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;မ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/054.mp3"><span style="color: #ffcc00;">မက်န္းမာသူမ်ားအတြက္ အထူးႏုလံုးသြင္းျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/353-ndml(29.3.16).mp3"><span style="color: #ffcc00;">မဂၤလာက်င့္စဥ္ျဖင့္ ဘဝကိုျမင့္တင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0834-ndml(15.2.16).mp3"><span style="color: #ffcc00;">မဂၤလာဦးဆြမ္းကပ္အလွဴ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0853-ndml(21.6.16).mp3"><span style="color: #ffcc00;">မိမိကိုယ္ကို ထိန္းေက်ာင္းပဲ့ျပင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/379-ndml(13.7.16).mp3"><span style="color: #ffcc00;">မိမိကိုယ္ကို ျမတ္နိုးပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/033.mp3"><span style="color: #ffcc00;">မိမိကုိယ္တိုင္ မိမိ၏ရန္သူမျဖစ္ပါေစႏွင့္အေၾကာင္း တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/357-ndml(10.4.16).mp3"><span style="color: #ffcc00;">မူးယစ္ကင္းကြာ မဂၤလာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/019.mp3"><span style="color: #ffcc00;">မူးယစ္ကင္းကြာမဂၤလာအေၾကာင္း တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/006.mp3"><span style="color: #ffcc00;">မေကာင္းမႈ မွ စိတ္ကို တားျမစ္ရမည္ အေၾကာင္း တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/373-ndml(22.5.16).mp3"><span style="color: #ffcc00;">မေကာင္းမႈ႕မွ စိတ္ကိုတားျမစ္ရမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0848-ndml(15.10.15).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ျငိမ္းခ်မ္းေရး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0849-ndml(16.10.15).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ျငိမ္းခ်မ္းေရး (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/413-ndml(11.9.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ သုနႏၵါ ဝိဟာရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/335-ndml(5.2.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးအမနွင့္ပညာရိွမ်ား၏ အၾကံျပဳစကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/383-ndml(24.7.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးအမျဖင့္ ရဟန္းဘဝရာသက္ပန္ ေပ်ာ္ေမြေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/338-ndml(28.2.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အာမခံစကားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/347-ndml(19.3.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမ ၾသဝါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/053.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶတို႔၏ အဆုံးအမ ပါတိေမာကၡဳေဒၵသကိုေလ့လာသုံးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/382-ndml(19.7.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶထံမွ သစၥာတရားကိုမထမဆံုးသိသူ (ဓမၼစၾကာေန့)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018/July/21.06.14.mp3"><span style="color: #ff9900;">ျမတ္ဗုဒၶဘဝ ႏွင္ ဝါဆိုလျပည့္ေန႔အမွတ္တရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/355-ndml(2.4.16).mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶေဟာၾကားသည့္ သင့္၊မသင့္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0831-ndml(22.1.16).mp3"><span style="color: #ffcc00;">ျမန္မာ့ေက်းလက္ေဒသ ယဥ္ေက်းမွုနွင့္သာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/042.mp3"><span style="color: #ffcc00;">ေမတၱာကို သမထအဆင့္သို႔တိုးျမွင့္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/041.mp3"><span style="color: #ffcc00;">ေမတၱာျဖင့္ ျငိမ္ခ်မ္းေရးကို ေဖာ္ေဆာင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0830-ndml(17.1.16).mp3"><span style="color: #ffcc00;">ေမတၱာသက္ဝင္ ခ်စ္ခင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/043.mp3"><span style="color: #ffcc00;">ေမတၱာအေျခခံ ၀ိပႆနာဉာဏ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/402-ndml(18.8.16).mp3"><span style="color: #ffcc00;">ေမတၱာႏွလံုးသား လူတိုင္းပြား (ေမတၱာအေခၚေတာ္ေန႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0842-ndml(1.5.16).mp3"><span style="color: #ffcc00;">ေမြးေန႔ အနုေမာဒနာ (၁.၅.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0833-ndml(15.2.16).mp3"><span style="color: #ffcc00;">ေမြးေန႔ အနုေမာဒနာ (၁၄.၂.၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0856-ndml(9.2.16).mp3"><span style="color: #ffcc00;">ေမြးေန႔ဂုဏပူဇာ အနုေမာဒနာ</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုႏွစ္ထိေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/129.ndml%202.mp3"><span style="color: #ffcc00;">မေကာင္းမႈမွေရွာင္ၾကဥ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/075.ndml%202.mp3"><span style="color: #ffcc00;">မေကာင္းမႈေရွာင္ ေကာင္းမႈေဆာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/140.mp3"><span style="color: #ffcc00;">မကယ္ႏိုင္တဲ႔ေဘး လြတ္ေျမာက္ေရး (၄.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0140-NDML.mp3"><span style="color: #ffcc00;">မတူတာေတြကိုအတူထားႏိုင္ျခင္း (၁၈-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/061.ndml%202.mp3"><span style="color: #ffcc00;">မထီမဲ့ျမင္ျပဳျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/918.mp3"><span style="color: #ffcc00;">မဓုပိ႑ိကသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/006.mp3"><span style="color: #ffcc00;">မေတြးသင္႔ေသာအေတြးမ်ား (၂၀.၇.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/633.mp3"><span style="color: #ffcc00;">မေတြေဝေသာအသိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/929.mp3"><span style="color: #ffcc00;">မေမ႔ေသာသတိ မေလွ်ာ႕ေသာဇြဲလံု႕လ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/939.mp3"><span style="color: #ffcc00;">မေၾကာက္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0058-NDML.mp3"><span style="color: #ffcc00;">မႏုႆဓမၼႏွင္႔ဥတၱရိမႏုႆဓမၼ (၁၉-၉-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/336.mp3"><span style="color: #ffcc00;">မဟာဒါန</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/16.mp3"><span style="color: #ffcc00;">မဟာဝိဇရသႏၱီ သိမ္ေက်ာင္းေတာ္ သိမ္ေရစက္ခ်က္ အႀကိဳတရားပြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/052.mp3"><span style="color: #ffcc00;">မဟာသာဝကႀကီးတို႔၏ စကားဝိုင္း (၁.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/22.11.2014/3%20%2823.11.2014%20am%29.mp3"><span style="color: #ffcc00;">မဂၤလာအခန္းအနား အႏုေမာဒနာ တရားေတာ္ (၂၃.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/163.ndml%202.mp3"><span style="color: #ffcc00;">မဂၤလာဦးဆြမ္းေကြ်းအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/749.mp3"><span style="color: #ffcc00;">မဂၤလာၾသဝါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/064.mp3"><span style="color: #ffcc00;">မစၦရိယအဖြင္႔ (၂၂.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/357.mp3"><span style="color: #ffcc00;">မတၱရာဆြမ္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/9.mp3"><span style="color: #ffcc00;">မန္းေလးၿမိဳ႕ ေစ်းခ်ဳိေတာ္ ေရႊဆိုင္တန္းမိသာစု ဆြမ္းအလွဴေတာ္ အႏုေမာဒနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/020.ndml%202.mp3"><span style="color: #ffcc00;">မရဏႆတိကထာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/280-ndml.mp3"><span style="color: #ffcc00;">မလႅိကာေဒ၀ီအေမးပုစၧာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/149.mp3"><span style="color: #ffcc00;">မသူေတာ္တရားကို အႏိုင္ယူျခင္း (၃၀.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/010.ndml%202.mp3"><span style="color: #ffcc00;">မဟာပညာေက်ာ္ပုဂၢိဳလ္တို႕၏ ထူးျခားေသာတရား (၂)ပုဒ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/893.mp3"><span style="color: #ffcc00;">မာဂ႑ီ မိသားစု၏ဘဝႏွင္႔သင္ခန္းစာ (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/894.mp3"><span style="color: #ffcc00;">မာဂ႑ီ မိသားစု၏ဘဝႏွင္႔သင္ခန္းစာ (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/895.mp3"><span style="color: #ffcc00;">မာဂ႑ီ မိသားစု၏ဘဝႏွင္႔သင္ခန္းစာ (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/066.mp3"><span style="color: #ffcc00;">မာနခက္ထန္သူကို ဆံုးမျခင္း (၂၄.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/250-ndml.mp3"><span style="color: #ffcc00;">မာနတရားကိုေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/082.ndml%202.mp3"><span style="color: #ffcc00;">မာန္ရစ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/319-ndml.mp3"><span style="color: #ffcc00;">မာလုက်ပုတၱရဟန္းအားအလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0121-NDML.mp3"><span style="color: #ffcc00;">ေမတၱာႏွလံုးအစဥ္သံုး (၁-၁-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/594.mp3"><span style="color: #ffcc00;">ေမ႔ေလ်ာ႔သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/009.mp3"><span style="color: #ffcc00;">ေမးခြန္းထုတ္၍ အေျဖရွာျခင္း (၂.၉.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/089.mp3"><span style="color: #ffcc00;">ေမးခြန္းထုတ္၍ အေျဖရွာျခင္း (၂၈.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/124.mp3"><span style="color: #ffcc00;">မိတၱပူဇာ ျမတ္ေဒသနာ (၁၈.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/232-ndml.mp3"><span style="color: #ffcc00;">မိတ္ေကာင္းေဆြေကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/056.mp3"><span style="color: #ffcc00;">မိဘရိပ္မွာ အၾကင္နာ (၈.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/072.ndml%202.mp3"><span style="color: #ffcc00;">မိဘေက်းဇူးတရားႏွင့္ ဗုဒၶ၏အဆံုးအမစကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/041.mp3"><span style="color: #ffcc00;">မိဘႏွင္႔သားသမီးအၾကား မွန္ကန္ေသာအျမင္မ်ား (၉.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/059.mp3"><span style="color: #ffcc00;">မိေကာင္းဖေကာင္း (၁၆.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0011-NDML.mp3"><span style="color: #ffcc00;">မူလပကၡဇာတ္ (၂၅-၄-၁၉၈၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/329-ndml.mp3"><span style="color: #ffcc00;">မံုရြာၿမိဳ႕ဘဒၵမၼေဇာတိကသုေဗာဓာရံုအတြင္း ေက်ာင္းေရစက္ခ်အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/365.mp3"><span style="color: #ffcc00;">မံုရြာေက်ာင္းဝါဆိုသကၤန္းကပ္ႏွင့္ ဓမၼာရံုအလွဴေတာ္ေငြလွဴဒါန္းမႈ အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/325-ndml.mp3"><span style="color: #ffcc00;">မံုရြာေက်ာင္းေရစက္ခ်အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0073-NDML.mp3"><span style="color: #ffcc00;">မွန္ကန္ေသာႀကိဳးစားအားထုတ္မႈ (၂၃-၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/358.mp3"><span style="color: #ffcc00;">ျမင္႔သူဇာေမြးေန႔အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/783.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏မွာၾကားခ်က္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/023.mp3"><span style="color: #ffcc00;">ျမတ္နိဗၺာန္တရားႏွင္႔ ပရိနိဗၺာန္စံဝင္မႈေလ႔လာသံုးသပ္ျခင္း (၇.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/087.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ စံျပတပည္႔မ်ား (၂၃.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/932.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ထိပ္တန္းတပည္႔ရွစ္ဦး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/638.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ မဇၥ်ိမပဋိပဒါတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/46.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးမအရ လူေတာ္လူေကာင္း အေရအျခင္းမ်ားအေၾကာင္း တရားေဒသနာေတာ္ (၇.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/59.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးအမျဖင့္ ခ်မ္းသာသုခကိုရွာျခင္း အေၾကာင္း ေဒသနာေတာ္ (၂၀.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/65.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးအမႏွင့္ ဗုဒၶဘာသာမိသားစုအေၾကာင္း ေဒသနာေတာ္ (၂၇.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/52.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အဆံုးအမႏွင့္ ေက်းလက္ေဒသ အေၾကာင္း တရားေဒသနာေတာ္ (၁၂.၂.၁၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/081.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ အေမြအႏွစ္မ်ား (၁၅.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/119.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ဘဝႏွင္႔ ဝါဆိုလျပည္႔ေန႔အမွတ္တရ (၁၁.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/782.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏မွာၾကားခ်က္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/010.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏သံေဝဂတရားႏွင္႔ အဆံုးအမစကား (၈.၉.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/639.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမ၏ အက်ိဳးသက္ေရာက္မႈမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/113.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမျဖင္႔ ခ်မ္းသာသုခကိုရွာျခင္း (၂၀.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/170.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမျဖင္႔ ဘဝေအာင္ျမင္မႈကိုရယူျခင္း (၈.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/039.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမအရ လူေတာ္လူေကာင္းအရည္အခ်င္းမ်ား (၇.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/115.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမႏွင္႔ ဗုဒၶဘာသာမိသားစုဘဝ (၂၇.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/688.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမႏွင္႔ ဘဝေနထိုင္နည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/657.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမႏွင္႔ လုိက္နာက်င္႔သံုးျခင္း (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/658.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမႏွင္႔ လုိက္နာက်င္႔သံုးျခင္း (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/757.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆံုးအမႏွင္႔အညီေနထိုင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/767.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏အဆုံးအမႏွင့္ညီညြတ္သည္႕ဇနီးေမာင္နံဘ၀</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/144.ndml%202.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ေက်းဇူးကို အထူးေပးဆပ္ခဲ့သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/016.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ၾကည္ညိဳဖြယ္ရာ ဂုဏ္ရည္မ်ား (၂.၁၀.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/194.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာႏွင္႔ သမဏေလးမ်ိဳး (၂၂.၂.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/020.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာႏွင္႔ သီတင္းကြ်တ္လျပည္႔ေန႔ အမွတ္တရမ်ား (၁၉.၁၀.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/078.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶအဆံုးအမႏွင္႔ ေက်းလက္ေဒသ (၁၂.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/074.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶအေပၚ ရွင္သာရိပုတၱရာ၏ၾကည္ညိဳမႈ (၃၀.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/155.ndml%202.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶေဒသနာ ႏွင့္စၾကာဝဠာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/177-ndml.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶေဒသနာႏွင္႔ယေန႔ကမၻာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/080.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶေဟာၾကားဆံုးမသည္႔ လူသားတို႔၏ကိုယ္က်င္႔တရား (၁၄.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/827.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶႏွင့္ ဗုဒၶသာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0057-NDML.mp3"><span style="color: #ffcc00;">ျမတ္ဥစၥာစုေဆာင္းပါ (၇-၉-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/011-DrNandamalabhivamsa-MyatBuddhaDayThaNarNhitYaNaeKhaBar.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ သာသနာႏွင့္ ယေန႔ကမာၻ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Dr-Nandanarlar-24-10-11-singapore.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ မစၨ်ိမ ပဋိပဒါတရားေဒသနာေတာ္ (စင္ကာပူ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.2.22.PM.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာ ႏွင့္ သမဏ ၄ မ်ိဳးအ ေၾကာင္းတရားေဒသနာေတာ္ (၂၂.၀၂.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/103.mp3"><span style="color: #ffcc00;">ျမန္မာတို႔၏ မဂၤလာပါ (၂၉.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/093.mp3"><span style="color: #ffcc00;">ျမန္မာတို႔၏ယဥ္ေက်းမႈႏွင္႔ ရွင္ျပဳမဂၤလာ (၈.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/25.mp3"><span style="color: #ffcc00;">ျမန္မာတို႔ရဲ႕ မဂၤလာပါ အေၾကာင္း တရားေဒသနာေတာ္ (၂၉.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/050-Dr-Nandamalabhivamsa-MP3-1-ManKanThawKyoSarArHoteMu.mp3"><span style="color: #ffcc00;">မွန္ကန္ေသာ ႀကိဳးစားအားထုတ္မႈ တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/128-ndml.mp3"><span style="color: #ffcc00;">ျမတ္ေသာဥစၥာစုေဆာင္းပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/013.ndml%202.mp3"><span style="color: #ffcc00;">မွတ္ဉာဏ္ေကာင္းေအာင္က်င့္ေဆာင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/033.mp3"><span style="color: #ffcc00;">မွန္ကန္စြာ ေရြးခ်ယ္ျခင္း (၂၈.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/139-ndml.mp3"><span style="color: #ffcc00;">မွန္ကန္ေသာ ႀကိဳးပန္းအားထုတ္မႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/259-ndml.mp3"><span style="color: #ffcc00;">ေမြးေန႔တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/24.mp3"><span style="color: #ffcc00;">ေမြးေန႔မဂၤလာ အခမ္းအနား အႏုေမာဒနာ ၾသဝါဒတရား(၂၉.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/125.ndml%202.mp3"><span style="color: #ffcc00;">ေမြးေန႔လက္ေဆာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/350.mp3"><span style="color: #ffcc00;">ေမြးေန႔လွဴဒါန္းမႈအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/752.mp3"><span style="color: #ffcc00;">ေမြးေန႔အမွတ္တရ ဂုဏပူဇာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/324-ndml.mp3"><span style="color: #ffcc00;">ေမြးေန႔အမွတ္တရၾသ၀ါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/360.mp3"><span style="color: #ffcc00;">ေမြးေန႔အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/094.ndml%202.mp3"><span style="color: #ffcc00;">ေမြးေန႕အႏုေမာဒနာ ( ကိုရန္ေအာင္ျဖဴး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/149.ndml%202.mp3"><span style="color: #ffcc00;">ေမြးေန႕အႏုေမာဒနာ (ျပင္ဦးလြင္မ်က္စိအထူးကုဆရာဝန္ၾကီးအိမ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/133.mp3"><span style="color: #ffcc00;">မေမဖူးသက္၏ (၂၂)ျပည့္မဂၤလာဆြမ္း မဂၤလာ အႏုေမာဒနာတရား (၃၀.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/696.mp3"><span style="color: #ffcc00;">ေမွ်ာ္လင္႔ျခင္း၏ အင္အားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/109.mp3"><span style="color: #ffcc00;">ေမတၱာဘာဝနာ (၅၂၈သြယ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/220-ndml.mp3"><span style="color: #ffcc00;">၁၂-ႏွစ္ၾကာအေျဖရွာခဲ႔ရေသာေမးခြန္းမ်ား</span></a></p>
<h5><span style="color: #00ffff;">&#8220;ရ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/349-ndml(20.3.16).mp3"><span style="color: #ffcc00;">ရင္တြင္းကေလာဘ ဖယ္ရွားၾက (၂၀.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/342-ndml(8.6.16).mp3"><span style="color: #ffcc00;">ရင္ထဲက ရတနာ (၈.၆.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/370-ndml(20.5.16).mp3"><span style="color: #ffcc00;">ရန္သူနဲ႔မိတ္ေဆြ (၂၀.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/334-ndml(21.1.16).mp3"><span style="color: #ffcc00;">ရဟန္းခံရွင္ျပဳ ျမတ္ေကာင္းမႈ (၂၁.၁.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/354-ndml(30.3.16).mp3"><span style="color: #ffcc00;">ရိုးသားၾကိဳးစား လူ႔စြမ္းအား (၃၀.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/052.mp3"><span style="color: #ffcc00;">႐ွင္မဟာေကာ႒ိကအားေဟာၾကားအပ္ေသာဝိပႆနာက်င့္စဥ္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0839-ndml(21.3.16).mp3"><span style="color: #ffcc00;">ရွင္ျပဳနားသ အနုေမာဒနာ (၂၁.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0836-ndml(2.3.16).mp3"><span style="color: #ffcc00;">ေရြးခ်ယ္ရမည့္လူ (၂.၃.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/369-ndml(19.5.16).mp3"><span style="color: #ffcc00;">ေရႊတစ္ေန႔ ေငြတစ္ေန႔ လူ႔ဘဝ၏အခိ်ဳးအေကြ႔မ်ား (၉.၅.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/024.mp3"><span style="color: #ffcc00;">ရခဲတဲ႔အခြင္႔အေရး သံုးပါး (၈.၁၁၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/295-ndml.mp3"><span style="color: #ffcc00;">ရင္းႏွီးျမွပ္ႏွံျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0100-NDML.mp3"><span style="color: #ffcc00;">ရင္ထဲမွဓမၼစြမ္းအားမ်ား-၁ (၉-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0101-NDML.mp3"><span style="color: #ffcc00;">ရင္ထဲမွဓမၼစြမ္းအားမ်ား-၂ (၁၀-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0009-NDML.mp3"><span style="color: #ffcc00;">ရတနာသံုးရပ္အၿမဲဆည္းကပ္သည္႔ဥပါသကာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/326-ndml.mp3"><span style="color: #ffcc00;">ရန္ကုန္ၿမိဳ႔သဒၵမၼရံသီေယာဂီမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0048-NDML.mp3"><span style="color: #ffcc00;">ရန္ရွင္းမွရန္ကင္းမည္ (၅-၄-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/282-ndml.mp3"><span style="color: #ffcc00;">ရသတဏွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/31.mp3"><span style="color: #ffcc00;">ရဟန္းခံ အလွဴေတာ္ မဂၤလာအခမ္းအနား အႏုေမာဒနာတရား (၁၂.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/821.mp3"><span style="color: #ffcc00;">ရဟန္းခံရွင္ျပဳၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/816.mp3"><span style="color: #ffcc00;">ရဟန္းခံၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/670.mp3"><span style="color: #ffcc00;">ရဟန္းငါးရာအတြက္ ဝိပႆနာအလုပ္ေပး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/035.mp3"><span style="color: #ffcc00;">ရဟႏၱာျဖစ္ရန္ အက်င္႔မွန္ (၂.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/021.ndml%202.mp3"><span style="color: #ffcc00;">ရာဓရဟန္း၏အေမးကိုေျဖဆိုျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/167.mp3"><span style="color: #ffcc00;">ရိုးသားေျဖာင္႔မတ္ျခင္းသည္ လူတို႔၏ဂုဏ္ရည္ (၆.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/142.mp3"><span style="color: #ffcc00;">ရဲစြမ္းသတိၱရွိသူမ်ား (၂၃.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/272-ndml.mp3"><span style="color: #ffcc00;">ရဲစြမ္းသတၱိရွိသူမွေအာင္ႏိုင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/018.mp3"><span style="color: #ffcc00;">ရွင္တိႆ၏ ဝိပႆနာ (၁၁.၁၀၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/075.mp3"><span style="color: #ffcc00;">ရွင္ပါကုလမေထရ္ျမတ္၏ ဆံုးမစကား (၁.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/60.mp3"><span style="color: #ffcc00;">ရွင္ျပဳအလွဴေတာ္ မဂၤလာ အႏုေမာဒနာတရား (၂၂.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/28.mp3"><span style="color: #ffcc00;">ရွင္ျပဳအလွဴေတာ္မဂၤလာ အခမ္းအနား အႏုေမာဒနာ တရား (၃၁.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/22.11.2014/17%20%286.12.2014%20am%29.mp3"><span style="color: #ffcc00;">ရွင္ျပဳအလွဴေတာ္မဂၤလာ အႏုေမာဒနာတရားေဒသနာေတာ္ (၆.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/64.mp3"><span style="color: #ffcc00;">ရွင္ျပဳအလွဴေတာ္မဂၤလာအခမ္းအနား အႏုေမာဒနာတရား (၂၇.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/207.mp3"><span style="color: #ffcc00;">ရွင္သမိဒၶႏွင္႔ နတ္မိမယ္ (၁၇.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0044-NDML.mp3"><span style="color: #ffcc00;">ရွစ္ေယာက္ႏွင္႔တစ္ေယာက္ (၉-၂-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/078.ndml%202.mp3"><span style="color: #ffcc00;">ရွာေဖြျခင္း ႏွင့္ ရရွိျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/083-ndml.mp3"><span style="color: #ffcc00;">ရတနာသံုးရပ္အၿမဲဆည္းကပ္သည္႕ဥပါသကာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/120-ndml.mp3"><span style="color: #ffcc00;">ရန္ရွင္းမွရန္ကင္းမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com//wp-content/uploads/mp3/DrNandamalabhivamsa/disc1/ndml.02/008-ndml.mp3"><span style="color: #ffcc00;">ရုပ္တရားကို ေလ့လာသံုးသပ္ျခင္း-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com//wp-content/uploads/mp3/DrNandamalabhivamsa/disc1/ndml.02/009-ndml.mp3"><span style="color: #ffcc00;">ရုပ္တရားကို ေလ့လာသံုးသပ္ျခင္း-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/023-DrNandamalabhivamsa-ShinTharReatPoakTaYarMaHtayMyatEatNhitMaTaw.mp3"><span style="color: #ffcc00;">ရွင္သာရိပုတၱရာ ႏွစ္မေတာ္တို႔၏ ဓမၼအျမင္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/090-ndml.mp3"><span style="color: #ffcc00;">ရွင္သာရိပုတၱရာမေထရ္ျမတ္၏သာသနာေတာ္အေရးေလ်ွာက္ထားခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0116-NDML.mp3"><span style="color: #ffcc00;">ေရစက္ခ်တရား (၂၀-၁၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/171-ndml.mp3"><span style="color: #ffcc00;">ေရစက္ခ်အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/311-ndml.mp3"><span style="color: #ffcc00;">ေရစက္ခ်အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/361.mp3"><span style="color: #ffcc00;">ေရစင္ေရစက္ခ်အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/181-ndml.mp3"><span style="color: #ffcc00;">ေရာဂါကုစားစိတ္စြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/32.mp3"><span style="color: #ffcc00;">ေရစက္သြန္းခ် အလွဴေတာ္ &#8211; ၁ ( Hi-Tech ဓမၼသဟာရတြင္ ခင္းက်င္းေသာ ကြန္းကရစ္လမ္းမႀကီး )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/33.mp3"><span style="color: #ffcc00;">ေရစက္သြန္းခ် အလွဴေတာ္ &#8211; ၂ ( Hi-Tech ဓမၼသဟာရတြင္ ခင္းက်င္းေသာ ကြန္းကရစ္လမ္းမႀကီး )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0123-NDML.mp3"><span style="color: #ffcc00;">ေရာဂါကုစားစိတ္စြမ္းအား (၁၀-၁-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/137.mp3"><span style="color: #ffcc00;">ေရာင့္ရဲျခင္းအေၾကာင္း တရားေဒသနာေတာ္ (၂၉.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/127.mp3"><span style="color: #ffcc00;">ေရာင္႔ရဲျခင္း (၂၉.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/138.mp3"><span style="color: #ffcc00;">ေရႊသားအစစ္ လူ႔အႏွစ္ (၂.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/265-ndml.mp3"><span style="color: #ffcc00;">ေရႊဥမင္ဆရာေတာ္ႀကီးအမွတ္တရ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/266-ndml.mp3"><span style="color: #ffcc00;">ေရႊဥမင္ဆရာေတာ္ႀကီးအမွတ္တရ(၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;လ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/038.mp3"><span style="color: #ffcc00;">လူ႔ကမၻာႀကီးကိုဖ်က္ဆီးသည့္ လူတို႔၏စ႐ိုက္ဆိုးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/351-ndml(26.3.16).mp3"><span style="color: #ffcc00;">လူ႔စိတ္ကို အဘိဓမၼာေဒသနာေတာ္အရ ေလ့လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/404-ndml(21.8.16).mp3"><span style="color: #ffcc00;">လူတိုင္းရႈ႕ပါ ဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/368-ndml(4.5.16).mp3"><span style="color: #ffcc00;">လူတိုင္းၾကိဳးစား ကုသိုလ္စီးပြား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/376-ndml(30.5.16).mp3"><span style="color: #ffcc00;">လူမိုက္ႏွင့္ သံသရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/051.mp3"><span style="color: #ffcc00;">လူမူကူညီ ျမတ္ပါရမီအေၾကာင္းတရားေတာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/366-ndml(1.5.16).mp3"><span style="color: #ffcc00;">လူေရြးပြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0837-ndml(13.3.16).mp3"><span style="color: #ffcc00;">လွည္းကူးဓမၼဝိနယေက်ာင္းလႊတ္ပူဇာေရစက္ခ်အနုေမာဒနာ</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုႏွစ္ထိ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/060.ndml%202.mp3"><span style="color: #ffcc00;">လက္တြဲညီညာ သာသနာျပဳၾက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/719.mp3"><span style="color: #ffcc00;">လက္ေတြ႔က်ေသာ အဆံုးအမ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0071-NDML.mp3"><span style="color: #ffcc00;">လက္ေတြ႔ဘ၀ကိုပဋိစၥသမုပၸါဒ္နည္းျဖင္႔ဆင္ျခင္သံုးသပ္ျခင္း (၁၃-၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0052-NDML.mp3"><span style="color: #ffcc00;">လက္ေတြ႔ဘ၀ကိုပဌာန္းျဖင္႔ေလ႔လာသံုးသပ္ျခင္း-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0053-NDML.mp3"><span style="color: #ffcc00;">လက္ေတြ႔ဘ၀ကိုပဌာန္းျဖင္႔ေလ႔လာသံုးသပ္ျခင္း-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/007.ndml%202.mp3"><span style="color: #ffcc00;">လက္ေတြ႕ဘဝႏွင့္ဒုကၡသမုဒယသစၥာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/356.mp3"><span style="color: #ffcc00;">လမ္းမွန္ႏွင္႔လမ္းမွား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/835.mp3"><span style="color: #ffcc00;">လမ္းႏွစ္သြယ္ျဖင့္ သံမတၱနိယာမသုိ႕၀င္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/192-ndml.mp3"><span style="color: #ffcc00;">လြတ္ေျမာက္တဲ႔စိတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/671.mp3"><span style="color: #ffcc00;">လြတ္ေျမာက္တဲ႔စိတ္အတြက္အားလံုးကို စြန္႔လြတ္ရမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/041.ndml%202.mp3"><span style="color: #ffcc00;">လိုခ်င္တာရႏိုင္ဖို႔လက္ေတြ႕က်င့္သံုးစို႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/584.mp3"><span style="color: #ffcc00;">လုပ္မိတဲ႔အမွားဖယ္ရွားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/106.mp3"><span style="color: #ffcc00;">လူ႔ဘဝႏွင္႔ ဓနဥစၥာ (၃.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/063.mp3"><span style="color: #ffcc00;">လူ႔ယဥ္ေက်းမႈႏွင္႔ ဂါရဝ (၂၁.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0005-NDML.mp3"><span style="color: #ffcc00;">လူ႔ျပည္ေရာက္နတ္တမန္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/046.mp3"><span style="color: #ffcc00;">လူ႔အရည္အခ်င္း (၁၇.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/152.mp3"><span style="color: #ffcc00;">လူ႔အရည္အခ်င္းမ်ာ (၂.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/176.mp3"><span style="color: #ffcc00;">လူဂုဏ္သိကၡာ (၁၉.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/644.mp3"><span style="color: #ffcc00;">လူဆယ္ေယာက္တြင္ အေတာ္ဆံုးလူတစ္ေယာက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/003.ndml%202.mp3"><span style="color: #ffcc00;">လူဆိုးလူမိုက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/784.mp3"><span style="color: #ffcc00;">လူဆႏၵ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/785.mp3"><span style="color: #ffcc00;">လူဆႏၵ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/148.mp3"><span style="color: #ffcc00;">လူတို႔၏ ကာမစၦႏၵ (၂၉.၁၀၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/304-ndml.mp3"><span style="color: #ffcc00;">လူတိုင္းက်င္႔ရန္သတိပဌာာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/956.mp3"><span style="color: #ffcc00;">လူတိုင္းရႈပြား ဝိပႆနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/247-ndml.mp3"><span style="color: #ffcc00;">လူတိုင္းအတြက္၀ိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0040-NDML.mp3"><span style="color: #ffcc00;">လူထဲကလူ (၁၉-၁၂-၂၀၀၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/908.mp3"><span style="color: #ffcc00;">လူမြဲဘဝမွ လာခဲ႔သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/173-ndml.mp3"><span style="color: #ffcc00;">လူျဖစ္က်ိဳးနပ္ပါေစ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/004.ndml%202.mp3"><span style="color: #ffcc00;">လူလိမၼာ ပညာရွိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/039.ndml%202.mp3"><span style="color: #ffcc00;">လူေတြေျပာၾကတဲ့လူ႕စကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/754.mp3"><span style="color: #ffcc00;">လူေတာ္လူေကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/178.mp3"><span style="color: #ffcc00;">လူေလာကမွ ေကာလဟာလမ်ား (၂၁.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/130.mp3"><span style="color: #ffcc00;">လူႏွင္႔စကား သတိထား (၁၇.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/136.mp3"><span style="color: #ffcc00;">လူႀကီးေရြးပြဲ (၁.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/753.mp3"><span style="color: #ffcc00;">ေလ႔က်င္ပြားမ်ားသညာမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/235-ndml.mp3"><span style="color: #ffcc00;">ေလာက၏အဆံုးသို႔ေရာက္ရွိျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/180-ndml.mp3"><span style="color: #ffcc00;">ေလာကဓံမုန္တိုင္းမ်ားႏွင္႔ႀကံ႔ခိုင္သည္႔စိတ္ထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/079.mp3"><span style="color: #ffcc00;">ေလာကသားတို႔အတြက္ ဓမၼအလင္းေရာင ္(၁၃.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0084-NDML.mp3"><span style="color: #ffcc00;">ေလာဘႏွင္႔အေလာဘ (၉-၈-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/124-ndml.mp3"><span style="color: #ffcc00;">လက္ေတြ႔ဘဝကိုပဠာန္းနည္းျဖင္႔ေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/082-ndml.mp3"><span style="color: #ffcc00;">လူ့႕ျပည္ေရာက္ နတ္တမန္မ်ားအေၾကာင္း တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/024-DrNandamalabhivamsa-LuHairKaLu.mp3"><span style="color: #ffcc00;">လူထဲကလူ တရားေဒသနာေတာ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;၀&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/337-ndml(24.2.16).mp3"><span style="color: #ffcc00;">ဝိနယေဒသနာနွင့္ ျမတ္ဗုဒၶသာသနာ (၂၄.၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0855-ndml(5.2.16).mp3"><span style="color: #ffcc00;">ဝိဝါဒမူလေျခာက္ပါးနွင့္ျမတ္ဗုဒၶ၏အဆံုးအမစကား(၅.၂.၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/694.mp3"><span style="color: #ffcc00;">ဝကၠလိရဟန္းအတြတ္စိတ္ဓါတ္ခြန္အားႏွင္႔ ဓမၼစြမ္းပကား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/351.mp3"><span style="color: #ffcc00;">ဝင္းပအထည္ခ်ဳပ္ ဆြမ္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/887.mp3"><span style="color: #ffcc00;">ဝဇၨီႏိုင္ငံေတာ္ ဖြံၿဖိဳးတိုးတက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/349.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/134.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းဆပ္ကပ္လွဴဒါန္းျခင္း အႏုေမာဒနာတရား (၃.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/131.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းဆပ္ကပ္လွဴဒါန္း အႏုေမာဒနာတရား (၂၉.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/323-ndml.mp3"><span style="color: #ffcc00;">၀ါဆိုသကၤန္းကပ္အႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/840.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္အႏုေမာဒနာ (တပည္႕အမ်ား)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/880.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္အႏုေမာဒနာ (ဓမၼဗ်ဴဟာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/836.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္အႏုေမာဒနာ(လႈိင္တကၠသိုလ္ဝင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/824.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္ၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/825.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္ၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/823.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္ၾသ၀ါဒ (ဦးကာလိက)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/860.mp3"><span style="color: #ffcc00;">၀ါဆုိသကၤန္းကပ္ၾသ၀ါဒ (ဦးခ်စ္ေမႊး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/346.mp3"><span style="color: #ffcc00;">ဝါဆိုသကၤန္းကပ္အႏုေမာဒနာ ( AKH မိသားစု)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/251-ndml.mp3"><span style="color: #ffcc00;">၀ိဇၨာႏွင္႔အ၀ိဇၨာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/273-ndml.mp3"><span style="color: #ffcc00;">၀ိယေတာ ဇာယေတ ေသာေကာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/369.mp3"><span style="color: #ffcc00;">ဝိညာဏ္သည္ အတၱမဟုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/036.ndml%202.mp3"><span style="color: #ffcc00;">ဝိပႆနာက်င့္စဥ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/107.ndml%202.mp3"><span style="color: #ffcc00;">ဝိပႆနာသမၼာဒိ႒ိကို ေလ့က်င့္ေမြးျမဴျခင္းႏွင့္ထိန္းသိမ္းေစာင့္ေရွာက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/070.mp3"><span style="color: #ffcc00;">ဝိသာခ၏ညီမကို ဆံုးမျခင္း (၂၇.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/697.mp3"><span style="color: #ffcc00;">ဝီေဏာပမသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<h5><span style="color: #00ffff;">&#8220;သ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/028.mp3"><span style="color: #ffcc00;">သံသရာခရီးသြားႏွင့္ကံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/344-ndml(8.3.16).mp3"><span style="color: #ffcc00;">သံသရာနွင့္ နိဗၺာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/345-ndml(14.3.16).mp3"><span style="color: #ffcc00;">သန္႔စင္ေစရမည့္ အညစ္အေၾကးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0852-ndml(17.5.16).mp3"><span style="color: #ffcc00;">သရဏဂံုတင္အမွ်ေဝျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/016.mp3"><span style="color: #ffcc00;">သီလႏွင့္ ပညာသည္ လူ႕အရည္အခ်င္း အေၾကာင္းတရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0840-ndml(22.3.16).mp3"><span style="color: #ffcc00;">သုခခ်မ္းသာ ရေၾကာင္းျဖာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/039.mp3"><span style="color: #ffcc00;">သုခပတၳနာသုတ္ အႏွစ္ခ်ဳပ္ တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0844-ndml(19.2.14).mp3"><span style="color: #ffcc00;">သုတကို ျမတ္နိုးပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/356-ndml(7.4.16).mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔၏ စြမ္းအား (ျပင္ဦးလြင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/378-ndml(10.7.16).mp3"><span style="color: #ffcc00;">ေသမင္း၏ နယ္ေျမကိုျဖတ္ေက်ာ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/403-ndml(19.8.16).mp3"><span style="color: #ffcc00;">ေသျခင္းမွ ထာဝရလြတ္ေျမာက္ေရး</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုနွစ္ထိ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/192.mp3"><span style="color: #ffcc00;">သံဃဖခင္ႀကီးမ်ားကို ေလးစားျခင္း (၂၇.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/917.mp3"><span style="color: #ffcc00;">သံဃာရတနာႏွင္႔သာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/814.mp3"><span style="color: #ffcc00;">သံသရာခရီးသြား ပ်က္စီးမွုေတြ သတိထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/582.mp3"><span style="color: #ffcc00;">သံသရာခရီးသြား အမွားလုပ္မိသူမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/286-ndml.mp3"><span style="color: #ffcc00;">သံသရာခရီးသြားအမွားမလုပ္မိေစႏွင္႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/071.ndml%202.mp3"><span style="color: #ffcc00;">သံသရာအမွား ႏွင့္ ရွင္သာရိပုၾတာ၏အၾကင္နာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/127.mp3"><span style="color: #ffcc00;">သံသရာႏွင္႔ နိဗၺာန္ – ၁ (၄.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/128.mp3"><span style="color: #ffcc00;">သံသရာႏွင္႔ နိဗၺာန္ – ၂ (၅.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/891.mp3"><span style="color: #ffcc00;">သံုးျခင္းႏွင္႔ ဆံုးျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/044.mp3"><span style="color: #ffcc00;">သံုးသပ္ဆင္ျခင္ စိတ္ထားျပင္ (၁၂.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/635.mp3"><span style="color: #ffcc00;">သံုးသပ္ဆင္ျခင္ျခင္းႏွင္႔အမွန္ျမင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/264-ndml.mp3"><span style="color: #ffcc00;">သံေ၀ဇနိယ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/224-ndml.mp3"><span style="color: #ffcc00;">သံေယာဇဥ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/830.mp3"><span style="color: #ffcc00;">သံေယာဇဥ္ကုိရွာေဖြျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/189.mp3"><span style="color: #ffcc00;">သံေဝဂဝတၳဳရွစ္ပါးႏွင္႔ သံေဝဂ (၁၄.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/714.mp3"><span style="color: #ffcc00;">သံေဝဂၾသဝါဒ (ေဒါက္တာဦးကိုကိုႀကီး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/131.ndml%202.mp3"><span style="color: #ffcc00;">သကၠာယဒိ႒ိက နိဗၺာန္လမ္းေၾကာင္းကို ပိတ္ဆို႕ထားသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/208-ndml.mp3"><span style="color: #ffcc00;">သက္ေတာ္(၆၉)ႏွစ္ျပည္႔ၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/305-ndml.mp3"><span style="color: #ffcc00;">သခၤတႏွင္႔အသခၤတ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/005.ndml%202.mp3"><span style="color: #ffcc00;">သင္ယူျခင္း ႏွင့္ သာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/641.mp3"><span style="color: #ffcc00;">သစၥာသိမွအမွန္ျမင္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/117.ndml%202.mp3"><span style="color: #ffcc00;">သစၥာအနက္ (၁၆)ခ်က္ကို ေလ့လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/246-ndml.mp3"><span style="color: #ffcc00;">သညာအသိႏွင္႔ပညာအသိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/318-ndml.mp3"><span style="color: #ffcc00;">သတိမထားကလွည္႔စားခံရျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/102.mp3"><span style="color: #ffcc00;">သတိျပဳေရွာင္ရွား ခိုးျခင္းႏွစ္ဆယ္႔ငါးပါး – ၁ (၁၀.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/103.mp3"><span style="color: #ffcc00;">သတိျပဳေရွာင္ရွား ခိုးျခင္းႏွစ္ဆယ္႔ငါးပါး – ၂ (၁၁.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/312-ndml.mp3"><span style="color: #ffcc00;">သတိၱမကြာအသိပညာျဖင္႔ေနထိုင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/897.mp3"><span style="color: #ffcc00;">သတိေကာင္းေအာင္က်င္႔ေဆာင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0165-NDML.mp3"><span style="color: #ffcc00;">သတၱဝါတို႔၏ (၃၁) ဘံု (၂၈-၃-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/898.mp3"><span style="color: #ffcc00;">သတၱဝါတို႔၏ဘဝႏွင္႔ျမတ္ဗုဒၶ၏ရႈျမင္သံုးသပ္ခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/101.ndml%202.mp3"><span style="color: #ffcc00;">သဒၶမၼပတိရူပကသုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/713.mp3"><span style="color: #ffcc00;">သန္႔ရွင္းစင္ၾကယ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/195-ndml.mp3"><span style="color: #ffcc00;">သဘာ၀တရား၏လွည္႔စားမႈမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0137-NDML.mp3"><span style="color: #ffcc00;">သဘာဝ၏လွည္႔စားမႈမ်ား (၁၅-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/067.mp3"><span style="color: #ffcc00;">သမဂၢႏွင္႔ ဝိဝါဒ (၂၅.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0087-NDML.mp3"><span style="color: #ffcc00;">သမၺဳတိသစၥာႏွင္႔ပရမတၱသစၥာ (၁၉-၈-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/303-ndml.mp3"><span style="color: #ffcc00;">သမထပုဗၺဂၤမ ၀ိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0115-NDML.mp3"><span style="color: #ffcc00;">သမထႏွင္႔၀ိပႆနာ (၁၈-၁၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/831.mp3"><span style="color: #ffcc00;">သမၼဒိဌိႏွင့္ မိစာၦဒိဌိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/583.mp3"><span style="color: #ffcc00;">သမၼာပဋိပဒါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/243-ndml.mp3"><span style="color: #ffcc00;">သမာဒိဌိအေၾကာင္းေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/338.mp3"><span style="color: #ffcc00;">သမာဓိဘာဝနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/690.mp3"><span style="color: #ffcc00;">သမာဓိဘာဝနာ စြမ္းေဆာင္မႈေလးမ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0015-NDML.mp3"><span style="color: #ffcc00;">သမာပတိသုတၱန္ (၂-၃-၁၉၉၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0014-NDML.mp3"><span style="color: #ffcc00;">သမာပတိသုတၱန္ (၂၆-၁၂-၁၉၉၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/341.mp3"><span style="color: #ffcc00;">သြားဘက္္ဆိုင္ရာ မဟာပုရိသလကၡဏာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/060.mp3"><span style="color: #ffcc00;">သားေကာင္းသမီးေကာင္း (၁၇.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/625.mp3"><span style="color: #ffcc00;">သာတိရဟန္း၏ မိစၦာဝါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/028.mp3"><span style="color: #ffcc00;">သာမညဖလႏွင႔္ တန္ေဆာင္တိုင္ည၏အမွတ္တရ (၁၆.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/154.ndml%202.mp3"><span style="color: #ffcc00;">သာမာဝတီ၏ဘဝ ႏွင့္ သခၤန္းစာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/040.ndml%202.mp3"><span style="color: #ffcc00;">သာရဏီယ အႏုေမာဒနာ (သံလ်င္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/568.mp3"><span style="color: #ffcc00;">သာရဏီယ ၾသဝါဒကထာ (ဦးစံသာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/233-ndml.mp3"><span style="color: #ffcc00;">သာရဏီယတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/570.mp3"><span style="color: #ffcc00;">သာရဏီယၾသဝါဒကထာ (သြားေဆးတကၠသိုလ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/057.mp3"><span style="color: #ffcc00;">သာသနာ႔အရိပ္မွာ ပညာ (၉.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/135.ndml%202.mp3"><span style="color: #ffcc00;">သာသနာကိုျမတ္ႏုိးသူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/002.mp3"><span style="color: #ffcc00;">သာသနာပူဇာ ျမတ္မဂၤလာ (၁၈.၁၁.၂၀၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/164-ndml.mp3"><span style="color: #ffcc00;">သာသနာျပဳစြမ္းအားစု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/253-ndml.mp3"><span style="color: #ffcc00;">သာသနာျပဳျမတ္ေကာင္းမႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/203-ndml.mp3"><span style="color: #ffcc00;">သာသနာေတာ္ရွည္ၾကာတည္တံ႔ေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/066.ndml%202.mp3"><span style="color: #ffcc00;">သိကၡာထပ္၊ ရဟန္းခံ၊ေမြးေန႕ အလွဴအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/699.mp3"><span style="color: #ffcc00;">သိမ္ေရစက္ခ်အႏုေမာဒနာ(သန္လ်င္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/327-ndml.mp3"><span style="color: #ffcc00;">သီတဂူဗုဒၶတကၠသိုလ္ေက်ာင္းသားသစ္ႀကိဳဆိုပြဲ ၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/703.mp3"><span style="color: #ffcc00;">သီရိေဂဟာျဖစ္ေအာင္က်င္႔ေဆာင္ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/364.mp3"><span style="color: #ffcc00;">သီရိေသာ္တာအလွဴအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/591.mp3"><span style="color: #ffcc00;">သီလစြမ္းအား အက်ိဳးဆယ္ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/712.mp3"><span style="color: #ffcc00;">သီလသည္နိဗၺာန္တိုင္ေအာင္အက်ိဳးေပးသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/134.ndml%202.mp3"><span style="color: #ffcc00;">သီလအေၾကာင္းကို ေလ့လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/778.mp3"><span style="color: #ffcc00;">သီလေစာင့္မွ အူမေတာင့္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/202.mp3"><span style="color: #ffcc00;">သီလေပး (၁၄.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/205.mp3"><span style="color: #ffcc00;">သီလေပး (၁၇.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/260-ndml.mp3"><span style="color: #ffcc00;">သီလႏွင္႔သုတ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/810.mp3"><span style="color: #ffcc00;">သီဟနာဒသုတ္ အႏွစ္ခ်ဳပ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/811.mp3"><span style="color: #ffcc00;">သီဟနာဒသုတ္ အႏွစ္ခ်ဳပ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-3%29/050.ndml%202.mp3"><span style="color: #ffcc00;">သုခခ်မ္းသာ အေၾကာင္းရွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/102.mp3"><span style="color: #ffcc00;">သုေမဓာေထရီမ၏ သံသရာဘဝမ်ားႏွင္႔ရင္တြင္းစကား (၂၈.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/737.mp3"><span style="color: #ffcc00;">သူ႔အျမင္ကိုယ္႔အျမင္ႏွင္႔ဓမၼအျမင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/229-ndml.mp3"><span style="color: #ffcc00;">သူ႔အေၾကာင္းကိုယ္႔အေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/132.mp3"><span style="color: #ffcc00;">သူတစ္ပါးအက်ိဳးေဆာင္ ကိုယ္႔က်ိဳးေအာင္ (၂၅.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/062.mp3"><span style="color: #ffcc00;">သူတို႔ဘဝ သူတို႔အေၾကာင္း တေစ႔တေစာင္း (၂၀.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/043.ndml%202.mp3"><span style="color: #ffcc00;">သူယုတ္မာတို႕၏ အမူအက်င့္မ်ား – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-2%29/044.ndml%202.mp3"><span style="color: #ffcc00;">သူယုတ္မာတို႕၏ အမူအက်င့္မ်ား -၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/560.mp3"><span style="color: #ffcc00;">သူျမတ္တို႔၏ ေလာကတၱိစရိယတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/129.mp3"><span style="color: #ffcc00;">သူလိုလူစား တရားမရွိ (၁၄.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/196.mp3"><span style="color: #ffcc00;">သူေတာ္သူျမတ္ (၂၇.၂.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/019.ndml%202.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္း ႏွင့္ သူေတာ္ေကာင္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0150-NDML.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရားတည္တံ႔ျပန္႔ပြားေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/145.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔ ေတာင္းေသာဆု (၂၆.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/036.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔၏ ဂုဏ္ရနံ႔ (၃.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/22.11.2014/8%20%2827.11.2014%20am%29.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔၏ အလွဴ႕ဒါနအေၾကာင္း တရားေဒသနာေတာ္ (၂၇.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/163.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔၏ အလွဴဒါန (၂၇.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/172-ndml.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတို႔၏စိတ္ေနသေဘာထား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/155.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းသည္ အားလံုးအတြက္ျဖစ္သည္ (၅.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0012-NDML.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းဥစၥာခုႏွစ္ျဖာ (၂၈-၃-၁၉၉၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/72.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းေတြ ေလွ်ာက္လမ္းတဲ့ လမ္းေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/027.mp3"><span style="color: #ffcc00;">သူေတာ္ေက်းဇူး အထူးသိျမင္ (၁၂.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/191-ndml.mp3"><span style="color: #ffcc00;">သေဗၺ ဓမၼာအနတၱာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/131.mp3"><span style="color: #ffcc00;">သႀကၤန္ အလုပ္ေပးတရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/132.mp3"><span style="color: #ffcc00;">သႀကၤန္ အလုပ္ေပးတရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.02/022-ndml.mp3"><span style="color: #ffcc00;">သတၱ၀ါတို ့၏ ၃၁ဘံု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com//wp-content/uploads/mp3/DrNandamalabhivamsa/disc1/ndml.02/007-ndml.mp3"><span style="color: #ffcc00;">သမၡတိသစၥာ ႏွင့္ ပရမတၱသစၥာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/086-ndml.mp3"><span style="color: #ffcc00;">သမာပတၱိ သုတၱန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/087-ndml.mp3"><span style="color: #ffcc00;">သမာပတၱိ သုတၱန္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/106-ndml.mp3"><span style="color: #ffcc00;">ေသာတပန္၏ဘဝရုပ္ပံုလႊာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0034-NDML.mp3"><span style="color: #ffcc00;">ေသာတာပန္၏ဘ၀ရုပ္ပံုလႊာ (၃၁-၃၀၂၀၀၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/164.mp3"><span style="color: #ffcc00;">ေသာတာပန္၏ဘဝႏွင္႔အသိ (၂၈.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/569.mp3"><span style="color: #ffcc00;">ေသာတာပန္ႏွင္႔ သံေယာဇဥ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/278-ndml.mp3"><span style="color: #ffcc00;">ေသ၀ိတဗၺႏွင္႔နေသ၀ိတဗၺ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/206-ndml.mp3"><span style="color: #ffcc00;">ေသခ်ာေသာလမ္းကေလွ်ာက္လွမ္းပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/673.mp3"><span style="color: #ffcc00;">ေသမင္းမျမင္ရာသို႔ သြားၾကစို႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/144-ndml.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရားတည္တန္႔ျပန္႔ပြားေရး</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;ဟ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/123.mp3"><span style="color: #ffcc00;">ဟိတႏွင္႔ သုခ (၁၇.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0104-NDML.mp3"><span style="color: #ffcc00;">ဟိုဘက္ကမ္းကၿငိမ္းေအးတယ္ (၁၅-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/081.ndml%202.mp3"><span style="color: #ffcc00;">ဟိုဘက္ကမ္းသို႕သြားၾကစို႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/023.ndml%202.mp3"><span style="color: #ffcc00;">ေဟာသူနာသူစိတ္ထားျဖဴ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">&#8220;အ, ဣ, ဥ, ၾသ&#8221; အကၡရာစဥ္ တရားေတာ္မ်ား</span></h5>
<h6><span style="color: #339966;">၂၀၁၆ခုႏွစ္တြင္ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/418-ndml(24.9.16).mp3"><span style="color: #ffcc00;">အပဏၰကသုတ္မွ ျမတ္ဗုဒၶ၏ အဆံုးအမစကား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/419-ndml(25.9.16).mp3"><span style="color: #ffcc00;">အပဏၰကသုတ္မွ ျမတ္ဗုဒၶ၏ အဆံုးအမစကား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/420-ndml(26.9.16).mp3"><span style="color: #ffcc00;">အပဏၰကသုတ္မွ ျမတ္ဗုဒၶ၏ အဆံုးအမစကား (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/407-ndml(27.8.16).mp3"><span style="color: #ffcc00;">အရွင္လတ္လတ္ ငရဲက်သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/397-ndml(8.8.16).mp3"><span style="color: #ffcc00;">အလိုရိွအပ္သူမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/030.mp3"><span style="color: #ffcc00;">အာဒိတၱသုတ္လာ ဗုဒၶေဟာၾကား ဝိပႆနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/339-ndml(29.2.16).mp3"><span style="color: #ffcc00;">အေပါင္းအသင္းနွစ္ေယာက္နွင့္ လူ႔ဘသ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/375-ndml(29.5.16).mp3"><span style="color: #ffcc00;">အေမွာင္တြင္းမွ အျမင္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/348-ndml(19.3.16).mp3"><span style="color: #ffcc00;">အေျပာအဆို လိမၼာယဥ္ေက်းမွု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/332-ndml(4.1.16).mp3"><span style="color: #ffcc00;">အၾကင္နာနွင့္ပညာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0846-ndml(31.12.14).mp3"><span style="color: #ffcc00;">အၾကမ္းဖက္မရိွေသာ ေမတၱာကမၻာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/0843-ndml(24.5.16).mp3"><span style="color: #ffcc00;">ေအာင္ခ်မ္းသာ ဆရာေတာ္ေမြးေန႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/374-ndml(23.5.16).mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ႀကီးပြား စိတ္(၄)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/377-ndml(9.7.16).mp3"><span style="color: #ffcc00;">ဥစၥာစီးပြား ယိုေပါက္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/025.mp3"><span style="color: #ffcc00;">ဥပါလိသုတ္မွ ဗုဒၶႏွင့္ နိဂ႑တို႔၏ မတူညီေသာကမၼ၀ါဒမ်ား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/026.mp3"><span style="color: #ffcc00;">ဥပါလိသုတ္မွ ဗုဒၶႏွင့္ နိဂ႑တို႔၏ မတူညီေသာကမၼ၀ါဒမ်ား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/027.mp3"><span style="color: #ffcc00;">ဥပါလိသုတ္မွ ဗုဒၶႏွင့္ နိဂ႑တို႔၏ မတူညီေသာကမၼ၀ါဒမ်ား (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2016/032.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတ္ကုိ ေလ့လာသုံးသပ္ျခင္းတရားေဒသနာေတာ္</span></a></p>
<h6><span style="color: #339966;">၂၀၁၅ခုႏွစ္ထိ ေဟာ္ၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/777.mp3"><span style="color: #ffcc00;">အံ႕ဖြယ္လူသား ျမတ္ဘုရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/336-ndml.mp3"><span style="color: #ffcc00;">အ၀ိဇၨာႏွင္႔၀ိဇၨာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0010-NDML.mp3"><span style="color: #ffcc00;">အကၡာနသုတၱန္ (၁၉-၁-၁၉၈၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0067-NDML.mp3"><span style="color: #ffcc00;">အကာကိုျပစ္၍အႏွစ္ကိုရွာ (၁၀-၁-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/606.mp3"><span style="color: #ffcc00;">အကုသိုလ္တားစိတ္စြမ္းအား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0042-NDML.mp3"><span style="color: #ffcc00;">အက်င္႔မွန္မွနိဗၺာန္ရ (၆-၁၀၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/095.mp3"><span style="color: #ffcc00;">အက်ိဳးႀကီးမားသည္႔ ဆံုစည္းမႈမ်ား (၁၂.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/321-ndml.mp3"><span style="color: #ffcc00;">အခက္အခဲေက်ာ္လႊားလူ႔ခြန္အား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/070.ndml%202.mp3"><span style="color: #ffcc00;">အခြင့္ေကာင္းကို ရေအာင္ယူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0153-NDML.mp3"><span style="color: #ffcc00;">အခြင္႔ေကာင္း (၁၉-၃-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/181.mp3"><span style="color: #ffcc00;">အခ်ိန္မေႏွာင္းမွီ ႀကိဳးစားျခင္း (၂၃.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/185.mp3"><span style="color: #ffcc00;">အခ်ိန္ႏွင္႔ႀကိဳးစား ျမတ္တရား (၂၈.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/899.mp3"><span style="color: #ffcc00;">အဂတိေလးပါး မလုိက္စားနဲ႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/597.mp3"><span style="color: #ffcc00;">အဂတိေလးပါး မလုိက္စားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0120-NDML.mp3"><span style="color: #ffcc00;">အင္အားရွိမွအခက္အခဲကိုေက်ာ္လႊားႏိုင္မည္ (၃၁-၁၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0114-NDML.mp3"><span style="color: #ffcc00;">အစြမ္းတန္ခိုးမ်ားႏွင္႔သာသနာ (၁၇-၁၁-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/916.mp3"><span style="color: #ffcc00;">အစြမ္းထက္ေသာကာကြယ္မႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/135-ndml.mp3"><span style="color: #ffcc00;">အစြဲျဖဳတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0069-NDML.mp3"><span style="color: #ffcc00;">အစြဲျဖဳတ္ (၃၁-၁-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/686.mp3"><span style="color: #ffcc00;">အဆံုးကိုေက်ာ္လြန္သည္႔ အဆံုးမဲ႔တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/949.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/950.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/951.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/952.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/953.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၅</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/954.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၆</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/955.mp3"><span style="color: #ffcc00;">အဆံုးအမမ်ား (စကၤာပူ) &#8211; ၇</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/121.mp3"><span style="color: #ffcc00;">အဆင္႔ေျခာက္ဆင္႔ျဖင္႔ သာသနာကြယ္ျခင္း (၃၀.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/674.mp3"><span style="color: #ffcc00;">အဆိုးဆံုးဒုကၡခ်ဳပ္ၿငိမ္းမွ အေကာင္းဆံုးခ်မ္းသာရမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/032.mp3"><span style="color: #ffcc00;">အဆိုးဆံုးဒုကၡႏွင္႔ အေကာင္းဆံုးခ်မ္းသာ (၂၀.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/727.mp3"><span style="color: #ffcc00;">အဆိုးသံသရာကို လြတ္ေျမာက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/150.mp3"><span style="color: #ffcc00;">အညစ္အေၾကးမ်ား ထာဝရသန္႔စင္ေရး (၃၁.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/031.mp3"><span style="color: #ffcc00;">အတံု႔အလွည္႔ႏွင္႔ ကာမနိယာမ၏သေဘာတရားမ်ား (၁၉.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0102-NDML.mp3"><span style="color: #ffcc00;">အတိုင္းမဲ႔ခ်မ္းသာ-၁ (၁၁-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0103-NDML.mp3"><span style="color: #ffcc00;">အတိုင္းမဲ႔ခ်မ္းသာ-၂ (၁၂-၁၀-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/589.mp3"><span style="color: #ffcc00;">အတၱဒီပႏွင္႔ တဒဂၤအၿငိမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/037.mp3"><span style="color: #ffcc00;">အတၱဟိတႏွင္႔ ပရဟိတ (၅.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0136-NDML.mp3"><span style="color: #ffcc00;">အတၱာဟိ အတၱေနာ နာေထာ (၁၄-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/288-ndml.mp3"><span style="color: #ffcc00;">အထင္မွားအျမင္မွား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0170-NDML.mp3"><span style="color: #ffcc00;">အထင္ႏွင္႔အျမင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0025-NDML.mp3"><span style="color: #ffcc00;">အဒိတၱာဇာတ္ (၁၇-၃-၂၀၀၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/620.mp3"><span style="color: #ffcc00;">အဓိပညာ ဓမၼဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/292-ndml.mp3"><span style="color: #ffcc00;">အနာမဲ႔ရွင္ဗာကု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0004-NDML.mp3"><span style="color: #ffcc00;">အၿမိဳက္ေရစင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/054.mp3"><span style="color: #ffcc00;">အဘယဌာနီ ေဘးမဲ႔ျပည္ (၄.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0013-NDML.mp3"><span style="color: #ffcc00;">အဘယသုတၱန္ (၁၃-၁၁-၁၉၉၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/605.mp3"><span style="color: #ffcc00;">အဘိဓမၼာက်မ္းမ်ား၏ေမးခြန္းႏွင္႔ ေျဖဆိုခ်က္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0142-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာဆိုင္ရာဗဟုသုတႏွင္႔အေမးအေျဖ-၁ (၂၁-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0143-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာဆိုင္ရာဗဟုသုတႏွင္႔အေမးအေျဖ-၂ (၂၂-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/842.mp3"><span style="color: #ffcc00;">အဘိဓမၼာဆုိင္ရာသင္တန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/576.mp3"><span style="color: #ffcc00;">အဘိဓမၼာပညာရပ္ႏွင္႔ပတ္သက္၍ ေမးခြန္းမ်ားကိုေျဖဆိုျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0086-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာျမတ္ေဒသနာ (၁၈-၈-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0138-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာသင္တန္းဆင္းၾသဝါဒ (၁၅-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/935.mp3"><span style="color: #ffcc00;">အဘိဓမၼာသင္ယူျခင္းသည္ သမၼာဒိဌိဥာဏ္ကိုရင္႔သန္ေစသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0169-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာသင္ယူရျခင္းအက်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0008-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာေန႔ျမတ္အခါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0141-NDML.mp3"><span style="color: #ffcc00;">အဘိဓမၼာႏွင္႔ဝိပႆနာ (၁၉-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/705.mp3"><span style="color: #ffcc00;">အဘိရူပနႏၵာ၏ဘဝႏွင္႔ ျမတ္ဗုဒၶ၏အဆံုးအမ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/095.ndml%202.mp3"><span style="color: #ffcc00;">အမၺၺပါလီ၏ဘဝ ႏွင့္ သခၤန္းစာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0020-NDML.mp3"><span style="color: #ffcc00;">အမတာဘိေသက (၁၄-၁၂-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0075-NDML.mp3"><span style="color: #ffcc00;">အမ်က္ေျဖ (၆-၃-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/092.mp3"><span style="color: #ffcc00;">အမ်ား၏ၾကည္ညိဳေလးစားမႈ (၅.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/043.mp3"><span style="color: #ffcc00;">အမ်ားအက်ိဳးျပဳ ေကာင္းမႈပါရမီ (၁၁.၁၂.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/191.mp3"><span style="color: #ffcc00;">အမ်ားအတြက္ သံဃာေတာ္မ်ား၏ေဆာင္ရြက္ခ်က္ (၂၆.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/201.mp3"><span style="color: #ffcc00;">အမ်ားအတြက္ သက္ေတာ္ရွည္ျခင္း (၉.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/144.mp3"><span style="color: #ffcc00;">အမ်ားႀကိဳက္တဲ႔ အမွားစရိုက္မ်ား (၂၅.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/258-ndml.mp3"><span style="color: #ffcc00;">အမွန္သိျခင္း မသိျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/612.mp3"><span style="color: #ffcc00;">အမွားကင္းစင္ပစၥကၡဥာဏ္အျမင္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/613.mp3"><span style="color: #ffcc00;">အမွားကင္းစင္ပစၥကၡဥာဏ္အျမင္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/716.mp3"><span style="color: #ffcc00;">အျငင္းပြားသူတို႔၏ အတြင္းေရးမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/565.mp3"><span style="color: #ffcc00;">အျပစ္ကင္းေသာ အစာအာဟာရ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/864.mp3"><span style="color: #ffcc00;">အျပစ္ကုိ ကုစားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/158.mp3"><span style="color: #ffcc00;">အျပစ္ခပ္သိမ္း လြတ္ၿငိမ္းေရး (၁၀.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/073.mp3"><span style="color: #ffcc00;">အျပစ္တင္ျခင္းႏွင႔္ ကဲ႔ရဲ႔ျခင္း (၂၉.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/261-ndml.mp3"><span style="color: #ffcc00;">အျဖဴလားအမဲလား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/139.mp3"><span style="color: #ffcc00;">အျမင္႔ဆံုး ေမွ်ာ္မွန္းခ်က္ရွိသူ (၃.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0068-NDML.mp3"><span style="color: #ffcc00;">အျမင္မွန္ (၂၃-၁-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/128.ndml%202.mp3"><span style="color: #ffcc00;">အျမင္ႏွစ္မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/71.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုးေသာ ဘာဝနာတရားျဖစ္တယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/238-ndml.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုးေသာဘာယ၀နာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/160.mp3"><span style="color: #ffcc00;">အျမတ္ဆံုးၾကည္ညိဳ ကိုးကြယ္မႈ (၁၇.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0019-NDML.mp3"><span style="color: #ffcc00;">အျမတ္ရတနာဥပသကာ (၁၃-၁၁-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/62.mp3"><span style="color: #ffcc00;">အရံႈးထဲက အျမတ္ရေရး တရားေဒသနာေတာ္ (၂၅.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/011.mp3"><span style="color: #ffcc00;">အရဏဝိဘဂၤသုတ္ အႏွစ္ခ်ဳပ္ (၁၄.၉.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/659.mp3"><span style="color: #ffcc00;">အရဏဝိဘဂၤသုတ္အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/624.mp3"><span style="color: #ffcc00;">အရိဌရဟန္း၏ မိစၦာဝါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/44.mp3"><span style="color: #ffcc00;">အရိယဘဝသို႔ေရာက္ေအာင္ က်င့္ေဆာင္ျခင္းအေၾကာင္း တရားေဒသနာေတာ္(၅.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/170.ndml%202.mp3"><span style="color: #ffcc00;">အရိယသစၥာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/108.mp3"><span style="color: #ffcc00;">အရိယာဘဝသို႔ေရာက္ေအာင္ က်င္႔ေဆာင္ျခင္း (၅.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/300-ndml.mp3"><span style="color: #ffcc00;">အရု၀တီသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/111.mp3"><span style="color: #ffcc00;">အရႈံးထဲက အျမတ္ရေရး (၂၅.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0063-NDML.mp3"><span style="color: #ffcc00;">အရႈံးအျမတ္-၁ (၆-၁၂-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0064-NDML.mp3"><span style="color: #ffcc00;">အရႈံးအျမတ္-၂ (၆-၁၂-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/100.ndml%202.mp3"><span style="color: #ffcc00;">အရႈပ္ကို ရွင္းႏိုင္သူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/017.mp3"><span style="color: #ffcc00;">အရွက္တရားႏွင္႔ အကုသိုလ္ကိုတားျခင္း (၁၀.၁၀.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/315-ndml.mp3"><span style="color: #ffcc00;">အရွင္ဆႏၵ၏၀ိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/122.ndml%202.mp3"><span style="color: #ffcc00;">အရွင္မိဂဇာလ၏ဝိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/030.mp3"><span style="color: #ffcc00;">အရွင္အာနႏၵာ၏ ယုဂနဒၶဘာဝနာ (၁၈.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/302-ndml.mp3"><span style="color: #ffcc00;">အရွင္အာနႏၵာ၏၀ိပႆနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0050-NDML.mp3"><span style="color: #ffcc00;">အရွင္အာနႏၵာ၏အလြမ္းစကားႏွင္႔ျမတ္ဗုဒၶ၏ၾသ၀ါဒတရား (၁၆-၇-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/672.mp3"><span style="color: #ffcc00;">အရွင္အာနႏၵာေဟာၾကားသည္႔ ေသခပဋိပဋာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/34.mp3"><span style="color: #ffcc00;">အလုပ္ေပးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/166.mp3"><span style="color: #ffcc00;">အလွဴဒါန၏ စြမ္းေဆာင္မႈမ်ား (၅.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/22.11.2014/16%20%285.12.2014%20pm%29.mp3"><span style="color: #ffcc00;">အလွဴဒါန၏ စြမ္းေဆာင္မႈမ်ားအေၾကာင္း တရားေဒသနာေတာ္ (၅.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/116.ndml%202.mp3"><span style="color: #ffcc00;">အလွဴအႏုေမာဒနာ (လင္း-စိန္ေရႊရတနာဆိုင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/26.mp3"><span style="color: #ffcc00;">အလွဴေတာ္မဂၤလာ အခမ္းအနား အႏုေမာဒနာတရား (၃၀.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/68.mp3"><span style="color: #ffcc00;">အလွဴေတာ္မဂၤလာအခမ္းအနား အႏုေမာဒနာတရား (၁၉.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/132.mp3"><span style="color: #ffcc00;">အလွဴေတာ္မဂၤလာအခမ္းအနား အႏုေမာဒနာ တရား (၂၆.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/135.mp3"><span style="color: #ffcc00;">အလွဴေတာ္ မဂၤလာအခမ္းအနား အႏုေမာဒနာတရား (၁၆.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/114.mp3"><span style="color: #ffcc00;">အသက္ရွည္သမွ် အက်ိဳးရွိေစရမည္ (၂၅.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/195.mp3"><span style="color: #ffcc00;">အသက္ရွည္ေလပိုေကာင္းေလ (၂၃.၂.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0108-NDML.mp3"><span style="color: #ffcc00;">အသိတရားရွိသူတုိ႔၏စိတ္ေနသေဘာထား (၅-၁၁-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0096-NDML.mp3"><span style="color: #ffcc00;">အသိသံုးပါးႏွင္႔အေမးအေျဖ-၁ (၁-၉-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0097-NDML.mp3"><span style="color: #ffcc00;">အသိသံုးပါးႏွင္႔အေမးအေျဖ-၂ (၁-၉-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/347.mp3"><span style="color: #ffcc00;">အိမ္သစ္တက္အလွဴအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/091.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးကို ေရြးခ်ယ္ျခင္း (၄.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/274-ndml.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးခ်မ္းသာရေအာင္ရွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/718.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးဘာသာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/263-ndml.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးလက္ေဆာင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0037-NDML.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးေသာညတစ္ည (၂၀-၁၀-၂၀၀၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/820.mp3"><span style="color: #ffcc00;">အေတြးမွားကုိ ဖယ္ရွားႏုိင္ရမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/104.ndml%202.mp3"><span style="color: #ffcc00;">အေဖၚနဲ႕ေနျခင္းႏွင့္ အေဖၚမဲ့ေနျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/119.ndml%202.mp3"><span style="color: #ffcc00;">အေမြ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/562.mp3"><span style="color: #ffcc00;">အေရာဂ်ံ ပရမာ လာဘာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/073.ndml%202.mp3"><span style="color: #ffcc00;">အေလးထား ၍စဥ္းစားဆင္ျခင္ေကာင္းေအာင္ျပင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/172.mp3"><span style="color: #ffcc00;">အေလးထားျခင္းမ်ားႏွင႔္ ဗုဒၶသာသနာ (၁၂.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/110.mp3"><span style="color: #ffcc00;">အေလးထားျခင္းသံုးမ်ိဳးျဖင္႔ ေနထိုင္ေဆာင္ရြက္ျခင္း (၁၈.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0056-NDML.mp3"><span style="color: #ffcc00;">အေလာင္းေတာ္သုေမဓါ၏ဘ၀အေပၚရႈျမင္သံုးသပ္ခ်က္ (၆-၉-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/254-ndml.mp3"><span style="color: #ffcc00;">အေၾကာင္းကင္းျမတ္အၿငိမ္းဓါတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/285-ndml.mp3"><span style="color: #ffcc00;">အေၾကာင္းစံုမွအေကာင္းစံုမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/679.mp3"><span style="color: #ffcc00;">အေၾကာင္းတရားကို စူးစမ္းရွာေဖြျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/145.ndml%202.mp3"><span style="color: #ffcc00;">အေၾကာင္းရွာၾကံ အေျဖမွန္ေတြ႕ – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/146.ndml%202.mp3"><span style="color: #ffcc00;">အေၾကာင္းရွာၾကံ အေျဖမွန္ေတြ႕ – ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/174.mp3"><span style="color: #ffcc00;">အႏုဂၢဟိတသုတ္ အႏွစ္ခ်ဳပ္ (၁၆.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/217-ndml.mp3"><span style="color: #ffcc00;">အႏုတမဂၢသံသရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/306-ndml.mp3"><span style="color: #ffcc00;">အႏုပုဗၺပဋိပဒါျမတ္ေဒသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/065.mp3"><span style="color: #ffcc00;">အႏုဗုဒၶသုတ္ အႏွစ္ခ်ဳပ္ (၂၃.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0128-NDML.mp3"><span style="color: #ffcc00;">အႏွစ္တစ္ရာႏွင္႔တစ္ေန႔တာ (၁၈-၁၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0107-NDML.mp3"><span style="color: #ffcc00;">အႏွစ္မဲ႔တာျမင္မွအႏွစ္သာရ ရႏိုင္သည္ (၄-၁၁-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/084-ndml.mp3"><span style="color: #ffcc00;">အကၡဏ သုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/133-ndml.mp3"><span style="color: #ffcc00;">အကာကိုျပစ္၍အႏွစ္ကိုရွာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/114-ndml.mp3"><span style="color: #ffcc00;">အက်င့္မွန္မွ နိဗၺာန္ရ တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/048-Dr-Nandamalabhivamsa-MP3-1_AswairPhote.mp3"><span style="color: #ffcc00;">အစြဲျဖဳတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/097-ndml.mp3"><span style="color: #ffcc00;">အဒိတၱာဇာတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.5.9.PM.mp3"><span style="color: #ffcc00;">အနာဂတ္၏ လူငယ္မ်ား အေၾကာင္းတရားေဒသနာေတာ္ (၀၉.၀၅.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/081-ndml.mp3"><span style="color: #ffcc00;">အၿမိဳက္ေရစင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/0851-ndml.mp3"><span style="color: #ffcc00;">အဘယ သုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com//wp-content/uploads/mp3/DrNandamalabhivamsa/disc1/ndml.02/006-ndml.mp3"><span style="color: #ffcc00;">အဘိဓမၼာ ေဒသနာေတာ္ၾကီး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/034-DrNandamalabhivamsa-AhBeatDhammarNaeMyatAhKhar.mp3"><span style="color: #ffcc00;">အဘိဓမၼာေန႔ျမတ္အခါ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/092-ndml.mp3"><span style="color: #ffcc00;">အမတာဘိေသက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/053-Dr-Nandamalabhivamsa-MP3-1-AhMyatPhay.mp3"><span style="color: #ffcc00;">အမ်က္ေျဖ တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.4.9.PM.mp3"><span style="color: #ffcc00;">အမ်ားအတြက္ သက္ေတာ္ရွည္ျခင္း တရားေတာ္ (၉.၀၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/049-Dr-Nandamalabhivamsa-MP3-1_AhMyinMan.mp3"><span style="color: #ffcc00;">အျမင္မွန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/091-ndml.mp3"><span style="color: #ffcc00;">အျမတ္ရတနာ ဥပါသကာက်င္႔စဥ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/130-ndml.mp3"><span style="color: #ffcc00;">အရံႈးအျမတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/122-ndml.mp3"><span style="color: #ffcc00;">အရွင္အာနႏၵာ၏အလြမ္းစကားႏွင္႔ျမတ္ဗုဒၶ၏ၾသဝါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/337.mp3"><span style="color: #ffcc00;">အဝိဇၨာႏွင္႔ဝိဇၨာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/109-ndml.mp3"><span style="color: #ffcc00;">အေကာင္းဆံုးေသာညတစ္ည</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/127-ndml.mp3"><span style="color: #ffcc00;">အေလာင္းေတာ္သုေမဓါ၏ဘဝအေပၚရႈျမင္သံုးသပ္ခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/129.mp3"><span style="color: #ffcc00;">အလုပ္ေပးတရား ( ၂၀၁၄ သႀကၤန္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/130.mp3"><span style="color: #ffcc00;">အလုပ္ေပးတရား ( ၂၀၁၄ သႀကၤန္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/090.mp3"><span style="color: #ffcc00;">အားကိုးရတဲ႔ မိတ္ေဆြမ်ား (၁.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/647.mp3"><span style="color: #ffcc00;">အားလံုးရဲ႕ေမတၱာကိုခံယူပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0139-NDML.mp3"><span style="color: #ffcc00;">အားေပးစကား (၁၇-၂-၂၀၀၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/611.mp3"><span style="color: #ffcc00;">အာကေခၤယ်သုတ္ အႏွစ္ခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/600.mp3"><span style="color: #ffcc00;">အာဃတနကိုေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/240-ndml.mp3"><span style="color: #ffcc00;">အာဒိတၱသုတ္ကိုေလ႔လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/086.mp3"><span style="color: #ffcc00;">အာမခံသူမရွိတဲ႔တရားမ်ား (၂၂.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/366.mp3"><span style="color: #ffcc00;">အာယုဒါနအလွဴအႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/025.mp3"><span style="color: #ffcc00;">အိပ္ေမာက်သူႏွင္႔ ႏိုးၾကားသူ (၉.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/317-ndml.mp3"><span style="color: #ffcc00;">အိမ္တက္မဂၤလာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/109.ndml%202.mp3"><span style="color: #ffcc00;">အိမ္တက္အလွဴမဂၤလာအႏုေမာဒနာ (ဦးစံသာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/151.mp3"><span style="color: #ffcc00;">ေအာင္ျမင္ႀကီးပြား အေၾကာင္းမ်ား (၁.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/182.mp3"><span style="color: #ffcc00;">ေအာင္ႏိုင္ျခင္းႏွစ္မ်ိဳး (၂၄.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/277-ndml.mp3"><span style="color: #ffcc00;">ဣၿႏၵိယဘာ၀နာျမတ္ေဒသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/692.mp3"><span style="color: #ffcc00;">ဣေျႏၵေစာင္းႀကိဳးညွိႏိုင္းမွ တရားသိမည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-1%29/008.ndml%202.mp3"><span style="color: #ffcc00;">ဤဘဝ၏အျခားမဲ့ ၌</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2015/2015.4.16.PM.mp3"><span style="color: #ffcc00;">ဥပုဒ္သည္တို႔ ၏ စကားဝိုင္း တရာ ေဒသနရေတာ္ (၁၆.၀၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/004.mp3"><span style="color: #ffcc00;">ဥစၥာဓန ရွာေဖြၾက (၉.၄.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/244-ndml.mp3"><span style="color: #ffcc00;">ဥပါဒါန ပစၥယာ ဘေ၀ါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/218-ndml.mp3"><span style="color: #ffcc00;">ဥပုဒ္ေစာင္႔ျခင္းအဓိပၸါယ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/206.mp3"><span style="color: #ffcc00;">ဥပုသ္သည္တို႔၏ စကားဝိုင္း (၁၆.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.12/314-ndml.mp3"><span style="color: #ffcc00;">ဦးကိတၱိသာရအားေျပာၾကားအပ္ေသာ ၾသ၀ါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/180.ndml%202.mp3"><span style="color: #ffcc00;">ဥေပကၡာတရားကို ေလ့လာသံုးသပ္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/817.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/768.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒ (ဓမၼသဟာယစင္တာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/769.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒ (ဓမၼသဟာယစင္တာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/781.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒ (မူဆယ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/813.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒ (အျပည္ျပည္ဆုိင္ရာအဘိဓမၼတကၠသုိလ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0035-NDML.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒႏွင္႔အေမးအေျဖ (၁၀-၉-၂၀၀၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/53.mp3"><span style="color: #ffcc00;">ၾသကတရနအႏွစ္ခ်ဳပ္တရားေဒသနာေတာ္ (၁၂.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0072-NDML.mp3"><span style="color: #ffcc00;">ၾသကာသရွင္းတမ္း (၁၇-၂-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/120.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတ္ အႏွစ္ခ်ဳပ္ (၁၂.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0049-NDML.mp3"><span style="color: #ffcc00;">ၾသဃတရဏီ (၄-၅-၂၀၀၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0074-NDML.mp3"><span style="color: #ffcc00;">ၾသဃေလးျဖာသံသရာ (၅-၃-၂၀၀၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/146.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (ဓမၼသဟာယသာသနစင္တာ) (၃၀.၉.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/702.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (ၿမိတ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/706.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (ဘုရားငါးဆူစာသင္တိုက္-ၿမိတ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/167.ndml%202.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (အျပည္ျပည္ဆိုင္ရာ ေထရဝါဒ ဗုဒၶသာသနာျပဳတကၠသိုလ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/695.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (အလက-၁-ဒဂံု)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/711.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (အေမထြား)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/704.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (ဦးအင္ပို)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/165.ndml%202.mp3"><span style="color: #ffcc00;">ၾသဝါဒ (ေက်းဇူးဆပ္အမွတ္တရအလွဴမဂၤလာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Singapore/Day%202%20P2.mp3"><span style="color: #ffcc00;">ၾသဝါဒ တရားေတာ္ (ဒုတိယပိုင္း) (၁၃.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Singapore/Day%202%20P1.mp3"><span style="color: #ffcc00;">ၾသဝါဒ တရားေတာ္ (ပထမပိုင္း) (၁၃.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/123.ndml%202.mp3"><span style="color: #ffcc00;">ၾသဝါဒ အႏုေမာဒနာ (ထားဝယ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/110.ndml%202.mp3"><span style="color: #ffcc00;">ၾသဝါဒ အႏုေမာဒနာ (သန္လ်င္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/588.mp3"><span style="color: #ffcc00;">ၾသဝါဒကထာအႏုေမာဒနာ (ေတာင္ႀကီး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/195.mp3"><span style="color: #ffcc00;">ၾသဝါဒစကား (အမွတ္ ၉၉ ေျချမန္တပ္မဌာနခ်ဳပ္) (၈.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-5%29/113.ndml%202.mp3"><span style="color: #ffcc00;">ၾသဝါဒအႏုေမာဒနာ (ျမန္ေအာင္သီလရွင္စာသင္တိုက္)</span></a><br />
<a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/051-Dr-Nandamalabhivamsa-MP3-1AwKarThaShinTan.mp3"><span style="color: #ffcc00;">ၾသကာသ ရွင္းတမ္း တရားေတဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/054-Dr-Nandamalabhivamsa-MP3-1-AwGaThaRaNi.mp3"><span style="color: #ffcc00;">ၾသဂသရဏီ တရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.10/121-ndml.mp3"><span style="color: #ffcc00;">ၾသဃတရဏီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/052-Dr-Nandamalabhivamsa-MP3-1-AwGaLayPharThanThaYar.mp3"><span style="color: #ffcc00;">ၾသဃလးျဖာ သံသရာ တရားတရားေဒသနာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.09/107-ndml.mp3"><span style="color: #ffcc00;">ၾသဝါဒႏွင္႕အေမးအေျဖ</span></a></p>
<h5><span style="color: #00ffff;">&#8220;အႏုေမာဒနာ&#8221; တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/30.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/disc1/ndml.11/207-ndml.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/166.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/171.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/726.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/730.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/738.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/746.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/863.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/888.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD-171/0155-NDML.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရား (၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-4%29/083.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ( ေရႊျမိဳင္သီလရွင္ေက်ာင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/154.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (၂.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/097.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (၇၄ႏွစ္ျပည္႔ ပါခ်ဳပ္ဆရာေတာ္) (၁၅.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (၇၅ႏွစ္ျပည္႔ပါခ်ဳပ္ဆရာေတာ္ေမြးေန႔) (၄.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/203.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (၇၅ႏွစ္ျပည္႔ပါခ်ဳပ္ဆရာေတာ္ေမြးေန႔) (၅.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/856.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (SSC)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/169.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ကံထပ္၊ ရဟန္းခံ၊ အလွဴေတာ္မဂၤလာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/186.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (စံတဝတ္ေက်းရြာ) (၁၉.၁၀၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/729.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (စစ္ကိုင္းတိုင္းဝန္ႀကီးခ်ဳပ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/150.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (စစ္ကိုင္းပညာေရးတကၠသိုလ္) (၇.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-6%29/118.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (စုေပါင္းရဟန္းခံရွင္ျပဳ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/595.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဆံုဆည္းရာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/902.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဆန္းကုမၸဏီ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/892.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဆန္းပြဲရံု)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/171.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဆရာႀကီး ေဒၚကဥၥာနာ) (၁၆.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/861.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (တပည့္မ်ား၀ါဆုိသကၤန္းကပ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/172.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (တယ္လီေနာ မိုဘိုင္း) (၂၀.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/580.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဒုဗိုလ္မွဴးႀကီးတင္မ်ိဳးျမင္႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/210.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဓမၼ သဟာယစင္တာေလးႏွစ္ျပည္႔) (၁၉.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/852.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဓမၼေစတီေက်ာင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/175.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (နည္းပညာတကၠသိုလ္ ရတနာပံု) (၂၉.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/125.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (နည္းပညာတကၠသိုလ္ ရတနာပံု) (၂၉.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/169.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ပင္လံုေဆးရံု ေျမာက္ဒဂံု) (၆.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/885.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ပန္းလိႈင္ေဆးရံု)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/934.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဖိုးစိန္လမ္းေဟာ္တယ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/172.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဗိုလ္မွဴးႀကီးျမင့္ၾကည္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/168.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဗိုလ္မွဴးႀကီးျမင္႔ၾကည္) (၄.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/168.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မံုရြာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/747.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မက္စ္ျမန္မာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/886.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မက္စ္ျမန္မာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/904.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မက္စ္ျမန္မာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/199.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မင္းသီဟမုန္႔မ်ိဳးစံု) (၂၈.၂.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/841.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မင္ဓမၼလမ္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/698.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မဏိရတနာသီလရွင္စာသင္တိုက္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/185.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မတၱရာၿမိဳ႕ကုသိုလ္ရွင္အေပါင္း) (၂.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/204.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မဟာသႏၱာေအးေက်ာင္းတိုက္) (၂၈.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/147.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မႏၱေလးတကၠသိုလ္) (၁၂.၁၀.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/100.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (မႏၱေလးေရႊဆိုင္တန္း) (၁၈.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/854.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ျပင္ဦးလြင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/855.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ျပင္ဦးလြင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/187.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ျပည္သူ႔ေဆာက္လုပ္ေရး ေအာက္ျမန္မာျပည္) (၂၂.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/164.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ျမတ္ပါရမီ မိသားစု) (၂၀.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/179.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရတနာညီအစ္ကိုမ်ားအဖြဲ႔) (၂၁.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/153.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရတနာပန္းကုန္းေက်ာင္းတိုက္၊ ေရႊျပည္သာ) (၂၄.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/173.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရန္ကင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/881.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရန္ကုန္တကၠသုိလ္ ဓာတုေဗဒ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/693.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရန္ကုန္တိုင္းဆက္သြယ္ေရး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/206.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရဲမွဴး ရဲသူရရန္ရွင္း) (၂.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/182.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရဲမွဴးႀကီးေအာင္ႏိုင္သူ) (၁၇.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/177.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရဲသူရ ရန္ရွင္း) (၃.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/158.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ရွင္ေဇာတိကလကၤာရ) (၂၄.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/884.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (လိႈင္သာယာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/833.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (လႈိင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/198.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဝင္းကိုယ္ပိုင္အထက္တန္းေက်ာင္း) (၃၀.၁.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/909.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဝင္းပပေရႊလုပ္ငန္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/207.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဝန္ႀကီးခ်ဳပ္ ဦးသာေအး (၉.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/812.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (သြားေဆးတကၠသုိလ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/883.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဟိုတယ္ရန္ကုန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/163.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (အပၸမာေတာစခန္းရိပ္သာ) (၁၉.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/196.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (အမွတ္ ၃၃ ေျချမန္တပ္မဌာနခ်ဳပ္) (၂၁.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/197.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (အေနာက္ေတာင္တိုင္းစစ္ဌာနခ်ဳပ္) (၂၅.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/851.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (အေမထြား)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/173.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (အေမမ်ားအဖြဲ႔ မႏၱေလး) (၂၁.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/866.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (အႏၱဂုဏပူဇာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/170.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးခ်စ္ေထြး+ေဒၚၾကင္စိန္) (၁၃.၆.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/838.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးခ်စ္ေမႊး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/156.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးစန္းလြင္) (၁၈.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/160.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးစိုး) (၃၀.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/579.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးတင္ျမင္႔ေအာင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/596.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးတင္ေမာင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/190.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးတင္ေအာင္) (၂၆.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/162.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးတင္ေအာင္မြန္) (၁၂.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/665.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးထင္ေက်ာ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/161.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးထြန္းသိန္း) (၃၁.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/933.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးျမင္႔ဦး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/166.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးျမင္႔ေရႊ) (၂၇.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/815.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးျမေအာင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/906.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးရဲျမင္႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/148.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးလူျမင္႔ဦး) (၁၁.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/183.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးလွေအာင္) (၂၁.၉.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/180.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးလွေအာင္) (၂၁.၉၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/178.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးဝင္းလြင္ဦး) (၁၆.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/151.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးဝင္းေမာင္) (၉.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/189.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးသက္ႏိုင္) (၂၅.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/903.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးသန္႔ဇင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/858.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးသာေအး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/157.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးသာႏု+ေဒၚသိန္းထိုက္) (၂၀.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/192.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးသိုက္ညြန္႔) (၃.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/208.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးအံ႔ေမာင္+ေဒၚခ်ယ္ရီ) (၁၁.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/577.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေကာင္း+ေဒၚၾကင္ေမႊး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/174.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေက်ာ္သူေအာင္) (၂၆.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/149.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေဇာ္လင္းထက္) (၂၄.၁၁.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/201.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေနေအာင္) (၃.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/137.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေမာင္ေမာင္) (၁.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/184.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေမာင္ေမာင္+ေဒၚနန္းစံဖုန္း) (၁.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/581.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေမာင္ေမာင္တာ+ေဒၚျမင္႔ျမင္႔ေဝ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/666.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေသာင္းစုၿငိမ္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/181.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေသာင္းလြင္+ေဒၚႏုႏုရီ) (၃၁.၈.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-8%29/174.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေအာင္ျမင့္ + ေဒၚေအးေအးျမင့္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/920.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေအာင္ဝင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/165.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးေအာင္သူမ်ိဳး) (၂၂.၄.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/194.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးၾကည္ျမင္႔) (၆.၁၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/862.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ဦးၾကည္သာဦး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/205.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေညာင္ပင္ရြာ) (၃၀.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/193.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဌးျမင္႔ေမာ္ေက်ာက္မ်က္) (၁၃.၁၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/808.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚ၀င္းလဲ႕ေအး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/915.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚကုမၼာရီ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/867.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚတင္တင္ဦး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/209.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚတင္မုံ) (၁၂.၄.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/152.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚထူးထူး) (၂၃.၁.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/786.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚနန္းခင္သိန္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/578.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚနန္းစံခမ္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/167.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚနန္းညြန္႔ေဝ) (၃၀.၅.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/839.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚယဥ္ယဥ္လွေမြးေန႕)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/731.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚလွျမင္႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/188.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚလွလွျမင္႔) (၂၃.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/680.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚသန္းစိန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/191.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚေမၾကည္) (၂၈.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/882.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒၚၾကည္ၾကည္စမ္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/819.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒါက္တာအဖြဲ႕)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/145.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေဒါက္တာဦးထြန္းလင္း) (၂၁.၇.၂၀၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/159.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေနသူရိန္ ေျမပဲဆီ) (၂၉.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/176.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေမဖူးသက္) (၃၀.၇.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/DVD180/dr.ndml%20%282-7%29/153.ndml%202.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေရႊအိုးေဝ ေက်ာင္းေရစက္ခ်)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/155.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ေအာင္ဘာဂီစာသင္တိုက္) (၁.၂.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-5/200.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ (ႏိုင္ျမန္မာကားေဘာ္ဒီ) (၂.၃.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/853.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ေရစက္ခ်တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20tayar/13.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ ေရစက္ခ်အလွဴေတာ္ တရား(၂၀.၃.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&#038;4/691.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ(ရတနာမာရ္ေအာင္ေတာရသာသနာ႔ရိပ္သာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/208.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/209.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/210.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/211.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/212.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/213.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/214.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/215.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/216.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/217.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/218.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/219.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/220.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/221.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားမ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-6/141.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာႏွင္႔ ဝိပႆနာတရား (၂၀.၁၀.၂၀၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-1/352.mp3"><span style="color: #ffcc00;">အႏုေမာနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/016_09.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၉.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/015_08.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၈.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/014_07.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၇.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/013_06.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၆.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/012_05.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၅.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/011_04.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၄.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/010_03.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၃.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/009_01.5.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၁.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/008_30.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၃၀.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/007_28.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၂၈.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/006_27.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၂၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/005_26.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၂၆.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/004_25.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၂၅.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/003_24.4.2018.mp3.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၂၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/002_23.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ဗာဟိရနိဒါနကထာ ပို႔ခ်ခ်က္ (၂၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/DrNandamalabhivamsa/2018-DhammaClass-Sarwar/001_22.4.2018.mp3"><span style="color: #ffcc00;">ပါရာဇိကက႑ အ႒ကထာ ပို႔ခ်ခ်က္ (၂၂.၄.၂၀၁၈)</span></a></p>
<h5><span style="color: #339966;">ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/opening-speak_6.9.2017.mp3"><span style="color: #ffcc00;">၁။ အဖြင့္ၾသ၀ါဒ (၆.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/001_6.9.2017.mp3"><span style="color: #ffcc00;">၂။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၆.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/002_6.9.2017.mp3"><span style="color: #ffcc00;">၃။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၆.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/002_Part1_7.9.2017.mp3"><span style="color: #ffcc00;">၄။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၇.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/002_Part2_7.9.2017.mp3"><span style="color: #ffcc00;">၅။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၇.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/003_Part1_8.9.2017.mp3"><span style="color: #ffcc00;">၆။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၈.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/003_Part2_8.9.2017.mp3"><span style="color: #ffcc00;">၇။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၈.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/004_Part1_9.9.2017.mp3"><span style="color: #ffcc00;">၈။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၉.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/004_Part2_9.9.2017.mp3"><span style="color: #ffcc00;">၉။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၉.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/005_Part1_10.9.2017.mp3"><span style="color: #ffcc00;">၁၀။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၀.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/005_Part2_10.9.2017.mp3"><span style="color: #ffcc00;">၁၁။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၀.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/006_Part1_11.9.2017.mp3"><span style="color: #ffcc00;">၁၂။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၁.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/006_Part2_11.9.2017.mp3"><span style="color: #ffcc00;">၁၃။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၁.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/007_Part1_12.9.2017.mp3"><span style="color: #ffcc00;">၁၄။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၂.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/007_Part2_12.9.2017.mp3"><span style="color: #ffcc00;">၁၅။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၂.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/008_Part1_13.9.2017.mp3"><span style="color: #ffcc00;">၁၆။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၃.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/008_Part2_13.9.2017.mp3"><span style="color: #ffcc00;">၁၇။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၃.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/009_Part1_14.9.2017.mp3"><span style="color: #ffcc00;">၁၈။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၄.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/009_Part2_14.9.2017.mp3"><span style="color: #ffcc00;">၁၉။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၄.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/010_Part1_15.9.2017.mp3"><span style="color: #ffcc00;">၂၀။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၅.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/010_Part2_15.9.2017.mp3"><span style="color: #ffcc00;">၂၁။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၅.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/011_Part1_16.9.2017.mp3"><span style="color: #ffcc00;">၂၂။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၆.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/011_Part2_16.9.2017.mp3"><span style="color: #ffcc00;">၂၃။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၆.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/012_Part1_17.9.2017.mp3"><span style="color: #ffcc00;">၂၄။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၇.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/012_Part2_17.9.2017.mp3"><span style="color: #ffcc00;">၂၅။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၇.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/013_Part1_18.9.2017.mp3"><span style="color: #ffcc00;">၂၆။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၈.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/013_Part2_18.9.2017.mp3"><span style="color: #ffcc00;">၂၇။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၈.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/014_Part1_19.9.2017.mp3"><span style="color: #ffcc00;">၂၈။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၉.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/014_Part2_19.9.2017.mp3"><span style="color: #ffcc00;">၂၉။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၁၉.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/015_Part1_20.9.2017.mp3"><span style="color: #ffcc00;">၃၀။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၀.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/015_Part2_20.9.2017.mp3"><span style="color: #ffcc00;">၃၁။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၀.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/016_Part1_21.9.2017.mp3"><span style="color: #ffcc00;">၃၂။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၁.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/016_Part2_21.9.2017.mp3"><span style="color: #ffcc00;">၃၃။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၁.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/017_Part1_22.9.2017.mp3"><span style="color: #ffcc00;">၃၄။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၂.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/017_Part2_22.9.2017.mp3"><span style="color: #ffcc00;">၃၅။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၂.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/018_Part1_23.9.2017.mp3"><span style="color: #ffcc00;">၃၆။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၃.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/018_Part2_23.9.2017.mp3"><span style="color: #ffcc00;">၃၇။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၃.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/019_Part1_24.9.2017.mp3"><span style="color: #ffcc00;">၃၈။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၄.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/019_Part2_24.9.2017.mp3"><span style="color: #ffcc00;">၃၉။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၄.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/020_Part1_25.9.2017.mp3"><span style="color: #ffcc00;">၄၀။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၅.၉.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Sep-Dhamma-Class/020_Part2_25.9.2017.mp3"><span style="color: #ffcc00;">၄၁။ ဝိသုဒၶိမဂ္ ပညာဘူမိနိေဒၵသ ပဋိစၥသမုပၸါဒကထာ အပိုင္း (၂) ပို႔ခ်ခ်က္ &#8211; (၂၅.၉.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<h5><span style="color: #339966;">၂၀၁၇ခုႏွစ္ အဘိဓမၼာအႏွစ္ခ်ဳပ္ အပိုင္း(၃) ပို႔ခ်ခ်က္တရားေတာ္မ်ား </span></h5>
<h6><a href="https://media.thitsarparamisociety.com/ebooks/DrNandamalabhivamsa/abidhamma-3.pdf" target="_blank"><span style="color: #33cccc;">&#8220;အဘိဓမၼာအႏွစ္ခ်ဳပ္ အပိုင္း(၃) သင္တန္းစာအုပ္&#8221; PDF </span></a></h6>
<h6><a href="https://media.thitsarparamisociety.com/ebooks/DrNandamalabhivamsa/pahtan-24-pyitsee.pdf" target="_blank"><span style="color: #33cccc;">&#8220;ပ႒ာန္း(၂၄)ပစၥည္း (ပစၥယုပၸန္ ပစၥယသတၱိ)&#8221; PDF </span></a></h6>
<h6><a href="https://media.thitsarparamisociety.com/ebooks/DrNandamalabhivamsa/pahtarna-parli.pdf" target="_blank"><span style="color: #33cccc;">&#8220;ပ႒ာနပါဠိ&#8221; PDF </span></a></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/001_7.8.2017.mp3"><span style="color: #ffcc00;">၁။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၇.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/002_8.8.2017.mp3"><span style="color: #ffcc00;">၂။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၈.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/003_Part1_9.8.2017.mp3"><span style="color: #ffcc00;">၃။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၉.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/003_Part2_9.8.2017.mp3"><span style="color: #ffcc00;">၄။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၉.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/004_Part1_10.8.2017.mp3"><span style="color: #ffcc00;">၅။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၀.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/004_Part2_10.8.2017.mp3"><span style="color: #ffcc00;">၆။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၀.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/005_Part1_11.8.2017.mp3"><span style="color: #ffcc00;">၇။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၁.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/005_Part2_11.8.2017.mp3"><span style="color: #ffcc00;">၈။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၁.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/006_Part1_12.8.2017.mp3"><span style="color: #ffcc00;">၉။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၂.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/006_Part2_12.8.2017.mp3"><span style="color: #ffcc00;">၁၀။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၂.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/007_Part1_13.8.2017.mp3"><span style="color: #ffcc00;">၁၁။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၃.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/007_Part2_13.8.2017.mp3"><span style="color: #ffcc00;">၁၂။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၃.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/008_Part1_14.8.2017.mp3"><span style="color: #ffcc00;">၁၃။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၄.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/008_Part2_14.8.2017.mp3"><span style="color: #ffcc00;">၁၄။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၄.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/009_Part1_15.8.2017.mp3"><span style="color: #ffcc00;">၁၅။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၅.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/009_Part2_15.8.2017.mp3"><span style="color: #ffcc00;">၁၆။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၅.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/010_Part1_16.8.2017.mp3"><span style="color: #ffcc00;">၁၇။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၆.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/010_Part2_16.8.2017.mp3"><span style="color: #ffcc00;">၁၈။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၆.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/011_Part1_17.8.2017.mp3"><span style="color: #ffcc00;">၁၉။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၇.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/011_Part2_17.8.2017.mp3"><span style="color: #ffcc00;">၂၀။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၇.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/012_Part1_18.8.2017.mp3"><span style="color: #ffcc00;">၂၁။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၈.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/012_Part2_18.8.2017.mp3"><span style="color: #ffcc00;">၂၂။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၈.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/013_19.8.2017.mp3"><span style="color: #ffcc00;">၂၃။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၁၉.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/014_Part1_20.8.2017.mp3"><span style="color: #ffcc00;">၂၄။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၀.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/014_Part2_20.8.2017.mp3"><span style="color: #ffcc00;">၂၅။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၀.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/015_Part1_21.8.2017.mp3"><span style="color: #ffcc00;">၂၆။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၁.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/015_part2_21.8.2017.mp3"><span style="color: #ffcc00;">၂၇။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၁.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/016_Part1_22.8.2017.mp3"><span style="color: #ffcc00;">၂၈။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၂.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/016_Part2_22.8.2017.mp3"><span style="color: #ffcc00;">၂၉။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၂.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/017_Part1_23.8.2017.mp3"><span style="color: #ffcc00;">၃၀။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၃.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/017_Part2_23.8.2017.mp3"><span style="color: #ffcc00;">၃၁။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၃.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/018_Part1_24.8.2017.mp3"><span style="color: #ffcc00;">၃၂။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၄.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/018_Part2_24.8.2017.mp3"><span style="color: #ffcc00;">၃၃။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၄.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/019_Part1_25.8.2017.mp3"><span style="color: #ffcc00;">၃၄။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၅.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/019_Part2_25.8.2017.mp3"><span style="color: #ffcc00;">၃၅။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၅.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/020_Part1_26.8.2017.mp3"><span style="color: #ffcc00;">၃၆။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၆.၈.၂၀၁၇) &#8211; ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2017-Aug-Dhamma-Class/020_Part2_26.8.2017.mp3"><span style="color: #ffcc00;">၃၇။ အဘိဓမၼာအႏွစ္ခ်ဳပ္အပိုင္း (၃)ပို႔ခ်ခ်က္ &#8211; (၂၆.၈.၂၀၁၇) &#8211; ဒုတိယပိုင္း</span></a></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/001.1.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ သင္တန္းဖြင့္ပြဲ ဆံုးမၾသဝါဒတရား (၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/003.1.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁) (၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/002.1.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၂) (၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/004.2.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၃) (၂.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/005.4.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၅။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၄) (၄.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/006.4.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၆။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၅) (၄.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/007.5.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၇။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၆) (၅.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/008.5.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၈။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၇) (၅.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/009.6.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၉။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၈) (၆.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/010.6.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၉) (၆.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/011.7.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၀) (၇.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/012.7.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၁) (၇.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/013.8.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၂) (၈.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/014.8.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၃) (၈.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/015.9.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၄) (၉.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/016.9.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၅) (၉.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/017.10.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၆) (၁၀.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/018.10.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၇) (၁၀.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/019.11.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၉။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၈) (၁၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/020.11.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၀။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၁၉) (၁၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/021.12.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၂၀) (၁၂.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/022.12.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၂။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၂၁) (၁၂.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/023.13.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၃။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၂၂) (၁၃.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/024.13.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၄။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၂၃) (၁၃.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/01.Abhidhamma%20mp3/025.14.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၅။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား အပိုင္း (၂၄) (၁၄.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/1.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၁။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၁) (၁.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/2.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၂။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၂) (၂.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/3.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၃။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၃) (၃.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/4.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၄။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၄) (၄.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/5.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၅။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၅) (၅.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/6.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၆။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၆) (၆.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/7.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၇။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၇) (၇.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/8.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၈။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၈) (၈.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/9.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၉။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၉) (၉.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/03.Dhammapada%20mp3/10.7.2014-64.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၁၀) (၁၀.၇.၂၀၁၄)</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/Thouttanta/11.7.2014.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၁။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၁၀) (၁၁.၇.၂၀၁၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/Thouttanta/12.7.2014.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၂။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၁၀) (၁၂.၇.၂၀၁၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/Thouttanta/13.7.2014.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၃။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၁၀) (၁၃.၇.၂၀၁၄)</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/Thouttanta/14.7.2014.mp3" target="_blank"><span style="color: #ffcc00;"><span style="color: #ffcc00;">၁၄။ သုတၱန္တ အႏွစ္ခ်ဳပ္ သင္တန္း အပိုင္း (၁၀) (၁၄.၇.၂၀၁၄)</span></span></a></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/01.1.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ သုတၱန္တ အပိုင္း(၂)ဘာသာသရပ္ သင္တန္းဖြင့္ပြဲ ၾသဝါဒ အမွာစကား</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/02.1.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;"> ၂။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၁) (၁.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/03.1.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၃။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်က္ခ်က္ အပို္င္း(၂) (၁.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/04.2.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၄။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၃) (၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/05.2.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၅။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၄) (၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/06.3.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၆။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်က္ အပိုင္း(၅) (၃.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/07.3.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၇။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်က္ခ်က္ အပိုင္း (၆) (၃.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/08.4.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၈။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်က္ခ်က္ အပိုင္း (၇) (၄.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/09.4.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၉။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်က္ခ်က္ အပိုင္း(၈) (၄.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/10.5.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း (၉) (၅.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/11.5.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၁၁။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း (၁၀) (၅.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/12.6.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၁၁) (၆.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/13.6.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်က္ခ်က္ အပိုင္း (၁၂) (၆.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/14.7.9.2014.am.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း (၁၃) (၇.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/15.7.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း (၁၄) (၇.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/16.8.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း (၁၅) (၈.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/09.Sanlekha%20%20Mp3/17.8.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ သုတၱန္တ အပိုင္း(၂) သေလႅခသုတ္ ပို႔ခ်ခ်က္ အပိုင္း (၁၆) (၈.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/18.9.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၁) (၉.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/19.9.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၉။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၂) (၉.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/20.10.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၀။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၃) (၁၀.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/21.10.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၁။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၄) (၁၀.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/22.11.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၂။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၅) (၁၁.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/23.11.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၃။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၆) (၁၁.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/24.12.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၄။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၇) (၁၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/25.12.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၅။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၈) (၁၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/26.13.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၆။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၉) (၁၃.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/11.Sabbhasava%20MP3/27.13.9.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၇။ သုတၱန္တ အပိုင္း(၂) သဗၺာသဝ သံဝရသုတ္ ပို႔ခ်ခ်က္ အပိုင္း(၁၀) (၁၃.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/01.1.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း (၂) သင္တန္း ဖြင့္လွစ္ျခင္း ၾသဝါဒ အမွာစကား (၁.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/02.1.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္း (၁.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/03.2.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္း (၂.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/04.3.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္း (၃.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/05.4.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္း (၄.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/06.5.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္းး (၅.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/07.6.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္း (၆.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/05.Pattan%20%20Mp3/08.7.8.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ အပိုင္း(၂) ပ႒ာန္းက်မ္း (၇.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/001.21.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ ဓမၼသင္တန္း ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္းဖြင့္လွစ္ျခင္း ၾသဝါဒတရား (၂၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/002.21.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၁) (၂၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/003.21.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၂) (၂၁.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/004.22.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၃) (၂၂.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/005.22.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၅။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၄) (၂၂.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/006.23.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၆။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၅) (၂၃.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/007.23.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၇။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၆) (၂၃.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/008.25.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၈။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၇) (၂၅.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/009.25.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၉။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၈) (၂၅.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/010.26.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၉) (၂၆.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/011.26.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၁၀) (၂၆.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/012.27.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၁၁) (၂၇.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/02.Visudhi%20%281%29%20%20mp3/013.27.5.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၁-၁၂) (၂၇.၅.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/01.22.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂) သင္တန္း စတင္ဖြင့္လွစ္ျခင္း ၾသဝါဒကဌာ (၂၂.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/02.22.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၁) (၂၂.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/03.23.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၂) (၂၃.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/04.24.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၃) (၂၄.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/05.25.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၄) (၂၅.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/06.26.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၉။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၅) (၂၆.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/07.27.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၀။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၆) (၂၇.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/04.Visudhi%20%282%29%20%20Mp3/08.28.7.2014%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၁။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၂-၇) (၂၈.၇.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/22.8.2014%20am.mp3.mp3" target="_blank"><span style="color: #ffcc00;">၂၂။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃) သင္တန္း စတင္ဖြင့္လွစ္ျခင္း ၾသဝါဒကဌာ (၂၂.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/22.8.2014%20am.mp31.mp3" target="_blank"><span style="color: #ffcc00;">၂၃။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၁) (၂၂.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/22.8.2014%20am.mp32.mp3" target="_blank"><span style="color: #ffcc00;">၂၄။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၂) (၂၂.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/23.8.2014%20am.mp3%201.mp3" target="_blank"><span style="color: #ffcc00;">၂၅။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္းအပိုင္း (၃-၃) (၂၃.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/23.8.2014%20am.mp3%202.mp3" target="_blank"><span style="color: #ffcc00;">၂၆။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၄) (၂၃.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/24.8.2014%20am.mp3%201.mp3" target="_blank"><span style="color: #ffcc00;">၂၇။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၅) (၂၄.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/24.8.2014%20am.mp3%202.mp3" target="_blank"><span style="color: #ffcc00;">၂၈။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၆) (၂၄.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/25.8.2014%20am.mp3%201.mp3" target="_blank"><span style="color: #ffcc00;">၂၉။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၇) (၂၅.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/25.8.2014%20am.mp3%202.mp3" target="_blank"><span style="color: #ffcc00;">၃၀။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၈) (၂၅.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/26.8.2014%20am.mp3%201.mp3" target="_blank"><span style="color: #ffcc00;">၃၁။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၉) (၂၆.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/26.8.2014%20am.mp3%202.mp3" target="_blank"><span style="color: #ffcc00;">၃၂။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၁၀) (၂၆.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/27.8.2014%20am.mp3%201.mp3" target="_blank"><span style="color: #ffcc00;">၃၃။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၁၁) (၂၇.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/27.8.2014%20am.mp3%202.mp3" target="_blank"><span style="color: #ffcc00;">၃၄။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၁၂) (၂၇.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/07%20Visudhi%20%283%29%20Mp3/28.8.2014%20am.mp3%201.mp3" target="_blank"><span style="color: #ffcc00;">၃၅။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၃-၁၃) (၂၈.၈.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.22.Mp.3.00.mp3" target="_blank"><span style="color: #ffcc00;">၃၆။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄) သင္တန္း စတင္ဖြင့္လွစ္ျခင္း ၾသဝါဒ တရား(၂၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.22.Mp.3.01.mp3" target="_blank"><span style="color: #ffcc00;">၃၇။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၁) (၂၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.22.Mp.3.02.mp3" target="_blank"><span style="color: #ffcc00;">၃၈။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၂) (၂၂.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.23.Mp.3.01.mp3" target="_blank"><span style="color: #ffcc00;">၃၉။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၃) (၂၃.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.23.Mp.3.02.mp3" target="_blank"><span style="color: #ffcc00;">၄၀။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၄) (၂၃.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.24.Mp.3.01.mp3" target="_blank"><span style="color: #ffcc00;">၄၁။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၅) (၂၄.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.24.Mp.3.02.mp3" target="_blank"><span style="color: #ffcc00;">၄၂။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၆) (၂၄.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.25.Mp.3.01.mp3" target="_blank"><span style="color: #ffcc00;">၄၃။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၇) (၂၅.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.25.Mp.3.02.mp3" target="_blank"><span style="color: #ffcc00;">၄၄။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၈) (၂၅.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.26.Mp.3.01.mp3" target="_blank"><span style="color: #ffcc00;">၄၅။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၉) (၂၆.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.26.Mp.3.02.mp3" target="_blank"><span style="color: #ffcc00;">၄၆။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၁၀) (၂၆.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.27.Mp.3.01.mp3" target="_blank"><span style="color: #ffcc00;">၄၇။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၁၁) (၂၇.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.27.Mp.3.02.mp3" target="_blank"><span style="color: #ffcc00;">၄၈။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၁၂) (၂၇.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2014%20%28new%29%20Dhamma%20Lectures/13.Visudhi%20%284%29%20MP3/2014.9.28.Mp.3..mp3" target="_blank"><span style="color: #ffcc00;">၄၉။ ပါဋိက်မ္းစာ ဝိသုဒၶိမဂ္ သင္တန္း အပိုင္း (၄-၁၃) (၂၈.၉.၂၀၁၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/7.8.2013%20all%20war%20da.mp3" target="_blank"><span style="color: #ffcc00;">၁။ ဓမၼပညာ သင္တန္းေက်ာင္း၏ ရက္ရွည္ သင္တန္း အမွတ္စဥ္(၁) ၾသဝါဒ (၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/7.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁) (၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/7.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၃။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂) (၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/8.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃) (၈.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/8.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၅။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄) (၈.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/9.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၆။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၅) (၉.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/9.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၇။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၆) (၉.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/10.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၈။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၇) (၁၀.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/10.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၉။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၈) (၁၀.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/11.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၉) (၁၁.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%281%29/11.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၁။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၀) (၁၁.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/12.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၁) (၁၂.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/12.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၂) (၁၂.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/13.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၃) (၁၃.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/13.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၄) (၁၃.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/14.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၅) (၁၄.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/14.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၆) (၁၄.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/15.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၇) (၁၅.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/15.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၉။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၈) (၁၅.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/16.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၀။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၁၉) (၁၆.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%282%29/16.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၂၁။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၀) (၁၆.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%283%29/17.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၂။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၁) (၁၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%283%29/17.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၂၃။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၂) (၁၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%283%29/18.8.2013%20Pm.mp3" target="_blank"><span style="color: #ffcc00;">၂၄။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၃) (၁၈.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%283%29/19.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၅။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၄) (၁၉.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%283%29/19.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၂၆။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၅) (၁၉.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%283%29/20.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၇။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၆) (၂၀.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/4.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၂၈။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၇) (၄.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/4.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၂၉။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၈) (၄.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/5.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃၀။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၂၉) (၅.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/5.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၃၁။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၀) (၅.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/6.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃၂။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၁) (၆.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/6.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၃၃။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၂) (၆.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/7.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃၄။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၃) (၇.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/7.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၃၅။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၄) (၇.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/8.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃၆။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၅) (၈.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%284%29/8.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၃၇။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၆) (၈.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/09.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃၈။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၇) (၉.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/09.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၃၉။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၈) (၉.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/10.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄၀။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၃၉) (၁၀.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/10.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၄၁။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၀) (၁၀.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/11.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄၂။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၁) (၁၁.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/11.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၄၃။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၂) (၁၁.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/12.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄၄။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၃) (၁၂.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/12.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၄၅။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၄) (၁၂.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/13.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄၆။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၅) (၁၃.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%285%29/13.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၄၇။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၆) (၁၃.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%286%29/14.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၄၈။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၇) (၁၄.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%286%29/14.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၄၉။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၈) (၁၄.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%286%29/15.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၅၀။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၄၉) (၁၅.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%286%29/15.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၅၁။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၅၀) (၁၅.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%286%29/16.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၅၂။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၅၁) (၁၆.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/W%20S%20D%286%29/16.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၅၃။ ဝိသုဒၶိမဂ္ သင္တန္းတရား (အပိုင္း -၅၂) (၁၆.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/001.mp3" target="_blank"><span style="color: #ffcc00;">၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/002.mp3" target="_blank"><span style="color: #ffcc00;">၂။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၂)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/003.mp3" target="_blank"><span style="color: #ffcc00;">၃။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/004.mp3" target="_blank"><span style="color: #ffcc00;">၄။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၄)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/005.mp3" target="_blank"><span style="color: #ffcc00;">၅။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၅)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/006.mp3" target="_blank"><span style="color: #ffcc00;">၆။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၆)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/007.mp3" target="_blank"><span style="color: #ffcc00;">၇။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၇)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/008.mp3" target="_blank"><span style="color: #ffcc00;">၈။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၈)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/009.mp3" target="_blank"><span style="color: #ffcc00;">၉။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၉)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/1-10.001%20Abhidhamma/010.mp3"><span style="color: #ffcc00;">၁၀။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၀)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/24.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၁။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၁) (၂၄.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/24.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၂) (၂၄.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/25.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၃) (၂၅.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/25.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၄) (၂၅.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/26.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၅) (၂၆.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/26.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၆) (၂၆.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/27.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၇) (၂၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/27.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၈) (၂၇.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/28.8.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၉။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၁၉) (၂၈.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/2-10.001%20Abhidhamma/28.8.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၂၀။ အဘိဓမၼာ အႏွစ္ခ်ဳပ္ သင္တန္းတရား (အပိုင္း &#8211; ၂၀) (၂၈.၈.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/21.9.2013%20aam.mp3" target="_blank"><span style="color: #ffcc00;">၁။ သင္တန္းဖြင့္ပြဲ ၾသဝါဒ (၂၁.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/21.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁) (၂၁.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/21.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၂။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၂) (၂၁.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/22.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၃။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၃) (၂၂.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/22.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၄။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၄) (၂၂.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/23.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၅။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၅) (၂၃.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/23.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၆။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၆) (၂၃.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/24.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၇။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၇) (၂၄.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/24.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၈။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၈) (၂၄.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/25.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၉။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၉) (၂၅.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/3-10.001%20mahasatipattanasutta/25.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၀။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၀) (၂၅.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/26.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၁။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၁) (၂၆.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/26.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၂။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၂) (၂၆.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/27.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၃။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၃) (၂၇.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/27.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၄။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၄) (၂၇.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/28.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၅။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၅) (၂၈.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/28.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၆။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၆) (၂၈.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/29.9.2013%20am.mp3" target="_blank"><span style="color: #ffcc00;">၁၇။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၇) (၂၉.၉.၂၀၁၃)</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/2013%20%28new%29%20Dhamma%20Lectures/4-10.001%20mahasatipattanasutta/29.9.2013%20pm.mp3" target="_blank"><span style="color: #ffcc00;">၁၈။ မဟာသတိပဌာန သုတၱန္ အႏွစ္ခ်ဳပ္ (အပိုင္း &#8211; ၁၈) (၂၉.၉.၂၀၁၃)</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/843.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/844.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/845.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/846.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/847.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/848.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/849.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/DrNandamalabhivamsa/Part-3&amp;4/850.mp3"><span style="color: #ffcc00;">၀ိဘင္က်မ္းသင္တန္း (အပိုင္း-၈)</span></a></p>"""

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