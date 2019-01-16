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
	<font color="#800080">
	<span style="font-family: Times New Roman;">
	<font style="font-size: 32pt;">Dr. Ashin Kaw Wi Da</font></span></font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 596px; top: 4px;" id="layer23">
	<img src="images/Dr-Ashin-Kaw-Wi-Da.gif" width="198" height="170" border="0"></div>






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
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5">Dr. Ashin Kaw Win Da</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">မဇၩိမဂုဏ္ရည္ 
								မဟာစည္ သာသနာ့ရိပ္သာ ပဓာန နာယက ဆရာေတာ္<br>
								</font><font size="6" face="Zawgyi-One">ေဒါက္တာ 
								ေကာဝိဒ</font><font size="4" face="Zawgyi-One">
								<br>
								BA (Buddhism)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">MBA (Buddhist 
								studies, Magadha University, India)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">Ph.D (Sanskrit 
								University, India)</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">ဓမၼကထိက 
								ဗဟုဇနဟိတဓရ ကမၼဌာနာစရိယ</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">မဟာစည္နယ္လွည္႔ 
								ဓမၼၼကထိက </font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">သာႆနတကၠသီလ 
								ဓမၼာစရိယ</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">မဇၩိမဂုဏ္ရည္လမ္း၊ 
								၁၀-ေတာင္၊ ၁၁ရပ္ကြက္၊ သာေကတၿမိဳ႕နယ္၊ ရန္ကုန္ၿမိဳ႕</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ဖုန္း - ၀၁-၅၄၇၁၃၂၊&nbsp; 
								၀၉-၅၀၂၂၉၈၆</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<br>
								ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား <br>
								<br>
								<br>
								</font>
								<b><font size="5">Dhamma Talk Video</font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-BairThuAhDeatKaLair-D01-14-11-2007.mp4">ဘယ္သူအဓိကလဲတရားေတာ္(၁) ၁၄-၁၁-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-BairThuAhDeatKaLair-D02-14-11-2007.mp4">ဘယ္သူအဓိကလဲတရားေတာ္(၂) ၁၄-၁၁-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-BairThuAhDeatKaLair-D03-14-11-2007.mp4">ဘယ္သူအဓိကလဲတရားေတာ္(၃) ၁၄-၁၁-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-NgarLairTaNayt-D01-03-12-2007.mp4">ငါလည္းတေန႕တရားေတာ္(၁) ၃-၁၂-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-NgarLairTaNayt-D02-03-12-2007.mp4">ငါလည္းတေန႕တရားေတာ္(၂) ၃-၁၂-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-TaKalYownYiakLah-D01-20-12-2007.mp4">တကယ္ယုံရဲ႕လားတရာေတာ္(၁) ၂၀-၁၂-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-TaKalYownYiakLah-D02-20-12-2007.mp4">တကယ္ယုံရဲ႕လားတရာေတာ္(၂) ၂၀-၁၂-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-MaNaingChinParNatMaShoneChinParNat-D01-22-12-2007.mp4">မႏိုင္ခ်င္ပါနဲ႕တရားေတာ္ ၂၂-၁၂-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-BarNhatPuZawKyaMharLair-D01-25-10-2007.mp4">ဘာနဲ႕ပူေဇာ္ၾကမလဲတရားေတာ္(၁) ၂၅-၁၀-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-BarNhatPuZawKyaMharLair-D02-25-10-2007.mp4">ဘာနဲ႕ပူေဇာ္ၾကမလဲတရားေတာ္(၂) ၂၅-၁၀-၂၀၀၇</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-AhYeikPaMar-D01-07-01-2008.mp4">အရိပ္ပမာတရားေတာ္(၁) ၇-၁-၂၀၀၈</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-AhYeikPaMar-D02-07-01-2008.mp4">အရိပ္ပမာတရားေတာ္(၂) ၇-၁-၂၀၀၈</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-SaitSoTatSait-D01-12-01-2008.mp4">စိတ္ဆိုတဲ့စိတ္တရားေတာ္(၁) ၁၂-၁-၂၀၀၈</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-SaitSoTatSait-D02-12-01-2008.mp4">စိတ္ဆိုတဲ့စိတ္တရားေတာ္(၂) ၁၂-၁-၂၀၀၈</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
