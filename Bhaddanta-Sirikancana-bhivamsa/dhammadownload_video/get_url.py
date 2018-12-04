from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">








<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

	
<!-- Start dhammadownload menu top and side bar -->


<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>

<div style="position: absolute; width: 479px; height: 63px; z-index: 2; left: 52px; top: 43px" id="layer22" align="center">
	<font size="6" color="#800080">
	ဘဒၵႏ ၱသီရိကၪၥနာဘိဝံသ</font></div>



<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 587px; top: 6px" id="layer23">
	<img src="images/Bhaddanta-Sirikancana-bhivamsa.gif" width="200" height="227" border="0"></div>



<div style="position: absolute; width: 186px; height: 58px; z-index: 1; left: 8px; top: 143px;" id="layer1">
       <a href="index.htm" target="_parent">
       <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
    <p></p>
</a></div><a href="index.htm" target="_parent">

</a><div style="position: absolute; width: 157px; height: 37px; z-index: 1; left: 22px; top: 154px;" id="layer2" align="center"><a href="index.htm" target="_parent">
    <font size="4">
      </font></a><font size="4"><a target="_parent" style="text-decoration: none" href="index.htm">Home Page</a>
   </font>
</div>


<div style="position: absolute; width: 186px; height: 58px; z-index: 2; left: 8px; top: 201px" id="layer3">
    <a href="AbhidhammaInEnglish.htm" target="_parent">
    <img src="images/Side-button-wt.gif" width="182" height="64" border="0">
</a></div><a href="AbhidhammaInEnglish.htm" target="_parent">

</a><div style="position: absolute; width: 160px; height: 33px; z-index: 3; left: 19px; top: 208px;" id="layer4" align="center"><a href="AbhidhammaInEnglish.htm" target="_parent">
    <font size="4">
       </font></a><font size="4"><a target="_parent" style="text-decoration: none" href="AbhidhammaInEnglish.htm">Abhidhamma in English</a>
    </font>
</div>


<div style="position: absolute; height: 58px; z-index: 4; left: 8px; top: 270px; width: 186px" id="layer5">
    <a href="AbhidhammaInMyanmar.htm" target="_parent">
    <img src="images/Side-button-wt.gif" width="182" height="64" border="0">
</a></div><a href="AbhidhammaInMyanmar.htm" target="_parent">


</a><div style="position: absolute; width: 159px; height: 32px; z-index: 5; left: 20px; top: 276px;" id="layer6" align="center"><a href="AbhidhammaInMyanmar.htm" target="_parent">
    <font size="4">
        </font></a><font size="4"><a target="_parent" style="text-decoration: none" href="AbhidhammaInMyanmar.htm">Abhidhamma in Myanmar</a>
    </font>
</div>


<div style="position: absolute; width: 186px; height: 58px; z-index: 6; left: 8px; top: 339px;" id="layer7">
    <a href="AudioInEnglish.htm" target="_parent">
     <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</a></div><a href="AudioInEnglish.htm" target="_parent">


</a><div style="position: absolute; width: 159px; height: 34px; z-index: 7; left: 20px; top: 350px;" id="layer8" align="center"><a href="AudioInEnglish.htm" target="_parent">
     <font size="4">
         </font></a><font size="4"><a target="_parent" href="AudioInEnglish.htm">Audio in English</a>
     </font>
</div>

<div style="position: absolute; width: 186px; height: 58px; z-index: 8; left: 8px; top: 398px;" id="layer9">
    <a href="AudioInMyanmar.htm" target="_parent">
     <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</a></div><a href="AudioInMyanmar.htm" target="_parent">


</a><div style="position: absolute; width: 160px; height: 33px; z-index: 9; left: 19px; top: 408px;" id="layer10" align="center"><a href="AudioInMyanmar.htm" target="_parent">
      <font size="4">
        </font></a><font size="4"><a target="_parent" style="text-decoration: none" href="AudioInMyanmar.htm">Audio in Myanmar</a>
      </font>
</div>

<div style="position: absolute; width: 186px; height: 58px; z-index: 10; left: 8px; top: 457px" id="layer11">
    <a href="VideoInEnglish.htm" target="_parent">
      <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</a></div><a href="VideoInEnglish.htm" target="_parent">

</a><div style="position: absolute; width: 156px; height: 30px; z-index: 11; left: 23px; top: 469px;" id="layer12" align="center"><a href="VideoInEnglish.htm" target="_parent">
     <font size="4">
        </font></a><font size="4"><a target="_parent" href="VideoInEnglish.htm">Video in English</a>
     </font>
</div>


<div style="position: absolute; width: 186px; height: 58px; z-index: 12; left: 8px; top: 516px" id="layer13">
    <a href="VideoInMyanmar.htm" target="_parent">
     <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</a></div><a href="VideoInMyanmar.htm" target="_parent">

</a><div style="position: absolute; width: 161px; height: 33px; z-index: 13; left: 18px; top: 527px;" id="layer14" align="center"><a href="VideoInMyanmar.htm" target="_parent">
     <font size="4"></font></a><font size="4"><a href="VideoInMyanmar.htm">Video in Myanmar </a></font>
</div>

<div style="position: absolute; width: 186px; height: 58px; z-index: 14; left: 8px; top: 575px" id="layer15">
    <a href="eBook-English.htm" target="_parent">
    <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</a></div><a href="eBook-English.htm" target="_parent">


</a><div style="position: absolute; width: 159px; height: 31px; z-index: 15; left: 19px; top: 587px;" id="layer16" align="center"><a href="eBook-English.htm" target="_parent">
    <font size="4">
    </font>
    <font size="4">
    </font></a><font size="4"><a href="eBook-English.htm">eBook in English</a></font></div>


