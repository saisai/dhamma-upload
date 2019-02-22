from bs4 import BeautifulSoup as bs4

one = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 


	




<!-- Start dhammadownload menu top and side bar -->



<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>

<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 542px; top: 12px;" id="layer23">
	<img src="images/YAWSayaDawUSiranandavi.gif" width="133" height="169" border="0"></div>
	


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
<a href="http://www.facebook.com/plugins/likebox.php?href=https%3A%2F%2Fwww.facebook.com%2Fdhammadownload.news&amp;width&amp;height=590&amp;colorscheme=light&amp;show_faces=true&amp;header=true&amp;stream=true&amp;show_border=true">
<img src="images/facebook-logo.gif" width="159" height="59" border="0"></a></div>



<!-- end dhammadownload menu top and side bar -->






	
	
	
	
<div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 218px; top: 156px" id="layer24" font="" face="Zawgyi-One">
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">Tipitakadhara </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">Tipitaka Kovidha </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">Tipitakadhara Dhamma 
									Bandagarika </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">Agga Maha Pandita </font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">Bhaddanta</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">
									Yaw SayaDaw&nbsp; Sireindabhivamsa</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One"><font size="5">
									တိပိဋကဓရ-အဂၢမဟာပ႑ိတ</font></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One"><font size="5">
									ေယာဆရာေတာ္ ဘဒၵႏၲသီရိႏၵာဘိဝံသ</font></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ဓမၼာစရိယ စာသင္သားမ်ားအတြက္ <br>
									စာခ်တန္း(၃)က်မ္းအတြက္စာဝါမ်ား<br>
									အသံဖိုင္မ်ား<br>
