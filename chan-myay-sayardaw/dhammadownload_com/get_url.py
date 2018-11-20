from bs4 import BeautifulSoup as bs4

text = """
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/01-ChanMyay-Ki-Lay-Thar-Pal-Naing-Hma-Cham-Thar-Ya.mp3">
၁။ ကိေလသာပယ္ႏိုင္မွ ခ်မ္းသာရ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/02-ChanMyay-Pav-Vi-Za-Min-Ga-Lar-Thar-Tha-Nar-Pyu-Ku-Tho.mp3">
၂။ ပဗၺဇၨမဂၤလာသာသနာျပဳ ကုသိုလ္ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/03-ChanMyay-Shin-Pyu-A-HLu--Damma.mp3">
၃။ ရွင္ျပဳအလွဴ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/04-ChanMyay-Shu-Tee-Thi-Ma-Nyi-Sin-Ye-Nyein.mp3">
၄။ ရႈ၊ တည္၊ သိ၊ မၿငိ ဆင္းရဲၿငိမ္း တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/05-ChanMyay-Tha-Ma-Hta-Bar-Wa-Nar--&amp;-Vi-passana-bar.mp3">
၅။ သမထ ဘာဝနာႏွင့္ ဝိပႆနာ ဘာဝနာ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/06-ChanMyay-Thar-Tha-Na-A-Mwe-Khan.mp3">
၆။ သာသနာ့ အေမြခံ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/07-ChanMyay-Thar-Tha-Nar-Taw-Tee-Tan-Kyaung.mp3">
၇။ သာသနာေတာ္အရွည္တည္တံ့ေၾကာင္း တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/08-ChanMyay-Tha-Ba-rWa--&amp;--Thar-Min-Nya-Let-Kha-Nar.mp3">
၈။ သဘာဝလကၡဏာႏွင့္ သာမညလကၡဏာ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/09-ChanMyay-Tha-Ti-Pat-Htan--Vipassana.mp3">
၉။ သတိပ႒ာန္ ဝိပႆနာ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D01/10-ChanMyay-Thin-Khar-Ra-&amp;Thin-Kha-Ta.mp3">
၁၀။ သခၤါရႏွင့္ သခၤတ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP3 Disc02</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/01-ChanMyay-A-Phyit-&amp;-A-Pyet(-14-12-1984-SUN).mp3">
၁။ အျဖစ္ႏွင့္ အပ်က္ တရားေတာ္ ၁၂-၁၂-၁၉၈၄</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/02-ChanMyay-BUDDHA-EI-A-Nat-Ta-War-Da.mp3">
၂။ ဗုဒၶ၏ အနတၱဝါဒ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/03-ChanMyay-Pu-Zaw-Htite-Thu-(4-8-2001-SAT).mp3">
၃။ ပူေဇာ္ထိုက္သူ တရားေတာ္ ၄-၈-၂၀၀၁</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/04-ChanMyay-Seik-Yin-Kye-Ka-Chan-Thar-Ya-(14-5-1997-Wednesday).mp3">
၄။ စိတ္ယဥ္ေက်းက ခ်မ္းသာရ တရားေတာ္ ၁၄-၅-၁၉၉၇</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/05-ChanMyay-Shu-Hmat-Hmu-Myai-Hlyin-Ki-La-Thar-Sin.mp3">
၅။ ရႈမွတ္မႈၿမဲလွ်င္ ကိေလသာစင္ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/06-ChanMyay-Swan-A-Kyoe-Twont-Pyan.mp3">
၆။ ဆြမ္းက်ိဳးတုန္႔ ျပန္ ျမတ္ေမြခံ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/07-ChanMyay-Tha-Thi-Pat-Htan-Vipassana.mp3">
၇။ သတိပ႒ာန္ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/08-ChanMyay-That-Tha-Ta,Oke-Se-Da,An-Ta-Rar-Ba-Wa-Deik-Hti.mp3">
၈။ သႆတဒိ႒ိ၊ ဥေစၦဒ ဒိ႒ိ၊ အႏ ၱရာဘဝဒိ႒ိ&nbsp; တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/09-ChanMyay-Theik-Khar-(3)-Par-AND-Khi-Le-Thar-(3)-Par-Pai-That-Pon-(14-11-1998-SAT.mp3">
၉။ သိကၡာသုံးပါးျဖင့္ ကိေလသာသုံးပါး ပယ္သတ္ပုံ တရားေတာ္ ၁၄-၁၁-၁၉၉၈</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D02/10-ChanMyay-Thi-Pai-Saik-Pwar-Ta-YarTaw.mp3">
၁၀။ သိ၊ ပယ္၊ ဆိုက္၊ ပြား တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP3 Disc 03</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/01-ChanMyay-A-Kyaung-&amp;-A-Kyo-.mp3">
၁။ အေၾကာင္းႏွင့္ အက်ိဳး တရားေတာ္
</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/02-ChanMyay-A-Pan-Na-Ka-Pa-Ti-Pa-Dar.mp3">
၂။ အပဏၰကပဋိပဒါ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/03-ChanMyay-AtTa-(-6--)myo.mp3">
၃။ အတၱေျခာက္မ်ိဳး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/04-ChanMyay-At-Ta-Dik-Hti-&amp;--Thet-Kar-Ya-Dik-Hti.mp3">
၄။ အတၱဒိ႒ိႏွင့္ သကၠယဒိ႒ိ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/05-ChanMyay-Beik-Ku-&amp;-Tha-Ma-Na-(11-4-2007-WED).mp3">
၅။ ဘိကၡဳႏွင့္ သမဏ တရားေတာ္ ၁၁-၄-၂၀၀၇</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/06-ChanMyay-Bo-(5)-Par.mp3">
၆။ ဗိုလ္ငါးပါး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/07-ChanMyay-Chan-Thar-(4)-Par.mp3">
၇။ ခ်မ္းသာေလးပါး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/08-ChanMyay-DhammaSetKyar.mp3">
၈။ ဓမၼစႀကၤာ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/09-ChanMyay-Ein-Da-Re-(5)-Par.mp3">
၉။ ဣေျႏၵငါးပါး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D03/10-ChanMyay-Khan-Dar-(5)-Par.mp3">
၁၀။ ခႏၶာငါးပါး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP3 Disc 04</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/01-ChanMyay-Ar-Zee-Wut-Ht-Ma-Ka-Thee-La-(11-8-2005-Thursday).mp3">
၁။ အာဇီဝ႒မကသီလ တရားေတာ္ ၁၁-၈-၂၀၀၅</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/02-ChanMyay-BaYaThok-&amp;-buddha-nee-kya-Chan-Thar-Swar-Ne-Htine-nee.mp3">
၂။ ဘယသုတ္ေဒသနာေတာ္ႏွင့္ ဗုဒၶနည္းက်ခ်မ္းသာစြာေနထိုင္နည္း တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/03-ChanMyay-BUDDHA-of-A-Sone-A-Ma.mp3">
၃။ ျမတ္စြာဘုရား၏ အဆုံးအမ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/04-ChanMyay-MetTar-ta-yar-(30-8-2004).mp3">
၄။ ေမတၱာ တရားေတာ္ ၃၀-၈-၂၀၀၄</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/05-ChanMyay-Seik-Ko-Fyu-Sin-Say-Thee-Nee-(-6-)-Myoe.mp3">
၅။ စိတ္ကိုျဖဴစင္ေစသည္႔&nbsp; နည္းေျခာက္မ်ိဳး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/06-ChanMyay-Se-Taw-Khi-La-(5)-par.mp3">
၆။ ေစေတာခိလငါးပါး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/07-ChanMyay-Ta-Sa-Pin-Sa-Ka-Ka-Ma-Htan.mp3">
၇။ တစပဥၥကမၼ႒ာန္း တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D04/08-ChanMyay-Ta-Yar-Gon-Taw-(6)-par.mp3">
၈။ တရားဂုဏ္ေတာ္ေျခာက္ပါး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">၉။ သမၼဇညေလးပါး တရားေတာ္</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">၁၀။ သရဏဂုံတရားႏွင့္ အေသးစိတ္ရႈပုံ တရားေတာ္</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP3 Disc 05</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/01-ChanMyay-Min-Ga-Lar-(1)-23-11-1988-Wednesday.mp3">
၁။ ခ်မ္းေျမ႔ မဂၤလာ သင္စရာ တရားေတာ္(၁) ၂၃-၁၁-၁၉၉၈</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/02-ChanMyay-Min-Ga-Lar-(2)-23-11-1988-Wednesday.mp3">
၂။ ခ်မ္းေျမ႔ မဂ္လာ သင္စရာ တရားေတာ္(၂) ၂၃-၁၁-၁၉၉၈</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/03-ChanMyay-MITTA-(1).mp3">
၃။ ေမတၱာ တရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/04-ChanMyay-MITTA-(2).mp3">
၄။ ေမတၱာ တရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/05-ChanMyay-Pok-Go(4)Myo-(1)-18-4-1999-Saturday.mp3">
၅။ ပုဂၢဳိလ္ေလးမ်ဳိး တရားေတာ္(၁) ၁၈-၄-၁၉၉၉</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/06-ChanMyay-Pok-Go(4)Myo-(2)-18-4-1999-Saturday.mp3">
၆။ ပုဂၢိဳလ္ေလးမ်ိဳး တရားေတာ္(၂) ၁၈-၄-၁၉၉၉</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/07-ChanMyay-Seik-ko-htein-hmy-chan-thar-ya-(1)-2-10-1999.mp3">
၇။ စိတ္ကိုထိန္းမွ ခ်မ္းသာရ တရားေတာ္(၁) ၂-၁၀-၁၉၉၉</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/08-ChanMyay-Seik-Ko-Htein-Hmy-Chan-Thar-Ya-(2)-2-10-1999.mp3">
၈။ စိတ္ကိုထိန္းမွ ခ်မ္းသာရ တရားေတာ္(၂) ၂-၁၀-၁၉၉၉</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/09-ChanMyay-Ya-Khu-Loke-Ya-Myi-A-Loke-(1).mp3">
၉။ ယခုလုပ္ရမည္႔ အလုပ္ တရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D05/10-ChanMyay-Ya-Khu-Loke-Ya-Myi-A-Loke-(2).mp3">
၁၀။ ယခုလုပ္ရမည္႔ အလုပ္ တရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP3 Disc 06</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/01-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(1).mp3">
၁။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/02-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(2).mp3">
၂။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/03-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(3).mp3">
၃။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/04-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(4).mp3">
၄။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/05-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(5).mp3">
၅။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/06-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(7).mp3">
၆။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D06/07-ChanMyay-Ein-Da-Re-(5)-Par-Ar-Kaung-Kyaung-In-Gar-(9)-Par-(6).mp3">
၇။ ဣေျႏၵငါးပါး အားေကာင္းေၾကာင္း အဂၤါကိုးပါး တရားေတာ္ (၇)</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 07</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/01-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(1).mp3">
၁။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/02-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(2).mp3">
၂။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/03-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(3).mp3">
၃။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/04-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(4).mp3">
၄။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/05-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(5).mp3">
၅။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/06-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(6).mp3">
၆။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/07-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(7).mp3">
၇။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၇)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/08-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(8).mp3">
၈။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၈)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/09-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(9).mp3">
၉။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၉)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D07/10-ChanMyay-BUDDHA-Myat-Swar-0f-Kyi-Pwar-Chan-Thar-Ye-Ta-Yar-(10).mp3">
၁၀။ ဗုဒၶျမတ္စြာ၏ ႀကီးပြါးခ်မ္းသာေရး တရားေတာ္ (၁၀) </a><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP-3 Disc 08</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/01-ChanMyay-A-Koung(4)Myo.mp3">
၁။ အေကာင္းေလးမ်ဳိး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/02-ChanMyay-Are-Koe-Hman-Hmy-Chan-Thar-Ya.mp3">
၂။ အားကိုးမွန္မွခ်မ္းသာရ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/03-ChanMyay-Dhan-Mok-De-Tha-(4)-par.mp3">
၃။ ဓမၼဳေဒၶသေလးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/04-ChanMyay-Mi-Laung-Ein-Hmy-Oke-Sar-Ya.mp3">
၄။ မီးေလာင္အိမ္မွ ဥစၥာရ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/05-ChanMyay-Min-Ga-Lar-Ta-Yar-&amp;-Ta-Yar-Nar-Ya-Kyo.mp3">
၅။ မဂၤလာတရားေတာ္ႏွင့္ တရားနာရျခင္းအက်ဳိးငါးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/06-ChanMyay-Pok-Go-(4)-Myo.mp3">
၆။ ပုဂၢိဳလ္ေလးမ်ဳိးတရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/07-ChanMyay-Sa-Lin-Ga-Dar-Na.mp3">
၇။ ဆ႒ဂၤဒါန တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/08-ChanMyay-That-Pu-Ri-Tha-Dar-Na.mp3">
၈။ သပၸဳရိသဒါန တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/09-ChanMyay-The-Four-Noble-Truths.mp3">
၉။ သစၥာေလးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D08/10-ChanMyay-Thi-La-Ya-Nan-A-Yat-Tine-Pyant.mp3">
၁၀။ သီလရနံ ့ အရပ္တိုင္းျပန္ ့ တရားေတာ္</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 09</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/01-ChanMyay-DAR-NA-TA-YAR.mp3">
၁။ ဒါနတရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/02-ChanMyay-NYAN-(16)-PAR.mp3">
၂။ ဉာဏ္တဆယ့္ေျခာက္ပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/03-ChanMyay-SET-(4)-PAR.mp3">
၃။ စက္ေလးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/04-ChanMyay-THEIKKHAR(3)PAR.mp3">
၄။ သိကၡာသံုးပါးတရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/05-ChanMyay-THETKARYADEIKHTI.mp3">
၅။ သကၠာယဒိ႒ိ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/06-ChanMyay-UPARDAN(4)PAR.mp3">
၆။ ဥပါဒါန္ေလးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/07-ChanMyay-YAKHULOKYAMYIALOK.mp3">
၇။ ယခုလုပ္ရမည့္အလုပ္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/08-ChanMyay-YAWGIAYEEATHWE(5)PAR.mp3">
၈။ ေယာဂီအရည္အေသြးငါးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/09-ChanMyay-YEESUHLUKYAMYATDARNA.mp3">
၉။ ရည္စူးလွဴၾက ျမတ္ဒါန တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D09/10-ChanMyay-ZAN(5)PAR.mp3">
၁၀။ စ်ာန္ငါးပါးတရား တရားေတာ္</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 10</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/01-ChanMyay-A-HLu-Tat-HLyin-Neik-Ban-Win.mp3">
၁။ အလွဴတတ္လွ်င္ နိဗၺာန္၀င္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/02-ChanMyay-Tha-Ti.mp3">
၂။ သတိ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/03-ChanMyay-That-Kar-Ya-Deik-Hti-.mp3">
၃။ သကၠာယဒိ႒ိ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/04-ChanMyay-That-Pu-Ri-Tha-Dar-Na--&amp;--U-Par-Dar-Net-Kan-Dar-.mp3">
၄။ သပၸဳရိသဒါနႏွင့္ ဥပါဒါနကၡႏၶာ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/05-ChanMyay-Theik-Khar-(-3-)-Par--Shin-Pyu-A-Hlu.mp3">
၅။ သိကၡာသံုးပါး ရွင္ျပဳအလွဴ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/06-ChanMyay-Thi-Lat-Ba-Ta-Pa-Rar-Mar-Tha.mp3">
၆။ သီလဗၺတပရာမာသ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/07-ChanMyay-ViPassana-A-Khye-Khan-.mp3">
၇။ ၀ိပႆနာ အေျခခံ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/08-ChanMyay-Vipassana-.mp3">
၈။ ၀ိပႆနာ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/09-ChanMyay-Way-Da-Nar-Nu-pat-tha-nar-.mp3">
၉။ ေ၀ဒနာ နုပႆနာ သတိပ႒ာန္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D10/10-ChanMyay-Wit-Sin-Ye-Hmy-Lut-Myauk-Ye.mp3">
၁၀။ ၀ဋ္ဆင္းရဲမွ လြတ္ေျမာက္ေရး တရားေတာ္ </a><br>
<br>
<br>
MP-3 Disc 11</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/01-ChanMyay-23-KyeinMauk-KaHtein-AHlu.mp3">
၁။ ၂၃-ႀကိမ္ေျမာက္ ကထိန္အလွဴ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/02-ChanMyay-ABiDhamMa-&amp;-ThaTiPatThan.mp3">
၂။ အဘိဓမၼာအေၾကာင္းႏွင့္ သတိပ႒ာန္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/03-ChanMyay-AMYATSONEPUZA.mp3">
၃။ အျမတ္ဆံုးပူဇာ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/04-ChanMyay-DarNa-ThiLa-BarWaNar-tayardaw.mp3">
၄။ ဒါန၊ သီလ၊ ဘာ၀နာ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/05-ChanMyay-Mok-Chy-Pyu-Lok-Ya-Myi-Ku-Tho-(3)-Myoe.mp3">
၅။ မုခ်ျပဳလုပ္ရမည့္ ကုသိုလ္ သံုးမ်ဳိး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/06-ChanMyay-PonNyaKyiRaiYaWatHtu(10)pa.mp3">
၆။ ပုညႀကိယ၀တၴဳဆယ္ပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/07-ChanMyay-ThaTiPatHtanAkyinKhyok.mp3">
၇။ သတိပ႒ာန္အက်ဥ္းခ်ဳပ္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/08-ChanMyay-BwatZin(7)pa.mp3">
၈။ ေဗာဇၥ်င္ ခုႏွစ္ပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/09-ChanMyay-YoneKyiHmuHyiHmaChanThaYa.mp3">
၉။ ယံုၾကည္မႈရွိမွ ခ်မ္းသာရ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D11/10-ChanMyay-Yoke-Nan-Thi-Hlyin-Deik-Hti-Sin.mp3">
၁၀။ ရုပ္ ၊ နာမ္ သိလွ်င္ ဒိ႒ိစင္ တရားေတာ္</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 12</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/01-ChanMyay-ATTA-(6)-MYO-(1)-31-8-1997-sun.mp3">
၁။ အတၱေျခာက္မ်ဳိး တရားေတာ္(၁) ၃၁-၈-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/02-ChanMyay-ATTA-(6)-MYO-TAYA(2)-6-9-1997-SAT.mp3">
၂။ အတၱေျခာက္မ်ဳိး တရားေတာ္(၂) ၆-၉-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/03-ChanMyay-BAYATH0K-(1).mp3">
၃။ ဘယသုတ္ တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/04-ChanMyay-BAYATH0K-(2).mp3">
၄။ ဘယသုတ္ တရားေတာ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/05-ChanMyay-EINDARE-(5)PA-TAYA-(1)-24-5-2000-SUN.mp3">
၅။ ဣေျႏၵငါးပါး တရားေတာ္ (၁) ၂၄-၅-၂၀၀၀</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/06-ChanMyay-EINDARE-(5)PA-TAYA-(2)-24-5-2000-SUN.mp3">
၆။ ဣေျႏၵငါးပါး တရားေတာ္ (၂) ၂၄-၅-၂၀၀၀</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/07-ChanMyay-NATTHOPYAWTHAN-TAYA-(1).mp3">
၇။ နတ္တို ့ ေပ်ာ္သံ တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/08-ChanMyay-NATTHOPYAWTHAN-TAYA-(2).mp3">
၈။ နတ္တို ေပ်ာ္သံ တရားေတာ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/09-ChanMyay-VIPASSANA-&amp;-YAWGIINGA(5)PA-(1)(9-10-2004-SAT).mp3">
၉။ ၀ိပႆနာတရား ႏွင့္ ေယာဂီအဂၤါငါးပါး တရားေတာ္ (၁) ၉-၁၀-၂၀၀၄</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D12/10-ChanMyay-VIPASSANA-&amp;-YAWGIINGA(5)PA--(2)(9-10-2004-SAT).mp3">
၁၀။ ၀ိပႆနာတရား ႏွင့္ ေယာဂီအဂၤါငါးပါး တရားေတာ္ (၂) ၉-၁၀-၂၀၀၄</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 13</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/01-ChanMyay-K0UNGMHU-&amp;-MAK0UNGMHU-27-11-2007-(TUE).mp3">
၁။ ေကာင္းမႈႏွင့္ မေကာင္းမႈ တရားေတာ္ ၂၇-၁၁-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/02-ChanMyay-NyanSin-AKyinChyok-5-10-2007-FRI.mp3">
၂။ ဉာဏ္စဥ္အက်ဥ္းခ်ဳပ္ တရားေတာ္ ၅-၁၀-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/03-ChanMyay-PINNYASHI-&amp;-LUMAIK-28-11-2007-(WED).mp3">
၃။ လူမိုက္ႏွင့္ လူလိမၼာပညာရွိ ျခားနားခ်က္ တရားေတာ္ ၂၈-၁၁-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/04-ChanMyay-SayFawYwayThauk-YawGaPyauk.mp3">
၄။ ေဆးေဖၚ၍ေသာက္ ေရာဂါေပ်ာက္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/05-ChanMyay-SeikAyeKyiLinAKyoMyin-28-4-2007--SAT.mp3">
၅။ စိတ္ေအးၾကည္လင္ အက်ဳိးျမင္ တရားေတာ္ ၂၈-၄-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/06-ChanMyay-ThaThaMiKyinWwat-(5)Pa-(29-8-2007-WED).mp3">
၆။ သားသမီးက်င့္၀တ္ငါးပါး တရားေတာ္ ၂၉-၈-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/07-ChanMyay-UParDan(4)Pa-&amp;-ThetKaYaDeikDi-(9-9-2007-WED.mp3">
၇။ ဥပါဒါန္ေလးပါး ႏွင့္သကၠာယဒိ႒ိ တရားေတာ္ ၉-၉-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/08-ChanMyay-WarReikTaThiLa-&amp;-SarReikTaThiLa-16-7-2007-THUR.mp3">
၈။ ၀ါရိတၱသီလႏွင့္ စာရိတၱသီလ တရားေတာ္ ၁၆-၇-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/09-ChanMyay-WiThokDi-(7)Myo-(19-10-2007-FRI).mp3">
၉။ ၀ိသုဒၶိ ခုနစ္မ်ဳိး တရားေတာ္ ၁၉-၁၀-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D13/10-ChanMyay-YawNiThawMaNaThiKaRa-&amp;-AYawNiThawMaNaThiKaRa-(10-9-2007-MON.mp3">
၁၀။ ေယာနိေသာမနသိကာရ ႏွင့္ အေယာနိေသာ မနသိကာရ တရားေတာ္ ၁၀-၉-၂၀၀၇</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 14</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/01-ChanMyay-SEIK-(1)-27-4-2007-FRI.mp3">
၁။ စိတ္ တရားေတာ္ (၁) ၂၇-၄-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/02-ChanMyay-SEIK-(2)-27-4-2007-FRI.mp3">
၂။ စိတ္ တရားေတာ္ (၂) ၂၇-၄-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/03-ChanMyay-Ta-Yar-Ar-Ht0k-Tar--Yee-Ywai-Chat-Ka-Bar-Lai-(1)-8-12-2007-SAT.mp3">
၃။ တရားအားထုတ္တာ ရည္ရြယ္ခ်က္ကဘာလဲ တရားေတာ္ (၁) ၈-၁၂-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/04-ChanMyay-Ta-Yar-Ar-Htok-Tar-Yee-Ywai-Chat-Ka-Bar-Lai-(2)-9-12-2007-SUN.mp3">
၄။ တရားအားထုတ္တာ ရည္ရြယ္ခ်က္ကဘာလဲ တရားေတာ္ (၂) ၉-၁၂-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/05-ChanMyay-Thu-Taw-Koung-And-Thar-Paung-Thin-Par-(1)-27-9-2007-WED.mp3">
၅။ သူေတာ္ေကာင္းႏွင့္သာေပါင္းပါ တရားေတာ္ (၁) ၂၇-၉-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/06-ChanMyay-Thu-Taw-Koung-And-Thar-Pound-Thin-Par-(2)-27-9-2000-WED.mp3">
၆။ သူေတာ္ေကာင္းႏွင့္သာေပါင္းပါ တရားေတာ္ (၂) ၂၇-၉-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/07-ChanMyay-We-Da-Nar-Nu-Pat-Tha-Nar-Tha-Thi-Pat-Htan-(1).mp3">
၇။ ေ၀ဒနာ ႏုပႆနာတရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/08-ChanMyay-We-Da-Nar-Nu-Pat-Tha-NarTha-Thi-Pat-Htan-(2).mp3">
၈။ ေ၀ဒနာ ႏုပႆနာတရားေတာ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/09-ChanMyay-Wwat-Sin-Yè-Hmy-Lwat-Myauk-Ye-(1).mp3">
၉။ ၀ဋ္ဆင္းရဲမွ လြတ္ေျမာက္ေရး တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D14/10-ChanMyay-Wwat-Sin-Yè-Hmy-Lwat-Myauk-Ye-(2).mp3">
၁၀။ ၀ဋ္ဆင္းရဲမွ လြတ္ေျမာက္ေရး တရားေတာ္ (၂)</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 15</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/01-ChanMyay-A-Bi-dham-mar-a-kyaung-&amp;-pa-war-ra-nar-pwe-a-kyaung-(28-10-2004-thur).mp3">
၁။ အဘိဓမၼာ ေဒသနာႏွင့္ ပ၀ါရဏာပြဲအေၾကာင္း တရားေတာ္ ၂၈-၁၀-၂၀၀၄</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/02-ChanMyay-APanNaKaPaTiPaDar-(1)-(1-12-1988-THUR).mp3">
၂။ အပဏၰက ပဋိပဒါ တရားေတာ္(၁) ၁-၁၂-၁၉၉၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/03-ChanMyay-APanNaKaPaTiPaDar-(2)-(1-12-1988-THUR).mp3">
၃။ အပဏၰက ပဋိပဒါ တရားေတာ္(၂) ၁-၁၂-၁၉၉၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/04-ChanMyay-MAN-(5)PA-(1).mp3">
၄။ မာရ္ငါးပါး တရားေတာ္(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/05-ChanMyay-MAN-(5)PA-(2).mp3">
၅။ မာရ္ငါးပါး တရားေတာ္(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/06-ChanMyay-MAN-(5)PA-(3).mp3">
၆။ မာရ္ငါးပါး တရားေတာ္(၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/07-ChanMyay-POKGALATHOK-DETHANA-(4)-MYO-(1)-DHAMMA-TALK-(12-12-2007-WED-.mp3">
၇။ ပုဂၢလသုတ္ေဒသနာတရားေတာ္ (၁) ၁၂-၁၂-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/08-ChanMyay-POKGALATHOK-DETHANA-(4)-MYO-(2)-DHAMMA-TALK(12-12-2007-WED).mp3">
၈။ ပုဂၢလသုတ္ေဒသနာတရားေတာ္ (၂) ၁၂-၁၂-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/09-ChanMyay-ThanPaDar(4)Par-(1).mp3">
၉။ သမၸဒါေလးပါးတရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D15/10-ChanMyay-ThanPaDar(4)Par-(2).mp3">
၁၀။ သမၸဒါေလးပါးတရားေတာ္ (၂)</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 16</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D16/01-ChanMyay-VI-PAN-LAR-THA-TA-YAR-(1)-14-4-1997-M0N.mp3">
၁။ ၀ိပလႅာသ တရားေတာ္(၁) ၁၄-၄-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D16/02-ChanMyay-VI-PAN-LAR-THA-TA-YAR-(2)-15-4-1997-TUE.mp3">
၂။ ၀ိပလႅာသ တရားေတာ္(၂) ၁၅-၄-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D16/03-ChanMyay-VI-PAN-LAR-THA-TA-YAR-(3)-16-4-1997-WED.mp3">
၃။ ၀ိပလႅာသ တရားေတာ္(၃) ၁၆-၄-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D16/04-ChanMyay-VI-PAN-LAR-THA-TA-YAR-(4)-17-4-1997-THUR.mp3">
၄။ ၀ိပလႅာသ တရားေတာ္(၄) ၁၇-၄-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D16/05-ChanMyay-VI-PAN-LAR-THA-TA-YAR-(5)-19-4-1997-SAT.mp3">
၅။ ၀ိပလႅာသ တရားေတာ္(၅) ၁၈-၄-၁၉၉၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D16/06-ChanMyay-VI-PAN-LAR-THA-TA-YAR-(6)-20-4-1997-SUN.mp3">
၆။ ၀ိပလႅာသ တရားေတာ္(၆) ၁၉-၄-၁၉၉၇</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 17</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/01-ChanMyay-Seik-ko-Shu-Ka-Chan-Tha-Ya-DHAMMA-TALKS.mp3">
၁။ စိတ္ကိုရႈက ခ်မ္းသာရ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/02-ChanMyay-Pa-han-(5)par.mp3">
၂။ ပဟာန္ငါးပါးတရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/03-ChanMyay-Ba-Thar-Ye-San-Thar-Tha-Na-Ye-Hmat-Kyauk-ta-yar-taw.mp3">
၃။ ဘာသာေရးစံ ၊ သာသနာေရးမွတ္ေက်ာက္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/04-ChanMyay-528-MITTA-(31-7-1998-friday).mp3">
၄။ ၅၂၈ သြယ္ ေမတၱာတရားေတာ္ ၃၁-၇-၁၉၉၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/05-ChanMyay-BUDDHA-DAY-TA-YAR-TAW-(1).mp3">
၅။ ဗုဒၶေန ့ တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/06-ChanMyay-BUDDHA-DAY-TA-YAR-TAW-(2).mp3">
၆။ ဗုဒၶေန ့တရားေတာ္ (၂) </a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/07-ChanMyay-Tha-Yai-Ma-Kyauk-Tai-Gar-Htar-ta-yar-taw-(1)-(17-4-2008-Thursday.mp3">
၇။ သရဲမေျခာက္တဲ ့ဂါထာ တရားေတာ္(၁) ၁၇-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/08-ChanMyay-Tha-Yai-Ma-Kyauk-Tai-Gar-Htar-ta-yar-taw-(2)-(17-4-2008-Thursday).mp3">
၈။ သရဲမေျခာက္တဲ ့ဂါထာ တရားေတာ္(၂) ၁၇-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/09-ChanMyay-PA-TAPE-SA-THA-MOK-PAT-TA-YAR-TAW-(1)-(10-8-2008-SUN).mp3">
၉။ ပဋိစၥသမုပၸါဒ္ တရားေတာ္ (၁) သက္ေတာ္ ၈၀ ျပည့္မွာေဟာ ၁၀-၈-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D17/10-ChanMyay-PA-T08-APE-SA-THA-MOK-PAT-TA-YAR-TAW-(2)-10-8-2008-SUNDAY.mp3">
၁၀။ ပဋိစၥသမုပၸါဒ္ တရားေတာ္ (၂) သက္ေတာ္ ၈၀ ျပည့္မွာေဟာ ၁၀-၈-၂၀၀၈</a><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP-3 Disc 18</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/01-ChanMyay-BUDDHA-ka-pi-la-wat-pyi-DayTha-Sar-ri-kyw-khyi-ta-yar-taw-(21-3-2008-fri).mp3">
၁။ ျမတ္စြာဘုရား ပထမဆံုး ကပိလ၀တ္ျပည္ ေဒသစာရီ ၾကြခ်ီေတာ္မူ တရားေတာ္ ၂၁-၃-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/02-ChanMyay-BUDDHA-Ya-Hu-La-Ar-Mein-Kyar-Thaw-Aw-War-Da-Ta-Yar-taw-(16-4-2008-Wednesday).mp3">
၂။ ျမတ္စြာဘုရား ရာဟုလာအား မိန့္ၾကားေသာ ၾသ၀ါဒ တရားေတာ္ ၁၆-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/03-ChanMyay-Thi-La-Theik-Khar-ta-yar-taw-(-22-And--23-3-2008-)-(fri-AND-SAT).mp3">
၃။ သီလသိကၡာ တရားေတာ္ ၂၂+၂၃-၃-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/04-ChanMyay-Tha-Mar-Di-Theik-Khar-ta-yar-taw-(31-3-2008-Monday).mp3">
၄။ သမာဓိသိကၡာ တရားေတာ္ ၃၁-၃-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/05-ChanMyay-Pin-Nyar-Theik-Khar-ta-yar-taw-(1)-1-4-2008(Tuesday).mp3">
၅။ ပညာသိကၡာ တရားေတာ္(၁) ၁-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/06-ChanMyay-Pin-Nyar-Theik-Khar-ta-yar-taw-(2)-4-4-2008-(Friday).mp3">
၆။ ပညာသိကၡာတရားေတာ္ (၂) ၄-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/07-ChanMyay-Ba-wa-tan-boe-ta-yar-taw-(11-5-2008-sunday).mp3">
၇။ ဘ၀တန္ဘိုးတရားေတာ္ ၁၁-၅-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/08-ChanMyay-Oke-Sar-(4)-Myo-Ta-Yar-Taw-(2-5-2008-Friday)-(32-minutes)-&amp;-Hmawbi-kyaung-dar-na-ta-yar-taw-2.mp3">
၈။ ဥစၥာေလးမ်ဳိး တရားေတာ္ႏွင့္ ေက်ာင္းအလွဴ တရားေတာ္ ၂-၅-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/09-ChanMyay-Ta-paw-sa-min-ga-lar-ta-yar-taw.mp3">
၉။ တေပါစမဂၤလာ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D18/10-ChanMyay-CHAMMYAY-MITTA-PO-TA-YAR-TAW-(4-8-1999-WEDNESDAY).mp3">
၁၀။ ခ်မ္းေျမ႔ ေမတၱာပို ့ အဓိပၸါယ္ တရားေတာ္ ၄-၈-၁၉၉၉</a><br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
MP-3 Disc 19</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/01-ChanMyay-A-Chein-Ywe-Ma-Ne-Nai-Ta-Yar-Taw.mp3">
၁။ အခ်ိန္ေရြးမေနႏွင့္ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/02-ChanMyay-3-par-thar-tha-nar-3-par-theik-khar-ta-yar-taw.mp3">
၂။ သံုးပါးသာသနာ သံုးပါး သိကၡာ တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/03-ChanMyay-Tha-mar-di-(3)-myo-(1-2-2007-Thursday).mp3">
၃။ သမာဓိသံုးမ်ဳိး တရားေတာ္ ၁-၂-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/04-ChanMyay-AW-WAR-DA-PAR-TI-MAUNT-TA-YAR-TAW.mp3">
၄။ ၾသ၀ါဒ ပါတိေမာက္ တရားေတာ္ ၃၀-၈-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/05-ChanMyay-Swan-a-kyo-(5)-par-ta-yar-taw-(-30-8-2008-SUN).mp3">
၅။ ဆြမ္းအက်ဳိးငါးပါး တရားေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/06-ChanMyay-Yai-kyaw-thu,s-happy-birthday-ta-yar-taw.mp3">
၆။ ေမာင္ရဲေက်ာ္သူ၏ ေမြးေန ့ အလွဴ တရားေတာ္ </a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/07-ChanMyay-War-so-thin-gan-a-hlu-ta-yar-taw-(1)-(30-7-1989-sunday.mp3">
၇။ ၀ါဆိုသကၤန္းအလွဴ တရားေတာ္(၁) ၃၀-၇-၁၉၈၉</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/08-ChanMyay-War-so-thin-gan-a-hlu-ta-yar-taw-(2)-30-7-1989-sunday.mp3">
၈။ ၀ါဆိုသကၤန္းအလွဴ တရားေတာ္(၂) ၃၀-၇-၁၉၈၉</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/09-ChanMyay-Ki-le-thar-(3)-pyar-theik-khar-(3)-par-(1)-(17-3-1994).mp3">
၉။ ကိေလသာ သံုးျဖာ သိကၡာသံုးပါး တရားေတာ္ (၁) ၁၇-၃-၁၉၉၄</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D19/10-ChanMyay-Ki-le-thar-(3)-pyar-theik-khar-(3)-par-(2)-(17-3-1994).mp3">
၁၀။ ကိေလသာ သံုးျဖာ သိကၡာသံုးပါး တရားေတာ္ (၂) ၁၇-၃-၁၉၉၄</a><br>
<br>
MP-3 Disc 20</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/01-ChanMyay-Tha-ma-hta-ka-ma-htan-&amp;-Vipassana-bar-wa-nar-(1)-(4-11-2008-tue).mp3">
၁။ သမထ ကမၼ႒ာန္း ႏွင့္ ၀ိပႆနာဘာ၀နာ တရားေတာ္ (၁) ၄-၁၁-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/02-ChanMyay-Tha-ma-hta-ka-ma-htan-&amp;-Vipassana-bar-wa-nar-(2)-(5-11-2008-wed).mp3">
၂။ သမထ ကမၼ႒ာန္း ႏွင့္ ၀ိပႆနာဘာ၀နာ တရားေတာ္ (၂) ၅-၁၁-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/03-ChanMyay-Tha-ma-hta-ka-ma-htan-&amp;-Vipassana-bar-wa-nar-(3)-(6-11-2008-thur).mp3">
၃။ သမထ ကမၼ႒ာန္း ႏွင့္ ၀ိပႆနာဘာ၀နာ တရားေတာ္ (၃) ၆-၁၁-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/04-ChanMyay-Tha-ma-hta-ka-ma-htan-&amp;-Vipassana-bar-wa-nar-(4)-9-11-2008-sunday.mp3">
၄။ သမထ ကမၼ႒ာန္း ႏွင့္ ၀ိပႆနာဘာ၀နာ တရားေတာ္ (၄) ၉-၁၁-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/05-ChanMyay-Tha-Thi-Pat-Htan-(4)-Pa-&amp;-NatTho-Pyaw-Chein(3)MyO-20-3-2008--Thursday).mp3">
၅။ သတိပ႒ာန္ေလးပါးတရားႏွင့္ နတ္တို ့ေပ်ာ္ခ်ိန္သံုးမ်ဳိး တရားေတာ္ ၂၀-၃-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/06-ChanMyay-MYANMAR-HAPPY-NEW-YEAR-1369-FROM-1370-TO-NEWYEAR-(5-4-2008-SAT).mp3">
၆။ ၁၃၆၉- ခုႏွစ္မွ ၊ ၁၃၇၀- ျပည့္ႏွစ္သို ့ ႏွစ္သစ္မဂၤလာသ၀ဏ္လႊာ တရားေတာ္ ၅-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/07-ChanMyay-Ko-kyin-ta-yar-myi-thi-a-khar-hmy-ma-khywat-yywin-par-se-and-ta-yar-taw-(7-4-2008-Monday).mp3">
၇။ ကိုယ္က်င့္တရား မည္သည့္အခါမ်ွ မခြ်တ္ယြင္းပါေစႏွင့္ တရားေတာ္ ၇-၄-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/08-ChanMyay-Thu-taw-koung-lat-kha-nar-&amp;-thu-yoke-mar-lat-kha-nar-ta-yar-taw-(-28-9-2008-Tuesday).mp3">
၈။ သူေတာ္ေကာင္းလကၡဏာႏွင့္ သူယုတ္မာလကၡဏာ တရားေတာ္ ၂၈-၉-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/09-ChanMyay-Mok-cha-pyu-lok-ya-myi-koung-hmu-ku-tho-(10)-myo-ta-yar-taw-(29-10-2008-wednesday).mp3">
၉။ မုခ် ျပဳလုပ္ရမည့္ ေကာင္းမႈကုသိုလ္အက်ယ္ဆယ္မ်ဳိး တရားေတာ္ ၂၉-၁၀-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D20/10-ChanMyay-Thar-tha-na-yai-baw-ta-yar-taw-(8-4-1998).mp3">
၁၀။ သာသနာ့ရဲေဘာ္ တရားေတာ္ ၈-၄-၁၉၉၈</a><br>
<br>
<br>
MP-3 Disc 21</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D21/01-ChanMyay-Than-la-thok-ta-yar-taw-(1)-13-4-1993.mp3">
၁။ သလႅသုတ္ေဒသနာ (ဆူး) တရားေတာ္ (၁) ၁၃-၄-၁၉၉၃</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D21/02-ChanMyay-Than-la-thok-ta-yar-taw-(2)-14-4-1993.mp3">
၂။ သလႅသုတ္ေဒသနာ (ဆူး) တရားေတာ္ (၂) ၁၄-၄-၁၉၉၃</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D21/03-ChanMyay-Than-la-thok-ta-yar-taw-(3)-15-4-1993.mp3">
၃။ သလႅသုတ္ေဒသနာ (ဆူး) တရားေတာ္ (၃) ၁၅-၄-၁၉၉၃</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D21/04-ChanMyay-Than-la-thok-ta-yar-taw-(4).mp3">
၄။ သလႅသုတ္ေဒသနာ (ဆူး) တရားေတာ္ (၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D21/05-ChanMyay-Than-la-thok-ta-yar-taw-(5)-.mp3">
၅။ သလႅသုတ္ေဒသနာ (ဆူး) တရားေတာ္ (၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D21/06-ChanMyay-Than-la-thok-ta-yar-taw-(6).mp3">
၆။ သလႅသုတ္ေဒသနာ (ဆူး) တရားေတာ္ (၆)</a><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">MP-3 Disc 22</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/01-ChanMyay-Seik.mp3">
၁။ စိတ္တရားေတာ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/02-ChanMyay-Seik.mp3">
၂။ စိတ္တရားေတာ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/03-ChanMyay-Seik.mp3">
၃။ စိတ္တရားေတာ္ (၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/04-ChanMyay-Seik.mp3">
၄။ စိတ္တရားေတာ္ (၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/05-ChanMyay-Seik.mp3">
၅။ စိတ္တရားေတာ္ (၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/06-ChanMyay-Seik.mp3">
၆။ စိတ္တရားေတာ္ (၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/07-ChanMyay-Seik.mp3">
၇။ စိတ္တရားေတာ္ (၇)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/08-ChanMyay-Seik.mp3">
၈။ စိတ္တရားေတာ္ (၈)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/09-ChanMyay-Seik.mp3">
၉။ စိတ္တရားေတာ္ (၉)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/10-ChanMyay-Seik.mp3">
၁၀။ စိတ္တရားေတာ္ (၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/11-ChanMyay-Seik.mp3">
၁၁။ စိတ္တရားေတာ္ (၁၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/12-ChanMyay-Seik.mp3">
၁၂။ စိတ္တရားေတာ္ (၁၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/13-ChanMyay-Seik.mp3">
၁၃။ စိတ္တရားေတာ္ (၁၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/14-ChanMyay-Seik.mp3">
၁၄။ စိတ္တရားေတာ္ (၁၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/15-ChanMyay-Seik.mp3">
၁၅။ စိတ္တရားေတာ္ (၁၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/MP3D22/16-ChanMyay-Seik.mp3">
၁၆။ စိတ္တရားေတာ္ (၁၆)</a><br>
<br>
<br>
<br>
</font>
****************************************************************************************<font size="4" face="Zawgyi-One"><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
၁၉၈၄ ဇူလိုင္လမွ ၁၉၈၅ ဇန္န၀ါရီလ အတြင္း<br>
မဟာစည္သာႆနရိပ္သာတြင္ ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/001-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁။ စိတ္တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/002-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂။ စိတ္တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/003-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃။ စိတ္တရားေတာ္ (၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/004-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄။ စိတ္တရားေတာ္ (၄)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/005-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅။ စိတ္တရားေတာ္ (၅)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/006-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၆။ စိတ္တရားေတာ္ (၆)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/007-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၇။ စိတ္တရားေတာ္ (၇)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/008-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၈။ စိတ္တရားေတာ္ (၈)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/009-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၉။ စိတ္တရားေတာ္ (၉)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/010-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၀။ စိတ္တရားေတာ္ (၁၀)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/011-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၁။ စိတ္တရားေတာ္ (၁၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/012-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၂။ စိတ္တရားေတာ္ (၁၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/013-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၃။ စိတ္တရားေတာ္ (၁၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/014-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၄။ စိတ္တရားေတာ္ (၁၄)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/015-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၅။ စိတ္တရားေတာ္ (၁၅)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/016-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၆။ စိတ္တရားေတာ္ (၁၆)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/017-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၇။ စိတ္တရားေတာ္ (၁၇)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/018-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၈။ စိတ္တရားေတာ္ (၁၈)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/019-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၁၉။ စိတ္တရားေတာ္ (၁၉)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/020-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၀။ စိတ္တရားေတာ္ (၂၀)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/021-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၁။ စိတ္တရားေတာ္ (၂၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/022-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၂။ စိတ္တရားေတာ္ (၂၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/023-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၃။ စိတ္တရားေတာ္ (၂၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/024-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၄။ စိတ္တရားေတာ္ (၂၄)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/025-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၅။ စိတ္တရားေတာ္ (၂၅)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/026-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၆။ စိတ္တရားေတာ္ (၂၆)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/027-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၇။ စိတ္တရားေတာ္ (၂၇)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/028-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၈။ စိတ္တရားေတာ္ (၂၈)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/029-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၂၉။ စိတ္တရားေတာ္ (၂၉)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/030-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၀။ စိတ္တရားေတာ္ (၃၀)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/031-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၁။ စိတ္တရားေတာ္ (၃၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/032-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၂။ စိတ္တရားေတာ္ (၃၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/033-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၃။ စိတ္တရားေတာ္ (၃၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/034-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၄။ စိတ္တရားေတာ္ (၃၄)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/035-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၅။ စိတ္တရားေတာ္ (၃၅)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/036-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၆။ စိတ္တရားေတာ္ (၃၆)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/037-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၇။ စိတ္တရားေတာ္ (၃၇)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/038-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၈။ စိတ္တရားေတာ္ (၃၈)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/039-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၃၉။ စိတ္တရားေတာ္ (၃၉)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/040-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၀။ စိတ္တရားေတာ္ (၄၀)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/041-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၁။ စိတ္တရားေတာ္ (၄၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/042-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၂။ စိတ္တရားေတာ္ (၄၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/043-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၃။ စိတ္တရားေတာ္ (၄၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/044-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၄။ စိတ္တရားေတာ္ (၄၄)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/045-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၅။ စိတ္တရားေတာ္ (၄၅)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/046-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၆။ စိတ္တရားေတာ္ (၄၆)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/047-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၇။ စိတ္တရားေတာ္ (၄၇)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/048-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၈။ စိတ္တရားေတာ္ (၄၈)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/049-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၄၉။ စိတ္တရားေတာ္ (၄၉)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/050-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၀။ စိတ္တရားေတာ္ (၅၀)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/051-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၁။ စိတ္တရားေတာ္ (၅၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/052-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၂။ စိတ္တရားေတာ္ (၅၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/053-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၃။ စိတ္တရားေတာ္ (၅၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/054-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၄။ စိတ္တရားေတာ္ (၅၄)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/055-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၅။ စိတ္တရားေတာ္ (၅၅)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/056-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၆။ စိတ္တရားေတာ္ (၅၆)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/FromJuly1984ToJan1985-at-Mahasi/057-ChanMyaySayaDawAshinJanakabhivamsa-SateTayar-July84toJan85.mp3">
၅၇။ စိတ္တရားေတာ္ (၅၇)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<br>
</font>
****************************************************************************************<font size="4" face="Zawgyi-One"><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
****dhamma talks uploaded and published on 27 Aug 2010 ****</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/001-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁။ ကုသိုလ္ အကုသိုလ္ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/002-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂။ ကုသိုလ္ အကုသိုလ္ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/003-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃။ သကၠာယဒိ႒ိ၊ အတၱဒိ႒ိ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/004-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄။ သႆတဒိ႒ိ၊ ဥေစၦဒဒိ႒ိ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/005-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅။ သႆတဒိ႒ိ၊ ဥေစၦဒဒိ႒ိ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/006-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆။ မီးေလာင္အိမ္မွ ဥစၥာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/007-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇။ ဆဠဂၤဒါန တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/008-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈။ သပၸဳရိသဒါန တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/009-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉။ ေစေတာခိလ(၅)ပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/010-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀။ အသိျမင္မွန္မွ ခ်မ္းသာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/011-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁။ သိ၊ ပယ္၊ ဆိုက္၊ ပြား&nbsp; တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/012-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂။ ဗုဒၶနည္းက် ခ်မ္းသာစြာ ေနထိုင္နည္း တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/013-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃။ အျဖစ္ႏွင့္ အပ်က္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/014-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄။ ဗုဒၶ၏ အနတၱဝါဒ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/015-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅။ ပူေဇာ္ထိုက္သူ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/016-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆။ စိတ္ယဥ္ေက်းက ခ်မ္းသာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/017-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇။ ရႈမွတ္မႈၿမဲလွ်င္ ကိေလသာစင္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/018-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈။ ဆြမ္းက်ိဳးတုန္႕ျပန္ ျမတ္ေမြခံ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/019-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉။ သတိပ႒ာန္&nbsp; တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/020-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀။ သႆတဒိ႒ိ၊ ဥေစၦဒဒိ႒ိ၊ အႏၱရာဘဝဒိ႒ိ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/021-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁။ သိကၡာသုံးပါးျဖင့္ ကိေလသာသုံးပါးပယ္သတ္ပုံ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/022-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂။ သိ၊ ပယ္၊ ဆိုက္၊ ပြား တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/023-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃။ အေၾကာင္းႏွင့္ အက်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/024-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄။ အပဏၰကပဋိပဒါ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/025-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅။ အတၱေျခာက္မ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/026-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆။ အတၱဒိ႒ိႏွင့္ သကၠာယဒိ႒ိ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/027-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇။ ဘိကၡဳႏွင့္ သမဏ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/028-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၈။ ဗိုလ္ငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/029-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၉။ ခ်မ္းသာေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/030-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၀။ ဓမၼစႀကၤာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/031-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၁။ ဣေႁႏၵငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/032-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၂။ ခႏၶာငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/033-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၃။ အာဇီဝဌမကသီလ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/034-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၄။ ဘယသုတ္ ေဒသနာေတာ္ႏွင့္ ဗုဒၶနည္းက် ခ်မ္းသာစြာေနထိုင္နည္း</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/035-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၅။ ျမတ္စြာဘုရား၏ အဆုံးအမ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/036-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၆။ ေမတၱာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/037-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၇။ စိတ္ကိုျဖဴစင္ေစနည္းေျခာက္မ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/038-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၈။ ေစေတာခိလငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/039-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၃၉။ တစပဥၥက ကမၼ႒ာန္း တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/040-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၀။ တရာဂုဏ္ေတာ္ေျခာက္ပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/041-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၁။ သမၸဇညေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/042-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၂။ သရဏဂုဏ္တရားႏွင့္ အေသးစိတ္ရႈပုံ</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/043-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၃။ ခ်မ္းေျမ႕မဂၤလာ သင္စရာ(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/044-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၄။ ခ်မ္းေျမ႕မဂၤလာ သင္စရာ(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/045-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၅။ ေမတၱာ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/046-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၆။ ေမတၱာ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/047-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၇။ ပုဂၢိဳလ္ေလးမ်ိဳး တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/048-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၈။ ပုဂၢိဳလ္ေလးမ်ဳး တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/049-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၄၉။ စိတ္ကိုထိန္းမွ ခ်မ္းသာရ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/050-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၀။ စိတ္ကိုထန္းမွ ခ်မ္းသာရ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/051-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၁။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/052-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၂။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/053-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၃။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/054-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၄။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/055-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၅။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/056-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၆။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/057-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၇။ ဣေႁႏၵငါးပါး အားေကာင္းေၾကာင္းအဂၤါကိုးပါး တရားေတာ္ (၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/058-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၈။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/059-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၅၉။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/060-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၀။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/061-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၁။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/062-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၂။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/063-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၃။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/064-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၄။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/065-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၅။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၈)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/066-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၆။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၉)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/067-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၇။ ဗုဒၶျမတ္စြာဘုရာ၏ ႀကီးပြားခ်မ္းသာေရး တရားေတာ္ (၁၀)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/068-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၈။ အေကာင္းေလးမ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/069-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၆၉။ အားကိုးမွန္မွ ခ်မ္းသာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/070-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၀။ ဓမၼဳေဒၶသေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/071-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၁။ မီးေလာင္အိမ္မွ ဥစၥာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/072-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၂။ မဂၤလာတရားေတာ္ႏွင့္ တရားနာရျခင္း အက်ိဳးငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/073-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၃။ ပုဂၢိဳလ္ေလးမ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/074-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၄။ ဆဠဂၤဒါန တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/075-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၅။ သပၸဳရိသဒါန တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/076-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၆။ သစၥာေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/077-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၇။ သီလရနံ႕ အရပ္တိုင္းပ်ံ႕ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/078-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၈။ ဒါန တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/079-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၇၉။ ဥာဏ္တဆယ့္ေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/080-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၀။ စက္ေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/081-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၁။ သိကၡာသုံးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/082-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၂။ သကၠာယဒိ႒ိ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/083-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၃။ ဥပါဒြန္ေလးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/084-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၄။ ယခုလုပ္ရမည္႕ အလုပ္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/085-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၅။ ေယာဂီအရည္အေသြးငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/086-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၆။ ရည္စူးလႈက ျမတ္ဒါန တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/087-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၇။ အလႈတတ္လွ်င္ နိဗၺာန္ဝင္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/088-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၈။ သတိတရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/089-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၈၉။ သကၠာယဒိဠိ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/090-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၀။ သပၸဳရိသ ဒါနႏွင့္ ဥပါဒါနကၡႏၶာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/091-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၁။ သိကၡာသုံးပါး ရွင္ျပဳအလႈ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/092-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၂။ သီလဗၺတပရာမာသ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/093-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၃။ ဝိပႆနာအေျခခံ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/094-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၄။ ဝိပႆနာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/095-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၅။ (၂၃)ႀကိမ္ေျမာက္ ကထိန္ အလႈ</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/096-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၆။ အဘိဓမၼာအေၾကာင္းႏွင့္ သတိပ႒ာန္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/097-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၇။ အျမတ္ဆုံးပူဇာ</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/098-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၈။ ဒါန၊ သီလဓ ဘာဝနာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/099-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၉၉။ မုခ်ျပဳလုပ္ရမည္႕ ကုသိုလ္သုံးမ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/100-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၀။ ပုညႀကိယဝတၳဳဆယ္ပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/101-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၁။ သတိပ႒ာန္ အက်ဥ္းခ်ဳပ္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/102-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၂။ ေဗာဇၥ်င္ ခုႏွစ္ပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/103-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၃။ ယုံၾကည္မႈရွိမွ ခ်မ္းသာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/104-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၄။ ရုပ္၊ နာမ္ သ္လွ်င္ ဒိ႒ိစင္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/105-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၅။ အတၱ (၆)မ်ိဳး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/106-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၆။ အတၱ (၆)မ်ိဳး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/107-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၇။ ဘယသုတ္ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/108-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၈။ ဘယသုတ္ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/109-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၀၉။ ဣေႁႏၵငါးပါး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/110-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၀။ ဣေႁႏၵငါးပါး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/111-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၁။ နတ္တို႕ေပ်ာ္သံ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/112-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၂။ နတ္တို႕ေပ်ာ္သံ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/113-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၃။ ဝိပႆနာတရားႏွင့္ ေယာဂီအဂၤါငါးပါး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/114-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၄။ ဝိပႆနာတရားႏွင့္ ေယာဂီအဂၤါငါးပါး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/115-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၅။ ေကာင္းမႈႏွင့္ မေကာင္းမႈ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/116-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၆။ ဏာဏ္စဥ္ အက်ဥ္းခ်ဳပ္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/117-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၇။ လူမိုက္ႏွင့္ လူလိမၼာ ပညာရွိ ျခားနားခ်က္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/118-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၈။ ေဆးေဖၚ၍ ေသာက္ ေရာဂါေပ်ာက္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/119-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၁၉။ စိတ္ေအးၾကည္လင္ အက်ိဳးျမင္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/120-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၀။ သားသမီးက်င့္ဝတ္ ငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/121-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၁။ ဥပါဒါန္ ေလးပါးႏွင့္ သကၠာယဒိ႒ိ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/122-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၂။ ဝါရိတၱသီလႏွင့္ စာရိတၱသီလ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/123-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၃။ ဝိသုဒၶိ ခုႏွစ္မ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/124-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၄။ ေယာနိေသာ မနသိကာရႏွင့္ အေယာသိက မနသိကာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/125-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၅။ စိတ္ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/126-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၆။ စိတ္ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/127-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၇။ တရားအားထုတ္တာ ရည္ရြယ္ခ်က္က ဘာလဲ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/128-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၈။ တရားအားထုတ္တာ ရည္ရြယ္ခ်က္က ဘာလဲ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/129-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၂၉။ သူေတာ္ေကာင္းႏွင့္သာ ေပါင္းသင္းပါ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/130-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၀။ သူေတာ္ေကာင္းႏွင့္သာ ေပါင္းသင္းပါ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/131-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၁။ ေဝဒနာႏုပႆနာ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/132-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၂။ ေဝဒနာႏုပႆနာ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/133-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၃။ အဘိဓမၼာေဒသနာႏွင့္ ပဝါရဏာပြဲအေၾကာင္း</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/134-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၄။ အပဏၰက ပဋိပဒါ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/135-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၅။ အပဏၰက ပဋိပဒါ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/136-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၆။ မာရ္ငါးပါး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/137-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၇။ မာရ္ငါးပါး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/138-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၈။ မာရ္ငါးပါး တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/139-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၃၉။ ပုဂၢလသုတ္ ေဒသနာေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/140-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၀။ ပုဂၢလသုတ္ ေဒသနာေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/141-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၁။ သမၸဒါေလးပါး တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/142-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၂။ သမၸဒါေလးပါး တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/143-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၃။ ဝိပလႅာသ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/144-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၄။ ဝိပလႅာသ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/145-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၅။ ဝိပလႅာသ တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/146-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၆။ ဝိပလႅာသ တရားေတာ္ (၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/147-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၇။ ဝိပလႅာသ တရားေတာ္ (၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/148-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၈။ ဝိပလႅာသ တရားေတာ္ (၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/149-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၄၉။ စိတ္ကိုရႈက ခ်မ္းသာရ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/150-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၀။ ပဟာန္ငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/151-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၁။ ဘာသာေရးစံသာသနာမွတ္ေက်ာက္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/152-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၂။ (၅၂၈)သြယ္ ေမတၱာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/153-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၃။ ဗုဒၶေန႕ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/154-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၄။ ဗုဒၶေန႕ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/155-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၅။ သရဲမေျခာက္တဲ့ဂါထာ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/156-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၆။ သရဲမေျခာက္တဲ့ဂါထာ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/157-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၇။ ပဋိစၥသမုပၸါဒ္ (သက္ေတာ္ ၈၀ျပည္႕ေဟာ) တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/158-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၈။ ပဋိစၥသမုပၸါဒ္ (သက္ေတာ္ ၈၀ျပည္႕ေဟာ) တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/159-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၅၉။ ျမတ္စြာဘုရားပထမဆုံး ကပိလဝတ္ ေဒသစာရီႂကြခ်ီေတာ္မူ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/160-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၀။ ျမတ္စြာဘုရား ရာဟုလာအား မိန္႕ၾကားေသာ ၾသဝါဒ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/161-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၁။ သီလ သိကၡာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/162-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၂။ သမာဓိ သိကၡာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/163-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၃။ ပညာသိကၡာ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/164-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၄။ ပညာသိကၡာ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/165-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၅။ ဘဝတန္ဘိုး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/166-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၆။ ဥစၥာေလးမ်ိဳး တရားေတာ္ႏွင့္ ေက်ာင္းအလႈ</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/167-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၇။ တေပါစ မဂၤလာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/168-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၈။ ခ်မ္းေျမ႕ ေမတၱာပို႕ အဓပၸါယ္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/169-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၆၉။ အခ်ိန္ေရြး ေႏွးမေနႏွင့္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/170-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၀။ သုံးပါးသာသနာ သုံးပါသိကၡာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/171-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၁။ သမာဓိ သုံးမ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/172-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၂။ ၾသဝါဒ ပါတိေမာက္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/173-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၃။ ဆြမ္းအက်ိဳး ငါးပါး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/174-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၄။ ေမာင္ရဲေက်ာ္သူ၏ ေမြေန႕အလႈ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/175-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၅။ ဝါဆိုသကၤန္းအလႈ တရာေးတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/176-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၆။ ဝါဆိုသကၤန္းအလႈ တရာေးတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/177-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၇။ ကိေလသာသုံးျဖာ သိကၡာသုံးပါး တရာေးတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/178-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၈။ ကိေလသာသုံးျဖာ သိကၡာသုံးပါး တရာေးတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/179-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၇၉။ သမထ ကမၼ႒ာန္းေလးပါးႏွင့္ ဝိပႆနာဘာဝနာ တရားေတာ္(၁)&nbsp; </a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/180-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၀။ သမထ ကမၼ႒ာန္းေလးပါးႏွင့္ ဝိပႆနာဘာဝနာ တရားေတာ္(၂)&nbsp; </a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/181-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၁။ သမထ ကမၼ႒ာန္းေလးပါးႏွင့္ ဝိပႆနာဘာဝနာ တရားေတာ္(၃) </a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/182-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၂။ သမထ ကမၼ႒ာန္းေလးပါးႏွင့္ ဝိပႆနာဘာဝနာ တရားေတာ္(၄)&nbsp;&nbsp; </a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/183-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၃။ (၁၃၇၀) ျပည္႕ႏွစ္ ႏွစ္သစ္မဂၤလာ သဝစ္လႊာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/184-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၄။ သတိပ႒ာန္ေလးပါႏွင့္ နတ္တို႕ေပ်ာ္ခ်ိန္သုံးမ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/185-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၅။ ကိုယ္က်င့္တရားမည္သည္႕အခါမွ် မခၽြတ္ယြင္းပါေစႏွင့္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/186-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၆။ သူေတာ္ေကာင္း လကၡဏာႏွင့္ သူယုတ္မာလကၡဏာ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/187-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၇။ မုခ်ျပဳလုပ္ရမည္႕ ေကာင္းမႈကုသိုလ္ အက်ယ္ ဆယ္မ်ိဳး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/188-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၈။ သာသနာ့ရဲေဘာ္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/189-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၈၉။ သလႅသုတ္ ေဒသနာေတာ္ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/190-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၀။ သလႅသုတ္ ေဒသနာေတာ္ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/191-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၁။ သလႅသုတ္ ေဒသနာေတာ္ တရားေတာ္(၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/192-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၂။ သလႅသုတ္ ေဒသနာေတာ္ တရားေတာ္(၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/193-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၃။ သလႅသုတ္ ေဒသနာေတာ္ တရားေတာ္(၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/194-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၄။ သလႅသုတ္ ေဒသနာေတာ္ တရားေတာ္(၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/195-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၅။ စုႏၵသုတ္ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/196-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၆။ စုႏၵသုတ္ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/197-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၇။ စုႏၵသုတ္ တရားေတာ္(၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/198-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၈။ ဓမၼစႀကၤာ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/199-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၁၉၉။ ဓမၼစႀကၤာ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/200-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၀။ ဓမၼစႀကၤာ တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/201-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၁။ ဓမၼစႀကၤာ တရားေတာ္ (၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/202-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၂။ ဓမၼစႀကၤာ တရားေတာ္ (၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/204-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၃။ ဓမၼစႀကၤာ တရားေတာ္ (၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/204-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၄။ ဓမၼစႀကၤာ တရားေတာ္ (၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/205-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၅။ ဓမၼစႀကၤာ တရားေတာ္ (၈)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/206-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၆။ ဓမၼစႀကၤာ တရားေတာ္ (၉)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/207-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၇။ ဓမၼစႀကၤာ တရားေတာ္ (၁၀)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/208-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၈။ ဓမၼစႀကၤာ တရားေတာ္ (၁၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/209-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၀၉။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/210-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၀။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/211-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၁။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/212-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၂။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/213-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၃။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/214-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၄။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/215-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၅။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/216-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၆။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၈)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/217-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၇။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၉)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/218-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၈။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၁၀)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/219-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၁၉။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၁၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/220-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၀။ ကခၤါဝိတရဏ ဝိသုဒိၶ တရားေတာ္ (၁၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/221-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၁။ ဒါရုကၡေႏၶာပမသုတ္ တရားေတာ္ (၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/222-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၂။ ဒါရုကၡေႏၶာပမသုတ္ တရားေတာ္ (၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/223-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၃။ ဒါရုကၡေႏၶာပမသုတ္ တရားေတာ္ (၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/224-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၄။ ဒါရုကၡေႏၶာပမသုတ္ တရားေတာ္ (၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/225-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၅။ ဒါရုကၡေႏၶာပမသုတ္ တရားေတာ္ (၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/226-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၆။ စိတ္ေကာင္းရွိမွ ခ်မ္းသာရ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/227-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၇။ စိတ္ေကာင္းရွိမွ ခ်မ္းသာရ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/228-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၈။ စိတ္ေကာင္းရွိမွ ခ်မ္းသာရ တရားေတာ္(၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/229-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၂၉။ စိတ္ေကာင္းရွိမွ ခ်မ္းသာရ တရားေတာ္(၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/230-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၀။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/231-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၁။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/232-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၂။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/233-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၃။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/234-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၄။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/235-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၅။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/236-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၆။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/237-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၇။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၈)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/238-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၈။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၉)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/239-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၃၉။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၀)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/240-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၀။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/241-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၁။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/242-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၂။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/243-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၃။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/244-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၄။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/245-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၅။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/246-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၆။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/247-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၇။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၈)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/248-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၈။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁၉)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/249-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၄၉။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၀)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/250-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၀။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/251-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၁။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/252-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၂။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/253-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၃။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/254-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၄။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/255-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၅။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/256-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၆။ ကံတမလြန္ဘဝ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/257-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၇။ စိတ္ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/258-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၈။ စိတ္ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/259-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၅၉။ စိတ္ တရားေတာ္(၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/260-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၀။ စိတ္ တရားေတာ္(၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/261-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၁။ စိတ္ တရားေတာ္(၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/262-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၂။ စိတ္ တရားေတာ္(၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/263-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၃။ စိတ္ တရားေတာ္(၇)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/264-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၄။ စိတ္ တရားေတာ္(၈)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/265-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၅။ စိတ္ တရားေတာ္(၉)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/266-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၆။ စိတ္ တရားေတာ္(၁၀)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/267-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၇။ စိတ္ တရားေတာ္(၁၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/268-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၈။ စိတ္ တရားေတာ္(၁၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/269-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၆၉။ စိတ္ တရားေတာ္(၁၃)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/270-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၀။ စိတ္ တရားေတာ္(၁၄)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/271-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၁။ စိတ္ တရားေတာ္(၁၅)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/272-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၂။ စိတ္ တရားေတာ္(၁၆)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/273-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၃။ ယခုလုပ္ရမည္႕အလုပ္ တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/274-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၄။ ယခုလုပ္ရမည္႕အလုပ္ တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/275-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၅။ ေဝဒနာႏုပႆနာ သတိပ႒ာန္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/276-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၆။ ဝဋ္ဆင္းရဲမွ လြတ္ေျမာက္ေရး တရာေးတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/277-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၇။ ဝဋ္ဆင္းရဲမွ လြတ္ေျမာက္ေရး တရာေးတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/278-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၈။ ဘာေၾကာင့္ ဗုဒၶဘာသာကို ကိုးကြယ္ၾကသလဲ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/279-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၇၉။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၁)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/280-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၈၀။ စိတ္ထားျဖဴေဖြး ခ်မ္းသာေရး တရားေတာ္(၂)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/281-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
၂၈၁။ ဝဋ္ဆင္းရဲမွ လြတ္ေျမာက္ေရး တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/282-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
282/ Vipassana Meditation (1)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/283-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
283/ Vipassana Meditation (2)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/284-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
284/ Vipassana Meditation (3)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/285-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
285/ Vipassana Meditation (4)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/286-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
286/ Vipassana Meditation (5)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/287-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
287/ Vipassana Meditation (6)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/288-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
288/ Vipassana Meditation (7)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/289-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
289/ Vipassana Meditation (8)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/290-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
290/ Vipassana Meditation (9)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/291-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
291/ Vipassana Meditation (10)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/292-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
292/ Vipassana Meditation (11)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/293-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
293/ Vipassana Meditation (12)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/294-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
294/ Vipassana Meditation (13)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/295-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
295/ Vipassana Meditation (14)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/296-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
296/ Vipassana Meditation (15)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/297-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
297/ Vipassana Meditation (16)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/298-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
298/ Vipassana Meditation (17)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/299-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
299/ Vipassana Meditation (18)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/300-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
300/ Vipassana Meditation (19)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/301-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
301/ Vipassana Meditation (20)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/302-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
302/ Vipassana Meditation (21)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/303-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
303/ Vipassana Meditation (22)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/304-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
304/ Vipassana Meditation (23)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/305-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
305/ Vipassana Meditation (24)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/306-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
306/ Vipassana Meditation (25)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/307-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
307/ Vipassana Meditation (26)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/308-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
308/ Vipassana Meditation (27)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/26-8-2010/309-ChanMyaySayaDaw-Ashin-Janakabhivamsa-DVD309.mp3">
309/ Vipassana Meditation (28)</a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/DarrokeKhanNawMaThoat/01-ChanMyay-Darroke-01-1995-4-15.mp3">ဒါရုကၡေႏၶာပမသုတၱန္ (၁) 
၁၅-၄-၁၉၉၅ ညေန ၄ နာရီ </a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/DarrokeKhanNawMaThoat/02-ChanMyay-Darroke-02-1995-4-16.mp3">ဒါရုကၡေႏၶာပမသုတၱန္ (၂) 
၁၆-၄-၁၉၉၅ ညေန ၄ နာရီ </a></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<a href="http://dhammadownload.com/MP3Library/AshinJanakavamsa-ChanMyay/myanmar/DarrokeKhanNawMaThoat/03-ChanMyay-Darroke-02-1995-4-17.mp3">ဒါရုကၡေႏၶာပမသုတၱန္ (၃) 
၁၇-၄-၁၉၉၅ ညေန ၄ နာရီ </a></p>
"""

soup = bs4(text, 'html.parser')

'''
with open('titles_links.txt', 'w') as f:
    count = 1
    for key in soup.find_all('a'):
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
            #f.write('{}\n'.format(key.get_text()))
            count += 1
'''            
count = 438
for key in soup.find_all('a'):
    if ".mp3" in key.get('href'):
        counter = '{:03d}'.format(count)
        print('{}.mp3|{}|{}'.format(counter, key.get('href'), key.get_text().strip().lstrip().rstrip()))
        #print(key.get_text())
        
        count += 1
    
    '''
    if ".mp3" in key.get('href'):
        counter = '{:03d}'.format(count)
        f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
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