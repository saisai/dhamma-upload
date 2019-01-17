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






	
	
	
	
</font><div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 219px; top: 156px" id="layer24" font="" face="Zawgyi-One"><font face="Zawgyi-One">
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
									Yaw SayaDaw Sirinandabhivamsa</font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One"><font size="5">
									တိပိဋကဓရ-အဂၢမဟာပ႑ိတ</font></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One"><font size="5">
									ေယာဆရာေတာ္ဘုရားႀကီး ဘဒၵႏၲသီရိႏၵာဘိဝံသ</font></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား<br>
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								********************</p>
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
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left"><u><b>တရားေတာ္မ်ား 
စုစည္းမႈ (၈၆၁) ပုဒ္</b></u></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-001-1987.mp3">၁။ အာဠာဝကသုတၱန္ 
(၁၉၈၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-002-1987.mp3">၂။ အာဠာဝကသုတၱန္ 
(၁၉၈၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-003-1992-04-22.mp3">၃။ 
စိတ္ဓာတ္ကိုျမႇင့္လုပ္ကိုင္ခြင့္ (၂၂.၄.၉၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-004-1992-04-20.mp3">၄။ 
အၾကမ္းအႏုစိတ္ကိုလု (၂၀.၄.၉၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-005-1992-03-25.mp3">၅။ 
သိကၡာသံုးပါးလူ႔စြမ္းအား (၂၅.၃.၉၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-006-1992-03-09.mp3">၆။ 
ဆင္းရဲ၏ေနာက္ခ်မ္းသာေရာက္ (၂၉.၃.၉၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-007-1993-03-30.mp3">၇။ပညာဦးစီးအလွဴႀကီး 
(၃၀.၃.၉၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-008-1993-01-26.mp3">၈။ ေမတၱာအလုပ္ခႏၶသုတ္ 
(၂၆.၁.၉၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-009-1994-01-06.mp3">၉။ 
ကုသိုလ္ထံုအမြမ္းလူ႔အစြမ္း (၆.၁.၉၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-010-1994-10-15.mp3">၁၀။ 
တရားေစာင့္သူစိတ္မပူ (၁၅.၁၀.၉၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-011-1994-11-26.mp3">၁၁။ 
စင္ၾကယ္ျမင့္ျမတ္လူ႔စိတ္ဓာတ္ (၂၆.၁၁.၉၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-012-1995-04-18.mp3">၁၂။ တရားျပည့္ဝအရိပ္ရ 
(၁၈.၄.၉၅)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-013-1995-11-05.mp3">၁၃။ 
အလွဴေက်းဇူးစြမ္းရည္ထူး (၅.၁၁.၉၅)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-014-1996-04-18.mp3">၁၄။ ပရိတ္ႀကီး 
(၄)သုတ္+ (၅)သုတ္ (၁၈.၄.၉၆)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-015-1996-04-15.mp3">၁၅။ 
ေမတၱာေက်းဇူးစြမ္းရည္ထူးႏွင့္ပရိတ္ (၄) သုတ္ (၁၅.၄.၉၆)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-016-1997-03-12.mp3">၁၆။ အသီးတရာအညႇာတခု 
(၁၂.၃.၉၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-017-1996-04-16.mp3">၁၇။ 
သံုးပါးျမတ္စြာမဂၤလာ (၁၆.၄.၉၆)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-018-1998-01-30.mp3">၁၈။ 
စိတ္ေကာင္းထားကမိတ္ေကာင္းရ (၃၀.၁.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-019-1998-03-08.mp3">၁၉။ နေမာဗုဒၶႆ 
(၈.၃.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-020-1998-01-10.mp3">၂၀။ 
အသိမွန္ကန္အဖိုးတန္ (၁၀.၁.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-021-1997-11-15.mp3">၂၁။ 
စိတ္ကိုႏိုင္မွခ်မ္းသာရ (၁၅.၁၁.၉၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-022-1998-03-12.mp3">၂၂။ 
ေမတၱာႏွလံုးအလွဆံုး (၁၂.၃.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-023-1998-05-10.mp3">၂၃။ 
ရဲရင့္စြန္႔စားမိန္းမသား (၁၀.၅.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-024-1998-10-18.mp3">၂၄။ 
အျဖဴအမဲႏွစ္လမ္းကြဲ (၁၈.၁၀.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-025-1999-02-24.mp3">၂၅။ 
အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၂၄.၂.၉၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-026-1999-03-27.mp3">၂၆။ 
အသိထူးျခားလူ႔စြမ္းအား (၂၇.၃.၉၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-027-1998-12-23.mp3">၂၇။ 
ပ႒ာန္းေက်းဇူးစြမ္းရည္ထူး (၂၃.၁၂.၉၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-028-1999-11-22.mp3">၂၈။ 
ႏွလံုးသားဝယ္ဘုရားတည္ (၂၂.၁၁.၉၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-029-1999-11-21.mp3">၂၉။ 
အသိမွန္ကန္အဖိုးတန္ (၂၁.၁၁.၉၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-030-1999-10-24.mp3">၃၀။ 
လူ၏စြမ္းအားျမတ္တရား (၂၄.၁၀.၉၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-031-1999-11-22.mp3">၃၁။ 
ကုသိုလ္လည္းရဝမ္းလည္းဝ (၂၂.၁၁.၉၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-032-2000-12-29.mp3">၃၂။ 
ေမတၱာႏွလံုးအလွဆံုး (၂၉.၁၂.၂၀၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-033-2000-01-18.mp3">၃၃။ အသီးတရာအညႇာတစ္ခု 
(၁၈.၁.၂၀၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-034-2000-09-03.mp3">၃၄။ 
အသိလက္ဦးစြမ္းရည္ထူး (၃.၉.၂၀၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-035-2000-09-20.mp3">၃၅။ 
ေမတၱာလႊမ္းျခံဳေဘးရန္လံု (၂၀.၉.၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-036-2000-11-09.mp3">၃၆။ 
ဘဝတန္ဖိုးလူ႔တန္ခိုး (၉.၁၁.၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-037-2001-04-22.mp3">၃၇။ 
ႏွစ္သစ္မဂၤလာရက္ရာဇာ (၂၂.၁၁.၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-038-2001-04-15.mp3">၃၈။ 
အခ်ိန္ကိုထိန္းအပူၿငိမ္း (၁၅.၁၂.၀၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-039-2001-02-04.mp3">၃၉။ 
ပစၥည္းတန္ဖိုးလူ႔တန္ခိုး (၄.၂.၀၁)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-040-2001-05-30.mp3">၄၀။ 
ႏွလံုးသားဝယ္တရားတည္ (၃၀.၅.၀၁)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-041-2001-05-20.mp3">၄၁။ 
အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၂၀.၅.၀၁)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-042-2001-11-25.mp3">၄၂။ 
ထိုက္တန္သူမွေကာင္းတာရ (၂၅.၁၁.၀၁)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-043-2001-12-28.mp3">၄၃။ 
အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၂၈.၁၂.၀၁)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-044-2002-01-09.mp3">၄၄။ 
ထိုက္တန္သူမွေကာင္းတာရ (၉.၁.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-045-2002-02-28.mp3">၄၅။ 
ေအးျမရႊင္ျပံဳးလူ႔ႏွလံုး (၂၈.၂.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-046-2002-03-04.mp3">၄၆။ 
စိတ္ေအးစရာလူ႔ခ်မ္းသာ (၄.၃.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-047-2002-09-18.mp3">၄၇။ 
ဘဝတစ္ေခါက္ခဏေရာက္ (၁၈.၉.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-048-2002-10-06.mp3">၄၈။ 
အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၆.၁၀.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-049-2002-11-02.mp3">၄၉။ 
ခႏၶာကိုယ္ထဲေဘာလံုးပြဲ (၂.၁၁.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-050-2002-12-17.mp3">၅၀။ သာဓုတရား 
(၁၇.၁၂.၀၂)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-051-2003-01-18.mp3">၅၁။ 
မီးသတိျပဳတရားေတာ္ (၁၈.၁.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-052-2003-02-16.mp3">၅၂။ 
လူ၏စြမ္းအားျမတ္တရား (၁၆.၂.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-053-2003-03-07.mp3">၅၃။ 
ႏွလံုးသားဝယ္ဘုရားတည္ (၇.၃.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-054-2003-03-21.mp3">၅၄။ 
ေမတၱာႏွလံုးအလွဆံုး (၂၁.၃.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-055-2003-07-26.mp3">၅၅။ တရားအသိလူ႔မ်က္စိ 
(၂၆.၇.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-056-2003-07-13.mp3">၅၆။ 
ကိုယ့္လမ္းကိုယ္ေလွ်ာက္ေကာင္းရာေရာက္ (၁၃.၇.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-057-2003-05-15.mp3">၅၇။ 
ကဆုန္လျပည့္ဗုဒၶဟူးေန႔ (၁၅.၅.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-058-2003-10-03.mp3">၅၈။ 
ဘဝျပင္က်ယ္ခရီးသည္ (၃.၁၀.၀၃)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-059-2004-01-01.mp3">၅၉။ 
သာဓုသံုးပါးျမတ္တရား (၁.၁.၀၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-060-2009-01-10.mp3">၆၀။ အား (၁၀.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-061-2004-02-06.mp3">၆၁။ 
ေမတၱာေပါင္းစုေငြရတု (၆.၂.၀၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-062-2004-02-17.mp3">၆၂။ အား (၁၇.၂.၀၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-063-2009-04-14.mp3">၆၃။ 
ဘဝတစ္ေခါက္ခဏေရာက္ (၁၄.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-064-2004-04-25.mp3">၆၄။ 
ေမတၱာကိုင္စြဲနႈတ္ဆက္ပြဲ (၂၅.၄.၀၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-065-2004-10-29.mp3">၆၅။ လူ႔ဘဝထဲစာေမးပြဲ 
(၂၉.၁၀.၀၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-066-2004-12-22.mp3">၆၆။ 
ကိုယ္ပိုင္အလုပ္ဥစၥာထုပ္ (၂၂.၁၂.၀၄)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-067-2005-04-15.mp3">၆၇။ 
တရားေရေအးအၿမိဳက္ေဆး (၁၅.၄.၀၅)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-068-2005-10-20.mp3">၆၈။ အား (၂၀.၁၀.၁၅)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-069-2006-03-18.mp3">၆၉။ 
ကုသိုလ္ဂုဏ္သိမ္လူ႔အရွိန္ (၁၈.၃.၀၆)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-070-2006-04-15.mp3">၇၀။ 
ေမတၱာေက်းဇူးစြမ္းရည္ထူး (၁၅.၄.၀၆)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-071-2006-09-09.mp3">
၇၁။ ဗိုလ္တရား (၉.၉.၀၆)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-072-2007-02-16.mp3">၇၂။ နႈတ္ဆက္မဂၤလာ 
(၁၆.၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-073-2007-07-20.mp3">၇၃။ 
ဂုဏ္ျပဳခ်ီးက်ဴးစြမ္းရည္ထူး (၂၀.၇.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-074-2007-07-29.mp3">၇၄။ တခါလာလဲဒါပါပဲ 
(၂၉.၇.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-075-2007-08-13.mp3">၇၅။ 
အခ်စ္ဆံုးေဆြမ်ိဳးတရားေတာ္ (၁၃.၈.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-076-2007-08-28.mp3">၇၆။ 
ေမတၱာလႊမ္းျခံဳေဘးရန္လံု (၂၈.၈.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-077-2007-09-19.mp3">၇၇။ ဘဝအႏွစ္အားအစစ္ 
(၁၉.၉.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-078-2007-10-26.mp3">၇၈။ 
ခႏၶာကိုယ္ထဲေဘာလံုးပြဲ (၂၆.၁၀.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-079-2007-11-14.mp3">၇၉။ 
ေမတၱာအစြမ္းစိတ္ေအးခ်မ္း (၁၄.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-080-2007-11-16.mp3">၈၀။ 
ေမတၱာအစစ္လူ႔အခ်စ္ (၁၆.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-081-2007-11-19.mp3">၈၁။ လူအား (၁၉.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-082-2007-11-22.mp3">၈၂။ 
ကိုယ္ပိုင္အလုပ္ဥစၥာထုပ္ (၂၂.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-083-2007-11-24.mp3">၈၃။ 
ေန႔စဥ္ဆင္ႏႊဲလူ႔ေအာင္ပြဲ (၂၄.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-084-2007-11-28.mp3">၈၄။ 
ေန႔စဥ္ဆင္ႏႊဲလူ႔ေအာင္ပြဲ (၂၈.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-085-2007-11-29.mp3">၈၅။ ခြန္အား 
(၂၉.၁၁.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-086-2007-12-04.mp3">၈၆။ 
ရာျပည့္ဂုဏ္သိမ္မစိုးရိမ္ (၄.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-087-2007-12-11.mp3">၈၇။ 
စိတ္ေအးစရာအားေလးျဖာ (၁၁.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-088-2007-12-14.mp3">၈၈။ 
ေန႔စဥ္ဆင္ႏႊဲလူ႔ၿပိဳင္ပြဲ (၁၄.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-089-2007-12-16.mp3">၈၉။ 
ေက်ာက္တူးသမားလူ႔စြမ္းအား (၁၆.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-090-2007-12-17.mp3">၉၀။ 
ေမတၱာတရားလူ႔စြမ္းအား (၁၇.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-091-2007-12-18.mp3">၉၁။ 
ႏွလံုးသားဝယ္ဘုရားတည္ (၁၈.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-092-2007-12-21.mp3">၉၂။ 
ေမတၱာႏွလံုးအလွဆံုး (၂၁.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-093-2007-12-22.mp3">၉၃။ တခါလာလဲဒါပါပဲ 
(၂၂.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-094-2007-12-23.mp3">၉၄။ လူအား (၂၃.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-095-2007-12-19.mp3">၉၅။ 
တရားေဆြမ်ိဳးလူ႔တန္ခိုး (၁၉.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-096-2007-12-25.mp3">၉၆။ လူ႔တာဝန္ 
(၂၅.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-097-2007-02-28.mp3">၉၇။ 
မိဘအခ်စ္ေဆြမ်ိဳးစစ္ (၂၈.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-098-2007-12-29.mp3">၉၈။ 
ဂုဏ္ျပဳခ်ီးက်ဴးစြမ္းရည္ထူး (၂၉.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-099-2007-12-30.mp3">၉၉။ 
မိဘအခ်စ္ေဆြမ်ိဳးစစ္ (၃၀.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-100-2007-12-31.mp3">၁၀၀။ စိန္တလံုး 
(၃၁.၁၂.၀၇)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-101-2008-01-03.mp3">၁၀၁။ 
ႏွစ္သစ္မဂၤလာရက္ရာဇာ (၃.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-102-2008-01-07.mp3">၁၀၂။ 
မိဘအခ်စ္ေဆြမ်ိဳးစစ္ (၇.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-103-2008-01-09.mp3">၁၀၃။ 
ကိုယ့္ကံကိုယ္ထိန္းအပူၿငိမ္း (၉.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-104-2008-01-09.mp3">၁၀၄။ 
ကိုယ္ပိုင္အလုပ္ကုသိုလ္ထုပ္ (၉.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-105-2008-01-21.mp3">၁၀၅။ လူ႔တာဝန္ 
(၁၀.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-106-2008-01-11.mp3">၁၀၆။ လူ႔ဘဝထဲစာေမးပြဲ 
(၁၁.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-107-2008-01-19.mp3">၁၀၇။ 
ကုသိုလ္ဂုဏ္သိမ္လူ႔အရွိန္ (၁၉.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-108-2008-01-21.mp3">၁၀၈။ 
ခႏၶာကိုယ္ထဲေဘာလံုးပြဲ (၂၁.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-109-2008-01-29.mp3">၁၀၉။ 
ေမတၱာလႊမ္းျခံဳေဘးရန္လံု (၂၉.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-110-2008-01-29.mp3">၁၁၀။ 
အခ်ိန္တန္ဖိုးလူ႔တန္ခိုး (၂၉.၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-111-2008-02-02.mp3">၁၁၁။ 
အသိမွန္ကန္အဖိုးတန္ (၂.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-112-2008-02-03.mp3">၁၁၂။ 
ႏွစ္သစ္မဂၤလာရက္ရာဇာ (၃.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-113-2008-02-06.mp3">၁၁၃။ 
ကုသိုလ္ေဖာ္ထုတ္လူ႔အလုပ္ (၆.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-114-2008-02-07.mp3">၁၁၄။ 
ဘဝတန္ဖိုးလူ႔တန္ခိုး (၇.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-115-2008-02-08.mp3">၁၁၅။ အား (၈.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-116-2008-02-12.mp3">၁၁၆။ 
ေမတၱာလႊမ္းျခံဳေဘးရန္လံု (၁၂.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-117-2008-02-15.mp3">၁၁၇။ 
ႏွလံုးသားဝယ္ဘုရားတည္ (၁၅.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-118-2008-02-18.mp3">၁၁၈။ အေပါင္းလကၡဏာ 
(၁၈.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-119-2008-02-20.mp3">၁၁၉။ 
တရားစုေဆာင္းအေဖာ္ေကာင္း (၂၀.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-120-2008-02-21.mp3">၁၂၀။ 
ကိုယ္ပိုင္ဥစၥာရတနာ (၂၁.၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-121-2008-03-19.mp3">၁၂၁။ ဘဝပန္းတိုင္ 
(၁၉.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-122-2008-03-20.mp3">၁၂၂။ အေပါင္းလကၡဏာ 
(၂၀.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-113-2008-02-06.mp3">၁၂၃။ တြန္းအား 
(၂၁.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-124-2008-03-22.mp3">၁၂၄။ 
ေမတၱာလႊမ္းျခံဳေဘးရန္လံု (၂၂.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-125-2008-03-26.mp3">၁၂၅။ 
မိဘအခ်စ္ေဆြမ်ိဳးစစ္ (၂၆.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-126-2008-03-30.mp3">၁၂၆။ 
တရားအသိလူ႔မ်က္စိ (၃၀.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-127-2008-03-31.mp3">၁၂၇။ စိတ္ေအးစရာသာသနာ 
(၃၁.၃.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-128-2008-04-01.mp3">၁၂၈။ လူ (၁.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-129-2008-04-04.mp3">၁၂၉။ 
တရားတန္ခိုးစြမ္းအားတိုး (၄.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-130-2008-04-06.mp3">၁၃၀။ 
တရားတန္ခိုးစြမ္းအားတိုး (၆.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-131-2008-04-07.mp3">၁၃၁။ လူ (၇.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-132-2008-04-08.mp3">၁၃၂။ 
လူ႔အက်ိဳးေဆာင္အလင္းေရာင္ (၈.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-133-2008-04-09.mp3">၁၃၃။ 
အက်င့္မွန္ကန္အဖိုးတန္ (၉.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-134-2008-04-15.mp3">၁၃၄။ ဘဝအလင္းေရာင္ 
(၁၅.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-135-2008-04-17.mp3">၁၃၅။ 
ဘဝတစ္ေခါက္ခဏေရာက္ (၁၇.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-136-2008-04-18.mp3">၁၃၆။ ႏွစ္သစ္အခါမဂၤလာ 
(၁၈.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-137-2008-04-19.mp3">၁၃၇။ လူအား (၁၉.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-138-2008-04-22.mp3">၁၃၈။ အရွိန္အဝါ 
(၂၂.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-139-2008-04-22.mp3">၁၃၉။ 
အဆိုးကိုႏိုင္အေကာင္းပိုင္ (၂၂.၄.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-140-2008-07-25.mp3">၁၄၀။ 
နိဗၺာန္ေရာက္ေၾကာင္းတရားေကာင္း (၂၅.၇.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-141-2008-08-11.mp3">၁၄၁။ ဂဏန္း (၁၁.၈.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-142-2008-09-07.mp3">၁၄၂။ လက္ေဆာင္ 
(၇.၉.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-143-2008-10-22.mp3">၁၄၃။ 
သတိကိုင္စြဲနႈတ္ဆက္ပြဲ (၂၂.၁၀.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-144-2008-10-13.mp3">၁၄၄။ ဘဝလက္က်န္ 
(၁၃.၁၀.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-145-2008-10-14.mp3">၁၄၅။ 
ယေန႔အလုပ္ယေန႔လုပ္ (၁၄.၁၀.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-146-2008-08-18.mp3">၁၄၆။ ေအာင္ပြဲ 
(၁၈.၁၀.၁၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-147-2008-10-25.mp3">၁၄၇။ 
အသိမွန္ကန္အဖိုးတန္ (၂၅.၁၀.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-148-2008-10-28.mp3">၁၄၈။ 
ေမတၱာတရားလူ႔စြမ္းအား (၂၈.၁၀.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-149-2008-11-02.mp3">၁၄၉။ 
အပူၿငိမ္းခ်မ္းလူသြားလမ္း (၂.၁၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-150-2008-11-03.mp3">၁၅၀။ လက္ေဆာင္ 
(၃.၁၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-151-2008-11-05.mp3">၁၅၁။ 
စိတ္ေကာင္းထားကမိတ္ေကာင္းရ (၅.၁၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-152-2008-11-10.mp3">၁၅၂။ 
ေမတၱာတရားလူ႔စြမ္းအား (၁၀.၁၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-153-2008-11-17.mp3">၁၅၃။ 
အလုပ္မရွိအလုပ္ရွာ (၁၇.၁၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-154-2008-11-22.mp3">၁၅၄။ လက္ေဆာင္ 
(၂၂.၁၁.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-155-2008-12-02.mp3">၁၅၅။ ေက်ာက္ 
(၂.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-156-2008-12-07.mp3">၁၅၆။ ေအာင္ပြဲ 
(၇.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-157-2008-12-08.mp3">၁၅၇။ 
လူ၏ခြန္အားျမတ္တရား (၈.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-158-2008-12-11.mp3">၁၅၈။ ယခုအလုပ္ယခုလုပ္ 
(၁၁.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-159-2008-12-13.mp3">၁၅၉။ ဘဝလက္က်န္ 
(၁၃.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-160-2008-12-14.mp3">၁၆၀။ 
ေမတၱာအစြမ္းစိတ္ေအးခ်မ္း (၁၄.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-161-2008-12-24.mp3">၁၆၁။ 
ေမတၱာေက်းဇူးကုသိုလ္ထူး (၂၄.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-162-2008-12-29.mp3">၁၆၂။ ဘဝလက္က်န္ 
(၂၉.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-163-2008-12-30.mp3">၁၆၃။ 
ေဘးရန္ကင္းေဝးၿငိမ္းခ်မ္းေရး (၃၀.၁၂.၀၈)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-164-2009-01-03.mp3">၁၆၄။ 
ေမတၱာေက်းဇူးကုသိုလ္ထူး (၃.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-165-2009-01-04.mp3">၁၆၅။ 
လူူသားေမတၱာဤကမ႓ာ (၄.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-166-2009-01-09.mp3">၁၆၆။ 
ေမတၱာစုေပါင္းအေဖာ္ေကာင္း (၉.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-167-2009-01-12.mp3">၁၆၇။ ေအာင္ပြဲ 
(၁၂.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-168-2009-01-13.mp3">၁၆၈။ 
လူ၏စြမ္းအားျမတ္တရား (၁၃.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-169-2009-01-17.mp3">၁၆၉။ ဘဝလက္က်န္ 
(၁၇.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-170-2009-01-18.mp3">၁၇၀။ လူသားေမတၱာဤကမ႓ာ 
(၁၈.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-171-2009-01-20.mp3">၁၇၁။ 
ေမတၱာလက္တြဲကုသိုလ္ပြဲ (၂၀.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-172-2009-01-26.mp3">၁၇၂။ ေဆြမ်ိဳး 
(၂၆.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-173-2009-01-27.mp3">၁၇၃။ ဘဝအလင္းေရာင္ 
(၂၇.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-174-2009-01-30.mp3">၁၇၄။ 
ေမတၱာကိုင္စြဲနႈတ္ဆက္ပြဲ (၃၀.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-175-2009-01-31.mp3">၁၇၅။ 
ေမတၱာလက္တြဲကုသိုလ္ပြဲ (၃၁.၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-176-2009-02-01.mp3">၁၇၆။ ဘဝအလင္းေရာင္ 
(၁.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-177-2009-02-02.mp3">၁၇၇။ 
ကိုယ့္လမ္းကိုယ္သြားလူ႔စြမ္းအား (၂.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-178-2009-02-03.mp3">၁၇၈။ 
တရားေဆာင္သူစိတ္မပူ (၃.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-179-2009-02-04.mp3">၁၇၉။ 
တရားေဆာင္သူစိတ္မပူ (၄.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-180-2009-02-09.mp3">၁၈၀။ 
ႏွလံုးသားစြမ္းအားႂကြယ္ (၉.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-181-2009-02-11.mp3">၁၈၁။ နေမာတႆ 
(၁၁.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-182-2009-02-14.mp3">၁၈၂။ 
ေမတၱာကိုင္စြဲေကာင္းမႈပြဲ (၁၄.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-183-2009-02-18.mp3">၁၈၃။ 
အသိစင္ၾကယ္စြမ္းအားႂကြယ္ (၁၈.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-184-2009-02-19.mp3">၁၈၄။ နေမာတႆ 
(၁၉.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-185-2009-02-23.mp3">၁၈၅။ 
ေမတၱာႏွလံုးအလွဆံုး (၂၃.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-186-2009-02-24.mp3">၁၈၆။ 
ေမတၱာႏွလံုးအလွဆံုး (၂၄.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-187-2009-02-28.mp3">၁၈၇။ 
ဘဝကိုေဆာင္အလင္းေရာင္ (၂၈.၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-188-2009-03-01.mp3">၁၈၈။ 
ေမတၱာကိုင္စြဲလူ႔ေအာင္ပြဲ (၁.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-189-2009-03-02.mp3">၁၈၉။ အား (၂.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-190-2009-03-28.mp3">၁၉၀။ 
ဘဝေဝစုျမတ္ေကာင္းမႈ (၂၈.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-191-2009-03-29.mp3">၁၉၁။ အား (၂၉.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-192-2009-03-30.mp3">၁၉၂။ ဘဝေဝစု 
(၃၀.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-193-2009-03-30.mp3">၁၉၃။ လုပ္အား 
(၃၀.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-194-2009-03-31.mp3">၁၉၄။ 
ေန႔စဥ္ျဖတ္သန္းလူ႔ဂဏန္း (၃၁.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-195-2009-03-31.mp3">၁၉၅။ 
ေမတၱာတန္ခိုးကုသိုလ္တိုး (၃၁.၃.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-196-2009-04-01.mp3">၁၉၆။ 
အဆင္းအတက္လမ္းႏွစ္ဖက္ (၁.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-197-2009-04-02.mp3">၁၉၇။ 
ေမတၱာတန္ခိုးကုသိုလ္တိုး (၂.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-198-2009-04-03.mp3">၁၉၈။ 
အဆိုးကိုႏိုင္အေကာင္းပိုင္ (၃.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-199-2009-04-03.mp3">၁၉၉။ 
ဓားျပသံုးေယာက္တေကာက္ေကာက္ (၃.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-200-2009-04-04.mp3">၂၀၀။ နေမာဗုဒၶႆ 
(၄.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-201-2009-04-06.mp3">၂၀၁။ 
ကုသိုလ္လည္းရဝမ္းလဲဝ (၆.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-202-2009-04-09.mp3">၂၀၂။ 
ကိုယ့္ကိုကိုယ္ယံုစြမ္းအားလံု (၉.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-203-2009-04-10.mp3">၂၀၃။ 
ဆင္းရဲ၏ေနာက္ခ်မ္းသာေရာက္ (၁၀.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-204-2009-04-17.mp3">၂၀၄။ 
ဓားျပသံုးေယာက္တေကာက္ေကာက္ (၁၇.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-205-2009-04-19.mp3">၂၀၅။ ဘဝအလင္းေရာင္ 
(၁၉.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-206-2009-04-20.mp3">၂၀၆။ 
အသိလက္ဦးႏွစ္သစ္ကူး (၂၀.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-207-2009-04-24.mp3">၂၀၇။ 
ဆင္းရဲ၏ေနာက္ခ်မ္းသာေရာက္ (၂၄.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-208-2009-04-30.mp3">၂၀၈။ 
ေန႔စဥ္ဆင္ႏႊဲဂုဏ္ျပဳပြဲ (၃၀.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-209-2009-05-01.mp3">၂၀၉။ 
ေန႔ညမစဲဂုဏ္ျပဳပြဲ (၁.၅.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-210-2009-05-05.mp3">၂၁၀။ ယူအား (၅.၅.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-211-2009-05-07.mp3">၂၁၁။ ယခုအလုပ္ယခုလုပ္ 
(၇.၅.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-212-2009-07-04.mp3">၂၁၂။အေပါင္းအနႈတ္လူ႔အလုပ္ (၄.၇.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-213-2009-07-06.mp3">၂၁၃။ 
နိဗၺာန္ေရာက္ေၾကာင္းတရားေကာင္း (၆.၇.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-214-2009-07-06.mp3">၂၁၄။ 
ခ်မ္းသာရေၾကာင္းတရားေကာင္း (၆.၇.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-215-2009-04-03.mp3">၂၁၅။ 
အဆိုးကိုႏိုင္အေကာင္းပိုင္ (၃.၄.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-216-2009-07-26.mp3">၂၁၆။ 
စိတ္ဓာတ္ကိုျမႇင့္လုပ္ပိုင္ခြင့္ (၂၆.၇.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-217-2009-07-21.mp3">၂၁၇။ 
အဆိုးကိုႏိုင္အေကာင္းပိုင္ (၂၁.၇.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-218-2009-08-05.mp3">၂၁၈။ 
ေမတၱာစြမ္းအင္အာနိသင္ (၅.၈.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-219-2009-08-19.mp3">၂၁၉။ 
ဆိုးတာႏိုင္မွေကာင္းတာရ (၁၉.၈.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-220-2009-08-26.mp3">၂၂၀။ 
သတိကိုင္စြဲနႈတ္ဆက္ပြဲ (၂၆.၈.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-221-2009-08-26.mp3">၂၂၁။ ဘဝလက္က်န္တရား 
(၂၆.၈.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-222-2009-08-28.mp3">၂၂၂။ 
ဘဝလက္က်န္ကုသိုလ္ကံ (၂၈.၈.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-223-2009-09-16.mp3">၂၂၃။ 
အသိမွန္ကန္လူ႔ေတာင္ပံ (၁၆.၉.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-224-2009-10-01.mp3">၂၂၄။ 
ဘဝလက္က်န္ကုသိုလ္ကံ (၁.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-225-2009-10-02.mp3">၂၂၅။ 
သူနဲ႔ကိုယ္ေပါင္းအကုန္ေကာင္း (၂.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-226-2009-10-03.mp3">၂၂၆။ 
ကုသိုလ္ေရႊအိုးလူမခိုး (၃.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-227-2009-10-03.mp3">၂၂၇။ ေနေကာင္းရဲ႕လား 
(၃.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-228-2009-10-04.mp3">၂၂၈။ 
အေပါင္းမွန္ကန္အေကာင္းက်န္ (၄.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-229-2009-10-04.mp3">၂၂၉။ 
အေပါင္းမွန္မွေကာင္းတာရ (၄.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-230-2009-10-08.mp3">၂၃၀။ 
သူနဲ႔ကိုယ္ေပါင္းအကုန္ေကာင္း (၈.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-231-2009-10-11.mp3">၂၃၁။ 
ေပါင္းတက္မွေကာင္းျမတ္လွ (၁၁.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-232-2009-10-16.mp3">၂၃၂။ 
တရားစုမွစိတ္ေအးရ (၁၆.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-233-2009-10-27.mp3">၂၃၃။ 
ေခြးကိုက္တက္သည္သတိျပဳ (၂၇.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-234-2009-10-27.mp3">၂၃၄။ 
သတိေမတၱာသူငါစုေပါင္းအကုန္ေကာင္း (၂၇.၁၀.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-235-2009-11-05.mp3">၂၃၅။ 
ေမတၱာကိုင္စြဲေအာင္ရၿမဲ (၅.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-236-2009-11-06.mp3">၂၃၆။ 
ေမတၱာေက်းဇူးစားဖြယ္ထူး (၆.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-237-2009-11-08.mp3">၂၃၇။ 
ေမတၱာလက္တြဲကုသိုလ္ပြဲ (၈.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-238-2009-11-10.mp3">၂၃၈။ 
လူ႔အလွဆံုးစိန္တလံုး (၁၀.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-239-2009-11-25.mp3">၂၃၉။ ဒီအတိုင္းပါပဲ 
(၂၅.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-240-2009-11-13.mp3">၂၄၀။ 
ေမတၱာတန္ခိုးကုသိုလ္တိုး (၁၃.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-241-2009-11-15.mp3">၂၄၁။ 
ေမတၱာေဖြးျဖဴေက်ာင္းအလွဴ (၁၅.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-242-2009-11-17.mp3">၂၄၂။ 
ေမတၱာေဖြးျဖဴေပးအလွဴ (၁၇.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-243-2009-11-21.mp3">၂၄၃။ 
ေခြးကိုက္တက္သည္သတိျပဳ (၂၁.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-244-2009-11-19.mp3">၂၄၄။ 
ေမတၱာေဖြးျဖဴေပးအလွဴ (၁၉.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-245-2009-11-25.mp3">၂၄၅။ ဒီအတိုင္းပဲ 
(၂၅.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-246-2009-11-29.mp3">၂၄၆။ 
ေမတၱာပန္းပြင့္ဆင့္တိုင္းတင့္ (၂၉.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-247-2009-11-30.mp3">၂၄၇။ ရတနာ (၃၀.၁၁.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-248-2009-12-25.mp3">၂၄၈။ 
ေမတၱာေပါင္းစုေငြရတု (၂၅.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-249-2009-12-01.mp3">၂၄၉။ 
ေမတၱာေဖြးျဖဴစားဖြယ္အလွဴ (၁.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-250-2009-12-02.mp3">၂၅၀။ 
ပစၥည္းတန္ခိုးကုသိုလ္တိုး (၂.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-251-2009-12-10.mp3">၂၅၁။ 
စားဖြယ္တန္ခိုးကုသိုလ္တိုး (၁၀.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-252-2009-12-11.mp3">၂၅၂။ ေပါင္းတာမွန္မွ 
ေကာင္းတာရ (၁၁.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-253-2009-12-13.mp3">၂၅၃။ အားပါရဲ႕လား 
(၁၃.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-254-2009-12-17.mp3">၂၅၄။ 
ေမတၱာေဖြးျဖဴေအာင္လံထူ (၁၇.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-255-2009-12-18.mp3">၂၅၅။ ဗုဒၶပူဇာမဂၤလာ 
(၁၈.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-256-2009-12-20.mp3">၂၅၆။ 
ကံကိုထိန္းခ်ဳပ္စိတ္ခလုတ္ (၂၀.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-257-2009-12-21.mp3">၂၅၇။ ယခုအလုပ္ယခုလုပ္ 
(၂၁.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-258-2009-12-22.mp3">၂၅၈။ 
ကုသိုလ္ထံုမႊမ္းပုလဲလမ္း (၂၂.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-259-2009-12-23.mp3">၂၅၉။ 
ကိုးနဝင္းကပ္ေက်ာ္ (၂၃.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-260-2009-12-26.mp3">၂၆၀။ 
ေမတၱာပန္းခိုင္သံုးပြင့္ဆိုင္ (၂၆.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-261-2009-12-31.mp3">၂၆၁။ 
တရားေစာင့္သူစိတ္မပူ (၃၁.၁၂.၀၉)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-262-2010-01-03.mp3">၂၆၂။ 
ေမတၱာျဖန္႔ျဖဴးႏွစ္သစ္ကူး (၃.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-263-2010-01-04.mp3">၂၆၃။ ကံထူး၊ ဉာဏ္ထူး၊ 
လံု႔လထူး (၄.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-264-2010-01-05.mp3">၂၆၄။ 
ေပါင္းတာမွန္မွေကာင္းတာရ (၅.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-265-2010-01-08.mp3">၂၆၅။ 
ေမတၱာျပန္႔ပြားလူ႔စြမ္းအား (၈.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-266-2010-12-09.mp3">၂၆၆။ 
ဗုဒၶေက်းဇူးစြမ္းရည္ထူး (၉.၁၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-267-2010-01-10.mp3">၂၆၇။ 
ေမတၱာပန္းခိုင္သံုးပြင့္ဆိုင္ (၁၀.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-268-2010-12-11.mp3">၂၆၈။ 
ေငြကိုလည္းရွာေမတၱာလည္းထား (၁၁.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-269-2010-12-12.mp3">၂၆၉။ 
ေငြကိုလည္းရွာေမတၱာလည္းထား (၁၂.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-270-2010-01-17.mp3">၂၇၀။ 
ကိုယ့္အလုပ္ကိုယ္လုပ္ကိုယ့္အထုပ္ကိုယ္ထုတ္ (၁၇.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-271-2010-01-17.mp3">၂၇၁။ 
သူနဲ႔ကိုယ္ေပါင္းအကုန္ေကာင္း (၁၇.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-272-2010-01-18.mp3">၂၇၂။ 
ကမ႓ာအႏွံ့ေမတၱာျပန္႔ (၁၈.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-273-2010-01-21.mp3">၂၇၃။ 
ကိုယ့္ကံကိုယ္ခံကိုယ္သာစံ (၂၁.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-274-2010-02-11.mp3">၂၇၄။ ဆရာ (၂၂.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-275-2010-01-23.mp3">၂၇၅။ 
ထိန္းကဃပ္ၫႊန္ၾကားဆရာ့အား (၂၃.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-276-2010-01-23.mp3">၂၇၆။ 
ကိုယ့္ကံကိုယ္ျပင္အလွဆင္ (၂၃.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-277-2010-02-01.mp3">၂၇၇။ 
ကိုယ့္ကိုယ္ကိုကယ္မွီေသးတယ္ (၂၄.၁.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-278-2010-02-02.mp3">၂၇၈။ 
သတိေမတၱာေကာင္းစြာကိုင္စြဲလူ႔ေအာင္ပြဲ (၂.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-279-2010-02-03.mp3">၂၇၉။ 
ေငြကိုလည္းရွာေမတၱာလည္းထားလူ႔စြမ္းအား (၃.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-280-2010-02-04.mp3">၂၈၀။ 
ေနရာအႏွံ့ေမတၱာျဖန္႔ (၄.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-281-2010-02-08.mp3">၂၈၁။ 
အေပါင္းမွန္ကန္အေကာင္းက်န္ဧကန္လူ႔ေအာင္ပြဲ (၈.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-282-2010-02-17.mp3">၂၈၂။ 
မအားေပမယ့္အားပါတယ္ (၁၇.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-283-2010-02-19.mp3">၂၈၃။ 
ေမတၱာေဖြးျဖဴေပးအလွဴ (၁၉.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-284-2010-02-25.mp3">၂၈၄။ ဂဏန္း (၂၅.၂.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-285-2010-03-20.mp3">၂၈၅။ 
ဂဏန္းေပါင္းစက္အေကာင္းတြက္ (၂၀.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-286-2010-03-21.mp3">၂၈၆။ 
ေငြကိုလည္းရွာေမတၱာလည္းထားလူ႔စြမ္းအား (၂၁.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-287-2010-03-24.mp3">၂၈၇။ 
မအားေပမယ့္အားပါတယ္ (၂၄.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-288-2010-03-25.mp3">၂၈၈။ ဗုဒၶျမတ္စြာရတနာ 
(၂၅.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-289-2010-03-28.mp3">၂၈၉။ 
ႏွစ္က်ိပ္ရွစ္ဆူေအာင္လံထူ (၂၈.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-290-2010-03-29.mp3">၂၉၀။ 
ဘဝအရွိမွန္ေထာင္ၾကည့္ (၂၉.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-291-2010-03-30.mp3">၂၉၁။ 
ေမတၱာေဖြးျဖဴေပးအလွဴ (၃၀.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-292-2010-03-31.mp3">၂၉၂။ 
အိမ္မႈကိစၥလူ႔အလွ (၃၁.၃.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-293-2010-04-01.mp3">၂၉၃။ တာဝန္ (၁.၄.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-294-2010-04-02.mp3">၂၉၄။ 
ေရႊေတာင္မွာနားေရႊေက်းအား (၂.၄.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-295-2010-04-03.mp3">၂၉၅။ 
ေနရာအႏွံ့ေမတၱာျဖန္႔ (၃.၄.၁၀)</a></span></p>
<p class="MsoNormal">
<span style="font-family:&quot;Zawgyi-One&quot;,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-296-2010-04-04.mp3">၂၉၆။ 
ပစၥည္းကိုရွာပညာကိုခင္းတရားသြင္း (၄.၄.၁၀)</a></span></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-297-2010-04-06.mp3">
၂၉၇။ သစၥာေရွ႔ထား ေမတၱာပြားဘုရားပူေဇာ္မည္ (၆.၄.၁၀)</a></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-298-2010-04-08.mp3">၂၉၈။ 
ၾကံ့ခိုင္ျမင့္မားလူ႔စြမ္းအား (၈.၄.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-299-2010-04-09.mp3">၂၉၉။ 
ဒုလႅဘၻ (၉.၄.၁၀) </a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-300-2010-04-12.mp3">၃၀၀။ 
မွီပါေသးတယ္ကိုယ့္ကိုကယ္ (၁၂.၄.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-301-2010-04-17.mp3">၃၀၁။ 
ခႏၶာကိုယ္ထဲသၾကၤန္ပြဲ (၁၇.၄.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-302-2010-04-23.mp3">၃၀၂။ 
ဂဏန္းေပါင္းစက္ (၂၃.၄.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-303-2010-04-24.mp3">၃၀၃။ 
တရားအသိစိတ္အားျဖည့္ (၂၄.၄.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-304-2010-05-02.mp3">၃၀၄။ 
ကုသိုလ္အႏွစ္ေဆြမ်ိဳးခ်စ္ (၂.၅.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-305-2010-05-22.mp3">၃၀၅။ 
ခဏငွားထားတဲ့ေလးဘီးကား (၂၂.၅.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-306-2010-07-08.mp3">၃၀၆။ 
တိမ္တိုက္ပမာသံသရာ (၈.၇.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-307-2010-07-09.mp3">၃၀၇။ 
ကိုယ့္ဟာကိုယ္အသာေနစမ္းပါ (၉.၇.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-308-2010-07-25.mp3">၃၀၈။ 
ကိုယ့္ဟာနဲ႔ကိုယ္ေနပါ (၂၅.၇.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-309-2010-07-26.mp3">၃၀၉။ 
ကိုယ့္ဒုကၡမွာကိုယ္ေနပါ (၂၆.၇.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-310-2010-07-26.mp3">၃၁၀။ 
ကိုယ့္ေနရာမွာကိုယ္ေနပါ (၂၆.၇.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-311-2010-08-10.mp3">၃၁၁။ 
ကိုယ့္သားကိုယ့္သမီး (၁၀.၈.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-312-2010-08-13.mp3">၃၁၂။ 
ေမြးေန႔ကာလလူ႔အလွ (၁၃.၈.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-313-2010-08-18.mp3">၃၁၃။ 
ေမတၱာရင္ေသြးအစဥ္ေအး (၁၈.၈.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-314-2010-08-18.mp3">၃၁၄။ 
ရင္ေသြးေမတၱာရတနာ (၁၈.၈.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-315-2010-08-25.mp3">၃၁၅။ 
လူသားေမတၱာရတနာ (၂၅.၈.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-316-2010-09-10.mp3">၃၁၆။ 
လူ၏တြန္းအားျမတ္တရား (၁၀.၉.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-317-2010-09-16.mp3">၃၁၇။ 
မိမိပညာကိုယ့္အရာ (၁၆.၉.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-318-2010-01-01.mp3">၃၁၈။ 
ကိုယ့္ကားကိုယ္ေမာင္းကိုယ့္လမ္းေၾကာင္း (၁.၁.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-319-2010-10-01.mp3">၃၁၉။ 
အသိစင္ၾကယ္ဥပုသ္သည္ (၁.၁၀.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-320-2010-10-22.mp3">၃၂၀။ 
ေနေကာင္းရဲ႕လားလူ႔စကား (၂၂.၁၀.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-321-2010-10-22.mp3">၃၂၁။ 
ဘဝလက္က်န္ကုသိုလ္ကံ (၂၂.၁၀.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-322-2010-10-23.mp3">၃၂၂။ 
ကိုယ့္ဟာနဲ႔ကိုယ္ေနပါ (၂၃.၁၀.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-323-2010-10-23.mp3">၃၂၃။ 
မကင္းႏိုင္တာတြဲေနပါ (၂၃.၁၀.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-324-2010-11-01.mp3">၃၂၄။ 
အေနတက္မွအျမတ္ရ (၁.၁၁.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-325-2010-11-16.mp3">၃၂၅။ 
ေငြကိုယ္လည္းရွာေမတၱာလည္းထားလူ႔စြမ္းအား (၁၆.၁၁.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-326-2010-11-19.mp3">၃၂၆။ 
တန္ခိုးတက္ေအာင္အက်ိဳးေဆာင္ (၁၉.၁၁.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-327-2010-11-24.mp3">၃၂၇။ 
ကံဉာဏ္လံု႔လလူ႔ဘဝ (၂၄.၁၁.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-328-2010-11-27.mp3">၃၂၈။ 
ႏွလံုးသားဝယ္ဘုရားတည္ (၂၇.၁၁.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-329-2010-11-28.mp3">၃၂၉။ 
သတၱဝါစံုေမတၱာျခံဳအကုန္ခ်မ္းသာရ (၂၈.၁၁.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-330-2010-12-01.mp3">၃၃၀။ 
အေနတက္မွအျမတ္ရ (၁.၁၂.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-331-2010-12-02.mp3">၃၃၁။ 
မိမိပညာျမတ္ဆရာ (၂.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-332-2010-12-03.mp3">၃၃၂။ ေရႊ 
(၃.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-333-2010-12-04.mp3">၃၃၃။ 
သစၥာေမတၱာအားကိုးရာ (၄.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-334-2010-12-05.mp3">၃၃၄။ 
ေမတၱာအစစ္ေတြမ်ိဳးခ်စ္ (၅.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-335-2010-12-15.mp3">၃၃၅။ 
သတိေမတၱာေကာင္းစြာကိုင္စြဲဆြမ္းေအာင္ပြဲ (၁၅.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-336-2010-12-18.mp3">၃၃၆။ 
ဆိုးတာႏိုင္မွေကာင္းတာရ (၁၈.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-337-2010-12-19.mp3">၃၃၇။ 
စိတ္ေအးစရာမဂၤလာ (၁၉.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-338-2010-12-20.mp3">၃၃၈။ 
သစၥာေရွ႕ထားေမတၱာပြားဘုရားပူေဇာ္ပါ (၂၀.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-339-2010-12-14.mp3">၃၃၉။ 
လူ၏ခြန္အားျမတ္တရား (၁၄.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-340-2010-12-25.mp3">၃၄၀။ 
စားဖြယ္တန္ခိုးကုသိုလ္တိုး (၂၅.၁၂.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-341-2010-12-25.mp3">၃၄၁။ 
ၿပိဳင္ဘက္ (၂၅.၁၂.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-342-2010-12-26.mp3">၃၄၂။ 
သတိကိုင္စြဲဆြမ္းေအာင္ပြဲ (၂၆.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-343-2010-12-27.mp3">၃၄၃။ 
ၿပီးတိုင္းျပည့္စံုလူ၏ဂုဏ္ (၂၇.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-344-2010-12-28.mp3">၃၄၄။ 
ကုသိုလ္ကိုင္စြဲဆြမ္းေအာင္ပြဲ (၂၈.၁၂.၁၀)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-345-2010-12-31.mp3">၃၄၅။ 
ကုသိုလ္ကိုင္စြဲလူ႔ေအာင္ပြဲ (၃၁.၁၂.၁၀) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-346-2011-01-02.mp3">၃၄၆။ 
ေမတၱာကိုင္စြဲလူ႔ေအာင္ပြဲ (၂.၁.၂၀၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-347-2011-01-03.mp3">၃၄၇။ 
သတိကိုင္စြဲလမ္းဖြင့္ပြဲ (၃.၁.၂၀၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-348-2011-01-04.mp3">၃၄၈။ 
ဗုဒၶျမတ္စြာတို႔ဆရာ (၄.၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-349-2011-01-05.mp3">၃၄၉။ 
ကိုယ့္ဟာကိုယ္ေရြးယူပါ (၅.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-350-2011-01-06.mp3">၃၅၀။ 
ေမတၱာလက္တြဲကုသိုလ္ပြဲ (၆.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-351-2011-01-07.mp3">၃၅၁။ 
ထိုက္တန္သူမွကုသိုလ္ရ (၇.၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-352-2011-01-09.mp3">၃၅၂။ 
ဘဝအႏွစ္အားအစစ္ (၉.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-353-2011-01-10.mp3">၃၅၃။ 
ေမြးေန႔မဂၤလာရတနာ (၁၀.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-354-2011-01-11.mp3">၃၅၄။ 
ေရႊကိုကပ္ကေရႊကိုရ (၁၁.၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-355-2011-12-15.mp3">၃၅၅။ 
သစၥာေရွ႕ထားေမတၱာပြားစြမ္းအားျမႇင့္တင္မည္ (၁၅.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-356-2011-01-16.mp3">၃၅၆။ 
တရားရွိမွအားျပည့္ဝ (၁၆.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-357-2010-11-21.mp3">၃၅၇။ 
ေမတၱာလက္တြဲဆြမ္းေအာင္ပြဲ (၂၁.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-358-2011-01-22.mp3">၃၅၈။ 
ကိုယ့္လမ္းကိုယ္သြားလူ႔စြမ္းအား (၂၂.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-359-2011-01-24.mp3">၃၅၉။ 
သတိေရွ႕ထားအားခ်င္းယွဥ္ၿပိဳင္ကိုယ္ကႏိုင္ (၂၄.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-360-2011-01-25.mp3">၃၆၀။ 
စိတ္ဓာတ္ကိုသန္႔ေမတၱာၫႊန္႔ (၂၅.၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-361-2011-01-29.mp3">၃၆၁။ 
တရားျပည့္ႂကြယ္ႏွစ္ပတ္လည္ (၂၉.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-362-2011-01-31.mp3">၃၆၂။ 
ရွင္ျပဳမဂၤလာရတနာ (၃၁.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-363-2011-01-31.mp3">၃၆၃။ 
အားကိုေပးကအားကိုရၿမဲဆြမ္းေအာင္ပြဲ (၃၁.၁.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-364-2011-02-06.mp3">၃၆၄။ အား 
(၆.၂.၁၁) </a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-365-2011-02-07.mp3">၃၆၅။ 
စိတ္ဓာတ္ကိုျမႇင့္တရားက်င့္ (၇.၂.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-366-2011-02-08.mp3">၃၆၆။ စိန္ 
(၈.၂.၁၁) </a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-367-2011-02-09.mp3">၃၆၇။ 
ကိုယ့္လမ္းကိုယ္သြားလူ႔စြမ္းအား (၉.၂.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-368-2011-02-10.mp3">၃၆၈။ 
ကိုယ့္ဟာကိုယ္စြဲလူ႔ေအာင္ပြဲ (၁၀.၂.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-369-2011-02-11.mp3">၃၆၉။ 
ကိုယ့္ဟာကိုယ္ယူစြမ္းတဲ့လူ (၁၁.၂.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-370-2011-02-12.mp3">၃၇၀။ 
ကိုယ့္အားကိုယ္ယူစြမ္းတဲ့လူ (၁၂.၂.၁၁)</a></span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-371-2011-02-14.mp3">၃၇၁။ 
ကိုယ့္လမ္းကိုယ္သြားမီးရထား (၁၄.၂.၁)</a></span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-372-2011-02-15.mp3">၃၇၂။ ကိုယ့္လမ္းကိုယ္သြားမီးရထား (၁၅.၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-373-2011-02-16.mp3">၃၇၃။ 
သစၥာေရွ႕ထားေမတၱာပြားဘုရားပူေဇာ္ၾက (၁၆.၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-374-2011-02-21.mp3">၃၇၄။ 
တရားရွိမွအားျပည့္ဝ (၂၁.၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-375-2011-02-24.mp3">၃၇၅။ 
တရားရွိမွအားျပည့္ဝ (၂၄.၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-376-2011-02-27.mp3">၃၇၆။ 
ပစၥည္းရွာေမတၱာကိုခင္းတရားသြင္း (၂၇.၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-377-2011-03-31.mp3">၃၇၇။ 
ပစၥည္းအႏွစ္ကုသိုလ္စစ္ (၃၁.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-378-2011-03-23.mp3">၃၇၈။ 
ဂုဏ္ျပဳခ်ီးက်ဴးကုသိုလ္ထူး (၂၃.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-379-2011-03-24.mp3">၃၇၉။ 
ေမြးေန႔အခါမဂၤလာ (၂၄.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-380-2011-03-25.mp3">၃၈၀။ 
တရားရွိမွအားျပည့္ဝ (၂၅.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-381-2011-03-25.mp3">၃၈၁။ 
လူသားေမတၱာမဂၤလာ (၂၅.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-382-2011-03-26.mp3">၃၈၂။ လူအား 
(၂၆.၃.၁၁)</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-383-2011-03-29.mp3">၃၈၃။ 
လူသားေမတၱာရတနာ (၂၉.၃.၁၁)</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-384-2011-03-28.mp3">၃၈၄။ 
လူမိုက္တေယာက္ပန္းတိုင္ေရာက္ (၂၈.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-385-2011-03-30.mp3">၃၈၅။ 
ရင္ေသြးေမတၱာမဂၤလာ (၃၀.၃.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-386-2011-04-07.mp3">၃၈၆။ 
လူအားေမတၱာရတနာ (၇.၄.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-387-2011-04-08.mp3">၃၈၇။ 
အလုပ္ကိုတင္းအရႈပ္ကင္း (၈.၄.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-388-2011-04-10.mp3">၃၈၈။ 
သနားၾကင္နာေမတၱာေဖြးျဖဴေအာင္လံထူ (၁၀.၄.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-389-2011-04-17.mp3">၃၈၉။ 
ကိုယ္ခႏၶာထဲသၾကၤန္ပြဲ (၁၇.၄.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-390-2011-09-19.mp3">၃၉၀။ 
ဘဝပန္းတိုင္လွမ္း၍ကိုင္ (၁၉.၄.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-391-2011-04-24.mp3">၃၉၁။ 
လူအားေမတၱာမဂၤလာ (၂၄.၄.၁၁)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-392-2011-04-26.mp3">၃၉၂။ ပစၥည္းႏွင့္ေပါင္းလူ႔အေကာင္း (၂၆.၄.၁၁)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-393-2011-05-01.mp3">၃၉၃။ ဂုဏ္ျပဳခ်ီးက်ဴးစြမ္းရည္ထူး (၁.၅.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-394-2011-05-17.mp3">၃၉၄။ 
သားေလး (၁၇.၅.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-395-2011-05-25.mp3">၃၉၅။ 
ေမတၱာအစြမ္းသစၥာလႊမ္းတရား (၂၅.၅.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-396-2011-06-21.mp3">၃၉၆။ 
အေပးလြယ္လ်က္အယူခက္ (၂၁.၆.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-397-2011-07-09.mp3">၃၉၇။ 
ဘဝအႏွစ္ေရႊအစစ္ (၉.၇.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-398-2011-07-14.mp3">၃၉၈။ 
ေမတၱာကိုဖြင့္သိကၡာျမင့္ (၁၄.၇.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-399-2011-07-15.mp3">၃၉၉။ 
ေမတၱာတန္ခိုးသိကၡာတိုး (၁၅.၇.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-400-2011-07-17.mp3">၄၀၀။ 
အသာေနတက္လူ႔အျမတ္ (၁၇.၇.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-401-2011-07-15.mp3">၄၀၁။ 
အိမ္တြင္းမဂၤလူ႔က်င့္စဥ္ (၁၅.၇.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-402-2011-07-30.mp3">၄၀၂။ 
သစၥာထံုမႊမ္းေမတၱာစြမ္း (၃၀.၇.၁၁) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-403-2011-08-28.mp3">၄၀၃။ ကိုယ့္ဝန္ကိုယ္ထမ္းစိတ္အစြမ္း (၂၈.၈.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-404-2011-08-28.mp3">၄၀၄။ 
ေမတၱာဝန္ထမ္းလူ႔အစြမ္း (၂၈.၈.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-405-2011-09-05.mp3">၄၀၅။ 
ေဆြမ်ိဳးရင္းခ်ာမဂၤလာ (၅.၉.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-406-2011-09-12.mp3">၄၀၆။ 
ၿပီးတိုင္းျပည့္စံုလူ၏ဂုဏ္ (၁၂.၉.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-407-2011-09-20.mp3">၄၀၇။ 
ဥပုသ္ေမတၱာရတနာ (၂၀.၉.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-408-2011-09-23.mp3">၄၀၈။ 
စြမ္းအားျပည့္ႂကြယ္ႏွစ္ပတ္လည္ (၂၃.၉.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-409-2011-10-11.mp3">၄၀၉။ 
သစၥာေရွ႕ထားေမတၱာအား (၁၁.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-410-2011-10-18.mp3">၄၁၀။ 
သူဦးကိုယ္ဦးသံုးမႊာပူး (၁၈.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-411-2011-10-12.mp3">၄၁၁။ 
ၿပီးလွ်င္ျပည့္စံုလူ၏ဂုဏ္ (၁၂.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-412-2011-10-18.mp3">၄၁၂။ 
သူဦးကိုယ့္ဦးသံုးမႊာပူး (၁၈.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-413-2011-10-12.mp3">၄၁၃။ 
ကန္ခ်ႏွင့္ကံလွ (၁၂.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-414-2011-10-16.mp3">၄၁၄။ 
ေကာင္းမႈျပည့္ႂကြယ္ႏွစ္ပတ္လည္ (၁၆.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-415-2011-10-18.mp3">၄၁၅။ 
သူဦးကိုယ့္ဦးသံုးမႊာပူး (၁၈.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-416-2011-10-25.mp3">၄၁၆။ 
အေပးလြယ္လ်က္အယူခက္ (၂၅.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-417-2011-10-26.mp3">၄၁၇။ 
သူကကန္ခ်ကိုယ္ကံလွ (၂၆.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-418-2011-10-27.mp3">၄၁၈။ 
ေဆြမ်ိဳးရင္းခ်ာရတနာ (၂၇.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-419-2011-11-30.mp3">၄၁၉။ 
စိတ္အားထက္သန္လူ႔တာဝန္ (၃၀.၁၀.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-420-2011-11-06.mp3">၄၂၀။ 
တရားမေမ့စိန္ေမြးေန႔ (၆.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-421-2011-11-12.mp3">၄၂၁။ 
ကိုယ့္ဟာ (၁၂.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-422-2011-11-13.mp3">၄၂၂။ 
မိခင္စိတ္ထားေမတၱာအား (၁၃.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-423-2011-11-14.mp3">၄၂၃။ 
အမွန္ေျပာၾကားေမတၱာပြားဘုရားပူေဇာ္မည္ (၁၄.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-424-2011-11-15.mp3">၄၂၄။ 
အိုပြဲေမတၱာမဂၤလာ (၁၅.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-425-2011-11-16.mp3">၄၂၅။ 
အိုပြဲမဂၤလာရတနာ (၁၆.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-426-2011-11-22.mp3">၄၂၆။ 
ဓားျပသံုးေယာက္တေကာက္ေကာက္ (၂၂.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-427-2011-11-28.mp3">၄၂၇။ 
ပညာဥစၥာေပါင္းမွသာလူမွာေကာင္းတာရ (၂၈.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-428-2011-11-29.mp3">၄၂၈။ 
အေနလည္းလွေရႊလည္းရ (၂၉.၁၁.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-429-2011-12-06.mp3">၄၂၉။ 
ကုသိုလ္လႊမ္းျခံဳလူ၏ဂုဏ္ (၆.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-430-2011-12-07.mp3">၄၃၀။ 
ကိုယ့္ဟာကိုယ္ထုပ္လူလည္လုပ္ (၇.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-431-2011-12-09.mp3">၄၃၁။ 
ပစၥည္းႏွင့္ဉာဏ္အေပါင္းမွန္ဧကန္ေကာင္းတာရ (၉.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-432-2011-12-12.mp3">၄၃၂။ 
ကုသိုလ္ျပည့္စံုလူ၏ဂုဏ္ (၁၂.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-433-2011-12-13.mp3">၄၃၃။ 
ကိုယ့္ဟာကိုယ္ထုတ္လူလည္လုပ္ (၁၃.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-434-2011-12-14.mp3">၄၃၄။ 
အမွန္ေျပာၾကားေမတၱာပြားဘုရားပူေဇာ္ပြဲ (၁၄.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-435-2011-12-16.mp3">၄၃၅။ 
ေမတၱာတန္ခိုးသိကၡာတိုး (၁၆.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-436-2011-12-19.mp3">၄၃၆။ 
ကုသိုလ္ကိုင္စြဲဆြမ္းေအာင္ပြဲ (၁၉.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-437-2011-12-10.mp3">၄၃၇။ 
အသာေနမွကိုယ့္ဟာရ (၂၀.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-438-2011-12-21.mp3">၄၃၈။ 
အသာေနမွအျမတ္ရ (၂၁.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-439-2011-12-24.mp3">၄၃၉။ 
တရားေဆာင္သူစိတ္မပူ (၂၄.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-440-2011-12-25.mp3">၄၄၀။ 
အမွန္ေျပာၾကားေမတၱာပြားဘုရားပူေဇာ္ပြဲ (၂၅.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-441-2011-12-27.mp3">၄၄၁။ 
တရားေဆာင္သူစြမ္းတဲ့လူ (၂၇.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-442-2011-12-28.mp3">၄၄၂။ 
စြမ္းအားျပည့္စံုလူ၏ဂုဏ္ (၂၈.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-443-2011-12-28.mp3">၄၄၃။ 
ပစၥည္းႏွင့္ဉာဏ္အေပါင္းမွန္ဧကန္ေကာင္းတာရ (၂၈.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-444-2011-12-29.mp3">၄၄၄။ 
မိခင္စိတ္ထားေမတၱာပြား (၂၉.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-445-2011-12-31.mp3">၄၄၅။ 
စားဝတ္ေနမႈက်န္းမာမႈ (၃၁.၁၂.၁၁) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-446-2012-01-01.mp3">၄၄၆။ 
ကုသိုလ္ေဖာ္ထုတ္လူလည္လုပ္ (၁.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-447-2012-01-02.mp3">၄၄၇။ 
ဘဝကိုေဆာင္အလင္းေရာင္ (၂.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-448-2012-01-03.mp3">၄၄၈။ 
မိခင္စိတ္ဓာတ္ေမတၱာျမတ္ (၃.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-449-2012-01-04.mp3">၄၄၉။ 
ကုသိုလ္အစစ္နံပါတ္တစ္ (၄.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-450-2012-01-05.mp3">၄၅၀။ 
စားဝတ္ေနေရးက်န္းမာေရး (၅.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-451-2012-01-06.mp3">၄၅၁။ 
တရားေဆာင္သူစြမ္းတဲ့လူ (၆.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-452-2012-01-07.mp3">၄၅၂။ 
အေမွာင္ကင္းေပ်ာက္အလင္းေရာက္ (၇.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-453-2012-01-08.mp3">၄၅၃။ 
ၿပီးလွ်င္ျပည့္စံုလူ၏ဂုဏ္ (၈.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-454-2012-01-09.mp3">၄၅၄။ 
ေအးခ်မ္းေအာင္ျမင္ေမတၱာရွင္ (၉.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-455-2012-01-10.mp3">၄၅၅။ 
အသာေနမွေအာင္ပြဲရ (၁၀.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-456-2012-01-11.mp3">၄၅၆။ 
ေအးခ်မ္းေအာင္ျမင္ကံထူးရွင္ (၁၁.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-457-2012-01-12.mp3">၄၅၇။ 
သစၥာေရွ႕ထားေမတၱာပြားဘုရားပူေဇာ္ပြဲ (၁၂.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-458-2012-01-12.mp3">၄၅၈။ 
ထူးျခားျမင့္ျမတ္လူ႔စိတ္ဓာတ္ (၁၂.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal"><span style="font-family: Zawgyi-One,sans-serif">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-459-2012-12.mp3">၄၅၉။ 
ေမတၱာျခံဳလႊမ္းေဘးမသန္း (၁၂.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-460-2012-01-13.mp3">၄၆၀။ ဘဝအႏွစ္အားအသစ္ (၁၃.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-461-2012-01-13.mp3">၄၆၁။ ကိုယ့္လမ္းကိုယ္သြားမီးရထား (၁၃.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-462-2012-01-14.mp3">၄၆၂။ ေဆြမ်ိဳးစိတ္ထားေမတၱာပြား (၁၄.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-463-2012-01-16.mp3">၄၆၃။ မိခင္စိတ္ထားေမတၱာပြား (၁၆.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-464-2012-01-17.mp3">၄၆၄။ ကုသိုလ္မေမ့စိန္ေမြးေန႔ (၁၇.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-465-2012-01-21.mp3">၄၆၅။ သုတေက်းဇူးစြမ္းရည္ထူး (၂၁.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-466-2012-01-26.mp3">၄၆၆။ သတိကိုင္စြဲရာျပည့္ပြဲ (၂၆.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-467-2012-01-27.mp3">၄၆၇။ ဆိုးတာကိုႏိုင္ေကာင္းတာပိုင္ (၂၇.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-468-2012-01-28.mp3">၄၆၈။ ခႏၶာသတင္းဉာဏ္မွာလင္း (၂၈.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-469-2012-01-30.mp3">၄၆၉။ ကိုယ့္ကိုကိုယ္ျဖည့္သူ႔ကိုၾကည့္ (၃၀.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-470-2012-01-31.mp3">၄၇၀။ သုတေက်းဇူးစြမ္းရည္ထူး (၃၁.၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-471-2012-02-01.mp3">၄၇၁။ သတိမေမ့စိန္ေမြးေန႔ (၁.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-472-2012-02-04.mp3">၄၇၂။ စိတ္အားတင္းကေအာင္ပြဲရ (၄.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-473-2012-02-04.mp3">၄၇၃။ ေလာကကိုႏိုင္စြမ္းအားပိုင္ (၄.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-474-2012-02-07.mp3">၄၇၄။ တရားကိုင္စြဲေအာင္ရၿမဲ (၇.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-475-2012-02-08.mp3">၄၇၅။ တရားကိုင္စြဲေအာင္ရၿမဲ (၈.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-476-2012-02-09.mp3">၄၇၆။ အားခ်င္းယွဥ္ၿပိဳင္ကိုယ္ကႏိုင္တရား (၉.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-477-2012-02-11.mp3">၄၇၇။ ေလာကကိုႏိုင္စြမ္းအားပိုင္ (၁၁.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-478-2012-02-17.mp3">၄၇၈။ ကုသိုလ္အစစ္နံပါတ္တစ္ (၁၇.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-479-2012-02-18.mp3">၄၇၉။ ေမတၱာေပါင္းစုေငြရတု (၁၈.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-480-2012-02-19.mp3">၄၈၀။ ေမတၱာဝန္ထမ္းလူ႔အစြမ္း (၁၉.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-481-2012-02-21.mp3">၄၈၁။ ပစၥည္းေမတၱာေပါင္းမွသာလူမွာေကာင္းတာရ (၂၁.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-482-2012-02-25.mp3">၄၈၂။ ႏွစ္ေထာင့္ေျခာက္ရာရတနာ (၂၅.၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-483-2012-03-02.mp3">၄၈၃။ ျမန္မာအထူးႏွစ္သစ္ကူး (၂.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-484-2012-03-03.mp3">၄၈၄။ ျမန္မာအႏွစ္သားအစစ္ (၃.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-485-2012-03-23.mp3">၄၈၅။ အားကိုးစရာရတနာ (၂၃.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-486-2012-03-24.mp3">၄၈၆။ ေဆြမ်ိဳးစိတ္ထားေမတၱာအား (၂၄.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-487-2012-03-25.mp3">၄၈၇။ ေဆြမ်ိဳးစိတ္ထားေမတၱာပြား (၂၅.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-488-2012-03-26.mp3">၄၈၈။ သီလေမတၱာျမတ္ပညာ (၂၆.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-489-2012-03-27.mp3">၄၈၉။ ဘဝဂုဏ္ရည္အႏွစ္တည္ (၂၇.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-490-2012-03-28.mp3">၄၉၀။ သူေျခာက္ကိုယ္ေျခာက္ေျခာက္ဆယ့္ေျခာက္ (၂၈.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-491-2012-03-28.mp3">၄၉၁။ ေတြ႕ခဲၾကံဳခဲဘုရားပြဲ (၂၈.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-492-2012-03-29.mp3">၄၉၂။ ခႏၶာသတင္းဉာဏ္မွာလင္း (၂၉.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-493-2012-03-31.mp3">၄၉၃။ ေမတၱာေဖြးျဖဴေက်ာင္းအလွဴ (၃၁.၃.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-494-2012-04-01.mp3">၄၉၄။ အေကာင္းတရားေတာ္ (၁.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-495-2012-04-02.mp3">၄၉၅။ ကုသိုလ္ေဖာ္ထုတ္လူလည္လုပ္ (၂.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-496-2012-04-03.mp3">၄၉၆။ စားဖြယ္အစြမ္းစိတ္ေအးခ်မ္း (၃.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-497-2012-04-05.mp3">၄၉၇။ ရဲရင့္စြန္႔စားမိန္းမသား (၅.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-498-2012-04-08.mp3">၄၉၈။ သူ႔ထက္ကိုယ္ဦးႏွစ္သစ္ကူး (၈.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-499-2012-04-18.mp3">၄၉၉။ ျမန္မာႏွစ္ဆန္းလူ႔အစြမ္း (၁၈.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-500-2012-04-21.mp3">၅၀၀။ ေမတၱာထံုမြန္းကမၼ႒ာန္း (၂၁.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-501-2012-04-27.mp3">၅၀၁။ ေဆြမ်ိဳးရင္းခ်ာေပါင္းတာမွန္မွေကာင္းတာရ (၂၇.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-502-2012-04-28.mp3">၅၀၂။ အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၂၈.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-503-2012-04-30.mp3">၅၀၃။ ကိုယ့္အိမ္ထဲမွာတရားရွာ (၃၀.၄.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-504-2012-05-02.mp3">၅၀၄။ အိုနာေသျခင္းေဆြမ်ိဳးရင္း (၂.၅.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-505-2012-06-18.mp3">၅၀၅။ ဂုဏ္တရားေတာ္ (၁၈.၆.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-506-2012-08-01.mp3">၅၀၆။ အိုျခင္းနာျခင္းေဆြမ်ိဳးရင္း (၁.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-507-2012-08-02.mp3">၅၀၇။ အိုျခင္းနာျခင္းေဆြမ်ိဳးရင္း (၂.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-508-2012-08-02.mp3">၅၀၈။ ေန႔ထူးေန႔ျမတ္မေမ့အပ္ (၂.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-509-2012-08-02.mp3">၅၀၉။ ျမန္မာ့စိတ္ထားလူ႔စြမ္းအား (၂.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-510-2012-08-05.mp3">၅၁၀။ ငါတို႔ျမန္မာ ငါတို႔သာသနာ (၅.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-511-2012-08-06.mp3">၅၁၁။ အသာေနမွေအာင္ပြဲရ (၆.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-512-2012-08-13.mp3">၅၁၂။ ရဲရင့္စြန္႔စားမိန္းမသား (၁၃.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-513-2012-08-25.mp3">၅၁၃။ အသက္ႀကီးျခင္းေဆြမ်ိဳးရင္း (၂၅.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-514-2012-09-23.mp3">၅၁၄။ ေဆြမ်ိဳးရွာကိုယ္မွာေတြ႕ (၂၃.၈.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-515-2012-09-17.mp3">၅၁၅။ အရင္းဘက္သာဆြဲယူပါ (၁၇.၉.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-516-2012-09-20.mp3">၅၁၆။ ပ်က္လွ်င္ျပဳျပင္လူ႔စြမ္းအင္ (၂၀.၉.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-517-2012-09-23.mp3">၅၁၇။ ေဆြမ်ိဳးကိုရွာကိုယ့္ဆီမွာေတြ႕ (၂၃.၉.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-518-2012-09-23.mp3">၅၁၈။ ကိုယ့္စိတ္ထဲမွာေဆြမ်ိဳးရွာ (၂၃.၉.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-519-2012-10-08.mp3">၅၁၉။ ျမန္မာရွာေကာင္းတာေတြ႕ (၈.၁၀.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-520-2012-10-20.mp3">၅၂၀။ ေမတၱာေဖြးျဖဴေက်ာင္းအလွဴအပူၿငိမ္းခ်မ္းရ (၂၀.၁၀.၁၂)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-521-2012-10-26.mp3">၅၂၁။ ကုသိုလ္ျပည့္စံုလူ၏ဂုဏ္ (၂၆.၁၀.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-522-2012-10-30.mp3">၅၂၂။ ကုသိုလ္ျပည့္စံုလူ၏ဂုဏ္ (၃၀.၁၀.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-523-2012-11-03.mp3">၅၂၃။ စိတ္ေအးစရာမဂၤလာ (၃.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-524-2012-11-03.mp3">၅၂၄။ ေကာင္းတာရွာျမန္မာေတြ႕ (၃.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-525-2012-01-03.mp3">၅၂၅။ ေပါ့ပါးလြတ္လပ္ကထိန္ျမတ္ (၃.၁၁.၁၂)
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-526-2012-11-04.mp3">၅၂၆။ ညီညာေပါင္းစုေမတၱာစု (၄.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-527-2012-11-07.mp3">၅၂၇။ ေမတၱာလႊမ္းျခံဳလူ၏ဂုဏ္ (၇.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-528-2012-11-10.mp3">၅၂၈။ ၿပီးတိုင္းျပည့္ဝေအာင္ပြဲရ (၁၀.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-529-2012-11-15.mp3">၅၂၉။ ထူးတာကိုရွာျမန္မာေတြ႕ (၁၅.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-530-2012-11-26.mp3">၅၃၀။ စားဝတ္ေနမႈက်န္းမာမႈေလးခုလူ႔ေအာင္ပြဲ (၂၆.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-531-2012-11-30.mp3">၅၃၁။ ဂုဏ္ကိုရွာကိုယ္မွာေတြ႕ (၃၀.၁၁.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-532-2012-12-02.mp3">၅၃၂။ ျမန္မာအႏွစ္အားအစစ္ (၂.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-533-2012-12-03.mp3">၅၃၃။ ေမတၱာတန္ခိုးကုသိုလ္တိုး (၃.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-534-2012-12-05.mp3">၅၃၄။ တရားကိုင္စြဲလူ႔ေအာင္ပြဲ (၅.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-535-2012-12-06.mp3">၅၃၅။ ေမတၱာလႊမ္းျခံဳလူ၏ဂုဏ္ (၆.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-536-2012-12-07.mp3">၅၃၆။ ျမန္မာ့လူအားျမတ္တရား (၇.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-537-2012-12-09.mp3">၅၃၇။ စားဝတ္ေနမႈက်န္းမာမႈေလးခုလူ႔ေအာင္ပြဲ (၉.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-538-2012-12-10.mp3">၅၃၈။ ဘဝပင္လယ္ခရီးသည္ (၁၀.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-539-2012-12-14.mp3">၅၃၉။ လူႏွင့္ပညာေပါင္းမွသာလူမွာေအာင္ပြဲရ (၁၄.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-540-2012-12-15.mp3">၅၄၀။ ပစၥည္းပညာေပါင္းမွသာလူမွာေကာင္းတာရ (၁၅.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-541-2012-12-15.mp3">၅၄၁။ ျမန္မာစြမ္းအားျမတ္တရား (၁၅.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-542-2012-12-17.mp3">၅၄၂။ စင္ၾကယ္ျမင့္ျမတ္ေရႊျပားကပ္ (၁၇.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-543-2012-12-18.mp3">၅၄၃။ ေမတၱာကိုင္စြဲဆြမ္းေအာင္ပြဲ (၁၈.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-544-2012-12-19.mp3">၅၄၄။ ေမတၱာထံုမႊမ္းလူ႔အစြမ္း (၁၉.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-545-2012-12-20.mp3">၅၄၅။ လူႏွင့္ဥစၥာေပါင္းမွသာလူမွာေအာင္ပြဲရ (၂၀.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-546-2012-12-23.mp3">၅၄၆။ လူႏွင့္ဥစၥာေပါင္းမွသာလူမွာေကာင္းတာရ (၂၁.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-547-2012-12-22.mp3">၅၄၇။ ကုသိုလ္ထံုမႊမ္းအထက္တန္း (၂၃.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-548-2012-12-22.mp3">၅၄၈။ အသီးတရာအညႇာတခုသတိျပဳ (၂၂.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-549-2012-12-25.mp3">၅၄၉။ လူႏွင့္ပညာေပါင္းမွသာလူမွာေအာင္ပြဲရ (၂၅.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-550-2012-12-26.mp3">၅၅၀။ တရားကိုင္စြဲလူ႔ေအာင္ပြဲ (၂၆.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-551-2012-12-27.mp3">၅၅၁။ စားဖြယ္တန္ခိုးစြမ္းအားတိုး (၂၇.၁၂.၁၂)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-552-2012-12-28.mp3">၅၅၂။ အထက္တန္းစားလူ႔စြမ္းအား (၂၈.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-553-2012-12-29.mp3">၅၅၃။ စိတ္ဓာတ္ဖြံ႕ၿဖိဳးလူ႔တန္ခိုး (၂၉.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-554-2012-12-30.mp3">၅၅၄။ စိတ္ဓာတ္ဖြံ႕ၿဖိဳးလူ႔တန္ခိုး (၃၀.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-555-2012-12-31.mp3">၅၅၅။ ကုသိုလ္ကိုင္စြဲရာျပည့္ပြဲ (၃၁.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-556-2012-12-31.mp3">၅၅၆။ စိတ္ဓာတ္ဖြံ႕ၿဖိဳးလူ႔တန္ခိုး (၃၁.၁၂.၁၂) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-557-2013-01-01.mp3">၅၅၇။ အသီးတရာအညႇာတစ္ခု (၁.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-558-2013-01-02.mp3">၅၅၈။ ဓမၼပူဇာမဂၤလာ (၂.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-559-2013-01-06.mp3">၅၅၉။ သာဓု (၆.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-560-2013-01-07.mp3">၅၆၀။ ႏွလံုးသားဝယ္တရားတည္ (၇.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-561-2013-01-08.mp3">၅၆၁။ ႏွလံုးသားဝယ္စြမ္းအားတည္ (၈.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-562-2013-01-09.mp3">၅၆၂။ အရင္းကိုသာေတြ႕ေအာင္ရွာ (၉.၁.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-563-2013-01-10.mp3">၅၆၃။ တိပိဋကဓမၼပူဇာမဂၤလာ (၁၀.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-564-2013-01-11.mp3">၅၆၄။ တိပိဋကဓမၼပူဇာမဂၤလာ (၁၁.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-565-2013-01-12.mp3">၅၆၅။ ကုသိုလ္လည္းရဝမ္းလည္းရ (၁၂.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-566-2013-01-13.mp3">၅၆၆။ အသီးတရာအညႇာတစ္ခု (၁၃.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-567-2013-01-14.mp3">၅၆၇။ သတိေရွ႕ထားအားျခင္းယွဥ္ၿပိဳင္ကိုယ္ကႏိုင္ (၁၄.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-568-2013-01-15.mp3">၅၆၈။ သတိေမတၱာကိုင္ထားပါကိုယ္သာေအာင္ပြဲရ (၁၅.၁.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-569-2013-01-18.mp3">၅၆၉။ အေပါင္းမွန္ကန္အေကာင္းက်န္ (၁၈.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-570-2013-01-19.mp3">၅၇၀။ လူႏွင့္ပညာေပါင္းမွသာလူမွာေအာင္ပြဲရ (၁၉.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-571-2013-01-20.mp3">၅၇၁။ ေတြ႕ခဲၾကံဳခဲဘုရားပြဲ (၂၀.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-572-2013-01-23.mp3">၅၇၂။ ပညာကိုင္စြဲလူ႔ေအာင္ပြဲ (၂၃.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-573-2013-01-25.mp3">၅၇၃။ အပူကင္းကြာမဂၤလာ (၂၅.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-574-2013-01-26.mp3">၅၇၄။ စိတ္အားတင္းကေအာင္ပြဲရ (၂၆.၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-575-2013-02-04.mp3">၅၇၅။ သံဃာ့ဂုဏ္ရည္အာဇာနည္ (၄.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-576-2013-02-04.mp3">၅၇၆။ တရားစြမ္းရည္အခ်ိန္မွီ (၄.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-577-2013-03-05.mp3">၅၇၇။ တရားကိုေဆာင္အလင္းေရာင္ (၅.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-578-2013-01-20.mp3">၅၇၈။ ေအာင္ပြဲမဂၤလာရတနာ (၁၀.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-579-2013-02-11.mp3">၅၇၉။ စားဝတ္ေနမႈက်န္းမာမႈေလးခုမဂၤလာ (၁၁.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-580-2013-02-19.mp3">၅၈၀။ အလွတန္ဆာရတနာ (၁၉.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-581-2013-02-20.mp3">၅၈၁။ အေပါင္းမွန္ကန္အေကာင္းက်န္ (၂၀.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-582-2013-02-21.mp3">၅၈၂။ အထိမ္းအမွတ္ကုသိုလ္ျမတ္ (၂၁.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-583-2013-02-22.mp3">၅၈၃။ ဗုဒၶပူဇာမဂၤလာ (၂၂.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-584-2013-02-23.mp3">၅၈၄။ စိတ္အားထက္သန္လူ႔တာဝန္ (၂၃.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-585-2013-02-25.mp3">၅၈၅။ ေတြ႕ခဲၾကံဳခဲဘုရားပြဲ (၂၅.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-586-2013-02-26.mp3">၅၈၆။ မိဘေက်းဇူးကုသိုလ္ထူး (၂၆.၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-587-2013-03-01.mp3">၅၈၇။ ကိုယ့္ကိုယ္ကိုကယ္မွီေသးတယ္ (၁.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-588-2013-02-02.mp3">၅၈၈။ လူေကာင္းလူလွေအာင္ပြဲရ (၃.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-589-2012-03-12.mp3">၅၈၉။ ျမတ္စြာဗုဒၶအလွတန္ဆာရတနာ (၁၂.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-590-2013-03-15.mp3">၅၉၀။ ရွင္ျပဳအခါမဂၤလာ (၁၅.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-591-2013-03-15.mp3">၅၉၁။ ျမန္မာ့ပညာမဂၤလာ (၁၅.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-592-2013-03-21.mp3">၅၉၂။ ကိုယ့္ဟာကိုယ္စြဲလူ႔ေအာင္ပြဲ (၂၁.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-593-2013-03-22.mp3">၅၉၃။ မွီပါေသးတယ္ကိုယ္ကိုကယ္ (၂၂.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-594-2013-02-29.mp3">၅၉၄။ စားဝတ္ေနမႈက်န္းမာမႈေလးခုမဂၤလာ (၂၉.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-595-2013-03-30.mp3">၅၉၅။ ကုသိုလ္ေကာင္းမႈဧကန္ျပဳ (၃၀.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-596-2013-03-30.mp3">၅၉၆။ ႏွစ္က်ိပ္ရွစ္ဆူေအာင္လံထူ (၃၀.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-597-2013-03-31.mp3">၅၉၇။ အထက္တန္းစားလူ႔စြမ္းအား (၃၁.၃.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-598-2013-04-01.mp3">၅၉၈။ သူမႏိုင္ခင္ႀကိဳ၍ျပင္ (၁.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-599-2013-04-02.mp3">၅၉၉။ ႏွစ္ကူးသျကၤန္သတင္းမွန္ (၂.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-600-2013-04-11.mp3">၆၀၀။ ႏွစ္ကူးသၾကၤန္သတင္းမွန္ (၁၁.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-601-2013-04-17.mp3">၆၀၁။ ႀကိဳက်ၾကတ္တက္သၾကၤန္ (၁၇.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-602-2013-04-18.mp3">၆၀၂။ ရွင္ရဟန္းျပဳျမတ္ေကာင္းမႈေပါင္းစုမဂၤလာ (၁၈.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-603-2013-04-20.mp3">၆၀၃။ တရားျဖည့္သြင္းလူႀကီးမင္း (၂၀.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-604-2013-04-21.mp3">၆၀၄။ ႏွစ္ကူးမဂၤလာဖိတ္ၾကားလႊာ (၂၁.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-605-2013-04-23.mp3">၆၀၅။ ရွင္ျပဳမဂၤလာဖိတ္ၾကားလႊာ (၂၃.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-606-2013-04-27.mp3">၆၀၆။ လူ၏ဘဝအလွတန္ဆာရတနာ (၂၇.၄.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-607-2013-04-28.mp3">၆၀၇။ မိဘရင္းခ်ာေတြ႕ေအာင္ရွာ (၂၈.၄.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-608-2013-05-02.mp3">၆၀၈။ တရားျဖည့္သြင္းလူႀကီးမင္း (၂.၅.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-609-2013-05-04.mp3">၆၀၉။ တိမ္တိုက္ပမာသံသရာ (၄.၅.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-610-2013-05-15.mp3">၆၁၀။ ေမြးေန႔မဂၤလာဖိတ္ၾကားလႊာ (၁၅.၅.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-611-2013-05-20.mp3">၆၁၁။ ကုသိုလ္အတြက္လူ႔တသက္ (၂၀.၅.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-612-2013-05-22.mp3">၆၁၂။ သတိကိုင္စြဲထီးတင္ပြဲ (၂၂.၅.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-613-2013-04-20.mp3">၆၁၃။ ႀကီးက်ယ္ျမင့္ျမတ္လူ႔စိတ္ဓာတ္ (၂၅.၅.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-614-2013-07-07.mp3">၆၁၄။ အသိမွန္ကန္အဖိုးတန္ (၇.၇.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-615-2013-07-13.mp3">၆၁၅။ ေပးတက္ယူတက္လူ႔အျမတ္ (၁၃.၇.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-616-2013-07-22.mp3">၆၁၆။ ကုသိုလ္မဂၤလာဖိတ္ၾကားလႊာ (၂၂.၇.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-617-2013-07-24.mp3">၆၁၇။ ပညာေက်းဇူးစြမ္းရည္ထူး (၂၄.၇.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-618-2013-08-21.mp3">၆၁၈။ ထူးျခားျမင့္ျမတ္လူ႔စိတ္ဓာတ္ (၂၁.၈.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-619-2013-09-04.mp3">၆၁၉။ ဒုကၡမဂၤလာဖိတ္ၾကားလႊာ (၄.၉.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-620-2013-09-12.mp3">၆၂၀။ ပစၥည္းတန္ခိုးကုသိုလ္တိုး (၁၂.၉.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-621-2013-09-13.mp3">၆၂၁။ မရပ္မစဲမွီရာဆြဲ (၁၃.၉.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-622-2013-09-21.mp3">၆၂၂။ ကိုယ့္လမ္းကိုယ့္ရွင္းကိုယ့္ဟာသြင္း (၂၁.၉.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-623-2013-09-22.mp3">၆၂၃။ ခႏၶာကိုယ္ထဲေဘာလံုးပြဲ (၂၂.၉.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-624-2013-09-07.mp3">၆၂၄။ တရားစင္ၾကယ္ဥပုသ္သည္ (၂၇.၉.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-625-2013-09-30.mp3">၆၂၅။ ကိုယ့္လမ္းကိုယ္သြားေလးဘီးကား (၃၀.၉.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-626-2013-10-01.mp3">၆၂၆။ ျမန္မာအခ်စ္ကုသိုလ္စစ္ (၁.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-627-2013-10-04.mp3">၆၂၇။ တရားအတြက္လူ႔တစ္ရက္ (၄.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-628-2013-10-06.mp3">၆၂၈။ ကုသိုလ္အတြက္လူ႔တစ္ရက္ (၆.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-629-2013-10-19.mp3">၆၂၉။ လက္ေဖ်ာက္တစ္ခ်က္စြမ္းအားတက္ (၁၉.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-630-2013-10-20.mp3">၆၃၀။ ကိုယ့္လမ္းကိုယ္ရွင္းကိုယ့္ဟာသြင္း (၂၀.၁၀.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-631-2013-10-20.mp3">၆၃၁။ ပစၥည္းအလွဘဝတန္ဆာရတနာ (၂၀.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-632-2013-10-21.mp3">၆၃၂။ ခႏၶာကိုယ္ထဲသၾကၤန္ပြဲ (၂၁.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-633-2013-10-23.mp3">၆၃၃။ ပစၥည္းအလွဘဝတန္ဆာရတနာ (၂၃.၁၀.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-634-2013-11-06.mp3">၆၃၄။ ေမတၱာကိုကိုင္အားျခင္းၿပိဳင္ (၆.၁၁.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-635-2013-11-11.mp3">၆၃၅။ ဆရာတပည့္လိုတာျဖည့္ (၁၁.၁၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-636-2013-11-18.mp3">၆၃၆။ ဆရာတပည့္လိုတာထည့္ (၁၈.၁၁.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-637-2013-11-20.mp3">၆၃၇။ ခႏၶာကိုယ္ထဲသၾကၤန္ပြဲ (၂၀.၁၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-638-2013-11-21.mp3">၆၃၈။ ေမတၱာကိုသြင္းအားျခင္းယွဥ္ၿပိဳင္ကိုယ္ကႏိုင္ (၂၁.၁၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-639-2013-11-22.mp3">၆၃၉။ တရားေဆာင္မွေအာင္ပြဲရ (၂၂.၁၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-640-2013-11-29.mp3">၆၄၀။ ေကာင္းတာရွာကိုယ္မွာေတြ႕ (၂၉.၁၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-641-2013-12-30.mp3">၆၄၁။ ကိုယ္ဟာရွာကိုယ္မွာေတြ႕ (၃၀.၁၁.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-642-2013-12-01.mp3">၆၄၂။ ေဆြမ်ိဳးရွာကိုယ္မွာေတြ႕ (၁.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-643-2013-12-02.mp3">၆၄၃။ အားကိုရွာကိုယ္မွာေတြ႕ (၂.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-644-2013-12-03.mp3">၆၄၄။ ေကာင္းတာရွာကိုယ္မွာေတြ႕ (၃.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-645-2013-12-04.mp3">၆၄၅။ လူ၏စကားေမတၱာအား (၄.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-646-2013-12-05.mp3">၆၄၆။ ပစၥည္းအလွရွစ္ဌာန (၅.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-647-2013-12-06.mp3">၆၄၇။ ေမတၱာျခံဳလႊမ္းေဘးမသန္း (၆.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-648-2013-12-07.mp3">၆၄၈။ ရက္လည္လလည္ႏွစ္ပတ္လည္ (၇.၁၂.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-649-2013-12-11.mp3">၆၄၉။ တရားရွာကိုယ္မွာေတြ႕ (၁၁.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-650-2013-12-08.mp3">၆၅၀။ ပိုင္တာရွာကိုယ္မွာေတြ႕ (၁၈.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-651-2013-12-19.mp3">၆၅၁။ ဘုရားပူေဇာ္ကုသိုလ္ေတာ္ (၁၉.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-652-2013-12-20.mp3">၆၅၂။ ဘုရားပူေဇာ္ကုသိုလ္ေက်ာ္ (၂၀.၁၂.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-653-2013-12-21.mp3">၆၅၃။ ကုသိုလ္အတြက္လူ႔တရက္ (၂၁.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-654-2013-12-23.mp3">၆၅၄။ ကိုယ့္လမ္းကိုယ္ရွင္းအပူကင္း (၂၃.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-655-2013-12-25.mp3">၆၅၅။ ကိုယ္ကေကာင္းမွသူေကာင္းရ (၂၅.၁၂.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-656-2013-12-26.mp3">၆၅၆။ ကိုယ္ကေကာင္းမွေကာင္းတာရ (၂၆.၁၂.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-657-2013-12-29.mp3">၆၅၇။ ေမတၱာျခံဳလႊမ္းစိတ္ေအးခ်မ္း (၂၉.၁၂.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-658-2013-12-30.mp3">၆၅၈။ အသိလက္ဦးႏွစ္သစ္ကူး (၃၀.၁၂.၁၃)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-659-2013-12-31.mp3">၆၅၉။ ပညာလက္ဦးႏွစ္သစ္ကူး (၃၁.၁၂.၁၃) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-660-2014-01-05.mp3">၆၆၀။ အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၅.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-661-2014-01-02.mp3">၆၆၁။ ေမတၱာေက်းဇူးႏွစ္သစ္ကူး (၂.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-662-2014-01-03.mp3">၆၆၂။ အခ်ိန္ေက်းဇူးႏွစ္သစ္ကူး (၃.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-663-2014-01-04.mp3">၆၆၃။ အခ်ိန္ကိုးစားျမတ္တရား (၄.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-664-2014-01-06.mp3">၆၆၄။ အိမ္တြင္းမဂၢင္လူ႔က်င့္စဥ္ (၆.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-665-2014-01-07.mp3">၆၆၅။ ေကာင္းတာရွာလူမွာေတြ႕ (၇.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-666-2014-01-08.mp3">၆၆၆။ ေကာင္းတာရွာလူမွာေတြ႕ (၈.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-667-2014-01-09.mp3">၆၆၇။ လူမွာရွာေကာင္းတာေတြ႕ (၉.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-668-2014-01-10.mp3">၆၆၈။ ေမတၱာရွာလူမွာေတြ႕ (၁၀.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-669-2014-01-11.mp3">၆၆၉။ တရားအတြက္လူ႔တသက္ (၁၁.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-670-2014-01-12.mp3">၆၇၀။ ေကာင္းတာရွာလမ္းမွာေတြ႕ (၁၂.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-671-2014-01-14.mp3">၆၇၁။ ထူးတာရွာလူမွာေတြ႕ (၁၄.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-672-2014-01-15.mp3">၆၇၂။ အေဆာင္ေကာင္းကေအးခ်မ္းရ (၁၅.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-673-2014-01-16.mp3">၆၇၃။ အမဲအျဖဴႀကိဳက္တာယူ (၁၆.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-674-2014-01-17.mp3">၆၇၄။ ဆရာတကာဆရာတပည့္လိုတာထည့္ (၁၇.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-675-2014-01-18.mp3">၆၇၅။ ကံဆိုးကံေကာင္းလူ႔လမ္းေၾကာင္း (၁၈.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-676-2014-01-19.mp3">၆၇၆။ ျမင့္ျမတ္ထူးျခားလူ႔စိတ္ထား (၁၉.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-677-2014-01-20.mp3">၆၇၇။ ကိုယ့္ကံသူ႔ကံၿပိဳင္ၾကရန္ကိုယ့္ကံအႏိုင္ရ (၂၀.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-678-2014-01-21.mp3">၆၇၈။ အသိျမင့္မားလူ႔စြမ္းအား (၂၁.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-679-2014-01-22.mp3">၆၇၉။ ကုသိုလ္တိုးပြားလူ႔စြမ္းအား (၂၂.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-680-2014-01-23.mp3">၆၈၀။ ကုသိုလ္တိုးပြားလူ႔စြမ္းအား (၂၃.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-681-2014-01-24.mp3">၆၈၁။ အသိထူးျခားလူ႔စြမ္းအား (၂၄.၁.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-682-2014-01-31.mp3">၆၈၂။ ေမတၱာျခံဳလႊမ္းလူ႔အစြမ္း (၃၁.၁.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-683-2014-02-02.mp3">၆၈၃။ ဆိုးတာရွိမွေကာင္းတာရ (၂.၂.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-684-2014-02-03.mp3">၆၈၄။ ျမန္မာ့လူအားျမတ္တရား (၃.၂.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-685-2014-02-04.mp3">၆၈၅။ တရားအတြက္လူ႔အသက္ (၄.၂.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-686-2014-02-05.mp3">၆၈၆။ တရားအတြက္လူ႔တသက္ (၅.၂.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-687-2014-02-10.mp3">၆၈၇။ ျမန္မာလူမ်ိဳးကုသိုလ္တိုး (၁၀.၂.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-688-2014-02-12.mp3">၆၈၈။ မအိုေသးခင္ႀကိဳ၍ျပင္ (၁၂.၂.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-689-2014-02-15.mp3">၆၈၉။ ျမန္မာလူမ်ိဳးကုသိုလ္တိုး (၁၅.၂.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-690-2014-02-23.mp3">၆၉၀။ ဘဝထဲမွာေကာင္းတာရွာ (၂၃.၂.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-691-2014-02-24.mp3">၆၉၁။ လူ႔ဘဝမွာအေကာင္းရွာ (၂၄.၂.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-692-2014-02-25.mp3">၆၉၂။ အမႈိက္ထဲမွာေကာင္းတာရွာ (၂၈.၂.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-693-2014-03-02.mp3">၆၉၃။ ေကာင္းတာပဲလိုခ်င္တယ္ (၂.၃.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-694-2014-03-22.mp3">၆၉၄။ ကိုယ့္ဘဝထဲစာေမးပြဲ (၂၂.၃.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-695-2014-03-23.mp3">၆၉၅။ ကိုယ့္ကိုယ္ကိုျဖည့္သူ႔ကိုၾကည့္ (၂၃.၃.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-696-2014-03-27.mp3">၆၉၆။ ႀကိဳ က် ၾကတ္ တက္ႏွစ္အသစ္ (၂၇.၃.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-697-2014-03-28.mp3">၆၉၇။ အိုပြဲမဂၤလာဖိတ္ၾကားလႊာ (၂၈.၃.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-698-2014-03-29.mp3">၆၉၈။ အမႈိက္ထဲမွာႀကိဳက္တာရွာ (၂၉.၃.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-699-2014-04-30.mp3">၆၉၉။ ေကာင္းတာပဲယူမယ္ (၃၀.၃.၁၄) 
</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-700-2014-03-30.mp3">၇၀၀။ ေကာင္းတာပဲရခ်င္တယ္ (၃၀.၃.၁၄)</a> </span></p>
<p class="MsoNormal">
<span style="font-family: Zawgyi-One,sans-serif; ">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-701-2014-03-31.mp3">၇၀၁။ ခႏၶာကိုယ္ထဲသၾကၤန္ပြဲ (၃၁.၃.၁၄) 
</a> </span></p>
</font>

<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-702-2014-04-01.mp3">၇၀၂။ ခႏၶာကိုယ္ထဲသၾကၤန္ပြဲ (၁.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-703-2014-04-02.mp3">၇၀၃။ အားကိုရွာကိုယ္မွာေတြ႕ (၂.၄.၁၄)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-704-2014-04-03.mp3">၇၀၄။ ကိုယ့္လမ္းကိုယ္ေလွ်ာက္လိုရာေရာက္ (၃.၄.၁၄)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-705-2014-04-03.mp3">၇၀၅။ ကိုယ့္လမ္းကိုယ္သြားျမတ္တရား (၃.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-706-2014-04-04.mp3">၇၀၆။ ကုသိုလ္ျပည့္ႂကြယ္ရက္ပတ္လည္ (၄.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-707-2014-04-05.mp3">၇၀၇။ စြမ္းအားတိုးတက္ႏွစ္အသစ္ (၅.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-708-2014-04-06.mp3">၇၀၈။ အေျပာင္းျမန္ဆန္အေကာင္းက်န္ (၆.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-709-2014-04-07.mp3">၇၀၉။ သၾကၤန္ရွာကိုယ္မွာေတြ႕ (၇.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-710-2014-04-10.mp3">၇၁၀။ အား (၁၁.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-711-2014-04-14.mp3">၇၁၁။ ကိုယ့္ခႏၶာထဲသၾကၤန္ပြဲ (၁၄.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-712-2014-04-14.mp3">၇၁၂။ အရြယ္ရွိခိုက္လံု႔လစိုက္ (၁၄.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-713-2014-04-16.mp3">၇၁၃။ ဘဝထဲမွာလွတာရွာ (၁၆.၄.၁၄)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-714-2014-04-17.mp3">၇၁၄။ ဘဝထဲမွာႏွစ္ေကာင္းရွာ (၁၇.၄.၁၄)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-715-2014-04-18.mp3">၇၁၅။ ကိုယ့္လမ္းကိုယ္သြားျမတ္တရား (၁၈.၄.၁၄)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-716-2014-04-19.mp3">၇၁၆။ ေရႊ႕တာမွန္မွေရြ႕တာလွ (၁၉.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-717-2014-04-20.mp3">၇၁၇။ ေရႊ႕တာမွန္မွေရြ႕တာလွ (၂၀.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-718-2014-04-28.mp3">၇၁၈။ အေသမေၾကာက္လူေလးေယာက္ (၂၈.၄.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-719-2014-05-03.mp3">၇၁၉။ ေကာင္းတာျမတ္တာရေအာင္ရွာ (၃.၅.၁၄)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-720-2014-05-05.mp3">၇၂၀။ အရြယ္ရွိခိုက္လံု႔လစိုက္ (၅.၅.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-721-2014-05-14.mp3">၇၂၁။ မွတ္မွတ္ရရလူ႔ဘဝ (၁၄.၅.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-722-2014-06-08.mp3">၇၂၂။ အမွတ္တရလူ႔အလွ (၈.၆.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-723-2014-06-28.mp3">၇၂၃။ ေကာင္းတာပဲေတြ႕ခ်င္တယ္ (၂၈.၆.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-724-2014-07-09.mp3">၇၂၄။ အမွတ္တရလူ႔အလွ (၆.၇.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-725-2014-07-10.mp3">၇၂၅။ ကိုယ့္ဟာအစစ္လူ႔အႏွစ္ (၁၀.၇.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-726-2014-07-11.mp3">၇၂၆။ ေထရဝါဒဓမၼအစစ္အားအႏွစ္ (၁၁.၇.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-727-2014-07-14.mp3">၇၂၇။ တရားအႏွစ္အားအစစ္ (၁၄.၇.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-728-2014-07-26.mp3">၇၂၈။ ကိုယ့္ကိုယ္ကိုျဖည့္ကိုယ့္ကိုၾကည့္ (၂၆.၇.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-729-2016-10-11.mp3">၇၂၉။ ကိုယ့္ဟာကိုယ္ယူစြမ္းတဲ့သူ (၁၁.၁၀.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-730-2016-10-16.mp3">၇၃၀။ အနာမသိေဆးမရွိ (၁၆.၁၀.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-731-2016-10-16.mp3">၇၃၁။ ကုသိုလ္ကိုျဖည့္ရက္လျပည့္ (၁၆.၁၀.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-732-2016-10-21.mp3">၇၃၂။ ကံေကာင္းဉာဏ္ေကာင္းလံု႔လေကာင္း အေကာင္းလူမွာျပည့္ (၂၁.၁၀.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-733-2016-10-28.mp3">၇၃၃။ အနာကိုသိေဆးရွိ၏ (၂၈.၁၀.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-734-2016-11-03.mp3">၇၃၄။ အသက္ႀကီးရင္အေဖာ္လိုတယ္ (၃.၁၁.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-735-2016-11-13.mp3">၇၃၅။ အေပါင္းမွန္ကန္အေကာင္းက်န္ ( ၁၃.၁၁.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-736-2016-01-18.mp3">၇၃၆။ ကိုယ္စိတ္အနာသက္သာေပ်ာက္ေရးတရားေဆး (၁၈.၁၁.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-737-2016-11-27.mp3">၇၃၇။ ေမတၱာေပါင္းစံုတစ္ခုေလာက္ကႏွစ္ခုရ (၂၇.၁၁.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-738-2016-11-20.mp3">၇၃၈။ ေမတၱာလႊမ္းျခံဳကိုယ့္မွာလံု (၂၈.၁၁.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-739-2016-12-02.mp3">၇၃၉။ ဗုဒၶျမတ္စြာရတနာ (၂.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-740-2016-12-03.mp3">၇၄၀။ စိတ္ေအးစရာလူ႔ခ်မ္းသာ (၃.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-741-2016-12-06.mp3">၇၄၁။ အပူကင္းကြာလူ႔ခ်မ္းသာ (၆.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-742-2016-12-07.mp3">၇၄၂။ တရားေဖာ္ထုတ္လူ႔အလုပ္ (၇.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-743-2016-12-09.mp3">၇၄၃။ လူႀကီးစိတ္ထားေမတၱာအား (၉.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-744-2016-12-10.mp3">၇၄၄။ ကုသိုလ္ဂုဏ္တက္လူ႔အႏွစ္ (၁၀.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-745-2016-12-10.mp3">၇၄၅။ အႏွစ္ယူရလူ႔ဘဝ (၁၀.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-746-2016-12-11.mp3">၇၄၆။ ပညာရဲရင့္ပြဲလည္တင့္ (၁၁.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-747-2016-12-11.mp3">၇၄၇။ ေကာင္းတာရွာသူ႔မွာေကာင္းတာေတြ႕ (၁၁.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-748-2016-12-14.mp3">၇၄၈။ တစ္ခ်က္ခုတ္တယ္ႏွစ္ခ်က္ျပတ္ျမင့္ျမတ္လူ႔အလုပ္ (၁၄.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-749-2016-12-15.mp3">၇၄၉။ ျခင္တစ္ေကာင္မိေအာင္ဖမ္းလူမွာစိတ္ေအးခ်မ္း (၁၅.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-750-2016-12-16.mp3">၇၅၀။ ျခင္တစ္ေကာင္ကင္းေအာင္ေခ်ာက္လူမွာထိပ္တန္းေရာက္ (၁၆.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-751-2016-12-17.mp3">၇၅၁။ အႏွစ္ငါးမ်ိဳးလူ႔တန္ခိုး (၁၇.၁၂.၁၆)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-752-2016-12-18.mp3">၇၅၂။ အႏွစ္ထုတ္ယူစြမ္းတဲ့လူ (၁၈.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-753-2016-12-19.mp3">၇၅၃။ တရားရတနာသာသနာ (၁၉.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-754-2016-12-20.mp3">၇၅၄။ ပစၥည္းအႏွစ္ကုသိုလ္စစ္ (၂၀.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-755-2016-12-21.mp3">၇၅၅။ ကုသိုလ္တရားပညာအား (၂၁.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-756-2016-12-23.mp3">၇၅၆။ ဗုဒၶျမတ္စြာရတနာ (၂၃.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-757-2016-12-25.mp3">၇၅၇။ ကုသိုလ္တရားေမတၱာအား (၂၅.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-758-2016-12-26.mp3">၇၅၈။ တိပိဋကဓမၼပူဇာမဂၤလာ (၂၆.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-759-2016-12-27.mp3">၇၅၉။ ပစၥည္းအႏွစ္ကုသိုလ္စစ္ (၂၇.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-760-2016-12-19.mp3">၇၆၀။ အဆိပ္ကင္းကြာလူ႔ခ်မ္းသာ (၁၉.၁၂.၁၄) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-761-2016-12-28.mp3">၇၆၁။ ႏွစ္ကူးတံတားကုသိုလ္အား (၂၈.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-762-2016-12-30.mp3">၇၆၂။ ႏွစ္ကူးတံတားျမတ္တရား (၃၀.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-763-2016-12-31.mp3">၇၆၃။ ႏွစ္ကူးတံတားကုသိုလ္ပြား (၃၁.၁၂.၁၆) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-764-2017-03-02.mp3">၇၆၄။ ကိုယ့္အိမ္အတြင္းတရားသြင္း (၂.၃.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-765-2017-03-23.mp3">၇၆၅။ ဗုဒၶတစ္ဆူေပၚေတာ္မူ (၂၃.၃.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-766-2017-03-24.mp3">၇၆၆။ ေန႔စဥ္ျပဳျငားကိစၥမ်ားတရားပါမွလူ႔အလုပ္ (၂၄.၃.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-767-2017-03-28.mp3">၇၆၇။ စိတ္တည္ၿငိမ္မွကိုယ္ပိုင္ရ (၂၈.၃.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-768-2017-03-30.mp3">၇၆၈။ လူႀကီးစိတ္ထားကေလးမ်ား (၃.၄.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-769-2017-04-03.mp3">၇၆၉။ ေန႔တိုင္းမေမ့လူ႔ေမြးေန႔ (၃.၄.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-770-2017-04-05.mp3">၇၇၀။ သစၥာျခံဳလႊမ္းေမတၱာစြမ္း (၅.၄.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-771-2017-04-07.mp3">၇၇၁။ ဂုဏ္ရည္ထြန္းေပၚသံဃာေတာ္ (၇.၄.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-772-2017-04-08.mp3">၇၇၂။ သံဃာဂုဏ္ရည္အာဇာနည္ (၈.၄.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-773-2017-04-09.mp3">၇၇၃။ လူ၏အလွဓမၼတစ္ဆူေပၚေတာ္မူ (၉.၄.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-774-2017-04-17.mp3">၇၇၄။ ကုသိုလ္ငါးခုမိသားစု (၁၇.၄.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-775-2017-05-03.mp3">၇၇၅။ သစၥာေမတၱာေကာင္းစြာျခံဳလႊမ္းေဘးမသန္း (၃.၅.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-776-2017-05-04.mp3">၇၇၆။ ေမတၱာျခံဳလႊမ္းေဘးမသန္းေအးခ်မ္းလူ႔ဘဝ (၄.၅.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-777-2017-05-17.mp3">၇၇၇။ ကိုယ့္အခ်ိန္မွာကိုယ့္ဟာကိုယ္ယူ (၁၇.၅.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-778-2017-05-30.mp3">၇၇၈။ ကုသိုလ္ေကာင္းမႈမိသားစု (၃၀.၅.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-779-2017-06-25.mp3">၇၇၉။ ေမတၱာေပါင္းစုမိသားစု (၂၅.၆.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-780-2017-07-01.mp3">၇၈၀။ ေမတၱာေပါင္းစုမိသားစု (၁.၇.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-781-2017-07-02.mp3">၇၈၁။ ကိုယ့္ဟာကိုယ္နႈိက္လူ႔အသိုက္ (၂.၇.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-782-2017-07-08.mp3">၇၈၂။ အဆိုးကင္းကြာေကာင္းတာရေၾကာင္းတရားေကာင္း (၈.၇.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-783-2017-07-08.mp3">၇၈၃။ အပူကင္းကြာခ်မ္းသာရေၾကာင္းတရားေကာင္း (၈.၇.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-784-2017-07-23.mp3">၇၈၄။ ဓမၼလမ္းမွန္လူ႔တာဝန္ (၂၃.၇.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-785-2017-08-07.mp3">၇၈၅။ သစၥာျခံဳလႊမ္းေမတၱာစြမ္း (၇.၈.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-786-2017-08-08.mp3">၇၈၆။ ကုသိုလ္ျပည့္စံုလူ၏ဂုဏ္ (၈.၈.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-787-2017-08-21.mp3">၇၈၇။ ေမတၱာငါးခုမိသားစု (၂၁.၈.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-788-2017-08-21.mp3">၇၈၈။ ကုသိုလ္ကိုျပဳမိသားစု (၂၁.၈.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-789-2017-09-10.mp3">၇၈၉။ သစၥာျခံဳလႊမ္းေမတၱာစြမ္းေအးခ်မ္းလူ႔ဘဝ (၁၀.၉.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-790-2017-10-04.mp3">၇၉၀။ ခရီးေဆာင္အိတ္လူႀကီးစိတ္ (၄.၁၀.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-791-2017-10-05.mp3">၇၉၁။ ခရီးေဆာင္အိတ္လူႀကီးစိတ္ (၅.၁၀.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-792-2017-10-13.mp3">၇၉၂။ သစၥာျခံဳလႊမ္းေမတၱာစြမ္း (၁၃.၁၀.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-793-2017-10-14.mp3">၇၉၃။ ျမန္မာစိတ္ထားကုသိုလ္ပြား (၁၄.၁၀.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-794-2017-10-24.mp3">၇၉၄။ သစၥာထံုမႊမ္းေမတၱာစြမ္း (၂၄.၁၀.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-795-2017-10-26.mp3">၇၉၅။ ေမတၱာေရွ႕ထားစုေပါင္းအား (၂၆.၁၀.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-796-2017-11-07.mp3">၇၉၆။ ဉာဏ္ပါရင္ခႏၶာနဲ႔တည္တယ္ (၇.၁၁.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-797-2017-11-20.mp3">၇၉၇။ မိမိလည္းေကာင္းသူလည္းေကာင္း (၂၀.၁၁.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-798-2017-11-25.mp3">၇၉၈။ သတိေမတၱာလူမွာကိုင္ထားရာျပည့္အား (၂၅.၁၁.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-799-2017-11-25.mp3">၇၉၉။ ကုသိုလ္အစစ္လူ႔အႏွစ္ (၂၅.၁၁.၁၇)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-800-2017-12-01.mp3">၈၀၀။ ဗုဒၶပူဇာရတနာ (၁.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-801-2017-12-03.mp3">၈၀၁။ တရားရွိမွအားျပည့္ဝ (၃.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-802-2017-12-03.mp3">၈၀၂။ ေမတၱာဆယ္ခုမိသားစု (၃.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-803-2017-12-04.mp3">၈၀၃။ ဓမၼပူဇာရတနာ (၄.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-804-2017-12-05.mp3">၈၀၄။ ကိုယ့္ေနရာမွာကိုယ္ေနပါ (၅.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-805-2017-12-06.mp3">၈၀၅။ ကိုယ့္အလုပ္သာကိုယ္လုပ္ပါ (၆.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-806-2017-12-07.mp3">၈၀၆။ ကိုယ့္ေနရာမွာကိုယ္ေနပါ (၇.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-807-2017-12-11.mp3">၈၀၇။ အမွန္ျမင္သိေအာင္ေဗာဓိ (၁၁.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-808-2017-12-12.mp3">၈၀၈။ ကုသိုလ္ကိုျပဳမိသားစု (၁၂.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-809-2017-12-18.mp3">၈၀၉။ လူႀကီးမဂၤလာဘာဝနာ (၁၈.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-810-2017-12-19.mp3">၈၁၀။ သစၥာမ႑ိုင္ေမတၱာကိုင္ (၁၉.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-811-2017-12-20.mp3">၈၁၁။ ပစၥည္းအလွျမတ္ပုည (၂၀.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-812-2017-12-24.mp3">၈၁၂။ သစၥာထံုမႊမ္းေမတၱာစြမ္း (၂၄.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-813-2017-12-25.mp3">၈၁၃။ ကုသိုလ္စုေဆာင္းအေဖာ္ေကာင္း (၂၅.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-814-2017-12-26.mp3">၈၁၄။ ေမတၱာပါမွေပးတာလွ (၂၆.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-815-2017-12-27.mp3">၈၁၅။ ေမတၱာငါးခုမိသားစု (၂၇.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-816-2017-12-26.mp3">၈၁၆။ ကုသိုလ္ကိုင္စြဲဂုဏ္ျပဳပြဲ (၂၉.၁၂.၁၇) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-817-2018-01-06.mp3">၈၁၇။ ဘုရားပူေဇာ္တရားေတာ္ (၄.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-818-2018-01-06.mp3">၈၁၈။ ေမတၱာေရွ႕ထားကုသိုလ္ပြားငါးပါးမိသားစု (၆.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-819-2018-01-07.mp3">၈၁၉။ ကုသိုလ္ရခိုက္ေန႔တြက္ကိုက္ (၇.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-820-2018-01-08.mp3">၈၂၀။ လက္ေဖ်ာက္တခ်က္စြမ္းအားတက္ (၈.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-821-2018-01-09.mp3">၈၂၁။ လက္ေဖ်ာက္တခ်က္စြမ္းအားတက္ (၉.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-822-2018-01-10.mp3">၈၂၂။ ေမတၱာဦးစီးကုသိုလ္ႀကီး (၁၀.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-823-2018-01-11.mp3">၈၂၃။ ထီးအထြဋ္တြင္စိန္ဖူးတင္ (၁၁.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-824-2018-01-12.mp3">၈၂၄။ ပစၥည္းအလွျမတ္ဓမၼ (၁၂.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-825-2018-01-17.mp3">၈၂၅။ ကံတက္ဉာဏ္တက္လံု႔လသြက္အထက္ဧကန္ေရာက္ႏိုင္ၾက (၁၇.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-826-2018-01-18.mp3">၈၂၆။ ကံဉာဏ္လံု႔လလူ႔ဘဝ (၁၈.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-827-2018-01-10.mp3">၈၂၇။ သစၥာေရွးရႈေမတၱာျပဳ (၂၀.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-728-2014-07-26.mp3">၈၂၈။ ကံဉာဏ္လံု႔လလူ႔အလွ (၂၁.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-829-2018-01-21.mp3">၈၂၉။ သစၥာေရွးရႈေမတၱာျပဳ (၂၁.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-830-2018-01-22.mp3">၈၃၀။ လူ၏အႏွစ္ကုသိုလ္စစ္ (၂၂.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-831-2018-01-23.mp3">၈၃၁။ အေပါင္းမွန္ကန္အေကာင္းက်န္ (၂၃.၁.၁၈)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-832-2018-01-25.mp3">၈၃၂။ သတိေမတၱာမွန္စြာကိုင္စြဲဆြမ္းေအာင္ပြဲ (၂၅.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-833-2018-01-26.mp3">၈၃၃။ သတိေမတၱာမွန္စြာကိုင္စြဲလူ႔ေအာင္ပြဲ (၂၆.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-834-2018-01-25.mp3">၈၃၄။ ေန႔စဥ္ဆင္ႏႊဲတရားပြဲ (၂၅.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-835-2018-01-28.mp3">၈၃၅။ ေန႔တိုင္းဆင္ႏႊဲတရားပြဲ (၂၈.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-836-2018-01-30.mp3">၈၃၆။ ေန႔စဥ္ဆင္ႏႊဲထီးတင္ပြဲ (၃၀.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-837-2018-01-31.mp3">၈၃၇။ ေန႔စဥ္ဆင္ႏႊဲဘုရားပြဲ (၃၁.၁.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-838-2018-02-01.mp3">၈၃၈။ ေန႔စဥ္အားခဲဘုရားပြဲ (၁.၂.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-839-2018-02-02.mp3">၈၃၉။ ေန႔စဥ္ဆင္ႏႊဲကုသိုလ္ပြဲ (၂.၂.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-840-2018-02-16.mp3">၈၄၀။ သတိေမတၱာညီညာကိုင္စြဲရာျပည့္ပြဲ (၁၆.၂.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-841-2018-03-20.mp3">၈၄၁။ လူ၏အႏွစ္ကုသိုလ္စစ္ (၂၀.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-842-2018-03-22.mp3">၈၄၂။ ခ်မ္းသာဖို႔ရာစီးပြားရွာ (၂၂.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-843-2018-03-24.mp3">၈၄၃။ ထီးသံုးလက္တြင္စိန္ဖူးတင္ (၂၄.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-844-2018-03-26.mp3">၈၄၄။ စီးပြားရွာကိုယ္မွာေတြ႕ (၂၆.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-845-2018-03-28.mp3">၈၄၅။ စီးပြားကိုရွာကိုယ့္ဆီမွာေတြ႕ (၂၈.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-846-2018-03-28.mp3">၈၄၆။ ေဆြမ်ိဳးရွာကိုယ္မွာေတြ႕ (၂၈.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-847-2018-03-29.mp3">၈၄၇။ ေဆြမ်ိဳးရွာကိုယ္မွာေတြ႕ (၂၉.၃.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-848-2018-04-03.mp3">၈၄၈။ မိဘအိမ္ျပန္ေဆြမ်ိဳးထံမွန္မွန္လာ၍ေတြ႕ (၃.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-849-2018-04-04.mp3">၈၄၉။ သိကၡာသံုးပါးျမတ္တရား (၄.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-850-2018-04-11.mp3">၈၅၀။ ေဆြမ်ိဳးရွာကိုယ္မွာေတြ႕ (၁၁.၄.၁၈)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-851-2018-04-12.mp3">၈၅၁။ ပိုက္ဆံရွာလူမွာေတြ႕ (၁၂.၄.၁၈)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-852-2018-04-12.mp3">၈၅၂။ စိတ္ဓာတ္ကိုျမႇင့္တရားက်င့္ (၁၂.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-853-2018-04-13.mp3">၈၅၃။ စီးပြားရွာလူမွာေတြ႕ (၁၃.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-854-2018-04-17.mp3">၈၅၄။ ေန႔စဥ္ဆင္ႏႊဲသၾကၤန္ပြဲ (၁၇.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-855-2018-04-21.mp3">၈၅၅။ ရက္သစ္အခါမဂၤလာ (၂၁.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-856-2018-04-26.mp3">၈၅၆။ ဓမၼပူဇာရတနာ (၂၆.၄.၁၈)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-857-2018-04-25.mp3">၈၅၇။ ေမတၱာကိုတြဲရာျပည့္ပြဲ (၂၅.၄.၁၈)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-858-2018-04-28.mp3">၈၅၈။ ကိုယ့္ဟာကိုယ္သာေရြးခ်ယ္ပါ (၂၈.၄.၁၈)</a> </p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-859-2018-04-29.mp3">၈၅၉။ ထီးကိုလည္းတင္စိန္ဖူးတင္ (၂၉.၄.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-860-2018-06-27.mp3">၈၆၀။ လက္ေဆာင္စကားျမတ္တရား (၂၇.၆.၁၈) 
</a></p>
<p class="MsoNormal">
<a href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-861/YawSayaDawSirinandabhivamsa-861-2018-07-09.mp3">၈၆၁။ စိတ္လံုျခံဳမွကိုယ္ပိုင္ရ (၉.၇.၁၈)</a></p>
<p class="MsoNormal">
&nbsp;</p>
<p class="MsoNormal">
***************************</p><font face="Zawgyi-One">






								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								MP3 တရားေတာ္မ်ား</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2017-7-1993%20NhitLoneTharWellPhaYarTel.wma">၁၇-၇-၁၉၉၃ 
								ႏွလုံးသား၀ယ္ဘုရားတည္</a></font></p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2030-11-1996%20KongYarKoYorkThayCharPout.wma">၃၀-၁၁-၁၉၉၆ 
								ေကာင္းရာကိုေရာက္ေသခ်ာေပါက္</a></font></p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2013-11-1997%20BawaWaiSuMyatKogMhu.wma">၁၃-၁၁-၁၉၉၇ 
								ဘ၀ေ၀စုေကာင္းျမတ္မႈ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2017-11-1998%20KoeKoKoChitLuAhSit.wma">၁၇-၁၁-၁၉၉၈ 
								ကိုယ့္ကိုကိုယ္ခ်စ္ လူအစစ္</a></font></p>
<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2030-1-1998%20SateHtarKongMhaMateKoneYa.wma">၃၀-၁-၁၉၉၈ 
								စိတ္ထားေကာင္းမွမိတ္ေကာင္းရ<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%208-12-1999%20AhTheeTaYarAhNharTaKhu.wma">၈-၂-၁၉၉၉ အသီးတရာ 
								အၫွာ တစ္ခု<br>
								</a>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2017-10-1999%20TaYarSoneThuSateMaPu.wma">၁၇-၁၀-၁၉၉၉ 
								တရားေဆာင္သူ စိတ္မပူ</a></font></p>
								<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/Audio-Library/
YawSayaDaw/YawSayadaw%2029-10-1999%20BaWaPinLelKhaYeeThal.wma">၂၉-၁၀-၁၉၉၉ 
								ဘ၀ပင္လယ္ ခရီးသည္<br>
&nbsp;</a></font></p>
<p style="margin-top: 0px; margin-bottom: 0px" align="left">
								&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc01</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/001-Yawsayadaw-29-11-2002.mp3">၁။ 29-11-2002 စိတ္ဓာတ္ၿငိမ္းခ်မ္း လူ႔႔႔အစြမ္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/002-Yawsayadaw-24-2-1999.mp3">၂။ 24-2-1999 အိမ္တြင္းမဂၢင္ လူ႔႔က်င္႕စဥ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/003-Yawsayadaw-7-7-2002.mp3">၃။ 7-7-2002 အသိမွန္ကန္ ကိုယ္႔ဘို႔က်န္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/004-Yawsayadaw-23-7-1998.mp3">၄။ 23-7-1998 အမွန္တရား လူ႔႔စြမ္းအား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/005-Yawsayadaw-25-8-2004.mp3">၅။ 25-8-2004 ေမတၲာလႊမ္းၿခဳံ ေဘးရန္လုံ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/006-Yawsayadaw-12-12-1998.mp3">၆။ 12-12-1998 ကိုယ္႔ကိုကိုယ္ႏိုင္ စြမ္းအားပိုင္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/007-Yawsayadaw-3-12-2002.mp3">၇။ 3-12-2002 သမုဒၵရာ 
ဝမ္းတထြာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/008-Yawsayadaw.mp3">၈။ ကိုယ္ပိုင္အလုပ္ ခပ္သုတ္သုတ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/009-Yawsayadaw-3-2-2001.mp3">၉။ 3-2-2001 အသိမွန္ကန္ အဖိုးတန္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D01/010-Yawsayadaw.mp3">၁၀။ မီးသတိျပဳ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc02</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/001-Yawsayadaw-2-2-1996(1).mp3">၁။ 2-2-1996 ေမတၲာတရား လူ႔႔႔စြမ္းအား(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/002-Yawsayadaw-2-2-1996(2).mp3">၂။ 2-2-1996 ေမတၲာတရား လူ႔႔႔စြမ္းအား(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/003-Yawsayadaw-13-3-1989(1).mp3">၃။ 19-3-1989 ပုညကိရိယ၀တၳဳသုတၲန္(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/004-Yawsayadaw-13-3-1989(2).mp3">၄။ 19-3-1989 ပုညကိရိယ၀တၳဳသုတၲန္(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/005-Yawsayadaw-22-1-1987(1).mp3">၅။ 22-1-1987 ဒကၡိဏာဝိဘဂၤသုတၲန္(၁)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/006-Yawsayadaw-22-1-1987(2).mp3">၆။ 22-1-1987 ဒကၡိဏာဝိဘဂၤသုတၲန္(၂)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/007-Yawsayadaw-17-7-1993.mp3">၇။ 17-7-1993 လူ႕၏စြမ္းအား ျမတ္တရား</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/008-Yawsayadaw.mp3">ဂ။ကိုယ္႕ဝန္ကိုယ္ထမ္း လူ႔႔႔အစြမ္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/009-Yawsayadaw-3-10-2002.mp3">၉။ 3-10-2002 စိတ္အားတင္းမွ အႏုိင္ရ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D02/010-Yawsayadaw-2-11-2002.mp3">၁၀။ 2-11-2002 ခႏၲာကိုယ္ထဲ ေဘာလံုးပဲြ</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc03</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/001-Yawsayadaw.mp3">၁။&nbsp; 
ကုသိုလ္လည္းရ ဝမ္းလည္းဝ&nbsp;&nbsp; သန္လွ်င္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/002-Yawsayadaw.mp3">၂။&nbsp; 
သမုဒၵရာဝမ္းတထြာ&nbsp;&nbsp; အင္းစိန္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/003-Yawsayadaw.mp3">၃။&nbsp; 
ေမတၱာႏွလုံး အလွဆုံး&nbsp;&nbsp; ပန္းဘဲတန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/004-Yawsayadaw.mp3">၄။&nbsp; အသိးတရာ 
အညွာတခု&nbsp;&nbsp;&nbsp; အလုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/005-Yawsayadaw.mp3">၅။&nbsp; 
အသိမွန္ကန္ အဖိုးတန္&nbsp;&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/006-Yawsayadaw.mp3">၆။&nbsp; 
ႏွလုံးသားဝယ္ ဘုရားတည္&nbsp; </a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/007-Yawsayadaw.mp3">၇။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp;&nbsp; အလုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/008-Yawsayadaw.mp3">၈။&nbsp; 
စြမ္းရည္သုံးတန္ အာမခံ&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/009-Yawsayadaw.mp3">၉။&nbsp; 
ဘဝလက္ေဆာင္ စြမ္းအားေျပာင္&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/010-Yawsayadaw.mp3">၁၀။&nbsp; 
ေမတၱာေပါင္းစု ျမတ္ေကာင္မႈ&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D03/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ရဲရင့္စြန္႕စား မိန္းမသား&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc04</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/001-Yawsayadaw.mp3">၁။&nbsp; 
အမွန္တရား&nbsp; လူတရား&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/002-Yawsayadaw.mp3">၂။&nbsp; 
ကိုယ့္လမ္းကိုယ္ေလွ်ာက္ ေကာင္းရာေရာက္&nbsp;&nbsp;&nbsp; အလုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/003-Yawsayadaw.mp3">၃။&nbsp; 
စိတ္ေအးစရာ မဂၤလာ&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/004-Yawsayadaw.mp3">၄။&nbsp; 
လူ၏စြမ္းအား ျမတ္တရား&nbsp;&nbsp;&nbsp; မဂၤလာဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/005-Yawsayadaw.mp3">၅။&nbsp; 
ဘဝတန္ဖိုးလူ႕တန္ခိုး&nbsp;&nbsp;&nbsp; စမ္ေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/006-Yawsayadaw.mp3">၆။&nbsp; 
ဘဝတန္ဖိုး လူ႕တန္ခိုး&nbsp;&nbsp;&nbsp; မႏ ၱေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/007-Yawsayadaw.mp3">၇။&nbsp; 
အိမ္တြင္းမဂၢင္ လူ႕က်င့္စဥ္&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/008-Yawsayadaw.mp3">၈။&nbsp; 
ေမတၱာလြမ္းၿခဳံ ေဘးရန္လုံ&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/009-Yawsayadaw.mp3">၉။&nbsp; 
အၾကမ္းအႏု စိတ္ကိုလု&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/010-Yawsayadaw.mp3">၁၀။&nbsp; 
စိတ္ကိုႏိုင္မွ ခ်မ္းသာရ&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D04/011-Yawsayadaw.mp3">၁၁။&nbsp; 
အသီးတစ္ရာ အညႇာတစ္ခု&nbsp;&nbsp;&nbsp; ကန္ေတာရ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc05</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/001-Yawsayadaw.mp3">၁။&nbsp; 
ေမတၱာလက္တြဲ ကုသိုလ္ပြဲ&nbsp;&nbsp;&nbsp; ေညာင္တုန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/002-Yawsayadaw.mp3">၂။&nbsp; 
လူေတာ္လူေကာင္း လြတ္ၿငိမ္ေၾကာင္း&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/003-Yawsayadaw.mp3">၃။&nbsp; 
ဆင္းရဲ၏ေနာက္ ခ်မ္းသာေရာက္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/004-Yawsayadaw.mp3">၄။&nbsp; 
အသိမွန္ကန္ အဖိုးတန္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/005-Yawsayadaw.mp3">၅။&nbsp; 
စင္ၾကယ္ျမင့္ျမတ္ လူ႕စိတ္ဓါတ္&nbsp;&nbsp;&nbsp; အလုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/006-Yawsayadaw.mp3">၆။&nbsp; 
စိန္တလုံး&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/007-Yawsayadaw.mp3">၇။&nbsp; 
မီးသတိျပဳ&nbsp;&nbsp;&nbsp; စမ္ေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/008-Yawsayadaw.mp3">၈။&nbsp; 
သတိစြဲကိုင္ ႏႈတ္ဆက္ပြဲ&nbsp;&nbsp;&nbsp; ရန္ကင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/009-Yawsayadaw.mp3">၉။&nbsp; ဗိုလ္&nbsp;&nbsp;&nbsp; 
မဂၤလာဒုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/010-Yawsayadaw.mp3">၁၀။&nbsp; 
ေမတၱာေက်းဇူး စြမ္ရည္ထူး&nbsp;&nbsp;&nbsp; ေလးေထာင့္ကန္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D05/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ဘဝစာေမးပြဲ&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc06</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/001-Yawsayadaw.mp3">၁။&nbsp; 
အလႉေက်းဇူး စြမ္ရည္ထူး&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/002-Yawsayadaw.mp3">၂။&nbsp; 
ပုညႀကိယဝတၱဳသုတၱန္&nbsp;&nbsp;&nbsp; တြံေတး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/003-Yawsayadaw.mp3">၃။&nbsp; 
ဘဝတစ္ေခါက္ ခဏေရာက္&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/004-Yawsayadaw.mp3">၄။&nbsp; 
ကိုယ့္အားကိုယ္ကိုး လူ႕တန္ဖိုး&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/005-Yawsayadaw.mp3">၅။&nbsp; 
တရားအသိလူ႕မ်က္စိ&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/006-Yawsayadaw.mp3">၆။&nbsp; 
ပစၥည္းတန္ဖိုး လူ႕တန္ဖိုး&nbsp;&nbsp;&nbsp;&nbsp; ေက်ာက္ေျမာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/007-Yawsayadaw.mp3">၇။&nbsp; 
အသိမွန္ကန္ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/008-Yawsayadaw.mp3">၈။&nbsp; 
အသြားမတတ္ မ်က္ေျချပတ္&nbsp;&nbsp;&nbsp; ၿမိတ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/009-Yawsayadaw.mp3">၉။&nbsp; 
ေျမသန္႕မဂၤလာ&nbsp;&nbsp;&nbsp; ကေမၻာဇအိမ္ရာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D06/010-Yawsayadaw.mp3">၁၀။&nbsp; 
၄၅-ႏွစ္ တရားသက္&nbsp;&nbsp;&nbsp; မဂၤလဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc07</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/001-Yawsayadaw.mp3">၁။ ဘဝျပင္က်ယ္ 
ခရီးသည္&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/002-Yawsayadaw.mp3">၂။&nbsp; 
ေမတၱႏွလုံး အလွဆုံး&nbsp;&nbsp;&nbsp; ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/003-Yawsayadaw.mp3">၃။&nbsp; 
လုပ္အားတန္ဖိုး လူ႕တန္ခိုး&nbsp;&nbsp;&nbsp; မရမ္ကုန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/004-Yawsayadaw.mp3">၄။&nbsp; 
စိတ္ဓါတ္ၿငိမ္းခ်မ္း လူ႕အစြမ္း&nbsp;&nbsp;&nbsp; မဂ္လဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/005-Yawsayadaw.mp3">၅။&nbsp; 
အသိမွန္ကန္ အဖိုးတန္&nbsp;&nbsp;&nbsp; ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/006-Yawsayadaw.mp3">၆။&nbsp; 
ေက်ာင္း၏ေက်းဇူးစြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/007-Yawsayadaw.mp3">၇။&nbsp; 
တရားစုေဆာင္း၊ အေဖာ္ေကာင္း&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/008-Yawsayadaw.mp3">၈။&nbsp; 
ႏွလုံးသားဝယ္ တရားတည္&nbsp;&nbsp;&nbsp; ပုဇြန္ေတာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/009-Yawsayadaw.mp3">၉။&nbsp; 
ခႏၶာကိုယ္ အလုပ္ခပ္သုတ္သုတ္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/010-Yawsayadaw.mp3">၁၀။&nbsp; 
တရားရေအး အၿမိဳက္ေဆး&nbsp;&nbsp;&nbsp; မဂ္လဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ကိုယ္ပိုင္ အလုပ္ခပ္သုတ္သုတ္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D07/012-Yawsayadaw.mp3">၁၂။&nbsp; အား&nbsp;&nbsp;&nbsp; 
ေတာင္ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc08</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/001-Yawsayadaw.mp3">၁။&nbsp; 
နေမာဗုဒၶႆ&nbsp;&nbsp;&nbsp; လိႈင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/002-Yawsayadaw.mp3">၂။&nbsp; 
အသိဆန္းၾကယ္ အႏွစ္ႂကြယ္&nbsp;&nbsp;&nbsp; မင္းကြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/003-Yawsayadaw.mp3">၃။&nbsp; 
ႏွလုံးသားဝယ္ ဘုရားတည္&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/004-Yawsayadaw.mp3">၄။&nbsp; 
ေမတၱာေပါင္းစုျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/005-Yawsayadaw.mp3">၅။&nbsp; 
လူ၏စြမ္းအားျမတ္တရား&nbsp;&nbsp;&nbsp; ေျမာက္ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/006-Yawsayadaw.mp3">၆။&nbsp; 
ႏႈတ္ဆက္မဂၤလာ&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/007-Yawsayadaw.mp3">၇။&nbsp; 
အသိအမွန္ အဖိုးတန္&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/008-Yawsayadaw.mp3">၈။&nbsp; 
စိတ္ေကင္းထားက မိတ္ေကာင္းရ&nbsp;&nbsp;&nbsp; ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/009-Yawsayadaw.mp3">၉။&nbsp; 
ေက်ာင္း၏ေက်းဇူး စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; ေျမာက္ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/010-Yawsayadaw.mp3">၁၀။&nbsp; 
ရဲရင့္စြန္႕စား မိန္းမသား&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D08/011-Yawsayadaw.mp3">၁၁။&nbsp; 
တရားတန္ခိုး စြမ္းအာတိုး&nbsp;&nbsp;&nbsp; ၿမိတ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc09</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/001-Yawsayadaw.mp3">၁။&nbsp; 
ပညာဦးစီးအလႉႀကီး&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/002-Yawsayadaw.mp3">၂။&nbsp; 
ေမတၱာေပါင္းစု ျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/003-Yawsayadaw.mp3">၃။&nbsp; 
မီးသတိျပဳ&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/004-Yawsayadaw.mp3">၄။&nbsp; ဥပၸါဒႏိ 
ၱ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/005-Yawsayadaw.mp3">၅။&nbsp; 
ေမတၱာေပါင္းစု ျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; ရန္ကင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/006-Yawsayadaw.mp3">၆။&nbsp; 
စိတ္ဓါတ္ျမင့္တင္ စြမ္းအားရွင္&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/007-Yawsayadaw.mp3">၇။&nbsp; 
စိတ္ေအးစရာ အားေလးျဖာ&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/008-Yawsayadaw.mp3">၈။&nbsp; 
ေဘာဇဥ္ေက်းဇူးစြမ္ရည္ထူး&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/009-Yawsayadaw.mp3">၉။&nbsp; 
ကုသိုလ္ဂုဏ္ရွိန္ လူ႕အရွိန္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/010-Yawsayadaw.mp3">၁၀။&nbsp; 
တရားေရေအးအၿမိဳက္ေဆး&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D09/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ကိုယ့္ကိုကိုယ္ႏိုင္စြမ္းအားပိုင္&nbsp;&nbsp;&nbsp; ဆူးေလ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc10</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/001-Yawsayadaw.mp3">၁။&nbsp; 
ေမတၱာႏွလုံး အလွဆုံး&nbsp;&nbsp;&nbsp; ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/002-Yawsayadaw.mp3">၂။&nbsp; 
ဘဝေဝစုျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; ဆက္သြယ္ေရး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/003-Yawsayadaw.mp3">၃။&nbsp; 
ပ႒ာန္းေက်းဇူး စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/003-Yawsayadaw.mp3">၄။&nbsp; 
ေမတၱာေပါင္းစု စိန္ရတု&nbsp;&nbsp;&nbsp; သထုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/005-Yawsayadaw.mp3">၅။&nbsp; 
အသိမွန္ကန္ အဖိုးတန္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/006-Yawsayadaw.mp3">၆။&nbsp; 
စိတ္ဓါတ္ျမႇင့္ ပညာရ်င္&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/007-Yawsayadaw.mp3">၇။&nbsp; 
လူ၏စြမ္းအားျမတ္တရား&nbsp;&nbsp;&nbsp; ကုန္သည္မ်ားဟိုတယ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/008-Yawsayadaw.mp3">၈။&nbsp; 
သမုဒၵရာဝမ္တထြာ&nbsp;&nbsp;&nbsp; သန္လွ်င္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/009-Yawsayadaw.mp3">၉။&nbsp;&nbsp; 
ကိုယ့္ကိုကိုယ္ေစာင့္ေရွာက္ ေဘးမေၾကာက္&nbsp;&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/010-Yawsayadaw.mp3">၁၀။&nbsp; 
စိတ္ေအးစရာအားေလးျဖာ&nbsp;&nbsp;&nbsp; လိႈင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ဥစၥထုပ္&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D10/012-Yawsayadaw.mp3">၁၂။&nbsp; 
အဆင္းအတက္ လမ္းႏွစ္ဘက္&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc11</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/001-Yawsayadaw.mp3">၁။&nbsp; 
သမုဒၵရာဝမ္တစ္ထြာ&nbsp;&nbsp;&nbsp; အင္းစိန္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/002-Yawsayadaw.mp3">၂။&nbsp; 
ကိုယ့္ကိုကိုယ္ခ်စ္ လူအစစ္&nbsp;&nbsp;&nbsp;&nbsp; ရန္ကင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/003-Yawsayadaw.mp3">၃။&nbsp; 
သာဓုသုံးပါးျမတ္တရား&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/004-Yawsayadaw.mp3">၄။&nbsp; 
ေမတၱာႏွလံုး အလွဆုံး&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/005-Yawsayadaw.mp3">၅။&nbsp; 
အခ်ိန္ကိုထိန္း အပူျငမ္း&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/006-Yawsayadaw.mp3">၆။&nbsp; အား&nbsp;&nbsp;&nbsp; 
ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/007-Yawsayadaw.mp3">၇။&nbsp; 
ေမတၱာႏွလုံး အလွဆု့း&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/008-Yawsayadaw.mp3">၈။&nbsp; 
အလႉေက်းဇူးစြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/009-Yawsayadaw.mp3">၉။&nbsp; 
အသိမွန္ကန္ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/010-Yawsayadaw.mp3">၁၀။&nbsp; 
စိတ္ေအးစရာ သာသနာ&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/011-Yawsayadaw.mp3">၁၁။&nbsp; 
အမွန္တရားလူ႕စြမ္းအား&nbsp;&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D11/012-Yawsayadaw.mp3">၁၂။&nbsp; 
အသီးတရာ အညႇာတစ္ခု&nbsp;&nbsp;&nbsp; ဥကၠံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc12</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/001-Yawsayadaw.mp3">၁။&nbsp; 
ကုသိုလ္ထုံမႊန္း နိဗၺာန္လမ္း&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/002-Yawsayadaw.mp3">၂။&nbsp; 
ေမတၱာေက်းဇူး စြမ္ရည္ထူး&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/003-Yawsayadaw.mp3">၃။ ေမတၱာေပါင္းစု 
စိန္ရတု&nbsp;&nbsp;&nbsp; ေညာင္တုန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/004-Yawsayadaw.mp3">၄။&nbsp; 
ဗုဒၶရတနာ အားကိုးပါ&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/005-Yawsayadaw.mp3">၅။&nbsp; 
အသိစင္ၾကယ္ စြမ္းရည္ႂကြယ္&nbsp;&nbsp;&nbsp; ေျမာက္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/006-Yawsayadaw.mp3">၆။&nbsp; 
ပညာဦးစီးအလႉႀကီး&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/007-Yawsayadaw.mp3">၇။&nbsp; 
အမွန္ေလးပါး ျမတ္တရား&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/008-Yawsayadaw.mp3">၈။&nbsp; 
အမွန္ေလးပါး ျမတ္တရား&nbsp;&nbsp;&nbsp; စမ္ေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/009-Yawsayadaw.mp3">၉။&nbsp; 
စိတ္ေအးစရာ လူ႕ခ်မ္းသာ&nbsp;&nbsp;&nbsp; လိႈင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/010-Yawsayadaw.mp3">၁၀။&nbsp; 
ေမတၱာပန္းခိုင္ သုံးပြင့္ဆိုင္&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ႏွလုံးသားဝယ္ တရားတည္&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D12/012-Yawsayadaw.mp3">၁၂။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc13</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/001-Yawsayadaw.mp3">၁။&nbsp; 
လက္ေတြ႕အလုပ္ ေမတၱာသုတ္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/002-Yawsayadaw.mp3">၂။&nbsp; 
ေမတၱာေပါင္းစု ေရႊရတု&nbsp;&nbsp;&nbsp; လမ္းမေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/003-Yawsayadaw.mp3">၃။&nbsp; 
တရားေက်းဇူး စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; ပုဇြန္ေတာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/004-Yawsayadaw.mp3">၄။&nbsp; 
ကိုယ့္လမ္းကိုယ္ေလွ်ာက္ ေကာင္းရာေရာက္&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/005-Yawsayadaw.mp3">၅။&nbsp; 
အဆင္းအတက္လမ္းႏွစ္ဘက္&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/006-Yawsayadaw.mp3">၆။&nbsp; 
ပ႒ာန္းေက်းဇူးစြမ္းရည္ထူး&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/007-Yawsayadaw.mp3">၇။&nbsp; 
ေမတၱာႏွလုံး အလွဆုံး&nbsp;&nbsp;&nbsp; လႈိင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/008-Yawsayadaw.mp3">၈။&nbsp; 
ကိုယ့္ကိုကိုယ္ႏိုင္စြမ္းအားပိုင္&nbsp;&nbsp;&nbsp; ေျမာက္ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/009-Yawsayadaw.mp3">၉။&nbsp; 
ဘုရားဆုံးမၾသဝါဒ&nbsp;&nbsp;&nbsp; မဂၤလာဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/010-Yawsayadaw.mp3">၁၀။&nbsp; 
အသိမွန္ကန္အဖိုးတန္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ဘဝေဝစုျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D13/012-Yawsayadaw.mp3">၁၂။&nbsp; 
စိတ္ေကာင္းထားက မိတ္ေကာင္းရ&nbsp;&nbsp;&nbsp; မဂၤလာဒုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc14</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/001-Yawsayadaw.mp3">၁။&nbsp; 
နေမာဗုဒၶႆ&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/002-Yawsayadaw.mp3">၂။&nbsp; 
ေမတၱာေပါင္စု ျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/003-Yawsayadaw.mp3">၃။&nbsp; 
ႏွလံုးသားဝယ္ ဘုရာတည္&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/004-Yawsayadaw.mp3">၄။&nbsp; 
ကိုယ့္ကိုကိုယ္ႏိုင္ စြမ္းအားပိုင္&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/005-Yawsayadaw.mp3">၅။&nbsp; 
ေမတၱာေက်းဇူး စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; ရန္ကင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/006-Yawsayadaw.mp3">၆။&nbsp; 
အသိစင္ၾကယ္စြမ္းရည္ႂကြယ္&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/007-Yawsayadaw.mp3">၇။&nbsp; 
စိတ္ေအးစရာ လူ႕ခ်မ္းသာ&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/008-Yawsayadaw.mp3">၈။&nbsp; 
ကိုယ့္ကိုကိုယ္ခ်စ္ လူအစစ္&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/009-Yawsayadaw.mp3">၉။&nbsp; 
တရားေက်းဇူး စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/010-Yawsayadaw.mp3">၁၀။&nbsp; 
အိမ္တြင္းမဂၢင္ လူ႕က်င့္စဥ္&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/011-Yawsayadaw.mp3">၁၁။&nbsp; 
တရားစုေဆာင္း ခ်မ္းသာေၾကာင္း&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D14/012-Yawsayadaw.mp3">၁၂။&nbsp; 
အသီးတရာအညႇာတစ္ခု&nbsp;&nbsp;&nbsp; ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc15</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/001-Yawsayadaw.mp3">၁။&nbsp; 
သုံးပါးျမတ္စြာ မဂၤလာ&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/002-Yawsayadaw.mp3">၂။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/003-Yawsayadaw.mp3">၃။&nbsp; 
ေမတၱာအလုပ္ အႏွစ္ခ်ဳပ္&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/004-Yawsayadaw.mp3">၄။&nbsp; 
ပ႒ာန္းေက်းဇူးစြမ္ရည္ထူး&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/005-Yawsayadaw.mp3">၅။&nbsp; 
ေမတၱာႏွလုံး အလွဆုံး&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/006-Yawsayadaw.mp3">၆။&nbsp; 
ကိုယ့္ကိုကိုယ္ႏိုင္စြမ္းအားပိုင္&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/007-Yawsayadaw.mp3">၇။&nbsp; 
ေမတၱာပန္းခိုင္ သုံးပြင့္ဆိုင္&nbsp;&nbsp; မဂၤလာဒုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/008-Yawsayadaw.mp3">၈။&nbsp; 
စားဖြယ္ေက်းဇူး စြမ္းရည္ထူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/009-Yawsayadaw.mp3">၉။&nbsp; 
တရားစုေဆာင္း ခ်မ္းသာေၾကာင္း&nbsp;&nbsp;&nbsp; ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/010-Yawsayadaw.mp3">၁၀။&nbsp; 
တရားအသိလူ႕မ်က္စိ&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ထိုက္တန္သူမွ ေကာင္းတာရ&nbsp;&nbsp;&nbsp; စက္မႈ(၁)ဓမၼာရုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D15/012-Yawsayadaw.mp3">၁၂။&nbsp; 
သမုဒၵရာ ဝမ္းတထြာ&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc16</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/001-Yawsayadaw.mp3">၁။&nbsp; 
ေမတၱာပန္းခိုင္ သုံးပြင့္ဆိုင္&nbsp;&nbsp;&nbsp; ေထာက္ၾကန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/002-Yawsayadaw.mp3">၂။&nbsp; 
အသိထူးျခား လူ႕စြမ္းအား&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/003-Yawsayadaw.mp3">၃။&nbsp; 
ခ်စ္ခင္ညီညြတ္ ေမတၱာဓါတ္&nbsp;&nbsp;&nbsp; မဂၤလာဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/004-Yawsayadaw.mp3">၄။&nbsp; 
ဘဝလက္ေဆာင္ စြမ္းအားေျပာင္&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/005-Yawsayadaw.mp3">၅။&nbsp; 
အိမ္တြင္းမဂၢင္ လူ႕က်င့္စဥ္&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/006-Yawsayadaw.mp3">၆။&nbsp; 
တရားေရေအး အႃမိႈက္ေဆး&nbsp;&nbsp;&nbsp; ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/007-Yawsayadaw.mp3">၇။&nbsp; 
ေမတၱာေက်းဇူး စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/008-Yawsayadaw.mp3">၈။&nbsp; 
ေကာင္းတာရွိမွ လိုတာရ&nbsp;&nbsp;&nbsp; ေျမာက္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/009-Yawsayadaw.mp3">၉။&nbsp; 
အသိမွန္ကန္ အဖိုးတန္&nbsp;&nbsp; ဆူးေလ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/010-Yawsayadaw.mp3">၁၀။&nbsp; 
အသီးတစ္ရာ အညႇာတစ္ခု&nbsp;&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/011-Yawsayadaw.mp3">၁၁။&nbsp; 
လူ၏စြမ္းအားျမတ္တရား&nbsp;&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D16/012-Yawsayadaw.mp3">၁၂။&nbsp; 
ေမတၱာေပါင္းစု ျမတ္ေကာင္းမႈ&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc17</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/001-Yawsayadaw.mp3">၁။&nbsp; 
သုတေက်းဇူးစြမ္ရည္ထး&nbsp;&nbsp;&nbsp; အင္းစိန္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/002-Yawsayadaw.mp3">၂။&nbsp; 
ေမတတာတရားလူ႕စြမ္းအား&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/003-Yawsayadaw.mp3">၃။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp; ပုဇြန္ေတာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/004-Yawsayadaw.mp3">၄။ 
ေမတၱာေက်းဇူးစြမ္ရည္ထူး&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/005-Yawsayadaw.mp3">၅။&nbsp; အသိးတရာ 
အညႇာတခု&nbsp;&nbsp;&nbsp; ေျမာက္ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/006-Yawsayadaw.mp3">၆။&nbsp; 
တရားေဆာင္သူစိတ္မပူ&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/007-Yawsayadaw.mp3">၇။&nbsp; 
လူ၏စြမ္းအား ျမတ္တရား&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/008-Yawsayadaw.mp3">၈။&nbsp; 
အသိမွန္ကန္ အဖိုးတန္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/009-Yawsayadaw.mp3">၉။&nbsp; 
ဘဝပင္လယ္ ခရီးသာ္&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/010-Yawsayadaw.mp3">၁၀။&nbsp; 
စိတ္ဓြတ္ျမႇင့္တင္ ကံထူးရွင္&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D17/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ႏွလုံးသားဝယ္ ဘုရာဒတည္&nbsp;&nbsp; မရမ္းကုန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc18</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/001-Yawsayadaw.mp3">၁။ 
ႏွလံုးသားဝယ္ဘုရားတည္&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလဗ်ဴဟာ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/002-Yawsayadaw.mp3">၂။ 
အသိမွန္ကန္အဖိုးတန္&nbsp;&nbsp;&nbsp;&nbsp; ဗဟန္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/003-Yawsayadaw.mp3">၃။ 
ကိုယ္ပိုင္အလုပ္ဥစၥာထုပ္ (ကံျမင္.တရား)&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/004-Yawsayadaw.mp3">၄။ 
လူ၏စြမ္းအားျမတ္တရား&nbsp;&nbsp;&nbsp;&nbsp; ေတာင္ဒဂံု</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/005-Yawsayadaw.mp3">၅။ 
အသီးတရားအညွာတစ္ခု&nbsp;&nbsp;&nbsp; တိုက္ၾကီး</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/006-Yawsayadaw.mp3">၆။ 
ဘဝပင္လယ္ခရီးသည္&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/007-Yawsayadaw.mp3">၇။ 
အခ်ိန္ကိုထိန္းအပူၿငိမ္း&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/008-Yawsayadaw.mp3">၈။ 
စိတ္ဓါတ္ျမွင္.တင္ကန္ထူးရွင္&nbsp;&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာပ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/009-Yawsayadaw.mp3">၉။ 
စိတ္ကိုယ္ထိန္းေၾကာင္းအခ်ိန္ေကာင္း&nbsp;&nbsp;&nbsp;&nbsp; 
ဦးစိန္သန္း+ေဒၚသန္းသန္း (ေနအိမ္)</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/010-Yawsayadaw.mp3">၁၀။ အဆိတ္ကင္းကြာ 
လူခ်မ္းသာ&nbsp;&nbsp;&nbsp;&nbsp; တာေမြ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D18/011-Yawsayadaw.mp3">၁၁။ 
တရားအသိလူမ်က္စိ&nbsp;&nbsp;&nbsp;&nbsp; ၾကည္.ျမင္တိုင္</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc19</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/001-Yawsayadaw.mp3">၁။ 
ေမတၱာေက်းဇူးစြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာပ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/002-Yawsayadaw.mp3">၂။ 
ကိုယ္.ကိုကိုယ္ခ်စ္လူအစစ္&nbsp;&nbsp;&nbsp;&nbsp; သာေကတ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/003-Yawsayadaw.mp3">၃။ 
ေမတၱာတရားလူ.စြမ္းအား&nbsp;&nbsp;&nbsp;&nbsp; သံုးခြ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/004-Yawsayadaw.mp3">၄။ 
လူ၏စြမ္းအားျမတ္တရား&nbsp;&nbsp;&nbsp;&nbsp; အင္းစိန္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/005-Yawsayadaw.mp3">၅။ 
အသီးတရာအညွာတစ္ခု&nbsp;&nbsp;&nbsp;&nbsp; သာေကတ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/006-Yawsayadaw.mp3">၆။ 
အသိမွန္ကန္အဖိုးတန္&nbsp;&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာပ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/007-Yawsayadaw.mp3">၇။ 
အခ်ိန္ကိုထိန္းအပူၿငိမ္း&nbsp;&nbsp;&nbsp;&nbsp; သာေကတ</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/008-Yawsayadaw.mp3">၈။ 
စိတ္ဓါတ္ျမွင္.တင္ကန္ထူးရွင္&nbsp;&nbsp;&nbsp;&nbsp; လမ္းမေတာ္</a><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/009-Yawsayadaw.mp3">၉။ 
ယဥ္ေက်းလိမ္မၼာအားကိုးရာ&nbsp;&nbsp;&nbsp;&nbsp; မႏၱေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/010-Yawsayadaw.mp3">၁၀။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ခပ္သုတ္သုတ္&nbsp;&nbsp;&nbsp; မဂၤလဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D19/011-Yawsayadaw.mp3">၁၁။&nbsp; 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">****dhamma talks uploaded and published on 
23 August 2009****</p>
								<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc20</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/001-Yawsayadaw.mp3">၁။ 
သုံးပါးျမတ္စြာ ကိုးကြယ္ရာ&nbsp;&nbsp;&nbsp;&nbsp; ဗိုလ္တစ္ေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/002-Yawsayadaw.mp3">၂။ 
ေမတၱာပန္းခိုင္ သုံးပြင့္ဆိုင္&nbsp;&nbsp;&nbsp;&nbsp; ေျမာက္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/003-Yawsayadaw.mp3">၃။အသီးတစ္ရာ 
အညႇာတစ္ခု&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/004-Yawsayadaw.mp3">၄။ အသိမွန္ကန္ 
အဖိုးတန္&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/005-Yawsayadaw.mp3">၅။ လူ၏စြမ္းအား 
ျမတ္တရား</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/006-Yawsayadaw.mp3">၆။ 
စိတ္ကိုထိန္းေၾကာင္း အခ်ိန္ေကာင္း&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/007-Yawsayadaw.mp3">၇။ 
ကိုယ္ပိုင္အလုပ္ ခပ္သုတ္သုတ္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/008-Yawsayadaw.mp3">၈။ ဘဝဇာတ္ခုံ 
ပုံစံစုံ&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/009-Yawsayadaw.mp3">၉။ ဗုဒၶလမ္းညႊန္ 
အက်င့္မွန္&nbsp;&nbsp;&nbsp; မဟာဝိဇယေစတီ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/010-Yawsayadaw.mp3">၁၀။ အခ်ိန္တနဖိုး 
လူ႕တန္ဖိုး&nbsp;&nbsp;&nbsp;&nbsp; ပညာေရာတကၠသိုလ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D20/011-Yawsayadaw.mp3">၁၁။ အိမ္တြင္း 
မဂၢင္လူ႕က်င့္စဥ္&nbsp;&nbsp;&nbsp; ရွမ္းျပည္နယ္</a></font></p>
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
<font size="5">MP3 Disc21</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/001-Yawsayadaw.mp3">၁။ လူ၏စြမ္းအား 
ျမတ္တရား&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာဒုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/002-Yawsayadaw.mp3">၂။ အသ္မွန္ကန္ 
အဖိုးတန္&nbsp;&nbsp;&nbsp; ေျမာက္ဒဂုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/003-Yawsayadaw.mp3">၃။ ေမတၱာေက်းဇူး 
စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/004-Yawsayadaw.mp3">၄။ အသီးတစ္ရာ 
အညွာတစ္ခု&nbsp;&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/005-Yawsayadaw.mp3">၅။ ယဥ္ေက်းလိမၼာ 
အားကိုးရာ&nbsp;&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/006-Yawsayadaw.mp3">၆။ ဗုဒၶလမ္းညႊန္ 
အက်င့္မွန္&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/007-Yawsayadaw.mp3">၇။ ဘဝတန္ဖိုး 
လူ႕တန္ခိုး&nbsp;&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/008-Yawsayadaw.mp3">၈။ 
စိတ္ထားေကာင္းက မိတ္ေကာင္းရ&nbsp;&nbsp;&nbsp;&nbsp; ကေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/009-Yawsayadaw.mp3">၉။&nbsp; 
တရားအသိလူ႕မ်က္စိ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D21/010-Yawsayadaw.mp3">၁၀။ တရားမေမ့ 
ဘုရားေန႕&nbsp;&nbsp;&nbsp; မဂၤလာဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc22</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One"><br>
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/001-Yawsayadaw.mp3">၁။ 
ေမတၱာလက္ေဆာင္စြမ္းအားေျပာင္&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာဗ်ဴဟာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/002-Yawsayadaw.mp3">၂။ အသီးတစ္ရာ 
အညႇာတစ္ခု&nbsp;&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/003-Yawsayadaw.mp3">၃။ 
ကိုယ့္ကိုႏိုင္မွ စြမ္းအားရ&nbsp;&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/004-Yawsayadaw.mp3">၄။ 
ေမတၱာေက်းဇူးစြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/005-Yawsayadaw.mp3">၅။ အသိမွန္ကန္ 
အဖိုးတန္&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာဒုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/006-Yawsayadaw.mp3">၆။ တရားစုေဆာင္း 
ခ်မ္းသာေၾကာင္း&nbsp;&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/007-Yawsayadaw.mp3">၇။ တရားအသိ 
လူ႕မ်က္စိ&nbsp;&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/008-Yawsayadaw.mp3">၈။ ထိုက္တန္သူမွ 
ေကာင္းတာရ&nbsp;&nbsp;&nbsp;&nbsp; ဆူးေလ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/009-Yawsayadaw.mp3">၉။ ကုသိုလ္လည္းရ 
ဝမ္းလည္းဝ&nbsp;&nbsp;&nbsp;&nbsp; သန္လွ်င္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D22/010-Yawsayadaw.mp3">၁၀။ 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp;&nbsp;&nbsp; အလုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">၁၁။ အသိမွန္ကန္ ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp; 
အလုံ</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc23</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/001-Yawsayadaw.mp3">၁။ 
ေမတၱာတရားလူစြမ္းအား&nbsp;&nbsp;&nbsp; အင္းစိန္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/002-Yawsayadaw.mp3">၂။ 
ေမတၱေက်းဇူးစြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/003-Yawsayadaw.mp3">၃။ 
ေမတၱာပန္းခိုင္ သုံးပြင့္ဆိုင္&nbsp;&nbsp;&nbsp;&nbsp; အလုံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/004-Yawsayadaw.mp3">၄။ အသီးတစ္ရာ 
အညႇာတစ္ခု&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/005-Yawsayadaw.mp3">၅။ 
တည္ၿငိမ္ေအးခ်မ္း လူ႕အစြမ္း&nbsp;&nbsp;&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/006-Yawsayadaw.mp3">၆။ အသိလက္ဦး 
စြမ္ရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; ပုဇြန္ေတာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/007-Yawsayadaw.mp3">၇။ အခ်ိန္တန္ဖိုး 
လူ႕တန္ဖိုး&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/008-Yawsayadaw.mp3">၈။ တရားအသိ 
လူ႕မ်က္စိ&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/009-Yawsayadaw.mp3">၉။ လူ၏စြမ္းအား 
ျမတ္တရား&nbsp;&nbsp;&nbsp;&nbsp; မဟာဝိဇယေစတီ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D23/010-Yawsayadaw.mp3">၁၀။ 
အိမ္တြင္းမဂၢင္ လူ႕က်င့္စဥ္&nbsp;&nbsp;&nbsp; ရွမ္းျပည္နယ္&nbsp; </a><br>
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
<font size="5">MP3 Disc24</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/001-Yawsayadaw.mp3">၁။ 
ေမတၱာလႊမ္းၿခံဳ ေဘးရန္လုံ&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/002-Yawsayadaw.mp3">၂။ ေမတၱာလက္တြဲ 
ကုသ္ုလ္ပြဲ&nbsp;&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/003-Yawsayadaw.mp3">၃။ ေမတၱႏွလုံ 
အလွဆုံး&nbsp;&nbsp;&nbsp;&nbsp; ဗိုလ္တေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/004-Yawsayadaw.mp3">၄။ အသီးတစ္ရာ 
အညႇာတစ္ခု&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/005-Yawsayadaw.mp3">၅။ အသိမွန္ကန္ 
ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/006-Yawsayadaw.mp3">၆။ အသိလက္ဦး 
စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; သဃၤန္းကၽြန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/007-Yawsayadaw.mp3">၇။ 
ေအးျမရႊင္ၿပံဳး လူ႕ႏွလုံး&nbsp;&nbsp;&nbsp;&nbsp; ဗိုလ္တစ္ေထာင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/008-Yawsayadaw.mp3">၈။ 
အသိမွန္ကန္ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/009-Yawsayadaw.mp3">၉။ တရားအသိ 
လူ႕မ်က္စိ&nbsp;&nbsp;&nbsp;&nbsp; တိပိဋကပူဇာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/010-Yawsayadaw.mp3">၁၀။ 
တရားေလးေထြက်က္သေရ&nbsp;&nbsp;&nbsp;&nbsp; လိႉင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/011-Yawsayadaw.mp3">၁၁။ အား&nbsp;&nbsp;&nbsp;&nbsp; 
ပဲခူး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D24/012-Yawsayadaw.mp3">၁၂။ 
ယဥ္ေက်းလိမ္မာ လူခ်မ္းသာ&nbsp;&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="5">MP3 Disc25</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/001-Yawsayadaw.mp3">၁။ ဘဝတစ္ေခါက္ 
ခဏေရာက္&nbsp;&nbsp;&nbsp;&nbsp; လႉိင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/002-Yawsayadaw.mp3">၂။ ဗုဒၶေက်းဇုး 
စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/003-Yawsayadaw.mp3">၃။ နေမာဗုဒၶႆ&nbsp;&nbsp;&nbsp;&nbsp; 
လႉိင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/004-Yawsayadaw.mp3">၄။ ေမတၱာႏွလုံး 
အလွဆုံး&nbsp;&nbsp;&nbsp; မဂၤလာေတာင္ညြန္႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/005-Yawsayadaw.mp3">၅။ ေမတၱာေပါင္းစု 
ျမတ္ေကာင္းမႉ&nbsp;&nbsp;&nbsp;&nbsp; ဗဟန္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/006-Yawsayadaw.mp3">၆။ တရားစုဆာင္း 
အေဖာ္ေကာင္း&nbsp;&nbsp;&nbsp;&nbsp; လႉိင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/007-Yawsayadaw.mp3">၇။ ေမတၱာေက်းဇူး 
စြမ္းရည္ထူး&nbsp;&nbsp;&nbsp;&nbsp; က်ိဳကၠဆံ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/008-Yawsayadaw.mp3">၈။ 
ကိုယ့္ကိုကိုယ္ ခ်စ္လူအစစ္&nbsp;&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/009-Yawsayadaw.mp3">၉။ 
ကိုယ္ပိုင္အလုပ္ ဥစၥာထုပ္&nbsp;&nbsp;&nbsp; တာေမြ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/010-Yawsayadaw.mp3">၁၀။ တရားေဆာင္သူ 
စိတ္မပူ&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D25/011-Yawsayadaw.mp3">၁၁။ အသိမွန္ကန္ 
ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp;&nbsp; အင္းစိန္</a></font></p>
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
<font size="5">MP3 Disc26</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/001-Yawsayadaw.mp3">၁။ ဗုဒၶေက်းဇူး 
စြမ္းရည္ထူးမ်ား&nbsp;&nbsp;&nbsp;&nbsp; စမ္ေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/002-Yawsayadaw.mp3">၂။ အိမ္တြင္း 
မဂၢင္လူ႕က်င့္စဥ္&nbsp;&nbsp;&nbsp;&nbsp; ေတာင္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/003-Yawsayadaw.mp3">၃။ အသိမွန္ကန္ 
ကိုယ့္ဖို႕က်န္&nbsp;&nbsp;&nbsp;&nbsp; ရန္ကင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/004-Yawsayadaw.mp3">၄။ အသိးတစ္ရာ 
အညႇာတစ္ခု&nbsp;&nbsp;&nbsp;&nbsp; ေျမာက္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/005-Yawsayadaw.mp3">၅။ တရားစုေဆာင္း 
ခ်မ္းသာေၾကာင္း&nbsp;&nbsp;&nbsp; ၾကည္႕ျမင္တိုင္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/006-Yawsayadaw.mp3">၆။ တရားအသိ 
လူ႕မ်က္စိ&nbsp;&nbsp;&nbsp;&nbsp; စမ္းေခ်ာင္း</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/007-Yawsayadaw.mp3">၇။ 
ေအးျမရႊင္ၿပဳံး လူ႕ႏွလုံး&nbsp;&nbsp;&nbsp;&nbsp; မႏၱေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/008-Yawsayadaw.mp3">၈။ ဘဝေဝစု 
ျမတ္ေကာင္းမႉ&nbsp;&nbsp;&nbsp;&nbsp; ေျမာက္ဥကၠလာ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/009-Yawsayadaw.mp3">၉။ ယဥ္ေက်ူလိမၼာ 
အားကိုးရာ&nbsp;&nbsp;&nbsp; မႏၱေလး</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/010-Yawsayadaw.mp3">၁၀။ ဘဝတန္ဖိုး 
လူ႕တန္ခိုး&nbsp;&nbsp;&nbsp; လက္ပန္၊ဂန္႕ေဂါ</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/YawSayaDawGyi-SiriNanda-Bhivamsa/MP3-D26/011-Yawsayadaw.mp3">၁၁။ 
ေမတၱာကိုင္စြဲ ေအာင္ရၿမဲ&nbsp;&nbsp;&nbsp; သာေကတ</a></font></p>
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
	<p>&nbsp;</p></font></div><font face="Zawgyi-One">
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
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

count = 42
with open('titles_links.txt', 'w') as f:
    files = ['.mp4', '.wmv']
    for key in soup.find_all('a'):
        #if ''
        ext = key.get('href').split('/')[-1].split('.')[-1]
        if 'mp3' in ext:
            #print(key.get('href').split('/')[-1].split('.')[-1])
            counter = '{:03d}'.format(count)
            #print('{}.{}|{}|{}'.format(counter, ext, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            f.write('{}.{}|{}|{}\n'.format(counter, ext, ''.join(key.get('href').split()), ' '.join(key.get_text().split()) ))
            #print(key.get_text())
            
            count += 1        
    
