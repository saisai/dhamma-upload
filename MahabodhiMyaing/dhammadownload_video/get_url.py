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
	<span style=""><font size="6" face="Times New Roman" color="#800080">
	Maha Bodhi Myaing Sayadaw&nbsp;
</font>
<o:p></o:p>
</span></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 596px; top: 4px;" id="layer23">
	<img src="images/Mahabodhi-Myaing-Sayadaw.gif" width="118" height="168" border="0"></div>
	
	
	






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









</font><div style="position: absolute; width: 1090px; height: 3628px; z-index: 21; left: 219px; top: 154px" id="layer24" font="" face="Zawgyi-One"><font face="Zawgyi-One">
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
          <p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
          &nbsp;</p>
          <p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
          <font size="5">Venerable Maha Bodhi Myaing Sayadaw </font></p>
          <font size="5">U Nyeyadhammatharmiaha</font></font><p></p>
          <p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
          <font size="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          </font></p>
          <p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
          <font size="4">သတိတစ္လံုး၊ လက္ကိုင္သံုး၊ ခ်ဳပ္ဆံုးနိဗၺာန္ဝင္</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
          <font size="4">ေက်းဇူးေတာ္ရွင္ </font></p>
          <p style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
			<font size="5" face="Zawgyi-One">မဟာေဗာဓိၿမိဳင္ ဆရာေတာ္ <br>
			ဝနဝါသီ အရွင္ ေဉယ်ဓမၼသာမိမေထရ္<br>
			</font><font size="4" face="Zawgyi-One">ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								**********************************</p>
			<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk Video</font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b>&nbsp;</b></p>
          <p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><b>
			<font size="5">DVD Disc 1</font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-01/001-MahaBodhiMyaingSayadaw-DVD1-WayThawLairNyeeShweKhaYee.mp4">၁။ ေဝးေသာ္လည္းနီး ေရႊ ခရီး</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-01/002-MahaBodhiMyaingSayadaw-DVD1-KaungSaitSoSait.mp4">၂။ ေကာင္းစိတ္ ဆိုးစိတ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-01/003-MahaBodhiMyaingSayadaw-DVD1-NyarParThiLaSauntHtaingKya.mp4">၃။ ငါးပါးသီလ ေစာင့္ထိမ္းၾက</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-01/004-MahaBodhiMyaingSayadaw-DVD1-KanBallZaTayarTaw.mp4">၄။ ကေမာၻဇ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><b>
			<font size="5">DVD Disc 2</font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-02/001-MahaBodhiMyaingSayadaw-DVD2-NyinKoNyanPhyintShinYouPar.mp4">၁။ ဉာဥ္ကို ဉာဏ္ျဖင့္ ယွဥ္ယူပါ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-02/002-MahabodhiMyaing-DVD2-ThuTawKongMuWarDa5Chat.mp4">၂။ သူေတာ္ေကာင္းမူဝါဒ (၅) ခ်က္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-02/003-MahaBodhiMyaingSayadaw-DVD2-DoteKhaSoneYarLookLanShar.mp4">၃။ ဒုကၡဆုံးရာ လြတ္လမ္းရွာ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-02/004-MahaBodhiMyaingSayadaw-DVD2-MaKawelKhinKaKhawelNhitPar.mp4">၄။ မကြဲခင္က ခြဲႏွင့္ပါ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-02/005-MahaBodhiMyaingSayadaw-DVD2-AhPalLayParPlazaGyiHtairMharNayKyaOwnMharLair.mp4">၅။ အပါယ္ေလးပါး ပလာဇာႀကီးထဲမွာ ေနၾကဦးမွာလား</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><b>
			<font size="5">DVD Disc 3</font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-03/001-MahaBodhiMyaingSayadaw-DVD3-ThaTeatTaLoneLetKaingThone.mp4">၁။ သတိတလုံး လက္ကိုင္သုံး</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-03/002-MahaBodhiMyaingSayadaw-DVD3-AhChainKaungAhYaKaungAhKharKaung.mp4">၂။ အခ်ိန္ေကာင္း အရေကာင္း အခါေကာင္း</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-03/003-MahaBodhiMyaingSayadaw-DVD3-ThuTawKaungOakSarKhuNhitPhyar.mp4">၃။ သူေတာ္ေကာင္းဥစၥာ (၇)ျဖာ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-03/004-MahaBodhiMyaingSayadaw-DVD3-YoneKyiKoeSarErrNharPar.mp4">၄။ ယုံၾကည္ကိုးစား အား(၅)ပါး</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-03/005-MahaBodhiMyaingSayadaw-DVD3-AhLoutPayTayarTaw.mp4">၅။ အလုပ္ေပးတရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><b>
			<font size="5">DVD Disc 4</font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-04/001-MahaBodhiMyaingSayadaw-DVD4-LuBawaAhThetSetSayarKoSauntBarwanarLayMyo.mp4">၁။ လူအသက္ ဆက္စရာ ကိုယ္ေစာင့္ဘာဝနာ (၄)မ်ိဳး</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-04/002-MahaBodhiMyaingSayadaw-DVD4-TaBawaSoTaBawaKhaYeeYorkAung.mp4">၂။ တစ္ဘဝဆို တစ္ဘဝ ခရီးေရာက္ေအာင္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-04/003-MahaBodhiMyaingSayadaw-DVD4-AhChainMhanHlaingMhanPhoatAhYaeKyee.mp4">၃။ အခ်န္မွန္ လိႈင္းမွန္ဖို႕ အေရးႀကီး</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-04/004-MahaBodhiMyaingSayadaw-DVD4-SeinTaungPawMharKyaukKaungShar.mp4">၄။ စိန္ေတာင္ေပၚမွာ ေက်ာက္ေကာင္းရွာ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-04/005-MahaBodhiMyaingSayadaw-DVD4-DarNaPyuYarNyanKhuPar.mp4">၅။ ဒါနျပဳရာ ဉာဏ္ကူပါ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">