<div style="position: absolute; width: 186px; height: 58px; z-index: 16; left: 8px; top: 634px" id="layer17">
     <a href="eBook-Myanmar.htm" target="_parent">
     <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</a></div><a href="eBook-Myanmar.htm" target="_parent">

</a><div style="position: absolute; width: 154px; height: 32px; z-index: 17; left: 22px; top: 646px;" id="layer18" align="center"><a href="eBook-Myanmar.htm" target="_parent"><font size="4">
	</font><font size="4">
	</font></a><font size="4"><a href="eBook-Myanmar.htm">eBook in Myanmar</a></font></div>

<div style="position: absolute; width: 186px; height: 58px; z-index: 18; left: 8px; top: 693px" id="layer19">
    <a href="dhammadownload-news.htm" target="_parent">
    <img style="top: 660px; height: 54px;" src="images/Side-button-wt.gif" width="182" border="0">
</a></div><a href="dhammadownload-news.htm" target="_parent">


</a><div style="position: absolute; width: 158px; height: 36px; z-index: 19; left: 22px; top: 705px;" id="layer20" align="center"><a href="dhammadownload-news.htm" target="_parent">
    <font size="4"></font></a><font size="4"><a href="dhammadownload-news.htm">NEWS
	သတင္း႑</a></font></div>


<div style="position: absolute; width: 186px; height: 58px; z-index: 1; left: 8px; top: 993px" id="layer37">
    <p style="margin-top: 3px; height: 54px;">
    <a target="_parent" href="Contribute-to-dhammadownload.htm">
    <img src="images/Side-button-wt.gif" width="182" height="64" border="0"></a><a href="Suggestion-cbox.htm" target="_parent">
    </a></p><a href="Suggestion-cbox.htm" target="_parent">
</a></div><a href="Suggestion-cbox.htm" target="_parent">


</a><div style="position: absolute; width: 186px; height: 58px; z-index: 1; left: 8px; top: 933px" id="layer35"><a href="Suggestion-cbox.htm" target="_parent">
    </a><a href="Suggestion-cbox.htm" target="_parent">
    <p style="margin-top: 3px; height: 54px;">
    <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</p>
</a></div><a href="Suggestion-cbox.htm" target="_parent">


</a><div style="position: absolute; width: 186px; height: 58px; z-index: 1; left: 8px; top: 872px;" id="layer33"><a href="Suggestion-cbox.htm" target="_parent">
    </a><p style="margin-top: 3px; height: 54px;"><a href="Suggestion-cbox.htm" target="_parent">
    </a><a target="_parent" href="contact.htm">
    <img src="images/Side-button-wt.gif" width="182" height="54" border="0"></a><a href="Suggestion-cbox.htm" target="_parent">
    </a></p><a href="Suggestion-cbox.htm" target="_parent">
</a></div><a href="Suggestion-cbox.htm" target="_parent">


</a><div style="position: absolute; width: 186px; height: 58px; z-index: 1; left: 8px; top: 811px" id="layer31"><a href="Suggestion-cbox.htm" target="_parent">
    </a><a href="usefullinks.htm" target="_parent">
    <p style="margin-top: 3px; height: 54px;">
    <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</p>
</a></div><a href="usefullinks.htm" target="_parent">


</a><div style="position: absolute; width: 186px; height: 58px; z-index: 1; left: 8px; top: 750px" id="layer27"><a href="usefullinks.htm" target="_parent"> </a><a href="live.htm" target="_parent">
    <p style="margin-top: 3px; height: 54px;">
    <img src="images/Side-button-wt.gif" width="182" height="54" border="0">
</p>
</a></div><a href="live.htm" target="_parent">


</a><div style="position: absolute; width: 146px; height: 37px; z-index: 1; left: 24px; top: 1010px;" id="layer38" align="center"><a href="live.htm" target="_parent">
    <font size="4"></font></a><font size="4"><a href="Contribute-to-dhammadownload.htm">လႈဒါန္းရန္</a></font></div>



<div style="position: absolute; width: 146px; height: 37px; z-index: 1; left: 24px; top: 946px;" id="layer36" align="center">
    <font size="4"><a href="Suggestion-cbox.htm">အႀကံျပဳခ်က္မ်ား</a></font></div>



<div style="position: absolute; width: 146px; height: 37px; z-index: 1; left: 24px; top: 886px;" id="layer34" align="center">
    <font size="4"><a href="contact.htm">Contact Us</a></font></div>



<div style="position: absolute; width: 146px; height: 37px; z-index: 1; left: 24px; top: 825px;" id="layer32" align="center">
    <font size="4"><a href="usefullinks.htm">Useful Link</a></font></div>



<div style="position: absolute; width: 146px; height: 37px; z-index: 1; left: 24px; top: 762px;" id="layer28" align="center">
    <font size="4"><a href="live.htm">LIVE Webcast</a></font></div>



<div style="position: absolute; width: 192px; height: 450px; z-index: 23; left: 9px; top: 1147px; background-color:#F3F3F3" id="layer30">
<font size="6">iPhone, iPAD </font><font size="2">ကိုအသံုးျပဳသူမ်ားသည္ 
	Mp3 မ်ားကို တိုက္ရိုက္ နာယူႏိုင္ပါသည္။ ဗီဒီယိုတရားေတာ္မ်ား အတြက္ App Store တြင္
	<font color="#FF0000">Oplayer Lite</font> (သို႕မဟုတ္) yxplayer2 Lite 
	ကို Free Download အသုံးျပဳၿပီး ၾကည္႕ရႈႏိုင္ပါသည္။
