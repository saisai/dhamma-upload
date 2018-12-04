from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">












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













<!-- Start dhammadownload menu top and side bar -->

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
    <img src="images/Top-button-wt.gif" width="680" height="132" border="0">
</div>

<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 31px;" id="layer22" align="center">
    <font color="#800080"><span style="font-size: 30pt">ဘဒၵႏ ၱတိေလာကာဘိဝံသ</span></font></div>

<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 596px; top: 4px;" id="layer23">
    <img src="images/Bhaddanta-Tilokarbhivamsa.gif" width="180" height="206" border="0">
</div>



<!-- Start dhammadownload menu top and side bar -->




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





















<div style="position: absolute; width: 1091px; height: 10865px; z-index: 21; left: 231px; top: 200px" id="layer24" font="" face="Zawgyi-One"><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="6">ဘဒၵႏ ၱတိေလာကာဘိဝံသ</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
	<br>
	<font size="4">အဂၢမဟာပ႑ိတ<br>
	ႏိုင္ငံေတာ္သံဃမဟာနာယကအဖြဲ႕ ဒုတိယဥကၠ႒<br>
	အင္းစိန္ရြာမ ပရိယတၱိစာသင္တိုက္<br>
	လက္ရွိ ပဓာန မဟာနာယကဆရာေတာ္ </font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
