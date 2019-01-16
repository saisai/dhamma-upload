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
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font size="6" color="#800080"><span style="font-family: Times New Roman">
	Dhammaduta Ashin Say Kane Da</span></font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 542px; top: 15px;" id="layer23">
	<img src="images/Dhammaduta-Ashin-Chakkinda.gif" width="161" height="182" border="0"></div>
	



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














<div style="position: absolute; width: 1023px; height: 21752px; z-index: 21; left: 219px; top: 156px" id="layer24" font="" face="Zawgyi-One">
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4"><b>Dhammaduta Ashin Say Kane 
									Da</b></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="2">Dhamma Kathika Sasanadhaja 
                                    Dhammarcariya Sadhamma Nepuna Dhammacariya 
                                    Sasanajoti-pala Dhamma-cariya AGTI (Civil)
                                    </font>
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font>
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;
                                    </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font face="Zawgyi-One">သာသနဓဇ။ သဒၶမၼေနပုည။ 
								သာသနေဇာတိပါလ ဓမၼာစရိယ။ ဓမၼကထိက ဗဟုဇနဟိတဓရ<br>
								<font size="5">ဓမၼဒူတ 
								ေဒါက္တာ အရွင္ ေဆကိႏၵ<br>
								</font>ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား<br>
								</font><br>
&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk </font></b>
								<font size="5"><b>Video</b></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b>&nbsp;</b></p>
                                <p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
