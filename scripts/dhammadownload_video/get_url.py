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
	
<div style="position: absolute; width: 506px; height: 53px; z-index: 2; left: 52px; top: 45px;" id="layer22" align="center">
	<font size="5" color="#800080">ဘဒၵႏ ၱဝိသုတ</font></div>
	
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 545px; top: 12px;" id="layer23">
	<img src="images/mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta.gif" width="279" height="348" border="0"></div>
	
	

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




	
	
<div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 219px; top: 156px" id="layer24" font="" face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
									&nbsp;</p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
									<font size="4" face="Zawgyi-One">
									<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font></p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
								မႏ ၱေလး၊ ရန္ကင္းေတာင္ ေလးကၽြန္းမာရ္ေအာင္ 
								သာမေဏေက်ာ္ စာသင္တိုက္၊ </p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
								<font size="6">ပဓာနာယက ဆရာေတာ္ ဘဒၵႏ ၱဝိသုတ
								</font></p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
								သာသန ဓဇဓမၼာစရိယ၊ ဝိနယ ဝိဒူ၊ ဒီဃနိကာယဝိဒူ၊ 
								ယမိုက္ပ႒ာန္း အထူးသင္တန္းနည္းျပ</p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">&nbsp;</p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
								၀၉-၄၃၁၉၇၁၇၆</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								~~~~~~~~~~<br>
								ဆရာေတာ္၏ ေထရုပတၱိအက်ဥ္းခ်ဳပ္၊<br>
								~~~~~~~~~~<br>
								မႏ ၱေလး ရန္ကင္းေတာင္ ေလးကၽြန္မာန္ေအာင္ 
								သာမေဏေက်ာ္၊ စာသင္တိုက္၊ မဓာန နာယက၊ ယမိုက္ပ႒ာန္း 
								အထူးသင္တန္း နည္းျပ၊ ဆရာေတာ္ ဘဒၵႏ ၱဝိသုတ ၏ 
								ေထရုပတၱိအက်ဥ္းခ်ဳပ္၊</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<br>
								ေမြးရပ္ခ်က္ေႂကြ ဇာတိေျမ<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								ဆရာေတာ္ ဘဒၵႏ ၱဝိသုတသည္ စစ္ကိုင္းတိုင္းေဒသႀကီး 
								ယင္းမာပင္ခရိုင္ ပုလဲၿမိဳ႕နယ္၊ သင္တီးကန္ရြာ၊ 
								ဖခမည္းေတာ္ ဦးပြ + မယ္ေတာ္ ေဒၚပဲတို႕မွ ၁၃၂၅ 
								ခုႏွစ္ တပို႕တြဲလဆန္း (၉)ရက္၊ ဗုဒၶဟူးေန႕တြင္ 
								မီးရႈးသန္႕စင္ ဖြားျမင္ေတာ္မူပါသည္။ ေမြးခ်င္း ၆ 
								ေယာက္ ရွိသည္႕အနက္ ဒုတိယေျမာက္ သားရတနာျဖစ္ပါသည္။ 
								ေနာင္ေတာ္ အႀကီးဆုံးမွာ စာေရးဆရာအေသာက (မုံရြာ) 
								ျဖစ္ၿပီး ညီငယ္မွာ အရွင္စေႏၵာေလာက (သာသနဓဇ 
								ဓမမာစရိယ၊ သာသနတကၠသီလဓမၼာစရိယ (ဘီေအ) 
								ပရိယတတသာသနပါလ ဓမၼာစရိယ၊ 
								မိုးကုတ္ဝိပႆနာနယ္လွည္ဓမၼကထိက၊ ေလးကၽြန္းမာန္ေအာင္ 
								သာမေဏေက်ာ္ စာသင္တိုက္ စာခ်ကထိက တိုက္အုပ္ 
								နာယကဆရာေတာ္ ျဖစ္သည္။ က်န္ (၃) ေယာက္မွာ 
								မတင္ျမင့္၊ ကိုျမင့္ဟန္၊ ကိုျမင့္ေရႊတို႕ 
								ျဖစ္ၾကပါသည္။</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<br>
								ရွင္သာမေဏျပဳျခင္း<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								ေက်ာင္းေနခ်ိန္ အသက္ (၈) ႏွစ္သား အရြယ္အေရာက္တြင္ 
								ပုလဲၿမိဳ႕နယ္ မု့ႀကိဳင္းရြာ ေတာရေက်ာင္း ဆရာေတာ္ 
								ဦးဇဝနထံေတာ္မွာ ျမန္မာသင္ပုန္းႀကီးႏွင့္ 
								ပါဠိျမန္မာ အေျခခံဖတ္စာ၊ ပရိတ္ႀကီး (၁၁)သုတ္၊ 
								ဂဏန္းသခ်ၤာ၊ ေဗဒင္လကၡဏာ ပညာရပ္မ်ားကို သင္ယူၿပီး 
								အသက္(၁၂)ႏွစ္ အရြယ္ အေရာက္ ေကာဇာသကၠရာဇ္ 
								၁၃၃၆-ခုႏွစ္၊ သီကၽြတ္လတြင္ 
								မုံႀကိဳင္းေတာရေက်ာင္းဆရာေတာ္ထံ၌ ဘႀကီးဦးထြန္းတင္ 
								အေမႀကီး ေဒၚဖြားယူ မိသားစုတို႕၏ ပစၥယာႏုဂၢဟျဖင့္ 
								ရွင္သာမေဏဝတ္ကာ သာသနာ့ေဘာင္သို႕ ဝင္ေရာက္ခဲ့ပါသည္။<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								ရဟန္းခံ မဂၤလာ<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၁၃၄၅ ခုႏွစ္၊ ကဆုန္လျပည္႕ေန႕တြင္ မုံရြာၿမိဳ႕၊ 
								မဟာေဇာတိကရာမ ပါဠိတကၠသိုလ္ ေက်ာင္းတိုက္ 
								သာသနာ့ေသာဘိနီသိမ္ေတာ္အတြင္းမွာ တိုက္အုပ္ဆရာေတာ္ 
								ဘဒၵႏ ၱကဝိႏၵကို ဥပဇၥ်ယ္ျပဳလွ်က္၊ မုံရြာၿမိဳ႕ 
								အလယ္ရပ္၊ မာဃလမ္းေန ရဟန္းဒါယကာ ဦးေအာင္ညြန္႕ + 
								ရဟန္းဒါယိကာမ ေဒၚလင္းၾကည္ (သား) ေမာင္ဝင္းထါန္း၊ 
								ေမာင္ေနဝင္ေအာင္၊ ေမာင္မင္းမင္ေအာင္ မိသားစုတိုက၏ 
								ပစၥယာနဂၢဟျဖင့္ ရဟန္းအျဖစ္ 
								ေရာက္ရွိေတာ္မူခဲ့ပါသည္။<br>
								ထို႕ေနာက္ မစိုးရိမ္ဂႏ ၱဆရာေတာ္၏ ပ႒ာန္းေခြမ်ားကို 
								အစမွ အဆုံးထိ (၃)ႀကိမ္တိုင္တိုင္သင္ယူခဲ့သည္။ 
								အင္းစိန္ဆရာေတာ္၏ ပ႒ာန္းေခြ (၅၀) ကို အစမွ အဆုံးထိ 
								(၂၂)ႀကိမ္ နားေထာင္ခဲ့သည္။ လယ္တီဆရာေတာ္၏ 
								ပ႒ာႏုေဒၵသဒီပနီက်မ္းကို အႀကိမ္မ်ားစြာ 
								ေလ့လာခဲ့သည္။ ဆ႒သဂၤါယနာဥကၠ႒ မစိုးရိမ္ဆရာေတာ္၏ 
								ပ႒ာနသေခၤပနယုပေဒသက်မ္းကိုလညး္ ဆရာျဖစ္သည္အထိ 
								သင္ယူခဲ့သည္။ ယၡဳေခတ္၌ ထြက္ေပၚလာေသာ 
								ပ႒ာန္းမွတ္တမ္းစာအုပ္မ်ားကိုလညး္ အားလုံးလိုလိုပင္ 
								မလြတ္ရေအာင္ ၾကည္႕ရႈ႕ခဲ့သည္။<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								စာခ် သာသနာျပဳျခင္း<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၁၃၄၈ ခုႏွစ္မွ စ၍ ၁၃၆၈ ခုႏွစ္အထိ (၂၁) ႏွစ္ၾကာ 
								မုံရြာၿမိဳ႕၊ မဟာေဇာတိကာရာမပါဠိတကၠသိုလ္ရွိ 
								စာသင္သားသံဃာေတာ္(၁၅၀၀)ေက်ာ္တို႕အား 
								အေျခခံအတန္းမ်ားႏွင့္ ငယ္၊ လတ္၊ ႀကီး ဓမၼာစရိယ 
								အတန္းမ်ားႏွင့္ သာမေဏေက်ာ္ စာဝါမ်ားကို 
								ပို႕ခ်ေပးေတာ္မူခဲ့ပါသည္။<br>
								၁၃၆၉ - ခုႏွစ္၊ ပထမဝါဆိုလၦန္း(၁)ရက္ေန႕တြင္ 
								ရန္ကုန္ၿမိဳ႕၊ အင္းစိန္ရြာမ ပရိယတၱိစာသင္တိုက္ 
								ဆရာေတာ္ အရွင္တိေလာကာဘိဝံသမွ ယမိုက္ပ႒ာန္း မေမြခံ 
								တပည္႕အေနအားျဖင့္ ခ်ီးျမွင့္အပ္ေသာ မႏ ၱေလး၊ 
								ရန္ကင္းေတာင္၊ ေလကၽြန္းမာန္ေအာင္ ေက်ာင္းတိုက္ 
								သာမေဏေက်ာ္ စာသင္တိုက္အျဖစ္ တည္ေထာင္ၿပီး 
								သာမေဏေက်ာ္ စာဝါမ်ားကို ပို႕ခ် သင္ၾကားေပးလွ်က္ 
								ရွိပါသည္။<br>
								ထို႕အျပင္ ၁၃၆၉ ခုႏွစ္စ၍ မႏ ၱေလး ရန္ကင္းေတာင္ 
								ပထမေက်ာ္၊ အဂၢမဟာအေက်ာ္၊ မဟာဂႏ ၱဝါစက ပ႑ိတဘြဲ႕ရ 
								ဆရာႀကီး ေဒၚေခမာစရီ တည္ေထာင္ေသာ 
								ခ်မ္းေျမ႕သီစာသင္တိုက္၌ ယမိုက္က်မ္းႏွင့္ 
								ပ႒ာန္းက်မ္း တို႕ကိုလည္းေကာင္း၊ 
								ဓမၼာစရိယစာခ်တန္းအတြက္ အ႒သာလိနီစာဝါကိုလည္းေကာင္း၊ 
								ေန႕စဥ္ ပို႕ခ်ေပးလွ်က္ရွိၿပီး 
								ႏွစ္စဥ္ေႏြရာသီေရာက္တိုင္း၊ မႏ ၱေလးဘုရားႀကီး 
								အေရွ႕မုခ္အနီးရွိ အရွင္သုစိတၱာဘိဝံသ (သ၊ စ၊ သ၊ အ) 
								ေလးဘြဲ႕ရ ဓမၼာစရိယ၏ ဓမၼိကာရာမေက်ာင္းတိုက္ 
								နံ႕သာၿမိဳင္ေက်ာင္းတြင္ သံမိုက္ပ႒ာန္း 
								အထူးသင္တန္းႀကီး ပို႕ခ်လာခဲ့သည္မွာ (၁၅)ႀကိမ္ 
								ရွိခဲ့ၿပီး ျဖစ္ပါသည္။<br>
								ထို႕ေနာက္ သင္တန္းနည္းျပ 
								ကၽြမ္းက်င္ဆရာမ်ားျဖစ္ၾကေသာ ေဒါက္တာ 
								ဦးခင္ေမာင္ၾကည္ႏွင့္ ဇနီး ေဒါက္တာ ေဒၚခ်ိဳခ်ိဳမာ 
								တို႕၏ ေတာင္းပန္ေလ်ာက္ထားခ်က္အရ မႏ ၱေလးၿမိဳ႕၊ 
								မဟာေအာင္ေျမၿမိဳ႕နယ္၊ ၆၉ လမ္း၊ မဟာႏြယ္စဥ္ရပ္၊ 
								မဟာေဗာဓိကုန္းရိပ္သာဝင္း၊ မဟာသႏ ၱိသုခ ဓမၼာရုံ 
								ဓမၼဒီပတြင္ လူပုဂၢိဳလ္မ်ားဆိုင္ရာ 
								ဗုဒၶစာေပသင္တန္းေက်ာင္းတါင္ သင္တန္းသူ၊ သင္တန္းသား 
								(၃၅၀) ခန္႕တို႕အား အပတ္စဥ္ စေန၊ တနဂၤေႏြေန႕မ်ားမွ 
								ပ႒ာန္းဘာသာရပ္ကို သင္ၾကားေပးလွ်က္ ရွိပါသည္။<br>
								ထို႕အျပင္ မႏ ၱေလးၿမိဳ႕၊ ႏိုင္ငံေတာ္ 
								ပရိယတၱိသာသနာ့တကၠသိုလ္ အဂၤလိပ္စာ ပါေမာကၡ 
								ေဒါက္တာအရွင္အာစာရ၏ စီစဥ္မငျဖင့္ စကၤာပူႏိုင္ငံ 
								ဓမၼေဒါင္းလုပ္မိသားစုတို႕၏ ပစၥယာႏုဂၢဟ ခံယူကာ 
								သာမေဏေက်ာ္စာဝါမ်ားကို အင္တာနက္မွ dhammadownload 
								မွ အႀကိမ္ (၁၅၀)ေက်ာ္ ထုတ္လႊင့္ပို႕ခ်ေပးလွ်က္ 
								ရွိပါသည္။ ဒုတိယဆင့္၊ တတိယဆင့္ သာမေဏေကာ်္ 
								စာဝ္မ်ားကိုလည္း ဆက္လက္ ထုတ္လႊင့္ ပို႕ခ်မည္ 
								ျဖစ္ပါသည္။<br>
								ဆရာေတာ္၏ ေလးကၽြန္းမာရ္ေအာင္ သာမေဏေက်ာ္ 
								စာသင္တိုက္အတြင္းမွာပင္ အဂၤါ ဗုဒၶဟူးေန႕ မ်ားတြင္ 
								နိကာယ္သင္တန္းမ်ားကိုလည္း ပို႕ခ်ေပးလွ်က္ 
								ရွိပါသည္။<br>
								၁၃၇၂ ခုႏွစ္၊ ပထမဝါဆိုလၦန္း (၂)ရက္ေန႕တြင္ 
								မုံရြာၿမိဳ႕၊ ကံခၽြန္မုန္႕တိုက္ႏွင့္ 
								လကမာၻပလက္စတစ္ ေရာင္းဝယ္ေရးမိသားစုမ်ားျဖစ္ၾကေသာ 
								ဖခင္ႀကီး ခ်စ္လိႈင္၊ မိခင္ႀကီး ေဒၚညႊန္႕ညႊန္႔ 
								အမႈးထား၍ (သမီး) ကလွ်ာဏီ ေဒၚသန္းသန္းႏု၊ 
								ေဒၚခင္မာဝင္း၊ ေဒၚျမင့္ျမင့္စိုး (သား) 
								ကိုေဌးလြင္၊ ေမာင္ဖိုးခ်ိဳ မိသားစုတို႕က 
								ဒုတိယအႀကိမ္ ရဟန္းဒကာ၊ ဒကာမ 
								မ်ားအျဖစ္ျဖင့္လည္းေကာင္း<br>
								၁၃၇၃ ခုႏွစ္ ျပာသိုလျပည္႕ေန႕တြင္ မႏ 
								ၱေလးပုသိမ္ႀကီးေခ်ာင္းဝန္း ဆည္ေျမာင္း႒ာန 
								ဦစီးအရာရွိ ဦးတင္စိုး + ေဒၚလွျမင့္ မိသားစုတို႕က 
								တတိယအႀကိမ္ ရဟန္းဒကာ၊ ဒကာမမ်ားအျဖစ္ျဖင့္ 
								လည္းေကာင္း၊ <br>
								၁၃၇၆ ခုႏွစ္ တပို႕တြဲလဆန္း (၈)ရက္ေန႕တြင္၊ မႏ 
								ၱေလးၿမိဳ႕၊ ၁၉ လမ္း ေညာင္ပင္ေစ်း ရတနာေ႒း 
								ေက်ာင္းေဆာင္ ေက်ာင္းအမ ေဒၚမာမာေ႒းႏွင့္ ညီအစ္ကို 
								ေမာင္ႏွမတစ္စုတို႕က စတုတထအႀကိမ္ အျဖစ္ျဖင့္ 
								လည္းေကာင္း ကံထပ္မဂၤလာျပဳလုပ္ၾကပါသည္။<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								ပရိယတၱိပညာမ်ား သင္ယူျခင္းႏွင့္ ေအာင္ျမင္ခဲ့ေသာ 
								စာေမးပြဲမ်ား<br>
&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၁၃၃၆ ခုႏွစ္၊ ကဆုန္လတြင္ မုံရြာၿမိဳ႕၊ 
								မဟာေဇာတိကာရာမပါဠိတကၠသိုလ္ေက်ာင္းတိုက္ႀကီးသို႕ 
								ေရာက္ရွိၿပီး ပဓာနနာယကဆရာေတာ္ ဘဒၵႏ ၱစႏၵာသီရိ 
								(အဘိဓဇမဟာရ႒ဂုရု ႏိုင္ငံေတာ္ ာသဝါဒါစရိယ၊ ဘဒၵႏ 
								ၱကဝိႏၵ (အဂၢမဟာပ႑ိတ၊ ႏိုင္ငံေတာ္ ၾသဝါဒါစရိယ)၊ 
								ဘဒၵႏ ၱဂါရဝ (အဂၢမဟာပ႑ိတ ႏိုင္ငံေတာ္ ၾသဝါဒစရိယ) 
								စသည္႕ နာယကဆရာေတာ္မ်ားႏွင့္ စာခ်ဆရာေတာ္မ်ားထံ 
								ပရိယတၱိစာေပမ်ားကို သင္ယူခဲ့ရာ အေျခခံအတန္းမ်ား 
								ပထမငယ္၊ ပထမလတ္၊ ပထမႀကီးတန္းမ်ား 
								ေအာင္ျမင္ေတာ္မူခဲ့ပါသည္။<br>
								ရဟန္းျဖစ္စ (၁)ဝါအရမွာပင္ ဓမၼာစရိယ စာေမးပြဲ 
								ဓမမသဂၤဏီက်မ္းေအာင္ျမင္ၿပီး ၁၃၄၆ ခုႏွစ္တြင္ 
								ပဲခူးၿမိဳ႕ သာသနာ့မ႑ိဳင္ေက်ာင္းတိုက္ 
								ေျပာင္းေရႊ႕ၿပီး ဆရာေတာ္ ဘဒၵႏ ၱသံဝရ (အဂၢမဟာပ႑ိတ) 
								ဘဒၵႏ ၱပညာသီဟ၊ ဘဒၵႏ ၱေတရိႏၵ၊ ဘဒၵႏ ၱဓမၷာနႏၵစာရ 
								စေသာ နာယကစာခ် ဆရာေတာ္မ်ားထံ ဆက္လက္ 
								ပညာသင္ၾကားခဲ့ရာ ဓမၼာစရိယစာေမးပြဲ သီလကၡန္က်မ္းကို 
								ရဟန္း (၂)ဝါအရ ဆက္လက္ေအာင္ျမင္ခဲ့ပါသည္။</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<br>
								၁၃၄၇-ခုႏွစ္တြင္ မုံရြာၿမိဳ႕ မဟာေဇာတိကာရာမတိုက္ 
								ျပန္လည္ေရာက္လာၿပီး ႏွစ္ႏွစ္္ဆက္ ေျဖဆိုရာ 
								၁၃၄၈-ခုႏွစ္ ပါရာဇိကဏ္က်မ္းေအာင္ျမင္သည္႕အတြက္ 
								သာသနာ့ဓဇ ဓမၼာစရိယဘြဲ႕ကို ရရွိေတာ္မူခဲ့ပါသည္။ 
								ဆက္လက္ၿပီး အစိုးရနိကယ္စာေမးပြဲမ်ားကို 
								ဝင္ေရာက္ေျဖဆိုခဲ့ရာ၊ ဝိနယဝိဒူ၊ ဒိဃကာယဝိဒူ၊ 
								အဘိဓမၼာဝိဒူဘြဲ႕မ်ားကို ရရွိေတာ္မူခဲ့ပါသည္။<br>
								အထူးသျဖင့္ အဘိဓမမာ (၇) က်မ္းတြင္ အခက္ဆုံးျဖစ္ေသာ 
								ယမိုက္က်မ္းႏွင့္ ပ႒ာန္းက်မ္းတို႕ကို 
								ရန္ကုန္ၿမိဳ႔၊ အဘိဓမၼာပါရဂူ အင္းစိန္ဆရာေတာ္ 
								အရွင္တိေလာကဘိဝံသ ထံ အထူးျပဳဘာသာအျဖစ္ 
								သင္ယူခဲ့ပါသည္။<br>
								ထို႕ျပင္ ပ႒ာန္းေဒသနာတြင္ 
								ကၽြမ္းက်င္ႏို္င္ရန္အတြက္ ဦးေတေဇာဘာသ 
								မစိုးရိမ္တက္ကုန္း ပ႒ာန္းေခြမ်ားကို အစမွ အဆုံး 
								(၁၀)ႀကိမ္တိုင္ နားေထာင္ခဲ့သည္။</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk Video</font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b>&nbsp;</b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								မႏၱေလး၊ ရန္ကင္းေတာင္၊ ေလးကၽြန္းမာရ္ေအာင္၊ <br>
								သာမေဏေက်ာ္စာသင္တိုက္၊ <br>
								ယမိုက္ ပ႒ာန္းအထူးသင္တန္း နည္းျပဆရာေတာ္ 
								သင္ၾကားပို႕ခ်ေသာ သာမေဏေက်ာ္ ပထမအဆင့္ - </p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/001-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-opening-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အဖြင့္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/002-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/003-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၂)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/004-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၃)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/005-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၄)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/006-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၅)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/007-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၆)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/008-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၇)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/009-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၈)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/010-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၉)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/011-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၀)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/012-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၁)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/013-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၂)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/014-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၃)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/015-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၄)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/016-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၅)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/017-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-slevel-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၆)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/018-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၇)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/019-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၈)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/020-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၁၉)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-thingahaletsaung/021-Mandalay-Yankintaung-Laykyun-Man-Aung-Tharmanaykyaw-level-1-thingahaletsaung-2014.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - သဂၤဟလက္ေဆာင္ စာဝါ - အမွတ္ 
								(၂၀)</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/001-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-06.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁) ၂၀၁၄ ဒီဇင္ဘာ 
								၆ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/002-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-06.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂) ၂၀၁၄ ဒီဇင္ဘာ 
								၆ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/003-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-06.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃) ၂၀၁၄ ဒီဇင္ဘာ 
								၆ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/004-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-07.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၄) ၂၀၁၄ ဒီဇင္ဘာ 
								၇ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/005-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-07.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၅) ၂၀၁၄ ဒီဇင္ဘာ 
								၇ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/006-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-07.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၆) ၂၀၁၄ ဒီဇင္ဘာ 
								၇ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/007-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-08.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၇) ၂၀၁၄ ဒီဇင္ဘာ 
								၈ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/008-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-08.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၈) ၂၀၁၄ ဒီဇင္ဘာ 
								၈ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/009-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-08.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၉) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/010-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-09.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၀) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/011-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-09.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၁) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/012-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-09.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၂) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/013-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-09.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၃) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/014-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-09.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၄) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/015-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-09.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၅) ၂၀၁၄ ဒီဇင္ဘာ 
								၉ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/016-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၆) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/017-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၇) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/018-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၈) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/019-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၁၉) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/020-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၀) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/021-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၁) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/022-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၂) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/023-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၃) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/024-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-10.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၄) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၀ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/025-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၅) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/026-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၆) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/027-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၇) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/028-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၈) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/029-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၂၉) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/030-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃၀) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/031-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃၁) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/032-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-11.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃၂) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၁ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/033-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-12.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃၃) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၂ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/034-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-12.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃၄) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၂ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level-1-Mahawar/035-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-Mahawar-2014-12-12.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ -
								မဟာဝါ - စာဝါ - အမွတ္ (၃၅) ၂၀၁၄ ဒီဇင္ဘာ 
								၁၂ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/001-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-13.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁) ၂၀၁၄ ဒီဇင္ဘာ ၁၃ ရက္ စေနေန႕ ည(၇)နာရီ</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/002-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-13.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂) ၂၀၁၄ ဒီဇင္ဘာ ၁၃ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/003-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-13.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃) ၂၀၁၄ ဒီဇင္ဘာ ၁၃ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/004-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-14.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄) ၂၀၁၄ ဒီဇင္ဘာ ၁၄ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/005-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-15.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၅) ၂၀၁၄ ဒီဇင္ဘာ ၁၅ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/006-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-15.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၆) ၂၀၁၄ ဒီဇင္ဘာ ၁၅ ရက္ </a><br>
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၇) ၂၀၁၄ ဒီဇင္ဘာ ၁၅ ရက္ </p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/008-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-15.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၈) ၂၀၁၄ ဒီဇင္ဘာ ၁၅ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/009-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-15.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၉) ၂၀၁၄ ဒီဇင္ဘာ ၁၅ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/010-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-16.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၀) ၂၀၁၄ ဒီဇင္ဘာ ၁၆ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/011-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-16.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၁) ၂၀၁၄ ဒီဇင္ဘာ ၁၆ ရက္ </a><br>
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/012-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-16.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၂) ၂၀၁၄ ဒီဇင္ဘာ ၁၆ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/013-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-16.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၃) ၂၀၁၄ ဒီဇင္ဘာ ၁၆ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/014-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-16.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၄) ၂၀၁၄ ဒီဇင္ဘာ ၁၆ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/015-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-16.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၅) ၂၀၁၄ ဒီဇင္ဘာ ၁၆ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/016-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-17.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၆) ၂၀၁၄ ဒီဇင္ဘာ ၁၇ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/017-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-17.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၇) ၂၀၁၄ ဒီဇင္ဘာ ၁၇ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/018-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-17.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၈) ၂၀၁၄ ဒီဇင္ဘာ ၁၇ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/019-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-17.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၁၉) ၂၀၁၄ ဒီဇင္ဘာ ၁၇ ရက္</a> </p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/020-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-17.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၀) ၂၀၁၄ ဒီဇင္ဘာ ၁၇ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/021-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-18.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၁) ၂၀၁၄ ဒီဇင္ဘာ ၁၈ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/022-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-18.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၂) ၂၀၁၄ ဒီဇင္ဘာ ၁၈ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/023-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-18.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၃) ၂၀၁၄ ဒီဇင္ဘာ ၁၈ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/024-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-19.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၄) ၂၀၁၄ ဒီဇင္ဘာ ၁၉ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/025-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-19.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၅) ၂၀၁၄ ဒီဇင္ဘာ ၁၉ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/026-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-19.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၆) ၂၀၁၄ ဒီဇင္ဘာ ၁၉ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/027-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-19.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၇) ၂၀၁၄ ဒီဇင္ဘာ ၁၉ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/028-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-20.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၈) ၂၀၁၄ ဒီဇင္ဘာ ၂၀ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/029-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-20.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၂၉) ၂၀၁၄ ဒီဇင္ဘာ ၂၀ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/030-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-20.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၀) ၂၀၁၄ ဒီဇင္ဘာ ၂၀ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/031-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-21.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၁) ၂၀၁၄ ဒီဇင္ဘာ ၂၁ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/032-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-21.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၂) ၂၀၁၄ ဒီဇင္ဘာ ၂၁ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/033-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-21.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၃) ၂၀၁၄ ဒီဇင္ဘာ ၂၁ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/034-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-21.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၄) ၂၀၁၄ ဒီဇင္ဘာ ၂၁ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/035-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-21.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၅) ၂၀၁၄ ဒီဇင္ဘာ ၂၁ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/036-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-22.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၆) ၂၀၁၄ ဒီဇင္ဘာ ၂၂ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/037-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-22.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၇) ၂၀၁၄ ဒီဇင္ဘာ ၂၂ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/038-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-22.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၈) ၂၀၁၄ ဒီဇင္ဘာ ၂၂ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/039-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-22.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၃၉) ၂၀၁၄ ဒီဇင္ဘာ ၂၂ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/040-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-22.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၀) ၂၀၁၄ ဒီဇင္ဘာ ၂၂ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/041-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-23.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၁) ၂၀၁၄ ဒီဇင္ဘာ ၂၃ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/042-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-23.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၂) ၂၀၁၄ ဒီဇင္ဘာ ၂၃ ရက္ </a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/043-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-23.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၃) ၂၀၁၄ ဒီဇင္ဘာ ၂၃ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/044-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-23.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၄) ၂၀၁၄ ဒီဇင္ဘာ ၂၃ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/045-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-23.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၅) ၂၀၁၄ ဒီဇင္ဘာ ၂၃ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/046-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-24.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၆) ၂၀၁၄ ဒီဇင္ဘာ ၂၄ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/047-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-24.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၇) ၂၀၁၄ ဒီဇင္ဘာ ၂၄ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Mandalay-Yankintaung-Laykyun-Man-Aung-Sayadaw-Bhaddanta-Withuta/Tharmanaykyaw-level1-InnGoadHto/048-Mandalay-Yankintaung-Laykyun-Man-Aung-(Tharmanaykyaw-level-1)-InnGoadHto-2014-12-24.mp4">
								သာမေဏေက်ာ္ ပထမအဆင့္ - အဂုၤတၳိဳရ္- စာဝါ - အမွတ္ 
								(၄၈) ၂၀၁၄ ဒီဇင္ဘာ ၂၄ ရက္</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
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
    