&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									************</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoNormal" style="line-height: normal"><b>
<span style="font-size: 18.0pt; font-family: Zawgyi-One,sans-serif">ေယာဆရာေတာ္</span></b></p>
<p class="MsoNormal" style="line-height: normal"><b>
<span style="font-size: 18.0pt; font-family: Zawgyi-One,sans-serif">အရွင္ 
သိရိႏၵာဘိဝံသ (ေယာဆရာေတာ္) (၁၃၀၄)</span></b></p>
<p class="MsoNormal" style="line-height: normal">
<span style="font-size: 12.0pt; font-family: Zawgyi-One,sans-serif">၁။ အမည္ရင္း 
– ေမာင္သာေမာင္<br>
၂။ မိဘအမည္ – ဦးရဲႏုိင္ + ေဒၚတုတ္ခုိင္<br>
၃။ ေမြးသကၠရာဇ္ – ၁၃၀၄ ခုႏွစ္ ၊ ေသာၾကာေန႕<br>
၄။ ေမြးဖြားရာရာ ေဒသ – မေကြးတုိင္း၊ ဂန္႕ေဂၚၿမိဳ႕နယ္ (ေယာနယ္)၊ လက္ပံ႐ြာ</span></p>
<p class="MsoNormal" style="line-height: normal"><b>
<span style="font-size: 18.0pt; font-family: Zawgyi-One,sans-serif">
ကုိယ္ေရးျဖစ္စဥ္</span></b></p>
<p class="MsoNormal" style="line-height: normal">
<span style="font-size: 12.0pt; font-family: Zawgyi-One,sans-serif">အရွင္ 
သိရိႏၵာဘိဝံသည္ အဖ ဦးရဲႏုိင္၊ အမိ ေဒၚတုတ္ခုိင္ တုိ႕မွ ၁၃၀၄ ခုႏွစ္၊ တေပါင္း 
လျပည့္ေက်ာ္ ၆ ရက္ ေသာၾကာေန႕တြင္ မေကြးတုိင္း ဂန္႕ေဂါၿမိဳ႕နယ္ (ေယာနယ္)၊ လက္ပံ႐ြာ၌ 
ဖြားျမင္ခဲ့ေသာ သားဦး ရတနာ ျဖစ္ပါသည္။ ၁၃၂၄ ခုႏွစ္၊ ကဆုန္ လျပည့္ေက်ာ္ ၂ ရက္ 
စေနေန႕တြင္ ဂန္႕ေဂၚၿမိဳ႕နယ္ ကန္ေတာရ ေက်ာင္းတုိက္တြင္ ရဟန္း အျဖစ္သုိ႕ ေရာက္ရွိ 
ခဲ့ပါသည္။</span></p>
<p class="MsoNormal" style="line-height: normal">
<span style="font-size: 12.0pt; font-family: Zawgyi-One,sans-serif">ပါဠိ ပထမျပန္ 
စာေမးပြဲ ငယ္၊ လတ္၊ ႀကီးႏွင့္ ဓမၼာ စရိယ စာေမးပြဲတြင္ သာသန ဓဇသီရိပဝရ ဓမၼာစရိယ 
ဘြဲ႕ကုိ လည္းေကာင္း၊ အဂၢမဟာ အေက်ာ္ဘြဲ႕ကုိ လည္းေကာင္း၊ ဝိနယ ပါဠိ ပါရဂူ ဘြဲ႕ႏွင့္ 
ပဋိသမႝိဒါမဂၢ ပါဠိ ပါရဂူဘြဲ႕ကုိ လည္းေကာင္း၊ နိကာယ္ စာေမးပြဲတြင္ နိကာယုေဇၨာတက 
အတၲဝိသာရဒ မူလအာဘိ ဓမၼိကဘြဲ႕၊ ဓမ ၼဝိသာရဒ မဇၥ်ိမ အာဘိဓမၼကဘြဲ႕၊ အတၲဝိသာရဒဒီဃဘာဏက 
ဘြဲ႕ကုိ လည္းေကာင္း၊ မႏၱေလး သက်သီဟ ဓမၼာ စရိယ ဘြဲ႕ကို လည္းေကာင္း၊ ရန္ကုန္ ေစတီယဂၤဏ 
ဓမၼာ စရိယ ဘြဲ႕ကုိ လည္းေကာင္း၊ တိပိဋက ေ႐ြးခ်ယ္ပြဲတြင္ (၂၃) ႀကိမ္ေျမာက္၌ 
ဝိနယဓရဝိနယ ေကာဝိဒ ဘြဲ႕ကုိ လည္းေကာင္း၊ (၂၄) ႀကိမ္ေျမာက္၌ အဘိဓမၼာ၊ ပထမပုိင္း 
ငါးက်မ္း အာဂုံကုိ လည္းေကာင္း၊ (၂၇) ႀကိမ္ေျမာက္၌ အဘိဓမၼာ ပထမပုိင္း ငါးက်မ္း သေဘာ 
ေရးေျဖကုိ လည္းေကာင္း၊ (၂၉) ႀကိမ္ေျမာက္ အာဘိဓမၼိက အဘိဓမၼေကာဝိဒ ဘြဲ႕ကုိ 
လည္းေကာင္း၊ (၃၁) ႀကိမ္ေျမာက္၌ ဒီဃဘာဏက ဘြဲ႕ႏွင့္ တိပိဋကဓရ ဘြဲ႕ကုိ လည္းေကာင္း ရရွိ 
ေအာင္ျမင္ ခဲ့ပါသည္။</span></p>
<p class="MsoNormal" style="line-height: normal">
<span style="font-size: 12.0pt; font-family: Zawgyi-One,sans-serif">၁၃၄၆ ခုႏွစ္၊ 
(၄၇) ႀကိမ္ေျမာက္ တိပိဋကဓရ ေ႐ြးခ်ယ္ပြဲတြင္ သုတၲႏၱဋကဒီဃနိကာယ သုံးက်မ္း (သေဘာ 
ေရးေျဖပြဲ) ကုိ ေအာင္ျမင္ေတာ္ မူေသာေၾကာင့္ ဒီဃနိကာယ ေကာဝိဒ ဘြဲ႕တံဆိပ္ေတာ္ႏွင့္ 
၎ေအာင္လက္မွတ္ တုိ႕ကုိ ရရွိ ခဲ့ပါသည္။ အရွင္ သိရိႏၵာဘိဝံသသည္ သင္႐ုိး ပိဋကတ္ 
သုံးပုံကုိ ၿပီးဆုံး ေအာင္ျမင္ၿပီး ျဖစ္သျဖင့္ တိပိဋကဓရ တိပိဋက ေကာဝိဒ 
ဘြဲ႕တံဆိပ္ေတာ္၊ ၎ေအာင္လက္မွတ္ႏွင့္ အ႐ုိးဝါကနကၠဒဏ္ ထီးျဖဴေတာ္ သုံးလက္ တံဆိပ္ 
ပါရွိေသာ သာသနာ့ ေအာင္လံေတာ္ကုိ ခံယူ ရရွိခဲ့ၿပီး ျပည္ေထာင္စု ျမန္မာႏုိင္ငံေတာ္ 
အစုိးရက လွဴဒါန္းေသာ ကုန္း၊ ေရ၊ ေလ သုံးဌာန၌ ခရီး သြားလာခြင့္ အခလြတ္ အၿမဲတမ္း 
အထက္တန္း လက္မွတ္ တုိ႕ကုိလည္း ရရွိ ခဲ့ပါသည္။</span></p>
<p class="MsoNormal" style="line-height: normal"><b>
<span style="font-size: 18.0pt; font-family: Zawgyi-One,sans-serif">ေရးသား 
ထုတ္ေဝ ခဲ့ေသာ စာအုပ္မ်ား</span></b></p>
<p class="MsoNormal" style="line-height: normal">
<span style="font-size: 12.0pt; font-family: Zawgyi-One,sans-serif">၁။ 
ကုသုိလ္လည္းရ ဝမ္းလည္းဝ – ၁၉၉၉ ခုႏွစ္<br>
၂။ စိတ္စြမ္းရည္ – ၂၀၀၀ ျပည့္ႏွစ္<br>
၃။ စိတ္ေအးစရာ သာသနာ – ၂၀၀၀ ျပည့္ႏွစ္<br>
၄။ ဆင္းရဲ၏ေနာက္ ခ်မ္းသာေရာက္ – ၁၉၉၉ ခုႏွစ္<br>
၅။ ႏွလုံးသားဝယ္ ဘုရားတည္ – ၁၉၉၈ ခုႏွစ္<br>
၆။ ပညာလမ္းျပ လူ႕အလွ – ၂၀၀၀ ျပည့္ႏွစ္<br>
၇။ ပေတၲာတသုတၲန္<br>
၈။ ဘဝဇာတ္ခုံ ပုံစံစုံ – ၂၀၀၀ ျပည့္ႏွစ္<br>
၉။ ဘဝဇာတ္ခုံ ပုံစံစုံ တရားေတာ္ – ၁၉၉၉ ခုႏွစ္<br>
၁၀။ ေမတၲာတရား လူ႕စြမ္းအား – ၂၀၀၀ ျပည့္ႏွစ္<br>
၁၁။ ေမတၲာႏွလုံး အလွဆုံး – ၁၉၉၉ ခုႏွစ္<br>
၁၂။ သမုဒၵရာ ဝမ္းတထြာ – ၂၀၀၀ ျပည့္ႏွစ္<br>
၁၃။ အဆင္းအတက္ လမ္းႏွစ္ဖက္ – ၁၉၉၉ ခုႏွစ္<br>
၁၄။ အေပါင္းလကၡဏာ – ၂၀၀၀ ျပည့္ႏွစ္<br>
၁၅။ အသိမွန္ကန္ အဖုိးတန္ – ၁၉၉၉ ခုႏွစ္<br>
၁၆။ အိမ္တြင္းမဂၢင္ လူ႕က်င့္စဥ္ – ၂၀၀၀ ျပည့္ႏွစ္<br>
06:24, 23 ဧျပီ 2010 (UTC)</span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="6">ဓမၼာစရိယ စာသင္သားမ်ားအတြက္ </font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="6">စာခ်တန္း(၃)က်မ္းအတြက္စာဝါမ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="6">အသံဖိုင္မ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">၁၃၇၀</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၂၀၀၈</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/001-YawSayaDawGyi-Sirinandabhivamsa-SR-22-5-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁<font face="Calibri,sans-serif">။ 
									၂၂-၅-၂၀၀၈ </font></font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/002-YawSayaDawGyi-Sirinandabhivamsa-SR-23-5-2008.mp3">
									<font size="4">၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၃-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/003-YawSayaDawGyi-Sirinandabhivamsa-SR-24-5-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃။ 
									၂၄-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/004-YawSayaDawGyi-Sirinandabhivamsa-SR-25-5-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄။ 
									၂၅-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/005-YawSayaDawGyi-Sirinandabhivamsa-SR-26-5-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅။ 
									၂၆-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/006-YawSayaDawGyi-Sirinandabhivamsa-SR-28-5-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆။ 
									၂၈-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/007-YawSayaDawGyi-Sirinandabhivamsa-SR-29-5-2008.mp3">
									<font size="4">၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၉-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/008-YawSayaDawGyi-Sirinandabhivamsa-SR-30-5-2008.mp3">
									<font size="4">၈</font><font size="4" face="Calibri,sans-serif">။ 
									၃၀-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/009-YawSayaDawGyi-Sirinandabhivamsa-SR-31-5-2008.mp3">
									<font size="4">၉</font><font size="4" face="Calibri,sans-serif">။ 
									၃၁-၅-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/010-YawSayaDawGyi-Sirinandabhivamsa-SR-01-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၀။ 
									၁-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/011-YawSayaDawGyi-Sirinandabhivamsa-SR-04-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၁။ 
									၄-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/012-YawSayaDawGyi-Sirinandabhivamsa-SR-05-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၂။ 
									၅-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/013-YawSayaDawGyi-Sirinandabhivamsa-SR-06-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၃။ 
									၆-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/014-YawSayaDawGyi-Sirinandabhivamsa-SR-10-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၄။ 
									၁၀-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/015-YawSayaDawGyi-Sirinandabhivamsa-SR-12-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၅။ 
									၁၂-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/016-YawSayaDawGyi-Sirinandabhivamsa-SR-13-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၆။ 
									၁၃-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/017-YawSayaDawGyi-Sirinandabhivamsa-SR-14-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၇။ 
									၁၄-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/018-YawSayaDawGyi-Sirinandabhivamsa-SR-15-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၈။ 
									၁၅-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၁</span></font></a><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/019-YawSayaDawGyi-Sirinandabhivamsa-SR-16-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၁၉။ 
									၁၆-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/020-YawSayaDawGyi-Sirinandabhivamsa-SR-19-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၀။ 
									၁၉-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/021-YawSayaDawGyi-Sirinandabhivamsa-SR-21-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၁။ 
									၂၁-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/022-YawSayaDawGyi-Sirinandabhivamsa-SR-22-06-2008.mp3">
									<font size="4">၂၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၂-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/023-YawSayaDawGyi-Sirinandabhivamsa-SR-23-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၃။ 
									၂၃-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/024-YawSayaDawGyi-Sirinandabhivamsa-SR-25-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၄။ 
									၂၅-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/025-YawSayaDawGyi-Sirinandabhivamsa-SR-26-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၅။ 
									၂၆-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/026-YawSayaDawGyi-Sirinandabhivamsa-SR-28-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၆။ 
									၂၈-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/027-YawSayaDawGyi-Sirinandabhivamsa-SR-29-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၇။ 
									၂၉-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/028-YawSayaDawGyi-Sirinandabhivamsa-SR-30-06-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၈။ 
									၃၀-၆-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/029-YawSayaDawGyi-Sirinandabhivamsa-SR-01-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၂၉။ 
									၁-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/030-YawSayaDawGyi-Sirinandabhivamsa-SR-03-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၀။ 
									၃-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/031-YawSayaDawGyi-Sirinandabhivamsa-SR-04-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၁။ 
									၄-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/032-YawSayaDawGyi-Sirinandabhivamsa-SR-05-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၂။ 
									၅-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/033-YawSayaDawGyi-Sirinandabhivamsa-SR-06-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၃။ 
									၆-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/034-YawSayaDawGyi-Sirinandabhivamsa-SR-14-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၄။ 
									၁၄-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/035-YawSayaDawGyi-Sirinandabhivamsa-SR-15-07-2008.mp3">
									<font size="4">၃၅</font><font size="4" face="Calibri,sans-serif">။ 
									၁၅-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/036-YawSayaDawGyi-Sirinandabhivamsa-SR-19-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၆။ 
									၁၉-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/037-YawSayaDawGyi-Sirinandabhivamsa-SR-20-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၇။ 
									၂၀-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/038-YawSayaDawGyi-Sirinandabhivamsa-SR-21-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၈။ 
									၂၁-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/039-YawSayaDawGyi-Sirinandabhivamsa-SR-22-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၃၉။ 
									၂၂-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/040-YawSayaDawGyi-Sirinandabhivamsa-SR-23-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၀။ 
									၂၃-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၁</font></span><font size="4"><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"> </span>
									</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">၁၃၇၀</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၂၀၀၈</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၂</font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/041-YawSayaDawGyi-Sirinandabhivamsa-SR-24-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၁။ 
									၂၄-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/042-YawSayaDawGyi-Sirinandabhivamsa-SR-26-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၂။ 
									၂၆-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/043-YawSayaDawGyi-Sirinandabhivamsa-SR-27-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၃။ 
									၂၇-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/044-YawSayaDawGyi-Sirinandabhivamsa-SR-28-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၄။ 
									၂၈-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/045-YawSayaDawGyi-Sirinandabhivamsa-SR-29-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၅။ 
									၂၉-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/046-YawSayaDawGyi-Sirinandabhivamsa-SR-31-07-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၆။ 
									၃၁-၇-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/047-YawSayaDawGyi-Sirinandabhivamsa-SR-03-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၇။ 
									၃-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/048-YawSayaDawGyi-Sirinandabhivamsa-SR-04-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၈။ 
									၄-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/049-YawSayaDawGyi-Sirinandabhivamsa-SR-05-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၄၉။ 
									၅-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/050-YawSayaDawGyi-Sirinandabhivamsa-SR-06-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၀။ 
									၆-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/051-YawSayaDawGyi-Sirinandabhivamsa-SR-07-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၁။ 
									၇-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/052-YawSayaDawGyi-Sirinandabhivamsa-SR-08-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၂။ 
									၈-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/053-YawSayaDawGyi-Sirinandabhivamsa-SR-10-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၃။ 
									၁၀-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/054-YawSayaDawGyi-Sirinandabhivamsa-SR-11-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၄။ 
									၁၁-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/055-YawSayaDawGyi-Sirinandabhivamsa-SR-12-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၅။ 
									၁၂-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/056-YawSayaDawGyi-Sirinandabhivamsa-SR-13-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၆။ 
									၁၃-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/057-YawSayaDawGyi-Sirinandabhivamsa-SR-14-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၇။ 
									၁၄-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/058-YawSayaDawGyi-Sirinandabhivamsa-SR-15-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၈။ 
									၁၅-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/059-YawSayaDawGyi-Sirinandabhivamsa-SR-17-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၅၉။ 
									၁၇-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/060-YawSayaDawGyi-Sirinandabhivamsa-SR-18-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၀။ 
									၁၈-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/061-YawSayaDawGyi-Sirinandabhivamsa-SR-19-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၁။ 
									၁၉-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/062-YawSayaDawGyi-Sirinandabhivamsa-SR-20-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၂။ 
									၂၀-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/063-YawSayaDawGyi-Sirinandabhivamsa-SR-25-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၃။ 
									၂၅-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/064-YawSayaDawGyi-Sirinandabhivamsa-SR-26-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၄။ 
									၂၆-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/065-YawSayaDawGyi-Sirinandabhivamsa-SR-27-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၅။ 
									၂၇-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/066-YawSayaDawGyi-Sirinandabhivamsa-SR-29-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၆။ 
									၂၉-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/067-YawSayaDawGyi-Sirinandabhivamsa-SR-31-08-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၇။ 
									၃၁-၈-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/068-YawSayaDawGyi-Sirinandabhivamsa-SR-01-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၆၈။ 
									၁-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/069-YawSayaDawGyi-Sirinandabhivamsa-SR-02-09-2008.mp3">
									<font size="4">၆၉</font><font size="4" face="Calibri,sans-serif">။ 
									၂-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/070-YawSayaDawGyi-Sirinandabhivamsa-SR-03-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၀။ 
									၃-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/071-YawSayaDawGyi-Sirinandabhivamsa-SR-04-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၁။ 
									၄-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/072-YawSayaDawGyi-Sirinandabhivamsa-SR-05-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၂။ 
									၅-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/073-YawSayaDawGyi-Sirinandabhivamsa-SR-06-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၃။ 
									၆-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/074-YawSayaDawGyi-Sirinandabhivamsa-SR-08-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၄။ 
									၈-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/075-YawSayaDawGyi-Sirinandabhivamsa-SR-09-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၅။ 
									၉-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/076-YawSayaDawGyi-Sirinandabhivamsa-SR-11-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၆။ 
									၁၁-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/077-YawSayaDawGyi-Sirinandabhivamsa-SR-12-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၇။ 
									၁၂-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/078-YawSayaDawGyi-Sirinandabhivamsa-SR-15-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၇၈။ 
									၁၅-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/079-YawSayaDawGyi-Sirinandabhivamsa-SR-16-09-2008.mp3">
									<font size="4">၇၉</font><font size="4" face="Calibri,sans-serif">။ 
									၁၆-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/080-YawSayaDawGyi-Sirinandabhivamsa-SR-17-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၀။ 
									၁၇-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၂</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၁၃၇၀-၂၀၀၈ စာခ်တန္းစာဝါ-၃
									</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/081-YawSayaDawGyi-Sirinandabhivamsa--SR-19-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၁။ 
									၁၉-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/082-YawSayaDawGyi-Sirinandabhivamsa-SR-20-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၂။ 
									၂၀-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/083-YawSayaDawGyi-Sirinandabhivamsa--SR-21-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၃။ 
									၂၁-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/084-YawSayaDawGyi-Sirinandabhivamsa-SR-23-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၄။ 
									၂၃-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/085-YawSayaDawGyi-Sirinandabhivamsa-SR-24-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၅။ 
									၂၄-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/086-YawSayaDawGyi-Sirinandabhivamsa-SR-25-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၆။ 
									၂၅-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/087-YawSayaDawGyi-Sirinandabhivamsa-SR-30-09-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၇။ 
									၃၀-၉-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/088-YawSayaDawGyi-Sirinandabhivamsa-SR-01-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၈။ 
									၁-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/089-YawSayaDawGyi-Sirinandabhivamsa-SR-02-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၈၉။ 
									၂-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/090-YawSayaDawGyi-Sirinandabhivamsa-SR-03-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၀။ 
									၃-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/091-YawSayaDawGyi-Sirinandabhivamsa-SR-04-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၁။ 
									၄-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/092-YawSayaDawGyi-Sirinandabhivamsa-SR-05-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၂။ 
									၅-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/093-YawSayaDawGyi-Sirinandabhivamsa-SR-06-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၃။ 
									၆-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/094-YawSayaDawGyi-Sirinandabhivamsa-SR-08-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၄။ 
									၈-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/095-YawSayaDawGyi-Sirinandabhivamsa-SR-09-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၅။ 
									၉-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/096-YawSayaDawGyi-Sirinandabhivamsa-SR-11-10-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၆။ 
									၁၁-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/097-YawSayaDawGyi-Sirinandabhivamsa-SR12-11-2008.mp3">
									<font size="4" face="Calibri,sans-serif">၉၇။ 
									၁၂-၁၀-၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/098-YawSayaDawGyi-Sirinandabhivamsa-SR17-11-2008-.mp3">
									<font size="4" face="Calibri,sans-serif">၉၈။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/099-YawSayaDawGyi-Sirinandabhivamsa-001.mp3">
									<font size="4" face="Calibri,sans-serif">၉၉။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/100-SayaDawGyi-Sirinandabhivamsa-002.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၀။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/101-SayaDawGyi-Sirinandabhivamsa-003.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၁။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/102-SayaDawGyi-Sirinandabhivamsa-004.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၂။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/103-SayaDawGyi-Sirinandabhivamsa-007.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၃။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/104-SayaDawGyi-Sirinandabhivamsa-008.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၄။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/105-SayaDawGyi-Sirinandabhivamsa-010.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၅။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/106-SayaDawGyi-Sirinandabhivamsa-014.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၆။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/107-SayaDawGyi-Sirinandabhivamsa-015.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/108-SayaDawGyi-Sirinandabhivamsa-019.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၈။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/109-SayaDawGyi-Sirinandabhivamsa-020.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၀၉။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/110-SayaDawGyi-Sirinandabhivamsa-021.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၀။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/111-SayaDawGyi-Sirinandabhivamsa-023.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၁။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/112-SayaDawGyi-Sirinandabhivamsa-024.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၂။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/113-SayaDawGyi-Sirinandabhivamsa-026.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၃။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/114-SayaDawGyi-Sirinandabhivamsa-A0.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၄။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/115-SayaDawGyi-Sirinandabhivamsa-A1.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၅။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/116-SayaDawGyi-Sirinandabhivamsa-A4.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၆။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/117-SayaDawGyi-Sirinandabhivamsa-A9.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/117-SayaDawGyi-Sirinandabhivamsa-A11.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/118-SayaDawGyi-Sirinandabhivamsa-A12.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၈။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/119-SayaDawGyi-Sirinandabhivamsa-A13.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၁၉။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/120-SayaDawGyi-Sirinandabhivamsa-A15.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၀။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/121-SayaDawGyi-Sirinandabhivamsa-A16.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၁။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/122-SayaDawGyi-Sirinandabhivamsa-A17.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၂။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/123-SayaDawGyi-Sirinandabhivamsa-A22.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၃။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/124-SayaDawGyi-Sirinandabhivamsa-A24.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၄။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/125-SayaDawGyi-Sirinandabhivamsa-A26.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၅။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/126-SayaDawGyi-Sirinandabhivamsa-A27.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၆။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/127-SayaDawGyi-Sirinandabhivamsa-A28.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/128-SayaDawGyi-Sirinandabhivamsa-A30.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၈။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/129-SayaDawGyi-Sirinandabhivamsa-A002.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၂၉။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/130-SayaDawGyi-Sirinandabhivamsa-A004.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၀။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/131-SayaDawGyi-Sirinandabhivamsa-A006.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၁။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/132-SayaDawGyi-Sirinandabhivamsa-A007.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၂။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/133-SayaDawGyi-Sirinandabhivamsa-A008.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၃။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/134-SayaDawGyi-Sirinandabhivamsa-A010.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၄။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/135-SayaDawGyi-Sirinandabhivamsa-A002.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၅။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/136-SayaDawGyi-Sirinandabhivamsa-A006.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၆။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/137-SayaDawGyi-Sirinandabhivamsa-A010.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/138-SayaDawGyi-Sirinandabhivamsa-A001.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၈။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/139-SayaDawGyi-Sirinandabhivamsa-A004.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၃၉။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/140-SayaDawGyi-Sirinandabhivamsa-A04.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၀။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/141-SayaDawGyi-Sirinandabhivamsa-A006.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၁။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/142-SayaDawGyi-Sirinandabhivamsa-A008.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၂။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/143-SayaDawGyi-Sirinandabhivamsa-A010.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၃။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/144-SayaDawGyi-Sirinandabhivamsa-A011.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၄။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/145-SayaDawGyi-Sirinandabhivamsa-A014.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၅။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/146-SayaDawGyi-Sirinandabhivamsa-A003.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၆။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/147-SayaDawGyi-Sirinandabhivamsa-A004.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/148-SayaDawGyi-Sirinandabhivamsa-A005.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၈။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/149-SayaDawGyi-Sirinandabhivamsa-A007.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၄၉။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/150-SayaDawGyi-Sirinandabhivamsa-A008+.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၀။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/151-SayaDawGyi-Sirinandabhivamsa-A009+.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၁။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/152-SayaDawGyi-Sirinandabhivamsa-%20A010+.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၂။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/153-SayaDawGyi-Sirinandabhivamsa-A011.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၃။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/154-SayaDawGyi-Sirinandabhivamsa-A014.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၄။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/155-SayaDawGyi-Sirinandabhivamsa-A015.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၅။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/156-SayaDawGyi-Sirinandabhivamsa-A016.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၆။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Calibri,sans-serif">
									၁၅၇။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၃</font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/158-SayaDawGyi-Sirinandabhivamsa-A018.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၈။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008/159-SayaDawGyi-Sirinandabhivamsa-A020.mp3">
									<font size="4" face="Calibri,sans-serif">
									၁၅၉။ ၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၃</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၁၃၇၀-၂၀၀၈ စာခ်တန္းစာဝါ-၄</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/001-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၁။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/002-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၂။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/003-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၃။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/004-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၄။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/005-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၅။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/006-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၆။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/007-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၇။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/008-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၈။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/009-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၉။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/010-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၁၀။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/011-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၁၁။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Calibri,sans-serif">၁၂။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၄</font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/013-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4" face="Calibri,sans-serif">၁၃။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/014-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၁၄။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/015-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4" face="Calibri,sans-serif">၁၅။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/016-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၁၆။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/017-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4" face="Calibri,sans-serif">၁၇။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Calibri,sans-serif">၁၈။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၄</font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/019-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4" face="Calibri,sans-serif">၁၉။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/020-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၀</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/021-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၂၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US"><font size="4">၄</font></span></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/023-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၃</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/024-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၄</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/025-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၅</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/026-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၆</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/027-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/028-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၈</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/029-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၂၉</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/030-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၃၀</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/031-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၃၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/032-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၃၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/033-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၃၃</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/034-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၃၄</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/035-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၃၅</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/036-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၃၆</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/037-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၃၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/038-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၃၈</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/039-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၃၉</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/040-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၄၀</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/041-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/042-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/043-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၃</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/044-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၄</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/045-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၅</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/046-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၆</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/047-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/048-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၈</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/049-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၄၉</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/050-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၀</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/051-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/052-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/053-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၃</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/054-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၄</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/056-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၅</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/056-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၆</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/057-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/058-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၈</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/059-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၅၉</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/060-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၀</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/060-1-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၀-၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/060-2-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၀</font><font size="4" face="Calibri,sans-serif">-၂။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/061-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/062-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/063-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၃</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/064-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၄</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/065-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၅</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/066-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၆</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/067-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/068-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၈</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/069-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၆၉</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/070-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၀</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/071-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၁</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/072-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၂</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/073-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၃</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/074-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၄</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/075-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၅</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/076-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၆</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/077-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.mp3">
									<font size="4">၇၇</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2008-2/078-YawSayaDawGyi-Sirinandabhivamsa-2008-Sarwar-04.MP3">
									<font size="4">၇၈</font><font size="4" face="Calibri,sans-serif">။ 
									၂၀၀၈ </font>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">(၁၃၇၀</font></span><span style="font-family: Calibri,sans-serif"><font size="4">)</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">
									</font></span>
									<span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">
									<font size="4">စာခ်တန္းစာဝါ</font></span><span style="line-height: 115%; font-family: Calibri,sans-serif" lang="EN-US"><font size="4">-</font></span><font size="4"><span style="line-height: 115%; font-family: Arial,sans-serif" lang="EN-US">၄</span></font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၁၃၇၁-၂၀၀၉ စာခ်တန္းစာဝါ-၅</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/079-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၇၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/080-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၈၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/081-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၈၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/082-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၈၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/083-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၈၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/084-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၈၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/085-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၈၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/086-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၈၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/087-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၈၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/088-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၈၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/089-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၈၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/090-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၉၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/091-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၉၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/092-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၉၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/093-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၉၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/094-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၉၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/095-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၉၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/096-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၉၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/097-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၉၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/098-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၉၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/099-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၉၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/100-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.mp3">၁၀၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/101-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/102-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/103-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/104-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/105-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/106-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/107-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/108-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/109-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၀၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/110-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/111-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/112-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/113-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/114-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/115-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/116-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/117-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/118-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/119-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၁၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/120-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/121-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/122-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/123-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/124-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/125-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/126-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/127-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/128-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/129-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၂၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/130-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/131-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/132-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/133-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/134-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/135-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/136-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/137-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/138-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/139-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၃၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/140-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/141-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/142-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/143-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/144-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/145-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/146-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၆။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/147-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၇။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/148-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၈။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/149-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၄၉။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/150-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၅၀။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/151-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၅၁။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/152-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၅၂။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/153-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၅၃။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/154-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၅၄။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2009/155-YawSayaDawGyi-Sirinandabhivamsa-2009-Sarwar-05.MP3">၁၅၅။ ၂၀၀၉ စာခ်တန္းစာဝါ-၅</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၂၀၁၀ စာခ်တန္းစာဝါမ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/001-YawSayaDawGyi-Sirinandabhivamsa-14-06-2010.mp3">၁။ ၁၄-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/002-YawSayaDawGyi-Sirinandabhivamsa-15-06-2010.mp3">၂။ ၁၅-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/003-YawSayaDawGyi-Sirinandabhivamsa-16-06-2010.mp3">၃။ ၁၆-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/004-YawSayaDawGyi-Sirinandabhivamsa-17-06-2010.mp3">၄။ ၁၇-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/005-YawSayaDawGyi-Sirinandabhivamsa-18-06-2010.mp3">၅။ ၁၈-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/006-YawSayaDawGyi-Sirinandabhivamsa-20-06-2010.mp3">၆။ ၂၀-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/007-YawSayaDawGyi-Sirinandabhivamsa-21-06-2010.mp3">၇။ ၂၁-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/008-YawSayaDawGyi-Sirinandabhivamsa-22-06-2010.mp3">၈။ ၂၂-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/009-YawSayaDawGyi-Sirinandabhivamsa-24-06-2010.mp3">၉။ ၂၄-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/010-YawSayaDawGyi-Sirinandabhivamsa-25-06-2010.MP3">၁၀။ ၂၅-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/011-YawSayaDawGyi-Sirinandabhivamsa-27-06-2010.mp3">၁၁။ ၂၇-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/012-YawSayaDawGyi-Sirinandabhivamsa-28-06-2010.mp3">၁၂။ ၂၈-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/013-YawSayaDawGyi-Sirinandabhivamsa-29-06-2010.mp3">၁၃။ ၂၉-၆-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/014-YawSayaDawGyi-Sirinandabhivamsa-06-07-2010.mp3">၁၄။ ၆-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/015-YawSayaDawGyi-Sirinandabhivamsa-07-07-2010.mp3">၁၅။ ၇-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/016-YawSayaDawGyi-Sirinandabhivamsa-08-07-2010.mp3">၁၆။ ၈-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/017-YawSayaDawGyi-Sirinandabhivamsa-09-07-2010.mp3">၁၇။ ၉-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/018-YawSayaDawGyi-Sirinandabhivamsa-10-07-2010.mp3">၁၈။ ၁၀-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/019-YawSayaDawGyi-Sirinandabhivamsa-17-07-2010.mp3">၁၉။ ၁၇-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/020-YawSayaDawGyi-Sirinandabhivamsa-20-07-2010.mp3">၂၀။ ၂၀-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/021-YawSayaDawGyi-Sirinandabhivamsa-21-07-2010.mp3">၂၁။ ၂၁-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/022-YawSayaDawGyi-Sirinandabhivamsa-22-07-2010.mp3">၂၂။ ၂၂-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/023-YawSayaDawGyi-Sirinandabhivamsa-28-07-2010.mp3">၂၃။ ၂၈-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/024-YawSayaDawGyi-Sirinandabhivamsa-29-07-2010.mp3">၂၄။ ၂၉-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/025-YawSayaDawGyi-Sirinandabhivamsa-30-07-2010.mp3">၂၅။ ၃၀-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/026-YawSayaDawGyi-Sirinandabhivamsa-31-07-2010.mp3">၂၆။ ၃၁-၇-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/027-YawSayaDawGyi-Sirinandabhivamsa-01-08-2010.mp3">၂၇။ ၁-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/028-YawSayaDawGyi-Sirinandabhivamsa-05-08-2010.mp3">၂၈။ ၅-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/029-YawSayaDawGyi-Sirinandabhivamsa-06-08-2010.mp3">၂၉။ ၆-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/030-YawSayaDawGyi-Sirinandabhivamsa-07-08-2010.mp3">၃၀။ ၇-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/031-YawSayaDawGyi-Sirinandabhivamsa-08-08-2010.mp3">၃၁။ ၈-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/032-YawSayaDawGyi-Sirinandabhivamsa-09-08-2010.mp3">၃၂။ ၉-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/033-YawSayaDawGyi-Sirinandabhivamsa-11-08-2010.mp3">၃၃။ ၁၁-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/034-YawSayaDawGyi-Sirinandabhivamsa-12-08-2010.mp3">၃၄။ ၁၂-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/035-YawSayaDawGyi-Sirinandabhivamsa-13-08-2010.mp3">၃၅။ ၁၃-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/036-YawSayaDawGyi-Sirinandabhivamsa-14-08-2010.mp3">၃၆။ ၁၄-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/037-YawSayaDawGyi-Sirinandabhivamsa-16-08-2010.mp3">၃၇။ ၁၆-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/038-YawSayaDawGyi-Sirinandabhivamsa-17-08-2010.mp3">၃၈။ ၁၇-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/039-YawSayaDawGyi-Sirinandabhivamsa-19-08-2010.mp3">၃၉။ ၁၉-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/040-YawSayaDawGyi-Sirinandabhivamsa-20-08-2010.mp3">၄၀။ ၂၀-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/041-YawSayaDawGyi-Sirinandabhivamsa-21-08-2010.MP3">၄၁။ ၂၁-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/042-YawSayaDawGyi-Sirinandabhivamsa-22-08-2010.mp3">၄၂။ ၂၂-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/043-YawSayaDawGyi-Sirinandabhivamsa-23-08-2010.mp3">၄၃။ ၂၃-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/044-YawSayaDawGyi-Sirinandabhivamsa-24-08-2010.MP3">၄၄။ ၂၄-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/045-YawSayaDawGyi-Sirinandabhivamsa-26-08-2010.mp3">၄၅။ ၂၆-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/046-YawSayaDawGyi-Sirinandabhivamsa-27-08-2010.mp3">၄၆။ ၂၇-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/047-YawSayaDawGyi-Sirinandabhivamsa-28-08-2010.mp3">၄၇။ ၂၈-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/048-YawSayaDawGyi-Sirinandabhivamsa-29-08-2010.mp3">၄၈။ ၂၉-၈-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/049-YawSayaDawGyi-Sirinandabhivamsa-04-09-2010.mp3">၄၉။ ၄-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/050-YawSayaDawGyi-Sirinandabhivamsa-05-09-2010.mp3">၅၀။ ၅-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/051-YawSayaDawGyi-Sirinandabhivamsa-06-09-2010.mp3">၅၁။ ၆-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/052-YawSayaDawGyi-Sirinandabhivamsa-07-09-2010.mp3">၅၂။ ၇-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/053-YawSayaDawGyi-Sirinandabhivamsa-09-09-2010.mp3">၅၃။ ၉-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/054-YawSayaDawGyi-Sirinandabhivamsa-10-09-2010.mp3">၅၄။ ၁၀-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/055-YawSayaDawGyi-Sirinandabhivamsa-11-09-2010.mp3">၅၅။ ၁၁-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/056-YawSayaDawGyi-Sirinandabhivamsa-12-09-2010.mp3">၅၆။ ၁၂-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/057-YawSayaDawGyi-Sirinandabhivamsa-13-09-2010.mp3">၅၇။ ၁၃-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/058-YawSayaDawGyi-Sirinandabhivamsa-14-09-2010.mp3">၅၈။ ၁၄-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/059-YawSayaDawGyi-Sirinandabhivamsa-15-09-2010.mp3">၅၉။ ၁၅-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/060-YawSayaDawGyi-Sirinandabhivamsa-17-09-2010.MP3">၆၀။ ၁၇-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/061-YawSayaDawGyi-Sirinandabhivamsa-18-09-2010.mp3">၆၁။ ၁၈-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/062-YawSayaDawGyi-Sirinandabhivamsa-19-09-2010.mp3">၆၂။ ၁၉-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/063-YawSayaDawGyi-Sirinandabhivamsa-20-09-2010.mp3">၆၃။ ၂၀-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/064-YawSayaDawGyi-Sirinandabhivamsa-22-09-2010.mp3">၆၄။ ၂၂-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/065-YawSayaDawGyi-Sirinandabhivamsa-24-09-2010.mp3">၆၅။ ၂၄-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/066-YawSayaDawGyi-Sirinandabhivamsa-25-09-2010.mp3">၆၆။ ၂၅-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/067-YawSayaDawGyi-Sirinandabhivamsa-26-09-2010.mp3">၆၇။ ၂၆-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/068-YawSayaDawGyi-Sirinandabhivamsa-27-09-2010.mp3">၆၈။ ၂၇-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/069-YawSayaDawGyi-Sirinandabhivamsa-28-09-2010.mp3">၆၉။ ၂၈-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/070-YawSayaDawGyi-Sirinandabhivamsa-29-09-2010.mp3">၇၀။ ၂၉-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/071-YawSayaDawGyi-Sirinandabhivamsa-30-09-2010.mp3">၇၁။ ၃၀-၉-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/072-YawSayaDawGyi-Sirinandabhivamsa-02-10-2010.MP3">၇၂။ ၂-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/073-YawSayaDawGyi-Sirinandabhivamsa-03-10-2010.mp3">၇၃။ ၃-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/074-YawSayaDawGyi-Sirinandabhivamsa-05-10-2010.mp3">၇၄။ ၅-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/075-YawSayaDawGyi-Sirinandabhivamsa-06-10-2010.MP3">၇၅။ ၆-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/076-YawSayaDawGyi-Sirinandabhivamsa-07-10-2010.mp3">၇၆။ ၇-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/077-YawSayaDawGyi-Sirinandabhivamsa-09-10-2010.mp3">၇၇။ ၈-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/078-YawSayaDawGyi-Sirinandabhivamsa-10-10-2010.mp3">၇၈။ ၁၀-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/079-YawSayaDawGyi-Sirinandabhivamsa-11-10-2010.mp3">၇၉။ ၁၁-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/080-YawSayaDawGyi-Sirinandabhivamsa-12-10-2010.mp3">၈၀။ ၁၂-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/081-YawSayaDawGyi-Sirinandabhivamsa-13-10-2010.mp3">၈၁။ ၁၃-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/082-YawSayaDawGyi-Sirinandabhivamsa-14-10-2010.mp3">၈၂။ ၁၄-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/083-YawSayaDawGyi-Sirinandabhivamsa-15-10-2010.mp3">၈၃။ ၁၅-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/084-YawSayaDawGyi-Sirinandabhivamsa-19-10-2010.mp3">၈၄။ ၁၉-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/085-YawSayaDawGyi-Sirinandabhivamsa-20-10-2010.mp3">၈၅။ ၂၀-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/086-YawSayaDawGyi-Sirinandabhivamsa-25-10-2010.mp3">၈၆။ ၂၆-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/087-YawSayaDawGyi-Sirinandabhivamsa-27-10-2010.mp3">၈၇။ ၂၇-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/088-YawSayaDawGyi-Sirinandabhivamsa-28-10-2010.mp3">၈၈။ ၂၈-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/089-YawSayaDawGyi-Sirinandabhivamsa-29-10-2010.mp3">၈၉။ ၂၉-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/090-YawSayaDawGyi-Sirinandabhivamsa-30-10-2010.mp3">၉၀။ ၃၀-၁၀-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/091-YawSayaDawGyi-Sirinandabhivamsa-01-11-2010.mp3">၉၁။ ၁-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/092-YawSayaDawGyi-Sirinandabhivamsa-02-11-2010.MP3">၉၂။ ၂-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/093-YawSayaDawGyi-Sirinandabhivamsa-03-11-2010.mp3">၉၃။ ၃-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/094-YawSayaDawGyi-Sirinandabhivamsa-04-11-2010.mp3">၉၄။ ၄-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/095-YawSayaDawGyi-Sirinandabhivamsa-05-11-2010.mp3">၉၅။ ၅-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/096-YawSayaDawGyi-Sirinandabhivamsa-07-11-2010.mp3">၉၆။ ၇-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/097-YawSayaDawGyi-Sirinandabhivamsa-16-11-2010.mp3">၉၇။ ၁၆-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/098-YawSayaDawGyi-Sirinandabhivamsa-17-11-2010.mp3">၉၈။ ၁၇-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/099-YawSayaDawGyi-Sirinandabhivamsa-18-11-2010.mp3">၉၉။ ၁၈-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/100-YawSayaDawGyi-Sirinandabhivamsa-19-11-2010.mp3">၁၀၀။ ၁၉-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/101-YawSayaDawGyi-Sirinandabhivamsa-20-11-2010.mp3">၁၀၁။ ၂၀-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/102-YawSayaDawGyi-Sirinandabhivamsa-23-11-2010.mp3">၁၀၂။ ၂၃-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/103-YawSayaDawGyi-Sirinandabhivamsa-24-11-2010.mp3">၁၀၃။ ၂၄-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/104-YawSayaDawGyi-Sirinandabhivamsa-26-11-2010.mp3">၁၀၄။ ၂၆-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/105-YawSayaDawGyi-Sirinandabhivamsa-27-11-2010.mp3">၁၀၅။ ၂၇-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/106-YawSayaDawGyi-Sirinandabhivamsa-28-11-2010.mp3">၁၀၆။ ၂၈-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/107-YawSayaDawGyi-Sirinandabhivamsa-29-11-2010.mp3">၁၀၇။ ၂၉-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/108-YawSayaDawGyi-Sirinandabhivamsa-30-11-2010.mp3">၁၀၈။ ၃၀-၁၁-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/109-YawSayaDawGyi-Sirinandabhivamsa-01-12-2010.mp3">၁၀၉။ ၁-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/110-YawSayaDawGyi-Sirinandabhivamsa-02-12-2010.MP3">၁၁၀။ ၂-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/111-YawSayaDawGyi-Sirinandabhivamsa-03-12-2010.mp3">၁၁၁။ ၃-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/112-YawSayaDawGyi-Sirinandabhivamsa-04-12-2010.mp3">၁၁၂။ ၄-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/113-YawSayaDawGyi-Sirinandabhivamsa-05-12-2010.mp3">၁၁၃။ ၅-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/114-YawSayaDawGyi-Sirinandabhivamsa-07-12-2010.mp3">၁၁၄။ ၇-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/115-YawSayaDawGyi-Sirinandabhivamsa-08-12-2010.mp3">၁၁၅။ ၈-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/116-YawSayaDawGyi-Sirinandabhivamsa-09-12-2010.mp3">၁၁၆။ ၉-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/117-YawSayaDawGyi-Sirinandabhivamsa-10-12-2010.mp3">၁၁၇။ ၁၀-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/118-YawSayaDawGyi-Sirinandabhivamsa-15-12-2010.mp3">၁၁၈။ ၁၅-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/119-YawSayaDawGyi-Sirinandabhivamsa-16-12-2010.mp3">၁၁၉။ ၁၆-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/120-YawSayaDawGyi-Sirinandabhivamsa-17-12-2010.mp3">၁၂၀။ ၁၇-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/121-YawSayaDawGyi-Sirinandabhivamsa-18-12-2010.mp3">၁၂၁။ ၁၈-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/122-YawSayaDawGyi-Sirinandabhivamsa-19-12-2010.mp3">၁၂၂။ ၁၉-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/123-YawSayaDawGyi-Sirinandabhivamsa-22-12-2010.mp3">၁၂၃။ ၂၂-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/124-YawSayaDawGyi-Sirinandabhivamsa-23-12-2010.mp3">၁၂၄။ ၂၃-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/125-YawSayaDawGyi-Sirinandabhivamsa-24-12-2010.mp3">၁၂၅။ ၂၄-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/126-YawSayaDawGyi-Sirinandabhivamsa-25-12-2010.mp3">၁၂၆။ ၂၅-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/127-YawSayaDawGyi-Sirinandabhivamsa-26-12-2010.mp3">၁၂၇။ ၂၆-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2010/128-YawSayaDawGyi-Sirinandabhivamsa-27-12-2010.mp3">၁၂၈။ ၂၇-၁၂-၂၀၁၀ စာခ်တန္းစာဝါ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၂၀၁၁-၂၀၁၂ စာခ်တန္းစာဝါမ်ား</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/001-YawSayaDawGyi-Sirinandabhivamsa-26-05-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁</font></span><font size="4">။ 