၂-၁၂-၂၀၀၃ အသုံးက်မွအသုံးခ် တရားေတာ္<br>
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-ChanChanTharTharNaeTalkMael-3-12-2003.wmv">
၃-၁၂-၂၀၀၃ ခ်မ္းခ်မ္းသာသာေနေတာ့မယ္ တရားေတာ္<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-SheetTarPayMaWaySaeNat-24-12-2003.wmv">
၂၄-၁၂-၂၀၀၃ ရွိတာေပးမေ၀းေစနဲ႕<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-TeTeKyiKyi-24-1-2004.wmv">
၂၄-၁-၂၀၀၄ တည္တည္ၾကည္ၾကည္ တရားေတာ္ (၁၃၆၅ခု တပို႔တြဲလဆန္း ၃ ရက္ေန႕။ ၂၄-၁-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaMyoutPawLwinTinPyanPyi-28-9-2004.wmv">
မျမဳပ္ေပၚလြင္တင္ျပန္ၿပၤီ (၁၃၆၆ခု ေတာ္သလင္းလျပၫ္႔ေန႕။ ၂၈-၉-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaKatSoneSoneMyoutPyanPyi-22-9-2004.wmv">
မကပ္စုန္းစုန္းျမဳပ္ျပန္ၿပီ (၁၃၆၆ခု ေတာ္သလင္းလဆန္း ၉ ရက္ေန႕။ ၂၂-၉-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaTinMyitKyaelLuSalPyi-6-10-2004.wmv">
မတင္ျမစ္က်ယ္လူဆယ္ၿပီီ (၁၃၆၆ခု ေတာ္သလင္းလဆုတ္ ၈ ရက္ေန႕။ ၆-၁၀-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaSaelLuMyatNetSaelPyi-14-10-2004.wmv">
မဆယ္လူျမတ္နတ္ဆယ္ၿပီ (၁၃၆၆ခု သီတင္ကြၽတ္လဆန္း ၁ ရက္ေန႕။ ၁၄-၁၀-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NetMaSalLairWellSoakPyi-21-10-2004.wmv">
နတ္မဆယ္လည္း ၀ဲစုပ္ၿပီ ၂၁-၁၁-၂၀၀၄<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-WairMaSoakPoutSaweWayYaPyi-28-10-2004.wmv">
၀ဲမစုပ္ပုပ္ေဆြး ေ၀းရၿပီ ၂၈-၁၀-၂၀၀၄<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HtaKarYetLaeMaKatPyanPyi-D1-23-8-2004.wmv">
ထကာရပ္လည္းမကပ္ၿပီ (ပထမပိုင္း) (၁၃၆၆ခု ၀ါေခါင္လဆန္း ၈ ရက္ေန႕။ ၂၃-၈-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HtaKarYetLaeMaKatPyanPyi-D2-30-8-2004.wmv">
ထကာရပ္လည္းမကပ္ၿပီ (ဒုတိယပိုင္း) (၁၃၆၆ခု ၀ါေခါင္လျပည္႕ ၁၅ ရက္ေန႕။ ၃၀-၈-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HtaKarYetLaeMaKatPyanPyi-D3-7-9-2004.wmv">
ထကာရပ္လည္းမကပ္ၿပီ (တတိယပိုင္း) (၁၃၆၆ခု ၀ါေခါင္လဆုတ္္ ၈ ရက္ေန႕။ ၇-၉-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HtaKarYetLaeMaKatPyanPyi-13-9-2004.wmv">
ထကာရပ္လည္းမကပ္ၿပီ (၁၃၆၆ခု ၀ါေခါင္လကြယ္ ၁၄ ရက္ေန႕။ ၁၃-၉-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PyoungKarLayKyaMaHtaPyi-15-8-2004.wmv">
ေျပာင္းကာလဲက်မထၿပီီ (၁၃၆၆ခု ဒုတိယ၀ါဆိုလကြယ္ ၁၅ ရက္ေန႕။ ၁၅-၈-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-TaneKarSoneLayMaPyoungPar-8-8-2004.wmv">
တိမ္းကာေစာင္းလည္းမေျပာင္းပါ (၁၃၆၆ခု ဒုတိယ၀ါဆိုလျပည္႔ေက်ာ္္ ၈ ရက္ေန႕။ ၈-၈-၂၀၀၄)
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NyoutYarTaneYoakYaineParThi-30-7-2004.wmv">
ၫြတ္ရာယိမ္း၍တိမ္းပါသည္ (၁၃၆၆ခု ဒုတိယ၀ါဆိုလျပည္႔ေန႕။ ၃၀-၇-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MharMharMhanMhan-29-1-2004.wmv">
မွားမွားမွန္မွန္ (၁၃၆၅ခု တပို႔တြဲလဆန္း ၈ ရက္ေန႕။ ၂၉-၁-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-TaneTaneMatMat-25-1-2004.wmv">
တန္းတန္းမတ္မတ္ (၁၃၆၅ခု တပို႔တြဲလဆန္း ၄ ရက္ေန႕။ ၂၅-၁-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-YinYinKyaeKyae-27-1-2004.wmv">
ယဥ္ယဥ္ေက်းေက်း (၁၃၆၅ခု တပို႔တြဲလဆန္း ၆ ရက္ေန႕။ ၂၇-၁-၂၀၀၄) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-ByarMarLuNetPullZawAtEat-3-12-2003.wmv">
ျဗဟၼာလူနတ္ပူေဇာ္အပ္၏ (၁၃၆၅ခု နတ္ေတာ္လဆန္း ၁၁ ရက္ေန႕။ ၃-၁၂-၂၀၀၃) <br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-YaeToakPineCharMaSoneNhaing-2-12-2003.wmv">
ေရတြက္ပိုင္းျခားမဆုံးႏိုင္ (၁၃၆၅ခု နတ္ေတာ္လဆန္း ၉ ရက္ေန႕။ ၂-၁၂-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-BelLoPyinLoatNaeParkMael-1-12-2003.wmv">
ဘယ္လိုျပင္လို႕ေနပါ့မယ္ (၁၃၆၅ခု နတ္ေတာ္လဆန္း ၈ ရက္ေန႕။ ၁-၁၂-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-ThuSheatYinMaKyoutTalkBull-11-10-2003.wmv">
သူရွိရင္မေၾကာက္ေတာ့ဘူး (၁၃၆၅ခု သီတင္းကြၽတ္လျပည္႕ေက်ာ္ ၁ ရက္ေန႕။ ၁၁-၁၀-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-TaweMyinTheat-10-10-2003.wmv">
ေတြ႕။ ျမင္။ သိ (၁၃၆၅ခု သီတင္းကြၽတ္လျပည္႕ေန႕။ ၁၀-၁၀-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-KoaSateSheatTarTheatTarPar-3-10-2003.wmv">
ကိုယ့္စိတ္ရွိတာသိတာပါ (၁၃၆၅ခု သီတင္းကြၽတ္လဆန္း ၈ ရက္ေန႕။ ၃-၁၀-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-KhaeYingMhanThiYinKyoSarPork-10-10-2004.wmv">
ခဲယဥ္းမွန္းသိရင္ႀကိဳးစားေပါ့ (၁၃၆၅ခု သီတင္းကြၽတ္လျပည္႕ေန႕။ ၁၀-၁၀-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-KoneNaeYaeNaeChanTharSae-26-9-2003.wmv">
ကုန္းေနေရေနခ်မ္းသာေစ (၁၃၆၅ခု သီတင္းကြၽတ္လဆန္း ၁ ရက္ေန႕။ ၂၆-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhTheatSheatLayChanTharLae-24-9-2003.wmv">
အသိရွိေလခ်မ္းသာေလ (၁၃၆၅ခု ေတာ္သလင္းလဆုတ္ ၁၄ ရက္ေန႕။ ၂၄-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
</font>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-TaYarSheatMaSheatThiParTel-19-9-2003.wmv">
<font size="4" face="Zawgyi-One">တရားရွိမရွိသိပါတယ္ (၁၃၆၅ခု ေတာ္သလင္းလဆုတ္ ၉ 
ရက္ေန႕။ ၁၉-၉-၂၀၀၃)<br>
</font></a>
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-SaYarkAhMoay-9-9-2003.wmv">
ဆရာ႔အေမြ (၁၃၆၅ခု ေတာ္သလင္းလဆန္း ၁၄ ရက္ေန႕။ ၉-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaPulKhinLongMhanThi-18-9-2003.wmv">
မပူခင္ေလာင္မွန္းသိ (၁၃၆၅ခု ေတာ္သလင္းလဆုတ္ ၈ ရက္ေန႕။ ၁၈-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-BaWaSarMayePaweAungMyinNee-8-9-2003.wmv">
ဘ၀စာေမးပြဲေအာင္ျမင္နည္း (၁၃၆၅ခု ေတာ္သလင္းလဆန္း ၁၃ ရက္ေန႕။ ၈-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-SateNayKongPhoat-9-9-2003.wmv">
စိတ္ေနေကာင္းဖို႔ (၁၃၆၅ ေတာ္သလင္လဆန္း ၁၄ ရက္ေန႕၊ ၉-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AwayMaThoarAhNarMaNae-D1-18-1-2004.wmv">
အေ၀းမသြားအနားမေန (၁) (၁၃၆၅ခု ျပာသိုလဆုတ္ ၁၂ ရက္ေန႕။ ၁၈-၁-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AwayMaThoarAhNarMaNae-D2-18-1-2004.wmv">
အေ၀းမသြားအနားမေန (၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-YokeNanTheinAyeNyainNateBanPyi-D1-2-2-2004.wmv">
ရုပ္နာမ္သိမ္းေအးၿငိမ္းနိဗၺာန္ျပည္ (၁) (၁၃၆၅ခု တပို႕တြဲလဆန္း ၁၂ ရက္ေန႕။ ၂-၂-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-YokeNanTheinAyeNyainNateBanPyi-D2-2-2-2004.wmv">
ရုပ္နာမ္သိမ္းေအးၿငိမ္းနိဗၺာန္ျပည္ (၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NyainNyainNyaineNyaine-D1-1-2-2004.wmv">
ၿငိမ္ၿငိမ္ ၿငိမ္းၿငိမ္း(၁) (၁၃၆၅ခု တပို႕တြဲလဆန္း ၁၁ ရက္ေန႕။ ၁-၂-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NyainNyainNyaineNyaine-D2-1-2-2004.wmv">
ၿငိမ္ၿငိမ္ ၿငိမ္းၿငိမ္း(၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-LinLinMhainMhain-D1-31-1-2004.wmv">
လင္းလင္းမွိန္မွိန္(၁) (၁၃၆၅ခု တပို႕တြဲလဆန္း ၁၀ ရက္ေန႕။ ၃၁-၁-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
လင္းလင္းမွိန္မွိန္(၂)<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MyanMyanShinShin-D1-30-1-2004.wmv">
ျမန္ျမန္ရွင္းရွင္း(၁) (၁၃၆၅ခု တပို႕တြဲလဆန္း ၉ ရက္ေန႕။ ၃၀-၁-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MyanMyanShinShin-D2-30-1-2004.wmv">
ျမန္ျမန္ရွင္းရွင္း(၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AyeAyeChanChan-D1-26-1-2004.wmv">
ေအးေအးခ်မ္းခ်မ္း(၁) (၁၃၆၅ခု တပို႕တြဲလဆန္း ၅ ရက္ေန႕။ ၂၆-၁-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AyeAyeChanChan-D2-26-1-2004.wmv">
ေအးေအးခ်မ္းခ်မ္း(၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaYaThayTarYaNhaingParTel-D1-31-12-2003.wmv">
မရေသးတာရႏိုင္ပါတယ္(၁) (၁၃၆၅ခု ျပာသိုလဆန္း ၉ ရက္ေန႕။ ၃၁-၁၂-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaYaThayTarYaNhaingParTel-D2-31-12-2003.wmv">
မရေသးတာရႏိုင္ပါတယ္(၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhLoLikeAhKyakPar-D1-2-1-2004.wmv">
အလိုလိုက္အႀကိဳက္ပါ(၁) (၁၃၆၅ခု ျပာသိုလဆန္း ၁၁ ရက္ေန႕။ ၂-၁-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhLoLikeAhKyakPar-D2-2-1-2004.wmv">
အလိုလိုက္အႀကိဳက္ပါ(၂)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-KoukSaYarKoKyaitKyaitSaYarKoKoukNaeTat-12-11-2005.wmv">
ေၾကာက္စရာကိုႀကိဳက္။ ႀကိဳက္စရာကိုေၾကာက္ေနတတ္ (၁၂-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-LonThoarPyi-15-11-2005.wmv">
လြန္သြားၿပီ (၁၅-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-MaTheatThayLoatPar-15-11-2005.wmv">
မသိေသးလို႕ပါ (၁၅-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-LoToePoShort-16-11-2005.wmv">
လိုတိုးပိုေလွ်ာ့ (၁၆-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HluPyieYinLaeYouSanParOo-17-11-2005.wmv">
လွဴၿပီးရင္လဲ ယူစမ္းပါဦး (၁၇-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HluLaeHluYouLairYouKyaPar-18-11-2005.wmv">
လွဴလဲလွဴ။ ယူလဲယူၾကပါဦး (၁၈-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-ThuParLoatKongTarPar-18-11-2005.wmv">
သူပါလို႕ေကာင္းတာပါ (၁၈-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-TheatMhatPhyitMael-10-9-2003.wmv">
သိမွျဖစ္မယ္ ျဖစ္မွသိမယ္ (၁၃၆၅ခု ေတာ္သလင္းလျပည္႔္ေန႕။ ၁၀-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-ChyeHtarMhanTheatYinPhyaLikePar-3-9-2003.wmv">
ခ်ည္ထားမွန္းသိရင္ ျဖည္လိုက္ပါ (၁၃၆၅ခု ေတာ္သလင္းလဆန္း ၈ ရက္ေန႕။ ၃-၉-၂၀၀၃)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PyatPyatTharThar-28-1-2004.wmv">
ျပတ္ျပတ္သားသား (၁၃၆၅ တပို႕တြဲလဆန္း ၇ ရက္ေန႕၊ ၂၈-၁-၂၀၀၄)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhMhanKoPyawNhaingParSay-26-11-2003.wmv">
အမွန္ကိုေျပာႏိုင္ပါေစ ၂၆-၁၁-၂၀၀၃<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D01-19-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၁) (၁၉-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D02-20-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၂) (၂၀-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D03-23-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၃) (၂၃-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၄) (၂၄-၁၁-၂၀၀၅)<br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D05-26-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၅) (၂၆-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D06-27-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၆) (၂၇-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၇) (၂၈-၁၁-၂၀၀၅)<br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D08-29-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၈) (၂၉-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D09-30-11-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၉) (၃၀-၁၁-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaticcaSamupa-D10-1-12-2005.wmv">
ပဋိစၥသမုပၸါဒ္ ေဒသနာေတာ္ (၁၀) (၁-၁၂-၂၀၀၅)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NaungYaeAyeYaAung-D1-21-11-2007.wmv">
ေနာင္ေရးေအးရေအာင္ တရားေတာ္ (၁) ၂၁-၁၁-၂၀၀၇ (က်ိဳကၠဆံ)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NaungYaeAyeYaAung-D2-21-11-2007.wmv">
ေနာင္ေရးေအးရေအာင္ တရားေတာ္ (၂) ၂၁-၁၁-၂၀၀၇ (က်ိဳကၠဆံ)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-KyawtKwinLookAung-15-12-2007.wmv">
ေက်ာ႕ကြင္းလြတ္ေအာင္ တရားေတာ္ - ကမာရြတ္(၄)ရပ္ကြက္ ၁၅-၁၂-၂၀၀၇<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhLaKarPhyitKoneParPyi-16-12-2007.wmv">
အလကားျဖစ္ကုန္ပါၿပီ တရားေတာ္ ၁၆-၁၂-၂၀၀၇ ပ်ားရည္ကုန္း(၁၄၈)လမ္း<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaHtan-D1-26-12-2007.wmv">
ပ႒ာန္း တရားေတာ္ (၁) ၂၆-၁၂-၂၀၀၇<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-PaHtan-D2-26-12-2007.wmv">
ပ႒ာန္း တရားေတာ္ (၂) ၂၆-၁၂-၂၀၀၇<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HlaKyeatSanParChanTharTel-D1-24-1-2008.wmv">
လွၾကည္႕စမ္းပါ ခ်မ္းသာတယ္ တရားေတာ္(၁) ၂၄-၁-၂၀၀၈<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-HlaKyeatSanParChanTharTel-D2-24-1-2008.wmv">
လွၾကည္႕စမ္းပါ ခ်မ္းသာတယ္ တရားေတာ္(၂) ၂၄-၁-၂၀၀၈<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NoonAhTwinPhookSinKuuNayKyaTel-D1-23-1-2008.wmv">
ႏြံအတြင္း ဇြတ္ဆင္းေနၾကတယ္ တရားေတာ္(၁) ၂၃-၁-၂၀၀၈<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-NoonAhTwinPhookSinKuuNayKyaTel-D2-23-1-2008.wmv">
ႏြံအတြင္း ဇြတ္ဆင္းေနၾကတယ္ တရားေတာ္(၁) ၂၃-၁-၂၀၀၈<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-ArrYaParYa-8-2-2008.wmv">
အားရပါး တရားေတာ္ ၈-၂-၂၀၀၈<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-KuThoPhyitPhotMaLwelParLay-11-2-2008.wmv">
ကုသိုလ္ျဖစ္မလြယ္ပါေလ တရားေတာ္ ၁၁-၂-၂၀၀၈ (၁၃-လမ္း)<br>
</a>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/DhammaDutaAshinChakkinda/AshinChakkinda-AhThoneKyaMhaAhThoneCha-2-12-2003.wmv">
<br>
&nbsp;</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
								<font size="4">****dhamma talks uploaded and published on 
								23 Sept 2011****</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>






<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၁)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/01-Ashin-SayKaneDa-DVD01.mp4">၀၀၁။ ေတြ႕ပါတယ္ ဒါေပမယ့္မျမင္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/02-Ashin-SayKaneDa-DVD01.mp4">၀၀၂။ ျမင္ေပမယ့္ မမွန္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/03-Ashin-SayKaneDa-DVD01.mp4">၀၀၃။ မွန္ေပမယ့္ တလြဲ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/04-Ashin-SayKaneDa-DVD01.mp4">၀၀၄။ လြဲေပမယ့္ ေကာင္းပါတယ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/05-Ashin-SayKaneDa-DVD01.mp4">၀၀၅။ ေကာင္းေပမယ့္ မလြတ္ေသး</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/06-Ashin-SayKaneDa-DVD01.mp4">၀၀၆။ လြတ္ခ်င္ေပမယ့္ မရပါ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/07-Ashin-SayKaneDa-DVD01.mp4">၀၀၇။ ရေပမယ့္ မယူ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/08-Ashin-SayKaneDa-DVD01.mp4">၀၀၈။ ယူေပမယ့္ ကိုယ့္စိတ္ၾကိဳက္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/09-Ashin-SayKaneDa-DVD01.mp4">၀၀၉။ ၾကိဳက္ေပမယ့္ ေဝးေဝးေရွာင္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/10-Ashin-SayKaneDa-DVD01.mp4">၀၁၀။ ေဝးေပမဲ့ မနီးပါ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/11-Ashin-SayKaneDa-DVD01.mp4">၀၁၁။ ကိုယ္လွဴလုိ႕ ကိုယ္ဝမ္းသာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/12-Ashin-SayKaneDa-DVD01.mp4">၀၁၂။ ယဥ္ယဥ္ ေက်းေက်း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/13-Ashin-SayKaneDa-DVD01.mp4">၀၁၃။ ေသမွာသိလို႕ မေသခ်ာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/14-Ashin-SayKaneDa-DVD01.mp4">၀၁၄။ အဆင္ေျပရဲ႕လား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/15-Ashin-SayKaneDa-DVD01.mp4">၀၁၅။ အမွန္ကို ျပန္ေျပာႏိုင္ပါေစ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/16-Ashin-SayKaneDa-DVD01.mp4">၀၁၆။ ေၾကာက္အားပိုပါသည္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/17-Ashin-SayKaneDa-DVD01.mp4">၀၁၇။ အမွန္အတိုင္း ျမင္ေစခ်င္တယ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/18-Ashin-SayKaneDa-DVD01.mp4">၀၁၈။ မအိုေဆး</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-01/19-Ashin-SayKaneDa-DVD01.mp4">၀၁၉။ အခုလိုဆိုေတာ့လြယ္သားပဲ</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၂)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/01-Ashin-SayKaneDa-DVD02.mp4">၀၀၁။ မွားသလား၊ မွန္သလား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/02-Ashin-SayKaneDa-DVD02.mp4">၀၀၂။ သံေယာဇဥ္ ျဖတ္ခ်င္တယ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/03-Ashin-SayKaneDa-DVD02.mp4">၀၀၃။ ႏိုးႏိုးၾကားၾကား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/04-Ashin-SayKaneDa-DVD02.mp4">၀၀၄။ အျမဲတမ္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/05-Ashin-SayKaneDa-DVD02.mp4">၀၀၅။ မဂၤလသုတ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/06-Ashin-SayKaneDa-DVD02.mp4">၀၀၆။ ရခဲပါေပတယ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/07-Ashin-SayKaneDa-DVD02.mp4">၀၀၇။ ပုဂၢိဳလ္(၂)မ်ိဳး(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/08-Ashin-SayKaneDa-DVD02.mp4">၀၀၈။ ပုဂၢိဳလ္(၂)မ်ိဳး(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/09-Ashin-SayKaneDa-DVD02.mp4">၀၀၉။ တစ္ေယာက္တည္းေန၊ တစ္ေရတည္းေသာက္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/10-Ashin-SayKaneDa-DVD02.mp4">၀၁၀။ ေပါင္းတတ္ သင္းတတ္ ေနထိုင္တတ္ပါေစ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/11-Ashin-SayKaneDa-DVD02.mp4">၀၁၁။ အာ႒ာဝကသုတၱန္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/12-Ashin-SayKaneDa-DVD02.mp4">၀၁၂။ ညႊတ္ရာယိမ္း၍ တိမ္းပါသည္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/13-Ashin-SayKaneDa-DVD02.mp4">၀၁၃။ တစ္ဆင့္ထက္တစ္ဆင့္ ျမင့္သထက္ျမင့္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/14-Ashin-SayKaneDa-DVD02.mp4">၀၁၄။ ေျပာင္းကာလဲက် မထျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/15-Ashin-SayKaneDa-DVD02.mp4">၀၁၅။ အားကိုးပါရေစ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/16-Ashin-SayKaneDa-DVD02.mp4">၀၁၆။ ေသာတာပန္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-02/17-Ashin-SayKaneDa-DVD02.mp4">၀၁၇။ အရႈံးလိုလိုအျမတ္လိုလို</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၃)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/01-Ashin-SayKaneDa-DVD03.mp4">၀၀၁။ ပီတိျဖစ္လိုက္တာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/02-Ashin-SayKaneDa-DVD03.mp4">၀၀၂။ ယံုၾကည္ထိုက္သူ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/03-Ashin-SayKaneDa-DVD03.mp4">၀၀၃။ ယံုၾကည္ထိုက္သူ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/04-Ashin-SayKaneDa-DVD03.mp4">၀၀၄။ ခုတစ္မ်ိဳး ေတာ္ၾကာတစ္မ်ိဳး</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/05-Ashin-SayKaneDa-DVD03.mp4">၀၀၅။ လွဴလည္းလွဴ ယူလည္းယူ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/06-Ashin-SayKaneDa-DVD03.mp4">၀၀၆။ ျဖစ္မွ ျဖစ္ပါ့မလား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/07-Ashin-SayKaneDa-DVD03.mp4">၀၀၇။ ဘုရားအေလာင္း မေဟာ္သဓာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/08-Ashin-SayKaneDa-DVD03.mp4">၀၀၈။ မိဘႏွင့္ သားသမီး(က)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/09-Ashin-SayKaneDa-DVD03.mp4">၀၀၉။ မိဘႏွင့္ သားသမီး(ခ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/10-Ashin-SayKaneDa-DVD03.mp4">၀၁၀။ ႏွေျမာလြန္းလို႕ပါ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/11-Ashin-SayKaneDa-DVD03.mp4">၀၁၁။ သုခ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/12-Ashin-SayKaneDa-DVD03.mp4">၀၁၂။ ေမတၱာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/13-Ashin-SayKaneDa-DVD03.mp4">၀၁၃။ အာသေဝါ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/14-Ashin-SayKaneDa-DVD03.mp4">၀၁၄။ တဏွာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/15-Ashin-SayKaneDa-DVD03.mp4">၀၁၅။ စိတ္ထားျပဳျပင္ ေျပာင္းပါ့မယ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/16-Ashin-SayKaneDa-DVD03.mp4">၀၁၆။ မေကာင္းရင္လဲ ကင္းေအာင္ေန</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/17-Ashin-SayKaneDa-DVD03.mp4">၀၁၇။ စိတ္မညစ္ခ်င္ေတာ့ဘူး</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/18-Ashin-SayKaneDa-DVD03.mp4">၀၁၈။ မျမဲတာနဲ႕ ျမဲတာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/19-Ashin-SayKaneDa-DVD03.mp4">၀၁၉။ ဆင္းရဲ ခ်မ္းသာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-03/20-Ashin-SayKaneDa-DVD03.mp4">၀၂၀။ ထင္သလိုမဟုတ္</a><br>
<br>
<br>
<br>
<br>
DVD အမွတ္စဥ္ (၄)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/01-Ashin-SayKaneDa-DVD04.mp4">၀၀၁။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/02-Ashin-SayKaneDa-DVD04.mp4">၀၀၂။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/03-Ashin-SayKaneDa-DVD04.mp4">၀၀၃။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/04-Ashin-SayKaneDa-DVD04.mp4">၀၀၄။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/05-Ashin-SayKaneDa-DVD04.mp4">၀၀၅။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/06-Ashin-SayKaneDa-DVD04.mp4">၀၀၆။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/07-Ashin-SayKaneDa-DVD04.mp4">၀၀၇။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၇)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/08-Ashin-SayKaneDa-DVD04.mp4">၀၀၈။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၈)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/09-Ashin-SayKaneDa-DVD04.mp4">၀၀၉။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၉)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/10-Ashin-SayKaneDa-DVD04.mp4">၀၁၀။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/11-Ashin-SayKaneDa-DVD04.mp4">၀၁၁။ ေနစဥ္အလုပ္၊ ေန႕စဥ္အလုပ္(၁၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/12-Ashin-SayKaneDa-DVD04.mp4">၀၁၂။ ရိွတဲ့အင္အားနဲ႕ ရုန္းလိုက္ပါ(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/13-Ashin-SayKaneDa-DVD04.mp4">၀၁၃။ ရိွတဲ့အင္အားနဲ႕ ရုန္းလိုက္ပါ(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/14-Ashin-SayKaneDa-DVD04.mp4">၀၁၄။ သူေတာ္ေကာင္း အလွဴ(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-04/15-Ashin-SayKaneDa-DVD04.mp4">၀၁၅။ သူေတာ္ေကာင္း အလွဴ(၂)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၅)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/01-Ashin-SayKaneDa-DVD05.mp4">၀၀၁။ အခု သိျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/02-Ashin-SayKaneDa-DVD05.mp4">၀၀၂။ အခု က်င့္ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/03-Ashin-SayKaneDa-DVD05.mp4">၀၀၃။ အခု ေသျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/04-Ashin-SayKaneDa-DVD05.mp4">၀၀၄။ အခု ရွင္ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/05-Ashin-SayKaneDa-DVD05.mp4">၀၀၅။ အခု လည္ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/06-Ashin-SayKaneDa-DVD05.mp4">၀၀၆။ အခု ရပ္ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/07-Ashin-SayKaneDa-DVD05.mp4">၀၀၇။ အခု ေတြ႕ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/08-Ashin-SayKaneDa-DVD05.mp4">၀၀၈။ အခု ျမင္ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/09-Ashin-SayKaneDa-DVD05.mp4">၀၀၉။ အခု ျပတ္ျပီ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/10-Ashin-SayKaneDa-DVD05.mp4">၀၁၀။ အလွဴတတ္ ျမတ္သထက္ျမတ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/11-Ashin-SayKaneDa-DVD05-Ya-Khae(1).mp4">၀၁၁။ ရခဲေတာ့မူ လွပါေပတယ္ (၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/12-Ashin-SayKaneDa-DVD05-Ya-Khae(2).mp4">၀၁၂။ ရခဲေတာ့မူ လွပါေပတယ္ (၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/13-Ashin-SayKaneDa-DVD05-Hlu-Kyi.mp4">၀၁၃။ လွဴၾကည္႕ရေအာင္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/14-Ashin-SayKaneDa-DVD05-Tayar-nar.mp4">၀၁၄။ တရားနာရင္း တရားရတယ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-05/15-Ashin-SayKaneDa-DVD05-Kyi-Pwar.mp4">၀၁၅။ ၾကီးပြားခ်မ္းသာေရး</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၆)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/01-Ashin-SayKaneDa-DVD06.mp4">၀၀၁။ သူတို႕ေၾကာင့္(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/02-Ashin-SayKaneDa-DVD06.mp4">၀၀၂။ သူတို႕ေၾကာင့္(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/03-Ashin-SayKaneDa-DVD06.mp4">၀၀၃။ သူတို႕ေၾကာင့္(၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/04-Ashin-SayKaneDa-DVD06.mp4">၀၀၄။ သူတို႕ေၾကာင့္(၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/05-Ashin-SayKaneDa-DVD06.mp4">၀၀၅။ သူတို႕ေၾကာင့္(၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/06-Ashin-SayKaneDa-DVD06.mp4">၀၀၆။ သူတို႕ေၾကာင့္(၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/07-Ashin-SayKaneDa-DVD06.mp4">၀၀၇။ သူတို႕ေၾကာင့္(၇)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/08-Ashin-SayKaneDa-DVD06.mp4">၀၀၈။ သူတို႕ေၾကာင့္(၈)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/09-Ashin-SayKaneDa-DVD06.mp4">၀၀၉။ သူတို႕ေၾကာင့္(၉)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/10-Ashin-SayKaneDa-DVD06.mp4">၀၁၀။ သူတို႕ေၾကာင့္(၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/11-Ashin-SayKaneDa-DVD06.mp4">၀၁၁။ သူတို႕ေၾကာင့္(၁၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/12-Ashin-SayKaneDa-DVD06.mp4">၀၁၂။ မဂၤလသုတၱန္(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/13-Ashin-SayKaneDa-DVD06.mp4">၀၁၃။ မဂၤလသုတၱန္(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/14-Ashin-SayKaneDa-DVD06.mp4">၀၁၄။ ပုဂၢိဳလ္ႏွစ္မ်ိဳး(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-06/15-Ashin-SayKaneDa-DVD06.mp4">၀၁၅။ ပုဂၢိဳလ္ႏွစ္မ်ိဳး(၂)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၇)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/01-Ashin-SayKaneDa-DVD07-15-2-2010.mp4">၀၀၁။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/02-Ashin-SayKaneDa-DVD07-16-2-2010.mp4">၀၀၂။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/03-Ashin-SayKaneDa-DVD07-17-2-2010.mp4">၀၀၃။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/04-Ashin-SayKaneDa-DVD07-18-2-2010.mp4">၀၀၄။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/04-Ashin-SayKaneDa-DVD07-18-2-2010.mp4">၀၀၅။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/06-Ashin-SayKaneDa-DVD07-20-2-2010.mp4">၀၀၆။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/07-Ashin-SayKaneDa-DVD07-21-2-2010.mp4">၀၀၇။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၇)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/08-Ashin-SayKaneDa-DVD07-22-2-2010.mp4">၀၀၈။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၈)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/09-Ashin-SayKaneDa-DVD07-23-2-2010.mp4">၀၀၉။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၉)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-07/10-Ashin-SayKaneDa-DVD07-24-2-2010.mp4">၀၁၀။ ကိုယ့္ဘဝ ကိုဖန္တီးပါ- အပိုင္း(၁၀)</a><br>
<br>
<br>
<br>
DVD အမွတ္စဥ္ (၈)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/01-Ashin-SayKaneDa-DVD08.mp4">၀၀၁။ တစ္ခုမဟုတ္ တစ္ခု(၁) (၇.၇.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/02-Ashin-SayKaneDa-DVD08.mp4">၀၀၂။ တစ္ခုမဟုတ္ တစ္ခု(၂) (၈.၇.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/03-Ashin-SayKaneDa-DVD08.mp4">၀၀၃။ တစ္ခုမဟုတ္ တစ္ခု(၃) (၉.၇.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/04-Ashin-SayKaneDa-DVD08.mp4">၀၀၄။ တစ္ခုမဟုတ္ တစ္ခု(၄) (၂၀.၇.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/05-Ashin-SayKaneDa-DVD08.mp4">၀၀၅။ တစ္ခုမဟုတ္ တစ္ခု(၅) (၂၁.၇.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/06-Ashin-SayKaneDa-DVD08.mp4">၀၀၆။ တစ္ခုမဟုတ္ တစ္ခု(၆) (၂၂.၇.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/07-Ashin-SayKaneDa-DVD08.mp4">၀၀၇။ တစ္ခုမဟုတ္ တစ္ခု(၇) (၄.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/08-Ashin-SayKaneDa-DVD08.mp4">၀၀၈။ တစ္ခုမဟုတ္ တစ္ခု(၈) (၅.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/09-Ashin-SayKaneDa-DVD08.mp4">၀၀၉။ တစ္ခုမဟုတ္ တစ္ခု(၉) (၆.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/10-Ashin-SayKaneDa-DVD08.mp4">၀၁၀။ တစ္ခုမဟုတ္ တစ္ခု(၁၀) (၁၁.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/11-Ashin-SayKaneDa-DVD08.mp4">၀၁၁။ တစ္ခုမဟုတ္ တစ္ခု(၁၁) (၁၂.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/12-Ashin-SayKaneDa-DVD08.mp4">၀၁၂။ တစ္ခုမဟုတ္ တစ္ခု(၁၂) (၁၃.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/13-Ashin-SayKaneDa-DVD08.mp4">၀၁၃။ တစ္ခုမဟုတ္ တစ္ခု(၁၃) (၁၄.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/14-Ashin-SayKaneDa-DVD08.mp4">၀၁၄။ တစ္ခုမဟုတ္ တစ္ခု(၁၄) (၁၅.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/15-Ashin-SayKaneDa-DVD08.mp4">၀၁၅။ တစ္ခုမဟုတ္ တစ္ခု(၁၅) (၉.၉.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/16-Ashin-SayKaneDa-DVD08.mp4">၀၁၆။ တစ္ခုမဟုတ္ တစ္ခု(၁၆) (၁၀.၉.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-08/17-Ashin-SayKaneDa-DVD08.mp4">၀၁၇။ တစ္ခုမဟုတ္ တစ္ခု(၁၇) (၁၁.၉.၂၀၁၀)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
<br>
DVD အမွတ္စဥ္ (၉)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/01-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၁။ မဂၤလသုတၱံေဒသနာေတာ္အရတရားအားထုတ္နည္း (နိဒါန္း)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/02-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၂။ အေသဝနာစဗလာနံ၊ ပ႑ိတနဥၥေသဝနာ၊ ပူဇာဇပူဇေနယ်ာနံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/03-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၃။ ပတိရူပေဒသဝါေသာစ၊ ပုေဗၺစကတပုညတာ၊ အတၱသမၼာပဏိဓိစ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/04-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၄။ ဗဟုသစၥဥၥ၊ သိပၸစၥဥၥ၊ ဝိနေယာစသုသိကၡိေတာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/05-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၅။ သုဘာသိတာစယာဝစာ၊ မာတာပိတုဥပ႒ာနံ (အမိကိုျပဳစုလုပ္ေကၽြးျခင္း)၊&nbsp; 
မာတာပိတုဥပ႒ာနံ (အဖိကိုျပဳစုလုပ္ေကၽြးျခင္း)၊</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/06-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၆။ ပုတၱဒါရႆသဂၤေဟာ၊ အနာကုလာစကၼႏာၱ၊ ဒါနဥၥ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/07-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၇။ ဓမၼစရိယာစ၊ ညာတကနဥၥသကၤေဟာ၊ အနဝဇၨာနိကမၼာနိ၊ အာရတီဝိရတီပါပါ၊ မဇၨပါနာစသယေမာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/08-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၈။ အပၸမာေဒါစဓေမၼသု၊ ဂါရေဝါစ၊ နိဝါေတာစ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/09-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၉။ သႏၱဳ႒ိစ၊ ကတညဳတာ၊ ကာေလနဓမၼႆဝနံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/10-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၁၀။ ခႏၱီစ၊ ေသာဝစႆတာ၊ သာမဏနစၥဒႆနံ၊ ကာေလနဓမၼသာကစာၦ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/11-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၁၁။ တေပါစ၊ ျဗဟၼစရိယ၊ အရိယာသစၥာနဒႆနံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/12-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၁၂။ နိဗၺာနသစိ ၦကိရိယာစ၊ ဖု႒ႆေလာကဓေမၼဟိ၊ စိတၱယႆနကမၸတိ၊ အေသာကံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-09/13-Ashin-SayKaneDa-DVD09-Mingalar.mp4">
၁၃။ ဝိရဇံ၊ ေခမံ၊ မဂၤလသုတၱံေဒႆနာေတာ္အရ တရားအားထုတ္နည္း (နိဂုံး)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၀)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/01-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၁။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၁) (၇.၅.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/02-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၂။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၂) (၇.၅.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/03-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၃။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၃) (၈.၅.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/04-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၄။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၄) (၈.၅.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/05-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၅။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၅) (၈.၅.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/06-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၆။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၆) (၈.၅.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/07-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၇။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၇) (၈.၅.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/08-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၈။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၈) (၉.၅.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/09-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၀၉။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၉) (၉.၅.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/10-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၁၀။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၁၀) (၉.၅.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-10/11-Ashin-SayKaneDa-DVD10-Thawtarpan.mp4">၀၁၁။ ေသာတပန္ျဖစ္ေၾကာင္း- အပုိင္း(၁၁) (၉.၅.၂၀၁၀-ည)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၁)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/01-Ashin-SayKaneDa-DVD11-Mahlantsarparne.mp4">၀၀၁။ မလွည္႕စားပါနဲ႕ အပိုင္း(၁) (၁၈.၆.၂၀၁၀-ေမွာ္ဘီ-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/02-Ashin-SayKaneDa-DVD11-Mahlant.mp4">၀၀၂။ မလွည္႕စားပါနဲ႕ အပိုင္း(၂) (၁၈.၆.၂၀၁၀-ေမွာ္ဘီ-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/03-Ashin-SayKaneDa-DVD11-Mahant.mp4">၀၀၃။ မလွည္႕စားပါနဲ႕ အပိုင္း(၃) (၁၉.၆.၂၀၁၀-ေမွာ္ဘီ-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/04-Ashin-SayKaneDa-DVD11-Mahant.mp4">၀၀၄။ မလွည္႕စားပါနဲ႕ အပိုင္း(၄) (၁၉.၆.၂၀၁၀-ေမွာ္ဘီ-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/05-Ashin-SayKaneDa-DVD11-Mahant.mp4">၀၀၅။ မလွည္႕စားပါနဲ႕ အပိုင္း(၅) (၁၉.၆.၂၀၁၀-ေမွာ္ဘီ-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/06-Ashin-SayKaneDa-DVD11-Mahant.mp4">၀၀၆။ မလွည္႕စားပါနဲ႕ အပိုင္း(၆) (၁၉.၆.၂၀၁၀-ေမွာ္ဘီ-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/07-Ashin-SayKaneDa-DVD11-Mahlant.mp4">၀၀၇။ မလွည္႕စားပါနဲ႕ အပိုင္း(၇) (၁၉.၆.၂၀၁၀-ေမွာ္ဘီ-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/08-Ashin-SayKaneDa-DVD11-Mahlant.mp4">၀၀၈။ မလွည္႕စားပါနဲ႕ အပိုင္း(၈) (၂၀.၆.၂၀၁၀-ေမွာ္ဘီ-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/09-Ashin-SayKaneDa-DVD11-Mahlant.mp4">၀၀၉။ မလွည္႕စားပါနဲ႕ အပိုင္း(၉) (၂၀.၆.၂၀၁၀-ေမွာ္ဘီ-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/10-Ashin-SayKaneDa-DVD11-Mahlant.mp4">၀၁၀။ မလွည္႕စားပါနဲ႕ အပိုင္း(၁၀) (၂၀.၆.၂၀၁၀-ေမွာ္ဘီ-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-11/11-Ashin-SayKaneDa-DVD11-Mahlant.mp4">၀၁၁။ မလွည္႕စားပါနဲ႕ အပိုင္း(၁၁) (၂၀.၆.၂၀၁၀-ေမွာ္ဘီ-ည)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၂)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/01-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၁။ အရုဏ္တက္မွ ေနထြက္ပါတယ္ (၂၃.၇.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/02-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၂။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း (၂) (၂၃.၇.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/03-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၃။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၃) (၂၄.၇.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/04-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၄။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၄) (၂၄.၇.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/05-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၅။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၅) (၂၄.၇.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/06-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၆။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၆) (၂၄.၇.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/07-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၇။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၇) (၂၅.၇.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/08-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၈။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၈) (၂၅.၇.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/09-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၀၉။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၉) (၂၅.၇.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-12/10-Ashin-SayKaneDa-DVD12-Dawn.mp4">၀၁၀။ အရုဏ္တက္မွ ေနထြက္ပါတယ္- အပိုင္း(၁၀) (၂၅.၇.၂၀၁၀-ည)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၃)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/01-Ashin-SayKaneDa-DVD13.mp4">၀၀၁။ တစ္သက္လံုးမွတ္တရ(၁) (၂၀.၈.၂၀၁၀)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/02-Ashin-SayKaneDa-DVD13.mp4">၀၀၂။ တစ္သက္လံုးမွတ္တရ(၂) (၂၀.၈.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/03-Ashin-SayKaneDa-DVD13.mp4">၀၀၃။ တစ္သက္လံုးမွတ္တရ(၃) (၂၁.၈.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/04-Ashin-SayKaneDa-DVD13.mp4">၀၀၄။ တစ္သက္လံုးမွတ္တရ(၄) (၂၁.၈.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/05-Ashin-SayKaneDa-DVD13.mp4">၀၀၅။ တစ္သက္လံုးမွတ္တရ(၅) (၂၁.၈.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/06-Ashin-SayKaneDa-DVD13.mp4">၀၀၆။ တစ္သက္လံုးမွတ္တရ(၆) (၂၁.၈.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/07-Ashin-SayKaneDa-DVD13.mp4">၀၀၇။ တစ္သက္လံုးမွတ္တရ(၇) (၂၂.၈.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/08-Ashin-SayKaneDa-DVD13.mp4">၀၀၈။ တစ္သက္လံုးမွတ္တရ(၈) (၂၀.၈.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/09-Ashin-SayKaneDa-DVD13.mp4">၀၀၉။ တစ္သက္လံုးမွတ္တရ(၉) (၂၀.၈.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-13/10-Ashin-SayKaneDa-DVD13.mp4">၀၁၀။ တစ္သက္လံုးမွတ္တရ(၁၀)(၂၀.၈.၂၀၁၀-ညေန)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၄)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/01-Ashin-SayKaneDa-DVD14.mp4">၀၀၁။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား 
(၁) (၂၄.၉.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/02-Ashin-SayKaneDa-DVD14.mp4">၀၀၂။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၂) (၂၄.၈.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/03-Ashin-SayKaneDa-DVD14.mp4">၀၀၃။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၃) (၂၅.၈.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/04-Ashin-SayKaneDa-DVD14.mp4">၀၀၄။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၄) (၂၅.၈.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/05-Ashin-SayKaneDa-DVD14.mp4">၀၀၅။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၅) (၂၅.၈.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/06-Ashin-SayKaneDa-DVD14.mp4">၀၀၆။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၆) (၂၅.၈.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/07-Ashin-SayKaneDa-DVD14.mp4">၀၀၇။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၇) (၂၆.၈.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/08-Ashin-SayKaneDa-DVD14.mp4">၀၀၈။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၈) (၂၆.၈.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/09-Ashin-SayKaneDa-DVD14.mp4">၀၀၉။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၉) (၂၆.၈.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-14/10-Ashin-SayKaneDa-DVD14.mp4">၀၁၀။ ေကာင္းတာလုပ္ဖို႕လြယ္ျပီလား (၁၀) (၂၆.၈.၂၀၁၀-ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">၀၁၁။</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<br>
<br>
DVD အမွတ္စဥ္ (၁၅)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/01-Ashin-SayKaneDa-DVD15.mp4">၀၀၁။ လုပ္ခဲ့သမွ် အရာမထင္ (၁၅.၁၀.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/02-Ashin-SayKaneDa-DVD15.mp4">၀၀၂။ လုပ္ခဲ့သမွ် အရာမထင္ (၂) (၁၅.၁၀.၂၀၁၀-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/03-Ashin-SayKaneDa-DVD15.mp4">၀၀၃။ လုပ္ခဲ့သမွ် အရာမထင္ (၃) (၁၆.၁၀.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/04-Ashin-SayKaneDa-DVD15.mp4">၀၀၄။ လုပ္ခဲ့သမွ် အရာမထင္ (၄) (၁၆.၁၀.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/05-Ashin-SayKaneDa-DVD15.mp4">၀၀၅။ လုပ္ခဲ့သမွ် အရာမထင္ (၅) (၁၆.၁၀.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/06-Ashin-SayKaneDa-DVD15.mp4">၀၀၆။ လုပ္ခဲ့သမွ် အရာမထင္ (၆) (၁၆.၁၀.၂၀၁၀-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/07-Ashin-SayKaneDa-DVD15.mp4">၀၀၇။ လုပ္ခဲ့သမွ် အရာမထင္ (၇) (၁၇.၁၀.၂၀၁၀-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/08-Ashin-SayKaneDa-DVD15.mp4">၀၀၈။ 
လုပ္ခဲ့သမွ် အရာမထင္ (၈) (၁၇.၁၀.၂၀၁၀-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/09-Ashin-SayKaneDa-DVD15.mp4">၀၀၉။ လုပ္ခဲ့သမွ် အရာမထင္ (၉) (၁၇.၁၀.၂၀၁၀-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-15/10-Ashin-SayKaneDa-DVD15.mp4">၀၁၀။ လုပ္ခဲ့သမွ် အရာမထင္ (၁၀) (၁၇.၁၀.၂၀၁၀-ညေန)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">****dhamma talks uploaded and published on 
								20 Nov 2011****</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၁၇)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-17/01-Ashin-SayKaneDa-DVD17.mp4">
၁။ ဆရာေကာင္းႏွင့္ မလြဲပါေစနဲက&nbsp; (၁၇-၁၁-၂၀၁၀&nbsp; က်ိဳက္ထို)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-17/02-Ashin-SayKaneDa-DVD17.mp4">
၂။ ညီညြတ္လို႕ခ်မ္းသာပါတယ္&nbsp; (၂၁-၁၁-၂၀၁၀&nbsp; ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-17/03-Ashin-SayKaneDa-DVD17.mp4">
၃။ ေဘးကင္းၿငိမ္းေအး&nbsp; (၇-၁၂-၂၀၁၀&nbsp; ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-17/04-Ashin-SayKaneDa-DVD17.mp4">
၄။ လူခ်စ္၊ နတ္ခ်စ္၊ ဘုရားခ်စ္&nbsp; (၁၃-၁၂-၂၀၁၀ လႈိင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-17/05-Ashin-SayKaneDa-DVD17.mp4">
၅။ လုပ္လိုျဖစ္ ျဖစ္လို႕လုပ္ (၁၄-၁၂-၂၀၁၀&nbsp; မရမ္းကုန္း)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၁၈)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/01-Ashin-SayKaneDa-DVD18.mp4">
၁။ ခ်မ္းသာရေၾကာင္း (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/02-Ashin-SayKaneDa-DVD18.mp4">
၂။ ခ်မ္းသာရေၾကာင္း (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/03-Ashin-SayKaneDa-DVD18.mp4">
၃။ ခ်မ္းသာရေၾကာင္း (၃)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/04-Ashin-SayKaneDa-DVD18.mp4">
၄။ ခ်မ္းသာရေၾကာင္း (၄)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/05-Ashin-SayKaneDa-DVD18.mp4">
၅။ ခ်မ္းသာရေၾကာင္း (၅)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/06-Ashin-SayKaneDa-DVD18.mp4">
၆။ ခ်မ္းသာရေၾကာင္း (၆)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/07-Ashin-SayKaneDa-DVD18.mp4">
၇။ ခ်မ္းသာရေၾကာင္း (၇)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/08-Ashin-SayKaneDa-DVD18.mp4">
၈။ ခ်မ္းသာရေၾကာင္း (၈)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-18/09-Ashin-SayKaneDa-DVD18.mp4">
၉။ ခ်မ္းသာရေၾကာင္း (၉)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၁၉)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/01-Ashin-SayKaneDa-DVD19.mp4">
၁။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၁) (၂၁-၁-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/02-Ashin-SayKaneDa-DVD19.mp4">
၂။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၂) (၂၁-၁-၂၀၁၁ ည)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/03-Ashin-SayKaneDa-DVD19.mp4">
၃။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၃) (၂၂-၁-၂၀၁၁ နံနက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/04-Ashin-SayKaneDa-DVD19.mp4">
၄။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၄) (၂၂-၁-၂၀၁၁ ေန႔)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/05-Ashin-SayKaneDa-DVD19.mp4">
၅။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၅) (၂၂-၁-၂၀၁၁ ေန႕လည္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/06-Ashin-SayKaneDa-DVD19.mp4">
၆။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၆) (၂၂-၁-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/07-Ashin-SayKaneDa-DVD19.mp4">
၇။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၇) (၂၂-၁-၂၀၁၁ ည)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/08-Ashin-SayKaneDa-DVD19.mp4">
၈။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၈) (၂၃-၁-၂၀၁၁ နံနက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/09-Ashin-SayKaneDa-DVD19.mp4">
၉။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၉) (၂၃-၁-၂၀၁၁ ေန႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/10-Ashin-SayKaneDa-DVD19.mp4">
၁၀။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၁၀) (၂၃-၁-၂၀၁၁ ေန႕လည္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-19/11-Ashin-SayKaneDa-DVD19.mp4">
၁၁။ ကိုယ္လုပ္ႏိုင္တာပဲ ကိုယ္လုပ္မယ္ (၁၁) (၂၃-၁-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၀)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-20/01-Ashin-SayKaneDa-DVD20.mp4">
၁။ ေမတၱာ&nbsp; (၁၃-၄-၂၀၁၁ ညေန၊ ေမွာဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-20/02-Ashin-SayKaneDa-DVD20.mp4">
၂။ ေလွခြက္ပမာ&nbsp; (၁၃-၄-၂၀၁၁ ည၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-20/03-Ashin-SayKaneDa-DVD20.mp4">
၃။ ျဖတ္လမ္းျဖတ္၊ မကပ္ေစနဲ႕ (၁၄-၄-၂၀၁၁ နံနက္၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-20/04-Ashin-SayKaneDa-DVD20.mp4">
၄။ မ်ိဳလည္းမမ်ိဳနဲ႕၊ ငိုလည္း မငိုနဲ႕ (၁၄-၄-၂၀၁၁ ညေန၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-20/05-Ashin-SayKaneDa-DVD20.mp4">
၅။ သိလို႕က်င့္၍၊ က်င့္လို႕သိ (၁) (၁၄-၄-၂၀၁၁ ည။ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-20/06-Ashin-SayKaneDa-DVD20.mp4">
၆။ သိလို႕က်င့္၍၊ က်င့္လို႕သိ (၂) (၁၅-၄-၂၀၁၁ နံနက္။ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၁)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-21/01-Ashin-SayKaneDa-DVD21.mp4">
၁။ ေနတတ္ပါေစ&nbsp; (၁၅-၄-၂၀၁၁ ညေန၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-21/02-Ashin-SayKaneDa-DVD21.mp4">
၂။ အသိနဲ႕ဆို ၿပီးပါတယ္&nbsp; (၁၅-၄-၂၀၁၁ ည၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-21/03-Ashin-SayKaneDa-DVD21.mp4">
၃။ ေရာင့္ရဲ တင္းတိမ္၊ ေလာဘႏွိမ္ (၁၆-၄-၂၀၁၁ နံနက္၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-21/04-Ashin-SayKaneDa-DVD21.mp4">
၄။ အတြင္စိတ္ေကာင္း၊ ျပင္မိတ္ေကာင္း (၁၆-၄-၂၀၁၁ ညေန၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-21/05-Ashin-SayKaneDa-DVD21.mp4">
၅။ မုန္းေလာက္ေအာင္ေကာင္းလိုက္စမ္းပါ (၁၆-၄-၂၀၁၁ ညေန၊ ေမွာ္ဘီ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၂)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-22/01-Ashin-SayKaneDa-DVD22.mp4">
၁။ တူခ်င္ရင္ တူလို႕ရပါတယ္&nbsp; (၃-၅-၂၀၁၁၊ ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-22/02-Ashin-SayKaneDa-DVD22.mp4">
၂။ သူ႕အတြက္၊ ကိုယ့္အတြက္၊ ဘယ္သူ႕အတြက္ (၄-၅-၂၀၁၁ ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-22/03-Ashin-SayKaneDa-DVD22.mp4">
၃။ မယုံတစ္ဝက္၊ ယုံတစ္ဝက္&nbsp; (၅-၅-၂၀၁၁&nbsp; ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-22/04-Ashin-SayKaneDa-DVD22.mp4">
၄။ သိေတာ့သိတယ္၊ နားမလည္ဘူး&nbsp; (၈-၅-၂၀၁၁&nbsp; ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-22/05-Ashin-SayKaneDa-DVD22.mp4">
၅။ ၿငိမ္းၿပီးေတာ့ ေအးၿပီေပါ့&nbsp; (၉-၅-၂၀၁၁ ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၃)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-23/01-Ashin-SayKaneDa-DVD23.mp4">
၁။ ေပ်ာ္ရာမွာမေန၊ ေတာ္ရာမွာေန&nbsp; (၁၀-၅-၂၀၁၁ ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-23/02-Ashin-SayKaneDa-DVD23.mp4">
၂။ ရွက္လြန္းလို႕&nbsp; (၁၁-၅-၂၀၁၁ ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-23/03-Ashin-SayKaneDa-DVD23.mp4">
၃။ မရွိေတာင့္တ၊ ရွိေၾကာင့္ၾက&nbsp; (၁၂-၅-၂၀၁၁&nbsp; ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-23/04-Ashin-SayKaneDa-DVD23.mp4">
၄။ မဆုံးႏိုင္ပါဘူး&nbsp; (၁၇-၅-၂၀၁၁&nbsp; ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-23/05-Ashin-SayKaneDa-DVD23.mp4">
၅။ မရွိရင္ မစိုးရိမ္ရေတာ့ဘူး&nbsp; (၁၇-၅-၂၀၁၁&nbsp; ကံျမင့္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၄)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/01-Ashin-SayKaneDa-DVD24.mp4">
၁။ ဘယ္သူ႕အတြက္လဲ (၁) (၁၃-၅-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/02-Ashin-SayKaneDa-DVD24.mp4">
၂။ ဘယ္သူ႕အတြက္လဲ (၂) (၁၃-၅-၂၀၁၁ ည)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/03-Ashin-SayKaneDa-DVD24.mp4">
၃။ ဘယ္သူ႕အတြက္လဲ (၃) (၁၄-၅-၂၀၁၁ နံနက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/04-Ashin-SayKaneDa-DVD24.mp4">
၄။ ဘယ္သူ႕အတြက္လဲ (၄) (၁၄-၅-၂၀၁၁ ေန႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/06-Ashin-SayKaneDa-DVD24.mp4">
၆။ ဘယ္သူ႕အတြက္လဲ (၅) (၁၄-၅-၂၀၁၁ ေန႕လည္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/07-Ashin-SayKaneDa-DVD24.mp4">
၇။ ဘယ္သူ႕အတြက္လဲ (၆) (၁၄-၅-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/08-Ashin-SayKaneDa-DVD24.mp4">
၈။ ဘယ္သူ႕အတြက္လဲ (၇) (၁၄-၅-၂၀၁၁ ည)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/09-Ashin-SayKaneDa-DVD24.mp4">
၉။ ဘယ္သူ႕အတြက္လဲ (၈) (၁၅-၅-၂၀၁၁ နံနက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/10-Ashin-SayKaneDa-DVD24.mp4">
၁၀။ ဘယ္သူ႕အတြက္လဲ (၉) (၁၅-၅-၂၀၁၁ ေန႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/11-Ashin-SayKaneDa-DVD24.mp4">
၁၁။ ဘယ္သူ႕အတြက္လဲ (၁၀) (၁၅-၅-၂၀၁၁ ေန႕လည္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-24/12-Ashin-SayKaneDa-DVD24.mp4">
၁၂။ ဘယ္သူ႕အတြက္လဲ (၁၁) (၁၅-၅-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
********** uploaded on 23 Aug 2012 ********************</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၅)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/01-Ashin-SayKaneDa-DVD25.mp4">၁။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၁) (၂၄-၅-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/02-Ashin-SayKaneDa-DVD25.mp4">၂။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၂) (၂၄-၅-၂၀၁၁ ည)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/03-Ashin-SayKaneDa-DVD25.mp4">၃။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၃) (၂၅-၅-၂၀၁၁ နံနက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/04-Ashin-SayKaneDa-DVD25.mp4">၄။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၄) (၂၅-၅-၂၀၁၁ ေန႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/05-Ashin-SayKaneDa-DVD25.mp4">၅။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၅) (၂၅-၅-၂၀၁၁ ေန႕လည္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/06-Ashin-SayKaneDa-DVD25.mp4">၆။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၆) (၂၅-၅-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/07-Ashin-SayKaneDa-DVD25.mp4">၇။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၇) (၂၅-၅-၂၀၁၁ ည)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/08-Ashin-SayKaneDa-DVD25.mp4">၈။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၈) (၂၆-၅-၂၀၁၁ နံနက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-25/09-Ashin-SayKaneDa-DVD25.mp4">၉။ ေစာင့္ခဲ့ရတာၾကာပါၿပီ (၉) (၂၆-၅-၂၀၁၁ ညေန)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၆)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/01-Ashin-SayKaneDa-DVD26.mp4">၁။ တို႕ဘဝ အရေတာ္လိုက္တာ (၁) (၈-၇-၂၀၁၁ -ညေန၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/02-Ashin-SayKaneDa-DVD26..mp4">၂။ တို႕ဘဝ အရေတာ္လိုက္တာ (၂) (၈-၇-၂၀၁၁ -ည၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/03-Ashin-SayKaneDa-DVD26.mp4">၃။ တို႕ဘဝ အရေတာ္လိုက္တာ (၃) (၉-၇-၂၀၁၁ -နံနက္၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/04-Ashin-SayKaneDa-DVD26.mp4">၄။ တို႕ဘဝ အရေတာ္လိုက္တာ (၄) (၉-၇-၂၀၁၁ -နံနက္၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/05-Ashin-SayKaneDa-DVD26.mp4">၅။ တို႕ဘဝ အရေတာ္လိုက္တာ (၅) (၉-၇-၂၀၁၁ -ေန႕လည္၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/06-Ashin-SayKaneDa-DVD26.mp4">၆။ တို႕ဘဝ အရေတာ္လိုက္တာ (၆) (၉-၇-၂၀၁၁ -ညေန၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/07-Ashin-SayKaneDa-DVD26.mp4">၇။ တို႕ဘဝ အရေတာ္လိုက္တာ (၇) (၉-၇-၂၀၁၁ -ည၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/08-Ashin-SayKaneDa-DVD26.mp4">၈။ တို႕ဘဝ အရေတာ္လိုက္တာ (၈) (၁၀-၇-၂၀၁၁ -နံနက္၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/09-Ashin-SayKaneDa-DVD26.mp4">၉။ တို႕ဘဝ အရေတာ္လိုက္တာ (၉) (၁၀-၇-၂၀၁၁ -နံနက္၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/10-Ashin-SayKaneDa-DVD26.mp4">၁၀။ တို႕ဘဝ အရေတာ္လိုက္တာ (၁၀) (၁၀-၇-၂၀၁၁ -ေန႕လည္၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-26/11-Ashin-SayKaneDa-DVD26.mp4">၁၁။ တို႕ဘဝ အရေတာ္လိုက္တာ (၁၁) (၁၀-၇-၂၀၁၁ -ညေန၊ ျပင္ဦးလြင္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၇)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-27/01-Ashin-SayKaneDa-DVD27.mp4">၁။ ေပ်ာ္ေပ်ာ္ပဲ နိဗၺာန္သြားမယ္ (၆-၁၂-၂၀၁၁ - လမ္းမေတာ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-27/02-Ashin-SayKaneDa-DVD27.mp4">၂။ ယူသာယူ ၾကည္ျဖဴပါတယ္&nbsp; (၂၉-၁၂-၂၀၁၁ - လသာ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-27/03-Ashin-SayKaneDa-DVD27.mp4">၃။ ကိုယ့္ကိုကိုယ္လည္းသိ၊ သူလည္းသိ (၇-၁-၂၀၁၂ - ေက်ာက္တံတား)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-27/04-Ashin-SayKaneDa-DVD27.mp4">၄။ တစ္လမ္းစီပါပဲ (၁၁-၁-၂၀၁၂ - အမာရြတ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">DVD အမွတ္စဥ္ (၂၈)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-28/01-Ashin-SayKaneDa-DVD28.mp4">၁။ မကယ္ႏိုင္ပါဘူး (၇-၁၂-၂၀၁၁ - အလုံ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-28/02-Ashin-SayKaneDa-DVD28.mp4">၂။ သြားတတ္ရင္ ေရာက္ပါတယ္ (၁၇-၁-၂၀၁၂ - လသာ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-28/03-Ashin-SayKaneDa-DVD28.mp4">၃။ ပီတိျဖစ္ေကာင္းလွပါတယ္ (၂၂-၁-၂၀၁၂ - ဗဟန္း)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-28/04-Ashin-SayKaneDa-DVD28.mp4">၄။ တို႕ဘဝ အရေတာ္လိုက္တာ (၂၇-၁၀-၂၀၁၁ - သာေကတ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">အမွတ္စဥ္(၂၉)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-29/01-Ashin-SayKaneDa-DVD29.mp4">
၁။ ေနတတ္ ထိုင္တတ္ပါမွ(၂၃.၈.၂၀၁၁-ကံၿမင္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-29/02-Ashin-SayKaneDa-DVD29.mp4">
၂။ ေနတတ္ ထိုင္တတ္ပါမွ(၂၄.၈.၂၀၁၁-ကံၿမင္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-29/03-Ashin-SayKaneDa-DVD29.mp4">
၃။ ေနတတ္ ထိုင္တတ္ပါမွ(၂၅.၈.၂၀၁၁-ကံၿမင္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-29/04-Ashin-SayKaneDa-DVD29.mp4">
၄။ ေနတတ္ ထိုင္တတ္ပါမွ(၂၆.၈.၂၀၁၁-ကံၿမင္႕)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္(၃၀)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-30/01-Ashin-SayKaneDa-DVD30.mp4">
၁။ သတိတစ္လံုး လက္ကိုင္သံုး(၁၄.၄.၂၀၀၈-ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-30/02-Ashin-SayKaneDa-DVD30.mp4">
၂။ သတိတစ္လံုး လက္ကိုင္သံုး(၂)(၁၅.၄.၂၀၀၈-ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-30/03-Ashin-SayKaneDa-DVD30.mp4">
၃။ သတိတစ္လံုး လက္ကိုင္သံုး(၃)(၁၆.၄.၂၀၀၈-ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-30/04-Ashin-SayKaneDa-DVD30.mp4">
၄။ လြတ္လြတ္လပ္လပ္ ေနခ်င္ပါၿပီ(၃.၄.၂၀၁၂-ကံၿမင္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-30/05-Ashin-SayKaneDa-DVD30.mp4">
၅။ လြတ္လြတ္လပ္လပ္ ေနခ်င္ပါၿပီ(၂)(၄.၄.၂၀၁၂-ကံၿမင္႕)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္(၃၁)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-31/01-Ashin-SayKaneDa-DVD31.mp4">
၁။ သိမ္းမထားခ်င္ေတာ႕ဘူး(၁၆.၂.၂၀၀၈-ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-31/02-Ashin-SayKaneDa-DVD31.mp4">
၂။ ၾကံဳရၾကံဳရ ဘံုဘ၀မွာၿဖင္႕(၇.၃.၂၀၀၈-ေတာင္ၾကီး)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-31/03-Ashin-SayKaneDa-DVD31.mp4">
၃။ စိတ္ပူမိပါေသးတယ္(၇.၅.၂၀၁၂-ကံၿမင္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-31/04-Ashin-SayKaneDa-DVD31.mp4">
၄။ သည္းမခံခ်င္ေတာ႕ဘူး(၈.၅.၂၀၁၂-ကံၿမင္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-31/05-Ashin-SayKaneDa-DVD31.mp4">
၅။ အနာရွိယင္ေဆးသိပါတယ္(၉.၅.၂၀၁၂-ကံၿမင္႕)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္(၃၂)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/01-Ashin-SayKaneDa-DVD32.mp4">
၁။ အဆင္ေၿပေအာင္ေနပါ႕မယ္(၂၂.၇.၂၀၁၁-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/02-Ashin-SayKaneDa-DVD32.mp4">
၂။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၂)(၂၂.၇.၂၀၁၁-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/03-Ashin-SayKaneDa-DVD32.mp4">
၃။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၃)(၂၃.၇.၂၀၁၁-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/04-Ashin-SayKaneDa-DVD32.mp4">
၄။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၄)(၂၃.၇.၂၀၁၁-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/05-Ashin-SayKaneDa-DVD32.mp4">
၅။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၅)(၂၃.၇.၂၀၁၁-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/06-Ashin-SayKaneDa-DVD32.mp4">
၆။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၆)(၂၃.၇.၂၀၁၁-ညေန)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/07-Ashin-SayKaneDa-DVD32.mp4">
၇။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၇)(၂၃.၇.၂၀၁၁-ည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/08-Ashin-SayKaneDa-DVD32.mp4">
၈။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၈)(၂၄.၇.၂၀၁၁-နံနက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/09-Ashin-SayKaneDa-DVD32.mp4">
၉။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၉)(၂၄.၇.၂၀၁၁-ေန႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/10-Ashin-SayKaneDa-DVD32.mp4">
၁၀။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၁၀)(၂၄.၇.၂၀၁၁-ေန႕လည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-32/11-Ashin-SayKaneDa-DVD32.mp4">
၁၁။ အဆင္ေၿပေအာင္ေနပါ႕မယ္-အပိုင္း(၁၁)(၂၄.၇.၂၀၁၁-ညေန)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္(၃၃)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-33/01-Ashin-SayKaneDa-DVD33.mp4">
၁။ လိုရာခရီးေရာက္ဖို႕(မဂၤလာေတာင္ညြန္႕)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-33/02-Ashin-SayKaneDa-DVD33.mp4">
၂။ ဆြဲရာေနာက္လိုက္ေနၾကတယ္(သာေကတ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-33/03-Ashin-SayKaneDa-DVD33.mp4">
၃။ အရွံဳးထဲကအၿမတ္(လွိဳင္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-33/04-Ashin-SayKaneDa-DVD33.mp4">
၄။ ေခၚရာေနာက္ကို လိုက္ေနၾကတယ္(ေက်ာက္တံတား)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-33/05-Ashin-SayKaneDa-DVD33.mp4">
၅။ တစ္ခါေသဘူး ပ်ဥ္ဖိုးနားလည္(ေက်ာက္တံတား)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-33/06-Ashin-SayKaneDa-DVD33.mp4">
၆။ သူေခၚရာေနာက္ လိုက္ေနရတယ္(မဂၤလာေတာင္ညြန္႕)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္(၃၄)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/01-Ashin-SayKaneDa-DVD34.mp4">
၁။ ဗုဒၶါႏုႆတိ(၁)(၉.၅.၂၀၁၁-စမ္းေခ်ာင္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/02-Ashin-SayKaneDa-DVD34.mp4">
၂။ ဗုဒၶါႏုႆတိ(၂)(၉.၅.၂၀၁၁-ကမာရြတ္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/03-Ashin-SayKaneDa-DVD34.mp4">
၃။ ဗုဒၶါႏုႆတိ(၃)(၁၀.၅.၂၀၁၁-လွိဳင္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/04-Ashin-SayKaneDa-DVD34.mp4">
၄။ ဗုဒၶါႏုႆတိ(၄)(၁၀.၅.၂၀၁၁-ပုဇြန္ေတာင္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/05-Ashin-SayKaneDa-DVD34.mp4">
၅။ ဗုဒၶါႏုႆတိ(၅)(၁၁.၅.၂၀၁၁-တာေမြ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/06-Ashin-SayKaneDa-DVD34.mp4">
၆။ ဗုဒၶါႏုႆတိ(၆)(၁၁.၅.၂၀၁၁-ကမာရြတ္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/07-Ashin-SayKaneDa-DVD34.mp4">
၇။ ဗုဒၶါႏုႆတိ(၇)(၁၂.၅.၂၀၁၁-ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/08-Ashin-SayKaneDa-DVD34.mp4">
၈။ ဗုဒၶါႏုႆတိ(၈)(၁၃.၅.၂၀၁၁-ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/09-Ashin-SayKaneDa-DVD34.mp4">
၉။ ဗုဒၶါႏုႆတိ(၉)(၁၃.၅.၂၀၁၁- ကမာရြတ္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-34/10-Ashin-SayKaneDa-DVD34.mp4">
၁၀။ ဗုဒၶါႏုႆတိ(၁၀)(၁၃.၅.၂၀၁၁-ေမွာ္ဘီ)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္(၃၇)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/01-Ashin-SayKaneDa-DVD37.mp4">
၁။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/02-Ashin-SayKaneDa-DVD37.mp4">
၂။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/03-Ashin-SayKaneDa-DVD37.mp4">
၃။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/04-Ashin-SayKaneDa-DVD37.mp4">
၄။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/05-Ashin-SayKaneDa-DVD37.mp4">
၅။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၅)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/06-Ashin-SayKaneDa-DVD37.mp4">
၆။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၆)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/07-Ashin-SayKaneDa-DVD37.mp4">
၇။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၇)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/08-Ashin-SayKaneDa-DVD37.mp4">
၈။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၈)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/09-Ashin-SayKaneDa-DVD37.mp4">
၉။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၉)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-37/10-Ashin-SayKaneDa-DVD37.mp4">
၁၀။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၁၀)</a><br>
၁၁။ တကၠသိုလ္၀င္တန္းမ်ားသို႕(အပိုင္း-၁၁)<br>
<br>
<br>
<br>
အမွတ္စဥ္(၃၈)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-38/01-Ashin-SayKaneDa-DVD38.mp4">
၁။ ယဥ္ေက်းလိမၼာ(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-38/02-Ashin-SayKaneDa-DVD38.mp4">
၂။ ယဥ္ေက်းလိမၼာ(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-38/03-Ashin-SayKaneDa-DVD38.mp4">
၃။ ယဥ္ေက်းလိမၼာ(၃)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-38/04-Ashin-SayKaneDa-DVD38.mp4">
၄။ ယဥ္ေက်းလိမၼာ(၄)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-38/05-Ashin-SayKaneDa-DVD38.mp4">
၅။ ယဥ္ေက်းလိမၼာ(၅)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">****dhamma talks uploaded and published on 
								26 March 2013 ****</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">အမွတ္စဥ္ (၃၉) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-39/01-Ashin-SayKaneDa-DVD39.mp4">၁။ အၿမဲတမ္းအမည္ရွိေသာ (ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-39/02-Ashin-SayKaneDa-DVD39.mp4">၂။ အပူေဝးမွ ေအးပါတယ္ (ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-39/03-Ashin-SayKaneDa-DVD39.mp4">၃။ အျမင္တူမွ အတူျမင္မယ္ (ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-39/04-Ashin-SayKaneDa-DVD39.mp4">၄။ ကုသိုလ္တန္ဘုိး (မရမ္းကုန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-39/05-Ashin-SayKaneDa-DVD39.mp4">၅။ တရားသိမွျဖစ္မယ္ (ကမာၻေအး - မရမ္းကုန္း) 
</a> <br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၄၆) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-46/01-Ashin-SayKaneDa-DVD46.mp4">၁။ ေနရာေလးေတာ့ ယူေပးပါ (၄.၇.၂၀၁၂ - ကံျမင့္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-46/02-Ashin-SayKaneDa-DVD46.mp4">၂။ ေနရာေလးေတာ့ ယူေပးပါ (၅.၇.၂၀၁၂ - ကံျမင့္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-46/03-Ashin-SayKaneDa-DVD46.mp4">၃။ ေနရာေလးေတာ့ ယူေပးပါ (၄.၇.၂၀၁၂ - ကံျမင့္)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၄၇) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-47/01-Ashin-SayKaneDa-DVD47.mp4">၁။ ေရႊတံခါးႀကီးဖြင့္ပါဦး (နဝမအႀကိမ္၊ ယဥ္ေက်းလိမၼာ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-47/02-Ashin-SayKaneDa-DVD47.mp4">၂။ ၁၂-ႏွစ္ေအာက္ - ယဥ္ေက်းလိမၼာ (2011-Informatic – Singapore) 
</a> <br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-47/03-Ashin-SayKaneDa-DVD47.mp4">၃။ ၁၂-ႏွစ္အထက္ - ယဥ္ေက်းလိမၼာ (2011-Informatic – Singapore) 
</a> <br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-47/04-Ashin-SayKaneDa-DVD47.mp4">၄။ ၁၂-ႏွစ္အထက္ - ယဥ္ေက်းလိမၼာ (English) (2011-Imformatic – Singapore) 
</a> <br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-47/05-Ashin-SayKaneDa-DVD47.mp4">၅။ ၇-ႏွစ္မွ ၁၅-ႏွစ္အထိ - ယဥ္ေက်းလိမၼာ (2011 – Poh Ean Shi Temple-Singapore)
</a> <br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-47/06-Ashin-SayKaneDa-DVD47.mp4">၆။ ၁၅-ႏွစ္မွ ၂၀-ႏွစ္အထိ - ယဥ္ေက်းလိမၼာ (2011 – Poh Ean Shi Temple-Singapore)
</a> <br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၀) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-50/01-Ashin-SayKaneDa-DVD50.mp4">၁။ မလြယ္ပါဘူး (၁) (၂၇.၈.၂၀၁၂ - ကံျမင့္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-50/02-Ashin-SayKaneDa-DVD50.mp4">၂။ မလြယ္ပါဘူး (၂) (၂၈.၈.၂၀၁၂ - ကံျမင့္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-50/03-Ashin-SayKaneDa-DVD50.mp4">၃။ မလြယ္ပါဘူး (၃) (၂၉.၈.၂၀၁၂ - ကံျမင့္)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၁)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-51/01-Ashin-SayKaneDa-DVD51.mp4">၁။ ဓမၼပဒ (အပိုင္း - ၁) (၉.၈.၂၀၁၂ - ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-51/02-Ashin-SayKaneDa-DVD51.mp4">၂။ ဓမၼပဒ (အပိုင္း - ၂) (၁၆.၈.၂၀၁၂ - ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-51/03-Ashin-SayKaneDa-DVD51.mp4">၃။ ဓမၼပဒ (အပိုင္း - ၃) (၃၀.၈.၂၀၁၂ - ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-51/04-Ashin-SayKaneDa-DVD51.mp4">၄။ ဓမၼပဒ (အပိုင္း - ၄) (၆.၉.၂၀၁၂ - ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-51/05-Ashin-SayKaneDa-DVD51.mp4">၅။ ဓမၼပဒ (အပိုင္း - ၅) (၁၃.၉.၂၀၁၂ - ဗဟန္း)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၂) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-52/01-Ashin-SayKaneDa-DVD52.mp4">၁။ ေခါင္းေဆာင္ေကာင္းတို႔၏အရည္အခ်င္း (၁) (ယုဇနတာဝါ)</a><br>
၂။ ေခါင္းေဆာင္ေကာင္းတို႔၏အရည္အခ်င္း (၂) (ယုဇနတာဝါ)<br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-52/03-Ashin-SayKaneDa-DVD52.mp4">၃။ ေခါင္းေဆာင္ေကာင္းတို႔၏အရည္အခ်င္း (၃) (ယုဇနတာဝါ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-52/04-Ashin-SayKaneDa-DVD52.mp4">၄။ ေခါင္းေဆာင္ေကာင္းတို႔၏အရည္အခ်င္း (၄) (ယုဇနတာဝါ)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၃) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-53/01-Ashin-SayKaneDa-DVD53.mp4">၁။ ၾကည္ညိဳရင္းစြဲ ရွိလို႔ပါ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-53/02-Ashin-SayKaneDa-DVD53.mp4">၂။ အားကိုးရင္းစြဲ ရွိလို႔ပါ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-53/03-Ashin-SayKaneDa-DVD53.mp4">၃။ အက်ဳိးၾကည့္ရင္းစြဲ ရွိလို႔ပါ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-53/04-Ashin-SayKaneDa-DVD53.mp4">၄။ အျပစ္ျမင္ရင္းစြဲ ရွိလို႔ပါ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-53/05-Ashin-SayKaneDa-DVD53.mp4">၅။ စကားေျပာရင္းစြဲ ရွိလို႔ပါ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၄) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-54/01-Ashin-SayKaneDa-DVD54.mp4">၁။ နံနက္ခင္း အသိေပး (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-54/02-Ashin-SayKaneDa-DVD54.mp4">၂။ ပဋိစၥသမုပၸါဒ္ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-54/03-Ashin-SayKaneDa-DVD54.mp4">၃။ အသိေပး (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-54/04-Ashin-SayKaneDa-DVD54.mp4">၄။ အသိမေပ်ာက္တဲ့ သတိ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-54/05-Ashin-SayKaneDa-DVD54.mp4">၅။ ဘာဝနာအလုပ္ေပး (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-54/06-Ashin-SayKaneDa-DVD54.mp4">၆။ ဉာဏ္အျမင္သံုးပါး (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၅)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-55/01-Ashin-SayKaneDa-DVD55.mp4">၁။ ထပ္ထပ္ထည့္မိလို႔ပါ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-55/02-Ashin-SayKaneDa-DVD55.mp4">၂။ သူမရွိလို႔ မျဖစ္ဘူး (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-55/03-Ashin-SayKaneDa-DVD55.mp4">၃။ ေကာင္းေသာလာျခင္း ျဖစ္ပါေပတယ္ (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-55/04-Ashin-SayKaneDa-DVD55.mp4">၄။ အတြက္မွား (ေဆကိႏၵာရာမေက်ာင္းတိုက္ - ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-55/05-Ashin-SayKaneDa-DVD55.mp4">၅။ အထင္ေသးရင္ ရင္ေလးစရာ (ေရႊျပည္သာ)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၆) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-56/01-Ashin-SayKaneDa-DVD56.mp4">၁။ နီးနီးေလးနဲ႔ေဝးေနတယ္ (၁) (၂၄.၉.၂၀၁၂ - ကံျမင့္ေက်ာင္းတိုက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-56/02-Ashin-SayKaneDa-DVD56.mp4">၂။ နီးနီးေလးနဲ႔ေဝးေနတယ္ (၂) (၂၅.၉.၂၀၁၂ - ကံျမင့္ေက်ာင္းတိုက္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-56/03-Ashin-SayKaneDa-DVD56.mp4">၃။ နီးနီးေလးနဲ႔ေဝးေနတယ္ (၃) (၂၆.၉.၂၀၁၂ - ကံျမင့္ေက်ာင္းတိုက္)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
အမွတ္စဥ္ (၅၇) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-57/01-Ashin-SayKaneDa-DVD57.mp4">၁။ ေနာက္ျပန္မဆုတ္စတမ္း (၆.၁.၂၀၁၃ - မဂၤလာေတာင္ညြန္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-57/02-Ashin-SayKaneDa-DVD57.mp4">၂။ အားကိုးပါရေစ (၂၉.၁၂.၂၀၁၂ - တာေမြ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-57/03-Ashin-SayKaneDa-DVD57.mp4">၃။ အားကိုးစရာ (၁၈.၁၁.၂၀၁၂ - အလံု)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-57/04-Ashin-SayKaneDa-DVD57.mp4">၄။ မိဘရိပ္မွာေနပါ့မယ္ (၂၇.၁၁.၂၀၁၂ - စမ္းေခ်ာင္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-57/05-Ashin-SayKaneDa-DVD57.mp4">၅။ မိဘနဲ႔ပဲ ေနေတာ့မယ္ (၂၄.၁၀.၂၀၁၂ - မရမ္းကုန္း) 
</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">အမွတ္စဥ္ (၅၈) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">အမွတ္စဥ္ (၅၉) </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-59/DVD-59-Title-01-Ashin-SayKaneDa.mp4">၁။ ျပည္႕စုံရင္ ႀကီးပြားပါတယ္ (၈-၁-၂၀၁၄ - ေတာင္ဒဂုံ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-59/DVD-59-Title-02-Ashin-SayKaneDa.mp4">၂။ အသိမေပ်ာက္တဲ့ သတိ (၉-၁-၂၀၁၄- ေဆကိႏၵရာမေက်ာင္းတိုက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-59/DVD-59-Title-03-Ashin-SayKaneDa.mp4">၃။ မရွိရင္ မစိုးရိမ္ရေတာ့ဘူး (၁-၈-၂၀၁၁ - ကံျမင့္ေက်ာင္းတိုက္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-59/DVD-59-Title-04-Ashin-SayKaneDa.mp4">၄။ မလြန္ပါေစနဲ႕ (၅-၅-၂၀၁၂ - ဆြာၿမိဳ႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">အမွတ္စဥ္ (၆၀)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-60/DVD-60-Title-01-Ashin-SayKaneDa.mp4">၁။ အသိဥာဏ္ အရြယ္ေရာက္ခ်င္ၿပီ (ရန္ကုန္ၿမိဳ႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-60/DVD-60-Title-02-Ashin-SayKaneDa.mp4">၂။ သူေခၚရာေနာက္ လိုက္ေနရတယ္ (မဂၤလာေတာင္ညြန္႕)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-60/DVD-60-Title-03-Ashin-SayKaneDa.mp4">၃။ ျပည္႕စုံရင္ ႀကီးပြားပါတယ္ (ေတာင္ဒဂုံ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-60/DVD-60-Title-04-Ashin-SayKaneDa.mp4">၄။ ကိုယ္ျဖစ္ခ်င္တာ ျဖစ္ပါတယ္ (လမ္းမေတာ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com//MP4Library/Ashin-SayKaneDa/DVD-60/DVD-60-Title-05-Ashin-SayKaneDa.mp4">၅။ လုပ္ရပ္ႏွင့္ စိတ္ဓါတ္ (သာေကတ)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">အမွတ္စဥ္ (၆၁)</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-61/01-Ashin-SayKaneDa-DVD61.mp4">၁။ ေခါင္းေဆာင္ေကာင္းျဖစ္ခ်င္လိုက္တာ (၁၈-၂-၂၀၁၅ - 
အင္းစိန္ၿမိဳ႕နယ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-61/02-Ashin-SayKaneDa-DVD61.mp4">၂။ ပါရမီရွင္ေကာင္း (၁-၃-၂၀၁၅ - ေတာင္ဥကၠလာပၿမိဳ႕နယ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/DhammaDuta-AshinSayKaneDa/DVD-61/03-Ashin-SayKaneDa-DVD61.mp4">၃။ ကိုယ့္ဘဝ ကိုယ္ေက်နပ္ပါတယ္ (၂-၅-၂၀၁၅ - တာေမြၿမိဳ႕နယ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">&nbsp;<br>
<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
                                &nbsp;</p>
								</div>
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
    