</font>
	<p><font size="2">
	တျခား Mobile Phone မ်ားအတြက္ Opera Browser ကို အသုံးျပဳႏိုင္ပါသည္။</font></p><p>
<font size="2">Android version 2.1တြင္ ျမန္မာလို မျမင္ရပါ။  Android  version 2.2 ႏွင့္ ဒီထက္ျမင့္ေသာ Android Version မ်ားပါရွိေသာ Mobile, Tablet မ်ားကို အသုံးျပဳက ျမန္မာလို ျမင္ရ ႏိုင္ပါသည္။</font></p></div>



<div style="position: absolute; width: 171px; height: 64px; z-index: 23; left: 9px; top: 1074px; " id="layer39">
<a href="https://www.facebook.com/groups/dhammadownload/?ref=br_rs#">
<img src="images/facebook-logo.gif" width="159" height="59" border="0"></a></div>
<!-- end dhammadownload menu top and side bar -->









<div style="position: absolute; width: 983px; height: 4205px; z-index: 21; left: 220px; top: 158px" id="layer24" font="" face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">တိပိဋက ေယာဆရာေတာ္ႀကီး 
									သီတင္းသံုး၍ စီမံအုပ္ခ်ဳပ္ေသာ </font>
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ရန္ကုန္တိုင္းေဒသႀကီး၊ 
									ဗဟန္းၿမိဳ႕နယ္၊ ေရတာရွည္ရပ္ကြက္၊ နႏၵဝန္လမ္း၊</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">မဟာဝိသုဒၶါရုံ(ပါဠိတကၠသိုလ္) 
									ေရႊက်င္တိုက္သစ္ ပရိယတၱိစာသင္တိုက္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">တုိက္အုပ္ဆရာေတာ္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အဂၢမဟာအေက်ာ္၊ သာသနဓဇဓမၼစရိယ၊ 
									ဝိသိ႒ ဝိနိယဝိဒူ၊</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ဝိနယပါဠိပါရဂူ၊ ပိဋကတၳယပါရဂူ၊ 
									ဒိပိဋကဓရ (ပိဋိကတ္ႏွစ္ပုံေဆာင္)၊</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">သမဏအာဇာနည္ </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">ဘဒၵႏ ၱသီရိကၪၥနာဘိဝံသ</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									☘️ ☘️ ☘️ ☘️ ☘️ ☘️ ☘️</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ေထရုပၸတၱိအက်ဥ္း</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 လူ႕ျပည္လူ႕ရြာ ဖြားျမင္လာ </p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ဆရာေတာ္ ေလာင္းလ်ာသည္ 
									မေကြးတိုင္းေဒသၾကီး၊နတ္ေမာက္ျမိဳ႕နယ္၊ 
									ထန္းပင္ကုန္းၾကီးရြာေန ခမည္းေတာ္ 
									ဦးေရႊမန္း+မယ္ေတာ္ ေဒၚတင္ျမ တို႔မွ ၁၃၂၄ 
									ခုႏွစ္၊ တပို႕တြဲ လျပည့္ေက်ာ္ (၇) ရက္ 
									၁၅-၂-၁၉၆၃ (ေသာၾကာေန႕) တြင္ ဖြားျမင္ခဲ့ပါသည္။ 
									ေမြးခ်င္း (၇) ေယာက္ ရိွရာတြင္ စတုတၳေျမာက္ 
									သားရတနာျဖစ္သည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 သာသနာေတာ္၀င္စ ရွင္သာမေဏဘ၀</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၇၇-ခုႏွစ္ တေပါင္းလဆန္း(၁၄) ရက္၊စေနေန႕တြင္ 
									ထန္းပင္ကုန္းၾကီးရြာ 
									ေအာင္ျပည့္ျငိမ္းခ်မ္းအေရွ႕ကၽြဲတဲေက်ာင္း 
									ဆရာေတာ္ဘဒၵ ႏၱေတေဇာဘာသကို ဥပဇၥ်ာယ္ျပဳလ်က္ 
									မိဘႏွစ္ပါးတို႕၏ ပစၥယာႏုဂၢဟကို ခံယုကာ 
									သာသနာေတာ္္၀င္စ ရွင္သာမေဏဘ၀သို႕ 
									ေရာက္ရိွခဲံပါသည္။ ဘြဲ ့အမည္မွာ ရွင္သိရီကဥၥန 
									ျဖစ္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 အထက္တန္းတက္လွမ္း ျမတ္ရဟန္း</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၄၅-ခုႏွစ္၊ နယုန္လဆန္း ( ၅ ) ရက္၊ 
									ဗုဒၶဟူးေန႕တြင္ ရန္ကုန္ျမိဳ႕ 
									ဗဟန္း၊နႏၵ၀န္လမ္း၊ မဟာ၀ိသုဒၶါရံု ( 
									ပါဠိတကၠသိုလ္) ေရႊက်င္တိုက္သစ္ ဒုတိယေျမာက္ 
									ပဓာနနာယက ဆရာေတာ္ ဘဒၵ ႏၱေကာ႑ည ( 
									တြဲဖက္အက်ဳိးေတာ္ေဆာင္ ႏိုင္ငံေတာ္ သံဃမဟာနာယက 
									အဖြဲ႕) ကို ဥပဇၥ်ာယ္ျပဳလ်က္ ျမိတ္ျမိဳ႕ေန 
									ဦးယံုစိုင္+ေဒၚေစာရွင္၊ နတ္ေမာက္ျမိဳ႕ေန 
									မိဘႏွစ္ပါး ၊ေတာင္စြန္းျမိဳ႕ေန 
									ဦးေက်ာ္ေရႊ+ေဒၚက်င္ေအး စေသာ ဒါယကာ 
									ဒါယိကာမမ်ား၏ ပစၥယာႏုဂၢဟခံယူကာ ျမင့္ျမတ္ေသာ 
									ရဟန္းအျဖစ္သို႕ ေရာက္ခဲ့ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 ေက်းဇူးၾကီးမား ဆရာမ်ား</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									နတ္္ေမာက္ျမိဳ႕ ထန္းပင္ကုန္းၾကီးရြာ၊ 
									ေအာင္ျပည့္ျငိမ္းခ်မ္းအေရွ႕ကၽြဲတဲေက်ာင္း 
									ဆရာေတာ္ ဘဒၵ ႏၱသူရိယ၊ဆရာေတာ္ဘဒၵ ႏၱေတေဇာဘာသ၊ 
									ထန္းပင္ကုန္းၾကီးရြာ ေျမာက္ေက်ာင္း ဆရာေတာ္ 
									ဘဒၵ ႏ ၱ ပညာေတေဇာ၊ ေက်ာက္တံခါးေက်ာင္းဆရာေတာ္ 
									ဘဒၵ ႏ ၱသာသန၊ မႏၱေလး ျမေတာင္ေက်ာင္းတိုက္ 
									ေရႊ၀ါ၀င္းဆရာေတာ္ အဘိဓဇမဟာရ႒ဂုရု ဘဒၵ ႏ 
									ၱသာသနာဘိ၀ံသ၊ မစိုးရိမ္တိုက္ေဟာင္း ဘဒၵ ႏ ၱ 
									ေကာ၀ိဒါဘိ၀ံသ ၊ မစိုးရိမ္တိုက္သစ္ ဘဒၵ ႏ 
									ၱရာဇာဓမၼာဘိ၀ံသ၊ ဘဒၵ ႏ ၱေကသရာဘိ၀ံသ ၊ 
									ျမေတာင္တိုက္ သာယာ၀င္းဆရာေတာ္ ဘဒၵ ႏ 
									ၱသာဂရာလကၤာရာဘိ၀ံသ ၊ ႏိုင္ငံေတာ္ 
									သံဃမဟာနာယကဥကၠ႒ ဗန္းေမာ္ဆရာေတာ္ ေဒါက္တာ ဘဒၵ ႏ 
									ၱကုမာရဘိ၀ံသ ၊ေတာင္စြန္း စမ္းေအးျမိဳင္ဆရာေတာ္ 
									ဘဒၵ ႏ ၱ နႏၵ၀ံသာဘိ၀ံသ ၊ရန္ကုန္ျမိဳ႕ 
									က်ဳိက္၀ိုင္းပစၦိမာရံုဆရာေတာ္ ဘဒၵ ႏ 
									ၱႏၵာ၀ုဓာဘိ၀ံသ၊ ရန္ကုန္ျမိဳ႕ ဆိပ္ကမ္းျမိဳ႕နယ္ 
									ေစတိယပါလေက်ာင္းဆရာေတာ္ ဘဒၵ ႏၱေသာဘိတ၊ 
									ဒဂံုျမိဳ႕သစ္အေရွ ႕ပိုင္း ၊တိပိဋက မဟာဂႏၶာ၀င္ 
									ေရစၾကိဳဆရာေတာ္ ဘဒၵ ႏၱ ၀ါယာမိႏၵာဘိ၀ံသ၊ဗဟန္း 
									-မဟာ၀ိသုဒၶါရံုေရႊက်င္တိုက္သစ္၊ 
									ဒုတိယေျမာက္ပဓာန နာယကဆရာေတာ္ 
									ႏိုင္ငံေတာ္သံဃမဟာနာယကအဖြဲ႕ တြဲဖက္အက်ုိးေဆာင္ 
									ဘဒၵ ႏၱ ေကာ႑ည၊ တိပိဋကဓရ ဓမၼဘ႑ာဂါရိက 
									ေယာဆရာေတာ္ ဘဒၵ ႏၱ သီရိႏၵာဘိ၀ံသ 
									စာခ်-ဒြိပိဋကေကာ၀ိဒ ဘဒၵ ႏၱ ကိတၱသာရ၊ 
									ေဒါပံုျမိဳ႕ သာသနာ့အလင္းေရာင္ဆရာေတာ္ 
									ဒီဃနိကာယေကာ၀ိဒ ဘဒၵ ႏၱေဇာတိက 
									စသည္တို႕ျဖစ္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 ေအာင္ျမင္ခဲ့ေသာ စာေမးပြဲမ်ားႏွင့္ 
									ဘြဲ႕တံဆိပ္ေတာ္မ်ား</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ႏိုင္ငံေတာ္အစိုးရ အဘိဓမၼာစာေမးပြဲ ရိုးရိုး 
									(၃) ဆင့္ ႏွစ္ခ်င္းေပါက္ ဘီးလင္းျမိဳ႕နယ္ 
									ဒုတိယ ဂုဏ္ထူးေဆာင္ ဋီကာေက်ာ္ ႏွစ္ခ်င္းေပါက္ 
									မြန္ျပည္နယ္ ဒုတိယ၊ မဟာ၀ိသုဒၶါရံု 
									ေရႊက်င္တိုက္သစ္၊ ပရိယတၱိ သဒၶမၼဟိတ 
									ဓမၼာစရိယဘြဲ႔ ၊ အစိုးရ သာသနဓဇ ဓမၼာစရိယ 
									တစ္ႏိုင္ငံလံုး ပထမ -အဂၢအေက်ာ္ဘြဲ႕ 
									၊မိုးကုတ္ျမိဳ႕ နိကာယ္သာသနာ ၾကီးပြားေရး 
									အသင္းစာေမးပြဲတြင္ 
									ပါရာဇိကဏ္/ပါစိတ္ပါဠိေတာ္ကို ပထမဂုဏ္ထူး ၊ 
									သထံုျမိဳ႕ သု၀ဏၰဘူမိ ပရိယတၱိသာသနဟိတအသင္း 
									ပိဋကတၱယပါရဂူစာေမးပြဲတြက္ သာသနာ့ေဇတိပါလ 
									ဓမၼာစရိယ ဒုတိယစာခ်ဘြဲ႕ ၊သာသနဟိတဂဏ၀ါစက အာစရိယ 
									ပထမစာခ်ဘြဲ႕ ၊သု၀ဏၰဘူမိပရိယတၱိ 
									သာသနဟိတပဥၥနိကာယဏၰ၀ 
									ပိဋကတၱပါရဂူဘြဲ႕၊နိကာယုေဇၨာတက၀ိနယဓရ 
									အဂၢဓမၼာစရိယဘြဲ႕ (ဗန္းေမာ္ဆရာေတာ္ၾကီးဆု) ၊ 
									ႏိုင္ငံေတာ္အစိုးရ နိကာယ္စာေမးပြဲ 
									၀ိသိ႒၀ိနယ၀ိဒူဘြဲ႕ ( တစ္ႏိုင္ငံလံုး ဒုတိယ) ၊ 
									၀ိနယ မဟာ၀ိဒူ၊ ပါစိတ်ာဒိ-စူဠ၀ဂၢါဒိ၊ 
									တိပိဋကဓရ-တိပိဋကေကာ၀ိဒ 
									ေရြးခ်ယ္ေရးစာေမးပြဲတြင္ ၀ိနယဓရ 
									-၀ိနယေကာ၀ိဒဘြဲ႕ ၊ဒီဃဘာဏက ဒြိပိဋိကဓရဘြဲ႕၊ ( 
									ပိဋကတ္ႏွစ္ပံုေဆာင္) တို႕ျဖစ္ပါသည္။ 
									၂၀၁၈-ခုႏွစ္၊ဇႏၷ၀ါရီလ (၄) ရက္၊ 
									လြတ္လပ္ေရးေန႕တြင္ ျမန္မာႏိုင္ငံေတာ္အစိုးရမွ 
									မဟာဂႏၱ၀ါစက ပ႑ိတ စာခ်ဘြဲ႕တံဆိပ္ေတာ္ကို 
									ဆက္ကပ္လွဴဒါန္းခဲ့ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 သာသနာေရး ေလာကေရး ေဆာင္ရြက္ခ်က္မ်ား</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ဆရာေတာ္သည္ သာသနာေရးေဆာင္ရြက္ခ်က္အားျဖင့္ 
									ဗဟန္းျမိဳ႕နယ္ ၀ိနည္းဓိုရ္၊ ရန္ကုန္တိုင္း 
									၀ိနည္းဓိုရ္၊ ရန္ကုန္တိုင္း 
									သံဃနာယကအဖြဲ႕၀င္(ေရႊက်င္)၊ ႏိုင္ငံေတာ္ 
									ဗဟိုသံဃ၀န္ေဆာင္၊ ႏိုင္ငံေတာ္ ၀ိနည္းဓိုရ္၊ 
									ေရႊက်င္နိကာယဂိုဏ္းလံုး၀န္ေဆာင္ နာယကတာ၀န္၊ 
									ေရႊက်င္နိကာယ ဂိုဏ္းလံုးကၽြတ္အစည္းအေ၀းၾကီး၌ 
									အက်ဳိးေဆာင္ အခမ္းအနားမွဴးတာ၀န္၊ 
									ေဒါက္တာခင္ခင္ရီ ပရဟိတေဖာင္ေဒးရွင္း နာယက၊ 
									ျပည္ေထာင္စု သမၼတ ျမန္မာႏိုင္ငံေတာ္ 
									ဓမၼစကူးလ္ေဖာင္ေဒးရွင္း ဗဟိုဥကၠ႒၊ 
									ျမန္မာႏိုင္ငံလံုးဆိုင္ရာ 
									ယဥ္ေက်းလိမၼာျပန္႕ပြားေရး ဗဟိုအဖြဲၾသ၀ါဒ စရိယ၊ 
									ျမန္မာႏိုင္ငံလံုးဆိုင္ရာ ၀ိနယ၀ံသပါလ အသင္း၊ 
									ပဓာနဦးေဆာင္နာယက တာ၀န္မ်ားအျပင္ ဇာတိျဖစ္ေသာ 
									နတ္ေမာက္ျမိဳ႕နယ္ ထန္းပင္ကုန္းၾကီးရြာ၌ 
									သဒၶမၼပီတိသႏၱိသုခအသင္းၾကီး ကိုဖြဲ ့စည္းျပီး 
									ေရွးေဟာင္းဘုရားမ်ား ျပဳျပင္ျခင္း 
									၊ေက်းရြာမူလတန္းေက်ာင္းကို မူလတန္းလြန္ေက်ာင္း 
									တြဲဘက္အလယ္တန္းေက်ာင္း၊အလယ္တန္းေက်ာင္း၊ 
									ယခုအခါ အထက္တန္းေက်ာင္းခြဲျဖစ္ေအာင္ 
									ကုညီပန္႕ပိုးေပးျခင္း၊ သၾကၤန္တြင္းကာလ၌ 
									ရြာသူရြာသားမ်ား 
									ကုသိုလ္တိုးပြားအပါယ္မလားရေအာင္ 
									ရဟန္းခံ၊ရွင္ျပဳ၊သီလရွင္၀တ္ေပးျပီး ၇ -ရက္ 
									တရားစခန္းပြဲမ်ားကို (၈)ၾကိမ္ေရာက္လာသည္အထိ 
									ႏွစ္စဥ္ ျပဳလုပ္ေပးျခင္း စသည္တို႕ကို 
									ေဆာင္ရြက္လ်က္ရိွပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									အထူးအားျဖင့္ ၂၀၁၂-ခုႏွစ္မွစ၍ 
									ေက်းရြာအသီးသီးရိွ ေလာကီအတန္းစာမ်ား 
									သင္ၾကားေနရေသာ ရွင္သာမေဏမ်ားအတြက္ 
									ယဥ္ေက်းလိမၼာမႈ ႏွင့္ ေလာကုတၱရာအပိုင္းအတြက္ 
									အေထာက္အပံ့ျဖစ္ေအာင္ ေက်ာင္းသား၊ ေက်ာင္းသူ ၊ 
									အရပ္သား အရပ္သူမ်ား အတြက္လည္း 
									ယဥ္ေက်းလိမၼာအသိပညာ ျပည့္၀သူမ်ားျဖစ္ေအာင္ 
									ရည္ရြယ္ျပီး ပရိယတၱိအေျချပဳ ဗုဒၶသာသနာ 
									ယဥ္ေက်းမႈ ႏႈတ္ေျဖ ေရးေျဖ စာေမးပြဲၾကီးကို 
									က်င္းပေပးလ်က္ရိွရာ ၂၀၁၂-ခုႏွစ္တြင္ ၄၂၆ ဦး၊ 
									၂၀၁၃ ခုႏွစ္တြင္ ၇၁၇ ဦး၊၂၀၁၄ ခုႏွစ္တြင္ ၈၃၃ 
									ဦး၊၂၀၁၅ ခုႏွစ္တြင္ ၉၉၁ ဦး၊ ၂၀၁၆ ခုႏွစ္တြင္ 
									၁၀၀၆ ဦး၊ ၂၀၁၇ ခုႏွစ္တြင္ ၁၀၇၅ ဦး၊ ၂၀၁၈ 
									ခုႏွစ္တြင္ ၁၀၉၆ ဦး ေျဖဆိုခဲ့သည္။ 
									(၇)ႏွစ္တာအတြင္း စုစုေပါင္း ( ၆၁၄၄) ဦး 
									ေျဖဆို၍ (၅၂၈၀ ) ဦးေအာင္ျမင္ခဲ့ပါသည္။ 
									ရွင္သာမေဏ မ်ားအတြက္ ပဗၺဇၨဓမၼ၀ိနယတန္း၌ 
									သံုးဆင့္ သတ္မွတ္ျပီး တစ္ဆင့္ တစ္ဆင့္၌ 
									သံုးဘာသာစီပါ၀င္ျပီး ႏွစ္စဥ္ေမလ၌ 
									စာေမးပြဲက်င္းပပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ျမန္မာႏိုင္ငံသားအားလံုး ယဥ္ေက်းလိမၼာ၍ အသိပညာ 
									ဥာဏ္ရည္ဥာဏ္ေသြးမ်ား ျပည့္၀သူမ်ားျဖစ္ေစရန္ 
									အနာဂတ္မ်ဳိးဆက္သစ္မ်ားကိုလည္း ယဥ္ေက်းလိမၼာ၍ 
									အသိပညာ ဥာဏ္ရည္ဥာဏ္ေသြး ျပည့္၀သူမ်ားျဖစ္ေစရန္ 
									ႏိုင္ငံႏွင့္ လူမ်ဳိး ဘာသာ သာသနာကို 
									အသိပညာပါေသာ ယံုၾကည္မႈျဖင့္ ေစာင့္ေရွာက္ေသာ 
									အမ်ဳိးသားေကာင္းသား၊ 
									အမ်ဳိးသမီးေကာင္းသမီးမ်ားျဖစ္ေစရန္ ရည္သန္လ်က္ 
									ေဆာင္ရြက္ေပးေနျခင္းျဖစ္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 ေအးျမရႊင္ျပံဳး သီတင္းသံုး</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ယခုအခါ ဆရာေတာ္သည္ ရန္ကုန္တိုင္းေဒသၾကီး၊ 
									ဗဟန္းျမိဳ႕နယ္၊ နႏၵ၀န္လမ္း၊မဟာ၀ိသုဒၶါရံု ( 
									ပါဠိတကၠသိုလ္ ) ေရႊက်င္တိုက္သစ္၌ 
									တိုက္အုပ္ဆရာေတာ္အျဖစ္ စာေပပို႕ခ် 
									သံဃာ့ေ၀ယ်ာ၀စၥေဆာင္ရြက္ စသည္ျဖင့္ 
									သာသနာ့တာ၀န္မ်ား ထမ္းေဆာင္လ်က္ရိွပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									🌺 ၾသ၀ါဒ "ယဥ္ေက်းမွ ေလာကလူသံုးေဆာင္”</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ေကာင္းသည့္ အလုပ္၊ငါလုပ္ေဆာင္သည္၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									မေကာင္းအလုပ္၊ ေနာက္ဆုတ္ေနမည္၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									စိတ္ျဖဴႏႈတ္ေကာင္း၊ကိုယ္ေကာင္းေစမည္၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									တစ္ကိုယ္ေကာင္း၊ အေကာင္းမ်ားေစမည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									အခ်ိန္ဇယား၊ ဆြဲထားလုပ္ေဆာင္၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									အခ်ိန္မွီသံုး၊ အျဖံဳးကိုေရွာင္၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ကိုယ္ႏႈတ္ယဥ္ေက်း၊ညႊန္ေပးနားေထာင္၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ယဥ္ေက်းမွ ေလာကလူ သံုးေဆာင္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									စာတက္ စိတ္ေကာင္း၊ မိတ္ေကာင္းရိွေစ၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ကိုယ္လည္းလူေကာင္း၊ မိတ္ေကာင္းျဖစ္ေစ၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									သီလအ၀တ္၊ေန႕တိုင္း၀တ္ေလ၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ပညာျမတ္၊ ေခါင္းတင္ ေမာင္းႏွင္ေလ။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ဗဟုသုတ၊ရွာၾကပါေလ၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									အဆိပ္ ေဆး၀ါး၊ခြဲျခားရွာေလ၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ဆရာ-မိဘဈ နိစၥရိုေသ၊</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									သူေတာ္ေကာင္း ရိပ္ေကာင္းရိွပါေစ။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ကိုယ္လွ သူလွ ဘ၀လွ ၊ အလွတူေစခ်င္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ကိုယ္ရ သူရ လိုတာရ အရတူေစခ်င္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ကိုယ္ေကာင္း သူေကာင္း၊ အက်င့္ေကာင္း၊ 
									အေကာင္းတူေစခ်င္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									☘️ ☘️ ☘️ ☘️ ☘️ ☘️ ☘️</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5" face="Zawgyi-One">သင္ႀကားပို႕ခ်ေသာ 
									တရားေတာ္မ်ား </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-04-26.mp4">
									၂၆-၄-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-04-27.mp4">
									၂၇-၄-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-04-28.mp4">
									၂၈-၄-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၃) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-04-29.mp4">
									၂၉-၄-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၄) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-04-30.mp4">
									၃၀-၄-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၅) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-01.mp4">
									၁-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၆) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-02.mp4">
									၂-၅-၂၀၁၅ ဗုဒၶေအာင္ပြဲ ကိုယ့္ေအာင္ပြဲ 
									တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-03.mp4">
									၃-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၇) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-04.mp4">
									၄-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၈) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-05.mp4">
									၅-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၉) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-06.mp4">
									၆-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၁၀) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-07.mp4">
									၇-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၁၁) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-08.mp4">
									၈-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၁၂) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-09.mp4">
									၉-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၁၃) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-10.mp4">
									၁၀-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁၄) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-11.mp4">
									၁၁-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁၅) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-12.mp4">
									၁၂-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁၆) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-13.mp4">
									၁၃-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁၇) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-14.mp4">
									၁၄-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁၈) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-15.mp4">
									၁၅-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၁၉) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-16.mp4">
									၁၆-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂၀) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-17.mp4">
									၁၇-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂၁) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-27.mp4">
									၂၇-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂၂) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-28.mp4">
									၂၈-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂၃) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-29.mp4">
									၂၉-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂၅) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-05-30.mp4">
									၃၀-၅-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ 
									ဓမၼဂုဏ္ျပ ဘဝပန္းခ်ီ အပိုင္း(၂၇) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-06-01.mp4">
									၁-၆-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၂၇) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-06-02.mp4">
									၂-၆-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၂၈) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2015-06-03.mp4">
									၃-၆-၂၀၁၅ ဧတဒဂ္ဘြဲ႔ခံ ဆုထူးပန္တို႕၏ ဓမၼဂုဏ္ျပ 
									ဘဝပန္းခ်ီ အပိုင္း(၂၉) တရားေတာ္</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									သီရိမဂၤလာလမ္း ေအာင္ခ်မ္းသာရပ္ကြက္ 
									ကံျမင့္ေက်ာင္းတိုက္ဓမၼာရုံ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ဗုဒၶေဟာၾကား ငါးရာငါးဆယ္ ဇာတ္ေတာ္မ်ား အစီအစဥ္</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-01-introduction.mp4">၁-၈-၂၀၁၈ ဗုဒၶေဟာၾကား ငါးရာငါးဆယ္ 
									ဇာတ္ေတာ္မ်ား အစီအစဥ္ နိဒါန္း</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-01.mp4">၁-၈-၂၀၁၈ ငါးရာငါးဆယ္ 
									အပိုင္း(၁) အပဏၰကဇာတ္ေတာ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-02.mp4">၂-၈-၂၀၁၈ ငါးရာငါးဆယ္ အပိုင္း(၂) - (၂) ဝဏၰပထဇာတ္၊ 
