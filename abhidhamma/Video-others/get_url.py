from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">



<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>

<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font color="#800080">
	<span style="font-family: Times New Roman; font-size: 32pt">Daw Khin Hla Tin</span></font></div>



<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 587px; top: 6px" id="layer23">
	<img src="images/DhammaByuharDawKhinHlaTin.gif" border="0"></div>



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
										<span style="FONT-WEIGHT: 700; FONT-FAMILY: Franklin Gothic Medium">
									Dhamma Byuhar </span></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">
									Daw Khin Hla Tin </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<b><font size="4" face="Franklin Gothic Medium">
									Thudhamma Jotikadaza </font></b></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<b><font size="4" face="Franklin Gothic Medium">Dhamma 
									Byuhar Tharthana Marmaka AhPwek</font></b></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="WinTaungyi">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font>
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">ဓမၼဗ်ဴဟာ</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<b><font size="5" face="Zawgyi-One">
									ေဒၚခင္လွတင္</font></b></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">
									မဟာ
									သဒၶမၶေဇာတိကဓဇ</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">ဓမၼဗ်ဴဟာ 
									သာသနမာမကအဖြဲ႕</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">
									လူပုဂၢိဳလ္မ်ားဆိုင္ရာ ဓမၼစာေပသင္တန္းေက်ာင္း&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္(၆)၊ ၾကားေတာရလမ္း၊ 
									ဗဟန္းၿမိဳ႕နယ္၊ ရန္ကုန္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ဖုန္း။ (၉၅) ၀၁-၃၈၀၈၈၀</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One">သင္ႀကားပို႕ခ်ေသာ 
									တရားေတာ္မ်ား </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk </font></b>
								<font size="5"><b>Video</b></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								ဓမၼစကၠပဝတၱနသုတ္ေတာ 
								(ဓမၼစၾကာ) သင္တန္း 
								(၂၀၁၈)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-07-DhammaSyatKaPaWuitNa/Dawkhinhlatin-DhammaCekka-26-7-2018-1.mp4">
								(၁) ပို႔ခ်ခ်က္ - ၁</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-07-DhammaSyatKaPaWuitNa/Dawkhinhlatin-DhammaCekka-26-7-2018-2.mp4">
								(၂) ပို႕ခ်ခ်က္ - ၂</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">မဟာသရဏဂုဏ္ေတာ္ၾကီး သင္တန္း 
								(၂၀၁၈)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ေက်းဇူေတာ္ရွင္ လယ္တီ 
								ဆရာေတာ္ဘုရားၾကီး၏...</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">မဟာသရဏဂံုေတာ္ၾကီး ၈ ရက္သင္တန္း</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ေဖေဖၚ၀ါရီလ ၂၀၁၈</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-01.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၁)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-02.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၂)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-03.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၃)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-04.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၄)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-05.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၅)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-06.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၆)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-07.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၇)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-08.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၈)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-09.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၉)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-10.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၁၀)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-11.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၁၁)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-12.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၁၂)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-13.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၁၃)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-Mettasutta/DawKhinHlaTin-MHBD-Mettasutta-14.mp4">ေမတၱာသုတ္ပရိတ္ေတာ္ က်င့္စဥ္သင္တန္း(၁၄)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-01.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၁)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-02.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၂)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-04.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၃)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-04.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၄)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-05.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၅)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-06.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၆)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-07.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၇)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-08.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၈)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-09.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၉)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-10.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၁၀)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/MHBD-GonePongWaiSarMyatYadanat/DawKhinHlaTin-MHBD-GonePongWaiSarMyatYadana-11.mp4">
								<font size="4">ဂုဏ္ေပါင္းေဝဆာ ျမတ္ရတနာ </font>
								<font size="4" face="Zawgyi-One">
								သင္တန္း 
								(၁၁)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								ပါရမီပုံရိပ္ အမွတ္တံဆိပ္&nbsp; သင္တန္း 
								(၂၀၁၃)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font><font size="4" face="Zawgyi-One"><br>
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2013-01-Parami-Pone-Yeik/Dawkhinhlatin-2013-01-12-Parami-Pone-Yeik.mp4">၁၂-၁-၂၀၁၃ (နံနက္ ၈-၁၀) ပါရမီပုံရိပ္ အမွတ္တံဆိပ္ 
								ဗုဒၶဂုတ္ေတာ္ ပို႕ခ်ခ်က္(၁)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2013-01-Parami-Pone-Yeik/Dawkhinhlatin-2013-01-13-Parami-Pone-Yeik.mp4">၁၃-၁-၂၀၁၃ 
								(နံနက္ ၈-၁၀) ပါရမီပုံရိပ္ အမွတ္တံဆိပ္ 
								ဗုဒၶဂုတ္ေတာ္ ပို႕ခ်ခ်က္(၂)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2013-01-Parami-Pone-Yeik/Dawkhinhlatin-2013-01-19-Parami-Pone-Yeik.mp4">၁၉-၁-၂၀၁၃ 
								(နံနက္ ၈-၁၀) ပါရမီပုံရိပ္ အမွတ္တံဆိပ္ 
								ဗုဒၶဂုတ္ေတာ္ ပို႕ခ်ခ်က္(၃)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2013-01-Parami-Pone-Yeik/DawKhinHlaTin-2013-01-20-Parami-Pone-Yeik.mp4">၂၀-၁-၂၀၁၃ 
								(နံနက္ ၈-၁၀) ပါရမီပုံရိပ္ အမွတ္တံဆိပ္ 
								ဗုဒၶဂုတ္ေတာ္ ပို႕ခ်ခ်က္(၄)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2013-01-Parami-Pone-Yeik/DawKhinHlaTin-2013-01-26-Parami-Pone-Yeik.mp4">၂၆-၁-၂၀၁၃ 
								(နံနက္ ၈-၁၀) ပါရမီပုံရိပ္ အမွတ္တံဆိပ္ 
								ဗုဒၶဂုတ္ေတာ္ ပို႕ခ်ခ်က္(၅)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2013-01-Parami-Pone-Yeik/DawKhinHlaTin-2013-01-27-Parami-Pone-Yeik.mp4">၂၇-၁-၂၀၁၃ 
								(နံနက္ ၈-၁၀) ပါရမီပုံရိပ္ အမွတ္တံဆိပ္ 
								ဗုဒၶဂုတ္ေတာ္ ပို႕ခ်ခ်က္(၆)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								ဓမၼစကၠပဝတၱနသုတ္ေတာ္ သင္တန္း 
								(၂၀၁၂)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-07-DhammaSyatKaPaWuitNa/DawKhinHlaTin-2012-07-30-DhammaSyatKaPaWuitNa-01.mp4">
								<font size="4">၃၀-၇-၂၀၁၂ </font>
								<font size="4" face="Zawgyi-One">
								ဓမၼစကၠပဝတၱနသုတ္ေတာ္ သင္တန္း</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-07-DhammaSyatKaPaWuitNa/DawKhinHlaTin-2012-07-31-DhammaSyatKaPaWuitNa-02.mp4">
								<font size="4">၃၁-၇-၂၀၁၂ </font>
								<font size="4" face="Zawgyi-One">
								ဓမၼစကၠပဝတၱနသုတ္ေတာ္ သင္တန္း</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-07-DhammaSyatKaPaWuitNa/DawKhinHlaTin-2012-08-01-DhammaSyatKaPaWuitNa-03.mp4">
								<font size="4">၁-၈-၂၀၁၂ </font>
								<font size="4" face="Zawgyi-One">
								ဓမၼစကၠပဝတၱနသုတ္ေတာ္ သင္တန္း</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-07-DhammaSyatKaPaWuitNa/DawKhinHlaTin-2012-08-02-DhammaSyatKaPaWuitNa-04.mp4">
								<font size="4">၂-၈-၂၀၁၂ </font>
								<font size="4" face="Zawgyi-One">
								ဓမၼစကၠပဝတၱနသုတ္ေတာ္ သင္တန္း</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								ဗုဒၶအခါေတာ္ေန႕သင္တန္း 
								(၂၀၁၂)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~</font><font size="4" face="Zawgyi-One"><br>
								၂၈-၄-၂၀၁၂ မွ ၂၉-၄-၂၀၁၂ ထိ<br>
								စေန၊ တနဂၤေႏြ ေန႕တိုင္း<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-04-Buddha-AhKharDawNyay/DawKhinHlaTin-2012-04-28-Buddha-AhKharDawNyay-01.mp4">
								<font size="4">၂၈-၄-၂၀၁၂ </font>
								<font size="4" face="Zawgyi-One">
								ဗုဒၶအခါေတာ္ေန႕သင္တန္း</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2012-04-Buddha-AhKharDawNyay/DawKhinHlaTin-2012-04-29-Buddha-AhKharDawNyay-02.mp4">
								<font size="4">၂၉-၄-၂၀၁၂ </font>
								<font size="4" face="Zawgyi-One">
								ဗုဒၶအခါေတာ္ေန႕သင္တန္း</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">အဆင့္ျမင့္ 
								ဗုဒၶဘာသာ ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း 
								(၂၀၁၁)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~~~~~~~</font><font size="4" face="Zawgyi-One"><br>
								၂၂-၁-၂၀၁၁ မွ ၁၃-၂-၂၀၁၁ ထိ<br>
								စေန၊ တနဂၤေႏြ ေန႕တိုင္း<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-22-buddhist-yinkayemhoot-01.mp4">၂၂-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-22-buddhist-yinkayemhoot-02.mp4">၂၂-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၂)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-23-buddhist-yinkayemhoot-03.mp4">၂၃-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၃)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-23-buddhist-yinkayemhoot-04.mp4">၂၃-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၄)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-29-buddhist-yinkayemhoot-05.mp4">၂၉-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၅)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-29-buddhist-yinkayemhoot-06.mp4">၂၉-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၆)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-30-buddhist-yinkayemhoot-07.mp4">၃၀-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၇)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-01-30-buddhist-yinkayemhoot-08.mp4">၃၀-၁-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၈)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-05-buddhist-yinkayemhoot-09.mp4">၅-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၉)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-05-buddhist-yinkayemhoot-10.mp4">၅-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁၀)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-06-buddhist-yinkayemhoot-11.mp4">၆-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁၁)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-06-buddhist-yinkayemhoot-12.mp4">၆-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁၂)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-12-buddhist-yinkayemhoot-13.mp4">၁၂-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁၃)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-12-buddhist-yinkayemhoot-14.mp4">၁၂-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁၄)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2011-01-Buddhist-YinKayeMhoot/DawKhinHlaTin-2011-02-13-buddhist-yinkayemhoot-15.mp4">၁၃-၂-၂၀၁၁ အဆင့္ျမင့္ ဗုဒၶဘာသာ 
								ယဥ္ေက်းမႈ မြမ္းမံသင္တန္း (၁၅)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								ဂရုဓမၼအခါေတာ္ေန႕သီလက်င့္စဥ္ သင္တန္း 
								(၂၀၁၀)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~~~</font><font size="4" face="Zawgyi-One"><br>
								<a href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/2000-09-GaruDhammaSila/2000-09-GaruDhammaSila.mp4">၂၃-၉-၂၀၁၀ ဂရုဓမၼအခါေတာ္ေန႕သီလက်င့္စဥ္ 
								သင္တန္း</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">~~~~~~~~~~~~~~~~~~</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">ေမတၲာသုတ္ေတာ္ 
								က်င္႕စဥ္ သင္တန္း 
								(၂၀၀၅)<br>
								</font><font size="5">~~~~~~~~~~~~~~~~~~</font><font size="4" face="Zawgyi-One"><br>
								၁၉-၈-၂၀၀၅ <br>
								(နံနက္ ၉ နာရီမွ ၁၁ နာရီထိ)<br>
								(မြန္းလြဲ ၁ နာရီမွ ၃ နာရီ)<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/old/Metta/01-DawKhinHlaTin-MettaThoutTawKyintSinThinTan-(01)-19-8-2005.mp4">ေမတၲာသုတ္ေတာ္ က်င္႕စဥ္ သင္တန္း (၁)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/old/Metta/02-DawKhinHlaTin-MettaThoutTawKyintSinThinTan-(02)-19-8-2005.mp4">ေမတၲာသုတ္ေတာ္ က်င္႕စဥ္ သင္တန္း (၂)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/old/Metta/03-DawKhinHlaTin-MettaThoutTawKyintSinThinTan-(03)-19-8-2005.mp4">ေမတၲာသုတ္ေတာ္ က်င္႕စဥ္ သင္တန္း (၃)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/DawKhinHlaTin/old/Metta/04-DawKhinHlaTin-MettaThoutTawKyintSinThinTan-(04)-19-8-2005.mp4">ေမတၲာသုတ္ေတာ္ က်င္႕စဥ္ သင္တန္း (၄)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<br>
								&nbsp;</font></p>
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
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
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
count = 444
with open('titles_links.txt', 'w') as f:
    
    for key in soup.find_all('a'):
        if ".mp4" in key.get('href'):
            counter = '{:03d}'.format(count)
            print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
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