from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 
<!-- Start dhammadownload menu top and side bar -->

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font size="6" color="#800080">သစၥာေရႊစည္ဆရာေတာ္ အရွင္ဥတၱမ</font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 542px; top: 13px;" id="layer23">
	<img src="images/ThitsarShweSi-Sayadaw-AshinOaktama.gif" width="147" height="178" border="0"></div>
	






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









	
<div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 222px; top: 162px" id="layer24" font="" face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									Thitsar ShweSi Sayadaw</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									Ashin Oaktama</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4">သစၥာေရႊစည္ဆရာေတာ္<br>
								</font><font size="5">အရွင္ဥတၱမ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4">(စစ္ကိုင္ မင္းဝံေတာင္တန္း)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4">ဖုန္း။ ၀၉-၂၀၃၁၀၅၁ ။ ၀၉-၇၃၅၀၂၁၅၀</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									**********************************</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									သစၥာေရႊစည္ဆရာေတာ္ အရွင္ဥတၱမ၏ 
									ကိုယ္ေရးမွတ္တမ္း</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									စစ္ကိုင္းတိုင္းေဒသၾကီး၊ တန္ ့ဆည္ျမိဳ ့နယ္၊ 
									ငါးႏုေခ်ာင္းအုပ္စု၊ ငါးႏုေခ်ာင္းရြာ၌ 
									ခမည္းေတာ္ၾကီး ဦးဘေသာင္+မယ္ေတာ္ၾကီး 
									ေဒၚသိန္းၾကြယ္တို ့မွ ၁၃၃၃ ခု၊ 
									ေတာ္သလင္းလျပည့္ေက်ာ္ (၈)ရက္ တနဂၤေႏြေန ့တြင္ 
									ဖြားျမင္သည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၄၇ ခုႏွစ္ ကဆုန္လတြင္ ရွင္သာမေဏျပဳသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၄၈ ခုႏွစ္တြင္ မူလတန္း၊ ၁၃၄၉ ခုႏွစ္တြင္ 
									ပထမငယ္တန္း၊ ၁၃၅၀ ခုႏွစ္တြင္ ပထမလတ္တန္း၊ ၁၃၅၁ 
									ခုႏွစ္တြင္ ပထမၾကီးတန္းတို ့ကို ေအာင္ျမင္သည္။ </p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၅၂ ခုႏွစ္ နတ္ေတာ္လျပည့္ေက်ာ္ (၁၂) ရက္ေန 
									့တြင္ မႏၱေလးတိုင္းေဒသၾကီး ျမစ္သားျမိဳ 
									့မင္းေက်ာင္းစာသင္တိုက္၌ ဆရာေတာ္ ဦးေဝဠဳရိယ 
									ကို ဥပဇၩယ္ျပဳျပီး အရွင္ဥာဏသာမိ 
									(ေအာင္ပန္းက်မ္းျပဳ) ၏ အႏုသာသန 
									ျပဳမွဳကိုခံယူျပီးလွ်င္ ရဟန္းအျဖစ္သို 
									့ေရာက္သည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၆၄ ခုႏွစ္ တပို ့တြဲလ (ရဟန္း(၁၂)ဝါအရ) တြင္ 
									က်န္းမာေရးမေကာင္းသျဖင့္ (၁)လခန္ 
									့ရွင္သာမေဏဘဝျဖင့္ ေနသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									၁၃၆၄ ခုႏွစ္ တေပါင္းလျပည့္ေက်ာ္ (၆) ရက္ေန 
									့တြင္ စစ္ကိုင္းတိုင္းေဒသၾကီး၊ တန္ ့ဆည္ျမိဳ 
									့နယ္၊ ငါးႏုေခ်ာင္းရြာ၊ စည္ရာန္ေက်ာင္းတိုက္၌ 
									ကံမ်ားေက်ာင္းဆရာေတာ္ဘုရားၾကီးကို 
									ဥပဇၩာယ္ျပဳျပီး ဒုတိယအၾကိမ္ ရဟန္းအျဖစ္သို 
									့ေရာက္သည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ယခုအခါ စစ္ကိုင္းျမိဳ ့ေရႊမင္းဝံရပ္ 
									သစၥာေရႊစည္ေက်ာင္းတိုက္၌ သီတင္းသံုးေနပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									သာသနာဝင္အမွတ္ မွာ ၅/ တဆန(သ)၀၀၀၄၆၂ ျဖစ္သည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									**********************************</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<b><font size="6">Dhamma Talk Video</font></b></p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">****dhamma talks 