<font face="Zawgyi-One">






								****dhamma talks uploaded and published on 
								5 Feb 2011****</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><b>
			<font size="5">DVD Disc 5</font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-05/001-MahaBodhiMyaingSayadaw-DVD5.mp4">၁။ ဘာသာေသြးကို ႏႈိးေဆာ္ပါ (ကေလးတရား)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-05/002-MahaBodhiMyaingSayadaw-DVD5.mp4">၂။ ေကာက္ပင္ရိတ္လွီး တရားနည္း</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-05/003-MahaBodhiMyaingSayadaw-DVD5.mp4">၃။ ေျခလက္ႏွစ္စုံ အကုန္ပါမွ တရားရ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-05/004-MahaBodhiMyaingSayadaw-DVD5.mp4">၄။ တစ္ကယ္ေၾကာက္ရင္ အဟုတ္လုပ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-05/005-MahaBodhiMyaingSayadaw-DVD5.mp4">၅။ အထက္ဆန္မွာလား ေအာက္ျပန္မွာလား</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">

<font face="Zawgyi-One">






								****dhamma talks uploaded and published on 
								17 Nov 2011****</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><b>
			<font size="5">DVD Disc 6</font></b></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-06/01-MahaBodhiMyaingSayadaw-DVD6.mp4">၁။ အေနတတ္မွ အေသျမတ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-06/02-MahaBodhiMyaingSayadaw-DVD6.mp4">၂။ အယုံကဲမွ အရဲပိုမည္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-06/03-MahaBodhiMyaingSayadaw-DVD6.mp4">၃။ ဘာသာေသြးကို ႏႈိးေဆာ္ပါ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-06/04-MahaBodhiMyaingSayadaw-DVD6.mp4">၄။ ၾသကာသရွင္းတမ္း</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-06/05-MahaBodhiMyaingSayadaw-DVD6.mp4">၅။ ဝေလးလုံးကို အသုံးခ်ပါ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