ေသရိဝဇာတ္</a></p>
								<p class="MsoTagline" style="text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-03.mp4">၃-၈-၂၀၁၈ ငါးရာငါးဆယ္ အပိုင္း(၃) - (၄)စူလေသ႒ိဇာတ္၊ 
(၅)တ႑ဳလနာဠိဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-04.mp4">၄-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၄) - (၆)ေဒဝဓမၼဇာတ္၊ (၇) 
က႒ဝါဟနဇာတ္၊(၈) ဂါမဏိဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-05.mp4">၅-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၅) - (၉) မဃေဒဝဇာတ္၊ (၁၀) 
သုခဝိဟာရီဇာတ္၊ (၁၁) လကၡဏမိဂဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-06.mp4">၆-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၆) - (၁၂)နိေျဂာဓဇာတ္၊ (၁၃) 
က႑ိဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-07.mp4">၇-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၇) - (၁၄) ဝါတမိဂဇာတ္၊ 
(၁၅)ခရာဒိယဇာတ္၊ (၁၆) တိပလႅတၳဇာတ္၊ (၁၇) မာလုတဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-08.mp4">၈-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၈) - (၁၉)အာယာစိတဘတၲ၊ 
(၂၀)နဠပါနဇာတ္၊ (၂၁)ကုရုဂၤမိဂဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-09.mp4">၉-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၉) - (၂၂) ကုကၠရဇာတ္ေတာ္၊ 
(၂၃) ေဘာဇာဇာနိယဇာတ္၊ (၂၄) အာဇညဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
(break) 
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-10.mp4">၁၀-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၀) - (၂၅) 
တိတၳဇာတ္၊ (၂၆) မဟိဠာမုခဇာတ္၊ (၂၇) အဘိဏွဇာတ္
</a> </p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-11.mp4">၁၁-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၁) - (၂၈) နႏၵိဝိသာလဇာတ္၊ 
(၂၉)ကဏွဇာတ္၊ (၃၀)မုနိကဇာတ္ 
</a> </p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-12.mp4">၁၂-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၂) - (၃၁)ကုလာဝကဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-13.mp4">၁၃-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၃) - (၃၂)နစၥဇာတ္၊ (၃၃) 
သေမၼာဒမာနဇာတ္၊ (၃၄) မစၧဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-14.mp4">၁၄-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၄) - (၃၅) ဝဋၬကဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-15.mp4">၁၅-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၅) - (၃၆)သကုဏဇာတ္၊ 
(၃၇)တိတိၱရဇာတ္၊ (၃၈)ဗကဇာတ္၊ (၃၉)နႏၵဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
(break) 
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-16.mp4">၁၆-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၆) - 
(၄၀)ခဒိရဂၤါရဇာတ္၊ (၄၁)ေလာသကဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-17.mp4">၁၇-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၇) - (၄၁)ေလာသကဇာတ္၊ 
(၄၂)ကေပါတဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-18.mp4">၁၈-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၈) - (၄၃)ေဝဠဳကဇာတ္၊ 
(၄၄)မကသဇာတ္၊ (၄၅)ေရာဟိဏီဇာတ္၊ (၄၆)အာရာမဒူသကဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-19.mp4">၁၉-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၁၉) - (၄၇)ဝါရုဏိဒူသကဇာတ္၊ 
(၄၈)ေဝဒဗၺဇာတ္ 
</a> </p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-20.mp4">၂၀-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၀) -&nbsp; 
(၄၉)နကၡတၱဇာတ္၊ (၅၀)ဒုေမၼဓဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-21.mp4">၂၁-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၁) - (၅၁)မဟာသီလဝဇာတ္၊ 
(၅၂)စူဠဇနကဇာတ္ 
</a> </p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-22.mp4">၂၂-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၂) -&nbsp; 
(၅၃)ပုဏၰပါတိဇာတ္၊ (၅၄)ကိ ံဖလဇာတ္၊ (၅၅)ပဥၥာဝုဓဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-23.mp4">၂၃-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၃) -&nbsp; 
(၅၆)ကဥၥနကၡႏၶဇာတ္၊ (၅၇)ဝါနရိႏၵဇာတ္၊ (၅၈)တေယာဓမၼဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-26.mp4">၂၆-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၄) - (၅၉)ေဘရိဝါဒကဇာတ္၊ 
(၆၀)သခၤဓမၼဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-27.mp4">၂၇-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၅) - (၆၁)အသာတမႏၱဇာတ္၊ 
(၆၂)အ႑ဘူတဇာတ္၊ (၆၃)တကၠပ႑ိတဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-29.mp4">၂၉-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၆) -&nbsp; 
(၆၄)ဒုရာဇာနဇာတ္၊ (၆၅)အနဘိရတိဇာတ္၊ (၆၆)မုဒုလကၡဏဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-08-30.mp4">၃၀-၈-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၇) -&nbsp; 
(၆၇)ဥစၦဂၤဇာတ္၊ (၆၈)သာေကတဇာတ္၊ (၆၉)ဝိသဝႏၱဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/Bhaddanta-Sirikancana-bhivamsa/Bhaddanta-Sirikancana-bhivamsa-2018-09-01.mp4">၁-၉-၂၀၁၈ ငါးရာငါးဆယ္&nbsp; အပိုင္း(၂၈) -&nbsp; 
(၇၀)ကုဒၵါလဇာတ္၊ (၇၁)ဝရုဏဇာတ္၊ (၇၂)သီလဝနာဂရာဇဇာတ္</a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p>&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p>&nbsp;</p></div>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>




<!-- Start Quantcast tag -->
<script type="text/javascript">
_qoptions={
qacct:"p-70zUvF4huN4OU"
};
</script>
<script type="text/javascript" src="http://edge.quantserve.com/quant.js"></script>
<noscript>
<img src="http://pixel.quantserve.com/pixel/p-70zUvF4huN4OU.gif" style="display: none;" border="0" height="1" width="1" alt="Quantcast"/>
</noscript>
<!-- End Quantcast tag -->
</font>



<font face="Zawgyi-One">






</font>
"""

soup = bs4(text, 'html.parser')

count = 1
with open('titles_links.txt', 'w') as f:
    
    for key in soup.find_all('a'):
        if ".mp4" in key.get('href'):
            counter = '{:03d}'.format(count)
            print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())
            
            count += 1        
    
