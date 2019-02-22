from bs4 import BeautifulSoup as bs4
import re
one = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 


	




<!-- Start dhammadownload menu top and side bar -->



<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>

<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 542px; top: 12px;" id="layer23">
	<img src="images/MyaSatKyarSayadaw-Bhaddanta-Indakabhivamsa.gif" width="300" height="222" border="0"></div>
	


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






	
	
	
	
<div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 218px; top: 156px" id="layer24" font="" face="Zawgyi-One">
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">
									Mya Sat Kyar Sayadaw</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">
									Bhaddanta Indakabhivamsa</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">စစ္ကိုင္းေတာင္ရိုး၊ 
									ေသာတာပန္ရပ္၊ ျမစၾကာေက်ာင္းတိုက္</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">ပဓာန နာယကဆရာေတာ္</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">ဘဒၵႏ ၱဣႏၵကာဘိဝံသ</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									************</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="6">စာသင္သားမ်ားအတြက္ </font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="6">ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="6">&nbsp;</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား 
									အမွတ္စဥ္ (၁)</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/001-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁။ ၁၃၆၆ ခုႏွစ္ ေတာ္သလင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/002-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂။ ၁၃၆၆ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/003-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃။ ၁၃၆၆ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/004-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄။ ၁၃၆၆ ခုႏွစ္ သီတင္းကၽြတ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/005-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅။ ၁၃၆၆ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/006-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆။ ၁၃၆၆ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/007-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇။ ၁၃၆၆ ခုႏွစ္ ျပာသိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/008-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈။ ၁၃၆၆ ခုႏွစ္ တပို႕တြဲလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/009-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉။ ၁၃၆၆ ခုႏွစ္ တေပါင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/010-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၀။ ၁၃၆၆ ခုႏွစ္&nbsp; တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/011-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၁။ ၁၃၆၇ ခုႏွစ္ ဦးတန္ခူးလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/012-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၂။ ၁၃၆၇ ခုႏွစ္ ဦးတန္ခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/013-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၃။ ၁၃၆၇ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/014-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၄။ ၁၃၆၇ ခုႏွစ္ ကဆုန္လျပည္႕ေက်ာ္ (၈)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/015-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၅။ ၁၃၆၇ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/016-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၆။ ၁၃၆၇ ခုႏွစ္ ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/017-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၇။ ၁၃၆၇ ခုႏွစ္ ဝါဆိုလျပည္႕ေက်ာ္ (၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/018-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၈။ ၁၃၆၇ ခုႏွစ္ ဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/019-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၁၉။ ၁၃၆၇ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/020-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၀။ ၁၃၆၇ ခုႏွစ္ ေတာ္သလင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/021-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၁။ ၁၃၆၇ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/022-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၂။ ၁၃၆၇ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ေက်ာ္ 
									(၈)ရက္ေန႔ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/023-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၃။ ၁၃၆၇ ခုႏွစ္ သီတင္းကၽြတ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/024-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၄။ ၁၃၆၇ ခုႏွစ္ တန္ေဆာင္မုန္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/025-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၅။ ၁၃၆၇ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/026-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၆။ ၁၃၆၇ ခုႏွစ္ နတ္ေတာ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/027-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၇။ ၁၃၆၇ ခုႏွစ္ ျပာသိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/028-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၈။ ၁၃၆၇ ခုႏွစ္ တပို႕တြဲလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/029-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၂၉။ ၁၃၆၇ ခုႏွစ္ တပို႕တြဲလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/030-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၀။ ၁၃၆၇ ခုႏွစ္ တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/031-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၁။ ၁၃၆၈ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/032-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၂။ ၁၃၆၈ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/033-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၃။ ၁၃၆၈ ခုႏွစ္ နယုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/034-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၄။ ၁၃၆၈ ခုႏွစ္ နယုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/035-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၅။ ၁၃၆၈ ခုႏွစ္ ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/036-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၆။ ၁၃၆၈ ခုႏွစ္ ဝါဆိုလျပည္႕ေက်ာ္(၂)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/037-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၇။ ၁၃၆၈ ခုႏွစ္ ဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/038-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၈။ ၁၃၆၈ ခုႏွစ္ ဝါေခါင္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/039-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၃၉။ ၁၃၆၈ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/040-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၀။ ၁၃၆၈ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/041-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၁။ ၁၃၆၈ ခုႏွစ္ 
									သီတင္းကၽြတ္လျပည္႕ေက်ာ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/042-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၂။ ၁၃၆၈ ခုႏွစ္ သီတင္းကၽြတ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/043-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၃။ ၁၃၆၈ ခုႏွစ္ တန္ေဆာင္မုန္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/044-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၄။ ၁၃၆၈ ခုႏွစ္ 
									တန္ေဆာင္မုန္းလျပည္႕ေက်ာ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/045-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၅။ ၁၃၆၈ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/046-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၆။ ၁၃၆၈ ခုႏွစ္ ျပာသိုလျပည္႕ေက်ာ္(၈)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/047-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၇။ ၁၃၆၈ ခုႏွစ္ ျပာသိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/048-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၈။ ၁၃၆၈ ခုႏွစ္ တပို႕တြဲလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/049-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၄၉။ ၁၃၆၈ ခုႏွစ္ တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/050-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၀။ ၁၃၆၈ ခုႏွစ္ ေႏွာင္းတန္ခူးလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/051-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၁။ ၁၃၆၈ ခုႏွစ္ ေႏွာင္တန္းခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/052-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၂။ ၁၃၆၉ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/053-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၃။ ၁၃၆၉ ခုႏွစ္ ကဆုန္လျပည္႕ေက်ာ္ (၁၂)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/054-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၄။ ၁၃၆၉ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/055-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၅။ ၁၃၆၉ ခုႏွစ္ နယုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/056-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၆။ ၁၃၆၉ ခုႏွစ္ ပထမဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/057-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၇။ ၁၃၆၉ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/058-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၈။ ၁၃၆၉ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ေက်ာ္(၁)ရက္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/059-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၅၉။ ၁၃၆၉ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ေက်ာ္(၈)ရက္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/060-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၀။ ၁၃၆၉ ခုႏွစ္ ဒု-ဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/061-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၁။ ၁၃၆၉ ခုႏွစ္ ဝါေခါင္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/062-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၂။ ၁၃၆၉ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/063-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၃။ ၁၃၆၉ ခုႏွစ္ သီတင္းကၽြတ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/064-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၄။ ၁၃၆၉ ခုႏွစ္ တန္ေဆာင္မုန္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/065-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၅။ ၁၃၆၉ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/066-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၆။ ၁၃၆၉ ခုႏွစ္ နတ္ေတာ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/067-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၇။ ၁၃၆၉ ခုႏွစ္ တပို႕တြဲလဆန္း(၈)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/068-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၈။ ၁၃၆၉ ခုႏွစ္ တပို႕တြဲလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/069-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၆၉။ ၁၃၆၉ ခုႏွစ္ တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/070-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၀။ ၁၃၇၀ ခုႏွစ္ ဦးတန္းခူးလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/071-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၁။ ၁၃၇၀ ခုႏွစ္ ဦးတန္ခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/072-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၂။ ၁၃၇၀ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/073-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၃။ ၁၃၇၀ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/074-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၄။ ၁၃၇၀ ခုႏွစ္ ဝါဆိုလျပည္႕ေက်ာ္ (၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/075-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၅။ ၁၃၇၀ ခုႏွစ္ ဝါဆိုလျပည္႕ေက်ာ္(၁)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/076-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၆။ ၁၃၇၀ ခုႏွစ္ ေတာ္သလင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/077-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၇။ ၁၃၇၀ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/078-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၈။ ၁၃၇၀ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ေက်ာ္ 
									(၁)ရက္ေန႔ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/079-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၇၉။ ၁၃၇၀ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/080-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၀။ ၁၃၇၀ ခုႏွစ္ တန္ေဆာင္မုန္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/081-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၁။ ၁၃၇၀ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/082-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၂။ ၁၃၇၀ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/083-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၃။ ၁၃၇၀ ခုႏွစ္ ျပာသိုလျပည္႕ေက်ာ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/084-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၄။ ၁၃၇၀ ခုႏွစ္ ျပာသိုလျပည္႕ေက်ာ္(၁၂)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/085-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၅။ ၁၃၇၀ ခုႏွစ္ တပို႕တြဲလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/086-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၆။ ၁၃၇၀ ခုႏွစ္ တပို႕တြဲလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/087-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၇။ ၁၃၇၀ ခုႏွစ္ တေပါင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/088-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၈။ ၁၃၇၀ ခုႏွစ္ ေႏွာင္းတန္ခူးလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/089-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၈၉။ ၁၃၇၁ ခုႏွစ္ ဦးတန္ခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/090-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၀။ ၁၃၇၁ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/091-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၁။ ၁၃၇၁ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/092-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၂။ ၁၃၇၁ ခုႏွစ္ နယုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/093-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၃။ ၁၃၇၁ ခုႏွစ္ ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/094-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၄။ ၁၃၇၁ ခုႏွစ္ ဝါဆိုလျပည္႕ေက်ာ္(၁၄)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/095-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၅။ ၁၃၇၁ ခုႏွစ္ ဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-01/096-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-01.mp3">
									၉၆။ ၁၃၇၁ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား 
									အမွတ္စဥ္ (၂)</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/001-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁။ ၁၃၇၁ ခုႏွစ္ ေတာ္သလင္းလဆန္း(၈)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/002-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၂။ ၁၃၇၁ ခုႏွစ္ ေတာ္သလင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/003-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၃။ ၁၃၇၁ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/004-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၄။ ၁၃၇၁ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/005-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၅။ ၁၃၇၁ ခုႏွစ္ သီတင္းကၽြတ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/006-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၆။ ၁၃၇၁ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/007-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၇။ ၁၃၇၁ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/008-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၈။ ၁၃၇၁ ခုႏွစ္ ျပာသိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/009-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၉။ ၁၃၇၁ ခုႏွစ္ တပို႕တြဲလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/010-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၀။ ၁၃၇၁ ခုႏွစ္ တေပါင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/011-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၁။ ၁၃၇၁ ခုႏွစ္ ေႏွာင္တန္းခူးလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/012-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၂။ ၁၃၇၁ ခုႏွစ္ ေႏွာင္တန္ခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/013-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၃။ ၁၃၇၂ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/014-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၄။ ၁၃၇၂ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/015-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၅။ ၁၃၇၂ ခုႏွစ္ နယုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၁၆။ ၁၃၇၂ ခုႏွစ္ နယုန္လကြယ္ည</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/017-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၇။ ၁၃၇၂ ခုႏွစ္ ပထမဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/018-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၈။ ၁၃၇၂ ခုႏွစ္ ပထမဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/019-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၁၉။ ၁၃၇၂ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/020-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၂၀။ ၁၃၇၂ ခုႏွစ္ ဒု-ဝါဆိုလဆုတ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/021-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၂၁။ ၁၃၇၂ ခုႏွစ္ ဒု-ဝါဆိုလဆုတ္(၇)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-02/022-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-02.mp3">
									၂၂။ ၁၃၇၂ ခုႏွစ္ ဒု-ဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား 
									အမွတ္စဥ္ (၃)</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/001-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁။ ၁၃၇၂ ခုႏွစ္ ဝါေခါင္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/002-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၂။ ၁၃၇၂ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/003-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၃။ ၁၃၇၂ ခုႏွစ္ ေတာ္သလင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/004-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၄။ ၁၃၇၂ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/005-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၅။ ၁၃၇၂ ခုႏွစ္ သီတင္းကႊတ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/006-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၆။ ၁၃၇၂ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ေက်ာ္(၈)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/007-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၇။ ၁၃၇၂ ခုႏွစ္ သီတင္းကၽြတ္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/008-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၈။ ၁၃၇၂ ခုႏွစ္ တန္ေဆာင္မုန္းလျပ္ည႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/009-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၉။ ၁၃၇၂ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/010-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၀။ ၁၃၇၂ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/011-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၁။ ၁၃၇၂ ခုႏွစ္ တေပါင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/012-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၂။ ၁၃၇၂ ခုႏွစ္ တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/013-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၃။ ၁၃၇၃ ခုႏွစ္ ဦးတန္ခူးလျပည္႕ေက်ာ္(၂)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/014-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၄။ ၁၃၇၃ ခုႏွစ္ ဥိးတန္ခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/015-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၅။ ၁၃၇၃ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/016-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၆။ ၁၃၇၃ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/017-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၇။ ၁၃၇၃ ခုႏွစ္ နယုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-03/018-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-03.mp3">
									၁၈။ ၁၃၇၃ ခုႏွစ္ နယုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား 
									အမွတ္စဥ္ (၄)</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/001-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁။ ၁၃၇၃ ခုႏွစ္ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/002-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၂။ ၁၃၇၃ ခုႏွစ္ ဝါဆိုလျပည္႕ေက်ာ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/003-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၃။ ၁၃၇၃ ခုႏွစ္ ဝါဆိုလျည္႕ေက်ာ္(၄)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/004-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၄။ ၁၃၇၃ ခုႏွစ္ ဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/005-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၅။ ၁၃၇၃ ခုႏွစ္ ဝါေခါင္လဆန္း(၈)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/006-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၆။ ၁၃၇၃ ခုႏွစ္ ဝါေခါင္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/007-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၇။ ၁၃၇၃ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/008-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၈။ ၁၃၇၃ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/009-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၉။ ၁၃၇၃ ခုႏွစ္ သီတင္းကၽြတ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/010-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၀။ ၁၃၇၃ ခုႏွစ္ တန္ေဆာင္မုန္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/011-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၁။ ၁၃၇၃ ခုႏွစ္ တန္ေဆာင္မုန္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/012-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၂။ ၁၃၇၃ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/013-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၃။ ၁၃၇၃ ခုႏွစ္ ျပာသိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/014-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၄။ ၁၃၇၃ ခုႏွစ္ တပို႕တြဲလဆန္း(၁၄)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/015-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၅။ ၁၃၇၃ ခုႏွစ္ တပို႕တြဲ႕လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/016-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၆။ ၁၃၇၃ ခုႏွစ္ တပို႕တြဲလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/017-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၇။ ၁၃၇၃ ခုႏွစ္ တေပါင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/018-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၈။ ၁၃၇၃ ခုႏွစ္ တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/019-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၁၉။ ၁၃၇၃ ခုႏွစ္ ေႏွာင္းတန္ခူးလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/020-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၂၀။ ၁၃၇၄ ခုႏွစ္ ဦးတန္ခူးလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-04/021-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-04.mp3">
									၂၁။ ၁၃၇၄ ခုႏွစ္ ကဆုန္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ညဥ္႕ဦးယံ ၾသဝါဒကထာမ်ား 
									အမွတ္စဥ္ (၅)</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/001-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-5-20.mp3">
									၁။ ၁၃၇၄ ခုႏွစ္ ကဆုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/002-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-6-13.mp3">
									၂။ ၁၃၇၄ ခုႏွစ္ နယုန္လျပည္႕ေက်ာ္(၉)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/003-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-6-18.mp3">
									၃။ ၁၃၇၄ ခုႏွစ္ နယုန္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/004-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-7-3.mp3">
									၄။ ၁၃၇၄ ခုႏွစ္ ပထမဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/005-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-7-18.mp3">
									၅။ ၁၃၇၄ ခုႏွစ္ ပထမဝါဆိုလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/006-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-8-2.mp3">
									၆။ ၁၃၇၄ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/007-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-8-3.mp3">
									၇။ ၁၃၇၄ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ေက်ာ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/008-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-8-9.mp3">
									၈။ ၁၃၇၄ ခုႏွစ္ ဒု-ဝါဆိုလျပည္႕ေက်ာ္(၇)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/009-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-9-9.mp3">
									၉။ ၁၃၇၄ ခုႏွစ္ ဝါေခါင္လျပည္႕ေက်ာ္(၈)ရက္ေန႔</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/010-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-9-15.mp3">
									၁၀။ ၁၃၇၄ ခုႏွစ္ ဝါေခါင္လကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/011-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-9-30.mp3">
									၁၁။ ၁၃၇၄ ခုႏွစ္ ေတာ္သလင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/012-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-10-15.mp3">
									၁၂။ ၁၃၇၄ ခုႏွစ္ ေတာ္သလင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/013-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-10-31.mp3">
									၁၃။ ၁၃၇၄ ခုႏွစ္သီတင္းကၽြတ္လျပည္႕ေက်ာ္(၁)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/014-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-11-14.mp3">
									၁၄။ ၁၃၇၄ ခုႏွစ္ တန္ေဆာင္မုန္းလဆန္း(၁)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/015-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-11-28.mp3">
									၁၅။ ၁၃၇၄ ခုႏွစ္ တန္ေဆာင္မုန္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/016-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2012-12-28.mp3">
									၁၆။ ၁၃၇၄ ခုႏွစ္ နတ္ေတာ္လျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/017-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-1-12.mp3">
									၁၇။ ၁၃၇၄ ခုႏွစ္ ျပာသိုလဆန္း(၁)ရက္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/018-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-2-17.mp3">
									၁၈။ ၁၃၇၄ ခုႏွစ္ တပို႕တြဲလဆန္း(၇)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/019-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-2-26.mp3">
									၁၉။ ၁၃၇၄ ခုႏွစ္ 
									တပို႕တြဲလျပည္႕ေက်ာ္(၁)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/020-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-3-18.mp3">
									၂၀။ ၁၃၇၄ ခုႏွစ္ တေပါင္းလဆန္း(၇)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/021-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-3-20.mp3">
									၂၁။ ၁၃၇၄ ခုႏွစ္ တေပါင္းလဆန္း(၉)ရက္ေန႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/022-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-3-26.mp3">
									၂၂။ ၁၃၇၄ ခုႏွစ္ တေပါင္းလျပည္႕ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/NyintOoYanAwwardakahtarmyar/MP3-05/023-MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-NyintOoYanAwwardakahtarmyar-MP3-05-2013-4-10.mp3">
									၂၃။ ၁၃၇၄ ခုႏွစ္ တေပါင္းလကြယ္ည</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အႏုေမာဒနာတရားေတာ္မ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-001.mp3">
									၁။ ေစတနာသံုးတန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-002.mp3">
									၂။ သံဃာအား ဘုရားယံုခဲ့သည္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-003.mp3">
									၃။ ကုသိုလ္သံုးမ်ိဳး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-004.mp3">
									၄။ မဂၤလာရိွပါေစ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-005.mp3">
									၅။ နတ္တို႔မွာတမ္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-006.mp3">
									၆။ မဂၤလာရိွပါေစ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-007.mp3">
									၇။ တေမာတမသုတၱန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-008.mp3">
									၈။ အာဇာနီယသုတၱန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-009.mp3">
									၉။ ဆရာဒကာညီညြတ္ပါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-010.mp3">
									၁၀။ ေၾကာင္႔ၾကမဲ႔စြာ မေနရာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-011.mp3">၁၁။ သံေ၀ဇနိယေလးဌာန</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-012.mp3">၁၂။ လူေလးမ်ိဳး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-013.mp3">၁၃။ 
									သာသနာကြယ္ေၾကာင္းတရားေလးပါး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-014.mp3">၁၄။ သာသနာ႔က်က္သေရေဆာင္မ်ား</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-015.mp3">၁၅။ ခ်မ္းသာေလးမ်ိဳး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-016.mp3">၁၆။ စြမ္းအားရွင္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-017.mp3">၁၇။ ပစၥဳပၸန္လက္ငင္းခ်မ္းသာေရး 
									(၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-018.mp3">၁၈။ ပစၥဳပၸန္လက္ငင္းခ်မ္းသာေရး 
									(၂)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-019.mp3">၁၉။ သုမနသုတၱန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-020.mp3">၂၀။ မွ်တမွ တရားရတယ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-021.mp3">၂၁။ စိတ္ေကာင္းရိွဖို႔က ပထမ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-022.mp3">၂၂။ သူေတာ္ေကာင္း လကၡဏာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-023.mp3">၂၃။ ဂဟ႒၀ႏၵနာသုတၱန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-024.mp3">၂၄။ ရွင္ျပဳအလွဴေမာဒနာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-025.mp3">၂၅။ အာဒိတၱဇာတ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-026.mp3">၂၆။ မရဏႆတိဘာ၀နာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-027.mp3">၂၇။ ဒုလႅဘတရားငါးပါး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-028.mp3">၂၈။ သိဂၤါလသုတၱန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-029.mp3">၂၉။ ကိုယ့္ကိုကိုယ္ 
									ခ်စ္ျမတ္ႏိုးပါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-030.mp3">၃၀။ လူခ်မ္းသာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-031.mp3">၃၁။ ပရိတ္အႏုေမာဒနာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-032.mp3">၃၂။ ဘာ၀နာအေျခခံအုတ္ျမစ္ (၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-033.mp3">၃၃။ ဘာ၀နာအေျခခံအုတ္ျမစ္ (၂)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-034.mp3">၃၄။ နိဓိက႑သုတၱန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-035.mp3">၃၅။ ဆည္းကပ္ကိုးကြယ္ျခင္းႏွင္႔ 
									ေပးကမ္းျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-036.mp3">၃၆။ စိတ္သာရွင္ေစာ ဘုရားေဟာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-037.mp3">၃၇။ ျမင္႔ျမတ္ေသာ ဘ၀တစ္ခုကို 
									တည္ေဆာက္ျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-038.mp3">၃၈။ လူ႔တန္ဖိုး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-039.mp3">၃၉။ လမ္းႏွစ္သြယ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-040.mp3">၄၀။ ခ်စ္ၾကည္မွ်တေရး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-041.mp3">၄၁။ ေက်ာင္းအႏုေမာဒနာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-042.mp3">၄၂။ ကထိန္အႏုေမာဒနာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-043.mp3">၄၃။ မိဘေက်းဇူး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-044.mp3">၄၄။ ပန္းပ်ိဳးေသာလက္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-045.mp3">၄၅။ ကံေလးမ်ိဳး၏ အက်ိဳးေပးအစဥ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-046.mp3">၄၆။ ရဟန္းခံအႏုေမာဒနာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-047.mp3">၄၇။ သူေတာ္ေကာင္းတို႔ သေဘာထား</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-048.mp3">၄၈။ သားေတာ္ရာဟုလာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-049.mp3">၄၉။ သေဘာထားမွန္ဖို႕ လိုပါတယ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-050.mp3">၅၀။ ေက်းဇူးဆပ္ျခင္းႏွင္႔ 
									အေမြေပးျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-051.mp3">၅၁။ ေက်ာင္းအႏုေမာဒနာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-052.mp3">၅၂။ 
									သူေတာ္ေကာင္းတို့ေတာင္းဆုမ်ား (၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-053.mp3">၅၃။ 
									သူေတာ္ေကာင္းတို့ေတာင္းဆုမ်ား (၂)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-054.mp3">၅၄။ ကိုယ္ပိုင္ပစၥည္းအစစ္အမွန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-055.mp3">၅၅။ လူၾကီးႏွင္႔လူၾကာၾကီး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-056.mp3">၅၆။ သာသနာျပဳစိတ္ဓာတ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-057.mp3">၅၇။ ရဟန္းဟူသည္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-058.mp3">၅၈။ ဒါနေၾကာင္႔ 
									သံသရာရွည္ပါသလား</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-059.mp3">၅၉။ သီရိေဂဟာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-060.mp3">၆၀။ ပန္းရနံ႔ကို နမ္းရႈဳမိသူ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-061.mp3">၆၁။ ပရိတ္တရားေတာ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-062.mp3">၆၂။ ပညာရတနာ (၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-063.mp3">၆၃။ ပညာရတနာ (၂)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-064.mp3">၆၄။ ေနကၡမၼပါရမီ (၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-065.mp3">၆၅။ ေနကၡမၼပါရမီ (၂)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-066.mp3">၆၆။ အတိုးေပးျခင္းေၾကာင္႔ 
									အျပစ္ရိွပါသလား</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-067.mp3">၆၇။ အၾကီးက်ယ္ဆံုးေရာဂါ၊ 
									ဒုကၡႏွင္႔သုခ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-068.mp3">၆၈။ နတ္တို႔ေျပာေသာ 
									သူေတာ္ေကာင္းလကၡဏာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-069.mp3">၆၉။ ဆူဆူဗုဒၶ ဆံုးအမ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-070.mp3">၇၀။ ဗုဒၶညႊန္ျပ ျမတ္ဒါန</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-071.mp3">၇၁။ လွဴမွ်ေ၀၍</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-072.mp3">၇၂။ ဗုဒၶေဟာၾကား 
									ေက်ာင္းအႏုေမာဒနာတရား</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-073.mp3">၇၃။ ေထရ္ျမတ္မဟာ 
									အရွင္သာရိပုတၱာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-074.mp3">၇၄။ လသာခိုက္ဗိုင္းငင္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-075.mp3">၇၅။ သူေတာ္စင္ျဖစ္ရန္ 
									အေၾကာင္းေလးတန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-076.mp3">၇၆။ ၾကီးပြားတိုးတက္ေရးလမ္းစဥ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-077.mp3">၇၇။ ဓာတ္ခံေကာင္းဖို႔လိုပါတယ္။</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-078.mp3">၇၈။ ၀ိသာခါ၏ ေတာင္းဆုရွစ္မ်ိဳး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-079.mp3">၇၉။ ေမးလာၾကေသာ ေမးခြန္းမ်ား 
									(၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-080.mp3">၈၀။ ျပည္႔စံုျခင္းသံုးျဖာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-081.mp3">၈၁။ သံေ၀ဂဓမၼလကၤာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-082.mp3">၈၂။ စိတ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-083.mp3">၈၃။ ဗုဒၶါႏုႆတိဘာ၀နာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-084.mp3">၈၄။ ဖူးေျမာ္မာန္ေလွ်ာ႔ 
									ကန္ေတာ႔ပါ၏ (၁)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-085.mp3">၈၅။ ဖူးေျမာ္မာန္ေလွ်ာ႔ 
									ကန္ေတာ႔ပါ၏ (၂)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-086.mp3">၈၆။ သာသနာကြယ္ရန္ 
									အေၾကာင္းငါးတန္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-087.mp3">၈၇။ မဟုတ္တာကို ခံႏိုင္ရတယ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-088.mp3">၈၈။ အာဇာနည္စူ႒သုဘဒၵါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-089.mp3">၈၉။ အနီးအေ၀း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-090.mp3">၉၀။ အရွင္အာနႏၵာ၏ ဆုရွစ္မ်ိဳး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-091.mp3">၉၁။ အရွင္အာနႏၵာမေထရ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-092.mp3">၉၂။ ဒါနျပဳနည္းႏွင္႔ ဘ၀ေနနည္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-093.mp3">၉၃။ ဗုဒၶလမ္းစဥ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-094.mp3">၉၄။ ေမတၱာေရျဖင္႔ ေဆးေၾကာပါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-095.mp3">၉၅။ သူျမတ္လမ္းစဥ္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-096.mp3">
									<font size="4">၉၆။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဆင္ျခင္ဖြယ္ရာကံႏွစ္ျဖာ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-097.mp3">
									<font size="4">၉၇။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဖုံးကြယ္ျခင္းသံုးျဖာ ဓမၼေဒသနာ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-098.mp3">
									<font size="4">၉၈။ </font>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									စူဠေသာတာပန္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-099.mp3">
									<font size="4">၉၉။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ယေန႔လူငယ္ ေနာင္၀ယ္လူႀကီး</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-100.mp3">၁၀၀။
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ဒါနတရားႏွင့္သူေတာ္ေကာင္းတို႔သေဘာထား</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-101.mp3">
									<font size="4">၁၀၁။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ပင္လယ္ကိုကူး မာလိန္မွဴးသို႔</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-102.mp3">
									<font size="4">၁၀၂။
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဗုဒၶလႊဲအပ္ တာ၀န္ႏွစ္ရပ</span></font><span style="font-size: 11.0pt; line-height: 115%; font-family: Zawgyi-One,sans-serif">္</span></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-103.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၀၃။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									၀တၱရားေက်မွ နိဗၺာန္ရ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-104.mp3">
									<font size="4">၁၀၄။
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ေခါင္းေဆာင္ေကာင္းဟူသည</span></font><span style="font-size: 11.0pt; line-height: 115%; font-family: Zawgyi-One,sans-serif">္</span></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-105.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၀၅။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									လြဲမွားေနေသာအယူအဆေလးမ်ား</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-106.mp3">
									<font size="4">၁၀၆။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ေက်ာင္းအလွဴႏွင့္ေက်းဇူးဆပ္ျခင္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-107.mp3">
									<font size="4">၁၀၇။ </font>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ရုိးဂုဏ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-108.mp3">
									<font size="4">၁၀၈။ </font>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး၏လမ္းစဥ္ျမတ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-109.mp3">
									<font size="4">၁၀၉။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									သမၸဳဏၰာရာမဆရာေတာ္ဘုရားႀကီး၏ဂုဏ္ရည္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-110.mp3">
									<font size="4">၁၁၀။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ျမတ္ဗုဒၶ၏ဆႏၵေတာ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-111.mp3">
									<font size="4">၁၁၁။ ေ<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">ၾကာက္လန္႔ဖြယ္ရာ 
									ပိသုဏ၀ါစာ</span></font><span style="font-size: 11.0pt; line-height: 115%; font-family: Zawgyi-One,sans-serif">
									</span></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-112.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၁၂။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									အနီးအေ၀းေနသင့္သူ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-113.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၁၃။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဘ၀တစ္သက္တာလိုက္နာက်င့္သုံးစရာေလးမ်ား</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-114.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၁၄။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဂုဏ္ရွိသူႏွင့္ဂုဏ္မဲ့သူ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-115.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၁၅။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									သစ္လြင္ေသာအနာဂတ္ကိုဖန္တီးျခင္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-116.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၁၆။ ေ</font></span><font size="4"><span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">မတၱာေရျဖင့္ေဆးေၾကာပါ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-117.mp3">၁၁၇။ ေက်းဇူးတရားႏွင္႔ သာသနာ</a></font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-118.mp3">၁၁၈။ ပါရမီကုသိုလ္</a></font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-119.mp3">၁၁၉။ မာတုေထရီဂုဏကထာ</a></font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-120.mp3">၁၂၀။ အေမးသံုးေထြ အေျဖသံုးပါး</a></font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-121.mp3">၁၂၁။ ရဟန္းခံမဂၤလာ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-122.mp3">၁၂၂။ မိတ္ေကာင္းေဆြေကာင္းႏွင္႔ 
									ခရီးသြားျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-123.mp3">၁၂၃။ ရုပ္လွသူႏွင္႕စိတ္လွသူ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-124.mp3">၁၂၄။ 
									အတိုင္းအရွည္ပမာဏကိုသိပါေစ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-125.mp3">၁၂၅။ ျငမ္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-126.mp3">၁၂၆။ မိဘေက်းဇူးသိပါေစ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-127.mp3">၁၂၇။ မွ်တေရး၊ ညီညႊတ္ေရး၊ 
									ခ်စ္ၾကည္ေရး (မဟာဂႏၶာရံု)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-128.mp3">၁၂၈။ 
									အျပစ္ကင္းေသာဆုေတာင္းျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-129.mp3">၁၂၉။ ေကာင္းျမတ္ေသာ 
									ဆုေတာင္းျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-130.mp3">၁၃၀။ ဘ၀သစ္ပင္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-131.mp3">၁၃၁။ ေလ႔လာသံုးသပ္ 
									ဆံုးျဖတ္ေစခ်င္</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-132.mp3">၁၃၂။ စိတ္ကိုေဆာက္တည္၍ေသျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-133.mp3">၁၃၃။ သိသူႏွင္႔မသိသူ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-134.mp3">၁၃၄။ ေသာတာပန္ႏွင္႔တူသူ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-135.mp3">၁၃၅။ ခ်စ္ၾကည္စြာ 
									ယွဥ္တြဲေနထိုင္ေရး</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-136.mp3">၁၃၆။ အနႏၱငါးပါးအား 
									ဦးခိုက္ပူေဇာ္ျခင္း</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-137.mp3">၁၃၇။ အပရေစတနာ ရွင္သန္ပါေစ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-138.mp3">၁၃၈။ မွ်တေရး၊ ညီညႊတ္ေရး၊ 
									ခ်စ္ၾကည္ေရး၊ (နတ္ေမာက္ျမိဳ႕)</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-139.mp3">
									<font size="4">၁၃၉။ </font>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ဆုေတာင္းျပည့္တဲ့ေန႔</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-140.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၀။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									လွဳိင္းကေလးသင္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-141.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၁။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ဗိုလ္ခ်ဳပ္ပုံရိပ္ 
									တစ္စိတ္တစ္ေဒသ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-142.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၂။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ေျပာင္လ်က္၀င္းလ်က္ 
									က်န္ေစသတည္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-143.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၃။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ေျပာင္လ်က္၀င္းလ်က္ 
									က်န္ေစသတည္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-144.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၄။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									စပါးပင္လား ေပါင္းျမက္လား</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-145.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၅။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									စပါးပင္လား ေပါင္းျမက္လား</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-146.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၆။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ဗုဒၵယၾတာ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-147.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၇။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ျမတ္ဗုဒၶသာသနာေတာ္၌ 
									ေပ်ာ္ရႊင္ခ်မ္းေျမ႕စြာ ေနထိုင္နည္း (၁)</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-148.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၄၈။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ျမတ္ဗုဒၶသာသနာေတာ္၌ 
									ေပ်ာ္ရႊင္ခ်မ္းေျမ႕စြာ ေနထိုင္နည္း (၂)</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-149.mp3">
									<font size="4">၁၄၉။ </font>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဆရာႀကီးဖြားစရ၀တီ၏ ဂုဏ္ရည္
									</span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-150.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၀။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ေက်းဇူးရနံ႔ သင္းပ်ံ႕သည့္ေျမ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-151.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၁။ </font></span>
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									<font size="4">ႏွလုံးသားကိုစားပြဲမခ</font></span><font size="4"><span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">င္းေၾကး 
									(အာစရိယပူဇာ)</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-152.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၂။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									လြတ္လပ္ေရးေန႔ အေတြးဂယက္
									</span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-153.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၃။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									စိတ္ထားတတ္ဖို႔ လိုပါတယ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-154.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၄။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									တရားမွန္ကို ၾကည့္ျခင္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-155.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၅။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									တန္ဖိုးျမင့္လူသား</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-156.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၆။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ဘုဥ္းက်က္သေရ ျပည့္စုံေစ
									</span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-157.mp3">
									<font size="4">၁၅၇။ </font>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ႏွလုံးသားကိုစားပြဲမခင္းေၾကး&nbsp; 
									(ရွင္ျပဳအလွဴ)</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-158.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၈။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									ျမင့္ျမတ္သူတို႔၏လုပ္ရပ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-159.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၅၉။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									အဆုံးစြန္ေသာအနာဂတ္အထိ 
									ေမွ်ာ္ၾကည့္ပါ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-160.mp3">
									<font size="4">၁၆၀။ </font>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									အမ်ဳိးကိုေစာင့္ေရွာက္ပါ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-161.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၁။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									သာသနာေတာ္စည္ပင္ေရး ႏွင့္ 
									ၿငိမ္းခ်မ္းေရး (ျမေတာင္)</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-162.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၂။</font></span><font size="4"><span style="line-height: 115%; font-family: Zawgyi-One,sans-serif"> 
									ဗုဒၶမိန္႔ၾကား ရခဲသူ(၅)ပါး </span> </font>
									</a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-163.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၃။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									အရွင္ဥတၱမသာရဘဝပုံရိပ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-164.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၄။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									အထူးကုသမားေတာ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-165.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၅။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ကမၻာ့အေကာင္းဆုံးေက်ာင္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-166.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၆။</font></span><font size="4"><span style="line-height: 115%; font-family: Zawgyi-One,sans-serif"> 
									ၿငိမ္းခ်မ္းနယ္ေျမ </span> </font>
									</a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-167.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၇။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ၿငိမ္းခ်မ္းေရးလမ္းစဥ္</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-168.mp3">၁၆၈။ အေမ႔ေက်းဇူး အေမ႔ေမတၱာ</a></font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-169.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၆၉။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									အျမင္မက်ဥ္းပါေစနဲ႔</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-170.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၇၀။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ပတ္ဝန္းက်င္ေကာင္းကို 
									ေရြးခ်ယ္ပါ </span> </font>
									</a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-171.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၇၁။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									ေက်ာင္းအႏုေမာဒနာ 
									</span> </font>
									</a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-172.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၇၂။ </font></span>
									<font size="4">
									<span style="line-height: 115%; font-family: Zawgyi-One,sans-serif">
									အာစရိယဂုေဏာအနေႏၱာ</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/Anumawdanar/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-173.mp3">
									<span style="font-family: Zawgyi-One,sans-serif">
									<font size="4">၁၇၃။ </font></span>
									<font size="4">
									<span style="font-family:&quot;Zawgyi-One&quot;,&quot;sans-serif&quot;">
									သာသနာ့၀န္ထမ္းႏွင့္ပရဟိတလုပ္ငန္း</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">တရားေတာ္မ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">***********</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-26-11-2017-001.mp3">၁။ ၂၆-၁၁-၂၀၁၇ စပ္မိစပ္ရာဓမၼကထာ ဂႏၵာရုံဘုံေက်ာ္စာသင္တုိက္ ႏွစ္ ၃၀ 
ျပည့္ပုလဲရတုဓမၼသဘင္ 
</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-3-9-2018-002.mp3">၂။ ၃-၉-၂၀၁၈ ၀ါေခါင္လဆုတ္(၈)ရက္ ဂုဏ္ျပဳပူေဇာ္ပြဲ ၾသ၀ါဒကထာ</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-25-2-2018-003.mp3">၃။ ၂၅-၂-၂၀၁၈ စာထဲက ရဟန္း</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-9-9-2018-004.mp3">၄။ ၉-၉-၂၀၁၈ ၀ါေခါင္လဆုတ္(၁၄)ရက္</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-18-1-2018-005.mp3">၅။ ၁၈-၁-၂၀၁၈ သူေတာ္စင္ႏွင့္သူယုတ္မာတုိ႔၏ျခားနားခ်က္</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-24-9-2018-006.mp3">၆။ ၂၄-၉-၂၀၁၈ ေတာ္သလင္းလဆန္း (၁၅)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-18-5-2018-007.mp3">၇။ ၁၈-၅-၂၀၁၈ ေလာ္လီသူ နဲ႔ ေဖာ္ေရႊသူ</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-9-10-2018-008.mp3">၈။ ၉-၁၀-၂၀၁၈ ေတာ္သလင္းလျပည့္္ေက်ာ္ (၁၅)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-24-10-2018-009.mp3">၉။ ၂၄-၁၀-၂၀၁၈ သီတင္းကၽြတ္လဆန္း (၁၅)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-22-7-2018-010.mp3">၁၀။ ၂၂-၇-၂၀၁၈ ဆည္းကပ္ကုိးကြယ္ပူေဇာ္နည္း</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-16-9-2018-011.mp3">၁၁။ ၁၆-၉-၂၀၁၈ ဒုိ႔က ဘယ္ေနရာမွာလဲ 
</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-15-10-2017-12.mp3">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">၁၂။
</font></span><font size="4">၁၅-၁၀-၂၀၁၇ အႏုေမာဒနာ</font></a></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-29-4-2018-013.mp3">၁၃။ ၂၉-၄-၂၀၁၈ ကဆုန္လဆန္း ၁၅ ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-18-4-2017-014.mp3">၁၄။ ၁၈-၄-၂၀၁၇ အာစရိယဂုေဏာ အနေႏ ၱာ&nbsp; အရွင္၀ိမလဗုဒၵိ၏အႏၱိမစ်ာပန</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-29-5-2018-15.mp3">၁၅။ ၂၉-၅-၂၀၁၈ နယုန္လဆန္း၁၅ ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-23-7-2017-016.mp3">၁၆။ ၂၃-၇-၂၀၁၇ ဗုဒၵအလုိက်စီးပြားဥစၥာကုိရွာေဖြ အသုံးျပဳနည္း 
</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-12-6-2018-017.mp3">၁၇။ ၁၂-၆-၂၀၁၈ နယုန္လျပည့္ေက်ာ္(၁၄)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-12-8-2017-18.mp3">၁၈။ ၁၂-၈-၂၀၁၇ သူေတာ္ေကာင္းစကားနာၾကားခြင့္ေပးပါ</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-27-6-2018-19.mp3">၁၉။ ၂၇-၆-၂၀၁၈ ပထမ၀ါဆုိလဆန္း(၁၅)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-31-8-2017-20.mp3">၂၀။ ၃၁-၈-၂၀၁၇ ျမတ္ဗုဒၵ၏အသားေရေတာ္ႏွင့္မွားခြင့္ကေလး ေပးလုိက္ပါ 
</a></font>
</span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-12-7-2018-21.mp3">၂၁။ ၁၂-၇-၂၀၁၈ ပထမ၀ါဆုိလဆုတ္ (၁၅)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-20-8-2017-022.mp3">၂၂။ ၂၀-၈-၂၀၁၇ ရက္ကန္းသည္မေလး၏ဘ၀ျဖစ္ရပ္အတၳဳပၸတ္&nbsp; 
</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-28-7-2018-023.mp3">၂၃။ ၂၈-၇-၂၀၁၈ ဒုတိယ၀ါဆုိလဆန္း (၁၅)ရက္ည</a></font></span></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif"><font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-3-10-2017-024.mp3">၂၄။ ၃-၁၀-၂၀၁၇ ငယ္ဘ၀အမွတ္တရပုံရိပ္မ်ား&nbsp; ပုညနႏၵီဆြမ္းကပ္အဖြဲ႔ 
</a></font></span>
</p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-3-8-2018-25.mp3">၂၅။ ၃-၈-၂၀၁၈ ၾသ၀ါဒ</a></font></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-11-8-2018-26.mp3">၂၆။ ၁၁-၈-၂၀၁၈ ၾသ၀ါဒ</a></font></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-26-8-2018-27.mp3">၂၇။ ၂၆-၈-၂၀၁၈ ထိုင္းခရီးစဥ္ 
</a></font></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-26-11-2018-28.mp3">၂၈။ ၂၆-၁၁-၂၀၁၈ ၾသ၀ါဒ</a></font></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
<font size="4">
<a href="http://dhammadownload.com/MP3Library/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa/MyaSatKyarSayadaw-BhaddantaIndakabhivamsa-28-11-2017-29.mp3">၂၉။ ၂၈-၁၁-၂၀၁၇ အႏုေမာဒနာ</a></font></p>
<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<br>
&nbsp;</font></p>
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
<div style="position: absolute; width: 501px; height: 63px; z-index: 2; left: 52px; top: 43px" id="layer22" align="center">
	<font style="font-size: 20pt" color="#800080">ျမစၾကာဆရာေတာ္ ဘဒၵႏ 
	ၱဣႏၵကာဘိဝံသ</font></div>

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

soup = bs4(one, 'html.parser')




with open('titles_links.txt', 'w') as f:


    #count = 1
    count = 1
    for key in soup.find_all('a'):
        
        
        try:
            if '.mp3' in key.get('href'):
                counter = '{:03d}'.format(count)
                #print(" ".join(key.find('td').find('a').get_text().strip().split()))
                #print('{}.mp3|{}|{}\n'.format(counter, key.get('href'),
                #" ".join(key.get_text().strip().split()) 
                #))
                f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'),
                " ".join(key.get_text().strip().split()) 
                ))            
                #f.write('{}.mp3|{}|{}\n'.format(counter, key.find('td').find('a').get('href'), 
                #    " ".join(key.find('td').find('a').get_text().strip().split())            
                #    ))
                count += 1
        except AttributeError as err:
            pass
        