‘သံဃာဂုဏ္ ယံုၾကည္တတ္ေစဘို႔’</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
အမွတ္စဥ္ (၇) </font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-07-2/01-MahaBodhiMyaingSayadaw-DVD07.mp4">
၁။ အိပ္ေနသူႏွင့္ သြားေနသူ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-07-2/02-MahaBodhiMyaingSayadaw-DVD07.mp4">
၂။ အျပစ္ခ်ည္း ၾကည့္မေနၾကပါနဲ႔</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-07-2/03-MahaBodhiMyaingSayadaw-DVD07.mp4">
၃။ ဆရာေတာ္အရွင္ဆႏၵာဓိကအား ၾသဝါဒမိန္႔ၾကားေတာ္မူျခင္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-07-2/04-MahaBodhiMyaingSayadaw-DVD07.mp4">
၄။ အစြန္းႏွစ္ဖက္ လြတ္ေသာလမ္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-07-2/05-MahaBodhiMyaingSayadaw-DVD07.mp4">
၅။ သံဃာ့ဂုဏ္ ယံုၾကည္တတ္ေစဘို႔</a><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
‘ခ်မ္းသာအစစ္ကိုရွာေဖြျခင္း’</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
အမွတ္စဥ္ (၈)</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-08/01-MahaBodhiMyaingSayadaw-DVD08-Chan-Thar-A-Sit-Ko-Shar-Pway-Chin-.mp4">
၁။ အမွတ္တစ္ခု ေန႔စဥ္ျပဳ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-08/02-MahaBodhiMyaingSayadaw-DVD08-Mg-Gin-Boung.mp4">
၂။ ခ်မ္းသာအစစ္ကို ရွာေဖြျခင္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-08/03-MahaBodhiMyaingSayadaw-DVD08-Myaing-Taw-Ma-Har.mp4">
၃။ မဂၢင္ေဖာင္ျပင္ ခရီးႏွင္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-08/04-MahaBodhiMyaingSayadaw-DVD08-Ta-Kal-Lote-Yin-A-Hote-Ya.mp4">
၄။ တစ္ကယ္လုပ္ရင္ အဟုတ္ရ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-08/05-MahaBodhiMyaingSayadaw-DVD08-Thin-Gyan-So-Dar-Pyaung-Lal-Chin.mp4">
၅။ သႀကၤန္ဆိုတာ ကူးေျပာင္းျခင္း</a><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
‘လူျဖစ္ေအာင္ႀကိဳးစားပါ’<br>
<br>
အမွတ္စဥ္ (၉)</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-09/01-MahaBodhiMyaingSayadaw-DVD09.mp4">
၁။ မိုးမိတ္ေရႊျမင္တင္ေတာင္ေတာ္မွ မပဒါန္းလႈိုင္ဂူသို႔ 
ေျပာင္းေရႊ႕သီတင္းသံုးေတာ္မူစဥ္ မတ္တမ္းပံုရိပ္မ်ား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-09/02-MahaBodhiMyaingSayadaw-DVD09.mp4">
၂။ ႏွစ္ဦးမဂၤလာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-09/03-MahaBodhiMyaingSayadaw-DVD09.mp4">
၃။ လက္ေတြ႕က်င့္စရာ ဝိပႆနာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-09/04-MahaBodhiMyaingSayadaw-DVD09.mp4">
၄။ သရဏဂံု ဥပုသ္ေတာ္ႏွင့္ သီလရွင္းတမ္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-09/05-MahaBodhiMyaingSayadaw-DVD09.mp4">
၅။ လူျဖစ္ေအာင္ ႀကိဳးစားပါ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-09/06-MahaBodhiMyaingSayadaw-DVD09.mp4">
၆။ ပဲေလွာ္ဝါးရင္း လွည္းစီးပါ</a><br>
<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">

<font face="Zawgyi-One">






								****dhamma talks uploaded and published on 
								23 March 2013****</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">အမွတ္စဥ္ (၁၀)<br>
&nbsp;</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-10/01-MahaBodhiMyaingSayadaw-DVD10.mp4">
၁။ မိုးမိတ္ေရႊျမင္တင္ေတာင္ေတာ္မွ မပဒါန္းလႈိင္ဂူသို႕ ႂကြခ်ီေတာ္မူျခင္းႏွင့္ 
တရားေဟာျခင္း</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-10/02-MahaBodhiMyaingSayadaw-DVD10.mp4">
၂။ ဆရာေတာ္ အရွင္ေသာမအား ၾသဝါဒ မိန္႕ၾကားေတာ္မူျခင္း</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-10/03-MahaBodhiMyaingSayadaw-DVD10.mp4">
၃။ အဓိပၸါယ္ရွိေသာေန႕ (မိုးမိတ္) (အရွင္ေသာမ)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-10/04-MahaBodhiMyaingSayadaw-DVD10.mp4">
၄။ ဆရာေတာ္ အရွင္ဇဝနမွ သြားေရာက္ ဖူးေမွ်ာ္ ၾသဝါဒ ခံယူျခင္း</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Maha-BodhiMyaing-Sayadaw/DVD-10/05-MahaBodhiMyaingSayadaw-DVD10.mp4">
၅။ သင္လူတေယာက္ျဖစ္ၿပီလား (မိုးမိတ္) (အရွင္ဇဝန)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">အမွတ္စဥ္ (၁၁)</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">၁။ 
ေရႊဘိုခရိုင္၊ ကန္႕ဘလူၿမိဳ႕နယ္ ဆရာေတာ္ဘုရားႀကီး သီတင္းသုံးေတာ္မူေသာ ေဉယ်ဓမ္ေတာရ 
ေက်ာင္းလႊတ္ပြဲေတာ္ ေဟာၾကားခ်ီးျမွင့္ေတာ္မူေသာ "ပါရမီထိုက္ေသာဒါန" (၁၇-၇-၂၀၁၃)</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">၂။ 
မဟာေဗာဓိၿမိဳင္ဆရာေတာ္ မဟာၿမိဳင္သာသနာျပဳမွတ္တမ္း၏ "ရဟန္းျဖစ္ရေသာဒုကၡ"</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left"><font size="4">၃။ 
ဝိပႆနာဆိုင္ရာ အေမးအေျဖ (၂၈-၄-၂၀၁၁)</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
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
    