uploaded&nbsp; on 31 March 2012 ****</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4"><br>
								<br>
								အမွတ္စဥ္(၁)</font></p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"အဆိုးဆုံးရန္သူ အေကာင္းဆုံးမိတ္ေဆြ"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-01/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD01-ASoeSoneYanThuHnintAKaungSoneMateSwe.mp4">
								၁။ အဆိုးဆုံးရန္သူ၊ အေကာင္းဆုံးမိတ္ေဆြ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-01/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD01-20091002-ThaTiHnintPyaw.mp4">
								၂။ သတိနဲ႕ေပ်ာ္၊ စိတ္ကိုေစာင့္၊ လြတ္ေအာင္ရုန္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-01/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD01-20100321-BaHuOoPaKarRaThodTan.mp4">
								၃။ ဗဟုဥပကာရသုတၱန္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-01/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD01-20100810-ALweMetYinAKetKyoneMal.mp4">
								၄။ အလြယ္မက္ရင္ အခက္ႀကဳံမယ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-01/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD01-20101221-ThuTawKaungToYeThaBawHtar.mp4">
								၅။ သူေတာ္ေကာင္းတို႕ရဲ့ သေဘာထား</a><br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<br>
								အမွတ္စဥ္(၂)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ဘုရားေပးေသာ ဥပမာမ်ား"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-02/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD02-20101218-ThuAKyaungKoAKyaung.mp4">
								၁။ သူ႕အေၾကာင္း ကိုယ့္အေၾကာင္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-02/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD02-20091003-ShiHpoHtetThiPhoKaAYayKyiThe.mp4">
								၂။ ရွိဖို႕ထက္ သိဖို႕က အေရးၾကီးသည္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-02/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD02-20100206-ThiHaNarDaThodTan.mp4">
								၃။ သီဟနာဒ သုတၱန္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-02/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD02-20091030-BayarPayThawOoPaMarMyar.mp4">
								၄။ ဘုရားေပးေသာ ဥပမာမ်ား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-02/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD02-20100319-ThuDathaNaThodTan.mp4">
								၅။ သုဒႆ သုတၱန္</a><br>
								<br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၃)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ရတနာထိုက္ေသာ စကား(၄)ခြန္း"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-03/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD03.mp4">
								၁။ ရတနာထိုက္ေသာ စကား(၄)ခြန္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-03/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD03.mp4">
								၂။ တန္ဘိုးရွိတဲ့လူ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-03/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD03.mp4">
								၃။ ခႏၶာေျမအိုး ကုသိုလ္ေရႊအိုး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-03/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD03.mp4">
								၄။ အသိနဲ႕ေနတာ ေကာင္းတယ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-03/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD03.mp4">
								၅။ ဥပမာ(၉)မ်ိဳး</a><br>
								<br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<br>
								အမွတ္စဥ္(၄)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ေလာဘသေဘာႏွင့္ ေကာင္းမႈအက်ိဳး"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-04/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD04.mp4">
								၁။ ဝိ႒ိသုတၱန္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-04/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD04.mp4">
								၂။ ေလာဘသေဘာႏွင့္ ေကာင္းမႈအက်ိဳး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-04/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD04.mp4">
								၃။ အားကိုးရာလား ရန္သူလား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-04/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD04.mp4">
								၄။ ဒီဖက္ကမ္းႏွင့္ ဟိုဖက္ကမ္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-04/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD04.mp4">
								၅။ ယဥ္ေက်းေသာစိတ္</a><br>
								<br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၅)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ရဟန္းပ်င္းႏွင့္ ရြဲကုန္သည္"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-05/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD05.mp4">
								၁။ ဆိုးသည္ျဖစ္ေစ၊ ေကာင္းသည္ျဖစ္ေစ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-05/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD05.mp4">
								၂။ နိဗၺာန္ခရီးႏွင့္ အတားအဆီးမ်ား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-05/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD05.mp4">
								၃။ ရဟန္းပ်င္းႏွင့္ ရြဲကုန္သည္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-05/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD05.mp4">
								၄။ သန္႕ရွင္းေသာစိတ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-05/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD05.mp4">
								၅။ သုခ(၁၂)ပါး</a><br>
								<br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<br>
								အမွတ္စဥ္(၆)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ပါရမီ ဆယ္ပါး"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-06/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD06.mp4">
								၁။ ပါရမီ ဆယ္ပါး(၁)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-06/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD06.mp4">၂။ ပါရမီ ဆယ္ပါး(၂)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-06/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD06.mp4">၃။ ပါရမီ ဆယ္ပါး(၃)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-06/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD06.mp4">၄။ ပါရမီ ဆယ္ပါး(၄)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-06/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD06.mp4">၅။ ပါရမီ ဆယ္ပါး(၅)</a><br>
								<br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								အမွတ္စဥ္(၇)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ေနာင္တေဝး၍ ေအးပါေစ"<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-07/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD07.mp4">
								၁။ စကားတို႕၏ အစြမ္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-07/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD07.mp4">
								၂။ စိတ္တို႕၏ အစြမ္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-07/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD07.mp4">
								၃။ ဧည္႕သည္ႏွင့္တူေသာ အရာမ်ား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-07/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD07.mp4">
								၄။ ေနာင္တေဝး၍ ေအးပါေစ</a><br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၈)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"စြန္႕ႏိုင္သေလာက္ ခ်မ္းတာမည္"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-08/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD08.mp4">
								၁။ စြန္႕ႏိုင္သေလာက္ ခ်မ္းသာမည္ (ေလာဘ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-08/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD08.mp4">
								၂။ ရန္သူ႕အၾကိဳက္ လိုက္ၾကမွာလား (ေဒါသ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-08/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD08.mp4">
								၃။ ေခါင္းေဆာင္ၾကီး ႏွစ္ဦး (ေမာဟ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-08/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD08.mp4">
								၄။ မျငိမ္းခ်မ္းတာ ဘာေၾကာင့္လဲ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-08/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD08.mp4">
								၅။ ေကာင္းတာေတြထက္ ေကာင္းတဲ့အရာ</a><br>
								<br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၉)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ျမတ္ဘုရား၏ စကားသုံးခြန္း"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-09/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD09.mp4">
								၁။ စိတ္ေကာင္းထားမွ ခ်မ္းသာရ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-09/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD09.mp4">
								၂။ စိတ္ထားလွမွ ျမတ္ႏိုးၾကသည္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-09/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD09.mp4">
								၃။ ေစာင့္စည္းျခင္းသည္ ေကာင္း၏</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-09/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD09.mp4">
								၄။ ျမတ္ဘုရား၏ စကားသုံးခြန္း</a><br>
								<br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<br>
								အမွတ္စဥ္(၁၀)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ခ်မ္းသာခ်င္လွ်င္ စိတ္ကိုျပင္"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-10/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD10.mp4">
								၁။ ေကာင္းေသာည</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-10/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD10.mp4">
								၂။ ဗကျဗဟၼာ၏ အတိတ္ဇာတ္လမ္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-10/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD10.mp4">
								၃။ ခ်မ္းသာခ်င္လွ်င္ စိတ္ကိုျပင္</a><br>
								<br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၁၁)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"မျငိမ္းခ်မ္းတာ ဘာေၾကာင့္လဲ"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-11/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD11.mp4">
								၁။ အနာထပိဏ္နဲ႕ ကံတရား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-11/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD11.mp4">
								၂။ မျငိမ္းခ်မ္းတာ ဘာေၾကာင့္လဲ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-11/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD11.mp4">
								၃။ ရွင္ရာဟုလာ</a><br>
								<br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၁၂)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								"ျမတ္ဗုဒၶဝါဒႏွင့္ ခ်ီးမြမ္းျခင္းႏွစ္မ်ိဳး"<br>
								<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-12/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD12.mp4">
								၁။ ေလးပါးခ်မ္းသာ ရေအာင္ရွာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-12/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD12.mp4">
								၂။ ေကာင္းတာေတြထက္ ေကာင္းတဲ့အရာ</a><br>
								၃။ ျမတ္ဗုဒၶဝါဒႏွင့္ ခ်ီးမြမ္းျခင္းႏွစ္မ်ိဳး<br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၁၃)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-13/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD13.MP4">
								၁။ ျမတ္ဗုဒၶႏွင္႔ ခ်ီးမြမ္းျခင္းႏွစ္မ်ိဳး&nbsp; 
								(၁၅.၁၂.၂၀၁၁-အလံု)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-13/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD13.MP4">
								၂။ သတိပဌာန္ဂုဏ္ရည္&nbsp; (၁၉.၃.၂၀၁၂-မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-13/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD13.mp4">
								၃။ ၾကီးပြားေၾကာင္းတရား(၇)ပါး 
								(၂၀.၃.၂၀၁၂-မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-13/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD13.mp4">
								၄။ အရွင္စူဠပန္ (၂၁.၃.၂၀၁၂-မ/ဥကၠလာ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-13/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD13.mp4">
								၅။ ညီညြတ္မွခ်မ္းသာမည္&nbsp; (၂၂.၃.၂၀၁၂-မ/ဥကၠလာ)</a><br>
								<br>
								<br>
								<br>
								<br>
								အမွတ္စဥ္(၁၄)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-14/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD14.mp4">
								၁။ အေမးေလးေထြ အေျဖေလးပါး&nbsp; 
								(၆.၄.၂၀၁၂-သဃၤန္းကြ်န္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-14/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD14.mp4">
								၂။ အဆိုးဆံုးရန္သူႏွင္႔ အေကာင္းဆံုးမိတ္ေဆြ(၁)&nbsp; 
								(၄.၂.၂၀၁၂-မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-14/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD14.mp4">
								၃။ အဆိုးဆံုးရန္သူႏွင္႔ အေကာင္းဆံုးမိတ္ေဆြ(၂) 
								(၈.၂.၂၀၁၂-တ/ဥကၠလာ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-14/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD14.mp4">
								၄။ အဆိုးဆံုးရန္သူႏွင္႔ အေကာင္းဆံုးမိတ္ေဆြ(၃) 
								(၂၃.၂.၂၀၁၂-ေထာက္ၾကန္႔)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-14/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD14.mp4">
								၅။ သူေတာ္ေကာင္းတို႔ရဲ႔သေဘာထား 
								(၃၁.၁.၂၀၁၁-ေတာင္ငူ)</a><br>
								<br>
								&nbsp;</font></p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left"><font size="4">****dhamma talks 
uploaded&nbsp; on 29 March 2013 ****</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္ (၁၅)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-15/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD15.mp4">၁။ အသိဥာဏ္၏ ဂုဏ္ေက်းဇူး
								(၂၈.၈.၂၀၁၂ - မိတၳီလာ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-15/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD15.mp4">၂။ ေလးပါးခ်မ္းသာ ရေအာင္ရွာ
								(၂၉.၈.၂၀၁၂ - သာစည္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-15/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD15.mp4">၃။ အေမးေလးေထြ အေၿဖေလးပါး
								(၃၀.၈.၂၀၁၂ - သာစည္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-15/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD15.mp4">၄။ တန္ဘိုးရွိတဲလူ (နာဂသုတၱန္)
								(၃၀.၈.၂၀၁၂ - သာစည္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-15/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD15.mp4">၅။ အရွင္ရဌပါလ
								(၂၅.၁၁.၂၀၁၁ - ေတာင္ဥကၠလာပ)</a><br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<br>
								အမွတ္စဥ္ (၁၆)<br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-16/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD16.mp4">၁။ ဓမၼစြမ္းရည္
								(၂၉.၇.၂၀၁၁ - မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-16/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD16.mp4">၂။ ခ်မ္းသာေၾကာင္းတရား (၁၂) ပါး
								(၂.၁၀.၂၀၁၁ - စစ္ကိုင္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-16/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD16.mp4">၃။ ေ၀လာမသုတၱန္
								(၅.၉.၂၀၁၁ - ဗဟန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-16/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD16.mp4">၄။ ဘုရားခ်ီးမႊမ္းခံထိုက္သူ
								(၂၂.၇.၂၀၁၂ - ေက်ာက္ဆည္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-16/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD16.mp4">၅။ သမုဒၵရာမ်ားကို ကူးခတ္ၿပီးသူ
								(၁၉.၈.၂၀၁၂ - လႈိင္)</a><br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<br>
								အမွတ္စဥ္ (၁၇)<br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-17/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD17.mp4">၁။ ဆြမ္းအႏုေမာဒနာ
								(၁၈.၁၀.၂၀၁၂ - ေက်ာက္ေၿမာင္း/တာေမြ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-17/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD17.mp4">၂။ အၿမတ္ဆံုး (၆) ပါး
								(၃၀.၉.၂၀၁၂ - ဗဟန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-17/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD17.mp4">၃။ ေလာကကို တင့္တယ္ေစသူမ်ား
								(၂၁.၁၀.၂၀၁၂ - ကမာရြတ္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-17/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD17.mp4">၄။ အေၿခအေနကို မေမ့ပါနဲ႕
								(၁.၁၁.၂၀၁၂ - သာေကတ)</a><br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<br>
								အမွတ္စဥ္ (၁၈)<br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-18/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD18.mp4">၁။ အခုေရာေနာင္ပါ ခ်မ္းသာေစဖို႔
								(၃၀.၁၁.၂၀၁၂ - မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-18/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD18.mp4">၂။ အေၿခအေနမွန္ကို မေမ့ပါနဲ႕
								(၃၀.၁၁.၂၀၁၂ - မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-18/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD18.mp4">၃။ အႏုသယ (သို႕) ေခ်ာင္းေနေသာ ရန္သူ
								(၃.၁၁.၂၀၁၂ - က်ိဳက္ထို)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-18/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD18.mp4">၄။ အဘိဏွသုတၱန္ (အၿမဲတမ္း)
								(၁၄.၅.၂၀၁၂ - ေက်ာက္ဆည္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-18/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD18.mp4">၅။ တန္ဖိုးရွိတဲ့ လူ
								(၂၈.၁၁.၂၀၁၂ - ေတာင္ဥကၠလာပ)</a><br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<br>
								အမွတ္စဥ္ (၂၀)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-20/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD20.mp4">၁။ ဘယ္လုိ တုန္႔ၿပန္မလဲ
								(၃.၁.၂၀၁၃ - ကမာရြတ္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-20/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD20.mp4">၂။ ေလးပါးခ်မ္းသာ ရေအာင္ရွာ
								(၇.၁.၂၀၁၃ - တာေမြ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-20/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD20.mp4">၃။ (အၿမတ္ဆံုး မဂၤလာ) အႏုေမာဒနာ
								(၁၁.၁.၂၀၁၃ - မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-20/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD20.mp4">၄။ လြန္ကဲေသာ တရားမ်ား
								(၉.၁၂.၂၀၁၂ - ေတာင္ငူ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-20/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD20.mp4">၅။ ေမဃိယသုတၱန္
								(၁၂.၈.၂၀၁၂ - ၿပင္ဦးလြင္)</a><br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၁)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-21/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD21.mp4">
								၁။ လႊ ဥပမာ 
								၂၆-၄-၂၀၁၃</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-21/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD21.mp4">
								၂။ ေစ်းသည္၂၇-၄-၂၀၁၃</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-21/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD21.mp4">
								၃။ သစၥာသိဖို ့အေရးၾကီးဆံုး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-21/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD21.mp4">
								၄။ သစၥာေလးပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၂)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-22/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD22-11-1-2013.mp4">၁။ ေဘးမၿဖစ္ေအာင္ေနပါ</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-22/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD22-13-1-2013.mp4">၂။ ဝိပလႅာသသုတၱန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-22/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD22-17-4-2013-DharNa.mp4">၃။ ဒါနအေၾကာင္း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-22/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD22-18-4-2013-Thela.mp4">၄။ သီလအေၾကာင္း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-22/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD22-19-4-2013-Barwanar.mp4">၅။ ဘာဝနာအေၾကာင္း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၃)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-23/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD23.mp4">၁။ မထူးဇာတ္ခင္းသူမ်ား</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-23/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD23.mp4">၂။ တစ္ခုေသာတရား၏ ဂုဏ္ေက်းဇူးမ်ား</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-23/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD23.mp4">၃။ ေဘးမၿဖစ္ေအာင္ေန</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၄)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-24/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD24.mp4">၁။ ေလာကဓံ</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-24/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD24.mp4">၂။ အၿမတ္ဆံုးေသာရွင္သန္ၿခင္း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-24/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD24.mp4">၃။ အၿမတ္ဆံုး (၄)ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၅)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-25/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD25-21-9-2013.mp4">၁။ တစ္ေၾကာင္းတည္းေသာလမ္း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-25/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD25-21-9-2013.mp4">၂။ ကာယာႏုပႆနာ သတိပဌာန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-25/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD25-21-9-2013.mp4">၃။ ေဝဒနာႏုပႆနာ သတိပဌာန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-25/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD25-21-9-2013.mp4">၄။ စိတၱာႏုပႆနာ သတိပဌာန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-25/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD25-21-9-2013.mp4">၅။ ဓမၼာႏုပႆနာ သတိပဌာန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၆)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">၁။ သတိပဌာန္ 
								တရား (၄) ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">၂။ သမၼပၸဒါန္ 
								တရား (၄) ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">၃။ ဣဒိၶပါဒ္ 
								(၄) ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">
								၄။ ဣေျႏၵ (၅) ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">၅။ ဗိုလ္ 
								(၅) ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/06-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">၆။ ေဗာဇၩင္ 
								(၇) ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-26/07-ThitsarShweSi-Sayadaw-AshinOaktama-DVD26.mp4">
								၇။ မဂၢင္ 
								(၈)ပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၇)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-27/DVD-27-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ ကံဏွာဇာတ္ (ေတာင္ညြန္႕ႀကီးဓမၼာရုံ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-27/DVD-27-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ အရိုးဆုံးႏွင့္ အေကာင္းဆုံး (ရန္ကုန္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-27/DVD-27-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ ျမင့္ျမတ္သူတို႕ အေတြၚ (မုံရြာ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၈)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-28/DVD-28-Title-001-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ ဘာကို ရွာေနတာလဲ</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-28/DVD-28-Title-002-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ အဆိုးဆုံးႏွင့္ အေကာင္းဆုံး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-28/DVD-28-Title-003-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ နႏၵေကာဝါဒ သုတၱန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-28/DVD-28-Title-004-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၄။ ေဒါသပါယ္ေၾကာင္း နည္းလမ္းေကာင္း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-28/DVD-28-Title-005-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၅။ ရွင္ရ႒ပါလသုတၱန္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၂၉)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-29/DVD-29-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama-2-1-2014.mp4">
								၁။ စိတ္သာလွ်င္ ပဓါန (၂-၁-၂၀၁၄ - ေတာင္ဥကၠလာပ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-29/DVD-29-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama-5-1-2014.mp4">
								၂။ အႏွစ္သုံးပါး (၅-၁-၂၀၁၄ - အင္းစိန္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-29/DVD-29-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama-14-1-2014.mp4">
								၃။ အစြမ္းထက္ေသာ အေတြးမ်ား (၁၄-၁-၂၀၁၄ - 
								ဇမၺဴသီရိဗိမာန္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">၄။ ငါးပါးကိုတည္ ေလးပါးကိုပြား 
								(၁၅-၁-၂၀၁၄ - ဇမၺဴသီရိဗိမာန္)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၃၀)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">၁။ ႏိႈင္းယွဥ္ မွန္းဆျခင္း 
								(မုံရြာၿမိဳ႕)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-30/DVD-30-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama-A-Lo-Aut.mp4">
								၂။ အလိုရွိအပ္ေသာ (မုံရြာၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-30/DVD-30-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama-A-Thi-Nae.mp4">
								၃။ ဆင္းရဲေဝးေၾကာင္း ခ်မ္းသာေၾကာင္း (ေတာင္ဥကၠလာပ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-30/DVD-30-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama-Thu-Taw-Kaung.mp4">
								၄။ သူေတာ္ေကာင္းတို႕ သေဘာထား (မႏ ၱေလး)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၃၁)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-31/DVD-31-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ အႏွစ္သုံးပါး (၂၀-၁-၂၀၁၄ - ေမာ္လၿမိဳင္ၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-31/DVD-31-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ စိတ္သာလွ်င္ ပဓာန (၃၁-၁-၂၀၁၄ - ေတာင္ဥကၠလာပ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-31/DVD-31-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ အေကာင္းဆုံးေဆး အေကာင္းဆုံးေရ (၁၀-၂-၂၀၁၄ - 
								ေတာင္ဥကၠလာပ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-31/DVD-31-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၄။ အားကိုးရာကို ဘယ္လိုရွာမလဲ (၂၅-၁-၂၀၁၄ - 
								ကမာရြတ္ၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-31/DVD-31-Title-05-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၅။ အားကိုးမွ ေဘးလြတ္မည္ (၂၂-၁-၂၀၁၄ - 
								ေတာင္ဥကၠလာပ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၃၂)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-32/DVD-32-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ ရဲရင့္ေသာ ျမတ္ဘုရား၏ အံ့ဖြယ္ (၄)ပါး (၉-၅-၂၀၁၄ 
								- ျပင္ဦးလြင္ၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-32/DVD-32-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ ကုသိုလ္ႏွင့္ အကုသိုလ္ (၆-၅-၂၀၁၄ - မႏ 
								ၱေလးၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-32/DVD-32-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ ေမတၱာရွိ၍ သစၥာသိပါ (၇-၅-၂၀၁၄ - မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-32/DVD-32-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၄။ ဘုရားႏွင့္ နီးသူ (၃၀-၃-၂၀၁၄ - 
								မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၃၃)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-33/DVD33-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">၁။ စိတၱသူႂကြယ္ (၂၂-၈-၂၀၁၃ - 
								မုံရြာၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-33/DVD33-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">၂။ အခြင့္သာတုန္း လြတ္ေအာင္ရုန္း 
								(၃၁-၃-၂၀၁၄ - မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-33/DVD33-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">၃။ တစ္ခုေသာတရား၏ ဂုဏ္ေက်းဇူးမ်ား 
								(၁၈-၈-၂၀၁၃ - မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-33/DVD33-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">၄။ ဆုတ္ယုတ္ေၾကာင္းႏွင့္ 
								ႀကီၚပြားေၾကာင္း (၁၆-၈-၂၀၁၃ - ေက်ာက္ဆည္ၿမိဳ႕)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၃၄)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-34/DVD-34-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ မဂၤလာ တရားေတာ္ (၁) (မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-34/DVD-34-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ မဂၤလာ တရားေတာ္ (၂) (မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-34/DVD-34-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ မဂၤလာ တရားေတာ္ (၃) (ေျမာက္ဥကၠလာပၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-34/DVD-34-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၄။ မဂၤလာ တရားေတာ္ (၄) (ေျမာက္ဥကၠလာပၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-34/DVD-34-Title-05-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၅။ မဂၤလာ တရားေတာ္ (၅) (မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အမွတ္စဥ္(၃၅)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-35/DVD-35-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ မဂၤလာ တရားေတာ္ (၆) (ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-35/DVD-35-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ မဂၤလာ တရားေတာ္ (၇) (ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-35/DVD-35-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ မဂၤလာ တရားေတာ္ (၈) (ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-35/DVD-35-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၄။ မဂၤလာ တရားေတာ္ (၉) (မုံရြာၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-35/DVD-35-Title-05-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၅။ မဂၤလာ တရားေတာ္ (၁၀) (မုံရြာၿမိဳ႕နယ္)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">အမွတ္စဥ္(၃၆)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								၁။ အားလုံးကို လႊတ္လိုက္ပါ (၁၂-၉-၂၀၁၄) 
								မုံရြာၿမိဳ႕</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">၂။ ေရေသာက္ျမစ္ (၁၂-၉-၂၀၁၄) 
								မုံရြာၿမိဳ႕</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">၃။ ဆီခြက္ (သို႕) ကာယဂတာသတိ 
								(၁၃-၉-၂၀၁၄) မုံရြာၿမိဳ႕</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">၄။ စိတ္မနာေအာင္ ေနတတ္သူ 
								(၁၃-၉-၂၀၁၄) မုံရြာၿမိဳ႕</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">၅။ ေကာင္းေသာတရားဆိုသည္မွာ 
								(၁၄-၉-၂၀၁၄) မုံရြာၿမိဳ႕</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">အမွတ္စဥ္(၃၇)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-37/DVD37-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ လုံ႕ဟဟူသည္ (၁၄-၉-၂၀၁၄) မုံရြာၿမိဳ႕</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-37/DVD37-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ ပုေဏၰာဝါဒ (၁၅-၉-၂၀၁၄) မုံရြာၿမိဳ႕</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-37/DVD37-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ စိတ္၏ ရန္သူ (၁၅-၉-၂၀၁၄) မုံရြာၿမိဳ႕</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-37/DVD37-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၄။ ေျပာမယုံ ႀကဳံမွ သိ (၁၆-၉-၂၀၁၄) မုံရြာၿမိဳ႕</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">အမွတ္စဥ္(၃၈)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-38/DVD38-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ ပညာဆိုတာ ရတနာပါ (၁၄-၆-၂၀၁၄) ေမွာ္ဘီၿမိဳ႕</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-38/DVD38-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ ဇနပဒၵကလ်ာဏီဝတၳဳ (၂-၁-၂၀၁၅) မဂၤလာေစ်း</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-38/DVD38-Title-04-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ အက်ိဳးမဲ့ျခင္းႏွင့္ အက်ိဳးရွိျခင္း၏ 
								အေၾကာင္းတရားမ်ား (၁၄-၁-၂၀၁၅) ပုဇြန္ေတာင္ၿမိဳ႕နယ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">အမွတ္စဥ္(၃၉)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-39/DVD39-Title-01-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၁။ သံသရာခရီးသြားလမ္းမမွားဖို႕လိုသည္ (၂၀-၄-၂၀၁၅) 
								ကမာရြတ္ၿမိဳ႕နယ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-39/DVD39-Title-02-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၂။ တစ္ေၾကာင္းတည္းေသာလမ္း (၂၁-၄-၂၀၁၅) 
								ကမာရြတ္ၿမိဳ႕နယ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-39/DVD39-Title-03-ThitsarShweSi-Sayadaw-AshinOaktama.mp4">
								၃။ သင္မွ တ္မည္၊ က်င့္မွ ျမတ္မည္ (၂၂-၄-၂၀၁၅) 
								ကမာရြတ္ၿမိဳ႕နယ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၀)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-40/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD40.mp4">၁။ လဆန္းရက္မွာ သာတဲ့လ (၅-၇-၂၀၁၅ - ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-40/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD40.mp4">၂။ တရားက်င့္သူ ဆိုသည္မွာ (၆-၇-၂၀၁၅ - ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-40/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD40.mp4">၃။ သံသရာခရီးသြားလမ္းမမွားဖို႕လိုသည္ (၂၀-၄-၂၀၁၅ - ကမာရြတ္ၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-40/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD40.mp4">၄။ တစ္ေၾကာင္းတည္းေသာလမ္း (၂၁-၄-၂၀၁၅ - ကမာရြတ္ၿမို႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-40/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD40.mp4">၅။ သင္မွတတ္မည္ က်င့္မွ ျမတ္မည္ (၂၂-၄-၂၀၁၅ - ကမာရြတ္ၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၁)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-41/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD41.mp4">၁။ ပညာရွိတို႕၏ အရည္အခ်င္းသုံးမ်ိဳး (၁၉-၆-၂၀၁၅ - 
မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-41/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD41.mp4">၂။ အေသေကာင္းဖို႕ အေသလြတ္ဖို႕ (၂၀-၆-၂၀၁၅ - မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-41/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD41.mp4">၃။ အားကိုးရာအမွန္ သတိပ႒ာန္ (၂၁-၆-၂၀၁၅ - မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-41/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD41.mp4">၄။ သတိပ႒ာန္ (သို႕) တစ္ေၾကာင္းတည္းေသာလမ္း (၂၂-၆-၂၀၁၅ - 
ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-41/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD41.mp4">၅။ ခ်မ္းသာစြာေနနည္း (၂၃-၆-၂၀၁၅ - ရန္ကင္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၂)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-42/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD42.mp4">၁။ ေရွာင္လြဲ၍ မရေသာအရာ (၂၃-၂-၂၀၁၅)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-42/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD42.mp4">၂။ မေကာင္းမႈေရွာင္ (၇-၁၀-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-42/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD42.mp4">၃။ ေကာင္းမႈေဆာင္ (၈-၁၀-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-42/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD42.mp4">၄။ ျဖဴေအာင္စိတ္ကိုထား (၉-၁၀-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၃)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-43/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD43.mp4">၁။ ဒီတရားေတြကို ေျပာေပးပါ (၁၆-၁၁-၂၀၁၅ - ဇမၺဴသီရိဗိမာန္ေတာ္၊။ 
မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-43/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD43.mp4">၂။ ရႏိုင္ခဲေသာ အခြင့္အေရး (၁၇-၁၁-၂၀၁၅ - ဇမၺဴသီရိဗိမာန္ေတာ္၊ 
မရမ္းကုန္းၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-43/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD43.mp4">၃။ သုခ (၁၂) ပါး (၁၈-၁၁-၂၀၁၅ - ဇမၺဴသီရိဗိမာန္ေတာ္၊ 
မရမ္းကုန္းၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-43/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD43.mp4">၄။ ပီယသုတၱန္ (၆-၉-၂၀၁၅ - သစၥာေရႊစည္ေက်ာင္းတိုက္၊ လွည္းကူးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၄)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-44/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD44.mp4">၁။ အျမတ္ႏွစ္ပါး (အလုံၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-44/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD44.mp4">၂။ ပါလႏွင့္ ပႏၵိတ (အင္းစိန္ၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-44/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD44.mp4">၃။ ထူးျမတ္ဂုဏ္သိမ္ ဥတ္ကထိန္ ဆက္ကပ္ပူဇာႏွင့္ 
သိကၡာထပ္ အလွဴေတာ္မဂၤလာ</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-44/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD44.mp4">
၄။ လူမိုက္ႏွင့္ ပညာရွိ (မဂၤလာေတာင္ညြန္႕ၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၅)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-45/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD45-27-2-2016(1).mp4">၁။ ကိုယ့္စိတ္ကို စစ္ေဆးပါ 
(၁) (၂၇-၂-၂၀၁၆၊ ေက်ာက္တံတားၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-45/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD45-27-2-2016(2).mp4">
၂။ ကိုယ့္စိတ္ကို စစ္ေဆးပါ 
(၂) (၂၇-၂-၂၀၁၆၊ ေက်ာက္တံတားၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-45/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD45-16-8-2015.mp4">
၃။ ဗလသုတၱန္ (၁၆-၈-၂၀၁၅၊ မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-45/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD45-7-12-2015.mp4">
၄။ သုခေလးမ်ိဳး (၇-၁၂-၂၀၁၅၊ အလုံၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-45/05-ThitsarShweSi-Sayadaw-AshinOaktama-DVD45-6-4-2015.mp4">
၅။ အက်ိဳးမ်ားေသာ သတိ (၁၀)မ်ိဳး၊ (၆-၄-၂၀၁၅၊ မရမ္းကုန္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<font size="4">
								အမွတ္စဥ္(၄၆)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-46/01-ThitsarShweSi-Sayadaw-AshinOaktama-DVD46-24-1-2016.mp4">၁။ သတိပ႒ာန္ (၂၄-၁-၂၀၁၆၊ တာေမြၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-46/02-ThitsarShweSi-Sayadaw-AshinOaktama-DVD46-25-1-2015.mp4">၂။ အက်ိဳးမဲ့ျခင္းႏွင့္ အက်ိဳရွိျခင္း အေၾကာင္းတရား (၂၅-၁-၂၀၁၅၊ 
စမ္းေခ်ာင္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-46/03-ThitsarShweSi-Sayadaw-AshinOaktama-DVD46-30-1-2015.mp4">၃။ ရႏိုင္ခဲေသာ အခြင့္အေရး (၃၀-၁၁-၂၀၁၅၊ သံလ်င္ၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/ThitsarShweSi-Sayadaw-AshinOaktama/DVD-46/04-ThitsarShweSi-Sayadaw-AshinOaktama-DVD46-30-3-2015.mp4">၄။ စစ္မွန္ေသာ အားကိုးရာ (၃၀-၃-၂၀၁၅၊ ေမွာ္ဘီၿမိဳ႕နယ္)</a></font></p>
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

count = 383        
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