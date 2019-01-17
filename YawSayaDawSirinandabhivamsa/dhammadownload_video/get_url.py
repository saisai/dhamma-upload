from bs4 import BeautifulSoup as bs4

text = """
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
<a href="https://www.facebook.com/groups/dhammadownload/?ref=br_rs#">
<img src="images/facebook-logo.gif" width="159" height="59" border="0"></a></div>



<!-- end dhammadownload menu top and side bar -->






	
	
	
	
<div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 219px; top: 156px" id="layer24" font="" face="Zawgyi-One">
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
									Yaw SayaDaw Gyi Sirinandabhivamsa</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One"><font size="5">
									တိပိဋကဓရ-အဂၢမဟာပ႑ိတ</font></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One"><font size="5">
									ေယာဆရာေတာ္ဘုရားႀကီး ဘဒၵႏၲသီရိႏၵာဘိဝံသ</font></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
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
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-PahtanPrayer.mp4">
<font size="5">ပ႒ာန္း တရားေတာ္</font></a></p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">****dhamma talks 
uploaded and published on 13 April 2010****</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">DVD 01</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/001-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၁။ ကိုယ္ပိုင္ အလုပ္ ဥစၥာထုပ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/002-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၂။ ေမတၱာအစြမ္း စိတ္ေအးခ်မ္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/003-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၃။ ႏႈတ္ဆက္မဂၤလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/004-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၄။ တစ္ခါလာလည္း ဒါပဲ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/005-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၅။ ေန႕စဥ္ဆင္ႏႊဲ လူ႕ေအာင္ပြဲ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/006-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၆။ အခ်စ္ဆုံးေဆြမ်ိဳး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/007-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၇။ လူ႕ဘဝထဲ စာေမးပြဲ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/008-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၈။ ေမတၱာအစစ္ လူ႕အခ်စ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/009-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၉။ ဂုဏ္ျပဳခ်ီးက်ဴး စြမ္းရည္ထူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-01/010-YawSayaDawGyiSiriNandaBhivamsa-DVD01.mp4">၁၀။ ခႏၶာကိုယ္ထဲ ေဘာလုံးပြဲ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">****dhamma talks 
uploaded and published on 20 Nov 2011****</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">DVD 02</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/001-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၁။ အႏ ၱရာယ္ကင္း ပရိတ္တရားေတာ္မ်ား</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/002-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၂။ ၁၇-၁၁-၂၀၀၉ ေမတၱာျဖဴေဖြး အလႈေပး တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/003-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၃။ ၁-၃-၂၀၀၉&nbsp; ေမတၱာကိုင္စြဲ လူ႕ေအာင္ပြဲ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/004-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၄။ ၁၃-၈-၂၀၀၇ အခ်စ္တုံး ေဆြမ်ိဳး တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/005-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၅။ ၁၈-၁-၂၀၀၉ လူသားေမတၱာ ဤကမာၻ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/006-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၆။ ၈-၁၁-၂၀၀၉ ေမတၱာလက္တြဲ ကုသိုလ္ပြဲ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/007-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၇။ ၁၄-၄-၂၀၀၄ ဘဝတေခါက္ ခဏေရာက္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-02/008-YawSayaDawGyiSiriNandaBhivamsa-DVD02.mp4">၈။ ၂၆-၇-၂၀၁၀ ကိုယ့္ဒုကၡနဲ႕ ကိုယ္ေနပါ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">DVD 03</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/01-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၁။ ေမတၱာကိုင္စြဲ လူ႕ေအာင္ပြဲ (၂-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/02-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၂။ သတိကိုင္စြဲ လမ္းဖြင့္ပြဲ (၃-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/03-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၃။ ဗုဒၶျမတ္စြာ တို႕ဆရာ (၄-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/04-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၄။ ကိုယ့္ကိုကိုယ္သာ ေရြးယူပါ (၅-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/05-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၅။ ေမတၱာလက္တြဲ ကုသိုလ္ပြဲ (၆-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/06-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၆။ ထိုက္တန္သူမွ ကုသိုလ္ရ (၇-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD03/07-yawsayadawgyisirinandabhivamsa-dvd03.mp4">
<font size="4">၇။ ေမတၱာကိုင္စြဲ ဆြမ္းေအာင္ပြဲ (၈-၁-၂၀၁၀)</font></a></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">DVD 2014</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/001-YawSayaDawGyiSiriNandaBhivamsa-2014-12-29.mp4">
၁။ ၂၉-၁၂-၂၀၁၄ စိတ္ဓါတ္စင္ျဖဴ ျမတ္အလွဴ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/002-YawSayaDawGyiSiriNandaBhivamsa-2014-4-3.mp4">
၂။ ၃-၄-၂၀၁၄ ကိုယ့္လမ္းကိုယ္ေလွ်ာက္ လိုရာေရာက္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/003-YawSayaDawGyiSiriNandaBhivamsa-2014-4-3.mp4">
၃။ ၃-၄-၂၀၁၄ ညေန ကိုယ့္လမ္း ကိုယ္သြား ျမတ္တရား တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/004-YawSayaDawGyiSiriNandaBhivamsa-2014-4-4.mp4">
၄။ ၄-၄-၂၀၁၄ ကုသိုလ္ျပည္႕ႂကြယ္ ရက္ပတ္လည္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/005-YawSayaDawGyiSiriNandaBhivamsa-2014-4-5.mp4">
၅။ ၅-၄-၂၀၁၄ စြမ္းအားတိုးတက္ ႏွစ္အသစ္တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/006-YawSayaDawGyiSiriNandaBhivamsa-2014-4-6.mp4">
၆။ ၆-၄-၂၀၁၄ အေျပာင္းျမန္ဆန္ အေကာင္းက်န္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/007-YawSayaDawGyiSiriNandaBhivamsa-2014-4-11.mp4">
၇။ ၁၁-၄-၂၀၁၄ " အား " တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/DVD-2014/008-YawSayaDawGyiSiriNandaBhivamsa-2014-4-14.mp4">
၈။ ၁၄-၄-၂၀၁၄ အရြယ္ရွိခိုက္ လုံ႕လစိုက္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyi-SiriNanda-Bhivamsa-2013-5-15-birthday-invitation.mp4">၁၅-၅-၂၀၁၃ ေမြးေန႕မဂၤလာ ဖိတ္ၾကားလႊာ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-2012-9-15-AhYinPhetTharShwlYoupar.mp4">
၁၅-၉-၂၀၁၂ အရင္းဘက္သာ ဆြဲယူပါ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-2011-3-24-birthday-mingala.mp4">၂၄-၃-၂၀၁၁ ေမြးေန႕အခါ မဂၤလာ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-2014-10-26-Kyanmarshwinlanmettaswan.mp4">
၂၆-၁၀-၂၀၁၄ က်န္းမာရွင္လန္း ေမတၱာစြမ္း တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-2010-1-11-birthday-mingala.mp4">၁၀-၁-၂၀၁၀ ေမြးေန႕မဂၤလာ ရတနာ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-2008-10-22-LetSaung.mp4">
၂၂-၁၀-၂၀၀၈ လက္ေဆာင္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/YawSayaDawGyi-SiriNanda-Bhivamsa/YawSayaDawGyiSiriNandaBhivamsa-2009-10-27.mp4">၂၇-၁၀-၂၀၀၉ ေခြးကိုက္တတ္သည္၊ သတိျပဳ တရားေတာ္</a></font></p>
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
<font size="4">တရားေဆာင္သူ စိတ္မပူ တရားေတာ္<br>
နေမာတႆ တရားေတာ္<br>
ပရိတ္ (၄) သုတ္<br>
လူ၏တြန္းအား ျမတ္တရား တရားေတာ္<br>
သူဦး ကိုယ္ဦး သံုးႁမႊာပူး တရားေတာ္ (သံုးမႊာ / သံုးႁမႊာ 
ေက်းဇူးျပဳ၍စာလံုးေပါင္းစစ္ေပးရန္။)<br>
အိုပဲြမဂၤလာ ရတနာ တရားေတာ္<br>
လူသားေမတၱာ ဤကမာၻတရားေတာ္<br>
မိခင္စိတ္ဓာတ္ ေမတၱာျမတ္ တရားေတာ္<br>
တစ္ခါလာလည္း ဒါပါပဲ<br>
ကုသိုလ္လည္းရ ဝမ္းလည္းဝ<br>
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္<br>
ေမတၱာေပါင္းစု ျမတ္ေကာင္းမႈ<br>
ႏွလံုးသားဝယ္ စြမ္းအားႂကြယ္<br>
ေအးျမရႊင္ၿပံဳး လူ႕ႏွလံုး<br>
ႏွစ္သစ္မဂၤလာ ရက္ရာဇာ<br>
ဂုဏ္ျပဳခ်ီးက်ဴး စြမ္းရည္ထူး<br>
&nbsp;</font></p>
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
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One"><br>
&nbsp;</font></p>
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
	<font size="6">Yaw SayaDaw Sirinandabhivamsa</font></span></font></div>

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
    files = ['.mp4', '.wmv']
    for key in soup.find_all('a'):
        #if ''
        ext = key.get('href').split('/')[-1].split('.')[-1]
        if 'mp4' in ext or 'wmv' in ext:
            #print(key.get('href').split('/')[-1].split('.')[-1])
            counter = '{:03d}'.format(count)
            #print('{}.{}|{}|{}'.format(counter, ext, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.{}|{}|{}\n'.format(counter, ext, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())
            
            count += 1        
    