****dhamma talks uploaded and published on 21 Oct 2009****</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-PhoneKanSheatThuToatToatEatHtarNay-D01-30-3-2008.mp4">ဘုန္းကံရွိသူတို႕၏ ဌာေန 
(၁) ၃၀-၃-၂၀၀၈</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-PhoneKanSheatThuToatToatEatHtarNay-D02-30-3-2008.mp4">ဘုန္းကံရွိသူတို႕၏ ဌာေန 
(၂) ၃၀-၃-၂၀၀၈</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-MyanLayKongLay-D01-24-2-2008.mp4">ျမန္ေလ ေကာင္းေလ(၁) ၂၄-၂-၂၀၀၈</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-MyanLayKongLay-D02-24-2-2008.mp4">ျမန္ေလ ေကာင္းေလ(၂) ၂၄-၂-၂၀၀၈</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-SanMharLarSoneMharLar-D01-1-11-2007.mp4">ဆန္မွာလား ဆုန္မွာလား(၁)&nbsp; ၁-၁၁-၂၀၀၇</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-SanMharLarSoneMharLar-D02-1-11-2007.mp4">ဆန္မွာလား ဆုန္မွာလား(၂)&nbsp; ၁-၁၁-၂၀၀၇</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-TanPhoKyeeMarChayHlanMyar-29-12-2005Am.mp4">တန္ဖိုးႀကီးမား ေျခလွမ္းမ်ား အလုပ္ေပးတရား 
၂၉-၁၂-၂၀၀၅ နံနက္</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-ThawKaPhaySay-D01-8-11-2007.mp4">ေသာကေျဖေဆး တရားေတာ္(၁) ၈-၁၁-၂၀၀၇
</a> </font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-ThawKaPhaySay-D02-8-11-2007.mp4">ေသာကေျဖေဆး တရားေတာ္(၂) ၈-၁၁-၂၀၀၇
</a>
<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-YanThuAhSitBalMharLae-D01-2-11-2007.mp4">ရန္သူအစစ္ဘယ္မွာလဲ(၁) ၂-၁၁-၂၀၀၇</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DrAshinKawWiDa-YanThuAhSitBalMharLae-D02-2-11-2007.mp4">ရန္သူအစစ္ဘယ္မွာလဲ(၂) ၂-၁၁-၂၀၀၇</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
****dhamma talks uploaded and published on 19 Sep 2010****</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a name="new-released"></a></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 01</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/001-DrAshinKawWiDa-DVD01.mp4">၁။ အေမြခံထိုက္သူျဖစ္ပါေစ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/002-DrAshinKawWiDa-DVD01.mp4">၂။ အေမြခံထိုက္သူျဖစ္ပါေစ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/003-DrAshinKawWiDa-DVD01.mp4">၃။ အေမြခံထိုက္သူျဖစ္ပါေစ - ၃</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/004-DrAshinKawWiDa-DVD01.mp4">၄။ တို႕အားလုံးရဲ႕ဆရာ</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/005-DrAshinKawWiDa-DVD01.mp4">၅။ တကယ္ဝမ္ေျမာက္ႏိုင္ၿပီလား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/006-DrAshinKawWiDa-DVD01.mp4">၆။ တကယ္ဝမ္းေျမာက္ႏိုင္ၿပီလား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/007-DrAshinKawWiDa-DVD01.mp4">၇။ ေတာရွင္းတရားေတာ္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/008-DrAshinKawWiDa-DVD01.mp4">၈။ ေတာရွင္းတရားေတာ္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/009-DrAshinKawWiDa-DVD01.mp4">၉။ အခ်ိန္ႏွင့္ အလုပ္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/010-DrAshinKawWiDa-DVD01.mp4">၁၀။ အခ်ိန္ႏွင့္ အလုပ္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/011-DrAshinKawWiDa-DVD01.mp4">၁၁။ ေနာက္ဆုံးစကား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/012-DrAshinKawWiDa-DVD01.mp4">၁၂။ ေနာက္ဆုံးစကား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/013-DrAshinKawWiDa-DVD01.mp4">၁၃။ အခြင့္အေရး - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/014-DrAshinKawWiDa-DVD01.mp4">၁၄။ အခြင့္အေရး - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/015-DrAshinKawWiDa-DVD01.mp4">၁၅။ ခ်မ္းသာလမ္းညႊန္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/016-DrAshinKawWiDa-DVD01.mp4">၁၆။ ခ်မ္းသာလမ္းညႊန္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/017-DrAshinKawWiDa-DVD01.mp4">၁၇။ လည္လမ္းႏွင့္ လြတ္လမ္း - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/018-DrAshinKawWiDa-DVD01.mp4">၁၈။ လည္လမ္းႏွင့္ လြတ္လမ္း - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-01/019-DrAshinKawWiDa-DVD01.mp4">၁၉။ မႏိုင္ခ်င္ပါနဲ႔ မရႈံးခ်င္ပါနဲ႕</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 02</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/001-DrAshinKawWiDa-DVD02.mp4">၁။ ဘုရားႀကိဳက္ေအာင္ ပူေဇာ္ပါ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/002-DrAshinKawWiDa-DVD02.mp4">၂။ ဘုရားႀကိဳက္ေအာင္ ပူေဇာ္ပါ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/003-DrAshinKawWiDa-DVD02.mp4">၃။ အေမအိုရဲ႕ ဓမၼေအာင္လံ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/004-DrAshinKawWiDa-DVD02.mp4">၄။ အေမအိုရဲ႕ ဓမၼေအာင္လံ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/005-DrAshinKawWiDa-DVD02.mp4">၅။ ေနာင္တဆယ္ဆင့္ လြတ္ေအာင္က်င့္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/006-DrAshinKawWiDa-DVD02.mp4">၆။ ေနာင္တဆယ္ဆင့္ လြတ္ေအာင္က်င့္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/007-DrAshinKawWiDa-DVD02.mp4">၇။ ေနာင္တဆယ္ဆင့္ လြတ္ေအာင္က်င့္ - ၃</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/008-DrAshinKawWiDa-DVD02.mp4">၈။ ေနာင္တဆယ္ဆင့္ လြတ္ေအာင္က်င့္ - ၄</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/009-DrAshinKawWiDa-DVD02.mp4">၉။ အျမတ္ေလးပါး - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/010-DrAshinKawWiDa-DVD02.mp4">၁၀။ အျမတ္ေလးပါး - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/011-DrAshinKawWiDa-DVD02.mp4">၁၁။ သူေတာ္ေကာင္းတို႕ရဲ႕ မူငါးခ်က္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/012-DrAshinKawWiDa-DVD02.mp4">၁၂။ သူေတာ္ေကာင္းတို႕ရဲ႕ မူငါးခ်က္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/013-DrAshinKawWiDa-DVD02.mp4">၁၃။ မေမ့အပ္သူမ်ား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/014-DrAshinKawWiDa-DVD02.mp4">၁၄။ မေမ့အပ္သူမ်ား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/015-DrAshinKawWiDa-DVD02.mp4">၁၅။ ငါသည္႕တေန႕- ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/016-DrAshinKawWiDa-DVD02.mp4">၁၆။ ငါသည္႕တေန႕- ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/017-DrAshinKawWiDa-DVD02.mp4">၁၇။ အေၾကာင္းသုံးျဖာ ညီညြတ္ပါေစ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/018-DrAshinKawWiDa-DVD02.mp4">၁၈။ အေၾကာင္းသုံးျဖာ ညီညြတ္ပါေစ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/019-DrAshinKawWiDa-DVD02.mp4">၁၉။ မေမ့ပါနဲ႕ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/020-DrAshinKawWiDa-DVD02.mp4">၂၀။ မေမ့ပါနဲ႕ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-02/021-DrAshinKawWiDa-DVD02.mp4">၂၁။ သတိပ႒ာန္ စြမ္းရည္</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 03</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/001-DrAshinKawWiDa-DVD03.mp4">၁။ အဆိုးဆုံးေရာဂါ ကုစားပါ</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/002-DrAshinKawWiDa-DVD03.mp4">၂။ ဆန္မွာလား စုန္မွာလား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/003-DrAshinKawWiDa-DVD03.mp4">၃။ ဆန္မွာလား စုန္မွာလား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/004-DrAshinKawWiDa-DVD03.mp4">၄။ ျမင္တတ္ပါေစ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/005-DrAshinKawWiDa-DVD03.mp4">၅။ ျမင္တတ္ပါေစ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/006-DrAshinKawWiDa-DVD03.mp4">၆။ သူစိမ္းေတြမွ မဟုတ္ဘဲ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/007-DrAshinKawWiDa-DVD03.mp4">၇။ သူစိမ္းေတြမွ မဟုတ္ဘဲ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/008-DrAshinKawWiDa-DVD03.mp4">၈။ ရန္သူအစစ္ ဘယ္မွာလဲ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/009-DrAshinKawWiDa-DVD03.mp4">၉။ ရန္သူအစစ္ ဘယ္မွာလဲ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/010-DrAshinKawWiDa-DVD03.mp4">၁၀။ အာဇာနည္ ႏွလုံးသားပိုင္ရွင္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/011-DrAshinKawWiDa-DVD03.mp4">၁၁။ အာဇာနည္ ႏွလုံးသားပိုင္ရွင္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/012-DrAshinKawWiDa-DVD03.mp4">၁၂။ အတုနဲ႕ေပ်ာ္ေနသလား အစစ္နဲ႕ ေပ်ာ္ေနသလား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/013-DrAshinKawWiDa-DVD03.mp4">၁၃။ အတုနဲ႕ေပ်ာ္ေနသလား အစစ္နဲ႕ ေပ်ာ္ေနသလား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/014-DrAshinKawWiDa-DVD03.mp4">၁၄။ ဘာေတြျပင္ဆင္ၿပီးၿပီလဲ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/015-DrAshinKawWiDa-DVD03.mp4">၁၅။ ဘာေတြျပင္ဆင္ၿပီးၿပီလဲ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/016-DrAshinKawWiDa-DVD03.mp4">၁၆။ တကယ္ယုံရဲ႕လား</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/017-DrAshinKawWiDa-DVD03.mp4">၁၇။ ဘယ္သူ အဓိကလဲ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/018-DrAshinKawWiDa-DVD03.mp4">၁၈။ ဘယ္သူ အဓိကလဲ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/019-DrAshinKawWiDa-DVD03.mp4">၁၉။ ေလာကဓံေျဖေဆး - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-03/020-DrAshinKawWiDa-DVD03.mp4">၂၀။ ေလာကဓံေျဖေဆး - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 04</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/001-DrAshinKawWiDa-DVD04.mp4">၁။ လႈတတ္ပါေစ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/002-DrAshinKawWiDa-DVD04.mp4">၂။ လႈတတ္ပါေစ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/003-DrAshinKawWiDa-DVD04.mp4">၃။ ခ်စ္စရာ တိရိစာၦန္ ကေလးမ်ား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/004-DrAshinKawWiDa-DVD04.mp4">၄။ ခ်စ္စရာ တိရိစာၦန္ ကေလးမ်ား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/005-DrAshinKawWiDa-DVD04.mp4">၅။ ဂုဏ္အစစ္ကို ရေအာင္ရွာ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/006-DrAshinKawWiDa-DVD04.mp4">၆။ ဂုဏ္အစစ္ကို ရေအာင္ရွာ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/007-DrAshinKawWiDa-DVD04.mp4">၇။ စြမ္းအားထက္တဲ့ စာက်က္သံ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/008-DrAshinKawWiDa-DVD04.mp4">၈။ စြမ္းအားထက္တဲ့ စာက်က္သံ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/009-DrAshinKawWiDa-DVD04.mp4">၉။ ဆင္းရဲခပ္သိမ္း ကင္းၿငိမ္းပါေစ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/010-DrAshinKawWiDa-DVD04.mp4">၁၀။ ဆင္းရဲခပ္သိမ္း ကင္းၿငိမ္းပါေစ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/011-DrAshinKawWiDa-DVD04.mp4">၁၁။ ဘုန္ကံရွိသူတို႕ဌာေန - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/012-DrAshinKawWiDa-DVD04.mp4">၁၂။ ဘုန္ကံရွိသူတို႕ဌာေန - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/013-DrAshinKawWiDa-DVD04.mp4">၁၃။ ဝမ္းေျမာက္ပါေတာ့ ကုသိုလ္ရွင္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/014-DrAshinKawWiDa-DVD04.mp4">၁၄။ ဝမ္းေျမာက္ပါေတာ့ ကုသိုလ္ရွင္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/015-DrAshinKawWiDa-DVD04.mp4">၁၅။ ေရႊႏႈတ္ဖ်ားက ေရႊစကား - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/016-DrAshinKawWiDa-DVD04.mp4">၁၆။ ေရႊႏႈတ္ဖ်ားက ေရႊစကား - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/017-DrAshinKawWiDa-DVD04.mp4">၁၇။ သီလ တရားေတာ္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/018-DrAshinKawWiDa-DVD04.mp4">၁၈။ သီလ တရားေတာ္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/019-DrAshinKawWiDa-DVD04.mp4">၁၉။ သီလ တရားေတာ္ - ၃</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/020-DrAshinKawWiDa-DVD04.mp4">၂၀။ သူေတာ္ေကာင္းတို႕၏ ဂုဏ္ရည္ - ၁</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-04/021-DrAshinKawWiDa-DVD04.mp4">၂၁။ သူေတာ္ေကာင္းတို႕၏ ဂုဏ္ရည္ - ၂</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 05</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/001-DrAshinKawWiDa-DVD05.mp4">၁။ ျမင္တတ္ ၾကားတတ္ပါေစ&nbsp; ၃၁-၁၀-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/002-DrAshinKawWiDa-DVD05.mp4">၂။ ဘယ္လိုျပန္ၾကမလဲ&nbsp; ၅-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/003-DrAshinKawWiDa-DVD05.mp4">၃။ မွတ္တိုင္တစ္ခု စိုက္ထူႏိုင္ၿပီ&nbsp; ၁၅-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/004-DrAshinKawWiDa-DVD05.mp4">၄။ ေသမင္းႏွင့္ စစ္ခင္းခဲ့စဥ္က (၁)&nbsp; ၂၄-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/005-DrAshinKawWiDa-DVD05.mp4">၅။ ေသမင္းႏွင့္ စစ္ခင္းခဲ့စဥ္က (၂)&nbsp; ၂၅-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/006-DrAshinKawWiDa-DVD05.mp4">၆။ ကိုယ့္မွတ္တိုင္ ကိုယ္စစ္&nbsp; ၂၈-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/007-DrAshinKawWiDa-DVD05.mp4">၇။ ေနဖို႕လည္းျပင္၊ ေသဖို႔လည္းျပင္&nbsp; ၁-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/008-DrAshinKawWiDa-DVD05.mp4">၈။ မဟာဓမၼပါလဇတ္&nbsp; ၅-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-05/009-DrAshinKawWiDa-DVD05.mp4">၉။ သတၱိစြမ္းအား&nbsp; ၆-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">****dhamma talks uploaded and published on 
								6 Feb 2011****</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 07</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/001-DrAshinKawWiDa-DVD07.mp4">၁။ ျမင္တတ္ ၾကားတတ္ပါေစ&nbsp; ၃၁-၁၀-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/002-DrAshinKawWiDa-DVD07.mp4">၂။ ဘယ္လိုျပန္ၾကမလဲ&nbsp; ၅-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/003-DrAshinKawWiDa-DVD07.mp4">၃။ မွတ္တိုင္တစ္ခု စိုက္ႏိုင္ၿပီ&nbsp; ၁၅-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/004-DrAshinKawWiDa-DVD07.mp4">၄။ ေသမင္းႏွင့္ စစ္ခင္းခဲ့စဥ္က (၁)&nbsp; ၂၄-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/005-DrAshinKawWiDa-DVD07.mp4">၅။ ေသမင္းႏွင့္ စစ္ခင္းခဲ့စဥ္က (၂)&nbsp; ၂၅-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/006-DrAshinKawWiDa-DVD07.mp4">၆။ ကိုယ့္မွတ္တိုင္ ကိုယ္စစ္&nbsp; ၂၈-၁၁-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/007-DrAshinKawWiDa-DVD07.mp4">၇။ ေနဖို႕လဲျပင္ ေသဖို႕လဲျပင္&nbsp; ၁-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/008-DrAshinKawWiDa-DVD07.mp4">၈။ မဟာဓမၼပါလဇာတ္ တရားေတာ္&nbsp; ၅-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-07/009-DrAshinKawWiDa-DVD07.mp4">၉။ သတၱိစြမ္းအား&nbsp; ၆-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 08</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/001-DrAshinKawWiDa-DVD08-24-12-2009.mp4">၁။ ဓမၼစြမ္းအား&nbsp; ၂၄-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/002-DrAshinKawWiDa-DVD08-26-12-2009.mp4">၂။ ေျပးေနတာလား ရပ္ေနတာလား&nbsp; ၂၆-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/003-DrAshinKawWiDa-DVD08-29-12-2009.mp4">၃။ ေသရဲၿပီလား&nbsp; ၂၉-၁၂-၂၀၀၉</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/004-DrAshinKawWiDa-DVD08-5-1-2010.mp4">၄။ အေကာင္းဆုံးအခ်ိန္&nbsp; ၅-၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/005-DrAshinKawWiDa-DVD08-9-1-2010.mp4">၅။ အေကာင္းဆုံးအလုပ္&nbsp; ၉-၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/006-DrAshinKawWiDa-DVD08-15-1-2010.mp4">၆။ ျမင့္ၿပီးရင္ ျမတ္ပါေစ&nbsp; ၁၅-၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/007-DrAshinKawWiDa-DVD08-22-1-2010(A).mp4">၇။ ကိုယ့္စိတ္ကိုယ္စစ္ (ပ)&nbsp; ၂၂-၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/008-DrAshinKawWiDa-DVD08-22-1-2010(B).mp4">၈။ ကိုယ့္စိတ္ကိုယ္စစ္ (ဒု)&nbsp; ၂၂-၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/009-DrAshinKawWiDa-DVD08-24-1-2010.mp4">၉။ ညီမွ်ျခင္းျဖစ္ၿပီလား&nbsp; ၂၄-၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-08/010-DrAshinKawWiDa-DVD08-7-2-2010.mp4">၁၀။ ျမင့္ရာကေန ျမတ္ပါေစ&nbsp; ၇-၂-၂၀၁၀</a></font></p>
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
<font size="4">DVD 09</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/001-DrAshinKawWiDa-DVD09.mp4">၁။ ျမင့္ျမတ္စိတ္ထား ပိုင္ရွင္မ်ား&nbsp; ၆-၂-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/002-DrAshinKawWiDa-DVD09.mp4">၂။ တဏွာကင္းတဲ့ ခ်စ္ျခင္းေမတၱာ(ပ)&nbsp; ၁၉-၂-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/003-DrAshinKawWiDa-DVD09.mp4">၃။ တဏွာကင္းတဲ့ ခ်စ္ျခင္းေမတၱာ(ဒု)&nbsp; ၁၃-၃-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/004-DrAshinKawWiDa-DVD09.mp4">၄။ ဓမၼႏွင့္ ဘဝ (၁)&nbsp; ၁၃-၃-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/005-DrAshinKawWiDa-DVD09.mp4">၅။ ဓမၼႏွင့္ ဘဝ (၂)&nbsp; ၁၃-၃-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/006-DrAshinKawWiDa-DVD09.mp4">၆။ ဘဝထဲက ဓမၼ&nbsp; ၅-၄-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-09/007-DrAshinKawWiDa-DVD09.mp4">၇။ အတူတူပဲ ရပါတယ္&nbsp; ၁၀-၄-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 10</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-10/001-DrAshinKawWiDa-DVD10.mp4">၁။ တရားဘာေၾကာင့္ အားထုတ္မယ္&nbsp; ၈-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-10/002-DrAshinKawWiDa-DVD10.mp4">၂။ ကိုယ္ႏွင့္လိုက္တာ ကိုယ္ယူပါ&nbsp; ၉-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-10/003-DrAshinKawWiDa-DVD10.mp4">၃။ ရုပ္ နာမ္ ဆင္ျခင္ နိဗၺာန္ဝင္(၁)&nbsp; ၁၀-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-10/004-DrAshinKawWiDa-DVD10.mp4">၄။ ရုပ္ နာမ္ ဆင္ျခင္ နိဗၺာန္ဝင္(၂)&nbsp; ၁၀-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 11</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/001-DrAshinKawWiDa-DVD11.mp4">၁။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး (၁) ၁၁-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/002-DrAshinKawWiDa-DVD11.mp4">၂။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး (၂) ၁၂-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/003-DrAshinKawWiDa-DVD11.mp4">၃။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး (၃) ၁၃-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/004-DrAshinKawWiDa-DVD11.mp4">၄။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး (၄) ၁၄-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/005-DrAshinKawWiDa-DVD11.mp4">၅။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/006-DrAshinKawWiDa-DVD11.mp4">၆။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-11/007-DrAshinKawWiDa-DVD11.mp4">၇။ သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 12</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-12/001-DrAshinKawWiDa-DVD12.mp4">၁။ အခ်ိန္ေကာင္း&nbsp; ၁၁-၁၁-၂၀၁၀&nbsp; ေစ်းခ်ိဳေတာ္၊ မႏ ၱေလး</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-12/002-DrAshinKawWiDa-DVD12.mp4">၂။ ဝမ္းေျမာက္ျခင္းေတြ ဆက္ပါေစ&nbsp; ၁၄-၁၁-၂၀၁၀&nbsp; 
ေညာင္ဦးေက်ာင္း၊ ရန္ကုန္</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-12/003-DrAshinKawWiDa-DVD12.mp4">၃။ ဘဝထဲမွာ ဓမၼေတြပါ&nbsp; ၂၂-၁၁-၂၀၁၀&nbsp; ေက်ာက္ဆည္ၿမိဳ႕</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/old/DVD-12/004-DrAshinKawWiDa-DVD12.mp4">၄။ ကိုယ္ႏွင္လိုက္တာ ကိုယ္တြဲပါ&nbsp; ၂၃-၁၁-၂၀၁၀&nbsp; 
ေက်ာက္ဆည္ၿမိဳ႕</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၁။ ဘဝထဲမွာ ဓမၼတြဲပါ</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၂။ ကိုယ္ႏွင့္လိုက္တာ ကိုယ္တြဲပါ</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၃။။ အတြဲလဲမွန္ ဇြဲလဲသန္</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၄။ သူမလာခင္ ႀကိဳတင္ျပင္ဆင္</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၅။ အညွာခိုင္ဖို႕ လိုပါတယ္</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၆။ </font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">****************************************</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD အမွတ္စဥ္ (၉)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/01-DrAshinKawWiDa-DVD09.mp4">၀၀၁. တရားဘာေၾကာင္႔အားထုတ္မယ္ (၀၈-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/02-DrAshinKawWiDa-DVD09.mp4">၀၀၂. ကိုယ္နဲ႔လိုက္တာ ကိုယ္ယူပါ (၀၉-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/03-DrAshinKawWiDa-DVD09.mp4">၀၀၃. ရုပ္နာမ္ဆင္ျခင္ နိဗၺာန္၀င္ (၁၀-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/04-DrAshinKawWiDa-DVD09.mp4">၀၀၄. သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး(၁) (၁၁-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/05-DrAshinKawWiDa-DVD09.mp4">၀၀၅. သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး(၂) (၁၂-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/06-DrAshinKawWiDa-DVD09.mp4">၀၀၆. သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး(၃) (၁၃-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-09/07-DrAshinKawWiDa-DVD09.mp4">၀၀၇. သတိပ႒ာန္အက်ဳိး ခ်စ္ျမတ္ႏိုး(၄) (၁၄-၁၀-၂၀၁၀ - ကံျမင္႔)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၀)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-10/01-DrAshinKawWiDa-DVD10.mp4">၀၀၁. ဘ၀ထဲမွာ ဓမၼတြဲပါ (၂၂-၁၁-၂၀၁၀ - ေက်ာက္ဆည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-10/02-DrAshinKawWiDa-DVD10.mp4">၀၀၂. ကိုယ္နဲ႔လိုက္တာ ကိုယ္တြဲပါ (၂၃-၁၁-၂၀၁၀ - ေက်ာက္ဆည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-10/03-DrAshinKawWiDa-DVD10.mp4">၀၀၃. အခ်ိန္ေကာင္း (၁၁.၁၁.၂၀၁၀ - မႏၱေလး )</a><br>
၀၀၄. ၀မ္းေျမာက္ျခင္းေတြဆက္ပါေစ (၁၄-၁၁-၂၀၁၀ - ရန္ကုန္)<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၁)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-11/01-DrAshinKawWiDa-DVD11.mp4">၀၀၁. ၀ိပႆနာအက်ဳိး ခ်စ္ျမတ္ႏိုး (၁) (ေျမာက္ဥကၠလာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-11/02-DrAshinKawWiDa-DVD11.mp4">၀၀၂. ၀ိပႆနာအက်ဳိး ခ်စ္ျမတ္ႏိုး (၂) (ေျမာက္ဥကၠလာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-11/03-DrAshinKawWiDa-DVD11.mp4">၀၀၃. အတြဲလဲမွန္၊ ဇြဲလဲသန္ (၁) (ဘားအံ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-11/04-DrAshinKawWiDa-DVD11.mp4">၀၀၄. အတြဲလဲမွန္၊ ဇြဲလဲသန္ (၂) (ဘားအံ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-11/05-DrAshinKawWiDa-DVD11.mp4">၀၀၅. အခါမလင္႔ (မဟာစည္ သာသနာ႔ရိပ္သာ )</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-11/06-DrAshinKawWiDa-DVD11.mp4">၀၀၆. မိတ္ေဆြေကာာင္း (ကမာရြတ္)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၂)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-12/01-DrAshinKawWiDa-DVD12.mp4">၀၀၁. ပရိတ္၊ ပ႒ာန္းေဒသနာႏွင္႔ သတိ၊ အခ်ိန္တိုင္း သၾကၤန္က်ေနသည္</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၃)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-13/01-DrAshinKawWiDa-DVD13.mp4">၀၀၁. ေရွးေရွးတုန္းကမဂၤလာ (၁) (မတၱရာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-13/02-DrAshinKawWiDa-DVD13.mp4">၀၀၂. ေရွးေရွးတုန္းကမဂၤလာ (၂) (မတၱရာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-13/03-DrAshinKawWiDa-DVD13.mp4">၀၀၃. ေရွးေရွးတုန္းကမဂၤလာ (၃) (မတၱရာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-13/04-DrAshinKawWiDa-DVD13.mp4">၀၀၄. ေရွးေရွးတုန္းကမဂၤလာ (၄) (မတၱရာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-13/05-DrAshinKawWiDa-DVD13.mp4">၀၀၅. ေရွးေရွးတုန္းကမဂၤလာ (၅) (မတၱရာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-13/06-DrAshinKawWiDa-DVD13.mp4">၀၀၆. ေရွးေရွးတုန္းကမဂၤလာ (၆) (မတၱရာ)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<br>
DVD အမွတ္စဥ္ (၁၄)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-14/01-DrAshinKawWiDa-DVD14.mp4">၀၀၁. အေကာင္းဆံုးအေဖၚ (၁၇-၀၂-၂၀၁၁ - သာမည)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-14/02-DrAshinKawWiDa-DVD14.mp4">၀၀၂. အေဖၚေကာင္း (၁၇-၀၁-၂၀၁၁ - ၄၆လမ္း၊ ရန္ကုန္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-14/03-DrAshinKawWiDa-DVD14.mp4">၀၀၃. အမွီေကာင္းေလးရွာထားပါ (၁၄-၀၅-၂၀၁၁ - ဗဟန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-14/04-DrAshinKawWiDa-DVD14.mp4">၀၀၄. ဘ၀ႏွင္႔ဓမၼ (၀၆-၀၄-၂၀၁၁ - ဗဟန္း)</a><br>
<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
အမွတ္စဥ္(၁၅)<br>
"အရွက္မွန္၊ အေၾကာက္မွန္"</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-15/01-DrAshinKawWiDa-DVD15.mp4">၁။ ေအာင္ျမင္ၾကီးပြါး ေသာ့ခ်က္မ်ား (၄-၉-၂၀၁၁၊ သကၤန္းကြၽန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-15/02-DrAshinKawWiDa-DVD15.mp4">၂။ သူ႕လိုေတြးပါ (၁၉-၉-၂၀၁၁၊ မႏၲေလး)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-15/03-DrAshinKawWiDa-DVD15.mp4">၃။ အရွက္မွန္၊ အေၾကာက္မွန္ (၂၀-၉-၂၀၁၁၊ မႏၲေလး)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-15/04-DrAshinKawWiDa-DVD15.mp4">၄။ အမွီေကာင္းေလးရွာထားပါ (၂၀-၉-၂၀၁၁၊ မႏၲေလး)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-15/05-DrAshinKawWiDa-DVD15.mp4">၅။ ထၾက၊ထၾက (၂၁-၉-၂၀၁၁၊ မႏၲေလး)</a><br>
<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
အမွတ္စဥ္(၁၆)<br>
"သူ႕လိုေတြးပါ"</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-16/01-DrAshinKawWiDa-DVD16.mp4">၁။ ငါလဲတစ္ေန႕ (၅-၁၁-၂၀၁၁၊ ေက်ာက္ဆည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-16/02-DrAshinKawWiDa-DVD16.mp4">၂။ မိဘဂုဏ္ရည္(၁) (၆-၁၁-၂၀၁၁၊ ေက်ာက္ဆည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-16/03-DrAshinKawWiDa-DVD16.mp4">၃။ မိဘဂုဏ္ရည္(၂) (၇-၁၁-၂၀၁၁၊ ေက်ာက္ဆည္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-16/04-DrAshinKawWiDa-DVD16.mp4">၄။ ဩကာသရွင္းတမ္းႏွင့္ သီလယူ ရွင္းတမ္း (၁၄-၁၁-၂၀၁၁၊ လသာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-16/05-DrAshinKawWiDa-DVD16.mp4">၅။ သူ႕လိုေတြးပါ (၂၇-၁၀-၂၀၁၁၊ လိႈင္)</a><br>
<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၁၇)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-17/01-DrAshinKawWiDa-DVD17.mp4">
၁။ ခြဲၾကရတဲ့အခါ&nbsp; (၃၀.၅.၂၀၁၁- ဘားအံ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-17/02-DrAshinKawWiDa-DVD17.mp4">
၂။ ကထိန္အလွူေတာ္ မဂၤလာ&nbsp; (၂၀.၁၁.၂၀၁၁- မႏ ၱေလး)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-17/03-DrAshinKawWiDa-DVD17.mp4">
၃။ ခ်မ္းသာရွင္းတမ္း&nbsp; (၂၉.၁၁.၂၀၁၁-မႏ ၱေလး)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-17/04-DrAshinKawWiDa-DVD17.mp4">
၄။ ဓါတ္ခံ&nbsp; (၁၀.၁.၂၀၁၂-ရန္ကုန္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-17/05-DrAshinKawWiDa-DVD17.mp4">
၅။ ခ်စ္သက္ေသေတြ ထူနိုင္ပါေစ (၁၄.၁.၂၀၁၂-ပဲခူး)</a><br>
<br>
<br>
<br>
အမွတ္စဥ္ (၁၈)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-18/01-DrAshinKawWiDa-DVD18.mp4">
၁။ သူ့လို အေတြး (၂၃.၃.၂၀၁၂-ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-18/02-DrAshinKawWiDa-DVD18.mp4">
၂။ ေျဖေဆး (၄.၄.၂၀၁၂-ေမွာ္ဘီ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-18/03-DrAshinKawWiDa-DVD18.mp4">
၃။ မဂၤလာအေပါင္းနဲ့ ျပည့္စံုၾကပါေစ (၂၀.၄.၂၀၁၂- စမ္းေခ်ာင္း)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">****dhamma talks uploaded and published on 
								29 March 2013 ****</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၁၉)<br>
<br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-19/01-DrAshinKawWiDa-DVD19.mp4">၁။ ဘ၀ရထား မနားေသးခင္ (၁.၁၀.၂၀၁၂ - ကံျမင့္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-19/02-DrAshinKawWiDa-DVD19.mp4">၂။ ျဖတ္လမ္း (၁) (၂.၁၀.၂၀၁၂ - ကံျမင့္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-19/03-DrAshinKawWiDa-DVD19.mp4">
၃။ ျဖတ္လမ္း (၁) (၃.၁၀.၂၀၁၂ - ကံျမင့္)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
အမွတ္စဥ္ (၂၀)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-20/01-DrAshinKawWiDa-DVD20.mp4">၁။ ကာလရထား (၁၀.၅.၂၀၁၂ - သာေကတ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-20/02-DrAshinKawWiDa-DVD20.mp4">၂။ ဘ၀ရထား မနားေသးခင္ (၂၀.၁၀.၂၀၁၂ - ရန္ကင္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-20/03-DrAshinKawWiDa-DVD20.mp4">၃။ လိမ္ေနတယ္ သတိထား (၁.၁၁.၂၀၁၂ - က်ိဳကၠဆံ)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
အမွတ္စဥ္ (၂၁)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-21/01-DrAshinKawWiDa-DVD21.mp4">၁။ ခြဲၾကရတဲ႔အခါ (၅.၁၁.၂၀၁၂ - မိတၳီလာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-21/02-DrAshinKawWiDa-DVD21.mp4">၂။ လိမ္ေနတယ္ သတိထား (၆.၁၁.၂၀၁၂ - မိတၳီလာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-21/03-DrAshinKawWiDa-DVD21.mp4">၃။ ခ်မ္းသာဆိုတာ ဘယ္ဟာလဲ (၇.၁၁.၂၀၁၂ - မိတၳီလာ)</a><br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
အမွတ္စဥ္ (၂၃)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-23/01-DrAshinKawWiDa-DVD23.mp4">၁။ သီလယူပံု႐ွင္းတမ္း (၂၆.၁၂.၂၀၁၂ - လသာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-23/02-DrAshinKawWiDa-DVD23.mp4">၂။ ေစ်းသည္ (၂၇.၁၂.၂၀၁၂ - လသာ)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-23/03-DrAshinKawWiDa-DVD23.mp4">၃။ ေလးမ်ိဳးစံုလင္ ျပဳေစခ်င္ (၂၃.၁၀.၂၀၁၂ - မရမ္းကုန္း)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-23/04-DrAshinKawWiDa-DVD23.mp4">
၄။ ဘ၀ရထား (၁၉.၁၂.၂၀၁၂ - လမ္းမေတာ္)</a><br>
<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၂၄)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-24/DVD-24-Title-01-2-DrAshinKawWiDa.mp4">၁။ ကံစြမ္းအား တရားေတာ္ (မြန္ျပည္နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-24/DVD-24-Title-02-DrAshinKawWiDa.mp4">၂။ ဂုဏ္ေတာ္စြမ္းအား တရားေတာ္ (မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-24/DVD-24-Title-03-DrAshinKawWiDa.mp4">၃။ ေယာဂီျပည္႕စုံရမည္႕ အဂၤ ါ (၅)ပါး (မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-24/DVD-24-Title-04-DrAshinKawWiDa.mp4">၄။ စကားေျပာလွ်င္ သတိယွဥ္ (မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၂၅)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-25/DVD-25-Title-01-DrAshinKawWiDa.mp4">၁။ ေလးမ်ိဳးစုံလင္ ျပဳေစခ်င္ (မရမ္းကုန္း)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-25/DVD-25-Title-02-DrAshinKawWiDa.mp4">၂။ မငိုပါနဲက တရားေတာ္ (ပဲခူး)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-25/DVD-25-Title-03-DrAshinKawWiDa.mp4">၃။ အားကိုးရာ ဘယ္မွာလဲ (မဟာစည္သာသနာ့ရိပ္သာ)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၂၆)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-26/DVD-26-Title-01-DrAshinKawWiDa.mp4">၁။ ဂုဏ္အစစ္ကိုၿပိဳင္</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၂။ ကိုယ္ကအၿမဲ ႏိုင္ပါေစ (မႏ ၱေလးၿမိဳ႕)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၃။ ရုန္းထြက္ႏိုင္ပါေစ (ေက်ာက္ဆည္)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၄။ ဒီအတိုင္းပဲ ဆက္သြားမွာလား (လသာၿမိဳ႕)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">၅။ ကထိန္အႏုေမယဒနာ (ရန္ကုန္)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၂၇)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-27/DVD-27-Title-01-DrAshinKawWiDa.mp4">၁။ ႏွစ္ပြင့္ပန္ရင္ ပိုလွမယ္ (မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-27/DVD-27-Title-02-DrAshinKawWiDa.mp4">၂။ အနာနဲ႕ေဆး တည္႕ေအာင္ေရြးပါ (မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-27/DVD-27-Title-03-DrAshinKawWiDa.mp4">၃။ ခြဲၾကရတဲ့အခါ (မႏ ၱေလးၿမိဳ႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-27/DVD-27-Title-04-DrAshinKawWiDa.mp4">၄။ အဆိုးဆုံးေရာဂါ (စမ္းေခ်ာင္းၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၂၈)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-28/DVD28-Title-01-DrAshinKawWiDa.mp4">
၁။ အထင္မေသးလိုက္ပါနဲ႕ (မဟာစည္သာသနာ့ရိပ္သာ)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-28/DVD28-Title-02-DrAshinKawWiDa.mp4">
၂။ ကံအလွည္႕ေလး ေစာင့္ေပးပါ (လႈိင္သာယာၿမိဳ႕နယ္)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-28/DVD28-Title-03-DrAshinKawWiDa.mp4">
၃။ ၿပဳံးၿပဳံေလးနဲ႕ ထြက္ႏိုင္ပါေစ (မဂၤလာေတာင္ညြန္႕)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">အမွတ္စဥ္ (၂၉)</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-29/DVD29-Title-01-DrAshinKawWiDa.mp4">
၁။ အထင္မေသးလိုက္ပါနဲ႕</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-29/DVD29-Title-02-DrAshinKawWiDa.mp4">
၂။ ျပန္လာလိမ့္မယ္ သတိထား (၂၉-၉-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-29/DVD29-Title-03-DrAshinKawWiDa.mp4">
၃။ ခဏ ခဏ ျပဴေပးၾက (၃၁-၉-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-29/DVD29-Title-04-DrAshinKawWiDa.mp4">
၄။ ကံအလွည္႕ေလးေစာင့္ေပးပါ (၁-၁၀-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-29/DVD29-Title-05-DrAshinKawWiDa.mp4">
၅။ ကိုယ့္လမ္းေလးလဲျပင္ၾကပါ (၂-၁၁-၂၀၁၄)</a></font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/Dr-Ashin-Kaw-Wi-Da/DVD-29/DVD29-Title-06-DrAshinKawWiDa.mp4">
၆။ ေဒါက္တာေကဝိဒ၏ မယ္ေတာ္ႀကီး ေဒၚေအးရီ အသက္၈၀ႏွစ္ျပည္႕ 
ဝိဇၾတပူဇာေမြးေန႕မဂၤလာအလွဴေတာ္</a></font></p>
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
<br>
<br>
&nbsp;</font></p>
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
        #print(key)
        if key.get('href') != None:
            print(key.get('href'))
            if ".mp4" in key.get('href'):
                counter = '{:03d}'.format(count)
                print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
                f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
                #print(key.get_text())

                count += 1
        ''''
        try:
            if not ".mp4" in key.get('href'):   
                print(key)
        except TypeError as err:
                print(err)
        '''
        '''
        if ".mp4" in key.get('href'):
            counter = '{:03d}'.format(count)
            print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())

            count += 1
        '''
    ''''
    try:
        for key in soup.find_all('a'):
            if ".mp4" in key.get('href'):
                counter = '{:03d}'.format(count)
                print('{}.mp4|{}|{}'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
                f.write('{}.mp4|{}|{}\n'.format(counter, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
                #print(key.get_text())

                count += 1
    except (TypeError,) as err:
        print(err)
    '''
    
