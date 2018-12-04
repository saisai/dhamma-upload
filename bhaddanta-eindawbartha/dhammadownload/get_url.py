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
	
<div style="position: absolute; width: 506px; height: 53px; z-index: 2; left: 52px; top: 53px;" id="layer22" align="center">
	<font size="5" color="#800080"><span style="font-family: Times New Roman">
	PakokKu Sayadaw U EinDawBarTha</span></font></div>
	
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 545px; top: 12px;" id="layer23">
	<img src="images/Bhaddanta-Eindawbartha.gif" width="139" height="213" border="0"></div>
	
	

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
									<font size="4">
										<span style="FONT-WEIGHT: 700; FONT-FAMILY: Franklin Gothic Medium">
									Pakokku Sayadaw </span></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									U EinDawBarTha</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
									<font size="4" face="Zawgyi-One">
									ေက်ူဇူးေတာ္ရွင္<br>
									ဓမၼာႏုပႆနာ ပခုကၠဴ ဆရာေတာ္ဘုရားႀကီး<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
								<font size="6" face="Zawgyi-One">ဘဒၵႏၲ ဣေႏၵာဘာသ</font></p>
								<p class="MsoTagline" style="text-kashida-space: 50%; text-align: left; margin-top: 0px; margin-bottom: 0px">
								<font size="5">အနိစၥ ဆရာေတာ္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">
									ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ပင္လုံဝိဟာရေက်ာင္း၊ ေတဇိႏၵရာမေက်ာင္းတိုက္၊ 
									ကုကၠိဳင္းလမ္းဆုံ၊ ကမာၻေအးဘုရားလမ္း၊ 
									ဗဟန္းၿမိဳ႕နယ္၊ ရန္ကုန္ၿမိဳ႕</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a href="http://www.aniccasayadaw.org/dhamma_talks.htm">
									http://www.aniccasayadaw.org/dhamma_talks.htm</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
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
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-ragaselmeenyainnyeehtonatevan.mp4">ရာဂဆယ္မီး ၿငိမ္းနည္း ထိုနိဗၺာန္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">၂-၁-၂၀၀၆ 
								ဓမၼာႏုပႆနာ တရားေတာ္<br>
								၃-၈-၂၀၀၇</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-7-7-2007.mp4">၇-၇-၂၀၀၇ ဓမၼာႏုပႆနာ တရားပြဲ</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-23-1-2007-singapore-1.mp4">၂၃-၁-၂၀၀၇ စကၤာပူ (၁)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-23-1-2007-singapore-2.mp4">၂၃-၁-၂၀၀၇ စကၤာပူ (၂)</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-21-1-2007-singapore.mp4">၂၁-၁-၂၀၀၇
								စကၤာပူ </a>
								</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-24-1-2007-singapore.mp4">၂၄-၁-၂၀၀၇&nbsp; 
								စကၤာပူ</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-13-6-2007-erthawalltayarphyitphoatahkaung.mp4">၁၃-၆-၂၀၀၇ အာသေ၀ါတရားျဖစ္ဖို႕ အေၾကာင္း တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-14-6-2007-ahhtoohtooahmyomyophyitnaythawahchinahyar.mp4">၁၄-၆-၂၀၀၇ အထူးထူး အမ်ိဳးမ်ိဳးျဖစ္ေနေသာ အျခင္းအရာ 
								တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-15-6-2007-ahyatenamateerryongmasheatya.mp4">၁၅-၆-၂၀၀၇ အရိပ္နမိတ္ အာရုံမရွိရ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-16-9-2007-lumasheatthawtayartaw.mp4">၁၆-၉-၂၀၀၇ လူမရွိေသာတရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-17-9-2007-attamasheatthawtayartaw.mp4">၁၇-၉-၂၀၀၇ အတၲမရွိေသာတရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-29-8-2007.mp4">၂၉-၈-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-3-9-2007.mp4">၃။၄-၉-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-7-9-2007.mp4">၇-၉-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-30-8-2007.mp4">၃၀-၈-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-8-9-2007.mp4">၈-၉-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-12-9-2007-waidanarkopinechairtheatchin.mp4">၁၂-၉-၂၀၀၇ ေ၀ဒနာကို ပိုင္းျခား၍ မသိသည္ရွိေသာ္ 
								တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-21-9-2007-setkhuanatesatordoakkhatorahnettator.mp4">၂၁-၉-၂၀၀၇ စကၡဳ အနိစၥေတာ၊ ဒုကၡေတာ၊ အနတၲေတာ 
								တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-24-9-2007-ahchainnayyarthabarwaahhannharmapar.mp4">၂၄-၉-၂၀၀၇ အခ်ိန္ေနရာ သဘာ၀ အဟံငါမပါ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-25-9-2007-oopardanphoaktaiktayartaw.mp4">၂၅-၉-၂၀၀၇ ဥပါဒါန္ျပဳတ္တဲ့ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-28-9-2007-wargonenhitkhukoakyoakhtutmanar.mp4">၂၈-၉-၂၀၀၇ ၀ါဂြမ္းႏွစ္ခုေကာက္၍ ထုနာမႈမရွိ 
								ဥေကၡာႏွင္ ေက်ာက္ခဲႏွစ္ခုေကာက္၍ ထုမနာမႈ 
								အနတၲတရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-30-9-2007-thutaparmakongkokansoeeat.mp4">၃၀-၉-၂၀၀၇ သူတစ္ပါးမေကာင္းႀကံ၊ ကိုယ္ကံဆိုး၏ 
								တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-1-10-2007-zarteatzayarmaranadoakkhathitsar.mp4">၁-၁၀-၂၀၀၇ ဇာတိ၊ ဇရာ၊ မရဏ ဒုကၡသစၥာ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-2-10-2007-ahkaungahkyotheat.mp4">၂-၁၀-၂၀၀၇ အေၾကာင္း အက်ိဳးသိ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-3-10-2007-oopadankoneyinphyitpyetkone.mp4">၃-၁၀-၂၀၀၇ ဥပါဒါန္ ကုန္ရင္ ျဖစ္ပ်က္ကုန္တဲ့ 
								တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-4-10-2007-zarteatphyityinzayarmaranaphyit.mp4">၄-၁၀-၂၀၀၇ ဇာတိျဖစ္ရင္ ဇရာမရဏျဖစ္တဲ့ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-5-10-2007-ahsaytanorahbyartanor.mp4">၅-၁၀-၂၀၀၇ အေစတေနာ အဗ်ာတေနာ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-6-10-2007-ahwaitzarmasheatlumasheat.mp4">၆-၁၀-၂၀၀၇ အ၀ိဇၨာမရွိ လူမရွိ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-7-10-2007-pyitsoakpanhtairmharahwaitzarsheattel.mp4">၇-၁၀-၂၀၀၇ ပစၥဳပန္ထဲမွာ အ၀ိဇၨာရွိတယ္ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-12-10-2007-sateparamettayartaw-01.mp4">၁၂-၁၀-၂၀၀၇ စိတ္ပရမတ္ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-6-1-2008-manorpyinnyan.mp4">၆-၁-၂၀၀၈ မေနာ ပညာဏ္ တရားေတာ္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">၇-၁-၂၀၀၈ 
								ေတာင္းတင္းကုသာ သိလိုက္ပါ၊ သူဟာတ၀က္က်ိဳးၿပီတည္း။</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-8-1-2008-lettheekoyaehtooyoeyoepahtaweemyin.mp4">၈-၁-၂၀၀၈ လက္သီးကိုေရထိုး ရုိးရုိးပထ၀ီျမင္</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/BhaddantaEindawbartha/Bhaddantaeindawbartha-12-1-2008-manorlawkaypeeyayoupanthantanyoupan.mp4">၁၂-၁-၂၀၀၈ မေနာေလာေက ပီယရူပံ သႏၲာန္ ရူပံ တရားေတာ္</a></font></p>
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
<span style="font-size: 14pt">****dhamma talks uploaded and published on 7 March 2010 ****</span></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">လက္ေရြးစင္ 
								တရားေတာ္မ်ား (၁)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/001-BhaddantaEindawbartha-20090510-KanPonYateHlwar-A.mp4">၁။ ၁၀-၅-၂၀၀၉&nbsp;&nbsp; ကံပုံရိပ္လႊာ (၁)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/002-BhaddantaEindawbartha-20090511-KanPonYateHlwar-B.mp4">၂။ ၁၁-၅-၂၀၀၉&nbsp;&nbsp; ကံပံုရိပ္လႊာ (၂)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/003-BhaddantaEindawbartha-20090512-AuParDanNetKhanDar.mp4">၃။ ၁၂-၅-၂၀၀၉&nbsp;&nbsp; ဥပါဒါနကၡႏၶာ ဒုကၡသစၥာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/004-BhaddantaEindawbartha-20090513-YawGarMaShinAungNayThi.mp4">၄။ ၁၃-၅-၂၀၀၉&nbsp;&nbsp; ေရာဂါမရွင္ေအာင္ေနသည္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/005-BhaddantaEindawbartha-20090514-KanWiParGarKiLayTharAHanNgarMaPar.mp4">၅။ ၁၄-၅-၂၀၀၉&nbsp;&nbsp; ကံ၀ိပါကာ ကိေလသာ၊ 
								အဟံငါမပါ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/006-BhaddantaEindawbartha-20090516-KoHtwetPyitSee.mp4">၆။ ၁၆-၅-၂၀၀၉&nbsp;&nbsp; ကိုယ္ထြက္ပစၥည္း 
								တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/007-BhaddantaEindawbartha-20090517-NgaAPawHmarHletThawThanThaYar.mp4">၇။ ၁၇-၅-၂၀၀၉&nbsp;&nbsp; ငါ့အေပၚမွာလွည့္ေသာ 
								သံသရာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/008-BhaddantaEindawbartha-20090518-MegginTiThawSay.mp4">၈။ ၁၈-၅-၂၀၀၉&nbsp;&nbsp; မဂၢတည္ေသာေဆး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/009-BhaddantaEindawbartha-20090519-ThanThaYarLutMinGaLar.mp4">၉။ ၁၉-၅-၂၀၀၉&nbsp;&nbsp; သံသရာလြတ္ မဂၤလာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/010-BhaddantaEindawbartha-20090520-DwayMayAnDar.mp4">၁၀။ ၂၀-၅-၂၀၀၉&nbsp;&nbsp; ေဒြးေမ အႏၲာအယုတ္ 
								တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/011-BhaddantaEindawbartha-20090521-KanThinKharYaDoteKhaThitSar.mp4">၁၁။ ၂၁-၅-၂၀၀၉&nbsp;&nbsp; ကံ၊ သခၤါရ ဒုကၡသစၥာ 
								တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/012-BhaddantaEindawbartha-20090522-KiLayTharKoNgarHmat.mp4">၁၂။ ၂၂-၅-၂၀၀၉&nbsp;&nbsp; ကိေလသာကုိ ငါမွတ္တဲ့ 
								တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/013-BhaddantaEindawbartha-20090523-ZaYarMaRaNaMonSarYa.mp4">၁၃။ ၂၃-၅-၂၀၀၉&nbsp;&nbsp; ဇရာ မရဏ အိုစာရ 
								တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/014-BhaddantaEindawbartha-20090524-SetKhuKaRaNiNyarNaKaRaNi.mp4">၁၄။ ၂၄-၅-၂၀၀၉&nbsp;&nbsp; စကၡဳကရဏီ၊ ဉာဏကရဏီ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/015-BhaddantaEindawbartha-20090525-TayKhiNaViZarAWiRuNiSanDar.mp4">၁၅။ ၂၅-၅-၂၀၀၉&nbsp;&nbsp; ေတခီဏဗီဇာ အ၀ိဂုဋါဆႏၵာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/016-BhaddantaEindawbartha-20090526-KarMaThuKharMyitZiMaPaDiPaDar.mp4">၁၆။ ၂၆-၅-၂၀၀၉&nbsp;&nbsp; ကာမသုခါ မဇၩိမာ ပဋာပဒါ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/017-BhaddantaEindawbartha-20090527-WutKaPhyitSe.mp4">၁၇။ ၂၇-၅-၂၀၀၉&nbsp;&nbsp; ၀ဋ္ကျဖစ္ဆဲ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/018-BhaddantaEindawbartha-20090529-ZiWaYoteSetYote.mp4">၁၈။ ၂၉-၅-၂၀၀၉&nbsp;&nbsp; ဇီ၀႐ုပ္ စက္႐ုပ္ 
								တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/019-BhaddantaEindawbartha-20090530-PyanPyawTonePyan.mp4">၁၉။ ၃၀-၅-၂၀၀၉&nbsp;&nbsp; ျပန္ေျပာတံု႕ ျပန္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-1/020-BhaddantaEindawbartha-20090531-KanKyauntPhyitTeKhanDar.mp4">၂၀။ ၃၁-၅-၂၀၀၉&nbsp;&nbsp; ကံေၾကာင့္ျဖစ္တဲ့ခႏၶာ 
								တရားေတာ္</a><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">လက္ေရြးစင္ 
								တရားေတာ္မ်ား (၂)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/001-BhaddantaEindawbartha-20090601-KaungDalHtinLoeLonKyuDal.mp4">၁။ ၁-၆-၂၀၀၉&nbsp;&nbsp; ေကာင္းတယ္ထင္လို႕ 
								လြန္က်ဴးတယ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/002-BhaddantaEindawbartha-20090602-ThuSaYiteTaYarDoeHniteMaMaeChin.mp4">၂။ ၂-၆-၂၀၀၉&nbsp;&nbsp; သုစ႐ိုက္တရားတုိ႕၌ 
								မေမ့ျခင္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/003-BhaddantaEindawbartha-20090603-AuParDanNayBaYanDiThwar.mp4">၃။ ၃-၆-၂၀၀၉&nbsp;&nbsp; ဥပၸဒါနေနဘယဒိသြာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/004-BhaddantaEindawbartha-20090604-KarYaKanWaZiKanMaNawKan.mp4">၄။ ၄-၆-၂၀၀၉&nbsp;&nbsp; ကာယကံ ၀စီကံ မေနာကံ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/005-BhaddantaEindawbartha-20090605-ThanMarDateHti.mp4">၅။ ၅-၆-၂၀၀၉&nbsp;&nbsp; သမၼာဒိ႒ိ တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/006-BhaddantaEindawbartha-20090607-ThitSarThaTawPaYateThanDi.mp4">၆။ ၇-၆-၂၀၀၉&nbsp;&nbsp; သစၥာႆေတာ ပရိတ္သႏၵိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/007-BhaddantaEindawbartha-20090608-ASweParThawKhanDar.mp4">၇။ ၈-၆-၂၀၀၉&nbsp;&nbsp; အစြဲပါေသာ ခႏၶာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/008-BhaddantaEindawbartha-20090610-ArYoneKoThiMaKatNyiLutEiThanThaYar.mp4">၈။ ၁၀-၆-၂၀၀၉&nbsp;&nbsp; အာ႐ံုကုိသိ မကပ္ၫွိ 
								လြတ္၏သံသရာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/009-BhaddantaEindawbartha-20090611-ThanMarDateHti.mp4">၉။ ၁၁-၆-၂၀၀၉&nbsp;&nbsp; သမၼာဒိ႒ိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/010-BhaddantaEindawbartha-20090612-MarNinSaPaDarNarHti.mp4">၁၀။ ၁၂-၆-၂၀၀၉&nbsp;&nbsp; မနဥၥ ပဓာနထိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/011-BhaddantaEindawbartha-20090613-BuddhaTwae.mp4">၁၁။ ၁၃-၆-၂၀၀၉&nbsp;&nbsp; ဘုရားေတြ႕တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/012-BhaddantaEindawbartha-20090614-ThuKhoeMaShi.mp4">၁၂။ ၁၄-၆-၂၀၀၉&nbsp;&nbsp; သူခိုးမရွိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/013-BhaddantaEindawbartha-20090615-YayDhammarHayTuPaBaWar.mp4">၁၃။ ၁၅-၆-၂၀၀၉&nbsp;&nbsp; ေယဓမၼာ ေဟတုပၸဘ၀ါ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/014-BhaddantaEindawbartha-20090617-DwayMayBateKhaWay.mp4">၁၄။ ၁၇-၆-၂၀၀၉&nbsp;&nbsp; ေဒြေမဘိကၡေ၀ အႏၲာ ၃၁ဘံု</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/015-BhaddantaEindawbartha-20090618-LuMaHoteTeKatPar.mp4">၁၅။ ၁၈-၆-၂၀၀၉&nbsp;&nbsp; လူမဟုတ္တဲ့ ကပ္ပါး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/016-BhaddantaEindawbartha-20090619-ThanThaYar.mp4">၁၆။ ၁၉-၆-၂၀၀၉&nbsp;&nbsp; သံသရာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/017-BhaddantaEindawbartha-20090620-DuSaYiteTharShaungKyinPar.mp4">၁၇။ ၂၀-၆-၂၀၀၉&nbsp;&nbsp; 
								ဒုစ႐ုိက္သာေရွာင္ၾကဥ္ပါထီးျဖဴေအာက္မွာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/018-BhaddantaEindawbartha-20090622-MaNawKanThi.mp4">၁၈။ ၂၂-၆-၂၀၀၉&nbsp;&nbsp; မေနာကံသိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-2/019-BhaddantaEindawbartha-20090623-AWateZarThinKharYaWaneNyanNanYote.mp4">၁၉။ ၂၃-၆-၂၀၀၉&nbsp;&nbsp; အ၀ိဇၨာ သခၤါရ ၀ိဉာဏ္၊ 
								နာမ္႐ုပ္</a><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">လက္ေရြးစင္ 
								တရားေတာ္မ်ား (၃)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/001-BhaddantaEindawbartha-20090705-ThaMarDateHti.mp4">၁။ ၅-၇-၂၀၀၉&nbsp;&nbsp; သမၼာဒိ႒ိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/002-BhaddantaEindawbartha-20090706-WutKaungNeltWut.mp4">၂။ ၆-၇-၂၀၀၉&nbsp;&nbsp; ၀ဋ္ေကာင္နဲ႕၀ဋ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/003-BhaddantaEindawbartha-20090707-PaRaMatSuPyitNyatSuLuYeltAHmu.mp4">၃။ ၇-၇-၂၀၀၉&nbsp;&nbsp; ပရမတ္စု ပညတ္စု လူရဲ႕အမႈ႕</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/004-BhaddantaEindawbartha-20090708-PaRaMatSuPyitNyatSu.mp4">၄။ ၈-၇-၂၀၀၉&nbsp;&nbsp; ပရမတ္စု ပညတ္စု 
								</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/005-BhaddantaEindawbartha-20090709-LuYeltAHmu.mp4">၅။ ၉-၇-၂၀၀၉&nbsp;&nbsp; လူရဲ႕အမႈ႕</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/006-BhaddantaEindawbartha-20090710-Wut3ParLuNeltTaCharSi.mp4">၆။ ၁၀-၇-၂၀၀၉&nbsp;&nbsp; ၀ဋ္သံုးပါးလူနဲ႕တၿခားစီ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/007-BhaddantaEindawbartha-20090711-PhaYarYaDaNar%20TaYarYaDaNar.mp4">၇။ ၁၁-၇-၂၀၀၉&nbsp;&nbsp; ဘုရားရတနာ တရားရတနာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/008-BhaddantaEindawbartha-20090712-ThaMarDateHti.mp4">၈။ ၁၂-၇-၂၀၀၉&nbsp;&nbsp; သမၼာဒိ႒ိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/009-BhaddantaEindawbartha-20090713-PuHtuZin.mp4">၉။ ၁၃-၇-၂၀၀၉&nbsp;&nbsp; ပုထုဇဥ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/010-BhaddantaEindawbartha-20090714-EiManThaMeinYayWa.mp4">၁၀။ ၁၄-၇-၂၀၀၉&nbsp;&nbsp; ဣမံသၼိေယ၀ ကေဠ၀ေရ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/011-BhaddantaEindawbartha-20090715-ABhiThinKharYaWiNyan.mp4">၁၁။ ၁၅-၇-၂၀၀၉&nbsp;&nbsp; နာဘိသခၤါရ 
								၀ိဉာဏ္တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/012-BhaddantaEindawbartha-20090718-NyitKatChinSweLanChinMaShiThaw.mp4">၁၂။ ၁၈-၇-၂၀၀၉&nbsp;&nbsp; ၿငိကပ္ၿခင္း 
								စဲြလမ္းၿခင္း မရွိေသာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/013-BhaddantaEindawbartha-20090719-ThaMarWarSar.mp4">၁၃။ ၁၉-၇-၂၀၀၉&nbsp;&nbsp; သမၼာ၀ါစာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/014-BhaddantaEindawbartha-20090720-MyitZiMaPaDiPaDar.mp4">၁၄။ ၂၀-၇-၂၀၀၉&nbsp;&nbsp; မဇၩိမပဋိပဒါ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/015-BhaddantaEindawbartha-20090721-Buddha.mp4">၁၅။ ၂၁-၇-၂၀၀၉&nbsp;&nbsp; ဘုရား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/016-BhaddantaEindawbartha-20090722-WiTateKaMa.mp4">၁၆။ ၂၂-၇-၂၀၀၉&nbsp;&nbsp; ၀ိတိကၠမ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/017-BhaddantaEindawbartha-20090723-KanThi.mp4">၁၇။ ၂၃-၇-၂၀၀၉&nbsp;&nbsp; ကံသိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-3/018-BhaddantaEindawbartha-20090724-ZarTiZaYarMaRaNa.mp4">၁၈။ ၂၄-၇-၂၀၀၉&nbsp;&nbsp; ဇာတိ ဇရာ မရဏ</a><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">လက္ေရြးစင္ 
								တရားေတာ္မ်ား (၄)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/001-BhaddantaEindawbartha-20090726-APhayMyinAThinThi.mp4">၁။ ၂၆-၇-၂၀၀၉&nbsp;&nbsp; အေၿဖၿမင္အသင္သိ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/002-BhaddantaEindawbartha-20090727-ThaMarDateHtiThaMarWarSar.mp4">၂။ ၂၇-၇-၂၀၀၉&nbsp;&nbsp; သမၼာဒိ႒ိ သမၼာ၀ါစာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/003-BhaddantaEindawbartha-20090801-DateHtiMatTar.mp4">၃။ ၁-၈-၂၀၀၉&nbsp;&nbsp; ဒိ႒ိေမတၲာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/004-BhaddantaEindawbartha-20090802-AMyetDawThaKoPalSontYarEi.mp4">၄။ ၂-၈-၂၀၀၉&nbsp;&nbsp; အမ်က္ေဒါသကို ပယ္စြန္႕ရာ၏</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/005-BhaddantaEindawbartha-20090803-AWateZarYaTayWa.mp4">၅။ ၃-၈-၂၀၀၉&nbsp;&nbsp; အ၀ိဇၨာရ ေတ၀</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/006-BhaddantaEindawbartha-20090808-WateZarWiYarGa.mp4">၆။ ၈-၈-၂၀၀၉&nbsp;&nbsp; ၀ိဇၨာ ၀ိရာဂ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/007-BhaddantaEindawbartha-20090809-KaneSiPiBaw.mp4">၇။ ၉-၈-၂၀၀၉&nbsp;&nbsp; ကိဥၥာ ပိေဘာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/008-BhaddantaEindawbartha-20090815-NateBanTiYar.mp4">၈။ ၁၅-၈-၂၀၀၉&nbsp;&nbsp; နိဗၺာန္တည္ရာ 
								သစၥာေလးပါတည္ရာ ဒြါရတည္ရာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/009-BhaddantaEindawbartha-20090816-AuParDarNetKhanDar.mp4">၉။ ၁၆-၈-၂၀၀၉&nbsp;&nbsp; ဥပါဒါန္နကၡႏၶာ 
								အေယာင္ေဆာင္လူ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/010-BhaddantaEindawbartha-20090817-PatWunKyinKoAThiHmar.mp4">၁၀။ ၁၇-၈-၂၀၀၉&nbsp;&nbsp; ပတ္၀န္းက်င္ကို 
								အသိမွား၊ အမွတ္မွား၊ အယူမွား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/011-BhaddantaEindawbartha-20090818-ThanMarDateHtiThanMarThinKatPa.mp4">၁၁။ ၁၈-၈-၂၀၀၉&nbsp;&nbsp; သမၼာဒိ႒ိ သမၼာသကၤပၸ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/012-BhaddantaEindawbartha-20090819-SetKhuNarThanWaYawTharDu.mp4">၁၂။ ၁၉-၈-၂၀၀၉&nbsp;&nbsp; စကၡဳနာ သံ၀ေရာသာဓု</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/013-BhaddantaEindawbartha-20090820-MyitZiMaPaDiPaDar.mp4">၁၃။ ၂၀-၈-၂၀၀၉&nbsp;&nbsp; မဇၩိမ ပဋိပဒါ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/014-BhaddantaEindawbartha-20090821-DateHtayDateHtaMatTan.mp4">၁၄။ ၂၁-၈-၂၀၀၉&nbsp;&nbsp; ဒိေ႒ဒိ႒မတၲံ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/015-BhaddantaEindawbartha-20090822-WateZarWiYawGa.mp4">၁၅။ ၂၂-၈-၂၀၀၉&nbsp;&nbsp; ၀ိေဇၨာ ၀ိေရာဂ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/016-BhaddantaEindawbartha-20090823-PatWunKyinKoAThiHmarTarAWateZar.mp4">၁၆။ ၂၃-၈-၂၀၀၉&nbsp;&nbsp; ပတ္၀န္းက်င္ကုိ 
								အသိမွားတာ အ၀ိဇၨာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/017-BhaddantaEindawbartha-20090824-TaPawSaMinGaLar.mp4">၁၇။ ၂၄-၈-၂၀၀၉&nbsp;&nbsp; တေပါစမဂၤလာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/018-BhaddantaEindawbartha-20090825-AWateZarYaTayWaAThayThaWiYawGar.mp4">၁၈။ ၂၅-၈-၂၀၀၉&nbsp;&nbsp; ပ၀ိဇၨာရေတ၀ အေသ၀ိေရာဂါ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-4/019-BhaddantaEindawbartha-20090826-ThitSarThatTaw.mp4">၁၉။ ၂၆-၈-၂၀၀၉&nbsp;&nbsp; သစၥာသေတၲာ</a><br>
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
								<font style="font-size: 14pt" face="Zawgyi-One">လက္ေရြးစင္ 
								တရားေတာ္မ်ား (၅)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/001-BhaddantaEindawbartha-20090828-KammaNeltKammaBaWa.mp4">၁။ ၂၈-၈-၂၀၀၉&nbsp;&nbsp; ကမၼနဲ႕ ကမၼဘ၀</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/002-BhaddantaEindawbartha-20090829-KarLaNeltThaBarWa.mp4">၂။ ၂၉-၈-၂၉ ကာလနဲ႕သဘာ၀၊ ကာလမရွိဘဲနဲ႕ သဘာ၀မရွိဘူး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/003-BhaddantaEindawbartha-20090901-AWateZarThode.mp4">၃။ ၁-၉-၂၀၀၉&nbsp;&nbsp; အ၀ိဇၨာသုတ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/004-BhaddantaEindawbartha-20090903-AuParDarNetKhanDarDoteKhaThitSar.mp4">၄။ ၃-၉-၂၀၀၉&nbsp;&nbsp; ဥပါဒါနကၡႏၶာ ဒုကၡသစၥာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/005-BhaddantaEindawbartha-20090905-ThitSarANet16Chet.mp4">၅။ ၅-၉-၂၀၀၉&nbsp;&nbsp; သစၥာအနက္ ၁၆ ခ်က္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/006-BhaddantaEindawbartha-20090907-ARiYaThitSar.mp4">၆။ ၇-၉-၂၀၀၉&nbsp;&nbsp; အရိယသစၥာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/007-BhaddantaEindawbartha-20090908-ArThaWaWatePaYote.mp4">၇။ ၈-၉-၂၀၀၉&nbsp;&nbsp; အာသ၀ ၀ိပၸယုတ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/008-BhaddantaEindawbartha-20090909-KarYaKoShuYarGaKoMaHmu.mp4">၈။ ၉-၉-၂၀၀၉&nbsp;&nbsp; ကာယကုိ႐ူ႕ ရာဂကိုမမႈ႕</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/009-BhaddantaEindawbartha-20090910-ZarTiSoThawChaukGyi.mp4">၉။ ၁၀-၉-၂၀၀၉&nbsp;&nbsp; ဇာတိဆုိေသာ ေခ်ာက္ၾကီး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/010-BhaddantaEindawbartha-20090915-ThinKhaTaYoteNanKoAHoteNyan.mp4">၁၀။ ၁၅-၉-၂၀၀၉&nbsp;&nbsp; သခၤါတ႐ုပ္နာမ္ကုိ 
								အဟုတ္ဥာဏ္တင္စီးျခင္း 
								</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/011-bhaddantaeindawbartha-20090916-watezarwimoteti.mp4">၁၁။ ၁၆-၉-၂၀၀၉&nbsp;&nbsp; ၀ိဇၨာ၀ိမုတၲိ တရားေတာ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/012-BhaddantaEindawbartha-20090917-ThinKharYaAKyaung.mp4">၁၂။ ၁၇-၉-၂၀၀၉&nbsp;&nbsp; သခၤါရအေၾကာင္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/013-BhaddantaEindawbartha-20090918-ArYoneHmanKaKiLayThar.mp4">၁၃။ ၁၈-၉-၂၀၀၉&nbsp;&nbsp; အာရံုမွန္ကကိေလသာ၊ 
								ဘယ္ခါအာ႐ံုမၪပၿပီ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/014-BhaddantaEindawbartha-20090919-MyetSiNeltMyinTarKo.mp4">၁၄။ ၁၉-၉-၂၀၀၉&nbsp;&nbsp; 
								မ်က္စိနဲ႕ျမင္တာကိုစိတ္ထဲက ဘယ္လုိထားတာတံုး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/015-BhaddantaEindawbartha-20090921-ThawTarNuGaTa.mp4">၁၅။ ၂၁-၉-၂၀၀၉&nbsp;&nbsp; ေသာတာႏုဂတ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/016-BhaddantaEindawbartha-20090922-SetKhuLawKayWutSwePone.mp4">၁၆။ ၂၂-၉-၂၀၀၉&nbsp;&nbsp; စကၡဳေလာေက၀ဋ္စြဲပံု</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-5/017-BhaddantaEindawbartha-20090923-PiYaYoteKarYaYoteKweHlinTaHnarChote.mp4">၁၇။ ၂၃-၉-၂၀၀၉&nbsp;&nbsp; ပီယရုပ္ကာယရုပ္ 
								ကြဲလွ်င္တဏွာခ်ဳပ္</a><br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">လက္ေရြးစင္ 
								တရားေတာ္မ်ား (၆)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font style="font-size: 14pt" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/001-BhaddantaEindawbartha-20090924-NgarMaYu.mp4">၁။ ၂၄-၉-၂၀၀၉&nbsp;&nbsp; ငါမယူ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/002-BhaddantaEindawbartha-20090925-NgarLarNgarOatSarLar.mp4">၂။ ၂၅-၉-၂၀၀၉&nbsp;&nbsp; ငါလား ငါ့ဥစၥာလား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/003-BhaddantaEindawbartha-20090927-ThuOThuNarThuThay.mp4">၃။ ၂၆-၉-၂၀၀၉&nbsp;&nbsp; အ၀ိဇၨာလား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/004-BhaddantaEindawbartha-20090929-YaThaKarYawHtiTaw.mp4">၄။ ၂၇-၉-၂၀၀၉&nbsp;&nbsp; သူအုိ သူနာ သူေသ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/005-BhaddantaEindawbartha-20090930-AtTaPaRaMaLunKeChin.mp4">၅။ ၂၉-၉-၂၀၀၉&nbsp;&nbsp; ယႆ၊ ကာေယာ၊ ႒ီေတာ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/006-BhaddantaEindawbartha-20091001-MiMiMaLoteTe.mp4">၆။ ၃၀-၉-၂၀၀၉&nbsp;&nbsp; အတၲပရ မလြန္ကဲျခင္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/007-BhaddantaEindawbartha-20091002-WiNyarNaDateHti7Par.mp4">၇။ ၁-၁၀-၂၀၀၉&nbsp;&nbsp; မိမိမလုပ္တဲ့</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/008-BhaddantaEindawbartha-20091003-ThatTaWarMaShiYarGaMaShi.mp4">၈။ ၂-၁၀-၂၀၀၉&nbsp;&nbsp; ၀ိဉာဏဒိ႒ိ (၇)ပါး</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/009-BhaddantaEindawbartha-20091004-ThaKatDratLane.mp4">၉။ ၃-၁၀-၂၀၀၉&nbsp;&nbsp; သတၱ၀ါမရိွ ရာဂမရိွ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/010-BhaddantaEindawbartha-20091005-PaMatHtaBanDuParPiMa.mp4">၁၀။ ၄-၁၀-၂၀၀၉&nbsp;&nbsp; သကတ္၊ ျဒပ္၊ လိင္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/011-BhaddantaEindawbartha-20091006-WiNyanHnitHtat.mp4">၁၁။ ၅-၁၀-၂၀၀၉&nbsp;&nbsp; ပမတၴ ဗႏၶဳ ပါပိမ</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/012-BhaddantaEindawbartha-20091007-WutHtuPuYarZarTaNateThaYa.mp4">၁၂။ ၆-၁၀-၂၀၀၉&nbsp;&nbsp; ၀ိဉာဏ္ ႏွစ္ထပ္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library1/BhaddantaEindawbartha/LetYaweZin-DVD-6/013-BhaddantaEindawbartha-20091008-PaRaMatThanTanTuKyaungKyoeTu.mp4">၁၃။ ၇-၁၀-၂၀၀၉&nbsp;&nbsp; ၀တၳဳပုေရဇာတ၊ 
								နိႆယပစၥည္း</a><br>
								၁၄။ ၈-၁၀-၂၀၀၉&nbsp;&nbsp; ပရမတ္သ႑ာန္တူ၊ 
								ေၾကာင္းက်ိဳးတူ<br>
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
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Zawgyi-One">&nbsp;</font></p>
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
    
