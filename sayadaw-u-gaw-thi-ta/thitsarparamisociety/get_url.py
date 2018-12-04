from bs4 import BeautifulSoup as bs4

text = """

<h5><span style="color: #339966;">ဆရာေတာ္ ဦးေဃာသိတေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား စုစည္းမွု (MP3)</span></h5>
<h3></h3>
<h5><span style="color: #339966;">ဖိုင္ (၁)</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/08-130493E.mp3"><span style="color: #ff9900;">၁။ ပဋိစၥသမုပၸါဒ္ အေျခခံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/02-140493M.mp3"><span style="color: #ff9900;"><span style="color: #ff9900;">၂။ ရွည္လ်ားတဲ့ ဘဝသံသရာ</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/09-140493E.mp3"><span style="color: #ff9900;"><span style="color: #ff9900;">၃။ ပဋိစၥသမုပၸါဒ္ႏွင့္ ကမၼဘဝရွင္းတမ္း</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/05-170493M.mp3"><span style="color: #ff9900;"><span style="color: #ff9900;">၄။ အတိတ္ကံအစြမ္းေၾကာင့္ ျဖစ္ေပၚလာပံု</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/03-150493M.mp3"><span style="color: #ff9900;"><span style="color: #ff9900;">၅။ ရုပ္နာမ္ခြဲ ပညတ္ပရမတ္ခြဲ</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/10-150493E.mp3"><span style="color: #ff9900;"><span style="color: #ff9900;">၆။ တဏွာသခၤယသုတ္</span></span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/04-160493M.mp3"><span style="color: #ff9900;">၇။ (၆၂)ပါးေသာ မိစၦာဒိ႒ိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/11-160493E.mp3"><span style="color: #ff9900;">၈။ ဆပၸါဏေကာပမသုတ္ (သားေကာင္-၆ ေကာင္ ဥပမာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/01-130493M.mp3"><span style="color: #ff9900;">၉။ သုညတဆိုက္ေအာင္ရႈပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/12-170493E.mp3"><span style="color: #ff9900;">၁၀။ ေတဝိဇၨသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/06-180493M.mp3"><span style="color: #ff9900;">၁၁။ ဖဂၢဳနရဟန္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/13-180493E.mp3"><span style="color: #ff9900;">၁၂။ ဒါရုကၡေႏ႖ာပမသုတ္</span></a></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/07-190493M.mp3"><span style="color: #ff9900;">၁၃။ သမၼဒိ႒ိ (၅)မ်ဳိး</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1993%207%20Days/14-190493E.mp3"><span style="color: #ff9900;">၁၄။ အဂၢိဝစ ၦသုတ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၂)</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/001%20060695M%20Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20AKhay%20Khan.mp3"><span style="color: #ff9900;">၁။ ပဋိစၥသမုပၸါဒ္အေျခခံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/006%20060695E%20Char%20Lae%20Du%20Kha.mp3"><span style="color: #ff9900;">၂။ ခ်ာလည္ဒုကၡေရာက္၊ ကမၼဘဝရွင္းတမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/002%20070695M%20A%20Tait%20Kan%20Swan.mp3"><span style="color: #ff9900;">၃။ အတိတ္ကံစြမ္းေၾကာင့္ ျဖစ္ေပၚလာပံု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/007%20070695E%20Yoat%20Nan%20Khoe.mp3"><span style="color: #ff9900;">၄။ ရုပ္နာမ္ခြဲ၊ ပညတ္ပရမတ္ခြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/003%20080695M%20Dat%20Kyi%20%2842%29Pa.mp3"><span style="color: #ff9900;">၅။ ဓာတ္ႀကီး (၄၂)ပါးမွ်သာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/008%20080695E%20%2862%29Par%20Mait%20Sar%20Dait%20Di.mp3"><span style="color: #ff9900;">၆။ (၆၂)ပါးေသာ မိစ ၦာဒိ႒ိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/004%20090695M%20Bat%20Tay%20Ka%20Rat%20Ta%20Thot.mp3"><span style="color: #ff9900;">၇။ ဘေဒၵကရတၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/009%20090695E%20Thon%20Nya%20Ta%20Sait.mp3"><span style="color: #ff9900;">၈။ သုညတဆိုက္ေအာင္ရႈပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/005%20100695M%20Pyin%20Sin%20Gi%20Ga%20Mag.mp3"><span style="color: #ff9900;">၉။ ပဥၨဂီ ၤကမဂ္ႏွင့္ အ႒ဂီ ၤကမဂ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1995%205%20Days/010%20100695E%20Ta%20Nyar%20Thin%20Kha%20Ya%20Thot.mp3"><span style="color: #ff9900;">၁၀။ တဏွာ သခၤယသုတ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၃)</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/01%20190997%20Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20Ne%20Kan%20Ma%20Ba%20Wa.mp3"><span style="color: #ff9900;">၁။ ပဋိစၥသမုပၸါဒ္ႏွင့္ ကမၼဘဝရွင္းတမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/02%20200997%20Eain%20Da%20Yay%20%285%29Par.mp3"><span style="color: #ff9900;">၂။ ဣေျႏ (၅)ပါး အင္အားညီမွ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/03%20210997%20Bat%20Tay%20Ka%20Rat%20Ta%20Thot.mp3"><span style="color: #ff9900;">၃။ ဘေဒၵကရတၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/04%20220997%20Pyin%20Sin%20Gi%20Ga%20Mag.mp3"><span style="color: #ff9900;">၄။ ပဥၨဂီ ၤကမဂ္ႏွင့္ အ႒ဂီ ၤကမဂ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/05%20230997%20Kan%20%284%29%20Myo.mp3"><span style="color: #ff9900;">၅။ ကံ (၄)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/06%20240997%20Kar%20Yar%20Nupasana.mp3"><span style="color: #ff9900;">၆။ ကာယာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/07%20250997%20Wai%20Da%20Na%20Nupasana.mp3"><span style="color: #ff9900;">၇။ ေဝဒနာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/08%20260997%20Saik%20Tar%20Nupasana.mp3"><span style="color: #ff9900;">၈။ စိတၱာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/09%20270997%20Da%20Mar%20Nupasana.mp3"><span style="color: #ff9900;">၉။ ဓမၼာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/1997%20%207%20Days/10%20280997%20Wi%20Thot%20Di%20%287%29%20Par.mp3"><span style="color: #ff9900;">၁၀။ ဝိသုဒၶိ(၇)ပါး</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၄)</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/001%20Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20A%20Khay%20Khan%282%29.mp3"><span style="color: #ff9900;">၁။ ပဋိစၥသမုပၸါဒ္အေျခခံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/002%20%20Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20Pon%20San%20Pya.mp3"><span style="color: #ff9900;">၂။ ပဋိစၥသမုပၸါဒ္ပံုစံျပ ဒိ႒ိျဖဳတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/003%20Yoap%20Nan%20Khwel.mp3"><span style="color: #ff9900;">၃။ ရုပ္နာမ္ခြဲ ပညတ္ပရမတ္ခြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/004%20%2862%29Par%20Mait%20Sar%20Dait%20Di.mp3"><span style="color: #ff9900;">၄။ (၆၂)ပါးေသာ မိစ ၦာဒိ႒ိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/005%20A%20Tait%20Kan%20Swan.mp3"><span style="color: #ff9900;">၅။ အတိတ္ကံအစြမ္းေၾကာင့္ ျဖစ္ေပၚလာပံု</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/006%20Char%20Lae%20Du%20Kha.mp3"><span style="color: #ff9900;">၆။ ခ်ာလညဒုကၡေရာက္၊ ကမၼဘဝရွင္းတမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/007%20Tha%20Mar%20Dait%20Thit%285%29Myo.mp3"><span style="color: #ff9900;">၇။ သမၼာဒိ႒ိ (၅)မ်ဳိး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/008%20A%20Soon%20%282%29%20Phat.mp3"><span style="color: #ff9900;">၈။ အစြန္းႏွစ္ဘက္ မကပ္ပါမွ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/009%20Kan%20%284%29%20Myo.mp3"><span style="color: #ff9900;">၉။ ကံ (၄)မ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/010%20Ta%20Nyar%20Thin%20Kha%20Ya%20Thot.mp3"><span style="color: #ff9900;">၁၀။ တဏွာသခၤယသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/011%20Bat%20Tay%20Ka%20Rat%20Ta%20Thot.mp3"><span style="color: #ff9900;">၁၁။ ဘေဒၵကရတၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/012%20Phit%20Pyat%20Myin%20Tae%20Vipasana%20Nyan.mp3"><span style="color: #ff9900;">၁၂။ ျဖစ္ပ်က္ျမင္တဲ့ ဝိပႆ နာဥာဏ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/013%20Bat%20Tay%20Ka%20Rat%20Ta%20Thot.mp3"><span style="color: #ff9900;">၁၃။ ဘေဒၵကရတၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/014%20Wi%20Thot%20Di%20%287%29%20Par.mp3"><span style="color: #ff9900;">၁၄။ ဝိသုဒၶိ(၇)ပါး ၊ ရထား (၇)စင္းဥပမာျပ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/015%20Eain%20Da%20Yi%20Ra%20Bar%20Wa%20Nar.mp3"><span style="color: #ff9900;">၁၅။ ဣေျႏၵလံုၿခံဳေစနညး္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/016%20Thon%20Nya%20Ta%20Sait.mp3"><span style="color: #ff9900;">၁၆။ သုတဆိုက္ေအာင္ရႈပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/017%20Phat%20Khu%20Na.mp3"><span style="color: #ff9900;">၁၇။ ဖဂၢဳနရဟန္း (ေသနည္းသင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%281%29/018%20Ar%20Tha%20Wal%20%284%29%20Par%20Kon%20Kyaung.mp3"><span style="color: #ff9900;">၁၈။ အာသေဝါ(၄)ပါးကုန္ေၾကာင္း</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၅)</span></h5>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/21.mp3"><span style="color: #ff9900;">၁။ ပဋိစၥသမုပၸါဒ္အေျခခံႏွင့္ ကမၼဘဝရွင္းတမ္း (၂)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/22.mp3"><span style="color: #ff9900;">၂။ ဣေျႏၵငါးပါးအင္အားညီမွ တရားေတာ္</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/23.mp3"><span style="color: #ff9900;">၃။ ဘေဒၵကရတၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/24.mp3"><span style="color: #ff9900;">၄။ ပဥၨဂီ ၤကမဂ္ႏွင့္ အ႒ဂီ ၤကမဂ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/25.mp3"><span style="color: #ff9900;">၅။ ကံေလးမ်ဳိး တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/26.mp3"><span style="color: #ff9900;">၆။ ကာယာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/27.mp3"><span style="color: #ff9900;">၇။ ေဝဒနာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/28.mp3"><span style="color: #ff9900;">၈။ စိတၱာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/29.mp3"><span style="color: #ff9900;">၉။ ဓမၼာႏုပႆ နာသတိပ႒ာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/210.mp3"><span style="color: #ff9900;">၁၀။ ဝိသုဒၶိ(၇)ပါး ရထား(၇)စီး ဥပမာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/211.mp3"><span style="color: #ff9900;">၁၁။ သီလဝႏ ၱသုတ္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/212.mp3"><span style="color: #ff9900;">၁၂။ ဝါသိဇဋသုတ္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/213.mp3"><span style="color: #ff9900;">၁၃။ အစြန္းႏွစ္ဖက္ သို႔ မကပ္ပါမွ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/214.mp3"><span style="color: #ff9900;">၁၄။ သခၤတမွ အသခၤတသို႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/PaYateKyi%20%281%29.mp3"><span style="color: #ff9900;">၁၅။ ပရိတ္ႀကီး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20%282%29/PaYateKyi%20%282%29.mp3"><span style="color: #ff9900;">၁၆။ ပရိတ္ႀကီး (၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၆)</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/3%20Mistakes.mp3"><span style="color: #ff9900;">၁။ အမွား (၃)ခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/9%20Days.mp3"><span style="color: #ff9900;">၂။ ၉ ရက္ေျမာက္ေသာေန႔</span></a></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/070898%20About%20MyitTar.mp3"><span style="color: #ff9900;">၃။ ေမတၱာအေၾကာင္း (၇.၈.၉၈)</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/100694%20PyinSeinGiKa%20Mag.mp3"><span style="color: #ff9900;">၄။ ပဥၥဂိ ၤကမဂ္ (၁၀.၆.၉၄)</span></a></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/110390%20E%20Kam%204%20Myo.mp3"><span style="color: #ff9900;">၅။ ကံေလးမ်ဳိး (၁၁.၃.၉၀)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/120694%20E%20KaMaGone%205%20Par.mp3"><span style="color: #ff9900;">၆။ ကာမဂုဏ္ (၅)ပါး (၁၂.၆.၉၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/120696%20M%20EainDray%205%20Par.mp3"><span style="color: #ff9900;">၇။ ဣေျႏၵငါးပါး (၁၂.၆.၉၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/220789%20AhNatTa%20LakKhaNar%20Toke.mp3"><span style="color: #ff9900;">၈။ အနတၱလကၡဏသုတ္ (၂၂.၇.၈၉)</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/About%20Buddha.mp3"><span style="color: #ff9900;">၉။ ဗုဒၶအေၾကာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/ADiPaTi%203%20Par.mp3"><span style="color: #ff9900;">၁၀။ အဓိပတိ (၃)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/AgGi%20WitSa%20Toke.mp3"><span style="color: #ff9900;">၁၁။ အဂၢိဝစ ၦသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/AwGa%20KaYaNa%20Toke.mp3"><span style="color: #ff9900;">၁၂။ ၾသဃကရဏသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/BadDayKa%20YaHta%20Toke.mp3"><span style="color: #ff9900;">၁၃။ ဘေဒၵကရတၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/DarYokeKhanDawPaMa%20Toke.mp3"><span style="color: #ff9900;">၁၄။ ဒါရုကၡေႏၶာပမသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/DayWa%20Duta%20Toke.mp3"><span style="color: #ff9900;">၁၅။ ေဒဝဒူတသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/DhaMaSetKyar.mp3"><span style="color: #ff9900;">၁၆။ ဓမၼစၾကာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/Kam%205%20Par%20&amp;%20MateSarDatHti.mp3"><span style="color: #ff9900;">၁၇။ ကံ(၅)ပါးႏွင့္ မိစ ၦာဒိ႒ိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/KanDar%205%20Par.mp3"><span style="color: #ff9900;">၁၈။ ခႏၶာ(၅)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/KaSone%20LaPyae%20Nayt.mp3"><span style="color: #ff9900;">၁၉။ ကဆုန္လျပည့္ေန႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/KhanDar%205%20Par%201.mp3"><span style="color: #ff9900;">၂၀။ ခႏၶာ(၅)ပါး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/KhanDar%205%20Par.mp3"><span style="color: #ff9900;">၂၁။ ခႏၶာ(၅)ပါး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/LawKa%203%20Par.mp3"><span style="color: #ff9900;">၂၂။ ေလာကသံုးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/MaHarThaMaYa%20Toke.mp3"><span style="color: #ff9900;">၂၃။ မဟာသမယသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/MawGaYarZa%20Monk.mp3"><span style="color: #ff9900;">၂၄။ ေမာဃရာဇရဟန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/NiLa%20WunTa%20Toke.mp3"><span style="color: #ff9900;">၂၅။ သီလဝႏ ၱသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/Nyan%203%20Myo.mp3"><span style="color: #ff9900;">၂၆။ နာမ္(၃)မ်ဳိး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/PharKhuNa%20Toke.mp3"><span style="color: #ff9900;">၂၇။ ဖဂၢဳဏသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/PonNaw%20WarDa%20Toke.mp3"><span style="color: #ff9900;">၂၈။ ပုေဏၰာဝါဒသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/PTSTMP.mp3"><span style="color: #ff9900;">၂၉။ ပဋိစၥသမုပၸါဒ္သင္တန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/RDateTa%20fire%2011.mp3"><span style="color: #ff9900;">၃၀။ အာဒိတၱမီး (၁၁)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/RYaTaNa%206%20Par.mp3"><span style="color: #ff9900;">၃၁။ အာယတန(၆)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/SaPanNaKawPaMa%20Toke.mp3"><span style="color: #ff9900;">၃၂။ ဆပၸါဏေကာပမသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/SateTar%20NuPaThaNar.mp3"><span style="color: #ff9900;">၃၃။ စိတၱာႏုပႆ နာ</span></a></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/SateTar%20NuPaThaNar1.mp3"><span style="color: #ff9900;">၃၄။ စိတၱာႏုပႆ နာ (၁)</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/TaDiPaHtan%204%20Par.mp3"><span style="color: #ff9900;">၃၅။ သတိပ႒ာန္ (၄)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/TakKaPyinNya%20Toke.mp3"><span style="color: #ff9900;">၃၆။ သကၠပညသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/TaNar%20ThinKhaYa%20Toke.mp3"><span style="color: #ff9900;">၃၇။ တဏွာသခၤယသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/TawTaPan%20InGar%207%20Par.mp3"><span style="color: #ff9900;">၃၈။ ေသာတပန္ အဂၤါ (၇)ပါး</span></a></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/TayWakeZa%20Toke.mp3"><span style="color: #ff9900;">၃၉။ ေတဝိဇၨာသုတ္</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/ThanLayKha%20Thoke.mp3"><span style="color: #ff9900;">၄၀။ သေလႅခသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/ThanMar%20DateHti.mp3"><span style="color: #ff9900;">၄၁။ သမၼာဒိ႒ိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/ThanWaTaNa%20Toke.mp3"><span style="color: #ff9900;">၄၂။ သံဝါသနသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/ThinKaTa%20Hma%20AhThinKaTa%20To.mp3"><span style="color: #ff9900;">၄၃။ သခၤတမွ အသခၤတသို႔</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/ThwTa%20NuGaTa%20Toke.mp3"><span style="color: #ff9900;">၄၄။ ေသာတႏုဂတသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/WaDaNar%20NuPaTHaNar.mp3"><span style="color: #ff9900;">၄၅။ ေဝဒနာႏုပႆ နာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/WaiDaNar%20NuPaTaNar.mp3"><span style="color: #ff9900;">၄၆။ ေဝဒနာႏုပႆ နာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/WarTi%20KaTa%20Toke.mp3"><span style="color: #ff9900;">၄၇။ ဝါသိဇဋသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/Way%20To%20Nibban.mp3"><span style="color: #ff9900;">၄၈။ နိဗၺာန္သြားလမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/WiThokDi%207%20Par.mp3"><span style="color: #ff9900;">၄၉။ ဝိသုဒၶိ (၇)ပါး</span></a></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/Yoke%20n%20Nam.mp3"><span style="color: #ff9900;">၅၀။ ရုပ္ႏွင့္နာမ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/NEW/GTT%20General/Yoke%20Nam.mp3"><span style="color: #ff9900;">၅၁။ ရုပ္နာမ္</span></a></span></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၇)</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.10-3-90%28Mng.%29.mp3"><span style="color: #ffcc00;">၁။ ၁၀.၃.၁၉၉၀ ပဋိစၥသမုပၸါဒ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.15-7-88%28Mng.%29.mp3"><span style="color: #ffcc00;">၂။ ၁၅.၇.၁၉၈၈ ေသာတာပန္ စိတ္ထား အဂၤါ (၇) ပါး</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.15-9-92.%28Nght.%29.mp3"><span style="color: #ffcc00;">၃။ ၁၅.၉.၁၉၉၂ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.17-9-92.%28Evng.%29.mp3"><span style="color: #ffcc00;">၄။ ၁၇.၉.၁၉၉၂ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.19-9-92.%20%28Nght.%29.mp3"><span style="color: #ffcc00;">၅။ ၁၉.၉.၁၉၉၂ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.19-9-92.%28Evng.%29.mp3"><span style="color: #ffcc00;">၆။ ၁၉.၉.၁၉၉၂ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.20-9-92.%28Evng.%29.mp3"><span style="color: #ffcc00;">၇။ ၂၀.၉.၁၉၉၂ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.G.Th.Ta.21-9-92.%28Evng.%29.mp3"><span style="color: #ffcc00;">၈။ ၂၁.၉.၁၉၉၂ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.Gawthita%28Karyar.Wedanar%29.mp3"><span style="color: #ffcc00;">၉။ ၉.၃.၁၉၉၆ ကာယာ ႏုပႆနာ အလုပ္ေပးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/U.Gawthita%28Seitar.Dammar%29.mp3"><span style="color: #ffcc00;">၁၀။ ၈.၃.၁၉၉၆ ဝိပႆနာ အလုပ္ေပးတရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGTh.Ta.7-5-88%28Evng.%29.mp3"><span style="color: #ffcc00;">၁၁။ ၇.၅.၁၉၈၈ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.%2814-6-96.mp3"><span style="color: #ffcc00;">၁၂။ ၁၄.၉.၁၉၉၆ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.10-4-95%28Mng.%29.mp3"><span style="color: #ffcc00;">၁၃။ ၁၀.၄.၁၉၉၅ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.10-6-96%28Nght.%7D.mp3"><span style="color: #ffcc00;">၁၄။ ၁၀.၆.၁၉၉၆ အစြန္းႏွစ္ဘက္သို႔ မကပ္ပါမွ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.11-6-97%28Evng.%29.mp3"><span style="color: #ffcc00;">၁၅။ ၁၁.၆.၁၉၉၇ ဝိပႆနာ အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.12-3-94%28Mng.%29.mp3"><span style="color: #ffcc00;">၁၆။ ၁၂.၃.၁၉၉၄ ပိဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.12-6-97-%28Evng.%29.mp3"><span style="color: #ffcc00;">၁၇။ ၁၂.၆.၁၉၉၇ ေဝဒနာ ႏုပႆနာ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.17-8-98.%28Evng.%29.mp3"><span style="color: #ffcc00;">၁၈။ ၁၇.၈.၁၉၉၈ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.18-4-94%28Evng.%7D.mp3"><span style="color: #ffcc00;">၁၉။ ၁၈.၄.၁၉၉၄ သကၠပညာသုတ္ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.25-9-96%28Nght.%29.mp3"><span style="color: #ffcc00;">၂၀။ ၁၅.၆.၁၉၉၆ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.27-9-97%28Evng.%29.mp3"><span style="color: #ffcc00;">၂၁။ ၂၇.၉.၁၉၉၇ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa.9-4-95%28Mng.%29.mp3"><span style="color: #ffcc00;">၂၂။ ၁၀.၃.၁၉၉၆ ဘေဒၵကရႆသုတ္ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/Patticcia%20mp3%201/UGThTa29-12-97.%28Mng.%29.mp3"><span style="color: #ffcc00;">၂၃။ ၂၉.၁၂.၁၉၉၇ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါးတရားေတာ္</span></a></span></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၈)</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/01-130493M.mp3"><span style="color: #ffcc00;">၁။ ၁၃.၄.၁၉၉၃ (နံနက္) ပိဋိစၥသမုပၸါဒ္အေျခခံတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/02-130493E.mp3"><span style="color: #ffcc00;">၂။ ၁၃.၄.၁၉၉၃ (ညေန) ရွည္လ်ားတဲ့ ဘဝသံသရာ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/03-140493M.mp3"><span style="color: #ffcc00;">၃။ ၁၄.၄.၁၉၉၃ (နံနက္) ပိဋိစၥသမုပၸါဒ္ ႏွင့္ ကမၼဘဝရွင္းတမ္း တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/04-140493E.mp3"><span style="color: #ffcc00;">၄။ ၁၄.၄.၁၉၉၃ (ညေန) အတိတ္ကံစြမ္းအားေၾကာင့္ ျဖစ္ေပၚလာပံု တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/05-150493M.mp3"><span style="color: #ffcc00;">၅။ ၁၅.၄.၁၉၉၃ (နံနက္) ႐ုပ္နာမ္ ခြဲ ပညတ္ ပရမတ္ ခြဲ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/06-150493E.mp3"><span style="color: #ffcc00;">၆။ ၁၅.၄.၁၉၉၃ (ညေန) တဏွာသခၤါယသုတ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/07-160493M.mp3"><span style="color: #ffcc00;">၇။ ၁၆.၄.၁၉၉၃ (နံနက္) ၆၂ – ပါးေသာ မိစာၦဒိ႒ိမ်ား တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/08-160493E.mp3"><span style="color: #ffcc00;">၈။ ၁၆.၄.၁၉၉၃ (ညေန) ဆပၸါဏေကာပမသုတ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/09-170493M.mp3"><span style="color: #ffcc00;">၉။ ၁၇.၄.၁၉၉၃ (နံနက္) သုညတဆိုက္ေအာင္ ႐ႈပါ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/10-170493E.mp3"><span style="color: #ffcc00;">၁၀။ ၁၇.၄.၁၉၉၃ (ညေန) ေတဝိဇၨသုတ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/11-180493M.mp3"><span style="color: #ffcc00;">၁၁။ ၁၈.၄.၁၉၉၃ (နံနက္) ဖဂၢဳန ရဟန္း တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%201/12-180493E.mp3"><span style="color: #ffcc00;">၁၂။ ၁၈.၄.၁၉၉၃ (ညေန) ဒါ႐ုကၡေႏၶာပမသုတ္ တရားေတာ္</span></a></span></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၉)</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/500.mp3"><span style="color: #ffcc00;">၁။ ၇.၆.၁၉၉၆ (ညေန) ႐ုပ္နာမ္ ခြဲ ပညတ္ ပရမတ္ ခြဲ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/501.mp3"><span style="color: #ffcc00;">၂။ ၈.၆.၁၉၉၆ (ညေန) သုညတ ဆိုက္ေအာင္ ႐ႈပါ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/502.mp3"><span style="color: #ffcc00;">၃။ ၉.၆.၁၉၉၆ (ညေန) ဘေဒၵကရႆသုတ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/503.mp3"><span style="color: #ffcc00;">၄။ ၁၀.၆.၁၉၉၆ (ညေန) အစြန္းႏွစ္ဖက္ သို႔ မကပ္ပါမွ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/504.mp3"><span style="color: #ffcc00;">၅။ ၆.၆.၁၉၉၆ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/505.mp3"><span style="color: #ffcc00;">၆။ ၇.၇.၁၉၈၈ ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/506.mp3"><span style="color: #ffcc00;">၇။ ၁၂.၃.၁၉၉၃ (နံနက္) အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/507.mp3"><span style="color: #ffcc00;">၈။ ၆.၃.၁၉၉၆ အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/508.mp3"><span style="color: #ffcc00;">၉။ ၂၇.၆.၁၉၈၇ အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/509.mp3"><span style="color: #ffcc00;">၁၀။ အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/510.mp3"><span style="color: #ffcc00;">၁၁။ ၁၃.၃.၁၉၉၃ (နံနက္) အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/511.mp3"><span style="color: #ffcc00;">၁၂။ ၆.၆.၁၉၉၁ (နံနက္) အလုပ္ေပး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/512.mp3"><span style="color: #ffcc00;">၁၃။ ၁၀.၆.၁၉၉၅ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/513.mp3"><span style="color: #ffcc00;">၁၄။ ၂၇.၉.၁၉၉၅ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/514.mp3"><span style="color: #ffcc00;">၁၅။ ၃၀.၉.၁၉၉၅ (ညေန) ဘေဒၵကရႆသုတ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/515.mp3"><span style="color: #ffcc00;">၁၆။ ၆.၆.၁၉၉၆ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/516.mp3"><span style="color: #ffcc00;">၁၇။ ၇.၆.၁၉၉၆ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/517.mp3"><span style="color: #ffcc00;">၁၈။ ၉.၆.၁၉၉၆ (နံနက္) ၆၂ ပါး ေသာ မိစာၦဒိ႒ိမ်ား တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/518.mp3"><span style="color: #ffcc00;">၁၉။ ၁၃.၆.၁၉၉၆ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/519.mp3"><span style="color: #ffcc00;">၂၀။ ၁၂.၆.၁၉၉၄ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/520.mp3"><span style="color: #ffcc00;">၂၁။ ဝိသုဒိၶ ၇ ပါး ရထား ၇ စင္း ဥပမာ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/521.mp3"><span style="color: #ffcc00;">၂၂။ ကံေလးမ်ိဳး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/522.mp3"><span style="color: #ffcc00;">၂၃။ ဣႏိၵယ ဘာဝနာ သုတ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%202/523.mp3"><span style="color: #ffcc00;">၂၄။ ဖဂၢဳန ရဟန္း တရားေတာ္</span></a></span></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">ဖိုင္ (၁၀)</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/01-Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20A%20Khay%20Khan.mp3"><span style="color: #ffcc00;"> ၁။ ပိဋိစၥသမုပၸါဒ္ အေျခခံ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/02-Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20Pon%20San%20Pya.mp3"><span style="color: #ffcc00;">၂။ ပိဋိစၥသမုပၸါဒ္ ပံုစံျပ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/03-Yoat%20Nan%20Khoe.mp3"><span style="color: #ffcc00;">၃။ ႐ုပ္နာမ္ အက်ိဳး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/04-%2862%29Par%20Mait%20Sar%20Dait%20Di.mp3"><span style="color: #ffcc00;">၄။ ၆၂ ပါး ေသာ မစာၦဒိ႒ိ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/05-A%20Tait%20Kan%20Swan.mp3"><span style="color: #ffcc00;">၅။ အတိတ္ကံ အစြမ္း တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/06-%20Char%20Lae%20Du%20Kha.mp3"><span style="color: #ffcc00;">၆။ အလုပ္ေပးတရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/07-Tha%20Mar%20Dait%20Thit%285%29Myo.mp3"><span style="color: #ffcc00;">၇။ သမၼာဒိ႒ိ (၅) မ်ိဳး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/08-A%20Soon%20%282%29%20Phat.mp3"><span style="color: #ffcc00;">၈။ အစြန္း ႏွစ္ဖက္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/12-Phit%20Pyat%20Myin%20Tae%20Vipasana%20Nyan.mp3"><span style="color: #ffcc00;">၉။ ျဖစ္ပ်က္ျမင္တဲ့ ဝိပႆနာဉာဏ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/18-Ar%20Tha%20Wal%20%284%29%20Par%20Kon%20Kyaung.mp3"><span style="color: #ffcc00;">၁၀။ အာသေဝါ (၄) ပါး ကုန္ခန္း တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/19-A%20Loat%20Pay%281%29.mp3"><span style="color: #ffcc00;">၁၁။ အလုပ္ေပးတရား အပိုင္း ၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/20-A%20Loat%20Pay%282%29.mp3"><span style="color: #ffcc00;">၁၂။ အလုပ္ေပးတရား အပိုင္း ၂</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/21-A%20Loat%20Pay%283%29.mp3"><span style="color: #ffcc00;">၁၃။ အလုပ္ေပးတရား အပိုင္း ၃</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/22-A%20Loat%20Pay%284%29.mp3"><span style="color: #ffcc00;">၁၄။ အလုပ္ေပးတရား အပိုင္း ၄</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/23-A%20Loat%20Pay%285%29.mp3"><span style="color: #ffcc00;">၁၅။ အလုပ္ေပးတရား အပိုင္း ၅</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/24-A%20Loat%20Pay%286%29.mp3"><span style="color: #ffcc00;">၁၆။ အလုပ္ေပးတရား အပိုင္း ၆</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/25-A%20Loat%20Pay%287%29.mp3"><span style="color: #ffcc00;">၁၇။ အလုပ္ေပးတရား အပိုင္း ၇</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/26-A%20Loat%20Pay%288%29.mp3"><span style="color: #ffcc00;">၁၈။ အလုပ္ေပးတရား အပိုင္း ၈</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/27-A%20Loat%20Pay%289%29.mp3"><span style="color: #ffcc00;">၁၉။ အလုပ္ေပးတရား အပိုင္း ၉</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/28-A%20Loat%20Pay%2810%29.mp3"><span style="color: #ffcc00;">၂၀။ အလုပ္ေပးတရား အပိုင္း ၁၀</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/29-A%20Loat%20Pay%2811%29.mp3"><span style="color: #ffcc00;">၂၁။ အလုပ္ေပးတရား အပိုင္း ၁၁</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%203/30-A%20Loat%20Pay%2812%29.mp3"><span style="color: #ffcc00;">၂၂။ အလုပ္ေပးတရား အပိုင္း ၁၂</span></a></span></p>
<h5></h5>
<h5><span style="color: #339966;">ဖိုင္ (၁၁)</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/01-060695M%20Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20AKhay%20Khan.mp3"><span style="color: #ffcc00;">၁။ ၆.၆.၁၉၉၅ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/02-060695E%20Char%20Lae%20Du%20Kha.mp3"><span style="color: #ffcc00;">၂။ ၆.၆.၁၉၉၅ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/03-070695M%20A%20Tait%20Kan%20Swan.mp3"><span style="color: #ffcc00;">၃။ ၇.၆.၁၉၉၅ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/04-070695E%20Yoat%20Nan%20Khoe.mp3"><span style="color: #ffcc00;">၄။ ၇.၆.၁၉၉၅ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/05-080695M%20Dat%20Kyi%20%2842%29Pa.mp3"><span style="color: #ffcc00;">၅။ ၈.၆.၁၉၉၅ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/06-080695E%20%2862%29Par%20Mait%20Sar%20Dait%20Di.mp3"><span style="color: #ffcc00;">၆။ ၈.၆.၁၉၉၅ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/07-090695M%20Bat%20Tay%20Ka%20Rat%20Ta%20Thot.mp3"><span style="color: #ffcc00;">၇။ ၉.၆.၁၉၉၅ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/08-090695E%20Thon%20Nya%20Ta%20Sait.mp3"><span style="color: #ffcc00;">၈။ ၉.၆.၁၉၉၅ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/09-100695M%20Pyin%20Sin%20Gi%20Ga%20Mag.mp3"><span style="color: #ffcc00;">၉။ ၁၀.၆.၁၉၉၅ (နံနက္) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/10-100695E%20Ta%20Nyar%20Thin%20Kha%20Ya%20Thot.mp3"><span style="color: #ffcc00;">၁၀။ ၁၁.၆.၁၉၉၅ (ညေန) ခႏၶာဉာဏ္ေရာက္ ဒိ႒ိျဖဳတ္ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ သစၥာေလးပါး တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/11-190997%20Pa%20Tait%20Sa%20Sa%20Mu%20Pa%20Ne%20Kan%20Ma%20Ba%20Wa.mp3"><span style="color: #ffcc00;">၁၁။ ၁၉.၉.၁၉၉၇ ပိဋိစၥသမုပၸါဒ္ ႏွင့္ ကမၼဘဝ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/12-200997%20Eain%20Da%20Yay%20%285%29Par.mp3"><span style="color: #ffcc00;">၁၂။ ၂၀.၉.၁၉၉၇ ဣေျႏၵ (၅) ပါး တရာေးတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/14-220997%20Pyin%20Sin%20Gi%20Ga%20Mag.mp3"><span style="color: #ffcc00;">၁၃။ ၂၂.၉.၁၉၉၇ ပဥၥဂႋကမဂ္ ႏွင့္ အ႒ဂႋကမဂ္ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/16-240997%20Kar%20Yar%20Nupasana.mp3"><span style="color: #ffcc00;">၁၄။ ၂၄.၉.၁၉၉၇ ကာယာ ႏုပႆနာ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/17-250997%20Wai%20Da%20Na%20Nupasana.mp3"><span style="color: #ffcc00;">၁၅။ ၂၅.၉.၁၉၉၇ ေဝဒနာ ႏုပႆနာ တရားေတာ္ </span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/18-260997%20Saik%20Tar%20Nupasana.mp3"><span style="color: #ffcc00;">၁၆။ ၂၆.၉.၁၉၉၇ စိတၳာ ႏုပႆနာ တရားေတာ္</span></a></span></p>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/SayaDaw%20U%20GawThiTa/UGTT%20mp3%20-%204/19-270997%20Da%20Mar%20Nupasana.mp3"><span style="color: #ffcc00;">၁၇။ ၂၇.၉.၁၉၉၇ ဓမၼာ ႏုပႆနာ တရားေတာ္ </span></a></span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
    
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