***************************************************************************************************</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
ဆရာေတာ္ အရွင္တိေလာကာဘိ၀ံသ၏ ေထရုပၸတိၱအက်ဥ္း</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<br>
<font size="2">ဖြားျမင္ေတာ္မူျခင္း<br>
ဆရာေတာ္ဘဒၵႏ ၱတိေလာကာဘိ၀ံသသည္ ဧရာ၀တီတိုင္း၊ ဇလြန္ၿမိဳ႕နယ္၊ ေညာင္ပင္သာရြာ၊ 
ခမည္းေတာ္ ဦးဘေဖ+မယ္ေတာ္ ေဒၚေစာစိန္ တို႔မွ ၁၃၀၀ ျပည့္ႏွစ္၊ တေပါင္းလဆန္း၁-ရက္၊ 
စေနေန႔နံနက္ ၄နာရီအခ်ိန္တြင္ ဖြားျမင္ေသာ စတုတၳေျမာက္ သားရတနာျဖစ္ပါသည္။<br>
<br>
ရွင္ ရဟန္းအျဖစ္သို႔ ေရာက္ရွိေတာ္မူျခင္း<br>
ဆရာေတာ္ေလာင္းလ်ာသည္ ၆ ႏွစ္သားအရြယ္တြင္ တစ္ႀကိမ္၊ ၁၅ ႏွစ္သားအရြယ္တြင္တစ္ႀကိမ္၊ 
ဇလြန္ၿမိဳ႕နယ္၊ ေညာင္ပင္သာေက်ာင္း ဆရာေတာ္ ဘဒၵႏ ၱဣႏၵ၀ံသကို ဥပဇၥ်ာယ္ျပဳ၍ 
ခမည္းေတာ္+မယ္ေတာ္တို႔၏ ပစၥာယာႏုဂၢဟ ကိုခံယူကာ ရွင္သာမေဏ အျဖစ္သို႔ 
ေရာက္ရွိေတာ္မူခဲ့ပါသည္၊ ဘြဲ႕ေတာ္မွာရွင္တိေလာက ျဖစ္ပါ သည္။ ၁၃၂၀ ခုႏွစ္၊ 
ကဆုန္လဆန္း ၁၀ရက္၊ တနဂၤေႏြေန႕ သက္ေတာ္ ၂၀ အရြယ္တြင္ ဇလြန္ၿမိဳ႕နယ္၊ ပကြဲ 
ေက်ာင္းေဟာင္းဆရာေတာ္ ဘဒၵႏ ၱစႏၵာ၀ရကို ဥပဇၥၥၥၥ်ာယ္ျပဳ၍ ေညာင္ပင္သာေက်းရြာေန 
ေနာင္ေတာ္ျဖစ္သူ ဦးမ်က္ျပဴး + ေဒၚသိန္းရင္ တို႕၏ ပစၥယာႏုဂၢဟကိုခံယူကာ 
ေညာင္ပင္သာေက်ာင္း ခ႑သိမ္ေတာ္၌ ျမင့္ျမတ္ေသာ ရဟန္းအျဖစ္သို႕ 
ေရာက္ရွိေတာ္မူခဲ့ပါသည္။<br>
<br>
စာေပပရိယတၱိ သင္ၾကားဆည္းပူးေတာ္မူျခင္း<br>
ဆရာေတာ္ေလာင္းလ်ာသည္ ေညာင္ပင္သာရြာဦးေက်ာင္းဆရာေတာ္ ႏွင့္ေညာင္ဦးၿမိဳ႕နယ္၊ 
ကံႀကီးကုန္းရြာ ေတာင္ေက်ာင္းဆရာေတာ္ ဦး၀ါသ၀ တို႔ထံတြင္ အေျခခံမွစ၍ ပိဋကတ္က်မ္းစာ 
မ်ားကိုသင္ယူဆည္းပူးေတာ္ မူခဲ့ၿပီး ၁၃၁၇ ခုႏွစ္တြင္ ျမင္းၿခံၿမိဳ႕၊ 
ကိုးေဆာင္တိုက္ဆရာေတာ္ အဘိဓဇမဟာရ႒ဂုရု ၊ အဘိဓဇအဂၢမဟာသဒၵမၼ<br>
ေဇာတိကဓဇ၊ ႏိုင္ငံေတာ္သံဃမဟာနာယကအဖြဲ႕ ဥကၠ႒ ဘဒၵႏ ၱေသာဘိတထံတြင္ မူလတန္းမွ၊ အစိုးရ 
ဓမၼာစရိယ ၿပီးသည့္တိုင္ေအာင္ ၉ႏွစ္ခန္႕ ပိဋကတ္က်မ္းစာမ်ားကို 
သင္ယူဆည္းပူးေတာ္မူခဲ့ပါသည္။ ထို႕ေနာက္ မႏၱေလးၿမိဳ႕၊ ခ်မ္းသာႀကီးတိုက္၊ 
ေညာင္ကန္တိုက္၊ ရန္ကုန္ၿမိဳ႕ေျခာက္ထပ္ႀကီးတိုက္တို႕တြင္ လွည့္လည္ သီတင္း သံုးလ်က္ 
စာခ်အေက်ာ္ ဆရာေတာ္မ်ားထံတြင္ ပရိယတၱိစာေပမ်ားကိုု ေလ့လာသင္ယူေတာ္မူခဲ့ပါသည္။<br>
<br>
ေအာင္ျမင္ေတာ္မူခဲ့ေသာ စာေမးပြဲမ်ား<br>
ႏိုင္ငံေတာ္အစိုးရ အဘိဓမၼာစာေမးပြဲ ပထမ၊ ဒုတိယ၊ တတိယ - ၃ဆင့္၊ ဋီကာေက်ာ္ 
ဂုဏ္ထူးေဆာင္ ပထမ၊ ဒုတိယ၊ တတိယ - ၃ဆင့္၊ ဇလြန္ၿမိဳ႕နယ္ လယ္ဦးေက်ာင္း၌ က်င္းပေသာ 
၀ိနယ မူလတန္းႏွင့္ ၀ိနယႏ ၱရိက သၿဂၤ ိဳဟ္တန္း၊ ျမင္းၿခံၿမိဳ႕၊ ကိုးေဆာင္တိုက္ 
သဒၶမပါလ စာေမးပြဲ ပထမငယ္၊ ပထမလတ္၊ ပထမႀကီး၊ စာခ်တန္း၊ ႏိုင္ငံေတာ္အစိုးရ ပထမငယ္၊ 
ပထမလတ္၊ ပထမႀကီး၊ သာသနဓဇဓမၼာစရိယ (တစ္ႏိုင္ငံလံုး ဒုတိယ) သာသနဓဇ သိရီပ၀ရ ဓမၼာစရိယ 
(ပဋိသမၻိဒါမဂ္ျမန္မာဂုဏ္ထူး) မႏ ၱေလး သက်သီဟ စာသင္တန္း၊ ဓမၼာစရိယ တန္း တို႕ကို 
ေအာင္ျမင္ေတာ္မူခဲ့ပါသည္။<br>
<br>
စာေပက်မ္းဂန္သင္ၾကားပို႕ခ်ေတာ္မူျခင္း<br>
ေညာင္ဦးၿမိဳ႕နယ္၊ ကံႀကီးကုန္းရြာ၌၁၃၂၈-၂၉ခုႏွစ္တြင္ ဘကမူလတန္း ဆရာအျဖစ္ 
လည္းေကာင္း၊ ျမင္းၿခံၿမိဳ႕၊ ကိုးေဆာင္တိုက္၌ ၁၃၂၉ ခုႏွစ္တြင္ စာခ်ဂဏ၀ါစကအျဖစ္ 
လည္းေကာင္း၊ အင္းစိန္ၿမိဳ႕ရြာမပရိယတၱိစာသင္ တိုက္၌ ၁၃၃၂ခုႏွစ္မွ ယေန႔တိုင္ေအာင္ 
တာ၀န္ခံစာခ်အျဖစ္လည္းေကာင္း၊ စာေပပရိယတၱိမ်ားကိုု ပို႔ခ်ေတာ္မူခဲ့ ပါသည္။ 
ႏိုင္ငံေတာ္ ပရိယတၱိသာသနာ့တကၠသိုလ္(ရန္ကုန္) စတင္ဖြင့္လွစ္ခ်ိန္မွစ၍ ၁၃၅၀ ခုႏွစ္အထိ 
၄ႏွစ္ခန္႕ အဘိဓမၼမဟာဌာန နာယက (ပါေမာကၡ) ၊ ဒုတိယနာယကခ်ဳပ္(ဒုတိယပါေမာကၡခ်ဳပ္) 
အျဖစ္တာ၀န္ယူ၍ စာေပ က်မ္းဂန္မ်ားကို သင္ၾကားပို႔ခ်ေတာ္မူခဲ့ပါသည္။<br>
<br>
ေရးသားျပဳစုေသာ က်မ္းစာမ်ား<br>
စာေပပရိယတ္ ပို႔ခ်ေတာ္မူရင္း စာသင္သားမ်ားႏွင့္ သုေတသီတို႔အတြက္ က်မ္းဂန္မ်ား 
ျပဳစုေရးသားခဲ့သည္၊ ယင္းက်မ္းစာမ်ားမွာ-<br>
(က)အေျဖစံု ၇က်မ္း (စနစ္ေဟာင္းငယ္၊လတ္၊ႀကီး အေျဖစံု ၃ က်မ္း၊ စနစ္သစ္မူလ၊ ငယ္၊ လတ္၊ 
ႀကီး အေျဖစံု ၄ က်မ္း) ၊<br>
(ခ) လက္ေဆာင္က်မ္း ၁၁ က်မ္း (မာတိကာဓာတုကထာ လက္ေဆာင္၊ ယမက လက္ေဆာင္ ၂ က်မ္း၊ 
ပ႒ာန္းလက္ေဆာင္၊ ပ႒ာန္းပို႔ခ်စဥ္လက္ေဆာင္၊ အဘိဓမၼာလက္ေဆာင္၊ ဆန္းလက္ ေဆာင္၊ 
ပါဠိသဒၵါအသံုးအႏူန္းႏွင့္ ပါဠိစာေပ ေကာက္ႏူတ္ခ်က္လက္ေဆာင္၊ သဒၵါလက္ေဆာင္၊ 
သုတ္နက္လက္ ေဆာင္၊ သဒၵါႀကီးနိႆယလက္ေဆာင္)။<br>
(ဂ) ဗဟုသုတပညာေပး ၆က်မ္း (ရဟန္းခံရွင္ျပဳအေၾကာင္း၊ 
ကိုးကြယ္မႈဆိုင္ရာသိစရာႏွင့္ဗုဒၶသာသနာ့သမိုင္း၊ ေစတီပုထိုး၊ မဲလံဆံေတာ္ရွင္၊ 
သက်မုနိ၊ လက္ေရြးစင္ ေဆာင္းပါးမ်ား၊ ပရိတ္ +ဂါထာ+ မႏ ၱန္စေသာ ပံုႏွိပ္ၿပီး 
က်မ္းေပါင္း ၂၄က်မ္း ႏွင့္ ဂႏၳာဘရဏႏွင့္ ဘုရားႀကီးနိယံလက္ေဆာင္၊ အ႒သာလိနီ 
အေျဖစံုစေသာ ပံုမႏွိပ္ ရေသးသည့္ က်မ္းမ်ားကို ေရးသားျပဳစုေတာ္မူခဲ့ပါသည္၊<br>
ယခု ေနာက္ဆုံး ေရးသားခဲ့သည္မွာ ျမန္မာ့သာသနာ့သမိုင္းတြင္ အထင္ကရအေနျဖင့္ 
သမိုင္းတြင္က်န္ရစ္မည့္ ပါဠိဘာသာျဖင့္ ေရးသားခဲ့သည့္ ပရိတ္ႀကီးဋီကာသစ္ေခၚ 
ပရိတၱအဘိန၀ဋီကာက်မ္းႏွင့္ အဂၤုတၱိဳရ္ပါဠိေတာ္ ျမန္မာျပန္သစ္က်မ္းမ်ား ျဖစ္ပါသည္။<br>
<br>
သာသနာေရး အားေပးေဆာင္ရြက္ေတာ္မူျခင္း<br>
ဂိုဏ္းေပါင္းစံု သံဃအဖြဲ႕အစည္း ပထမအႀကိမ္ ၿမိဳ႕နယ္ႏွင့္တိုင္း ၀ိနည္းဓိုရ္၊ 
ဒုတိယအႀကိမ္ အင္းစိန္ၿမိဳ႕နယ္ သံဃနာယကအဖြဲ႕ ဒုတိယဥကၠ႒၊ တတိယအႀကိမ္ ႏိုင္ငံေတာ္ဗဟို 
သံဃာ့၀န္ေဆာင္ႏွင့္ ေတာင္တန္း သာသနာျပဳ ၾသ၀ါဒါစရိယ၊ အင္းစိန္ၿမိဳ႕နယ္ 
ပထမျပန္စာေမးပြဲႀကီးၾကပ္ေရးေကာ္မတီ ဥကၠ႒၊ ႏိုင္ငံေတာ္ ပရိယတၱိသာသနာ့တကၠသိုလ္ 
(ရန္ကုုန္) အဘိဓမၼပါေမာကၡ၊ ဒုတိယနာယကခ်ဳပ္ (ဒုတိယပါေမာကၡခ်ဳပ္) ၊ ပဥၥမအႀကိမ္ 
ႏိုင္ငံေတာ္ သံဃာ့မဟာနာယက၊ ဆ႒မအႀကိမ္ ႏိုင္ငံေတာ္သံဃမဟာနာယက တြဲဖက္အက်ိဳးေတာ္ 
ေဆာင္၊ ႏိုင္ငံေတာ္သံဃမဟာနာယက ဒုတိယ ဥကၠ႒၊ အဘိဓမၼာ ျပန္႕ပြားေရးအသင္း 
ပရိယတၱိႏုဂၢဟအသင္း စေသာ အသင္းမ်ား၏ ၾသ၀ါဒစရိယ တာ၀န္မ်ားကို ထမ္းေဆာင္ 
ေတာ္မူခဲ့ပါသည္။ ၎ျပင္ေႏြရာသီ ယမိုက္+ပ႒ာန္း+ဆန္းစေသာသင္တန္းမ်ားကို 
ရန္ကုန္ၿမိဳ႕မဂၤလာဗ်ဴဟာအသင္း၌ ၃-ႏွစ္၊ အင္းစိန္ရြာမ ပရိယတၱိစာသင္တိုက္၌ ၁၄-ႏွစ္၊ 
ပဲခူး၊ မႏ ၱေလး၊ ေတာင္ႀကီး၊ ကေလးၿမိဳ႕တို႔၌ အခါအားေလ်ာ္စြာ လွည့္လည္ 
ပို႔ခ်ေတာ္မူခဲ့ပါသည္။ လူ၀တ္ေၾကာင္မ်ားအတြက္ အဘိဓမၼာသင္တန္းမ်ားကိုလည္း အဘိဓမၼာ 
စာေမးပြဲမ်ား ေျဖဆိုႏိုင္သည္အထိ ၁ ႏွစ္ ၂ ႀကိမ္ခန္႔ပို႔ခ်ေပးေတာ္မူခဲ့ပါသည္။ 
ရဟန္းခံ သိမ္သမုတ္စေသာ ကံႀကီး၊ ကံငယ္ သံဃာ့ကိစၥမ်ားကိုလညး္ ဆက္စပ္ေနသည့္ ေနရာတုိင္း 
ဦးေဆာင္ဦးရြက္ျပဳကာ အေလးထား ေဆာင္ရြက္ ေပးေတာ္မူေလ့ရွိသည္။<br>
<br>
ၾကည္ညိဳဖြယ္ရာ ထူးျခားေသာဂုဏ္ရည္မ်ား<br>
ဆရာေတာ္သည္ ပရိယတၱိစာေပမ်ားကို ျမတ္ျမတ္ႏိုုးႏိုုး ကိုယ္ႀကိဳးမငဲ့ပဲ 
ေဆာင္ရြက္ေလ့ရွိျခင္း၊ စာေပဗဟုသုတ အကူအညီ ေတာင္းခံလာသူမွန္သမွ်အား ပုဂၢိဳလ္မေရြး၊ 
အခ်ိန္အခါမေရြး အမ်ားအတြက္ကို မဆိုထားႏွင့္ သာမန္ တစ္ဦးတစ္ေယာက္ကိုပင္ ထက္သန္စြာ 
ကူညီေပးေလ့ရွိျခင္း၊ သင္နည္းစနစ္မ်ားကိုလညး္ လြယ္သည္ထက္ လြယ္ေအာင္ ေခတ္မီေအာင္ 
တီထြင္ႀကံဆၿပီး သင္ၾကားပို႕ခ်ေရးသားေလ့ရွိျခင္း၊ အမ်ားႏွင့္ဆက္ဆံရာတြင္ 
ဟိတ္ဟန္မရွိပဲ တည္ၿငိမ္ေအးေဆးစြာ ရိုးရိုးသားသား ဆက္ဆံေလ့ရွိျခင္း၊ ပရိယတ္၊ ပဋိပတ္ 
၂ မ်ိဳးလံုးကို ျမတ္ႏိုးစြာ မိမိအတြက္ေရာ သူတစ္ပါးအတြက္ပါ ေဆာင္ရြက္ေပးေလ့ရွိျခင္း၊ 
ပစၥည္းလာဘ္လာဘကို တြယ္တာမႈ မရွိဘဲ ရက္ရက္ေရာေရာ ေပးကမ္းလွဴဒါန္းေလ့ရွိျခင္း၊ 
တပည့္မ်ားအေပၚ မိဘသဖြယ္ ေစတနာ ေမတၱာထား၍ ေစာင့္ေရွာက္ခ်ီးေျမွာက္ေလ့ရွိျခင္း၊ 
ေျပာဆိုဆံုးမရာ၌ အမိန္႔ေပးသည့္သေဘာမ်ိဳးမဟုတ္ပဲ က်ိဳးေၾကာင္း ယုတၱိ ျပ၍ 
တရားဓမၼျဖင့္ ညင္သာစြာ ဆိုဆံုးမေလ့ရွိျခင္း ဒါယကာ ဒါယိကာမမ်ား အေပၚတြင္ 
တြယ္တာမက္ေမာမႈ မထားပဲ ကုေလသု အနႏုဂိဒၶဂုဏ္ႏွင့္ ညီႏိုင္သမွ်ညီေအာင္ 
လုိက္နာက်င့္သံုးေလ့ရွိျခင္း စေသာဂုဏ္တို႕သည္ ရဟန္းရွင္လူ ျပည္သူတို႔၏ 
ၾကည္ညိဳေလးစားျခင္းခံရေသာ ဆရာေတာ္၏ ဂုဏ္ရည္မ်ားျဖစ္ပါသည္။<br>
<br>
အဂၢမဟာပ႑ိတဘြဲ႕တံဆိပ္ေတာ္ကို အလွဴခံရရွိေတာ္မူျခင္း<br>
ဤသို႔ေသာ ဂုဏ္တို႕ႏွင့္ ကံုလံု ျပည့္စံုေတာ္မူေသာ ဆရာေတာ္ ဘဒၵႏ ၱ တိေလာကာဘိ၀ံသအား 
၁၃၅၉ခု (၁၉၉၈-ခုႏွစ္)တြင္ ျပည္ေထာင္စု ျမန္မာႏိုင္ငံေတာ္အစိုးရ၊ 
ႏိုင္ငံေတာ္ေအးခ်မ္းသာယာေရးႏွင့္ ဖြံ႕ၿဖိဳးေရး ေကာင္စီက အဂၢမဟာပ႑ိတ 
ဘြဲ႕တံဆိပ္ေတာ္ျမတ္ကို ဆက္ကပ္လွဴဒါန္းခဲ့ပါသည္။</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="2">
*****************************************************************************************************</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
								<b><font size="5">Dhamma Talk Video</font></b></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">****dhamma talks uploaded on 
								5 May 2012****</font></p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">(၁၇)ႀကိမ္ေျမာက္ ေႏြရာသီ ယမိုက္ + ပ႒ာန္း အထူး သင္တန္း</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">ဘာသာ + စဥ္</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">ဆန္း (၁)</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/01-Sun-01/01-Ashin-Tilokarbhivamsa-DVD01-sun01.mp4">
<font size="4">&nbsp;၁။ 
ဆန္း(၁) ၆-၅-၂၀၁၀</font></a></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/01-Sun-01/02-Ashin-Tilokarbhivamsa-DVD01-sun01.mp4">
<font size="4">&nbsp;၂။ 
ဆန္း(၁) ၇-၅-၂၀၁၀</font></a></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/01-Sun-01/03-Ashin-Tilokarbhivamsa-DVD01-sun01.mp4">
<font size="4">&nbsp;၃။ 
ဆန္း(၁) ၈-၅-၂၀၁၀</font></a></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/01-Sun-01/04-Ashin-Tilokarbhivamsa-DVD01-sun01.mp4">
<font size="4">&nbsp;၄။ 
ဆန္း(၁) ၉-၅-၂၀၁၀</font></a></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">ဆန္း (၂)</font></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/02-Sun-02/01-Ashin-Tilokarbhivamsa-DVD02-sun02.mp4">
<font size="4">&nbsp;၁။ 
ဆန္း(၂) ၁၀-၅-၂၀၁၀</font></a></p>
	<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/02-Sun-02/02-Ashin-Tilokarbhivamsa-DVD02-sun02.mp4">
<font size="4">&nbsp;၂။ 
ဆန္း(၂) ၁၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၁)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/03-Pahtan-01/01-Ashin-Tilokarbhivamsa-DVD03-Pahtan01.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၁) ၂၂-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/03-Pahtan-01/02-Ashin-Tilokarbhivamsa-DVD03-Pahtan01.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၁) ၂၃-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/03-Pahtan-01/03-Ashin-Tilokarbhivamsa-DVD03-Pahtan01.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၁) ၂၄-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/03-Pahtan-01/04-Ashin-Tilokarbhivamsa-DVD03-Pahtan01.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၁) ၂၅-၄-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၂)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/04-Pahtan-02/01-Ashin-Tilokarbhivamsa-DVD04-Pahtan02.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၂) ၂၆-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/04-Pahtan-02/02-Ashin-Tilokarbhivamsa-DVD04-Pahtan02.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၂) ၂၈-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/04-Pahtan-02/03-Ashin-Tilokarbhivamsa-DVD04-Pahtan02.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၂) ၂၉-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/04-Pahtan-02/04-Ashin-Tilokarbhivamsa-DVD04-Pahtan02.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၂) ၃၀-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၃)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/05-Pahtan-03/01-Ashin-Tilokarbhivamsa-DVD05-Pahtan03.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၃) ၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/05-Pahtan-03/02-Ashin-Tilokarbhivamsa-DVD05-Pahtan03.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၃) ၂-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/05-Pahtan-03/03-Ashin-Tilokarbhivamsa-DVD05-Pahtan03.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၃) ၃-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/05-Pahtan-03/04-Ashin-Tilokarbhivamsa-DVD05-Pahtan03.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၃) ၄-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၄)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/06-Pahtan-04/01-Ashin-Tilokarbhivamsa-DVD06-Pahtan04.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၄) ၅-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/06-Pahtan-04/02-Ashin-Tilokarbhivamsa-DVD06-Pahtan04.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၄) ၆-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/06-Pahtan-04/03-Ashin-Tilokarbhivamsa-DVD06-Pahtan04.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၄) ၇-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/06-Pahtan-04/04-Ashin-Tilokarbhivamsa-DVD06-Pahtan04.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၄) ၈-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၅)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/07-Pahtan-05/01-Ashin-Tilokarbhivamsa-DVD07-Pahtan05.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၅) ၉-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/07-Pahtan-05/02-Ashin-Tilokarbhivamsa-DVD07-Pahtan05.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၅) ၁၀-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/07-Pahtan-05/03-Ashin-Tilokarbhivamsa-DVD07-Pahtan05.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၅) ၁၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/07-Pahtan-05/04-Ashin-Tilokarbhivamsa-DVD07-Pahtan05.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၅) ၁၂-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၆)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/08-Pahtan-06/01-Ashin-Tilokarbhivamsa-DVD08-Pahtan06.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၆) ၁၃-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/08-Pahtan-06/02-Ashin-Tilokarbhivamsa-DVD08-Pahtan06.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၆) ၁၄-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/08-Pahtan-06/03-Ashin-Tilokarbhivamsa-DVD08-Pahtan06.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၆) ၁၅-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/08-Pahtan-06/04-Ashin-Tilokarbhivamsa-DVD08-Pahtan06.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၆) ၁၆-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<font size="4">ပ႒ာန္း (၇)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/09-Pahtan-07/01-Ashin-Tilokarbhivamsa-DVD09-Pahtan07.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၇) ၁၇-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/09-Pahtan-07/02-Ashin-Tilokarbhivamsa-DVD09-Pahtan07.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၇) ၁၈-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/09-Pahtan-07/03-Ashin-Tilokarbhivamsa-DVD09-Pahtan07.mp4">
	<font size="4">&nbsp;၃။ 
	ပ႒ာန္း (၇) ၁၉-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/09-Pahtan-07/04-Ashin-Tilokarbhivamsa-DVD09-Pahtan07.mp4">
	<font size="4">&nbsp;၄။ 
	ပ႒ာန္း (၇) ၂၀-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ပ႒ာန္း (၈)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/10-Pahtan-08/01-Ashin-Tilokarbhivamsa-DVD10-Pahtan08.mp4">
	<font size="4">&nbsp;၁။ 
	ပ႒ာန္း (၈) ၂၁-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/10-Pahtan-08/02-Ashin-Tilokarbhivamsa-DVD10-Pahtan08.mp4">
	<font size="4">&nbsp;၂။ 
	ပ႒ာန္း (၈) ၄-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ေအာက္ယမိုက္ (၁)</font></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/11-auk-ya-mike-01/01-Ashin-Tilokarbhivamsa-DVD11-AukYaMike01.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၁) ၂၂-၄-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/11-auk-ya-mike-01/02-Ashin-Tilokarbhivamsa-DVD11-AukYaMike01.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၁) ၂၃-၄-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/11-auk-ya-mike-01/03-Ashin-Tilokarbhivamsa-DVD11-AukYaMike01.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၁) ၂၄-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/11-auk-ya-mike-01/04-Ashin-Tilokarbhivamsa-DVD11-AukYaMike01.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၁) ၂၆-၄-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ေအာက္ယမိုက္ (၂)</font></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/12-auk-ya-mike-02/01-Ashin-Tilokarbhivamsa-DVD12-AukYaMike02.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၂) ၂၈-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/12-auk-ya-mike-02/02-Ashin-Tilokarbhivamsa-DVD12-AukYaMike02.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၂) ၂၉-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/12-auk-ya-mike-02/03-Ashin-Tilokarbhivamsa-DVD12-AukYaMike02.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၂) ၃၀-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/12-auk-ya-mike-02/04-Ashin-Tilokarbhivamsa-DVD12-AukYaMike02.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၂) ၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<font size="4">ေအာက္ယမိုက္ (၃)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/13-auk-ya-mike-03/01-Ashin-Tilokarbhivamsa-DVD13-AukYaMike03.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၃) ၂-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/13-auk-ya-mike-03/02-Ashin-Tilokarbhivamsa-DVD13-AukYaMike03.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၃) ၃-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/13-auk-ya-mike-03/03-Ashin-Tilokarbhivamsa-DVD13-AukYaMike03.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၃) ၄-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/13-auk-ya-mike-03/04-Ashin-Tilokarbhivamsa-DVD13-AukYaMike03.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၃) ၅-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<font size="4">ေအာက္ယမိုက္ (၄)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/14-auk-ya-mike-04/01-Ashin-Tilokarbhivamsa-DVD14-AukYaMike04.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၄) ၆-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/14-auk-ya-mike-04/02-Ashin-Tilokarbhivamsa-DVD14-AukYaMike04.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၄) ၇-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/14-auk-ya-mike-04/03-Ashin-Tilokarbhivamsa-DVD14-AukYaMike04.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၄) ၈-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/14-auk-ya-mike-04/04-Ashin-Tilokarbhivamsa-DVD14-AukYaMike04.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၄) ၉-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ေအာက္ယမိုက္ (၅)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/15-auk-ya-mike-05/01-Ashin-Tilokarbhivamsa-DVD15-AukYaMike05.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၅) ၁၀-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/15-auk-ya-mike-05/02-Ashin-Tilokarbhivamsa-DVD15-AukYaMike05.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၅) ၁၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/15-auk-ya-mike-05/03-Ashin-Tilokarbhivamsa-DVD15-AukYaMike05.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၅) ၁၂-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/15-auk-ya-mike-05/04-Ashin-Tilokarbhivamsa-DVD15-AukYaMike05.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၅) ၁၃-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ေအာက္ယမိုက္ (၆)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/16-auk-ya-mike-06/01-Ashin-Tilokarbhivamsa-DVD16-AukYaMike06.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၆) ၁၄-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/16-auk-ya-mike-06/02-Ashin-Tilokarbhivamsa-DVD16-AukYaMike06.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၆) ၁၅-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/16-auk-ya-mike-06/03-Ashin-Tilokarbhivamsa-DVD16-AukYaMike06.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၆) ၁၆-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/16-auk-ya-mike-06/04-Ashin-Tilokarbhivamsa-DVD16-AukYaMike06.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၆) ၁၇-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">ေအာက္ယမိုက္ (၇)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/17-auk-ya-mike-07/01-Ashin-Tilokarbhivamsa-DVD17-AukYaMike07.mp4">
	<font size="4">&nbsp;၁။ 
	ေအာက္ယမိုက္ (၇) ၁၈-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/17-auk-ya-mike-07/02-Ashin-Tilokarbhivamsa-DVD17-AukYaMike07.mp4">
	<font size="4">&nbsp;၂။ 
	ေအာက္ယမိုက္ (၇) ၁၉-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/17-auk-ya-mike-07/03-Ashin-Tilokarbhivamsa-DVD17-AukYaMike07.mp4">
	<font size="4">&nbsp;၃။ 
	ေအာက္ယမိုက္ (၇) ၂၀-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/17-auk-ya-mike-07/04-Ashin-Tilokarbhivamsa-DVD17-AukYaMike07.mp4">
	<font size="4">&nbsp;၄။ 
	ေအာက္ယမိုက္ (၇) ၂၁-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၁) 
	</font> </p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/18-AHtet-YaMike-01/01-Ashin-Tilokarbhivamsa-DVD18-AhHtetYaMike01.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၁) ၂၂-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/18-AHtet-YaMike-01/02-Ashin-Tilokarbhivamsa-DVD18-AhHtetYaMike01.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၁) ၂၃-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/18-AHtet-YaMike-01/03-Ashin-Tilokarbhivamsa-DVD18-AhHtetYaMike01.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၁) ၂၄-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/18-AHtet-YaMike-01/04-Ashin-Tilokarbhivamsa-DVD18-AhHtetYaMike01.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၁) ၂၅-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၂) 
	</font> </p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/19-AHtet-YaMike-02/01-Ashin-Tilokarbhivamsa-DVD19-AhHtetYaMike02.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၂) ၂၆-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/19-AHtet-YaMike-02/02-Ashin-Tilokarbhivamsa-DVD19-AhHtetYaMike02.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၂) ၂၈-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/19-AHtet-YaMike-02/03-Ashin-Tilokarbhivamsa-DVD19-AhHtetYaMike02.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၂) ၂၉-၄-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/19-AHtet-YaMike-02/04-Ashin-Tilokarbhivamsa-DVD19-AhHtetYaMike02.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၂) ၃၀-၄-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၃) 
	</font> </p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/20-AHtet-YaMike-03/01-Ashin-Tilokarbhivamsa-DVD20-AhHtetYaMike03.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၃) ၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/20-AHtet-YaMike-03/02-Ashin-Tilokarbhivamsa-DVD20-AhHtetYaMike03.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၃) ၂-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/20-AHtet-YaMike-03/03-Ashin-Tilokarbhivamsa-DVD20-AhHtetYaMike03.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၃) ၃-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/20-AHtet-YaMike-03/04-Ashin-Tilokarbhivamsa-DVD20-AhHtetYaMike03.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၃) ၄-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၄) 
	</font> </p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/21-AHtet-YaMike-04/01-Ashin-Tilokarbhivamsa-DVD21-AhHtetYaMike04.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၄) ၅-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/21-AHtet-YaMike-04/02-Ashin-Tilokarbhivamsa-DVD21-AhHtetYaMike04.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၄) ၆-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/21-AHtet-YaMike-04/03-Ashin-Tilokarbhivamsa-DVD21-AhHtetYaMike04.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၄) ၇-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/21-AHtet-YaMike-04/04-Ashin-Tilokarbhivamsa-DVD21-AhHtetYaMike04.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၄) ၈-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၅)</font></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/22-AHtet-YaMike-05/01-Ashin-Tilokarbhivamsa-DVD22-AhHtetYaMike05.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၅) ၉-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/22-AHtet-YaMike-05/02-Ashin-Tilokarbhivamsa-DVD22-AhHtetYaMike05.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၅) ၁၀-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/22-AHtet-YaMike-05/03-Ashin-Tilokarbhivamsa-DVD22-AhHtetYaMike05.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၅) ၁၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/22-AHtet-YaMike-05/04-Ashin-Tilokarbhivamsa-DVD22-AhHtetYaMike05.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၅) ၁၂-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၆)</font></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/23-AHtet-YaMike-06/01-Ashin-Tilokarbhivamsa-DVD23-AhHtetYaMike06.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၆) ၁၃-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/23-AHtet-YaMike-06/02-Ashin-Tilokarbhivamsa-DVD23-AhHtetYaMike06.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၆) ၁၄-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/23-AHtet-YaMike-06/03-Ashin-Tilokarbhivamsa-DVD23-AhHtetYaMike06.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၆) ၁၅-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/23-AHtet-YaMike-06/04-Ashin-Tilokarbhivamsa-DVD23-AhHtetYaMike06.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၆) ၁၆-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၇)</font></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/24-AHtet-YaMike-07/01-Ashin-Tilokarbhivamsa-DVD24-AhHtetYaMike07.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၇) ၁၇-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/24-AHtet-YaMike-07/02-Ashin-Tilokarbhivamsa-DVD24-AhHtetYaMike07.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၇) ၁၈-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/24-AHtet-YaMike-07/03-Ashin-Tilokarbhivamsa-DVD24-AhHtetYaMike07.mp4">
	<font size="4">&nbsp;၃။ 
	အထက္ယမိုက္ (၇) ၁၉-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/24-AHtet-YaMike-07/04-Ashin-Tilokarbhivamsa-DVD24-AhHtetYaMike07.mp4">
	<font size="4">&nbsp;၄။ 
	အထက္ယမိုက္ (၇) ၂၀-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0"><font size="4">အထက္ယမိုက္ (၈) 
	</font> </p>
	<p style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/25-AHtet-YaMike-08/01-Ashin-Tilokarbhivamsa-DVD25-AhHtetYaMike08.mp4">
	<font size="4">&nbsp;၁။ 
	အထက္ယမိုက္ (၈) ၂၁-၅-၂၀၁၀</font></a></p>
	<p style="margin-top: 0; margin-bottom: 0">
	<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Ashin-Tilokarbhivamsa/25-AHtet-YaMike-08/02-Ashin-Tilokarbhivamsa-DVD25-AhHtetYaMike08.mp4">
	<font size="4">&nbsp;၂။ 
	အထက္ယမိုက္ (၈) ၂၂-၅-၂၀၁၀</font></a></p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p style="margin-top: 0; margin-bottom: 0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0"><font face="Zawgyi-One">&nbsp;</font></p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">&nbsp;</p><p>&nbsp;</p></div><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp; </p>
<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>



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
    
