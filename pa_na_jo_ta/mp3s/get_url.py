from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 
<!-- Start dhammadownload menu top and side bar -->

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font size="6" color="#800080">အရွင္သူရိယ</font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 542px; top: 13px;" id="layer23">
	<img src="images/Ashin-Thuriya(AungSyatKyar).gif" width="208" height="209" border="0"></div>
	






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
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								Ashin-Thuriya(AungSyatKyar)</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4">မိုးကုတ္ဝိပသနာအဖြဲ႕ခ်ုပ္ၾကီး၏ 
								ကမၼ႒ာနစရိယ<br>
								သာသနာျပဳ နယ္လွည့္ ဓမၼကထိက ဓမၼစရိယ</font></p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4"><br>
								</font>
								<font size="6">အရွင္သူရိယ</font><font size="4"><br>
								(ရွမ္းစုေအာင္စၾကာ မိုးကုတ္ဝိပသနာဓမၼ ရိပ္သာ)<br>
								</font>ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									**********************************</p>
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
								&nbsp;</font></p>
								<p><font size="4">ပုညၾကိယာ ဆယ္ပါး</font></p>
								<p><font size="4"><br>
								အမွတ္စဥ္ (၁)</font></p>
								<p><font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/01-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၁။ ဒါန ကထာ (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/02-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၂။ သီလ ကထာ (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/03-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၃။ ဘာဝနာ ကထာ (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/04-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၄။ အပစာယန ကထာ (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/05-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၅။ ေဝယ်ာဝ စၥ ကထာ (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/06-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၆။ ပတၱိဒါန (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/07-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၇။ ပတၱာနုေမာဒနာႏွင့္ ဓမၼသဝန 
								(ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-01/08-Ashin-Thuriya(AungSyatKyar)-DVD01.mp4">
								၈။ ဓမၼေဒသနာႏွင့္ ဒိဌိဇုကမ္မ&nbsp; 
								(ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a></font></p>
								<p>&nbsp;</p>
								<p><font size="4"><br>
								ဒိဌိစင္မွ ခ်မ္းသာရ</font></p>
								<p><font size="4"><br>
								အမွတ္စဥ္ (၂)</font></p>
								<p><font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-02/01-Ashin-Thuriya(AungSyatKyar)-DVD02-paypay-myatar-tar-lainmar.mp4">
								၁။ မ်က္စိအလည္ ေပ်ာက္ပါေစ (၁၆.၂.၂၀၁၀- မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-02/02-Ashin-Thuriya(AungSyatKyar)-DVD02-eachitsothimar.mp4">
								၂။ ဒိဌိစင္မွ ခ်မ္းသာရ (၁၁.၉.၂၀၁၀- ပုညာရာမ၊ 
								သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-02/03-Ashin-Thuriya(AungSyatKyar)-DVD02-myatsi-ealal-pyut-par-say.mp4">
								၃။ သစၥာရင္မွာ ပိုက္လုိက္ပါေတာ့မယ္ (၁၁.၂.၂၀၁၀- 
								မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-02/04-Ashin-Thuriya(AungSyatKyar)-DVD02-datdisinma.mp4">
								၄။ ေဖေဖ့ ေမတၱာ သားလိမ္မာ (၈.၂.၂၀၁၀- မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-02/05-Ashin-Thuriya(AungSyatKyar)-DVD02-thitsaryinmar-piplikepardotmal.mp4">
								၅။ အခ်စ္ဆိုသည္မွာ (၁၃.၂.၂၀၁၀- မရမ္းကုန္း)</a></font></p>
								<p>&nbsp;</p>
								<p>&nbsp;</p>
								<p><font size="4">ဘဝပင္လယ္ ခရီးသည္</font></p>
								<p><font size="4"><br>
								အမွတ္စဥ္ (၃)<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-03/01-Ashin-Thuriya(AungSyatKyar)-DVD03.mp4">
								၁။ ေရြးပါ လွူပါ စိစစ္ပါ (သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-03/02-Ashin-Thuriya(AungSyatKyar)-DVD03.mp4">
								၂။ တရားရျခင္း မရျခင္း (ပုညာရာမေက်ာင္း- သာေကတ)</a><br>
								၃။ ဘဝပင္လယ္ ခရီးသည္ (ပုညာရာမေက်ာင္း- သာေကတ)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-03/04-Ashin-Thuriya(AungSyatKyar)-DVD03.mp4">
								၄။ အမွားျဖစ္တာ သူ့ေၾကာင့္ပါ (ပုညာရာမေက်ာင္း- 
								သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-03/05-Ashin-Thuriya(AungSyatKyar)-DVD03.mp4">
								၅။ အငိုနဲ႕စ၍ အျပံဳးနဲ႕ဆံုးသည္ (ပုညာရာမေက်ာင္း- 
								သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-03/06-Ashin-Thuriya(AungSyatKyar)-DVD03.mp4">
								၆။ အမွားသိလွ်င္ အမွန္ျပင္ (မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-03/07-Ashin-Thuriya(AungSyatKyar)-DVD03.mp4">
								၇။ လာရာသြားရာ သိဥာဏ္ရွာ (မရမ္းကုန္း)</a><br>
&nbsp;</font></p>
								<p>&nbsp;</p>
								<p><font size="4">တရားနဲ႕ပဲ ေပ်ာ္ေတာ့မယ္</font></p>
								<p><font size="4"><br>
								အမွတ္စဥ္ (၄)<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-04/01-Ashin-Thuriya(AungSyatKyar)-DVD04.mp4">
								၁။ ဘယ္လိုလူစားလဲ (ေတာင္ဥကၠလာ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-04/02-Ashin-Thuriya(AungSyatKyar)-DVD04.mp4">
								၂။ ႏွုတ္ဆက္မွာၾကား (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-04/03-Ashin-Thuriya(AungSyatKyar)-DVD04.mp4">
								၃။ အမွန္ေျပာတာပါ (ပုညာရာမေက်ာင္းတိုက္- သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-04/04-Ashin-Thuriya(AungSyatKyar)-DVD04.mp4">
								၄။ လမ္းေဟာင္းမျပန္နဲ႕ (ပုညာရာမေက်ာင္းတိုက္- 
								သာေကတ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-04/05-Ashin-Thuriya(AungSyatKyar)-DVD04.mp4">
								၅။ တရားနဲ႕ပဲ ေပ်ာ္ေတာ့မယ္ (ပုညာရာမေက်ာင္းတိုက္- 
								သာေကတ)</a><br>
								<br>
								<br>
								<br>
								<br>
								သူေတာ္ကိုးကြယ္ ေကာင္းက်ိဳးၾကြယ္</font></p>
								<p><font size="4"><br>
								အမွတ္စဥ္ (၅)<br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-05/01-Ashin-Thuriya(AungSyatKyar)-DVD05.mp4">
								၁။ မ ဘက္လိုက္ေတာ့ မိုက္ ဘက္ပါ (မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-05/02-Ashin-Thuriya(AungSyatKyar)-DVD05.mp4">
								၂။ ေသာတာပန္အစစ္ျဖစ္ေၾကာင္း (မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-05/03-Ashin-Thuriya(AungSyatKyar)-DVD05.mp4">
								၃။ ခနၶာငါးခ်က္ ဥာဏ္ေဖ်ာက္ဖ်က္ (မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-05/04-Ashin-Thuriya(AungSyatKyar)-DVD05.mp4">
								၄။ ခနၶာရွုကြက္ ဥာဏ္သံုးခ်က္ (မရမ္းကုန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-05/05-Ashin-Thuriya(AungSyatKyar)-DVD05.mp4">
								၅။ သူေတာ္ကိုးကြယ္ ေကာင္းက်ိဳးၾကြယ္</a><br>
&nbsp;</font></p>
								<p><font size="4">ပဋိစၥသမုပၸါဒ္</font></p>
								<p><font size="4">အမွတ္စဥ္ (၇)</font></p>
								<p><font size="4">ဗဟန္းၿမိဳကနယ္၊ မိုးကုတ္ဝိပႆနာ 
								ဇနိတာရာမေက်ာင္းတိုက္ႀကီး အတြင္း၌ ၃၃၂ ႀကိမ္ေျမာက္
								</font></p>
								<p><font size="4">မိုးကုတ္ဝိပသနာ ၁၀ရက္ အဓိ႒ာန္ 
								တရားစခန္း</font></p>
								<p>&nbsp;</p>
								<p><font size="4">၁။ ၂၅-၉-၂၀၁၃ ပဋိစၥသမုပၸါဒ္ 
								သင္တန္း</font></p>
								<p><font size="4">၂။ ၂၆-၉-၂၀၁၃ ပဋိစၥသမုပၸါဒ္ 
								သင္တန္း</font></p>
								<p><font size="4">၃။ ၂၇-၉-၂၀၁၃ ပဋိစၥသမုပၸါဒ္ 
								သင္တန္း</font></p>
								<p><font size="4">၄။ ၂၈-၉-၂၀၁၃ ပဋိစၥသမုပၸါဒ္ 
								သင္တန္း</font></p>
								<p><font size="4">၅။ ၂၉-၉-၂၀၁၃ ပဋိစၥသမုပၸါဒ္ 
								သင္တန္း</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၈)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">ရန္ကုန္ၿမိဳ႕၊ မိုးကုတ္ဝိပႆနာ တရားစဥ္ႏွင့္ လုပ္ငန္းစဥ္ 
ျပန္႕ပြားေရး အဖြဲ႕ခ်ဳပ္</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အဖြဲ႕ခ်ဳပ္ဓမၼာရုံႀကီးအတြင္း</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">က်င္းပအပ္ေသာ ဝါတြင္း၊ ဝါဆို ပထမအပတ္</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အထူးအလုပ္ေပးတရားစခန္းပြဲႀကီးတြင္ ေဟာၾကားေတာ္မူအပ္ေသာ</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္မ်ား</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/01-Ashin-Thuriya(AungSyatKyar)-DVD08-17-7-14.mp4">၁။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၁)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/02-Ashin-Thuriya(AungSyatKyar)-DVD08-18-7-14.mp4">၂။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၂)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/03-Ashin-Thuriya(AungSyatKyar)-DVD08-19-7-14.mp4">၃။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၃)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/04-Ashin-Thuriya(AungSyatKyar)-DVD08-20-7-14.mp4">၄။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/05-Ashin-Thuriya(AungSyatKyar)-DVD08-21-7-14.mp4">၅။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၅)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/06-Ashin-Thuriya(AungSyatKyar)-DVD08-22-7-14.mp4">၆။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၆)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/07-Ashin-Thuriya(AungSyatKyar)-DVD08-23-7-14.mp4">၇။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၇)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/08-Ashin-Thuriya(AungSyatKyar)-DVD08-24-7-14.mp4">၈။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၈)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/09-Ashin-Thuriya(AungSyatKyar)-DVD08-25-7-14.mp4">၉။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၉)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Ashin-Thuriya(AungSyatKyar)/DVD-08/10-Ashin-Thuriya(AungSyatKyar)-DVD08-26-7-14.mp4">၁၀။ ပဋိစၥသမုပၸါဒ္ သင္တန္း တရားေတာ္ (၁၀)</a></font></p>
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
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
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

count = 1
with open('titles_links.txt', 'w') as f:
    
    for key in soup.find_all('a'):
        if ".mp4" in key.get('href'):
            counter = '{:03d}'.format(count)
            print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())
            
            count += 1        
    
