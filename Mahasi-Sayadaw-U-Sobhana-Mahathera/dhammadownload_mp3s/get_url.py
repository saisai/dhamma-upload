from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 

<!-- Start dhammadownload menu top and side bar -->

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 33px;" id="layer22" align="center">
	<p style="margin-top: 0; margin-bottom: 0"><span style="">
	<font size="6" face="Times New Roman" color="#800080">
	Mahasi Sayadaw
</font>
</span></p>
	<p style="margin-top: 0; margin-bottom: 0"><span style="">
	<font size="6" face="Times New Roman" color="#800080">
	U Sobhana Mahathera</font><o:p></o:p></span></p></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 596px; top: 4px;" id="layer23">
	<img src="images/MahasiSayadaw-USobhana-Mahathera.gif" width="149" height="192" border="0"></div>







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










<div style="position: absolute; width: 1038px; height: 9185px; z-index: 21; left: 219px; top: 153px" id="layer24" font="" face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4"><b>Venerable Mahasi Sayadaw </b></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4"><b>U Sobhana Mahathera <br>
									&nbsp;</b></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="2">Mahathera, Sasana 
									dhaja-siri-pavara dhanamacariya, Agga Maha 
									Pandita, Chattha-sangiti-pucchaka</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font>
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;
                                    </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">
									ဆဌသံဂီတိပုစၥက အဂၢမဟာပ႑ိတ 
									ႏိုင္ငံေတာ္ၾသ၀ါဒစရိယ<br>
									</font><font size="5" face="Zawgyi-One">
									မဟာစည္ဆရာေတာ္ဘုရားႀကီး<br>
									ဦးေသာဘန မဟာသာရ</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">(၁၂၆၆ - ၁၃၄၄)</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One"><br>
									ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									Biography</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Video-Library/Mahasi-Sayadaw-U-Sobhana-Mahathera/Mahasi-Sayadaw-U-Sobhana-Mahathera-Biography.wmv">
									မဟာစည္ဆရာေတာ္ဘုရားႀကီး၏ 
									ဘဝျဖစ္ေတာ္စဥ္ေထရုပၸတိ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://www.mahasi.org.mm/biography.html">
									http://www.mahasi.org.mm/biography.html</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<a href="http://www.mahasi.org.mm/m_biography.html">
								http://www.mahasi.org.mm/m_biography.html</a></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk Audio</font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">MP3 စုေပါင္း အမွတ္စဥ္ (၁) - ၆၅ ပုဒ္</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/001-MahasiSayadawGyi-DailyGoantawPrayer.mp3">၁။ ဆရာေတာ္ႀကီး ေန႕စဥ္ရွိခိုးေတာ္မူေသာ ဂုဏ္ေတာ္ 
								ဘုရားရွိခိုး၊ တရားရွိခိုး၊ သံဃာရွိခိုး (၁၅ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/002-MahasiSayadawGyi-PyatGyi-Parli.mp3">၂။ ပရိတ္ႀကီး ပါဠိေတာ္ ( ၃၀ - မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/003-MahasiSayadawGyi-Vipassana-AhloatpayTayar.mp3">၃။ ဝိပႆနာ အလုပ္ေပးတရားေတာ္ (၃၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/004-MahasiSayadawGyi-Vipassana-AhloatpayTayar.mp3">၄။ ဝိပႆနာ အလုပ္ေပးတရားေတာ္ ( ၁ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/005-MahasiSayadawGyi-Vipassana-AhloatpayTayar(best-quality).mp3">၅။ ဝိပႆနာ လုပ္ငန္းစဥ္ တရားေတာ္ (၁၅ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/006-MahasiSayadawGyi-Vipassana-AhloatpayTayar-English.mp3">6 - Vipassana Meditation Guide (English) (1 
								hour)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/007-MahasiSayadawGyi-and-Devas-conversation-1312.mp3">၇။ ၁၃၁၂-ခုႏွစ္ ဆရာေတာ္ႀကီးအား အဘိဓမၼာတရား 
								နာၾကားခဲ့ရေသာ နတ္သား ေလွ်ာက္ထားျခင္း (၂ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/007-MahasiSayadawGyi-and-Devas-conversation-1312.mp3">၈။ ၁၃၂၂ ခုႏွစ္ ပုရာေဘႅသုတ္ တရားေတာ္ 
								(၁) (၁ နာရီ ၃၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/009-MahasiSayadawGyi-PurabaydaSutta(2)-1322.mp3">၉။ ၁၃၂၂ ခုႏွစ္ ပုရာေဘႅသုတ္ တရားေတာ္ 
								(၂) (၁ နာရီ ၃၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/010-MahasiSayadawGyi-PurabaydaSutta(3)-1322.mp3">၁၀။ ၁၃၂၂ ခုႏွစ္ ပုရာေဘႅသုတ္ တရားေတာ္ 
								(၃) (၂ နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/011-MahasiSayadawGyi-BuddaykarathtaSutta(1)-1323.mp3">၁၁။ ၁၃၂၃ ခုႏွစ္ ဘေဒၵကရတထသုတ္ တရားေတာ္ (၂ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/012-MahasiSayadawGyi-BuddaykarathtaSutta(2)-1323.mp3">၁၂။ ၁၃၂၃ ခုႏွစ္ ဘေဒၵကရတထသုတ္ တရားေတာ္ (၂ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/013-MahasiSayadawGyi-PiTeatThanBalZin(1)-1323.mp3">၁၃။ ၁၃၂၃ ခုႏွစ္ ပီတိသေမၺာဇၥ်င္ တရားေတာ္ 
								(၁) ( ၁ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/014-MahasiSayadawGyi-PiTeatThanBalZin(2)-1323.mp3">၁၄။ ၁၃၂၃ ခုႏွစ္ ပီတိသေမၺာဇၥ်င္ တရားေတာ္ 
								(၂) ( ၁ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/015-MahasiSayadawGyi-PiTeatThanBalZin(3)-1323.mp3">၁၅။ ၁၃၂၃ ခုႏွစ္ ပီတိသေမၺာဇၥ်င္ တရားေတာ္ 
								(၃) ( ၃၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/016-MahasiSayadawGyi-DaweiTrip-1323.mp3">၁၆။ ၁၃၂၃ ခုႏွစ္ ေမာ္လၿမိဳင္ - ထားဝယ္ ခရီးစဥ္ ( 
								၁၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/017-MahasiSayadawGyi-DhamarNupassanaSitaphatan(1)-1323.mp3">၁၇။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- ဓမၼာႏုပႆနာ သတိပ႒ာန္ (၁) ( ၁ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/018-MahasiSayadawGyi-DhamarNupassanaSitaphatan(2)-1323.mp3">
								၁၈။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - ဓမၼာႏုပႆနာ 
								သတိပ႒ာန္ (၂) ( ၁ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/019-MahasiSayadawGyi-DhamarNupassanaSitaphatan(3)-1323.mp3">
								၁၉။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - ဓမၼာႏုပႆနာ 
								သတိပ႒ာန္ (၃) ( ၄၆ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/020-MahasiSayadawGyi-DhamarNupassanaSitaphatan(4)-1323.mp3">
								၂၀။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - ဓမၼာႏုပႆနာ 
								သတိပ႒ာန္ (၄) ( ၁ နာရီ ၆ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/021-MahasiSayadawGyi-DukhaThitsar(1)-1323.mp3">၂၁။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- ဒုကၡသစၥာ (၁) ( ၁ နာရီ 
								၉ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/022-MahasiSayadawGyi-DukhaThitsar(2)-1323.mp3">
								၂၂။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - ဒုကၡသစၥာ 
								(၂) ( ၄၄ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/023-MahasiSayadawGyi-ThamudayaThitsar-1323.mp3">
								၂၃။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - သမုဒၵယသစၥာ ( 
								၁ နာရီ ၁၆ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/024-MahasiSayadawGyi-NiyawdaThitsar(1)-1323.mp3">
								၂၄။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - နိေယဓသစၥာ 
								(၁) ( ၁ နာရီ ၆ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/025-MahasiSayadawGyi-NiyawdaThitsar(2)-1323.mp3">၂၅။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- နိေယဓသစၥာ (၂) ( ၁ နာရီ 
								၁၂ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/026-MahasiSayadawGyi-NiyawdaThitsar(3)-1323.mp3">
								၂၆။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - နိေယဓသစၥာ 
								(၃) ( ၃ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/027-MahasiSayadawGyi-MeggaThitsar(1)-1323.mp3">
								၂၇။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၁) ( ၁ နာရီ ၂၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/028-MahasiSayadawGyi-MeggaThitsar(2)-1323.mp3">
								၂၈။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၂) ( ၂၈ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/029-MahasiSayadawGyi-MeggaThitsar(3)-1323.mp3">
								၂၉။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၃) ( ၁ နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/030-MahasiSayadawGyi-MeggaThitsar(4)-1323.mp3">၃၀။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- မဂၢသစၥာ (၄) ( ၅ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/031-MahasiSayadawGyi-MeggaThitsar(5)-1323.mp3">
								၃၁။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၅) ( ၁ နာရီ ၁၁ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/032-MahasiSayadawGyi-MeggaThitsar(6)-1323.mp3">
								၃၂။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၆) ( ၁ နာရီ ၁၃ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/033-MahasiSayadawGyi-MeggaThitsar(7)-1323.mp3">၃၃။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- မဂၢသစၥာ (၇) ( ၁ နာရီ 
								၁၂ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/034-MahasiSayadawGyi-MeggaThitsar(8)-1323.mp3">
								၃၄။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၈) ( ၅ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/035-MahasiSayadawGyi-MeggaThitsar(9)-1323.mp3">၃၅။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- မဂၢသစၥာ (၉) ( ၁ နာရီ ၇ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/036-MahasiSayadawGyi-MeggaThitsar(10)-1323.mp3">
								၃၆။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - မဂၢသစၥာ 
								(၁၀) ( ၁၃ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/037-MahasiSayadawGyi-SatipahtanaSuttar(1)-1323.mp3">
								၃၇။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၁) ( ၁ နာရီ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/038-MahasiSayadawGyi-SatipahtanaSuttar(2)-1323.mp3">
								၃၈။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၂) ( ၁ နာရီ 
								၂၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/039-MahasiSayadawGyi-SatipahtanaSuttar(3)-1323.mp3">၃၉။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- သတိပ႒ာနသုတၱံ (၃) ( ၂၉ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/040-MahasiSayadawGyi-SatipahtanaSuttar(4)-1323.mp3">
								၄၀။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၄) ( ၁ နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/041-MahasiSayadawGyi-SatipahtanaSuttar(5)-1323.mp3">
								၄၁။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၅) ( ၁၁ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/042-MahasiSayadawGyi-SatipahtanaSuttar(6)-1323.mp3">၄၂။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- သတိပ႒ာနသုတၱံ (၆) ( ၁ နာရီ 
								၁၃ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/043-MahasiSayadawGyi-SatipahtanaSuttar(7)-1323.mp3">
								၄၃။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၇) ( ၄၃ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/044-MahasiSayadawGyi-SatipahtanaSuttar(8)-1323.mp3">
								၄၄။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၈) ( ၂ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/045-MahasiSayadawGyi-SatipahtanaSuttar(9)-1323.mp3">၄၅။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- သတိပ႒ာနသုတၱံ (၉) ( ၁ နာရီ 
								၁၁ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/046-MahasiSayadawGyi-SatipahtanaSuttar(10)-1323.mp3">၄၆။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ 
								- သတိပ႒ာနသုတၱံ (၁၀) ( ၁၉ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/047-MahasiSayadawGyi-SatipahtanaSuttar(11)-1323.mp3">
								၄၇။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၁၁) ( ၄၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/048-MahasiSayadawGyi-SatipahtanaSuttar(12)-1323.mp3">
								၄၈။ ၁၃၂၃ ခုႏွစ္ သစၥာေလးပါး တရားေတာ္ - 
								သတိပ႒ာနသုတၱံ (၁၂) ( ၁ နာရီ 
								၆ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/049-MahasiSayadawGyi-donation-tayar-1323.mp3">၄၉။ ၁၃၂၃ ခုႏွစ္ ဝိသုဒၶိမဂ္ မဟာဋီကာနိႆယ ပုံႏွိပ္ 
								အလွဴေငြ ေပးအပ္ပြဲ အႏုေမာဒနာ တရားေတာ္ (၃၆ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/050-MahasiSayadawGyi-AriyaWatha(1)-1324.mp3">၅၀။ ၁၃၂၄ ခုႏွစ္ အရိယာဝါသ တရားေတာ္ 
								(၁) ( ၁နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/051-MahasiSayadawGyi-AriyaWatha(2)-1324.mp3">၅၁။ ၁၃၂၄ ခုႏွစ္ အရိယာဝါသ တရားေတာ္ 
								(၂) ( ၁နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/052-MahasiSayadawGyi-AriyaWatha(3)-1324.mp3">၅၂။ ၁၃၂၄ ခုႏွစ္ အရိယာဝါသ 
								တရားေတာ္ (၃) ( ၁နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/053-MahasiSayadawGyi-AriyaWatha(4)-1324.mp3">၅၃။ ၁၃၂၄ ခုႏွစ္ အရိယာဝါသ တရားေတာ္ 
								(၄) ( ၁နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/054-MahasiSayadawGyi-AriyaWatha(5)-1324.mp3">၅၄။ ၁၃၂၄ ခုႏွစ္ အရိယာဝါသ တရားေတာ္ 
								(၅) ( ၁နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/055-MahasiSayadawGyi-AriyaWatha(6)-1324.mp3">၅၅။ ၁၃၂၄ ခုႏွစ္ အရိယာဝါသ 
								တရားေတာ္ (၆) ( ၁နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/056-MahasiSayadawGyi-BagoSasanaYeikTha-kathina-1324.mp3">၅၆။ ၁၃၂၄ ခုႏွစ္ ပဲခူးသာသနာ့ရိပ္သာ ကထိန္ တရားေတာ္ 
								(၁ နာရီ ၃၀ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/057-MahasiSayadawGyi-AhZitaSutta(1)-at-BagoSasanaYeikTha-1324.mp3">၅၇။ ၁၃၂၄ ခုႏွစ္ အဇိတသုတ္တရားေတာ္ 
								(၁) (ပဲခူးသာသနာ့ရိပ္သာ) ( 
								၁နာရီ&nbsp; ၁၁မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/058-MahasiSayadawGyi-AhZitaSutta(2)-at-BagoSasanaYeikTha-1324.mp3">၅၈။ ၁၃၂၄ ခုႏွစ္ အဇိတသုတ္တရားေတာ္ 
								(၂) (ပဲခူးသာသနာ့ရိပ္သာ) ( 
								၁နာရီ&nbsp; ၁၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/059-MahasiSayadawGyi-AhZitaSutta(3)-at-BagoSasanaYeikTha-1324.mp3">၅၉။ ၁၃၂၄ ခုႏွစ္ အဇိတသုတ္တရားေတာ္ 
								(၃) (ပဲခူးသာသနာ့ရိပ္သာ) ( 
								၁၂ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/060-MahasiSayadawGyi-BasicVipassana(1)-1324.mp3">၆၀။ ၁၃၂၄ ခုႏွစ္ ဝိပႆနာအေျခခံ တရားေတာ္ 
								(၁) ( ၁နာရီ&nbsp;၁၀ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/061-MahasiSayadawGyi-BasicVipassana(1)-1324.mp3">၆၁။ ၁၃၂၄ ခုႏွစ္ ဝိပႆနာအေျခခံ တရားေတာ္ 
								(၂) ( ၁နာရီ&nbsp;၁၁ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/062-MahasiSayadawGyi-BasicVipassana(1)-1324.mp3">၆၂။ ၁၃၂၄ ခုႏွစ္ ဝိပႆနာအေျခခံ တရားေတာ္ 
								(၃) ( ၁နာရီ&nbsp;၁၂ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/063-MahasiSayadawGyi-BasicVipassana(1)-1324.mp3">၆၃။ ၁၃၂၄ ခုႏွစ္ ဝိပႆနာအေျခခံ တရားေတာ္ 
								(၄) ( ၁နာရီ&nbsp;၉ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/064-MahasiSayadawGyi-BasicVipassana(1)-1324.mp3">၆၄။ ၁၃၂၄ ခုႏွစ္ ဝိပႆနာအေျခခံ တရားေတာ္ 
								(၅) ( ၁နာရီ&nbsp;)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-01/065-MahasiSayadawGyi-BasicVipassana(1)-1324.mp3">၆၅။ ၁၃၂၄ ခုႏွစ္ ဝိပႆနာအေျခခံ တရားေတာ္ 
								(၆) ( ၅၆မိနစ္)</a></font></p>
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
								<font size="5">MP3 စုေပါင္း အမွတ္စဥ္ (၁၁) - 
								၉၅ ပုဒ္</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/001-MahasiSayadawGyi-AhpannaSutta-1335-DVD11.mp3">
								၁။ ၁၃၃၅ ခုႏွစ္ အပဏၰသုတ္တရားေတာ္။ ( ၁နာရီ 
								၄၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/002-MahasiSayadawGyi-Awwada-1335-DVD11.mp3">
								၂။ ၁၃၃၅ ခုႏွစ္&nbsp; ႏွစ္ပတ္လည္ပူေဇာ္ပြဲၾသဝါဒ 
								တရားေတာ္။ ( ၁နာရီ ၁၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/003-MahasiSayadawGyi-AukChayThein-1335-DVD11.mp3">
								၃။ ၁၃၃၅ ခုႏွစ္&nbsp; ေအာက္ေျခသိမ္းတရားေတာ္။ ( 
								၁နာရီ ၃၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/004-MahasiSayadawGyi-Kathana(1)-1335-DVD11.mp3">
								၄။ ၁၃၃၅ ခုႏွစ္&nbsp; ကထိန္အႏုေမာဓနာတရားေတာ္(၁) ( 
								၁နာရီ ၃၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/005-MahasiSayadawGyi-Kathana(1)-1335-DVD11.mp3">
								၅။ ၁၃၃၅ ခုႏွစ္&nbsp; ကထိန္အႏုေမာဓနာတရားေတာ္(၂) ( 
								၁နာရီ ၃၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/006-MahasiSayadawGyi-free-from-ThanthayarWeiallda-1335-DVD11.mp3">
								၆။ ၁၃၃၅ ခုႏွစ္&nbsp; သံသရာဝဲၾသဃမွ 
								လြန္ေျမာက္ေရးတရားေတာ္။ ( ၁နာရီ )</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/007-MahasiSayadawGyi-ThamaSutta(1)-1335-DVD11.mp3">
								၇။ ၁၃၃၅ ခုႏွစ္&nbsp; သမၼသသုတ္ တရားေတာ္ (၁) ( 
								၄နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/008-MahasiSayadawGyi-ThamaSutta(2)-1335-DVD11.mp3">
								၈။ ၁၃၃၅ ခုႏွစ္&nbsp; သမၼသသုတ္ တရားေတာ္ (၂) ( 
								၄နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/009-MahasiSayadawGyi-ThamaSutta(3)-1335-DVD11.mp3">
								၉။ ၁၃၃၅ ခုႏွစ္&nbsp; သမၼသသုတ္ တရားေတာ္ (၃) ( 
								၄နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/010-MahasiSayadawGyi-ThamaSutta(4)-1335-DVD11.mp3">
								၁၀။ ၁၃၃၅ ခုႏွစ္&nbsp; သမၼသသုတ္ တရားေတာ္ (၄) ( 
								၄နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/011-MahasiSayadawGyi-ThamaSutta(5)-1335-DVD11.mp3">
								၁၁။ ၁၃၃၅ ခုႏွစ္&nbsp; သမၼသသုတ္ တရားေတာ္ (၅) ( 
								၄နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/002-MahasiSayadawGyi-Awwada-1335-DVD11.mp3">
								၁၂။ ၁၃၃၅ ခုႏွစ္&nbsp; သီလဝႏၱသုတ္ တရားေတာ္(၁) ( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/013-MahasiSayadawGyi-SilawontaSutta(1)-1335-DVD11.mp3">
								၁၃။ ၁၃၃၅ ခုႏွစ္&nbsp; သီလဝႏၱသုတ္ တရားေတာ္(၂) ( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/014-MahasiSayadawGyi-SilawontaSutta(1)-1335-DVD11.mp3">
								၁၄။ ၁၃၃၅ ခုႏွစ္&nbsp; သီလဝႏၱသုတ္ တရားေတာ္(၃) ( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/015-MahasiSayadawGyi-SilawontaSutta(1)-1335-DVD11.mp3">
								၁၅။ ၁၃၃၅ ခုႏွစ္&nbsp; သီလဝႏၱသုတ္ တရားေတာ္(၄) ( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/016-MahasiSayadawGyi-Thitsarlaypar-1335-DVD11.mp3">
								၁၆။ ၁၃၃၅ ခုႏွစ္&nbsp; သစၥာေလးပါးတရားေတာ္။ ( 
								၁နာရီ ၃၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/017-MahasiSayadawGyi-Yahankongkyintsin(1)-1335-DVD11.mp3">
								၁၇။ ၁၃၃၅ ခုႏွစ္&nbsp; ရဟန္းေကာင္းက်င့္စဥ္ 
								တရားေတာ္(၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/018-MahasiSayadawGyi-Yahankongkyintsin(2)-1335-DVD11.mp3">
								၁၈။ ၁၃၃၅ ခုႏွစ္&nbsp; ရဟန္းေကာင္းက်င့္စဥ္ 
								တရားေတာ္(၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/019-MahasiSayadawGyi-Kathina(1)-1335-DVD11.mp3">
								၁၉။ ၁၃၃၅ ခုႏွစ္&nbsp; ကထိန္အႏုေမာဓနာ တရားေတာ္ 
								(၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/020-MahasiSayadawGyi-Kathina(2)-1335-DVD11.mp3">
								၂၀။ ၁၃၃၅ ခုႏွစ္&nbsp; ကထိန္အႏုေမာဓနာ တရားေတာ္ 
								(၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/021-MahasiSayadawGyi-WarsoAwwada-1336-DVD11.mp3">
								၂၁။ ၁၃၃၆ ခုႏွစ္&nbsp; ဝါဆိုၾသဝါဒ တရားေတာ္။ ( 
								၄၅မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/022-MahasiSayadawGyi-YahankhanShinpyu-1336-DVD11.mp3">
								၂၂။ ၁၃၃၆ ခုႏွစ္ ရဟန္းခံရွင္ျပဳ တရားေတာ္။ ( 
								၁နာရီ)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/023-MahasiSayadawGyi-PalinYaesetcha-1337-DVD11.mp3">
								၂၃။ ၁၃၃၇ ခုႏွစ္ ပလႅင္ေရစက္ခ် တရားေတာ္။ ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/024-MahasiSayadawGyi-ShifPhyarMagginNibbanwin(1)-1338-DVD11.mp3">
								၂၄။ ၁၃၃၈ ခုႏွစ္ ရွစ္ျဖာမဂၢင္ နိဗၺာန္ဝင္ 
								တရားေတာ္(၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/025-MahasiSayadawGyi-ShifPhyarMagginNibbanwin(2)-1338-DVD11.mp3">
								၂၅။ ၁၃၃၈ ခုႏွစ္ ရွစ္ျဖာမဂၢင္ နိဗၺာန္ဝင္ 
								တရားေတာ္(၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/026-MahasiSayadawGyi-ShifPhyarMagginNibbanwin(3)-1338-DVD11.mp3">
								၂၆။ ၁၃၃၈ ခုႏွစ္ ရွစ္ျဖာမဂၢင္ နိဗၺာန္ဝင္ 
								တရားေတာ္(၃) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/027-MahasiSayadawGyi-SilawontaSutta(1)-1338-DVD11.mp3">
								၂၇။ ၁၃၃၈ ခုႏွစ္ သီလဝႏၱသုတ္ တရားေတာ္(၁) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/028-MahasiSayadawGyi-SilawontaSutta(2)-1338-DVD11.mp3">
								၂၈။ ၁၃၃၈ ခုႏွစ္ သီလဝႏၱသုတ္ တရားေတာ္(၂) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/029-MahasiSayadawGyi-SilawontaSutta(3)-1338-DVD11.mp3">
								၂၉။ ၁၃၃၈ ခုႏွစ္ သီလဝႏၱသုတ္ တရားေတာ္(၃) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/030-MahasiSayadawGyi-SilawontaSutta(4)-1338-DVD11.mp3">
								၃၀။ ၁၃၃၈ ခုႏွစ္ သီလဝႏၱသုတ္ တရားေတာ္(၄) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/031-MahasiSayadawGyi-SilawontaSutta(5)-1338-DVD11.mp3">
								၃၁။ ၁၃၃၈ ခုႏွစ္ သီလဝႏၱသုတ္ တရားေတာ္(၅) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/032-MahasiSayadawGyi-SilawontaSutta(6)-1338-DVD11.mp3">
								၃၂။ ၁၃၃၈ ခုႏွစ္ သီလဝႏၱသုတ္ တရားေတာ္(၆) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/033-MahasiSayadawGyi-Allwadakahtar-1339-DVD11.mp3">
								၃၃။ ၁၃၃၉ ခုႏွစ္ ၾသဝါဒ ကထာ တရားေတာ္ ( ၁၈ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/034-MahasiSayadawGyi-MyaTheintankyaungYaesetcha(1)-1339-DVD11.mp3">
								၃၄။ ၁၃၃၉ ခုႏွစ္ ျမသိန္းတန္ေက်ာင္း ေရစက္ခ် 
								တရားေတာ္(၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/035-MahasiSayadawGyi-MyaTheintankyaungYaesetcha(2)-1339-DVD11.mp3">
								၃၅။ ၁၃၃၉ ခုႏွစ္ ျမသိန္းတန္ေက်ာင္း ေရစက္ခ် 
								တရားေတာ္(၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/036-MahasiSayadawGyi-Pahtan-no-9-1339-DVD11.mp3">
								၃၆။ ၁၃၃၉ ခုႏွစ္ ပ႒ာန္းတရားေတာ္ (၁) ဥပနိႆယပစၥည္း 
								(ဝါေတာ္စဥ္) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/037-MahasiSayadawGyi-Pahtan-no-14-15-1339-DVD11.mp3">
								၃၇။ ၁၃၃၉ ခုႏွစ္ ပ႒ာန္းတရားေတာ္ (၂)&nbsp; ၀ိပါက + 
								အဟာရ ပစၥည္း(ဝါေတာ္စဥ္) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/038-MahasiSayadawGyi-Pahtan-no-16-1339-DVD11.mp3">
								၃၈။ ၁၃၃၉ ခုႏွစ္ ပ႒ာန္းတရားေတာ္ (၃) ဣၿႏၵိယပစၥည္း 
								(ဝါေတာ္စဥ္) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/039-MahasiSayadawGyi-Pahtan-no-17-1339-DVD11.mp3">
								၃၉။ ၁၃၃၉ ခုႏွစ္ ပ႒ာန္းတရားေတာ္ (၄) စ်ာနပစၥည္း 
								(ဝါေတာ္စဥ္) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/040-MahasiSayadawGyi-Pahtan-no-18-1339-DVD11.mp3">
								၄၀။ ၁၃၃၉ ခုႏွစ္ ပ႒ာန္းတရားေတာ္ (၅) မဂၢပစၥည္း 
								(ဝါေတာ္စဥ္) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/041-MahasiSayadawGyi-Pahtan-no-19-to-24-1339-DVD11.mp3">
								၄၁။ ၁၃၃၉ ခုႏွစ္ ပ႒ာန္းတရားေတာ္ (၆) သမၸယုတၱ၊ 
								၀ိပၸယုတၱ၊ အတၳိ၊ နတၳိ၊ ၀ိဂတ၊ 
								အ၀ိဂတပစၥေယာ(ဝါေတာ္စဥ္) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/042-MahasiSayadawGyi-Allwarda-1340-DVD11.mp3">
								၄၂။ ၁၃၄၀ ခုႏွစ္ ေခ်ာင္းဆုံ မုရစ္ႀကီးရိပ္သာ ၾသဝါဒ 
								တရားေတာ္ ( ၂၄ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/043-MahasiSayadawGyi-BudaykaratSutta(1)-1340-DVD11.mp3">
								၄၃။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၁) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/044-MahasiSayadawGyi-BudaykaratSutta(2)-1340-DVD11.mp3">
								၄၄။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၂) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/045-MahasiSayadawGyi-BudaykaratSutta(3)-1340-DVD11.mp3">
								၄၅။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၃) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/046-MahasiSayadawGyi-BudaykaratSutta(4)-1340-DVD11.mp3">
								၄၆။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၄) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/047-MahasiSayadawGyi-BudaykaratSutta(5)-1340-DVD11.mp3">
								၄၇။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၅) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/048-MahasiSayadawGyi-BudaykaratSutta(6)-1340-DVD11.mp3">
								၄၈။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၆) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/049-MahasiSayadawGyi-BudaykaratSutta(7)-1340-DVD11.mp3">
								၄၉။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၇) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/050-MahasiSayadawGyi-BudaykaratSutta(8)-1340-DVD11.mp3">
								၅၀။ ၁၃၄၀ ခုႏွစ္ ဘေဒၵကရတၱသုတ္ တရားေတာ္ (၈) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/051-MahasiSayadawGyi-DhammadaryatSutta(1)-1340-DVD11.mp3">
								၅၁။ ၁၃၄၀ ခုႏွစ္ ဓမၼဒါယာဒသုတ္တရားေတာ္(၁) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/052-MahasiSayadawGyi-DhammadaryatSutta(2)-1340-DVD11.mp3">
								၅၂။ ၁၃၄၀ ခုႏွစ္ ဓမၼဒါယာဒသုတ္တရားေတာ္(၂) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/053-MahasiSayadawGyi-WisudaryoneSayadawZarpana(1)-1340-DVD11.mp3">
								၅၃။ ၁၃၄၁ ခုႏွစ္ ဗဟန္း၊ 
								မဟာဝိသုဒၶါရုံေရႊက်င္တိုက္သစ္ ဆရာေတာ္ႀကီး 
								အရွင္ဝါသဘိဝံသ စ်ာပမ၌ ေဟာၾကားအပ္ေသာတရားေတာ္(၁)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/054-MahasiSayadawGyi-WisudaryoneSayadawZarpana(2)-1340-DVD11.mp3">
								၅၄။ ၁၃၄၁ ခုႏွစ္ ဗဟန္း၊ 
								မဟာဝိသုဒၶါရုံေရႊက်င္တိုက္သစ္ ဆရာေတာ္ႀကီး 
								အရွင္ဝါသဘိဝံသ စ်ာပမ၌ ေဟာၾကားအပ္ေသာတရားေတာ္(၂)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/055-MahasiSayadawGyi-WisudaryoneSayadawZarpana(3)-1340-DVD11.mp3">
								၅၅။ ၁၃၄၁ ခုႏွစ္ ဗဟန္း၊ 
								မဟာဝိသုဒၶါရုံေရႊက်င္တိုက္သစ္ ဆရာေတာ္ႀကီး 
								အရွင္ဝါသဘိဝံသ စ်ာပမ၌ ေဟာၾကားအပ္ေသာတရားေတာ္(၃)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/056-MahasiSayadawGyi-WisudaryoneSayadawZarpana(4)-1340-DVD11.mp3">
								၅၆။ ၁၃၄၁ ခုႏွစ္ ဗဟန္း၊ 
								မဟာဝိသုဒၶါရုံေရႊက်င္တိုက္သစ္ ဆရာေတာ္ႀကီး 
								အရွင္ဝါသဘိဝံသ စ်ာပမ၌ ေဟာၾကားအပ္ေသာတရားေတာ္(၄)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/057-MahasiSayadawGyi-AnargatabayaSutta(1)-DVD11.mp3">
								၅၇။ အနာဂတဘယသုတ္တရားေတာ္ (၁) (ဝါဆိုၾသဝါဒ) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/058-MahasiSayadawGyi-AnargatabayaSutta(2)-DVD11.mp3">
								၅၈။ အနာဂတဘယသုတ္တရားေတာ္ (၂) (ဝါဆိုၾသဝါဒ) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/059-MahasiSayadawGyi-ArditaSutta(1)-DVD11.mp3">
								၅၉။ အာဒိတၱသုတ္ (၁) (ေျခာက္ထပ္ႀကီးေက်ာင္းတိုက္) 
								(နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/060-MahasiSayadawGyi-ArditaSutta(2)-DVD11.mp3">
								၆၀။ အာဒိတၱသုတ္ (၂) (ေျခာက္ထပ္ႀကီးေက်ာင္းတိုက္) 
								(နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/061-MahasiSayadawGyi-Awwardapartimoul-DVD11.mp3">
								၆၁။ ၾသဝါဒပါတိေမာက္တရားေတာ္ (မဂၤလာဗ်ဴဟာ) ( ၁နာရီ 
								၂၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/062-MahasiSayadawGyi-KaungChinLayPhyar(1)-DVD11.mp3">
								၆၂။ ေကာင္းျခင္းေလးျဖာ တရားေတာ္ (၁) (ဓမၼေတးဝိဇၨာ) 
								( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/063-MahasiSayadawGyi-KaungChinLayPhyar(2)-DVD11.mp3">
								၆၃။ ေကာင္းျခင္းေလးျဖာ တရားေတာ္ (၂) (ဓမၼေတးဝိဇၨာ) 
								( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/064-MahasiSayadawGyi-KaungChinLayPhyar(3)-DVD11.mp3">
								၆၄။ ေကာင္းျခင္းေလးျဖာ တရားေတာ္ (၃) (ဓမၼေတးဝိဇၨာ) 
								( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/065-MahasiSayadawGyi-KaungChinLayPhyar(4)-DVD11.mp3">
								၆၅။ ေကာင္းျခင္းေလးျဖာ တရားေတာ္ (၄) (ဓမၼေတးဝိဇၨာ) 
								( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/066-MahasiSayadawGyi-ManipanitaSutta(1)-DVD11.mp3">
								၆၆။ မဓုပိ႑ိကသုတ္တရားေတာ္ (၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/067-MahasiSayadawGyi-ManipanitaSutta(2)-DVD11.mp3">
								၆၇။ မဓုပိ႑ိကသုတ္တရားေတာ္ (၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/068-MahasiSayadawGyi-MagginShifpar-DVD11.mp3">
								၆၈။ မဂၢင္ရွစ္ပါးတရားေတာ္ (ဆိပ္ခြန္၊ ေရႊဘို) ( 
								၁နာရီ ၂၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/069-MahasiSayadawGyi-AhKwintTharKhiteLoneLaSight(1)-DVD11.mp3">
								၆၉။ အခြင့္သာခိုက္ လုံ႕လစိုက္ တရားေတာ္ (၁) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/070-MahasiSayadawGyi-AhKwintTharKhiteLoneLaSight(2)-DVD11.mp3">
								၇၀။ အခြင့္သာခိုက္ လုံ႕လစိုက္ တရားေတာ္ (၂) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/071-MahasiSayadawGyi-AhKwintTharKhiteLoneLaSight(3)-DVD11.mp3">
								၇၁။ အခြင့္သာခိုက္ လုံ႕လစိုက္ တရားေတာ္ (၃) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/072-MahasiSayadawGyi-AhKwintTharKhiteLoneLaSight(4)-DVD11.mp3">
								၇၂။ အခြင့္သာခိုက္ လုံ႕လစိုက္ တရားေတာ္ (၄) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/073-MahasiSayadawGyi-AhKwintTharKhiteLoneLaSight(5)-DVD11.mp3">
								၇၃။ အခြင့္သာခိုက္ လုံ႕လစိုက္ တရားေတာ္ (၅) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/074-MahasiSayadawGyi-AhKwintTharKhiteLoneLaSight(6)-DVD11.mp3">
								၇၄။ အခြင့္သာခိုက္ လုံ႕လစိုက္ တရားေတာ္ (၆) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/075-MahasiSayadawGyi-SaveGuard-to-buddhasana(1)-DVD11.mp3">
								၇၅။ ဗုဒၶသာသနအႏၱာရယ္ ကာကြယ္ေရးတရားေတာ္ (၁) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/076-MahasiSayadawGyi-SaveGuard-to-buddhasana(2)-DVD11.mp3">
								၇၆။ ဗုဒၶသာသနအႏၱာရယ္ ကာကြယ္ေရးတရားေတာ္ (၂) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/077-MahasiSayadawGyi-SaveGuard-to-buddhasana(3)-DVD11.mp3">
								၇၇။ ဗုဒၶသာသနအႏၱာရယ္ ကာကြယ္ေရးတရားေတာ္ (၃) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/078-MahasiSayadawGyi-SaveGuard-to-buddhasana(4)-DVD11.mp3">
								၇၈။ ဗုဒၶသာသနအႏၱာရယ္ ကာကြယ္ေရးတရားေတာ္ (၄) ( နာရီ 
								မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/079-MahasiSayadawGyi-Awwarda(1)-DVD11.mp3">
								၇၉။ ပူေဇာ္ပြဲၾသဝါဒ တရားေတာ္ (၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/080-MahasiSayadawGyi-Awwarda(2)-DVD11.mp3">
								၈၀။ ပူေဇာ္ပြဲၾသဝါဒ တရားေတာ္ (၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/081-MahasiSayadawGyi-SangaGonedaw-DVD11.mp3">
								၈၁။ သံဃာ့ဂုဏ္ေတာ္တရားေတာ္ ( ၄၀မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/082-MahasiSayadawGyi-Satipahtantayartaw(1)-DVD11.mp3">
								၈၂။ သတိပ႒ာန္တရားေတာ္ (၁) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/083-MahasiSayadawGyi-Satipahtantayartaw(2)-DVD11.mp3">
								၈၃။ သတိပ႒ာန္တရားေတာ္ (၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/084-MahasiSayadawGyi-Satipahtantayartaw(3)-DVD11.mp3">
								၈၄။ သတိပ႒ာန္တရားေတာ္ (၃) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/085-MahasiSayadawGyi-the-most-important-tayar-in-sasana-DVD11.mp3">
								၈၅။ သာသနာေတာ္တြင္း အေရးႀကီးဆုံးတရားေတာ္ ( 
								၄၅မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/086-MahasiSayadawGyi-OopantaSutta(1)-DVD11.mp3">
								၈၆<font size="4">။ ဥပန္တသုတ္တရားေတာ္ (၁) ( နာရီ 
								မိနစ္)</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/087-MahasiSayadawGyi-OopantaSutta(2)-DVD11.mp3">
								၈၇။ ဥပန္တသုတ္တရားေတာ္ (၂) ( နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/088-MahasiSayadawGyi-Dhammasatkyar(1)-DVD11.mp3">
								၈၈။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၁)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/089-MahasiSayadawGyi-Dhammasatkyar(2)-DVD11.mp3">
								၈၉။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၂)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/090-MahasiSayadawGyi-Dhammasatkyar(3)-DVD11.mp3">
								၉၀။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၃)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/091-MahasiSayadawGyi-Dhammasatkyar(4)-DVD11.mp3">
								၉၁။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၄)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/092-MahasiSayadawGyi-Dhammasatkyar(5)-DVD11.mp3">
								၉၂။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၅)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/093-MahasiSayadawGyi-Dhammasatkyar(6)-DVD11.mp3">
								၉၃။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၆)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/094-MahasiSayadawGyi-Dhammasatkyar(7)-DVD11.mp3">
								၉၄။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၇)( 
								နာရီ မိနစ္)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP3Library/MahasiSayadawUSobhanaMahathera/DVD-11/095-MahasiSayadawGyi-Dhammasatkyar(8)-DVD11.mp3">
								၉၅။ ၁၃၄၄ခုႏွစ္ ပ်ံလြန္ေတာ္မမူမီ 
								ေနာက္ဆုံးေဟာၾကားေတာ္မူေသာ ဓမၼစၾကာတရားေတာ္ (၈)( 
								နာရီ မိနစ္)</a></font></p>
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
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">။ တရားေတာ္ ( နာရီ မိနစ္)</font></p>
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
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								~~~~~ OLD MP3 files ~~~~~</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 01
								<br>
								<br>
								</font><font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/001%20MahasiSayadaw%20AhloatPayTaYarMyanmar.mp3">
								၁။ အလုပ္ေပးတရားေတာ္ (ျမန္မာ)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/002%20MahasiSayadaw%20AhloatPayTaYarMyanmar30min.mp3">
								၂။ အလုပ္ေပးတရားေတာ္ (ျမန္မာ)- ၃၀ မိနစ္ <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/003%20MahasiSayadaw%20AhloatPayTaYarMyanmar15min.mp3">
								၃။ အလုပ္ေပးတရားေတာ္ (ျမန္မာ)- ၁၅ မိနစ္ <br>
								</a></font><font size="5" face="Tim">4) 
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/004%20MahasiSayadaw%20AhloatPayTaYarChinese.mp3">Practical Vippassana Meditation Exercise (Chinese)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Tim">5) 
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/005%20MahasiSayadaw%20AhloatPayTaYarKorea.mp3">Practical Vippassana Meditation Exercise (Koera)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Tim">6) 
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/006%20MahasiSayadaw%20AhloatPayTaYarGerman.mp3">Practical Vippassana Meditation Exercise (German)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Tim">7) 
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/007%20MahasiSayadaw%20AhloatPayTaYarJapan.mp3">Practical Vippassana Meditation Exercise (Japan)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Tim">8) 
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/008%20MahasiSayadaw%20AhloatPayTaYarFrance.mp3">Practical Vippassana Meditation Exercise (France)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Tim">9) 
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/009%20MahasiSayadaw%20AhloatPayTaYarEnglish.mp3">Practical Vippassana Meditation Exercise (English)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/010%20MahasiSayadaw%20VipasanaAhChayKhanTaYarTaw01.mp3">
								၁၀။ ၀ိပႆနာအေျခခံတရားေတာ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/011%20MahasiSayadaw%20VipasanaAhChayKhanTaYarTaw02.mp3">
								၁၁။ ၀ိပႆနာအေျခခံတရားေတာ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/012%20MahasiSayadaw%20VipasanaAhChayKhanTaYarTaw03.mp3">
								၁၂။ ၀ိပႆနာအေျခခံတရားေတာ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/013%20MahasiSayadaw%20VipasanaAhChayKhanTaYarTaw04.mp3">
								၁၃။ ၀ိပႆနာအေျခခံတရားေတာ္ (၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/014%20MahasiSayadaw%20VipasanaAhChayKhanTaYarTaw05.mp3">
								၁၄။ ၀ိပႆနာအေျခခံတရားေတာ္ (၅)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/015%20MahasiSayadaw%20VipasanaAhChayKhanTaYarTaw06.mp3">
								၁၅။ ၀ိပႆနာအေျခခံတရားေတာ္ (၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc01/016%20MahasiSayadaw%20AhNarGaTaBaYaThout01.mp3">
								၁၆။ အနာဂတဘယသုတ္(၁)<br>
&nbsp;</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 02
								<br>
								</font>
								<font size="4" face="Zawgyi-One"><br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/001%20MahasiSayadaw%20AhNarGaTaBaYaThout02.mp3">
								၁။ အနာဂတဘယသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/002%20MahasiSayadaw%20DammaDarYaDaThout01.mp3">
								၂။ ဓမၼဒါယဒသုတ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/003%20MahasiSayadaw%20DammaDarYaDaThout02.mp3">
								၃။ ဓမၼဒါယဒသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/004%20MahasiSayadaw%20DoteKhaThitSarTaYarTaw01.mp3">
								၄။ ဒုကၡသစၥာတရားေတာ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/005%20MahasiSayadaw%20DoteKhaThitSarTaYarTaw02.mp3">
								၅။ ဒုကၡသစၥာတရားေတာ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/006%20MahasiSayadaw%20DoteKhaThitSarTaYarTaw03.mp3">
								၆။ ဒုကၡသစၥာတရားေတာ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/007%20MahasiSayadaw%20OakDayThaWeapBinGaThout01.mp3">
								၇။ ဥေဒၵသ၀ိဘဂၤသုတ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/008%20MahasiSayadaw%20OakDayThaWeapBinGaThout02.mp3">
								၈။ ဥေဒၵသ၀ိဘဂၤသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/009%20MahasiSayadaw%20OakDayThaWeapBinGaThout03.mp3">
								၉။ ဥေဒၵသ၀ိဘဂၤသုတ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/010%20MahasiSayadaw%20ThaTeatPaHtarNaThout01.mp3">
								၁၀။ သတိပ႒ာနသုတ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/011%20MahasiSayadaw%20ThaTeatPaHtarNaThout02.mp3">
								၁၁။ သတိပ႒ာနသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/012%20MahasiSayadaw%20ThaTeatPaHtarNaThout03.mp3">
								၁၂။ သတိပ႒ာနသုတ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/013%20MahasiSayadaw%20LawKaDanShitParTaYarTaw01.mp3">
								၁၃။ ေလာကဓံရွစ္ပါးတရားေတာ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc02/014%20MahasiSayadaw%20LawKaDanShitParTaYarTaw02.mp3">
								၁၄။ ေလာကဓံရွစ္ပါးတရားေတာ္ (၂)<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 03<br>
								</font><font size="4" face="Zawgyi-One"><br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/001%20MahasiSayadaw%20ShitPhyarMetGinNibbanWin01.mp3">
								၁။ ရွစ္ျဖာမဂၢင္နိဗၺာန္၀င္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/002%20MahasiSayadaw%20ShitPhyarMetGinNibbanWin02.mp3">
								၂။ ရွစ္ျဖာမဂၢင္နိဗၺာန္၀င္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/003%20MahasiSayadaw%20ShitPhyarMetGinNibbanWin03.mp3">
								၃။ ရွစ္ျဖာမဂၢင္နိဗၺာန္၀င္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/004%20MahasiSayadaw%20PaticcaSamupaTaYarTaw01.mp3">
								၄။ ပဋိစၥသမုပၸါဒ္တရားေတာ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/005%20MahasiSayadaw%20PaticcaSamupaTaYarTaw02.mp3">
								၅။ ပဋိစၥသမုပၸါဒ္တရားေတာ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/006%20MahasiSayadaw%20DammaSatKyarTayarTaw01.mp3">
								၆။ ဓမၼစႀကၤာတရားေတာ္ (၁) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/007%20MahasiSayadaw%20DammaSatKyarTayarTaw02.mp3">
								၇။ ဓမၼစႀကၤာတရားေတာ္ (၂) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/008%20MahasiSayadaw%20DammaSatKyarTayarTaw03.mp3">
								၈။ ဓမၼစႀကၤာတရားေတာ္ (၃) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/009%20MahasiSayadaw%20DammaSatKyarTayarTaw04.mp3">
								၉။ ဓမၼစႀကၤာတရားေတာ္ (၄) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/010%20MahasiSayadaw%20DammaSatKyarTayarTaw05.mp3">
								၁၀။ ဓမၼစႀကၤာတရားေတာ္ (၅) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/011%20MahasiSayadaw%20DammaSatKyarTayarTaw06.mp3">
								၁၁။ ဓမၼစႀကၤာတရားေတာ္ (၆) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/012%20MahasiSayadaw%20DammaSatKyarTayarTaw07.mp3">
								၁၂။ ဓမၼစႀကၤာတရားေတာ္ (၇) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc03/013%20MahasiSayadaw%20DammaSatKyarTayarTaw08.mp3">
								၁၃။ ဓမၼစႀကၤာတရားေတာ္ (၈) 
								(ဆရာေတာ္ေနာက္ဆုံးေဟာၾကားေတာ္မူခဲ့သည္႕တရား)<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 04<br>
								</font>
								<font size="4" face="Zawgyi-One"><br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/001%20MahasiSayadaw%20DammaSatKyarTayarTaw01.mp3">
								၁။ ဓမၼစႀကၤာတရားေတာ္ (၁) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/002%20MahasiSayadaw%20DammaSatKyarTayarTaw02.mp3">
								၂။ ဓမၼစႀကၤာတရားေတာ္ (၂) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/003%20MahasiSayadaw%20DammaSatKyarTayarTaw03.mp3">
								၃။ ဓမၼစႀကၤာတရားေတာ္ (၃) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/004%20MahasiSayadaw%20DammaSatKyarTayarTaw04.mp3">
								၄။ ဓမၼစႀကၤာတရားေတာ္ (၄) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/005%20MahasiSayadaw%20DammaSatKyarTayarTaw05.mp3">
								၅။ ဓမၼစႀကၤာတရားေတာ္ (၅) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/006%20MahasiSayadaw%20DammaSatKyarTayarTaw06.mp3">
								၆။ ဓမၼစႀကၤာတရားေတာ္ (၆) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/007%20MahasiSayadaw%20DammaSatKyarTayarTaw07.mp3">
								၇။ ဓမၼစႀကၤာတရားေတာ္ (၇) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/008%20MahasiSayadaw%20DammaSatKyarTayarTawe08.mp3">
								၈။ ဓမၼစႀကၤာတရားေတာ္ (၈) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/009%20MahasiSayadaw%20DammaSatKyarTayarTaw09.mp3">
								၉။ ဓမၼစႀကၤာတရားေတာ္ (၉) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/010%20MahasiSayadaw%20DammaSatKyarTayarTaw10.mp3">
								၁၀။ ဓမၼစႀကၤာတရားေတာ္ (၁၀) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/011%20MahasiSayadaw%20DammaSatKyarTayarTaw11.mp3">
								၁၁။ ဓမၼစႀကၤာတရားေတာ္ (၁၁) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc04/012%20MahasiSayadaw%20DammaSatKyarTayarTaw12.mp3">
								၁၂။ ဓမၼစႀကၤာတရားေတာ္ (၁၂) <br>
&nbsp;</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 05<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/001%20MahasiSayadaw%20DammaSatKyarTayarTaw13.mp3">
								၁။ ဓမၼစႀကၤာတရားေတာ္ (၁၃) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/002%20MahasiSayadaw%20DammaSatKyarTayarTaw14.mp3">
								၂။ ဓမၼစႀကၤာတရားေတာ္ (၁၄) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/003%20MahasiSayadaw%20DammaSatKyarTayarTaw15.mp3">
								၃။ ဓမၼစႀကၤာတရားေတာ္ (၁၅) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/004%20MahasiSayadaw%20DammaSatKyarTayarTaw16.mp3">
								၄။ ဓမၼစႀကၤာတရားေတာ္ (၁၆) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/005%20MahasiSayadaw%20DammaSatKyarTayarTaw17.mp3">
								၅။ ဓမၼစႀကၤာတရားေတာ္ (၁၇) <br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/006%20MahasiSayadaw%20SuLaWaiDaLaThout01.mp3">
								၆။ စူဠေ၀ဒလႅသုတ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/007%20MahasiSayadaw%20SuLaWaiDaLaThout02.mp3">
								၇။ စူဠေ၀ဒလႅသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/008%20MahasiSayadaw%20SuLaWaiDaLaThout03.mp3">
								၈။ စူဠေ၀ဒလႅသုတ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/009%20MahasiSayadaw%20SuLaWaiDaLaThout04.mp3">
								၉။ စူဠေ၀ဒလႅသုတ္ (၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/010%20MahasiSayadaw%20SuLaWaiDaLaThout05.mp3">
								၁၀။ စူဠေ၀ဒလႅသုတ္ (၅)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/011%20MahasiSayadaw%20SuLaWaiDaLaThout06.mp3">
								၁၁။ စူဠေ၀ဒလႅသုတ္ (၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc05/012%20MahasiSayadaw%20SuLaWaiDaLaThout07.mp3">
								၁၂။ စူဠေ၀ဒလႅသုတ္ (၇)<br>
&nbsp;</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 06<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/001%20MahasiSayadaw%20SuLaWaiDaLaThout08.mp3">
								၁။ စူဠေ၀ဒလႅသုတ္ (၈)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/002%20MahasiSayadaw%20SuLaWaiDaLaThout09.mp3">
								၂။ စူဠေ၀ဒလႅသုတ္ (၉)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/003%20MahasiSayadaw%20SuLaWaiDaLaThout10.mp3">
								၃။ စူဠေ၀ဒလႅသုတ္ (၁၀)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/004%20MahasiSayadaw%20SuLaWaiDaLaThout11.mp3">
								၄။ စူဠေ၀ဒလႅသုတ္ (၁၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/005%20MahasiSayadaw%20ErDateTaThout01.mp3">
								၅။ အာဒိတၲသုတ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/006%20MahasiSayadaw%20ErDateTaThout02.mp3">
								၆။ အာဒိတၲသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/007%20MahasiSayadaw%20ErDateTaThout03.mp3">
								၇။ အာဒိတၲသုတ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc06/008%20MahasiSayadaw%20ErDateTaThout04.mp3">
								၈။ အာဒိတၲသုတ္ (၄)<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 07<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/001%20MahasiSayadaw%20ErDateTaThout05.mp3">
								၁။ အာဒိတၲသုတ္ (၅)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/002%20MahasiSayadaw%20ErDateTaThout06.mp3">
								၂။ အာဒိတၲသုတ္ (၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/003%20MahasiSayadaw%20ErDateTaThout07.mp3">
								၃။ အာဒိတၲသုတ္ (၇)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/004%20MahasiSayadaw%20ErDateTaThout08.mp3">
								၄။ အာဒိတၲသုတ္ (၈)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/005%20MahasiSayadaw%20AhReatYarWarThaTaYarTaw01.mp3">
								၅။ အရိယာ၀ါသတရားေတာ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/006%20MahasiSayadaw%20AhReatYarWarThaTaYarTaw02.mp3">
								၆။ အရိယာ၀ါသတရားေတာ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/007%20MahasiSayadaw%20AhReatYarWarThaTaYarTaw03.mp3">
								၇။ အရိယာ၀ါသတရားေတာ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/008%20MahasiSayadaw%20AhReatYarWarThaTaYarTaw04.mp3">
								၈။ အရိယာ၀ါသတရားေတာ္ (၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc07/009%20MahasiSayadaw%20AhReatYarWarThaTaYarTaw05.mp3">
								၉။ အရိယာ၀ါသတရားေတာ္ (၅)<br>
&nbsp;</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 08<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/001%20MahasiSayadaw%20AhReatYarWarThaTaYarTaw06.mp3">
								၁။ အရိယာ၀ါသတရားေတာ္ (၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/002%20MahasiSayadaw%20ErThiWeatThawPaMaThout01.mp3">
								၂။ အာသီ၀ီေသာပမသုတ္ (၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/003%20MahasiSayadaw%20ErThiWeatThawPaMaThout02.mp3">
								၃။ အာသီ၀ီေသာပမသုတ္ (၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/004%20MahasiSayadaw%20ErThiWeatThawPaMaThout03.mp3">
								၄။ အာသီ၀ီေသာပမသုတ္ (၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/005%20MahasiSayadaw%20ErThiWeatThawPaMaThout04.mp3">
								၅။ အာသီ၀ီေသာပမသုတ္ (၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/006%20MahasiSayadaw%20ErThiWeatThawPaMaThout05.mp3">
								၆။ အာသီ၀ီေသာပမသုတ္ (၅)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/007%20MahasiSayadaw%20ErThiWeatThawPaMaThout06.mp3">
								၇။ အာသီ၀ီေသာပမသုတ္ (၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/008%20MahasiSayadaw%20ErThiWeatThawPaMaThout07.mp3">
								၈။ အာသီ၀ီေသာပမသုတ္ (၇)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/009%20MahasiSayadaw%20ErThiWeatThawPaMaThout08.mp3">
								၉။ အာသီ၀ီေသာပမသုတ္ (၈)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/010%20MahasiSayadaw%20ErThiWeatThawPaMaThout09.mp3">
								၁၀။ အာသီ၀ီေသာပမသုတ္ (၉)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/011%20MahasiSayadaw%20ErThiWeatThawPaMaThout10.mp3">
								၁၁။ အာသီ၀ီေသာပမသုတ္ (၁၀)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc08/012%20MahasiSayadaw%20ErThiWeatThawPaMaThout11.mp3">
								၁၂။ အာသီ၀ီေသာပမသုတ္ (၁၁)<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 09<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/001%20MahasiSayadaw%20ErThiWeatThawPaMaThout12.mp3">
								၁။ အာသီ၀ီေသာပမသုတ္ (၁၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/002%20MahasiSayadaw%20ErThiWeatThawPaMaThout13.mp3">
								၂။ အာသီ၀ီေသာပမသုတ္ (၁၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/003%20MahasiSayadaw%20ErThiWeatThawPaMaThout14.mp3">
								၃။ အာသီ၀ီေသာပမသုတ္ (၁၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/004%20MahasiSayadaw%20AhNetTaLatKhaNaThout01.mp3">
								၄။ အနတၲလကၡဏသုတ္(၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/005%20MahasiSayadaw%20AhNetTaLatKhaNaThout02.mp3">
								၅။ အနတၲလကၡဏသုတ္(၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/006%20MahasiSayadaw%20AhNetTaLatKhaNaThout03.mp3">
								၆။ အနတၲလကၡဏသုတ္(၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/007%20MahasiSayadaw%20AhNetTaLatKhaNaThout04.mp3">
								၇။ အနတၲလကၡဏသုတ္(၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/008%20MahasiSayadaw%20AhNetTaLatKhaNaThout05.mp3">
								၈။ အနတၲလကၡဏသုတ္(၅)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/009%20MahasiSayadaw%20AhNetTaLatKhaNaThout06.mp3">
								၉။ အနတၲလကၡဏသုတ္(၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/010%20MahasiSayadaw%20AhNetTaLatKhaNaThout07.mp3">
								၁၀။ အနတၲလကၡဏသုတ္(၇)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/011%20MahasiSayadaw%20AhNetTaLatKhaNaThout08.mp3">
								၁၁။ အနတၲလကၡဏသုတ္(၈)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/012%20MahasiSayadaw%20AhNetTaLatKhaNaThout09.mp3">
								၁၂။ အနတၲလကၡဏသုတ္(၉)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc09/013%20MahasiSayadaw%20AhNetTaLatKhaNaThout10.mp3">
								၁၃။ အနတၲလကၡဏသုတ္(၁၀)<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3Disc 10<br>
								&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/001%20MahasiSayadaw%20AhNetTaLatKhaNaThout11.mp3">
								၁။ အနတၲလကၡဏသုတ္(၁၁)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/002%20MahasiSayadaw%20AhNetTaLatKhaNaThout12.mp3">
								၂။ အနတၲလကၡဏသုတ္(၁၂)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/003%20MahasiSayadaw%20AhNetTaLatKhaNaThout13.mp3">
								၃။ အနတၲလကၡဏသုတ္(၁၃)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/004%20MahasiSayadaw%20AhNetTaLatKhaNaThout14.mp3">
								၄။ အနတၲလကၡဏသုတ္(၁၄)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/005%20MahasiSayadaw%20AhNetTaLatKhaNaThout15.mp3">
								၅။ အနတၲလကၡဏသုတ္(၁၅)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/006%20MahasiSayadaw%20AhNetTaLatKhaNaThout16.mp3">
								၆။ အနတၲလကၡဏသုတ္(၁၆)<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/MP3Disc10/007%20MahasiSayadaw%20AhNetTaLatKhaNaThout17.mp3">
								၇။ အနတၲလကၡဏသုတ္(၁၇)<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Franklin Gothic Medium">
								************************************</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Zawgyi-One">ဆ႒သဂၤါယနာတင္ 
								တရားေတာ္မ်ား<br>
								</font>
								<font size="4" face="Zawgyi-One">
								မဟာစည္ဆရာေတာ္ဘုရားႀကီးေမး၍ 
								မင္းကြန္းဆရာေတာ္ဘုရားႀကီးေျဖဆိုသည္<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="WinTaungyi"><br>
								</font><font size="5" face="Times New Roman">MP3 
								Disc 1<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/001%20Mahasi-Mingun-SatHtaThinGarYaNar%20SueLaKaMaWeakBinGaThoutTan.mp3">
								၁။ စူဠကမၼ၀ိဘဂၤသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/002%20Mahasi-Mingun-SatHtaThinGarYaNar%20ShinTharMaNaeKyawLayPar.mp3">
								၂။ ရွင္သာမေဏေက်ာ္ ၄ ပါး<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/003%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaelShaKaThoutTan.mp3">
								၃။ မယ္ယွက သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/004%20Mahasi-Mingun-SatHtaThinGarYaNar%20ThuWaNaMeatGaShweThaMinThoutTan.mp3">
								၄။ သု၀ဏၰမိဂ ေရႊသမင္ သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/005%20Mahasi-Mingun-SatHtaThinGarYaNar%20KeatNhaDeePaThoutTan.mp3">
								၅။ ကိဏွဒီပ သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/006%20Mahasi-Mingun-SatHtaThinGarYaNar%20NaKuLaPeTuThoutTan-YaMaTaThoutTan.mp3">
								၆။ နကုလပီတုသုတၲန္။ ယမတသတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/007%20Mahasi-Mingun-SatHtaThinGarYaNar%20TayThaTuNhaZat.mp3">
								၇။ ေတသသုဏဇာတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/008%20Mahasi-Mingun-SatHtaThinGarYaNar%20SueLaThuDarYaHanNharParSawYaThoutTan.mp3">
								၈။ စူ႒သုဘဒၵါ - ရဟန္းငါးပါးေစာရသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/009%20Mahasi-Mingun-SatHtaThinGarYaNar%20YaeWaKaTharMaNaeThoutTan.mp3">
								၉။ ေရ၀တသာမေဏ သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/010%20Mahasi-Mingun-SatHtaThinGarYaNar%20KuNaKaCoatSeatTheinDaWaThoutTan.mp3">
								၁၀။ ကု႑ကကုစိ ၦသိႏၶသ သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/011%20Mahasi-Mingun-SatHtaThinGarYaNar%20ParYaYarTheatThoutTan.mp3">
								၁၁။ ပါရရာသိ သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/012%20Mahasi-Mingun-SatHtaThinGarYaNar%20OoDaYaThoutTanMhaKaTeatBarYaDowarZaThoutTan.mp3">
								၁၂။ ဥဒယ သုတၲန္မွ ကတိဘာရဒြါဇသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/013%20Mahasi-Mingun-SatHtaThinGarYaNar%20ErZeeWaKaOopParLiThoutTan.mp3">
								၁၃။ အာဇိ၀က- ဥပါလီသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc01/014%20Mahasi-Mingun-SatHtaThinGarYaNar%20MahaThaTeatPaHtanNhitSanDaPaMaThoutTan.mp3">
								၁၄။ မဟာသတိပဌာန္ႏွင့္ စႏၵပမသုတၲန္<br>
								</a><br>
								<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One"><br>
								</font><font size="5" face="Times New Roman">MP3 
								Disc 2<br>
								</font><font size="4" face="Zawgyi-One"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/001%20Mahasi-Mingun-SatHtaThinGarYaNar%20MuLaPaYeatYarYaThoutTan.mp3">
								၁။ မူလပရိယာယ သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/002%20Mahasi-Mingun-SatHtaThinGarYaNar%20YarZaMaHtayAhThaZeatPuNetBaThuTaYaHanNharYarLatKhaNarYaeThonePar.mp3">
								၂။ ရာဓ မေထရ္ - အႆဇိပုနပၺသုတ ရဟန္ငါးရာ 
								လကၡဏာေရးသုံးပါး<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/003%20Mahasi-Mingun-SatHtaThinGarYaNar%20ZorTeatYaZat.mp3">
								၃။ ေဇာတိယဇာတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/004%20Mahasi-Mingun-SatHtaThinGarYaNar%20KanDaYaKaThoutTanPaulTaTeatYaThoutTan.mp3">
								၄။ ကႏၵရာက သုတၲန္။ ေပါတတိယသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/005%20Mahasi-Mingun-SatHtaThinGarYaNar%20PoatPathoutGeeLarNaThoutTan.mp3">
								၅။ ပုပၸ သုတ္ - ဂီလာနသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/006%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaRetDarZaThoutTan.mp3">
								၆။ မရဒြါဇသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/007%20Mahasi-Mingun-SatHtaThinGarYaNar%20CallThamMeeParThiTakeThaTharMaNayPyinSaOopParThaKarWouldHtoo.mp3">
								၇။ ေကာသမ ၻီပါသီတိႆ။ သာမေဏ။ ပဥၥဥပါသကာ၀တၳဳ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/008%20Mahasi-Mingun-SatHtaThinGarYaNar%20MeatLetKhaThoutTanMaNaThaTeatThout.mp3">
								၈။ မိလကၡသုတၲန္။ မဏသတိသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/009%20Mahasi-Mingun-SatHtaThinGarYaNar%20WeatTharKharOopParTheatKarWouldHtoo.mp3">
								၉။ ၀ိသာခါဥပါသိကာ၀တၳဳ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/010%20Mahasi-Mingun-SatHtaThinGarYaNar%20MeatHtaTaThoutAhHteetKaThout.mp3">
								၁၀။ မိဠတသုတ္၊ အ႒ိကသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/011%20Mahasi-Mingun-SatHtaThinGarYaNar%20KuLaMaKaThoutThaDanMaPaTeatYouPaKaThout.mp3">
								၁၁။ ကုလမကသုတ္၊ သဒၶမၸပဋိရူပကသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/012%20Mahasi-Mingun-SatHtaThinGarYaNar%20SueLaTaNharThinKharYaThoutMarYaKitZaNeatThaThout.mp3">
								၁၂။ စူဠတဏွာ၊ သခၤါယသုတ္၊ မာရကဇၨဏိသသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/013%20Mahasi-Mingun-SatHtaThinGarYaNar%20KaKaSuePaMaThoutNeatWarPaThout.mp3">
								၁၃။ ကာကစူပမသုတ၊ နိ၀ါပသုတ္္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc02/014%20Mahasi-Mingun-SatHtaThinGarYaNar%20KhallMaDutTaThout.mp3">
								၁၄။ ေခါမဒူတသုတ္<br>
								</a>
								<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One"><br>
								</font><font size="5" face="Times New Roman">MP3 
								Disc 3<br>
								</font><font size="4" face="Zawgyi-One"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/001%20Mahasi-Mingun-SatHtaThinGarYaNar%20EaByarKaTaThout.mp3">
								၁။ အဗ်ာကတသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/002%20Mahasi-Mingun-SatHtaThinGarYaNar%20WetGaLeatThout.mp3">
								၂။ ၀ိဂၢိလသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/003%20Mahasi-Mingun-SatHtaThinGarYaNar%20ThuMaNaThoutTan.mp3">
								၃။ သုမနသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/004%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaelLeatKarWeatMoatTeatyaTaNarThout.mp3">
								၄။ မလႅိကာ၊ ၀ိမုတၲိရတနာသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/005%20Mahasi-Mingun-SatHtaThinGarYaNar%20AhNateSaThoutMhaThanMarDateHteetThout.mp3">
								၅။ အနိစၥသုတ္မွ သမၼာဒိ႒ိသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/006%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaTheatTaNarKhanThout.mp3">
								၆။ မဟာသိတနခံ သုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/007%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaDarNaThoutMaHaPaYateNiteBarThout.mp3">
								၇။ မဟာပဒါနသုတ္၊ မဟာပရိနိဗၺာသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/008%20Mahasi-Mingun-SatHtaThinGarYaNar%20EaBaYaKuMarYaThout.mp3">
								၈။ အဘရကုမာရသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/009%20Mahasi-Mingun-SatHtaThinGarYaNar%20GarYaWaThoutBarYaDowarZaThout.mp3">
								၉။ ဂါရ၀သုတ္၊ ဘာရဒြါဇသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/010%20Mahasi-Mingun-SatHtaThinGarYaNar%20KhanDarYaMikeThout.mp3">
								၁၀။ ခႏၶာယမိုက္သုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/011%20Mahasi-Mingun-SatHtaThinGarYaNar%20PainNaThout.mp3">
								၁၁။ ပိ႑သုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/012%20Mahasi-Mingun-SatHtaThinGarYaNar%20DutWarYaPetTaThoutDeeGarYaThout.mp3">
								၁၂။ ဒု၀ါယပတၲသုတ္၊ ဒီဂါရသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/013%20Mahasi-Mingun-SatHtaThinGarYaNar%20BarThaPenNeatTaThoutDarYokeKhanDorePaMaThout.mp3">
								၁၃။ ဗာသ၊ ပ႑ိတသုတ္၊ ဒါရုကၡေႏၶာပမသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/014%20Mahasi-Mingun-SatHtaThinGarYaNar%20DarTuWeatBinGaThout.mp3">
								၁၄။ ဓာတု၀ိဘဂၤသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc03/015%20Mahasi-Mingun-SatHtaThinGarYaNar%20ErLarWaKaThoutThoatPaBuddhaThout.mp3">
								၁၅။ အာဠာ၀ကသုတ္၊ သုပၸဗုဒၶသုတ္<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One"><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One"><br>
								</font><font size="5" face="Times New Roman">MP3 
								Disc 4<br>
								</font><font size="4" face="Zawgyi-One"><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/001%20Mahasi-Mingun-SatHtaThinGarYaNar%20AtBaHtaThoutYarHootLarThanYoke.mp3">
								၁။ အမၺဋသုတ္၊ ရာဟုလာသံယုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/002%20Mahasi-Mingun-SatHtaThinGarYaNar%20YaMaKaThoutMaHaSoneDaThout.mp3">
								၂။ ယမကသုတ္၊ မဟာစုႏၵသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/003%20Mahasi-Mingun-SatHtaThinGarYaNar%20DhammaThinGaNiThout.mp3">
								၃။ ဓမၼသဂၤဏီသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/004%20Mahasi-Mingun-SatHtaThinGarYaNar%20BateKhuNiWeatBin.mp3">
								၄။ ဘိကၡဳနီ၀ိဘင္း<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/005%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaThaTeatPaHtarNaThoutParYarTheatYarZaThout.mp3">
								၅။ မဟာသတိပ႒ာနသုတ္၊ ပါရာသိရာဇသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/006%20Mahasi-Mingun-SatHtaThinGarYaNar%20AtTeatPaDoreMaPaThoutDarYokeKhanDoreMaPaThout.mp3">
								၆။ အတၲိပေဒါမပသုတ္၊ ဒါရုကၡေႏၶာမပသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/007%20Mahasi-Mingun-SatHtaThinGarYaNar%20SueLathitSaKaThoutTanMaHaThitSaKaThoutTan.mp3">
								၇။ စူဠသစၥကသုတၲန္၊ မဟာသစၥကသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/008%20Mahasi-Mingun-SatHtaThinGarYaNar%20SinKeeThoutTan.mp3">
								၈။ စကႌသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/009%20Mahasi-Mingun-SatHtaThinGarYaNar%20YaMikeParLeatTaw.mp3">
								၉။ ယမိုက္ပါဠိေတာ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/010%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaPaYateNibbanNaThoutTanMaHaPaDayThaLayPar.mp3">
								၁၀။ မဟာပရိနိဗၺာန္နသုတၲန္၊ မဟာပေဒသ (၄)ပါး<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/011%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaDhammaParLaZat.mp3">
								၁၁။ မဟာဓမၼပါလဇတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/012%20Mahasi-Mingun-SatHtaThinGarYaNar%20ThawNaKaZat.mp3">
								၁၂။ ေသာနကဇတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/013%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaThiHaNarDaZat.mp3">
								၁၃။ မဟာသီဟနာဒဇာတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc04/014%20Mahasi-Mingun-SatHtaThinGarYaNar%20ErNanDaThayHteePyinSaOopYaThaKarWouldHtooLairThaMarWouldHtoo.mp3">
								၁၄။ အာနႏၵေသ႒ီ၊ ပဥၥဥယသကာ၀တၳ၊ လယ္သမား၀တၳဳ<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3 Disc 5<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/001%20Mahasi-Mingun-SatHtaThinGarYaNar%20WeatTharKharWouldHtooThamMaHootTheatLarDeatBateKhuWouldHtoo.mp3">
								၁။ ၀ိသာခါ၀တၳဳ၊ သမၼဟုသိလာဒိ ဘိကၡဳ၀တၳဳ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/002%20Mahasi-Mingun-SatHtaThinGarYaNar%20KuLuPaKaThamDhammaPaRateYouPaKaThout.mp3">
								၂။ ကုလူပကသဒၶမၼပဋိရူပကသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/003%20Mahasi-Mingun-SatHtaThinGarYaNar%20MaHaThiYaNarDaThoutTanTeatTaYaThetDeatYaThoutTan.mp3">
								၃။ မဟာသီယနာဒသုတၲန္၊ တိတယသဒိၶယသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/004%20Mahasi-Mingun-SatHtaThinGarYaNar%20.mp3">
								၄။ ရဟန္းငါးရာ၀တၳဳ၊ ပတိပူဇိကာ၀တၳဳ၊ 
								ထင္းခုတ္သမား၀တၳဳ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/005%20Mahasi-Mingun-SatHtaThinGarYaNar%20YaHanNharYarWouldHtooPaTeatPullZeatKarWouldHtooHtinnKhoutThaMarWouldHtoo.mp3">
								၅။ ဓမၼသန၀တၳဳ၊ တိႆသာမေဏ၊ ပဥၥဥပႆကာ၀တၳဳ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/006%20Mahasi-Mingun-SatHtaThinGarYaNar%20DhammaThaWaNaWouldHtooTakeThaTharMaNayPyinSaOopPaThaKarWouldHtoo.mp3">
								၆။ ဒုကၠဋ္အာပါတ္ေတာ္၀ိနည္းေတာ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/007%20Mahasi-Mingun-SatHtaThinGarYaNar%20DoteKhaHteetErPetWeatNyeeTaw.mp3">
								၇။ နိသိ၀ိနည္းေတာ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/008%20Mahasi-Mingun-SatHtaThinGarYaNar%20NeatTheatWeatNyeeTaw.mp3">
								၈။ ယမကသုတ္၊ ရွင္နာဂီယသုတ္၊ ဣနသုတ္၊ မဟာစုႏၵသုတ္၊ 
								ေဖာ္သဠိယသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/009%20Mahasi-Mingun-SatHtaThinGarYaNar%20YaMaKaThoutShinNarGeeYaThoutKoneNaThoutMaHaSoneDaThout.mp3">
								၉။ ေခါမဒုႆသုတ္၊ ၀ဂႌသုတ္၊ အာနႏၵသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/010%20Mahasi-Mingun-SatHtaThinGarYaNar%20KhallMaDoteThaThoutWinGeeThoutErNanDarThout.mp3">
								၁၀။ ဧကပုတၲသုတၲံ၊ ဧကသီသုတ္၊ ရာဟုလာသုတ္၊ အတၲိသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/011%20Mahasi-Mingun-SatHtaThinGarYaNar%20AieKaPokeTaThoutTanAieKaThiThoutYarHootLarThoutAtTeatThout.mp3">
								၁၁။ ပါတရာသိ(၀ါ) အရိယာပရိေယသန၊ 
								စူဠအတၲိကေသာပမာသုတၲန္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/012%20Mahasi-Mingun-SatHtaThinGarYaNar%20ParTaYarTheatWarAhYeatYarPaReatYaeThaNaSueLaAtTeatKaThawPaMarThoutTan.mp3">
								၁၂။ တတိယၾသ၀ါဒသုတ္၊ ဘဒၵမပတိရူပသုတ္၊ ေမာလိကၤာ 
								ဖဂၢဳဏရဟန္း<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc05/013%20Mahasi-Mingun-SatHtaThinGarYaNar%20TaKeatYaAllWarDaThoutBadDaMaPaTeatYouPaThoutMallLainKarPhaKhuNaYaHan.mp3">
								၁၃။&nbsp; ----------------------- </a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One"><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Times New Roman">MP3 Disc 6<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc06/001%20Mahasi-Mingun-SatHtaThinGarYaNar%20WetMaLayWouldHtooAhNyaTaYaPullYaThaThout.mp3">
								၁။ ၀က္မေလး၀တၳဳ၊ အညတရပူရသသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc06/002%20Mahasi-Mingun-SatHtaThinGarYaNar%20NaKuLaPeeTuThoutAhNateSaLatKhaNaThoutErNeatThoutNaWaThoutMeatHtaKaThout.mp3">
								၂။ နကုလပီတုသုတ္၊ အနိစၥလကၡဏသုတ္၊ အာနိသုတ္၊ 
								န၀သုတ္၊ မိဠကသုတ္<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
MahasiSayadawUSobhanaMahathera/SatHtaThinGarYaNar/MP3Disc06/003%20Mahasi-Mingun-SatHtaThinGarYaNar%20RaHtaWeatNateTaThoutNaWarYaThoutGanDaYaHtaPokeGaLaSaHtoutHtaThout.mp3">
								၃။ ရ႒၀ိနိတၲသုတ္၊ န၀ါယသုတ္၊ ဂႏၵရထပုဂၢလစတုတၳသုတ္<br>
&nbsp;</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p></div>
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
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            print('{}.mp3|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.mp3|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())
            
            count += 1        
    