၂၆-၅-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/002-YawSayaDawGyi-Sirinandabhivamsa-27-05-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂</font></span><font size="4">။ 
၂၇-၅-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/003-YawSayaDawGyi-Sirinandabhivamsa-28-05-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃</font></span><font size="4">။ 
၂၈-၅-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/004-YawSayaDawGyi-Sirinandabhivamsa-29-05-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄</font></span><font size="4">။ 
၂၉-၅-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/005-YawSayaDawGyi-Sirinandabhivamsa-30-05-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅</font></span><font size="4">။ 
၃၀-၅-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/006-YawSayaDawGyi-Sirinandabhivamsa-31-05-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆</font></span><font size="4">။ 
၃၁-၅-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/007-YawSayaDawGyi-Sirinandabhivamsa-02-06-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇</font></span><font size="4">။ 
၂-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/008-YawSayaDawGyi-Sirinandabhivamsa-12-06-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈</font></span><font size="4">။ 
၁၂-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/009-YawSayaDawGyi-Sirinandabhivamsa-14-06-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉</font></span><font size="4">။ 
၁၄-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/010-YawSayaDawGyi-Sirinandabhivamsa-15-06-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀</font></span><font size="4">။ 
၁၅-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/011-YawSayaDawGyi-Sirinandabhivamsa-18-06-2011.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁</font></span><font size="4">။ 
၁၈-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/012-YawSayaDawGyi-Sirinandabhivamsa-19-06-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂</font></span><font size="4">။ 
၁၉-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/013-YawSayaDawGyi-Sirinandabhivamsa-20-06-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃</font></span><font size="4">။ 
၂၀-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/014-YawSayaDawGyi-Sirinandabhivamsa-21-06-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄</font></span><font size="4">။ 
၂၁-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/015-YawSayaDawGyi-Sirinandabhivamsa-22-06-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅</font></span><font size="4">။ 
၂၂-၆-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/016-YawSayaDawGyi-Sirinandabhivamsa-01-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၆</font></span><font size="4">။ 
၁-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/017-YawSayaDawGyi-Sirinandabhivamsa-02-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၇</font></span><font size="4">။ 
၂-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/018-YawSayaDawGyi-Sirinandabhivamsa-03-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၈</font></span><font size="4">။ 
၃-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/019-YawSayaDawGyi-Sirinandabhivamsa-04-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၉</font></span><font size="4">။ 
၄-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/020-YawSayaDawGyi-Sirinandabhivamsa-05-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၀</font></span><font size="4">။ 
၅-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/021-YawSayaDawGyi-Sirinandabhivamsa-06-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၁</font></span><font size="4">။ 
၆-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/022-YawSayaDawGyi-Sirinandabhivamsa-09-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၂</font></span><font size="4">။ 
၉-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/023-YawSayaDawGyi-Sirinandabhivamsa-09-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၃</font></span><font size="4">။ 
၉-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/024-YawSayaDawGyi-Sirinandabhivamsa-10-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၄</font></span><font size="4">။ 
၁၀-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/025-YawSayaDawGyi-Sirinandabhivamsa-11-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၅</font></span><font size="4">။ 
၁၁-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/026-YawSayaDawGyi-Sirinandabhivamsa-17-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၆</font></span><font size="4">။ 
၁၇-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/027-YawSayaDawGyi-Sirinandabhivamsa-18-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၇</font></span><font size="4">။ 
၁၈-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/028-YawSayaDawGyi-Sirinandabhivamsa-20-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၈</font></span><font size="4">။ 
၂၀-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/029-YawSayaDawGyi-Sirinandabhivamsa-21-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၂၉</font></span><font size="4">။ 
၂၁-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/030-YawSayaDawGyi-Sirinandabhivamsa-26-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၀</font></span><font size="4">။ 
၂၆-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/031-YawSayaDawGyi-Sirinandabhivamsa-27-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၁</font></span><font size="4">။ 
၂၇-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/032-YawSayaDawGyi-Sirinandabhivamsa-28-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၂</font></span><font size="4">။ 
၂၈-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/033-YawSayaDawGyi-Sirinandabhivamsa-29-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၃</font></span><font size="4">။ 
၂၉-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/034-YawSayaDawGyi-Sirinandabhivamsa-31-07-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၄</font></span><font size="4">။ 
၃၁-၇-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/035-YawSayaDawGyi-Sirinandabhivamsa-01-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၅</font></span><font size="4">။ 
၁-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/036-YawSayaDawGyi-Sirinandabhivamsa-02-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၆</font></span><font size="4">။ 
၂-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/037-YawSayaDawGyi-Sirinandabhivamsa-03-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၇</font></span><font size="4">။ 
၃-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/038-YawSayaDawGyi-Sirinandabhivamsa-04-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၈</font></span><font size="4">။ 
၄-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/039-YawSayaDawGyi-Sirinandabhivamsa-09-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၃၉</font></span><font size="4">။ 
၉-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/040-YawSayaDawGyi-Sirinandabhivamsa-10-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၀</font></span><font size="4">။ 
၁၀-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/041-YawSayaDawGyi-Sirinandabhivamsa-11-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၁</font></span><font size="4">။ 
၁၁-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/042-YawSayaDawGyi-Sirinandabhivamsa-12-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၂</font></span><font size="4">။ 
၁၂-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/043-YawSayaDawGyi-Sirinandabhivamsa-13-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၃</font></span><font size="4">။ 
၁၃-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/044-YawSayaDawGyi-Sirinandabhivamsa-15-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၄</font></span><font size="4">။ 
၁၅-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/045-YawSayaDawGyi-Sirinandabhivamsa-16-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၅</font></span><font size="4">။ 
၁၆-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/046-YawSayaDawGyi-Sirinandabhivamsa-17-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၆</font></span><font size="4">။ 
၁၇-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/047-YawSayaDawGyi-Sirinandabhivamsa-18-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၇</font></span><font size="4">။ 
၁၈-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/048-YawSayaDawGyi-Sirinandabhivamsa-19-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၈</font></span><font size="4">။ 
၁၉-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/049-YawSayaDawGyi-Sirinandabhivamsa-20-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၄၉</font></span><font size="4">။ 
၂၀-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/050-YawSayaDawGyi-Sirinandabhivamsa-21-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၀</font></span><font size="4">။ 
၂၁-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/051-YawSayaDawGyi-Sirinandabhivamsa-23-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၁</font></span><font size="4">။ 
၂၃-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/052-YawSayaDawGyi-Sirinandabhivamsa-24-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၂</font></span><font size="4">။ 
၂၄-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/053-YawSayaDawGyi-Sirinandabhivamsa-25-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၃</font></span><font size="4">။ 
၂၅-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/054-YawSayaDawGyi-Sirinandabhivamsa-26-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၄</font></span><font size="4">။ 
၂၆-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/055-YawSayaDawGyi-Sirinandabhivamsa-27-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၅</font></span><font size="4">။ 
၂၇-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/056-YawSayaDawGyi-Sirinandabhivamsa-29-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၆</font></span><font size="4">။ 
၂၉-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/057-YawSayaDawGyi-Sirinandabhivamsa-30-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၇</font></span><font size="4">။ 
၃၀-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/058-YawSayaDawGyi-Sirinandabhivamsa-31-08-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၈</font></span><font size="4">။ 
၃၁-၈-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/059-YawSayaDawGyi-Sirinandabhivamsa-01-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၅၉</font></span><font size="4">။ 
၁-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/060-YawSayaDawGyi-Sirinandabhivamsa-02-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၀</font></span><font size="4">။ 
၂-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/061-YawSayaDawGyi-Sirinandabhivamsa-03-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၁</font></span><font size="4">။ 
၃-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/062-YawSayaDawGyi-Sirinandabhivamsa-04-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၂</font></span><font size="4">။ 
၄-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/063-YawSayaDawGyi-Sirinandabhivamsa-06-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၃</font></span><font size="4">။ 
၆-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/064-YawSayaDawGyi-Sirinandabhivamsa-07-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၄</font></span><font size="4">။ 
၇-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/065-YawSayaDawGyi-Sirinandabhivamsa-08-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၅</font></span><font size="4">။ 
၈-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/066-YawSayaDawGyi-Sirinandabhivamsa-09-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၆</font></span><font size="4">။ 
၉-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/067-YawSayaDawGyi-Sirinandabhivamsa-10-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၇</font></span><font size="4">။ 
၁၀-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/068-YawSayaDawGyi-Sirinandabhivamsa-11-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၈</font></span><font size="4">။ 
၁၁-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/069-YawSayaDawGyi-Sirinandabhivamsa-13-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၆၉</font></span><font size="4">။ 
၁၃-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/070-YawSayaDawGyi-Sirinandabhivamsa-14-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၀</font></span><font size="4">။ 
၁၄-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/071-YawSayaDawGyi-Sirinandabhivamsa-15-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၁</font></span><font size="4">။ 
၁၅-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/072-YawSayaDawGyi-Sirinandabhivamsa-16-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၂</font></span><font size="4">။ 
၁၆-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/073-YawSayaDawGyi-Sirinandabhivamsa-17-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၃</font></span><font size="4">။ 
၁၇-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/074-YawSayaDawGyi-Sirinandabhivamsa-18-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၄</font></span><font size="4">။ 
၁၈-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/075-YawSayaDawGyi-Sirinandabhivamsa-19-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၅</font></span><font size="4">။ 
၁၉-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/076-YawSayaDawGyi-Sirinandabhivamsa-21-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၆</font></span><font size="4">။ 
၂၁-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/077-YawSayaDawGyi-Sirinandabhivamsa-22-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၇</font></span><font size="4">။ 
၂၂-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/078-YawSayaDawGyi-Sirinandabhivamsa-23-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၈</font></span><font size="4">။ 
၂၃-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/079-YawSayaDawGyi-Sirinandabhivamsa-24-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၇၉</font></span><font size="4">။ 
၂၄-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/080-YawSayaDawGyi-Sirinandabhivamsa-25-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၀</font></span><font size="4">။ 
၂၅-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/081-YawSayaDawGyi-Sirinandabhivamsa-29-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၁</font></span><font size="4">။ 
၂၉-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/082-YawSayaDawGyi-Sirinandabhivamsa-30-09-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၂</font></span><font size="4">။ 
၃၀-၉-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/083-YawSayaDawGyi-Sirinandabhivamsa-01-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၃</font></span><font size="4">။ 
၁-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/084-YawSayaDawGyi-Sirinandabhivamsa-02-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၄</font></span><font size="4">။ 
၂-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/085-YawSayaDawGyi-Sirinandabhivamsa-03-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၅</font></span><font size="4">။ 
၃-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/086-YawSayaDawGyi-Sirinandabhivamsa-04-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၆</font></span><font size="4">။ 
၄-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/087-YawSayaDawGyi-Sirinandabhivamsa-06-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၇</font></span><font size="4">။ 
၅-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/088-YawSayaDawGyi-Sirinandabhivamsa-08-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၈</font></span><font size="4">။ 
၈-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/089-YawSayaDawGyi-Sirinandabhivamsa-09-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၈၉</font></span><font size="4">။ 
၉-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/090-YawSayaDawGyi-Sirinandabhivamsa-10-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၀</font></span><font size="4">။ 
၁၀-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/091-YawSayaDawGyi-Sirinandabhivamsa-14-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၁</font></span><font size="4">။ 
၁၄-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/092-YawSayaDawGyi-Sirinandabhivamsa-15-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၂</font></span><font size="4">။ 
၁၅-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/093-YawSayaDawGyi-Sirinandabhivamsa-16-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၃</font></span><font size="4">။ 
၁၆-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/094-YawSayaDawGyi-Sirinandabhivamsa-18-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၄</font></span><font size="4">။ 
၁၈-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/095-YawSayaDawGyi-Sirinandabhivamsa-25-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၅</font></span><font size="4">။ 
၂၅-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/096-YawSayaDawGyi-Sirinandabhivamsa-27-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၆</font></span><font size="4">။ 
၂၇-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/097-YawSayaDawGyi-Sirinandabhivamsa-28-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၇</font></span><font size="4">။ 
၂၈-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/098-YawSayaDawGyi-Sirinandabhivamsa-29-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၈</font></span><font size="4">။ 
၂၉-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/099-YawSayaDawGyi-Sirinandabhivamsa-30-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၉၉</font></span><font size="4">။ 
၃၀-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/100-YawSayaDawGyi-Sirinandabhivamsa-31-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၀</font></span><font size="4">။ 
၃၁-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/101-YawSayaDawGyi-Sirinandabhivamsa-31-10-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၁</font></span><font size="4">။ 
၃၁-၁၀-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/102-YawSayaDawGyi-Sirinandabhivamsa-01-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၂</font></span><font size="4">။ 
၁-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/103-YawSayaDawGyi-Sirinandabhivamsa-02-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၃</font></span><font size="4">။ 
၂-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/104-YawSayaDawGyi-Sirinandabhivamsa-04-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၄</font></span><font size="4">။ 
၄-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/105-YawSayaDawGyi-Sirinandabhivamsa-05-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၅</font></span><font size="4">။ 
၅-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/106-YawSayaDawGyi-Sirinandabhivamsa-06-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၆</font></span><font size="4">။ 
၆-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/107-YawSayaDawGyi-Sirinandabhivamsa-07-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၇</font></span><font size="4">။ 
၇-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/108-YawSayaDawGyi-Sirinandabhivamsa-08-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၈</font></span><font size="4">။ 
၈-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/109-YawSayaDawGyi-Sirinandabhivamsa-09-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၀၉</font></span><font size="4">။ 
၉-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/110-YawSayaDawGyi-Sirinandabhivamsa-11-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၀</font></span><font size="4">။ 
၁၁-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/111-YawSayaDawGyi-Sirinandabhivamsa-12-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၁</font></span><font size="4">။ 
၁၂-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/112-YawSayaDawGyi-Sirinandabhivamsa-13-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၂</font></span><font size="4">။ 
၁၃-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/113-YawSayaDawGyi-Sirinandabhivamsa-14-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၃</font></span><font size="4">။ 
၁၄-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/114-YawSayaDawGyi-Sirinandabhivamsa-15-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၄</font></span><font size="4">။ 
၁၅-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/115-YawSayaDawGyi-Sirinandabhivamsa-16-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၅</font></span><font size="4">။ 
၁၆-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/116-YawSayaDawGyi-Sirinandabhivamsa-17-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၆</font></span><font size="4">။ 
၁၇-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/117-YawSayaDawGyi-Sirinandabhivamsa-22-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၇</font></span><font size="4">။ 
၂၂-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/118-YawSayaDawGyi-Sirinandabhivamsa-23-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၈</font></span><font size="4">။ 
၂၃-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/119-YawSayaDawGyi-Sirinandabhivamsa-24-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၁၉</font></span><font size="4">။ 
၂၄-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/120-YawSayaDawGyi-Sirinandabhivamsa-26-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၀</font></span><font size="4">။ 
၂၆-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/121-YawSayaDawGyi-Sirinandabhivamsa-27-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၁</font></span><font size="4">။ 
၂၇-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/122-YawSayaDawGyi-Sirinandabhivamsa-28-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၂</font></span><font size="4">။ 
၂၈-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/123-YawSayaDawGyi-Sirinandabhivamsa-29-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၃</font></span><font size="4">။ 
၂၉-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/124-YawSayaDawGyi-Sirinandabhivamsa-30-11-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၄</font></span><font size="4">။ 
၃၀-၁၁-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/125-YawSayaDawGyi-Sirinandabhivamsa-02-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၅</font></span><font size="4">။ 
၂-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/126-YawSayaDawGyi-Sirinandabhivamsa-04-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၆</font></span><font size="4">။ 
၄-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/127-YawSayaDawGyi-Sirinandabhivamsa-06-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၇</font></span><font size="4">။ 
၆-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/128-YawSayaDawGyi-Sirinandabhivamsa-07-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၈</font></span><font size="4">။ 
၇-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/129-YawSayaDawGyi-Sirinandabhivamsa-08-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၂၉</font></span><font size="4">။ 
၈-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/130-YawSayaDawGyi-Sirinandabhivamsa-09-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၀</font></span><font size="4">။ 
၉-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/131-YawSayaDawGyi-Sirinandabhivamsa-11-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၁</font></span><font size="4">။ 
၁၁-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/132-YawSayaDawGyi-Sirinandabhivamsa-12-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၂</font></span><font size="4">။ 
၁၂-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/133-YawSayaDawGyi-Sirinandabhivamsa-13-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၃</font></span><font size="4">။ 
၁၃-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/134-YawSayaDawGyi-Sirinandabhivamsa-14-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၄</font></span><font size="4">။ 
၁၄-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/135-YawSayaDawGyi-Sirinandabhivamsa-15-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၅</font></span><font size="4">။ 
၁၅-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/136-YawSayaDawGyi-Sirinandabhivamsa-16-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၆</font></span><font size="4">။ 
၁၆-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/137-YawSayaDawGyi-Sirinandabhivamsa-17-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၇</font></span><font size="4">။ 
၁၇-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/138-YawSayaDawGyi-Sirinandabhivamsa-19-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၈</font></span><font size="4">။ 
၁၉-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/139-YawSayaDawGyi-Sirinandabhivamsa-20-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၃၉</font></span><font size="4">။ 
၂၀-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/140-YawSayaDawGyi-Sirinandabhivamsa-21-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၀</font></span><font size="4">။ 
၂၁-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/141-YawSayaDawGyi-Sirinandabhivamsa-22-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၁</font></span><font size="4">။ 
၂၂-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/142-YawSayaDawGyi-Sirinandabhivamsa-25-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၂</font></span><font size="4">။ 
၂၅-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/143-YawSayaDawGyi-Sirinandabhivamsa-26-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၃</font></span><font size="4">။ 
၂၆-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/144-YawSayaDawGyi-Sirinandabhivamsa-27-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၄</font></span><font size="4">။ 
၂၇-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/145-YawSayaDawGyi-Sirinandabhivamsa-28-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၅</font></span><font size="4">။ 
၂၈-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/146-YawSayaDawGyi-Sirinandabhivamsa-29-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၆</font></span><font size="4">။ 
၂၉-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/147-YawSayaDawGyi-Sirinandabhivamsa-30-12-2011.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၇</font></span><font size="4">။ 
၃၀-၁၂-၂၀၁၁ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/148-YawSayaDawGyi-Sirinandabhivamsa-02-01-2012.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၈</font></span><font size="4">။ 
၂-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/149-YawSayaDawGyi-Sirinandabhivamsa-03-01-2012.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၄၉</font></span><font size="4">။ 
၃-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/150-YawSayaDawGyi-Sirinandabhivamsa-04-01-2012.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၀</font></span><font size="4">။ 
၄-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/150-YawSayaDawGyi-Sirinandabhivamsa-04-01-2012.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၁</font></span><font size="4">။ 
၅-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt;text-kashida-space:
50%">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/152-YawSayaDawGyi-Sirinandabhivamsa-09-01-0212.mp3"><span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၂</font></span><font size="4">။ 
၉-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/153-YawSayaDawGyi-Sirinandabhivamsa-10-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၃</font></span><font size="4">။ 
၁၀-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/154-YawSayaDawGyi-Sirinandabhivamsa-11-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၄</font></span><font size="4">။ 
၁၁-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/155-YawSayaDawGyi-Sirinandabhivamsa-12-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၅</font></span><font size="4">။ 
၁၂-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/156-YawSayaDawGyi-Sirinandabhivamsa-13-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၆</font></span><font size="4">။ 
၁၃-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/157-YawSayaDawGyi-Sirinandabhivamsa-14-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၇</font></span><font size="4">။ 
၁၄-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/158-YawSayaDawGyi-Sirinandabhivamsa-15-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၈</font></span><font size="4">။ 
၁၅-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/159-YawSayaDawGyi-Sirinandabhivamsa-17-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၅၉</font></span><font size="4">။ 
၁၇-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/160-YawSayaDawGyi-Sirinandabhivamsa-18-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၆၀</font></span><font size="4">။ 
၁၈-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/161-YawSayaDawGyi-Sirinandabhivamsa-19-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၆၁</font></span><font size="4">။ 
၁၉-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="msotagline" style="margin:0cm;margin-bottom:.0001pt">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/Sarwar/Sarwar-2011-2012/162-YawSayaDawGyi-Sirinandabhivamsa-20-01-2012.mp3">
<span style="font-family: Zawgyi-One,sans-serif"><font size="4">၁၆၂</font></span><font size="4">။ 
၂၀-၁-၂၀၁၂ စာခ်တန္းစာဝါ</font></a></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
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
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font color="#800080">
	<span style="font-family: Times New Roman;">
	<font size="6">Yaw SayaDaw&nbsp; Sireindabhivamsa</font></span></font></div>

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
            if '.mp3' in key.get('href') or '.MP3' in key.get('href'):
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
    
