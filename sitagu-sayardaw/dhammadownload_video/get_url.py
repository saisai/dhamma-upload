from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">










 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 




<!-- Start dhammadownload menu top and side bar -->

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 535px; top: 6px;" id="layer23">
	<img src="images/UNyanissara.gif" width="160" height="178" border="0"></div>
	


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






	
	
<div style="position: absolute; width: 1007px; height: 18017px; z-index: 21; left: 217px; top: 153px" id="layer24" font="" face="Zawgyi-One">
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<span style="font-family: Franklin Gothic Medium; font-weight: 700">SayaDaw U Nyanissara (D.Litt)</span></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">သပိတ္အိုင္ဆရာေတာ္</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">သဲကုန္းဆရာေတာ္</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">သီတဂူဆရာေတာ္ </font>
<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">&nbsp;&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">စစ္ကိုင္းေတာင္ရုိး၊ ကမ ၻာ႔ ဗုဒၶတကၠသိုလ္ အဓိပတိ<br>
မဟာဓမၼကထိက ဗဟုဇနဟိတဓရ</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">အဂၢမဟာသဒၵမၼေဇာတိကဓဇ</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">အဂၢမဟာပ႑ိတ</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="6">သ</font><font size="6" face="Zawgyi-One">ီတဂူဆရာေတာ္ဘုရားႀကီး ဦးဥာဏိႆရ</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font face="Zawgyi-One">ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="5">သီတဂူအဓိ႒ာန္</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
ငါတို႕ျဖစ္ရ၊ ဤေလာက၀ယ္<br>
ဘ၀သမုိင္း၊ မရိုင္းေစရန္<br>
စိတ္မန္မခ်၊ မာနမပါ<br>
ဒို႕စြမ္းရာျဖင့္<br>
ဒို႕သာသနာ<br>
ဒို႕ျပည္ရြာကို<br>
သာယာေစမႈ၊ လုံ႕လျပဳအံ့။ ။<br>
<br>
ဒို႕ သီတဂူအဓိ႒ာန္မွာ မွာထားတဲ့စကားႏွစ္ရပ္ကို အားလုံးစြဲစြဲၿမဲၿမဲ မွတ္သားၿပီးေတာ့ 
ေဆာင္ရြက္ၾကဘို႕လိုတယ္။ အဲဒီထဲမွာ ”ဘ၀သမိုင္း မရိုင္းေစရန္” ဆိုတဲ့အခ်က္ပဲ။ 
မင္းတို႕တပည့္ေတြအားလုံး သာသနာေတာ္အတြက္ ကံေကာင္းလို႕လုပ္ခြင့္ရေနတာ၊ 
အဲ့ဒီလုပ္ခြင့္ရေန တာကိုက ကံေကာင္းလို႕ လုပ္ခြင့္ရေနတာ။ ဒီလုပ္ငန္းကို 
လုပ္ခြင့္ရေနတာကိုက ကံေကာင္းတဲ့အခြင့္အေရးလို႕ မွတ္သားၿပီးေတာ့ 
အဲဒီအခြင့္အေရးေတြကို အလြဲသုံးစားမလုပ္ဘို႕၊ ရထားတဲ့လုပ္ခြင့္ကို 
ထိထိေရာက္ေရာက္လုပ္ၿပီးေတာ့ အခြင့္အေရးကို မိမိရရ အရယူဘို႕၊ 
လုပ္ကိုင္ခြင့္ေပးထားတဲ့အလုပ္ကို ထိထိေရာက္ေရာက္မလုပ္ပဲ အခြင့္အေရးကို 
ရေအာင္မယူတတ္ဘူး၊ မယူႏိုင္ဘူးဆိုလို႕ရွိရင္ ဘ၀သမိုင္းဟာ ရိုင္းသြားလိမ့္မယ္။<br>
<br>
ထိထိေရာက္ေရာက္မလုပ္တဲ့အျပင္ ရထားတဲ့အခြင့္အေရးကို 
ပ်က္စီးေအာင္လုပ္လိုက္မယ္ဆိုလို႕ရွိရင္ အဲဒီသူဟာ ကိုယ့္ဘ၀သမိုင္းကို 
ကိုယ္ကိုယ္တိုင္ အရိုင္းသမိုင္းလို႕သိၿပီး ေနာင္တပူပန္ျဖစ္ရလိမ့္မယ္။ အဲ့ဒါေၾကာင့္ 
အားလုံး ဘ၀သမိုင္းမွာ မရိုင္းရေအာင္၊ သမိုင္းမွတ္တမ္း ေကာင္းေအာင္ သင္သြားဘို႕၊ 
လုပ္သြားဘို႕၊ က်င့္သြားဘို႕တိုက္တြန္းတယ္။<br>
<br>
ဘ၀သမိုင္းမရိုင္းေအာင္ ဘာလုပ္မလဲဆိုရင္ ဒို႕သာသနာ ဒို႕ျပည္ရြာကို သာယာေစမႈ 
လုံ႕လျပဳရမယ္။ တိုင္းျပည္နဲ႕သာသနာအတြက္ ေကာင္းတဲ့လုပ္ငန္းမွန္သမွ်ကို 
လုပ္ခြင့္ရသေလာက္၊ လုပ္ႏိုင္သေလာက္ အကုန္လုံးလုပ္ၾကရမယ္။ ငါ့တိုင္းျပည္နဲ႕ 
ငါ့သာသနာအတြက္ ငါ ဘာေတြလုပ္ႏိုင္သလဲ၊ ဘာေတြလုပ္ခြင့္ရသလဲ၊ အဲဒီႏွစ္ခ်က္တြက္ၿပီးေတာ့ 
အေလးအနက္ လုပ္ႏိုင္သေလာက္၊ လုပ္ခြင့္ရသေလာက္၊ ထည့္လိုက္ဦး လုပ္ျဖစ္သေလာက္ 
အကုန္လုံးလုပ္ရမယ္။ တိုင္းျပည္နဲ႕သာသနာမွာ လုပ္ခြင့္ရပါလွ်က္နဲ႕၊ 
လုပ္ႏိုင္စြမ္းရွိပါလွ်က္နဲ႕၊ လုပ္လို႕ျဖစ္ ပါလ်က္နဲ႕ မလုပ္လိုက္ရဘူးဆိုလို႕ရွိရင္ 
သိတတ္တဲ့လူတစ္ေယာက္အေနနဲ႕ ဘ၀မွာအသက္ရွည္ရင္ ရွည္သေလာက္ အဲဒီခၽြတ္ယြင္းမႈေတြနဲ႕ 
ကိုယ့္ဘ၀ကို ကုိယ္ဖ်က္ဆီးရာက်တယ္။ ကိုယ့္ဘ၀ကို ကုိယ္ဖ်က္ဆီးျခင္းဟာ 
ကိုယ့္တိုင္းျပည္နဲ႕ ကိုယ့္သာသနာကို ဖ်က္ဆီးျခင္းပဲ။ 
တိုင္းျပည္နဲ႕သာသနာကိုဖ်က္ဆီးျခင္းဟာလည္း ကိုယ့္ဘ၀ကို ဖ်က္ဆီးျခင္းပဲ။ ဘ၀ရယ္ 
တိုင္းျပည္ရယ္ သာသနာရယ္ဟာ ခြဲလို႕မရဘူး။ ဒီသုံးခုဟာ အတူတူပဲ။<br>
<br>
ခုလိုအထက္တန္းေရာက္လာတာဟာ တိုင္းျပည္နဲ႕ သာသနာက ေက်းဇူးျပဳလို႕ပဲ။ 
သီတဂူဆရာေတာ္ကေက်းဇူးျပဳလို႕ဆိုတာထက္ သာသနာကေက်းဇူးျပဳတာလို႕ ဒီလိုတြက္ရမယ္။ 
တိုင္းျပည္နဲ႕သာသနာက ဒို႕ကိုဒီေလာက္ေက်းဇူးျပဳထားရင္ ဒို႕ကလည္း ဒို႕တိုင္းျပည္နဲ႕ 
ဒို႕သာသနာေတာ္အတြက္ ျပန္ၿပီးေတာ့ေက်းဇူးျပဳရမယ္။ အဲဒီလို သုံးခု ဟန္ခ်က္ညီသြားရင္ 
ဘ၀သမိုင္းဟာ ေကာင္းသြားတာပဲ။ အဲဒါေၾကာင့္ ဘ၀သမိုင္းမရိုင္းၾကရေအာင္ရယ္၊ 
တိုင္းျပည္နဲ႕သာသနာလွပေအာင္ရယ္ ေဆာင္ရြက္ႏိုင္ၾကမယ္ဆိုရင္ ကို္ယ္ကိုယ္တိုင္လည္း 
သမိုင္း မရိုင္းဘူး။ ကိုယ့္ဘ၀လည္း လွပလာလိမ့္မယ္။ အဲဒီခံယူခ်က္နဲ႕ 
ရထားတဲ့အခြင့္အေရးေတြကို စနစ္တက် တိုင္းျပည္နဲ႕သာသနာေတာ္အတြက္ေရာ မိမိအတြက္ေရာ 
အသုံးခ်။<br>
<br>
သေဗၺာ ေလာေကာ အႆေကာ-တစ္ေလာကလုံး ကိုယ္ပိုင္ဥစၥာ ဘာမွမရွိဘူး။ သဗၺံ ပဟာယ 
ဂမနီယံ-အကုန္လုံးစြန္႕ပစ္ထားၿပီး သြားၾကရမွာပဲ။ 
အလြန္တိုေတာင္းတဲ့အခ်ိန္ကေလးအတြင္းမွာ ဒါေတြဟာ အကုန္လုံးၿပီးသြားၾကၿပီ၊ 
လြန္သြားၾကၿပီ၊ ေနာက္ျပန္လွည့္လို႕မရဘူး။ အဲဒါေၾကာင့္ 
အႏွစ္သာရနဲ႕ကိုယ္ပိုင္ဥစၥာရွာမရတဲ့ ဒိကမၻာမွာ ငါ့တိုင္းျပည္နဲ႕ ငါ့သာသနာအတြက္ 
ငါဘာထားပစ္ခဲ့မလဲ၊ ငါ့အတြက္ေကာ ဘာေတြယူသြားမလဲ၊ အဲဒီစိတ္ေတြကို အေလးအနက္ျပဳၿပီးေတာ့ 
ရထားတဲ့အခြင့္အေရး၊ ရထားတဲ့အခ်ိန္၊ ရထားတဲ့ဘ၀နဲ႕ခႏၶာကို တိုင္းျပည္ 
နဲ႕သာသနာေတာ္အတြက္ မ်ားမ်ားႀကီးအသုံးခ်ပါလို႕ဆိုတာ တိုက္တြန္းရင္း 
နိဂုံးခ်ဳပ္ပါတယ္။<br>
<br>
သီတဂူဆရာေတာ္ဘုရားႀကီး</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								**************************************************</p>

								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="5">
								<a href="https://www.facebook.com/sitagulivedhamma/?fref=ts">
								သီတဂူဆရာေတာ္ဓမၼသဘင္ - LIVE</a> မွ 
								ျပန္လည္ တင္ျပေသာ တရားေတာ္မ်ား</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">






								**************************************************</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
သီတဂူဆရာေတာ္ ဓမၼသဘင္ခရီးစဥ္"<br>
(ေရႊကူေစတီေတာ္ရင္ျပင္၊ ပခုကၠဴၿမိဳ႕)<br>
ေက်းဇူးေတာ္ရွင္ သီတဂူဆရာေတာ္ႀကီးသည္ ၃-၁၀-၂၀၁၆ ရက္ေန႔႔၊ ညခ်မ္းခ်ိန္ခါ ၇:၃၀ 
နာရီအခ်ိန္တြင္ ပခုကၠဴၿမိဳ႕၊ ဗိုလ္ခ်ဳပ္လမ္း၊ ေရႊကူေစတီေတာ္ရင္ျပင္တြင္ 
က်င္းပျပဳလုပ္ေသာ ဓမၼသဘင္ကို ေဟာၾကားေပးပါေၾကာင္း တပည့္ဒကာအေပါင္းကို 
သိရွိေစအပ္ပါသည္။<br>
တရားေတာ္နာယူလိုသူ ဓမၼမိတ္ေဆြမ်ားအေနျဖင့္ ယေန႔ည ဓမၼသဘင္ ဗီဒီယိုဖိုင္ကို 
"သီတဂူဆရာေတာ္ ဓမၼသဘင္ - LIVE" တြင္ နာယူပူေဇာ္ႏိုင္ပါသည္။<br>
==============================<br>
သီတဂူစန္းလပမာ ခ်မ္းျမသာယာ ရွိၾကပါေစ။<br>
သီတဂူသာသနာျပဳအဖြဲ႔<br>
==============================<br>
Posted by သီတဂူသတင္း<br>
ဓါတ္ပံု - သီတဂူေမာင္ေမာင္အဖြဲ႕<br>
Live Admin - သီတဂူေမာင္ေမာင္</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-17-April-2011-Myanmar-New-Year-singapore.mp4">Dhamma Talk on 17th April at Poh Ern Shih Temple</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0">
<b><font size="4" face="Zawgyi-One">
<a href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-InnSein-Prison-21-8-2010.mp4">သီတဂူဆရာေတာ္&nbsp; ဩဂုတ္လ ၂၁ ရက္ေန႔တြင္ အင္းစိန္ (ဗဟို)ေထာင္အတြင္း တရားပြဲ 
(video - wmv file)</a></font></b></p>
<p style="margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0">
<b><font size="4" face="Zawgyi-One">
<a href="http://www.dhammadownload.com/Video-Library/UNyanissara/Un-compress-video/U-Nyanissara-InnSein-Prison-21-8-2010.mpg">သီတဂူဆရာေတာ္&nbsp; ဩဂုတ္လ ၂၁ ရက္ေန႔တြင္ အင္းစိန္ (ဗဟို)ေထာင္အတြင္း တရားပြဲ 
(video - dvd quality mepg file - 3.9GB)</a></font></b></p>
<p style="margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThaTaHtarNaKhuNhitPetPhyitSinBuddaWin.mp4">သတၲဌာန ခုႏွစ္ပါတ္ျဖစ္စဥ္ ဗုဒၶ၀င္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThanWeiZaNeatYaLayHtarNa.mp4">သံေ၀ဇနိယေလး႒ာန (ဗုဒၶေန႕တရားေတာ္)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">ေလးဆူဓာတ္ပုံ ေ႐ႊတိဂုံ ေစတီေတာ္ျမတ္ႀကီး၏ ႏွစ္၂၅၀၀ 
ျဖစ္စဥ္အက်ဥ္း<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatPhaYarShweTaGone-D1.mp4">ျမတ္ဘုရားေ႐ႊတိဂုံ(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatPhaYarShweTaGone-D2.mp4">ျမတ္ဘုရားေ႐ႊတိဂုံ(၂)</a><br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MettaTaYar-3-12-2001.mp4">ေမတၲာ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">၁၃၆၃ တန္ေဆာင္မုန္း လဆုတ္ (၃) ရက္ ရန္ကုန္ၿမိဳ႕<br>
စြယ္ေတာ္ျမတ္ ေစတီေတာ္တြင္ ေဟာၾကားေတာ္မူသည္။<br>
&nbsp;</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatBuddhaThiYiYaPuZar-D1.mp4">ျမတ္ဗုဒၶသရီရပူဇာ တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatBuddhaThiYiYaPuZar-D2.mp4">ျမတ္ဗုဒၶသရီရပူဇာ တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">သာမညဆရာေတာ္ႀကီး၏ အႏၲိမစ်ာပန သာဓုကီဠန ဓမၼပူဇာသဘင္၌ 
ေဟာၾကားေတာ္မူသည္။</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">၁၀-၇-၂၀၀၀ ထိုင္၀မ္ႏုီင္ငံ။ ထိုင္ေပၿမိဳ႕တြင္ 
ေဟာၾကားေတာ္မူသည္။</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-10-7-2001-EiteTharNatMitSaYiYa(Taiwan).mp4">ဣႆာႏွင့္ မစၦရိယ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DhamaParLaSuToung-8-1-2001-d1.mp4">၈-၁-၂၀၀၁ အရွင္ဓမၼပါလဆုေတာင္း တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DhamaParLaSuToung-8-1-2001-d2.mp4">၈-၁-၂၀၀၁ အရွင္ဓမၼပါလဆုေတာင္း တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PyannaSheetParMhaPawePhyitThi-9-1-2001.mp4">၉-၁-၂၀၀၁ ပညာရွိပါမွ ပြဲျဖစ္သည္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-HtoutPyanChinNhatSwelSongChin-1-6-2001.mp4">၁-၆-၂၀၀၁ ထုတ္ျပန္ျခငး္ႏွင့္ ဆြဲေဆာင္ျခင္း တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KuMuDararTwePuintTatNya-30-11-2001-d1.mp4">၃၀-၁၁-၂၀၀၁ ကုမုျဒာေတြပြင့္တဲ့ည တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KuMuDararTwePuintTatNya-30-11-2001-d2.mp4">၃၀-၁၁-၂၀၀၁ ကုမုျဒာေတြပြင့္တဲ့ည တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThabaMangala-31-12-2001d1.mp4">၃၁-၁၂-၂၀၀၁ သဗၺမဂၤလာ တရားေတာ္(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThabaMangala-31-12-2001d2.mp4">၃၁-၁၂-၂၀၀၁ သဗၺမဂၤလာ တရားေတာ္(၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatBuddhaCheeMhongTheatKongMhout-8-1-2002-d1.mp4">၈-၁-၂၀၀၂ ျမတ္ဗုဒၶခ်ီးမြမ္းသၫ္႔ေကာင္းမႈတရားေတာ္(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatBuddhaCheeMhongTheatKongMhout-8-1-2002-d2.mp4">၈-၁-၂၀၀၂ ျမတ္ဗုဒၶခ်ီးမြမ္းသၫ္႔ေကာင္းမႈတရားေတာ္(၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MahaParateTaTaYarTaw-21-2-002.mp4">၂၁-၂-၂၀၀၂ မဟာပရိတၲ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhBeatDhamarNhatVippassana-1-11-2001-d1.mp4">၁-၁၁-၂၀၀၁ အဘိဓမၼာႏွင့္ ၀ိပႆနာ တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhBeatDhamarNhatVippassana-1-11-2001-d2.mp4">၁-၁၁-၂၀၀၁ အဘိဓမၼာႏွင့္ ၀ိပႆနာ တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KoneNaLaKayThiHtayYeeAhParDan-19-11-2002-d1.mp4">၁၉-၁၁-၂၀၀၂ ကု႑လေကသီေထရီအပါဒါန္ တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KoneNaLaKayThiHtayYeeAhParDan-19-11-2002-d2.mp4">၁၉-၁၁-၂၀၀၂ ကု႑လေကသီေထရီအပါဒါန္ တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KhuZoatTaYar-2-12-2002-d1.mp4">၂-၁၂-၂၀၀၂ ခုဇၨဳတၲရာ တရားေတာ္(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KhuZoatTaYar-2-12-2002-d2.mp4">၂-၁၂-၂၀၀၂ ခုဇၨဳတၲရာ တရားေတာ္(၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-OakTaRarWouldHtoot-1-3-2003-d1.mp4">
၁-၃-၂၀၀၃ ဥတၱရာဝတၳဳ (အမ်ိဳးသမီးေရးရာ) တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-OakTaRarWouldHtoot-1-3-2003-d2.mp4">
၁-၃-၂၀၀၃ ဥတၱရာဝတၳဳ (အမ်ိဳးသမီးေရးရာ) တရားေတာ္ (2)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThaKyarMinYaeeThawKhanDeeSarTan-23-1-2003-d1.mp4">၂၃-၁-၂၀၀၃ သိၾကားမင္းေရးေသာခႏီ ၱစာတမ္း တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThaKyarMinYaeeThawKhanDeeSarTan-23-1-2003-d2.mp4">၂၃-၁-၂၀၀၃ သိၾကားမင္းေရးေသာခႏီ ၱစာတမ္း တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhChainNateAhLoat-25-2-2003-d1.mp4">၂၅-၂-၂၀၀၃ အခ်ိန္ႏွင့္ အလုပ္ တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhChainNateAhLoat-25-2-2003-d2.mp4">၂၅-၂-၂၀၀၃ အခ်ိန္ႏွင့္ အလုပ္ တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThoutPaWarThar-27-2-2003-d1.mp4">၂၇-၂-၂၀၀၃ သုပၸ၀ါသာ တရားေတာ္(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThoutPaWarThar-27-2-2003-d2.mp4">၂၇-၂-၂၀၀၃ သုပၸ၀ါသာ တရားေတာ္(၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThiLaNatPyanNyar-20-12-2003.mp4">၂၀-၁၂-၂၀၀၃ သီလႏွင့္ပညာ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NiannavanaDhammaGoneYee-13-11-2004.mp4">၁၃-၁၁-၂၀၀၄ နိဗၺာနဓမၼဂုဏ္ရည္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-YaDaNarThoneParTanGo-20-11-2004-d1.mp4">၂၀-၁၁-၂၀၀၄ ရတနာသုံးပါးတန္ခိုး တရားေတာ္(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-YaDaNarThoneParTanGo-20-11-2004-d2.mp4">၂၀-၁၁-၂၀၀၄ ရတနာသုံးပါးတန္ခိုး တရားေတာ္(၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhTwinMeeAhPyinMee-18-10-2004.mp4">၁၈-၁၀-၂၀၀၄ အတြင္းမီး အျပင္မီး တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KaYoutNarBarWaNar-11-1-2005.mp4">၁၁-၁-၂၀၀၅ ကရုဏာဘာ၀နာ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TharThaNarTawKyeePhourKoungTaYar7Par-16-2-2005-d1.mp4">၁၆-၂-၂၀၀၅ သာသနာေတာ္ႀကီးပြားေၾကာင္း တရား(၇)ပါး တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TharThaNarTawKyeePhourKoungTaYar7Par-16-2-2005-d2.mp4">၁၆-၂-၂၀၀၅ သာသနာေတာ္ႀကီးပြားေၾကာင္း တရား(၇)ပါး တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NayeSinThone-8-4-2005.mp4">၈-၄-၂၀၀၅ ေန႕စဥ္သုံး တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KanKaungThuMyar-17-10-2005.mp4">၁၇-၁၀-၂၀၀၅ ကံေကာင္းသူမ်ား တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BaWaKongKaungLayPar-13-11-2005.mp4">၁၃-၁၁-၂၀၀၅ ဘ၀ေကာင္းေၾကာင္း ေလးပါး တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhShoakAhShin-26-4-2005.mp4">၂၆-၄-၂၀၀၅ အရႈပ္ အရွင္း တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhaTharThaTawPyantPourYae-24-12-2004.mp4">၂၄-၁၂-၂၀၀၄ ဗုဒၶသာသနာေတာ္ျပန္႕ပြားေရး တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhaTaYarTawNhitKabaNyainChanYae(1)-6-1-2005.mp4">၆-၁-၂၀၀၅ ဗုဒၶတရားေတာ္ႏွင့္ ကမၻာ့ ၿငိမ္ခ်မ္းေရး တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhaTaYarTawNhitKabaNyainChanYae(2)-6-1-2005.mp4">၆-၁-၂၀၀၅ ဗုဒၶတရားေတာ္ႏွင့္ ကမၻာ့ ၿငိမ္ခ်မ္းေရး တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatMhoutKhitKaBaAhChayNayNhitBuddhaTaYarTaw-2004.mp4">၂၀၀၅ မ်က္ေမွာက္ေခတ္ ကမၻာ့အေျခအေနႏွင့္ ဗုဒၶတရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThawTarPanThanGaYaTaNarGoneYe-16-2-2006.mp4">၁၆-၂-၂၀၀၆ ေသာတာပန္ သံဃာ့ ရတနာ ဂုဏ္ရည္ တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-OweKwairYaeLongMaPhyitSaeNhit-D1-30-11-2006.mp4">၃-၁၁-၂၀၀၆ အိုးကြဲေရေလာင္း မျဖစ္ေစနဲ႕(၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-OweKwairYaeLongMaPhyitSaeNhit-D2-30-11-2006.mp4">၃-၁၁-၂၀၀၆ အိုးကြဲေရေလာင္း မျဖစ္ေစနဲ႕(၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-LuMikeToatEiThoarYarLan-D1-13-10-2007.mp4">၁၃-၁၀-၂၀၀၇ လူမိုက္တို႕၏ သြားရာလမ္း (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-LuMikeToatEiThoarYarLan-D2-13-10-2007.mp4">၁၃-၁၀-၂၀၀၇ လူမိုက္တို႕၏ သြားရာလမ္း (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AyeKaRickMinGyiEiBaWaNeatGone-D1-30-10-2007.mp4">၃၀-၁၀-၂၀၀၇ ဧကရာဇ္ မင္းႀကီး၏ ဘ၀နိဂုံုး (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AyeKaRickMinGyiEiBaWaNeatGone-D2-30-10-2007.mp4">၃၀-၁၀-၂၀၀၇ ဧကရာဇ္ မင္းႀကီး၏ ဘ၀နိဂုံုး (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BawaSiMeeTing-D1-2-11-2007.mp4">၂-၁၁-၂၀၀၇ ဘ၀ဆီမီးတိုင္ တရားေတာ္ (၁) မႏၲေလးၿမိဳ႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BawaSiMeeTing-D2-2-11-2007.mp4">၂-၁၁-၂၀၀၇ ဘ၀ဆီမီးတိုင္ တရားေတာ္ (၂) မႏၲေလးၿမိဳ႕</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-HtanPinNgout-4-11-2007-D01.mp4">၄-၁၁-၂၀၀၇ ထန္းပင္ငုတ္တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-HtanPinNgout-4-11-2007-D02.mp4">၄-၁၁-၂၀၀၇ ထန္းပင္ငုတ္တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NaKaungThuKaungMahope-5-11-2007.mp4">၅-၁၁-၂၀၀၇ ငါ့ေၾကာင့္မဟုတ္၊ သူ႕ေၾကင့္မဟုတ္ တရားေတာ္ ထန္းတပင္ၿမိဳ႕ 
</a> </font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NayNyeeThonePar-D1-21-10-2007.mp4">၂၁-၁၀-၂၀၀၇ ေနနည္းသုံးပါး တရားေတာ္ (၁)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NayNyeeThonePar-D2-21-10-2007.mp4">၂၁-၁၀-၂၀၀၇ ေနနည္းသုံးပါး တရားေတာ္ (၂)</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThetTaWarTwaiKoBairThuPhanSinHtarThaLair-22-12-2007.mp4">၂၂-၁၂-၂၀၀၇ သတၲ၀ါေတြကို ဘယ္သူဖန္ဆင္းထားသလဲ
</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4">****dhamma talks uploaded and published on 5 August 2009****</font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KanKaungThuMyar-17-10-2005.mp4">၁၇-၁၀-၂၀၀၅ ကံေကာင္းသူမ်ား တရားေတာ္</a></font></p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top: 0; margin-bottom: 0">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhaEthicAndSocialWork-12-8-2008-D01.mp4">၁၂-၈-၂၀၀၈ ဗုဒၶဘာသာသာက်င့္ထုံးႏွင့္ လူမႈေရးလုပ္ငန္မ်ား အမွတ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhaEthicAndSocialWork-12-8-2008-D02.mp4">၁၂-၈-၂၀၀၈ ဗုဒၶဘာသာသာက်င့္ထုံးႏွင့္ လူမႈေရးလုပ္ငန္မ်ား အမွတ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhaEthicAndSocialWork-12-8-2008-D03.mp4">၁၂-၈-၂၀၀၈ ဗုဒၶဘာသာသာက်င့္ထုံးႏွင့္ လူမႈေရးလုပ္ငန္မ်ား အမွတ္ (၃)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KawThaLaYaikSawYaGyiTawe-10-12-2007-D01.mp4">၁၀-၁၂-၂၀၀၇ ေကာသလရဲ႕ေစာရႀကီးေတြ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KawThaLaYaikSawYaGyiTawe-10-12-2007-D02.mp4">၁၀-၁၂-၂၀၀၇ ေကာသလရဲ႕ေစာရႀကီးေတြ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-EuPaZaLarPyawThawLawKaThaBaw-1-11-2007-D01.mp4">၁-၁၁-၂၀၀၇ ဥပစာလာေျပာေသာ ေလာကသေဘာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-EuPaZaLarPyawThawLawKaThaBaw-1-11-2007-D02.mp4">၁-၁၁-၂၀၀၇ ဥပစာလာေျပာေသာ ေလာကသေဘာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NaLanDar-9-11-2008-D01.mp4">၉-၁၁-၂၀၀၈ နာလႏၵ အမွတ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NaLanDar-9-11-2008-D02.mp4">၉-၁၁-၂၀၀၈ နာလႏၵ အမွတ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhKateTiZat-22-4-2007-D01.mp4">၂၂-၄-၂၀၀၇ အကိတၱိဇာတ္ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhKateTiZat-22-4-2007-D02.mp4">၂၂-၄-၂၀၀၇ အကိတၱိဇာတ္ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ShweOhMyout-17-1-2005-D01.mp4">၁၇-၁-၂၀၀၅ ေရႊအိုးျမဳပ္ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ShweOhMyout-17-1-2005-D02.mp4">၁၇-၁-၂၀၀၅ ေရႊအိုးျမဳပ္ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThanWaiGaKaHtarDayThaNar-17-10-2008-D01.mp4">၁၇-၁၀-၂၀၀၈ သံေဝဂကထာေဒသနာေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThanWaiGaKaHtarDayThaNar-17-10-2008-D02.mp4">၁၇-၁၀-၂၀၀၈ သံေဝဂကထာေဒသနာေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KyaukSeinLatKauk-1-12-2008-D01.mp4">၁-၁၂-၂၀၀၈ ေက်ာက္စိမ္းလက္ေကာက္ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KyaukSeinLatKauk-1-12-2008-D02.mp4">၁-၁၂-၂၀၀၈ ေက်ာက္စိမ္းလက္ေကာက္ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-EuPatKhar-4-9-2008-D01.mp4">၄-၉-၂၀၀၈ ဥေပကၡာတရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-EuPatKhar-4-9-2008-D02.mp4">၄-၉-၂၀၀၈ ဥေပကၡာတရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NyiNyoutChinEatKyaeZoo-20-12-2006.mp4">၂၀-၁၂-၂၀၀၆ ညီညြတ္ခ်င္း၏ေက်းဇူး</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TaKhuThawLan-21-7-2008-D01.mp4">၂၁-၇-၂၀၀၈ တစ္ခုေသာလမ္း (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TaKhuThawLan-21-7-2008-D02.mp4">၂၁-၇-၂၀၀၈ တစ္ခုေသာလမ္း (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MettaWaiMhaAyeLakeMael-21-10-2008-D01.mp4">၂၁-၁၀-၂၀၀၈ ေမတၱာေဝမွ ေအးလိမ့္မယ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MettaWaiMhaAyeLakeMael-21-10-2008-D02.mp4">၂၁-၁၀-၂၀၀၈ ေမတၱာေဝမွ ေအးလိမ့္မယ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-HtanPinNgoak-D1-4-11-2007.mp4">၄-၁၁-၂၀၀၇ ထန္းပင္ငုပ္တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-HtanPinNgoak-D2-4-11-2007.mp4">၄-၁၁-၂၀၀၇ ထန္းပင္ငုပ္တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThuTawKaungLatKhaNarThonePar-3-1-2008-D01.mp4">၃-၁-၂၀၀၈ သူေတာ္ေကာင္းလကၡဏာ(၃)ပါး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThuTawKaungLatKhaNarThonePar-3-1-2008-D02.mp4">၃-၁-၂၀၀၈ သူေတာ္ေကာင္းလကၡဏာ(၃)ပါး (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DoteKhaEiLookMyoutYar-4-1-2008-D01.mp4">၄-၁-၂၀၀၈ ဒုကၡ၏လြတ္ေျမာက္ရာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DoteKhaEiLookMyoutYar-4-1-2008-D02.mp4">၄-၁-၂၀၀၈ ဒုကၡ၏လြတ္ေျမာက္ရာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PhoneKanKyeeThuMyar-17-4-2008-D01.mp4">၁၇-၄-၂၀၀၈ ဘုန္းကံႀကီးသူမ်ား (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PhoneKanKyeeThuMyar-17-4-2008-D02.mp4">၁၇-၄-၂၀၀၈ ဘုန္းကံႀကီးသူမ်ား (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NatPyiYorkKaungMhoot-13-3-2008-D01.mp4">၁၃-၃-၂၀၀၈ နတ္ျပည္ေရာက္ေၾကာင္း ေကာင္းမႈ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NatPyiYorkKaungMhoot-13-3-2008-D02.mp4">၁၃-၃-၂၀၀၈ နတ္ျပည္ေရာက္ေၾကာင္း ေကာင္းမႈ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThiHaTayar-30-3-2008-D01.mp4">၃၀-၃-၂၀၀၈ သီဟ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThiHaTayar-30-3-2008-D02.mp4">၃၀-၃-၂၀၀၈ သီဟ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThuKhaLayPar-19-7-2008-D01.mp4">၁၉-၇-၂၀၀၈ သုခေလးပါးတရားေတာ္ (ေရႊျပည္မိုး) (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThuKhaLayPar-19-7-2008-D02.mp4">၁၉-၇-၂၀၀၈ သုခေလးပါးတရားေတာ္ (ေရႊျပည္မိုး) (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KaungAhHlu-13-11-2008-D01.mp4">၁၃-၁၁-၂၀၀၈ ေက်ာင္းအလႉတရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KaungAhHlu-13-11-2008-D02.mp4">၁၃-၁၁-၂၀၀၈ ေက်ာင္းအလႉတရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ChanTharLayPar-17-6-2008-D01.mp4">၁၇-၆-၂၀၀၈ ခ်မ္းသာေလးပါး တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ChanTharLayPar-17-6-2008-D02.mp4">၁၇-၆-၂၀၀၈ ခ်မ္းသာေလးပါး တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhKanKaBarMhaThitSarMyatLone-3-10-2008-D01.mp4">၃-၁၀-၂၀၀၈ အကန္းကမ ၻာမွ သစၥာမ်က္လုံး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NyietKatChinHteetKatChinMhaShaungKyinYaMyee-9-11-2008-D01.mp4">၉-၁၁-၂၀၀၈ ၿငိကပ္ျခင္း၊ ထိကပ္ျခင္းမွ ေရွာင္ၾကဥ္ရမည္ (၁)</a> </font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NyietKatChinHteetKatChinMhaShaungKyinYaMyee-9-11-2008-D02.mp4">၉-၁၁-၂၀၀၈ ၿငိကပ္ျခင္း၊ ထိကပ္ျခင္းမွ ေရွာင္ၾကဥ္ရမည္ (၂)</a> </font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatSwarPhaYarNoutSoneMharKyarThawSaKarChoutKhon-29-9-2006-D01.mp4">၂၉-၉-၂၀၀၆ ျမတ္စြာဘုရား ေနာက္ဆုံးမိန္႕ၾကားခဲ့ေသာ စကား(၆)ခြန္း (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatSwarPhaYarNoutSoneMharKyarThawSaKarChoutKhon-29-9-2006-D02.mp4">၂၉-၉-၂၀၀၆ ျမတ္စြာဘုရား ေနာက္ဆုံးမိန္႕ၾကားခဲ့ေသာ စကား(၆)ခြန္း (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-GaYuNarTayar-15-7-2008-D01.mp4">၁၅-၇-၂၀၀၈ ကရုဏာတရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-GaYuNarTayar-15-7-2008-D02.mp4">၁၅-၇-၂၀၀၈ ကရုဏာတရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-7-9-2006-D01.mp4">၇-၉-၂၀၀၆ ပက္ရွ္ဝါရ္မွသည္ မႏ ၱေလးသို႕ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-7-9-2006-D02.mp4">၇-၉-၂၀၀၆ ပက္ရွ္ဝါရ္မွသည္ မႏ ၱေလးသို႕ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-EinTawYarGaYouthNar-17-7-2008-D01.mp4">၁၇-၇-၂၀၀၈ အိမ္ေတာ္ရာကရုဏာ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-EinTawYarGaYouthNar-17-7-2008-D02.mp4">၁၇-၇-၂၀၀၈ အိမ္ေတာ္ရာကရုဏာ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PhwintPhyoToeTetMhootNharMyo-9-12-2007-D01.mp4">၉-၁၂-၂၀၀၇ ဖြံ ႔ၿဖိဳးတိုးတက္မႈ(၅)မ်ိဳး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PhwintPhyoToeTetMhootNharMyo-9-12-2007-D02.mp4">၉-၁၂-၂၀၀၇ ဖြံ ႔ၿဖိဳးတိုးတက္မႈ(၅)မ်ိဳး (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AungTawMu-18-7-2008-D1.mp4">၁၈-၇-၂၀၀၈ ေအာင္ေတာ္မူ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AungTawMu-18-7-2008-D2.mp4">၁၈-၇-၂၀၀၈ ေအာင္ေတာ္မူ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KawThaLaMinGyiiAhPaMarDa-19-3-2008-D01.mp4">၁၉-၃-၂၀၀၈ ေကာသလမင္းႀကီး၏ အပၸမာဒ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KawThaLaMinGyiiAhPaMarDa-19-3-2008-D02.mp4">၁၉-၃-၂၀၀၈ ေကာသလမင္းႀကီး၏ အပၸမာဒ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhKaungSheatLoatPhyitTar-8-1-2008-D01.mp4">၈-၁-၂၀၀၇ အေၾကာင္းရွိလို႕ျဖစ္တာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhKaungSheatLoatPhyitTar-8-1-2008-D02.mp4">၈-၁-၂၀၀၇ အေၾကာင္းရွိလို႕ျဖစ္တာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TaYarAhKyinChok-8-12-2007-D01.mp4">၈-၁၂-၂၀၀၇ တရားအက်ဥ္းခ်ဳပ္ေလးပါး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TaYarAhKyinChok-8-12-2007-D02.mp4">၈-၁၂-၂၀၀၇ တရားအက်ဥ္းခ်ဳပ္ေလးပါး (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">****dhamma talks uploaded and published on 26 October 2009****</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DoteKhaKaBarAtTaweLoAtChat-d1-7-1-2008.mp4">၇-၁-၂၀၀၈ ဒုကၡကမၻာအတြက္လိုအပ္ခ်က္ ကရုဏာဘာဝနာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DoteKhaKaBarAtTaweLoAtChat-d2-7-1-2008.mp4">၇-၁-၂၀၀၈ ဒုကၡကမၻာအတြက္လိုအပ္ခ်က္ ကရုဏာဘာဝနာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatBuddhaCheeMhongTheatKongMhout-8-1-2002-d1.mp4">၈-၁-၂၀၀၂ ျမတ္ဗုဒၶခ်ီးမြမ္းသည္႕ေကာင္းမႈတရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MyatBuddhaCheeMhongTheatKongMhout-8-1-2002-d2.mp4">၈-၁-၂၀၀၂ ျမတ္ဗုဒၶခ်ီးမြမ္းသည္႕ေကာင္းမႈတရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NiannavanaDhammaGoneYee-13-11-2004.mp4">၁၃-၁၁-၂၀၀၄&nbsp; နိဗၺာန ဓမၼဂုဏ္ရည္ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NyainChanYaeNhitBawaTaughtPaungYaee-5-8-2008.mp4">၅-၈-၂၀၀၈ ၿငိမ္းခ်မ္းေရးႏွင့္ ဘဝေတာက္ေျပာင္ေရး တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MettaNhitPyannaYaeLoKyintPar-d1-11-9-2008.mp4">၁၁-၉-၂၀၀၈ ေမတၱာႏွင့္ပညာ (ေရလိုက်င့္ပါ) တရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-MettaNhitPyannaYaeLoKyintPar-d2-11-9-2008.mp4">၁၁-၉-၂၀၀၈ ေမတၱာႏွင့္ပညာ (ေရလိုက်င့္ပါ) တရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-LakeKaLayLoNay-17-9-2007.mp4">၁၇-၉-၂၀၀၇ ကုမၼဴပမာ (လိပ္ကေလးလိုေန) တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KoKyaintTayarThiSinYeTharToatEiAhYinAhNhee-9-2-2005.mp4">၉-၂-၂၀၀၅ ကိုယ္က်င့္တရားသည္ဆင္းရဲသားတို႕၏အရင္းအႏွီး Character is the poor man 
capital</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KhanDeMyayGyiLoKyintPar-d1-12-1-2009.mp4">၁၂-၁-၂၀၀၉ ခႏီ ၱ ေျမႀကီးလိုက်င့္ပါ တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KhanDeMyayGyiLoKyintPar-d2-12-1-2009.mp4">၁၂-၁-၂၀၀၉ ခႏီ ၱ ေျမႀကီးလိုက်င့္ပါ တရားေတာ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KanSHarThawNaik-6-12-2008.mp4">၆-၁၂-၂၀၀၈&nbsp; ကမ္းရွာေသာဌက္ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BuddhistConversion.mp4">&nbsp; 
Buddhist Conversion</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PhoneKanKyeeThuToatEiTharThaNar-d1-17-11-2005.mp4">၁၇-၁၁-၂၀၀၅ ဘုန္းကံႀကီးသူတို႕၏ သာသနာ တရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PhoneKanKyeeThuToatEiTharThaNar-d2-17-11-2005.mp4">၁၇-၁၁-၂၀၀၅ ဘုန္းကံႀကီးသူတို႕၏ သာသနာ တရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KhanDiParMe-20-11-2008.mp4">၂၀-၁၁-၂၀၀၈&nbsp; ခႏီ ၱပါရမီ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-AhThuYarTikePwe.mp4">အသူရာတိုက္ပြဲ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-KoePineNetKoeSarKyat-4-11-2006.mp4">၄-၁၁-၂၀၀၆ ကိုယ့္ပိုင္နက္ ကိုယ့္စားက်က္ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-NyanMyatSeatSheatKyaSanPar-20-1-2008.mp4">၂၀-၁-၂၀၀၈ ဥာဏ္မ်က္စိ ရွိၾကစမ္းပါ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-SuTaungPaungLikePar-11-11-2007.mp4">၁၁-၁၁-၂၀၀၇ ဆုေတာင္းေျပာင္းလိုက္ပါ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BarLaPandita-12-1-2008-d1.mp4">၁၂-၁-၂၀၀၈ ဗာလပ႑ိတမိတ္ဆက္ တရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-BarLaPandita-12-1-2008-d2.mp4">၁၂-၁-၂၀၀၈ ဗာလပ႑ိတမိတ္ဆက္ တရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-OopPaSarYeePyawThawLawKaThaBal4Myo-d1-22-9-2007.mp4">၂၂-၉-၂၀၀၇ ဥပစာလာေျပာေသာ ေလာကသေဘာ (၄) မ်ိဳး တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-OopPaSarYeePyawThawLawKaThaBal4Myo-d2-22-9-2007.mp4">၂၂-၉-၂၀၀၇ ဥပစာလာေျပာေသာ ေလာကသေဘာ (၄) မ်ိဳး တရားေတာ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TharThaNarKyeePawrKaungTaYarLayPar-d1-10-1-2008.mp4">၁၀-၁-၂၀၀၈ သာသနာႀကီးပြားေၾကာင္းတရား(၄)ပါးတရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-TharThaNarKyeePawrKaungTaYarLayPar-d2-10-1-2008.mp4">၁၀-၁-၂၀၀၈ သာသနာႀကီးပြားေၾကာင္းတရား(၄)ပါးတရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-YaeNhitToooAungKyintKyaPar-d1-7-11-2008.mp4">၇-၁၁-၂၀၀၈ ေရႏွင့္တူေအာင္က်င့္ၾကပါတရားေတာ္(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-YaeNhitToooAungKyintKyaPar-d2-7-11-2008.mp4">၇-၁၁-၂၀၀၈ ေရႏွင့္တူေအာင္က်င့္ၾကပါတရားေတာ္(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-ThinKyarChinNhitThinYouChin-13-10-2008.mp4">၁၃-၁၀-၂၀၀၈ သင္ၾကားျခင္းႏွင့္သင္ယူျခင္းတရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-DoteKhaYorkThuMyarKoSoutShoutChin-13-11-2008.mp4">၁၃-၁၁-၂၀၀၈ ဒုကၡေရာက္သူမ်ားကိုေစာင့္ေရွာက္ျခင္းတရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4" face="Zawgyi-One">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-PanTeatKaLatKhaNa-11-1-2008.mp4">၁၁-၁-၂၀၀၈ ပႏၱိကလကၡဏ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">****dhamma talks uploaded and published on 6 Sept 2010****</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">DVD-16</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/001-UNyanissara-Ma-Mae-At-te'-Lay-Htar-Na-A.mp4">၁။ မေမ့အပ္တဲ့ ေလးဌာန (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/002-UNyanissara-Ma-Mae-At-te'-Lay-Htar-Na-B.mp4">၂။ မေမ့အပ္တဲ့ ေလးဌာန (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/003-UNyanissara-A-Myat-Sone-Aote-Sar-A.mp4">၃။ လူ႕ေလာကတစ္ခုလုံး အျမတ္ဆုံးဥစၥာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/004-UNyanissara-A-Myat-Sone-Aote-Sar-B.mp4">၄။ လူ႕ေလာကတစ္ခုလုံး အျမတ္ဆုံးဥစၥာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/005-UNyanissara-Thar-Du-4-Par-A.mp4">၅။ သာဓု ေလးပါး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/006-UNyanissara-Thar-Du-4-Par-B.mp4">၆။ သာဓု ေလးပါး (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/007-UNyanissara-yout-thar-aoe-yway-pyin-nyar-ma-oo-A.mp4">၇။ ရုပ္သာအို၍ ဉာဏ္ပညာမအို (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/008-UNyanissara-yout-thar-aoe-yway-pyin-nyar-ma-oo-B.mp4">၈။ ရုပ္သာအို၍ ဉာဏ္ပညာမအို (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/009-UNyanissara-Myat-Buddha-Chee-Myint-The-UNyanissara-Kaung-Mu-A.mp4">၉။ ျမတ္ဗုဒၶ ခ်ီးမြမ္းသည္႕ ေကာင္းမႈ(၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/010-UNyanissara-Myat-Buddha-Chee-Myint-The-UNyanissara-Kaung-Mu-B.mp4">၁၀။ ျမတ္ဗုဒၶ ခ်ီးမြမ္းသည္႕ ေကာင္းမႈ(၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/011-UNyanissara-A-Chain-and-A-Lote-A.mp4">၁၁။ အခ်ိန္ႏွင့္ အလုပ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/012-UNyanissara-A-Chain-and-A-Lote-B.mp4">၁၂။ အခ်ိန္ႏွင့္ အလုပ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/013-UNyanissara-Dar-Na-Ka-Htar-A.mp4">၁၃။ ေစတီယပူဇာ ကာကြယ္ျခင္း (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/014-UNyanissara-Dar-Na-Ka-Htar-B.mp4">၁၄။ ေစတီယပူဇာ ကာကြယ္ျခင္း (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/015-UNyanissara-A-Kyaung-Shi-Lol-Pyit-Tar-A.mp4">၁၅။ အေၾကာင္းရွိလို႕ ျဖစ္တာပါ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-16/016-UNyanissara-A-Kyaung-Shi-Lol-Pyit-Tar-B.mp4">၁၆။ အေၾကာင္းရွိလို႕ ျဖစ္တာပါ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">DVD-17</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/001-UNyanissara-Tite-Pwel-and-Aung-Pwel.mp4">၁။ တိုက္ပြဲႏွင့္ ေအာင္ပြဲ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/002-UNyanissara-Byat-Ta-Na-5-A.mp4">၂။ ဗ်ႆနတရား ငါးပါး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/003-UNyanissara-Byat-Ta-Na-5-B.mp4">၃။ ဗ်ႆနတရား ငါးပါး (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/004-UNyanissara-Ma-Har-Ta-Ma-Ya-A.mp4">၄။ မဟာသမယသုတ္ အႏွစ္ခ်ဳပ္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/005-UNyanissara-Ma-Har-ta-ma-ya-B.mp4">၅။ မဟာသမယသုတ္ အႏွစ္ခ်ဳပ္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/006-UNyanissara-Bote-Da-Ei-Ya-Ta-Nar-A.mp4">၆။ ဗုဒၶ၏ ရတနာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/007-UNyanissara-Bote-Da-Ei-Ya-Ta-Nar-B.mp4">၇။ ဗုဒၶ၏ ရတနာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/008-UNyanissara-Da-Ma-Par-La-Su-Taung-A.mp4">၈။ ဓမၼပါလဆုေတာင္း (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/009-UNyanissara-Da-Ma-Par-La-Su-Taung-B.mp4">၉။ ဓမၼပါလဆုေတာင္း (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/010-UNyanissara-Ba-Wa-Tan-Boe-A-Ya-Yu.mp4">၁၀။ ဘဝတန္ဖိုး အရယူ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/011-UNyanissara-Aye-Yar-Wai-De-A.mp4">၁၁။ ဧရာဝတီမွာ ရြာတဲ့ရတနာမိုး (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/012-UNyanissara-Aye-Yar-Wai-De-b.mp4">၁၂။ ဧရာဝတီမွာ ရြာတဲ့ရတနာမိုး (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/013-UNyanissara-Dama-Sat-Kyar-A.mp4">၁၃။ ဓမၼစႀကၤာ မိတ္ဆက္ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/014-UNyanissara-Dama-Sat-Kyar-b.mp4">၁၄။ ဓမၼစႀကၤာ မိတ္ဆက္ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/015-UNyanissara-Kyi-Kyal-Myint-Myat-A.mp4">၁၅။ ႀကီးက်ယ္ျမင့္ျမတ္ မဟာသမယ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-17/016-UNyanissara-Kyi-Kyal-Myint-Myat-B.mp4">၁၆။ ႀကီးက်ယ္ျမင့္ျမတ္ မဟာသမယ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">DVD-18</font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/001-UNyanissara-A-Shi-Ta-Yar-A-Man-Ta-Yar.mp4">၁။ အရွိတရားႏွင့္ အမွန္တရား</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/002-UNyanissara-Mit-Tar-Swan-Yae-A.mp4">၂။ ေမတၱာစြမ္းရည္ (၁) ဗုဒၶတကၠသိုလ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/003-UNyanissara-Mit-Tar-Swan-Yae-B.mp4">၃။ ေမတၱာစြမ္းရည္ (၂) ဗုဒၶတကၠသိုလ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/004-UNyanissara-Myit-Zwi-Ma-Pa-Di-Pa-Dar.mp4">၄။ မဇၥ်ိမ ပဋိပဒါ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/005-UNyanissara-Bote-Da-Ei-Nout-sone-Sa-Kar-A.mp4">၅။ ဗုဒၶ၏ ေနာက္ဆုံးစကား (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/006-UNyanissara-Bote-Da-Ei-Nout-sone-Sa-Kar-B.mp4">၆။ ဗုဒၶ၏ ေနာက္ဆုံးစကား (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/007-UNyanissara-A-Mway-Pay-A-Mway-Yu.mp4">၇။ အေမြေပး၊ အေမြယူ</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/008-UNyanissara-Sate-Pyin-Nee-A.mp4">၈။ စိတ္ကိုျပင္မွ ခ်မ္းသာရ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/009-UNyanissara-Sate-Pyin-Nee-B.mp4">၉။ စိတ္ကိုျပင္မွ ခ်မ္းသာရ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/010-UNyanissara-Ta-Ti-Pa-Htar-Na-Thote.mp4">၁၀။ သတိပဌာနသုတ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/011-UNyanissara-That-Ba-Min-Ga-Lar-A.mp4">၁၁။ သဗၺမဂၤလာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/012-UNyanissara-That-Ba-Min-Ga-Lar-B.mp4">၁၂။ သဗၺမဂၤလာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/013-UNyanissara-Nit-Thit-Min-Ga-Lar-A.mp4">၁၃။ ႏွစ္သစ္မဂၤလာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/014-UNyanissara-Nit-Thit-Min-Ga-Lar-B.mp4">၁၄။ ႏွစ္သစ္မဂၤလာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/015-UNyanissara-Kote-Zote-Ta-Yar-A.mp4">၁၅။ ခုဇၨဳတၱရာ (၁)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/old/DVD-18/016-UNyanissara-Kote-Zote-Ta-Yar-B.mp4">၁၆။ ခုဇၨဳတၱရာ (၂)</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">
<a href="http://dhammadownload.com/MP4Library/UNyanissara/old/UNyanissara-InnSein-Prison-21-8-2010.mp4">၂၀၁၀ဩဂုတ္လ ၂၁ ရက္ေန႔တြင္ အင္းစိန္ (ဗဟို)ေထာင္အတြင္း ေဟာၾကားေတာ္မူေသာ တရားေတာ္</a></font></p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">****dhamma talks uploaded and 
								published on 20 Nov 2011****</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>








<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 01</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/01-UNyanissara-DVD01-thay-ra-war-da.mp4">
								၁။&nbsp; ေထရဝါဒမိတ္ဆက္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/02-UNyanissara-DVD01-u-pa-sar-ra-thay-ri.mp4">
								၂။ ဥပစာလာေထရီ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/03-UNyanissara-DVD01-a-thu-yar-taik-pwal.mp4">
								၃။ အသူရာတိုက္ပြဲ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/04-UNyanissara-DVD01-that-teet.mp4">
								၄။ သတၱိ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/05-UNyanissara-DVD01-lake-nhit-tu-aung-nay.mp4">
								၅။ လိပ္ႏွင့္တူေအာင္ေနပါ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/06-UNyanissara-DVD01-kar-ya-kan.mp4">
								၆။ ကရုဏာျဖင့္ ကာယကံေျမာက္ျပဳလုပ္ျခင္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/07-UNyanissara-DVD01-nyaine-chan.mp4">
								၇။ ၿငိမ္းခ်မ္းေရးႏွင့္ဘဝ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/08-UNyanissara-DVD01-bot-da-day.mp4">
								၈။ သံေဝဇနိယေလးဌာန</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/09-UNyanissara-DVD01-pyin-nyar-sheet.mp4">
								၉။ ပညာရွိပါမွ ပြဲျဖစ္သည္။</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/10-UNyanissara-DVD01-myitter.mp4">
								၁၀။ ေမတၱာတရား</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/11-UNyanissara-DVD01-nyi-nyout.mp4">
								၁၁။ ညီညြတ္စြာက်င့္ျခင္း၏ခ်မ္းသာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/12-UNyanissara-DVD01-nhit-haung-nhit-thit.mp4">
								၁၂။ ႏွစ္ေဟာင္းႏွစ္သစ္ သုံးသပ္ခ်က္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/13-UNyanissara-DVD01-a-yar-waddy.mp4">
								၁၃။ ဧရာဝတီအတြက္ ကရုဏာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/14-UNyanissara-DVD01-kan-kaung-thu-myar.mp4">
								၁၄။ ကံေကာင္းသူမ်ား</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-01/15-UNyanissara-DVD01-sate-pyin-nee.mp4">
								၁၅။ စိတ္ျပင္နည္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 02</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/01-UNyanissara-DVD02-naing-gan.mp4">၁။ ႏိုင္ငံပိုင္ ရတနာမ်ား ထိမ္းသိမ္းေရး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/02-UNyanissara-DVD02-thin-kyar-thin-you.mp4">
								၂။ သင္ၾကားျခင္းႏွင့္ သင္ယူျခင္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/03-UNyanissara-DVD02-bot-da-note-ta-tee.mp4">
								၃။ ဗုဒၶႏုႆတိဘာဝနာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/04-UNyanissara-DVD02-ko-kyint.mp4">
								၄။ ကိုယ္က်င့္သိကၡာသည္ ဆင္းရဲသားတို႕၏ အရင္းအႏွီး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/05-UNyanissara-DVD02-that-ta-war.mp4">
								၅။ သတၱဝါေတြကို ဘယ္သူဖန္တီးထားသလဲ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/06-UNyanissara-DVD02-a-tway-a-kyan.mp4">
								၆။ အေတြးအႀကံမွန္မွ ဆုံးျဖတ္ခ်က္မွန္မည္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/07-UNyanissara-DVD02-a-chain-mha-a-chain.mp4">
								၇။ အခ်ိန္မွ အခ်ိန္စားျခင္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/08-UNyanissara-DVD02-than-ga-gon-yi.mp4">
								၈။ သံဃာ့ဂုဏ္ရည္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/09-UNyanissara-DVD02-ko-paing-net.mp4">
								၉။ ကိုယ့္ပိုင္နက္ ကိုယ္စားက်က္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/10-UNyanissara-DVD02-nate-van-na-gon-yi.mp4">
								၁၀။ နိဗၺာန ဓမၼဂုဏ္ရည္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/11-UNyanissara-DVD02-that-ta-thar-na.mp4">
								၁၁။ သတၱဌာန</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/12-UNyanissara-DVD02-thu-kyaung-ma-hope.mp4">
								၁၂။ သူ႕ေၾကာင့္မဟုတ္ ငါ့ေၾကာင့္ မဟုတ္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/13-UNyanissara-DVD02-buddhist-conversion.mp4">
								၁၃။&nbsp; Buddhist Conversion</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/14-UNyanissara-DVD02-khan-tee.mp4">
								၁၄။ ခႏီ ၱပါရမီ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-02/15-UNyanissara-DVD02.mp4">၁၅။ ကမ္းရွာေသာ ဌက္</a></font></p>
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
								<font size="4">DVD 03</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/01-UNyanissara-DVD03-bawa-s-m-t-1.mp4">
								၁။ ဘဝဆီမီးတိုင္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/02-UNyanissara-DVD03-bawa-s-m-t-2.mp4">
								၂။ ဘဝဆီမီးတိုင္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/04-UNyanissara-DVD03-thit-sar-2.mp4">
								၃။ သစၥာတရား လက္ကိုင္ထား ဘဝခိုင္ၿမဲမည္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/04-UNyanissara-DVD03-thit-sar-2.mp4">
								၄။ သစၥာတရား လက္ကိုင္ထား ဘဝခိုင္ၿမဲမည္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/05-UNyanissara-DVD03-thar-mag-gi-1.mp4">
								၅။ သာမဂၢီသုခ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/06-UNyanissara-DVD03-thar-mag-gi-2.mp4">
								၆။ သာမဂၢီသုခ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/07-UNyanissara-DVD03-sa-te-lay-par-1.mp4">
								၇။ ေစတီေလးပါး (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/08-UNyanissara-DVD03-sa-te-lay-par-2.mp4">
								၈။ ေစတီေလးပါး (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/09-UNyanissara-DVD03-eain-taw-yar-1.mp4">
								၉။ အိမ္ေတာ္ရာ ဂရုဏာ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/10-UNyanissara-DVD03-eain-taw-yar-2.mp4">
								၁၀။ အိမ္ေတာ္ရာ ဂရုဏာ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/11-UNyanissara-DVD03-swan-in-thet-teet-1.mp4">
								၁၁။ စြမ္းအင္သတၱိေလးပါး (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/12-UNyanissara-DVD03-swan-in-thet-teet-2.mp4">
								၁၂။ စြမ္းအင္သတၱိေလးပါး (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/13-UNyanissara-DVD03-o-kwel-1.mp4">
								၁၃။ အိုးကြဲေရေလာင္း (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/14-UNyanissara-DVD03-o-kwel-2.mp4">
								၁၄။ အိုးကြဲေရေလာင္း (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/15-UNyanissara-DVD03-myit-ter-1.mp4">
								၁၅။ ေမတၱာနဲ႕ ပညာ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-03/16-UNyanissara-DVD03-myit-ter-2.mp4">
								၁၆။ ေမတၱာနဲ႕ ပညာ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 04</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/01-UNyanissara-DVD04-a-twin-mee.mp4">၁။ အတြင္းမီး အျပင္မီး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/02-UNyanissara-DVD04-thot-pyan-chin.mp4">
								၂။ ထုတ္ျပန္ျခင္းႏွင့္ ဆြဲေဆာင္ျခင္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/03-UNyanissara-DVD04-bate-ku-ni-1.mp4">
								၃။ ဘိကၡဳနီအစ ေဂါတမီက(၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/04-UNyanissara-DVD04-bate-ku-ni-2.mp4">
								၄။ ဘိကၡဳနီအစ ေဂါတမီက(၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/05-UNyanissara-DVD04-su-taung-lay-1.mp4">
								၅။ ဆုေတာင္းေလးေတြ ေျပာင္းလိုက္ပါ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/06-UNyanissara-DVD04-su-taung-lay-2.mp4">
								၆။ ဆုေတာင္းေလးေတြ ေျပာင္းလိုက္ပါ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/07-UNyanissara-DVD04-ku-mu-dra-1.mp4">
								၇။ ကုမုျဒာေတြ ပြင့္တဲ့ည (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/08-UNyanissara-DVD04-ku-mu-dra-2.mp4">
								၈။ ကုမုျဒာေတြ ပြင့္တဲ့ည (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/09-UNyanissara-DVD04-dot-kha-kabar-1.mp4">
								၉။ ဒုကၡကမာၻအတြက္ လိုအပ္ခ်က္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/10-UNyanissara-DVD04-dot-kha-kabar-2.mp4">
								၁၀။ ဒုကၡကမာၻအတြက္ လိုအပ္ခ်က္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/11-UNyanissara-DVD04-a-kan-ka-bar-1.mp4">
								၁၁။ အကန္းကမာၻ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/12-UNyanissara-DVD04-a-kan-ka-bar-2.mp4">
								၁၂။ အကန္းကမာၻ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/13-UNyanissara-DVD04-myat-bot-da-1.mp4">
								၁၃။ ျမတ္ဗုဒၶ၏ ေနာက္ဆုံစကား (၆)ခြန္း (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/14-UNyanissara-DVD04-myat-bot-da-2.mp4">
								၁၄။ ျမတ္ဗုဒၶ၏ ေနာက္ဆုံစကား (၆)ခြန္း (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/15-UNyanissara-DVD04-nat-pyay-1.mp4">
								၁၅။ နတ္ျပည္ေရာက္ေၾကာင္း ေကာင္းမႈ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-04/16-UNyanissara-DVD04-nat-pyay-2.mp4">
								၁၆။ နတ္ျပည္ေရာက္ေၾကာင္း ေကာင္းမႈ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>








<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 05</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/01-UNyanissara-DVD05.mp4">
								၁။ ဂႏၶာရမင္းႀကီး သစၥာတရားရွာေဖြပုံ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/02-UNyanissara-DVD05.mp4">
								၂။ ဂႏၶာရမင္းႀကီး သစၥာတရားရွာေဖြပုံ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/03-UNyanissara-DVD05.mp4">
								၃။ စူဠပႏ ၱက ေထရပါဒါန္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/04-UNyanissara-DVD05.mp4">
								၄။ စူဠပႏ ၱက ေထရပါဒါန္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/05-UNyanissara-DVD05.mp4">
								၅။ ဒုကၡ၏ လြတ္ေျမာက္ရာ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/06-UNyanissara-DVD05.mp4">
								၆။ ဒုကၡ၏ လြတ္ေျမာက္ရာ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/07-UNyanissara-DVD05.mp4">
								၇။ ခ်မ္းသာေရးေလးပါး (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/08-UNyanissara-DVD05.mp4">
								၈။ ခ်မ္းသာေရးေလးပါး (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/09-UNyanissara-DVD05.mp4">
								၉။ အကန္းကမာၻ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/10-UNyanissara-DVD05.mp4">
								၁၀။ အကန္းကမာၻ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/11-UNyanissara-DVD05.mp4">
								၁၁။ ကာလသည္ ကာလကို စားသည္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/12-UNyanissara-DVD05.mp4">
								၁၂။ ကာလသည္ ကာလကို စားသည္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/13-UNyanissara-DVD05.mp4">
								၁၃။ မဂၢင္ရွစ္ပါး (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/14-UNyanissara-DVD05.mp4">
								၁၄။ မဂၢင္ရွစ္ပါး (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/15-UNyanissara-DVD05.mp4">
								၁၅။ ေမတၱာၿခံဳမွ လုံလိမ့္မည္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/16-UNyanissara-DVD05.mp4">
								၁၆။ ေမတၱာၿခံဳမွ လုံလိမ့္မည္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/17-UNyanissara-DVD05.mp4">
								၁၇။ မေမ့ႏိုင္ေသာ ညတစ္ည</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/18-UNyanissara-DVD05.mp4">
								၁၈။ ကရုဏာဓါတ္ အဆက္မျပတ္ေစနဲ႕</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/19-UNyanissara-DVD05.mp4">
								၁၉။ ဘီလုံးဌက္ႏွင့္ စြန္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/20-UNyanissara-DVD05.mp4">
								၂၀။ စာရိတၱေကာင္းမွ ဘဝေကာင္းမည္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-05/21-UNyanissara-DVD05.mp4">
								၂၁။ ဘဝကို အညီအမွ်ရႈ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 06</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/01-UNyanissara-DVD06.mp4">
								၁။ သရက္ပင္ေအာက္က ခႏီ ၱ(၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/02-UNyanissara-DVD06.mp4">
								၂။ သရက္ပင္ေအာက္က ခႏီ ၱ(၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/03-UNyanissara-DVD06.mp4">
								၃။ ဧရာဝတီမွာ ရြာတဲံ ရတနာမိုး (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/04-UNyanissara-DVD06.mp4">
								၄။ ဧရာဝတီမွာ ရြာတဲံ ရတနာမိုး (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/05-UNyanissara-DVD06.mp4">
								၅။ ေန႕စဥ္သုံး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/06-UNyanissara-DVD06.mp4">
								၆။ ေကာင္းျခင္းေလးပါး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/07-UNyanissara-DVD06.mp4">
								၇။ သီလႏွင့္ ပညာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/08-UNyanissara-DVD06.mp4">
								၈။ ေထာင္ျမင္ ရာစြန္႕</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/09-UNyanissara-DVD06.mp4">
								၉။ ထန္းပင္ငုတ္ (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-06/10-UNyanissara-DVD06.mp4">
								၁၀။ ထန္းပင္ငုတ္ (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၁။ ရတနာမိုး (၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၂။ ရတနာမိုး (၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၃။ တစ္ခုတည္းေသာ လမ္း (၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၄။ တစ္ခုတည္းေသာ လမ္း (၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၅။ အရႈပ္ အရွင္း (၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၆။ အရႈပ္ အရွင္း (၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၇။ နိဗၺာန္ရွာနည္း (၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၈။ နိဗၺာန္ရွာနည္း (၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁၉။ အေမ</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၂၀။ အေမ</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၂၁။ ညီေတာ္ အာနႏၵာ (၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၂၂။ ညီေတာ္ အာနႏၵာ (၂)</font></p>
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
								<font size="4">DVD 07</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/01-UNyanissara-DVD07-AUNG-Taw-MUU-(A).mp4">
								၁။ ေအာင္ေတာ္မူ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/02-UNyanissara-DVD07-Aung-Taw-muu-(B).mp4">
								၂။ ေအာင္ေတာ္မူ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/03-UNyanissara-DVD07-BAR-LA-(A).mp4">
								၃။ ဗာလပ႑ိတ မိတ္ဆက္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/04-UNyanissara-DVD07-Bar-La-(B).mp4">
								၄။ ဗာလပ႑ိတ မိတ္ဆက္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/05-UNyanissara-DVD07-BRAIN-EYE-(A).mp4">
								၅။ ဥာဏ္မ်က္စိ ရွိၾကစမ္းပါ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/06-UNyanissara-DVD07-Brain-eye-(B).mp4">
								၆။ ဥာဏ္မ်က္စိ ရွိၾကစမ္းပါ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/07-UNyanissara-DVD07-KA-YU-NAR-(A).mp4">
								၇။ ကရုဏာ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/08-UNyanissara-DVD07-Ka-Yu-nar-(B).mp4">
								၈။ ကရုဏာ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/09-UNyanissara-DVD07-KAN-NAR-YA-TARTANAR-(A).mp4">
								၉။ ဂႏၶာရ သာသနာေတာ္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/10-UNyanissara-DVD07-Kan-nar-ya-tartanar-(B).mp4">
								၁၀။ ဂႏၶာရ သာသနာေတာ္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/11-UNyanissara-DVD07-MOTHER-(A).mp4">
								၁၁။ အေမ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/12-UNyanissara-DVD07-Mother-(B).mp4">
								၁၂။ အေမ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/13-UNyanissara-DVD07-PAN-NE-TA.mp4">
								၁၃။ ပ႑ိတ လကၡဏာ </a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/14-UNyanissara-DVD07-PU-ZAW-HITKE-THU-(A).mp4">
								၁၄။ ပူေဇာ္ထိုက္သူကို ဂုဏ္ျပဳပူေဇာ္ျခင္း (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/15-UNyanissara-DVD07-PU-ZAW-HITKE-THU-(B).mp4">
								၁၅။ ပူေဇာ္ထိုက္သူကို ဂုဏ္ျပဳပူေဇာ္ျခင္း (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/16-UNyanissara-DVD07-SHWE-O-(A).mp4">
								၁၆။ ေရႊအိုးျမဳပ္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-07/17-UNyanissara-DVD07-Shwe-O-(B).mp4">
								၁၇။ ေရႊအိုးျမဳပ္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 08</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/01-UNyanissara-DVD08-UNNTY-(BOSS-1).mp4">
								၁။ သူေ႒းႀကီးမ်ားအေၾကာင္း (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/02-UNyanissara-DVD08-UNNTY-(BOSS-2)-A.mp4">
								၂။ သူေ႒းႀကီးမ်ားအေၾကာင္း (၂-ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/03-UNyanissara-DVD08-UNNTY-(BOSS-2)B.mp4">
								၃။ သူေ႒းႀကီးမ်ားအေၾကာင္း (၂-ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/04-UNyanissara-DVD08-UNNTY(BOSS)3.mp4">
								၄။ သူေ႒းႀကီးမ်ားအေၾကာင္း (၃)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/05-UNyanissara-DVD08-UNNTY-(Ayeyar-Wai-De-A).mp4">
								၅။ ဧရာဝတီမွာ ရြာတဲ့ ရတနာမိုး(ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/06-UNyanissara-DVD08-UNNTY(Ayeyar-Wai-De-B).mp4">
								၆။ ဧရာဝတီမွာ ရြာတဲ့ ရတနာမိုး(ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/07-UNyanissara-DVD08-UNNTY-(MIND).mp4">
								၇။ စိတ္ျပင္နည္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/08-UNyanissara-DVD08-UNNTY(Tayar-Nar-Ya-Chin)1.mp4">
								၈။ တရားနာရျခင္းသည္ ကံေကာင္းသည္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/09-UNyanissara-DVD08-UNNTY(Tayar-Nar-Ya-Chin)2.mp4">
								၉။ တရားနာရျခင္းသည္ ကံေကာင္းသည္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/10-UNyanissara-DVD08-UNNTY-(dama-sat-kyar-A).mp4">
								၁၀။ ဓမၼစႀကၤာ မိတ္ဆက္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/11-UNyanissara-DVD08-UNNTY-(dama-sat-kyar-B).mp4">
								၁၁။ ဓမၼစႀကၤာ မိတ္ဆက္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-08/12-UNyanissara-DVD08-UNNTY-(THIN-KA-TA-).mp4">
								၁၂။ သခၤတလကၡဏာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 09</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/01-UNyanissara-DVD09-Darotekhandawpamar-(1).mp4">
								၁။ ဒါရုကၡေႏၶာပမာသုတၱန္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/02-UNyanissara-DVD09-Darotekhandawpamar-(2).mp4">
								၂။ ဒါရုကၡေႏၶာပမာသုတၱန္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/03-UNyanissara-DVD09-Alotepay-(Anarhtapaindikawada-1).mp4">
								၃။ အနာထပိ႑ိေကာဝါဒ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/04-UNyanissara-DVD09-Alotepay-(Anarhtapaindikawwahda-2).mp4">
								၄။ အနာထပိ႑ိေကာဝါဒ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/05-UNyanissara-DVD09-Alotepay-(Anarhtapaindikawahda-3).mp4">
								၅။ အနာထပိ႑ိေကာဝါဒ (တ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/06-UNyanissara-DVD09-Alotepay-(Anarhtapaindikawida-4).mp4">
								၆။ အနာထပိ႑ိေကာဝါဒ (စ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/07-UNyanissara-DVD09-Anarparna-(1).mp4">
								၇။ အာနာပါန သတိပ႒ာန္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/08-UNyanissara-DVD09-Anarparna-(2).mp4">
								၈။ အာနာပါန သတိပ႒ာန္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/09-UNyanissara-DVD09-Anarparna-(3).mp4">
								၉။ အာနာပါန သတိပ႒ာန္ (တ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/10-UNyanissara-DVD09-Daththtba-(1).mp4">
								၁၀။ ေဝဒနာဒ႒ဗၺ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/11-UNyanissara-DVD09-daththtba-(2).mp4">
								၁၁။ ေဝဒနာဒ႒ဗၺ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/12-UNyanissara-DVD09-Waidanarnupatanar(1).mp4">
								၁၂။ ေဝဒနာႏုပႆနာသတိပ႒ာန္ (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/13-UNyanissara-DVD09-Waidanarnupatnar(2).mp4">
								၁၃။ ေဝဒနာႏုပႆနာသတိပ႒ာန္ (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/14-UNyanissara-DVD09-Waidanarnapatanar-(3).mp4">
								၁၄။ ေဝဒနာႏုပႆနာသတိပ႒ာန္ (တ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/15-UNyanissara-DVD09-Waidanarwaitkhanbana(1).mp4">
								၁၅။ ေဝဒနာနိကၡမ ၻန (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/16-UNyanissara-DVD09-Waidanarwaitkhanbana-(2).mp4">
								၁၆။ ေဝဒနာနိကၡမ ၻန (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-09/17-UNyanissara-DVD09-Bawatanboe.mp4">
								၁၇။ ဘဝတန္ဘိုး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 10</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/01-UNyanissara-DVD10-Mist-si-Ma-Pa-Ti-Pa-Tar.mp4">
								၁။မဇၥ်ိမပဋိပဋာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/02-UNyanissara-DVD10-Gayunar-Dat.mp4">
								၂။ ကရုဏာဓါတ္ အဆက္မျပတ္ေစနဲ႕</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/03-UNyanissara-DVD10-Nake-Ban-Ko-Oo-Tei-Ti-Larn.mp4">
								၃။ နိဗၺာန္သို႕ ဦးတည္သည္႕လမ္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/04-UNyanissara-DVD10-Amway-Pay-Amway-Yu.mp4">
								၄။ အေမြေပး အေမြယူ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/05-UNyanissara-DVD10-A-Shit-Tayar-to-tt.mp4">
								၅။ အရွိတရားႏွင့္ အမွန္တရား</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/06-UNyanissara-DVD10-Buddha-Note-Thara.mp4">
								၆။ ဗုဒၶႏုႆတိဘာဝနာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/07-UNyanissara-DVD10-Khaung-MU-KO.mp4">
								၇။ ေကာင္းမႈကို အထင္းမေသးနဲ႕</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/08-UNyanissara-DVD10-UNNTY(Tayar-Nar-Ya-Chin)1.mp4">
								၈။ တရားနာရျခင္း၏ အက်ိဳးေက်းဇူး (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/09-UNyanissara-DVD10-UNNTY(Tayar-Nar-Ya-Chin)2.mp4">
								၉။ တရားနာရျခင္း၏ အက်ိဳးေက်းဇူး (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/10-UNyanissara-DVD10-Kaung-Chinn-(4)-Parr.mp4">
								၁၀။ ေကာင္းျခင္းေလးပါ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/11-UNyanissara-DVD10-Htaung-Myin-Yar-Swint.mp4">
								၁၁။ ေထာင္ျမင္ ရာစြန္႕</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/12-UNyanissara-DVD10-Amyatsone-Apatmarda.mp4">
								၁၂။ အျမတ္ဆုံး အပၸမာဒ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/13-UNyanissara-DVD10-Pahtann-Yaung.mp4">
								၁၃။ ပ႒ာန္းေရာင္ျခည္ ဘုရားရွိခိုး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/14-UNyanissara-DVD10-Atuyar-Tite-Pwe.mp4">
								၁၄။ အသူရာတိုက္ပြဲ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/15-UNyanissara-DVD10-Nay-Sin-Thone.mp4">
								၁၅။ ေန႕စဥ္သုံး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-10/16-UNyanissara-DVD10-Barkula.mp4">
								၁၆။ အရွင္ဗာကုလ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 11</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/01-UNyanissara-DVD11-The-Kone-(Nat-Mauk-Myo-Ka-Su-Taung-Tan).mp4">
								၁။ နတ္ေမာက္ၿမိဳ႕မွ ဆုေတာင္းသံ (နတ္ေမာက္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၂။ သံေယာဇဥ္အားလုံးမွ လြတ္ေျမာက္သူ 
								(နတ္ေမာက္)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/02-UNyanissara-DVD11-HarHin.mp4">
								<font size="4">၂</font></a><font size="4"><a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/02-UNyanissara-DVD11-HarHin.mp4">။ 
								ဟာ..ဟင္ (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/03-UNyanissara-DVD11-Donation.mp4">
								၃။ ဆင္းရဲသားအလႈႏွင့္ သူေ႒းအလႈ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/04-UNyanissara-DVD11-Tayarnaryachinthe-Kankaungthe.mp4">
								၄။ တရားနာျခင္းသည္ ကံေကာင္းသည္ (တာေမြ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/05-UNyanissara-DVD11-Shwemyayhmar-balo-nehmarle.mp4">
								၅။ ေရႊေျမမွာ ဘယ္လိုေနမလဲ (က်ိဳက္မေရာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/06-UNyanissara-DVD11-Buddhist.mp4">၆။ ဗုဒၶ၏ေနာက္ဆုံးစကား (မေကြး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/07-UNyanissara-DVD11-Su-Taung-(5)-Myo-A.mp4">
								၇။ ဆုေတာင္းငါးမ်ိဳး (က) (ေျမာက္ဥကၠလာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/08-UNyanissara-DVD11-Su-Taung-(5)Myo-B.mp4">
								၈။ ဆုေတာင္းငါးမ်ိဳး (ခ) (ေျမာက္ဥကၠလာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/09-UNyanissara-DVD11-Tan-Phoe-Shi-Tar-A.mp4">
								၉။ တန္ဖိုးရွိတာ တန္ဖိုးသိပါ (က) (ေျမဇင္းေတာရ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/10-UNyanissara-DVD11-Tan-Phoe-Shi-Tar-B.mp4">
								၁၀။ တန္ဖိုးရွိတာ တန္ဖိုးသိပါ (ခ) (ေျမဇင္းေတာရ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/11-UNyanissara-DVD11-A-Twinn-Shoke-A.mp4">
								၁၁။ အတြင္းရႈပ္ရႈပ္၊ အျပင္ရႈပ္ရႈပ္ (က) 
								(ဗိုလ္တေထာင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-11/12-UNyanissara-DVD11-A-Twinn-Shoke-B.mp4">
								၁၂။ အတြင္းရႈပ္ရႈပ္၊ အျပင္ရႈပ္ရႈပ္ (ခ) 
								(ဗိုလ္တေထာင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 12</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/01-UNyanissara-DVD12-UpyitKhar(A).mp4">
								၁။ ဥေပကၡာျဖင့္ ဘဝကို အလွျပင္ (က) (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/02-UNyanissara-DVD12-Upyitkar(B).mp4">
								၂။ ဥေပကၡာျဖင့္ ဘဝကို အလွျပင္ (ခ) (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/03-UNyanissara-DVD12-KyaukSeinLatKauk(A).mp4">
								၃။ ေက်ာက္စိမ္းလက္ေကာက္ (က) (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/04-UNyanissara-DVD12-kyaukSeinLatKauk(B).mp4">
								၄။ ေက်ာက္စိမ္းလက္ေကာက္ (ခ) (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/05-UNyanissara-DVD12-Damma(A).mp4">
								၅။ ဓမၼကထာ (က) (မႏ ၱေလးသာသနာ့တကၠသိုလ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/06-UNyanissara-DVD12-Damma(B).mp4">
								၆။ ဓမၼကထာ (ခ) (မႏ ၱေလးသာသနာ့တကၠသိုလ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/07-UNyanissara-DVD12-Dana(A).mp4">
								၇။ ဒါနကထာ (က) (က်ိဳက္လတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/08-UNyanissara-DVD12-Dana(B).mp4">
								၈။ ဒါနကထာ (ခ) (က်ိဳက္လတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/09-UNyanissara-DVD12-ThanWaiga(A).mp4">
								၉။ သံေဝဂကထာ (က) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/10-UNyanissara-DVD12-ThanWaiga(B).mp4">
								၁၀။ သံေဝဂကထာ (ခ) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/11-UNyanissara-DVD12-AsonLokaungneKyapar.mp4">
								၁၁။ အစြန္းလြတ္ေအာင္ ေနၾကပါ (ေျမာက္ဥကၠလာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/12-UNyanissara-DVD12-KoSarKyatHmarKoNePa.mp4">
								၁၂။ ကိုယ့္စာက်က္မွာ ကိုယ္ေနပါ (ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/13-UNyanissara-DVD12-Thadar(A).mp4">
								၁၃။ သဒၵါႏွင့္ မစ ၦရိယတိုက္ပြဲ (၁) (ကမာရြတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/14-UNyanissara-DVD12-Thada(B).mp4">
								၁၄။ သဒၵါႏွင့္ မစ ၦရိယတိုက္ပြဲ (၂) (ကမာရြတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/15-UNyanissara-DVD12-Thada(C).mp4">
								၁၅။ သဒၵါႏွင့္ မစ ၦရိယတိုက္ပြဲ (၃) (ကမာရြတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-12/16-UNyanissara-DVD12-Thada(D).mp4">
								၁၆။ သဒၵါႏွင့္ မစ ၦရိယတိုက္ပြဲ (၄) (ကမာရြတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 13</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/01-UNyanissara-DVD13-Maharthamaya(A).mp4">
								၁။ မဟာသမယသုတ္ အႏွစ္ခ်ဳပ္ (၁) ဗဟန္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/02-UNyanissara-DVD13-Maharthamaya(B).mp4">
								၂။ မဟာသမယသုတ္ အႏွစ္ခ်ဳပ္ (၂) ဗဟန္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/03-UNyanissara-DVD13-Nenee(A).mp4">
								၃။ ေနနည္းေလးပါး (၁) (ၾကည္႕ျမင္တိုင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/04-UNyanissara-DVD13-Nenee(B).mp4">
								၄။ ေနနည္းေလးပါး (၂) (ၾကည္႕ျမင္တိုင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/05-UNyanissara-DVD13-SuTaungMaHmar(A).mp4">
								၅။ ဆုေတာင္းမမွားေစနဲ႕ (၁) (သံေစ်း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/06-UNyanissara-DVD13-SuTaungMaHmar(B).mp4">
								၆။ ဆုေတာင္းမမွားေစနဲ႕ (၂) (သံေစ်း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/07-UNyanissara-DVD13-MyintTarSwanYi-(1).mp4">
								၇။ ေမတၱာစြမ္းရည္ (၁) (မႏ ၱေလးဗုဒၶတကၠသိုလ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/08-UNyanissara-DVD13-MyintTarSwanYi(B).mp4">
								၈။ ေမတၱာစြမ္းရည္ (၂) (မႏ ၱေလးဗုဒၶတကၠသိုလ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/09-UNyanissara-DVD13-SanPyaKuThoShin(A).mp4">
								၉။ စံျပကုသိုလ္ရွင္မ်ား (၁) (ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/10-UNyanissara-DVD13-SanPyaKuThoShin(B).mp4">
								၁၀။ စံျပကုသိုလ္ရွင္မ်ား (၂) (ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/11-UNyanissara-DVD13-ThaMarDikeHtee.mp4">
								၁၁။ သမၼာဒိ႒ိ (ၾကည္႕ျမင္တိုင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-13/12-UNyanissara-DVD13-BaWaTanBoAYaYou.mp4">
								၁၂။ ဘဝတန္ဘိုး အရယူပါ (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 14</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/01-UNyanissara-DVD14-nauk-sone(10)-(A).mp4">
								၁။ ေနာက္ဆုံးဆယ္လ ျမတ္ဗုဒၶ (၁) (မႏ ၱေလး၊ 
								မဟာဂႏၶာရုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/02-UNyanissara-DVD14-nauk-sone(10)-(B).mp4">
								၂။ ေနာက္ဆုံးဆယ္လ ျမတ္ဗုဒၶ (၂) (မႏ ၱေလး၊ 
								မဟာဂႏၶာရုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/03-UNyanissara-DVD14-myat-buddha.mp4">
								၃။ ျမတ္ဗုဒၶ၏ အလယ္လမ္း (ပုသိမ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/04-UNyanissara-DVD14-DammaDuta(A).mp4">
								၄။ ဓမၼဒူတပုဂၢိဳလ္တို႕၏ ဓမၼေအာင္လံ (၁) 
								(မရမ္းကုန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/05-UNyanissara-DVD14-DammaDuta(B).mp4">
								၅။ ဓမၼဒူတပုဂၢိဳလ္တို႕၏ ဓမၼေအာင္လံ (၂) 
								(မရမ္းကုန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/06-UNyanissara-DVD14-Damma.mp4">
								၆။ ဓမၼႏွင့္ ဝိနိယ (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/07-UNyanissara-DVD14-Thatipahtan.mp4">
								၇။ သတိပ႒ာန္ေလးပါး (စမ္းေခ်ာင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/08-UNyanissara-DVD14-Ah-Kwint-Ah-Ray.mp4">
								၈။ အခြင့္အေရး (မတၱရာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/09-UNyanissara-DVD14-Dama.mp4">
								၉။ ဓမၼဝိဒီ (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/10-UNyanissara-DVD14-Luwine(A).mp4">
								၁၀။ လူ ဝိနည္း (၁) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-14/11-UNyanissara-DVD14-Luwine(B).mp4">
								၁၁။ လူ ဝိနည္း (၂) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 15</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/01-UNyanissara-DVD15-(AwWarDa).mp4">
								၁။ ၾသဝါဒ (မဂၤလာတိုက္၊ ေမွာ္ဘီ) ၁၁-၆-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/02-UNyanissara-DVD15-InSein(1).mp4">
								၂။ သံေလွာင္အိမ္ (၁) (အင္းစိန္ဗဟိုအက်ဥ္းေထာင္) 
								၂၁-၈-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/03-UNyanissara-DVD15-InSein(2).mp4">
								၃။ သံေလွာင္အိမ္ (၂) (အင္းစိန္ဗဟိုအက်ဥ္းေထာင္) 
								၂၁-၈-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/04-UNyanissara-DVD15-InSein(3).mp4">
								၄။ သံေလွာင္အိမ္ (၃) (အင္းစိန္ဗဟိုအက်ဥ္းေထာင္) 
								၂၁-၈-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/05-UNyanissara-DVD15-Malaysia(1).mp4">
								၅။ ဗုဒၶဘာသာဝင္ဟူသည္ (၁) (မေလးရွား) ၁၈-၂-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/06-UNyanissara-DVD15-Malaysia(2).mp4">
								၆။ ဗုဒၶဘာသာဝင္ဟူသည္ (၂) (မေလးရွား) ၁၈-၂-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/07-UNyanissara-DVD15-Marnat(10).mp4">
								၇။ မာရ္နတ္ဖမ္းစားျခင္း (ဗဟန္း)&nbsp; ၁၄-၁-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/08-UNyanissara-DVD15-ThanThaYa.mp4">
								၈။ သံသာရ ရိကၡာ (မႏ ၱေလး) ၂၂-၁-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/09-UNyanissara-DVD15-Ason-hnit-phat.mp4">
								၉။ အစြန္းႏွစ္ဖက္ လြတ္ေအာင္ေရွာင္ (အင္းစိန္) 
								၂၃-၃-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-15/10-UNyanissara-DVD15-Pyinnyar.mp4">
								၁၀။ ပညာျဖင့္ အက်င့္ကို ေတာက္ေျပာင္ပါေစ (အိမ္မဲ)&nbsp; 
								၃၀-၃-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 16</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/01-UNyanissara-DVD16-Father-Day.mp4">
								၁။ အေဖေန႕ (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/02-UNyanissara-DVD16-Mother(A).mp4">
								၂။ အေမ (က) (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/03-UNyanissara-DVD16-Mother(B).mp4">
								၃။ အေမ (ခ) (မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/04-UNyanissara-DVD16-TawAoke.mp4">
								၄။ ေတာအုပ္ႀကီးႏွင့္တူေသာ သာသနာ (တိုက္ႀကီး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/05-UNyanissara-DVD16-Htar-Wal.mp4">
								၅။ ခြင့္လႊတ္ျခင္းႏွင့္ သည္းခံျခင္း၊ 
								ေမ့ေပ်ာက္ျခင္း (ထားဝယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/06-UNyanissara-DVD16-PanTANaw.mp4">
								၆။ ေျမႀကီးမွ ေရႊထီးသို႕ (ပန္းတေနာ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/07-UNyanissara-DVD16-Kyaung-Hlu-(A).mp4">
								၇။ ေက်ာင္းလႈရျခင္းအက်ိဳး (က) (မတၱရာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/08-UNyanissara-DVD16-Kyaung-Hlu-(B).mp4">
								၈။ ေက်ာင္းလႈရျခင္းအက်ိဳး (ခ) (မတၱရာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/09-UNyanissara-DVD16-Sate-Yine-Ko-Pyin.mp4">
								၉။ စိတ္ရိုင္းကိုျပင္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-16/10-UNyanissara-DVD16-Dote-Kha-Har.mp4">
								၁၀။ ဒုကၡဘာေၾကာင့္ ျဖစ္ရသလဲ (ရန္ကင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 17</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/01-UNyanissara-DVD17-Mandalay(A).mp4">
								၁။ ခ်မ္းသာစြာ အိပ္စက္ႏိုင္ၾကပါေစ (ပ)&nbsp; (မႏ 
								ၱေလးအက်ဥ္းေထာင္) ၁၆-၁၀-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/02-UNyanissara-DVD17-Mandaly(B).mp4">
								၂။ ခ်မ္းသာစြာ အိပ္စက္ႏိုင္ၾကပါေစ (ဒု)&nbsp; (မႏ 
								ၱေလးအက်ဥ္းေထာင္) ၁၆-၁၀-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/03-UNyanissara-DVD17-Mandalay(C).mp4">
								၃။ ခ်မ္းသာစြာ အိပ္စက္ႏိုင္ၾကပါေစ (တ)&nbsp; (မႏ 
								ၱေလးအက်ဥ္းေထာင္) ၁၆-၁၀-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/04-UNyanissara-DVD17-Thawtarpan.mp4">
								၄။ ေသာတာပန္ကရုဏာ (စစ္ကိုင္း) ၁၄-၉-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/05-UNyanissara-DVD17-ShweBo.mp4">
								၅။ ေရႊဘိုကရုဏာ (ေရႊဘို)&nbsp; ၁၇-၉-၂၀၁၀</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/06-UNyanissara-DVD17-eain-taw-yar(A).mp4">
								၆။ အိမ္ေတာ္ရာ ကရုဏာ (၁) (မႏ ၱေလး၊ အိပ္ေတာ္ရာ 
								၁၄ခန္း ဓမၼဗိမာန္) ၁၇-၇-၂၀၀၈</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/07-UNyanissara-DVD17-eain-taw-yar-(B).mp4">
								၇။ အိမ္ေတာ္ရာ ကရုဏာ (၂) (မႏ ၱေလး၊ အိပ္ေတာ္ရာ 
								၁၄ခန္း ဓမၼဗိမာန္) ၁၇-၇-၂၀၀၈</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/08-UNyanissara-DVD17-Ka-Yu-Nar-(A).mp4">
								၈။ ကရုဏာ (ပ) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-17/09-UNyanissara-DVD17-Ka-Yu-nar-(B).mp4">
								၉။ ကရုဏာ (ဒု) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 18</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/01-UNyanissara-DVD18-22-11-2010.mp4">
								၁။ အိုသည္႕တိုင္ေအာင္ ေကာင္းမယ့္တရား (၄) ပါး 
								(လမ္းမေတာ္ - သံေစ်း&nbsp;&nbsp; ၂၂-၁၁-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/02-UNyanissara-DVD18-09-10-2010.mp4">
								၂။ သစၥာတရားကို ရွာေဖြျခင္းႏွင့္ လြတ္ေျမာက္ေရးကို 
								ရွာေဖြျခင္း (မိထၳီလာ&nbsp; ၉-၁၀-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/03-UNyanissara-DVD18-25-8-2010.mp4">
								၃။ ေမတၱာစြမ္းရည္&nbsp; (ပုဂံ&nbsp; ၂၅-၈-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/04-UNyanissara-DVD18-10-6-2010.mp4">
								၄။ သာသနာေတာ္၏ အႏွစ္သုံးပါး (စကၤာပူ&nbsp; 
								၁၀-၆-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/05-UNyanissara-DVD18-12-6-2010.mp4">
								၅။ ဘဝ၏ ရည္ရြယ္ခ်က္ေလးပါး (စကၤာပူ&nbsp; 
								၁၂-၆-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/06-UNyanissara-DVD18-10-8-2009.mp4">
								၆။ အစြန္းမေရာက္ေစနဲ႕ (မိထၳီလာ&nbsp; ၁၀-၈-၂၀၀၉)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/07-UNyanissara-DVD18-27-6-2010.mp4">
								၇။ သံသရာရဲ႕ အဆန္လမ္း (မရမ္းကုန္း&nbsp; 
								၂၇-၆-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-18/08-UNyanissara-DVD18-6-3-2010.mp4">
								၈။ ပုကၠဳသမလႅ&nbsp; (ျပင္ခရိုင္&nbsp; ၆-၃-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 19</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/01-UNyanissara-DVD19-ABiDamMa(Intro).mp4">
								၁။ အဘိဓမၼာမိတ္ဆက္&nbsp; (ကမ ၻာေအး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/02-UNyanissara-DVD19-KaBarAye.mp4">၂။ အဘိဓမၼာသင္တန္း (ကမ ၻာေအး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/03-UNyanissara-DVD19-ThaTiPaHtan(1).mp4">၃။ သတိပ႒ာန္(၁) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/04-UNyanissara-DVD19-ThaTiPaHtan(2).mp4">
								၄။ သတိပ႒ာန္(၂) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/05-UNyanissara-DVD19-ThaTiPaHtan(3).mp4">
								၅။ သတိပ႒ာန္(၃) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/06-UNyanissara-DVD19-ThatiPaHtan(4).mp4">
								၆။ သတိပ႒ာန္(၄) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/07-UNyanissara-DVD19-ThaTiPaHtan(5).mp4">
								၇။ သတိပ႒ာန္(၅) (စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-19/08-UNyanissara-DVD19-18-11-2010.mp4">
								၈။ အိုေအာင္ေကာင္းေသာ တရားေလးပါး (ဒဂုံေတာင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 20</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-20/01-UNyanissara-DVD20.mp4">
								၁။ ဆရာေတာ္၏ (၇၃)ႏွစ္ေျမာက္ ေမြးေန႕ အလႈေတာ္မဂၤလာ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-20/02-UNyanissara-DVD20.mp4">
								၂။ သာဓု သုတၱန္ (၃၀-၂၂-၂၀၁၀ မေကြး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-20/03-UNyanissara-DVD20.mp4">
								၃။ ဘဝပင္လယ္မွာ ကၽြန္းကေလးမ်ား တည္ေဆာက္ႏိုင္ပါ 
								(၁) ၃၀-၁၂-၂၀၁၀ မႏ ၱေလး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-20/04-UNyanissara-DVD20.mp4">
								၄။ ဘဝပင္လယ္မွာ ကၽြန္းကေလးမ်ား တည္ေဆာက္ႏိုင္ပါ 
								(၂) ၃၀-၁၂-၂၀၁၀ မႏ ၱေလး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-20/05-UNyanissara-DVD20.mp4">၅။ သဒၶမၼပဋိရူပက (၃-၂-၂၀၁၁ ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-20/06-UNyanissara-DVD20.mp4">၆။ အနာဂါတ္ လူငယ္ဖြံ႕ၿဖိဳးေရး 
								(၁၃-၂-၂၀၁၁&nbsp; ေဒါပုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 21</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-21/01-UNyanissara-DVD21.mp4">
								၁။ နတ္သားေမးေသာပုစာၦေလးမ်ိဳး (ပန္းဘဲတန္း&nbsp; 
								၆-၂-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-21/02-UNyanissara-DVD21.mp4">
								၂။ သာသနာတည္ျခင္း၏ အေၾကာင္းႏွင့္ သာသနာ 
								ပ်က္စီးျခင္း၏ အေၾကာင္း (သုဝဏၰစစ္ကိုင္း 
								စာသင္တိုက္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-21/03-UNyanissara-DVD21.mp4">
								၃။ မ်ိဳးဆက္သစ္လူငယ္မ်ားသို႕ စိတ္ဓါတ္ျမွင့္တင္ေရး 
								(ကမာရြတ္&nbsp; ၃၁-၁-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-21/04-UNyanissara-DVD21.mp4">
								၄။ အရွင္အႏုရုဒၶါ (ရာေက်ာ္ - စစ္ကိုင္း&nbsp; 
								၂၈-၈-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-21/05-UNyanissara-DVD21.mp4">
								၅။ ဘဝသမိုင္းမွတ္တမ္းတင္ ေကာင္းရမည္&nbsp; 
								(ျမင္းၿခံ&nbsp; ၂၉-၈-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-21/06-UNyanissara-DVD21.mp4">
								၆။ အရွင္ဗာကုလ (ရာေက်ာ္ - စစ္ကိုင္၊ ၃-၈-၂၀၁၀)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 22</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-22/01-UNyanissara-DVD22-20-1-2011.mp4">
								၁။ တရားတုက တရားစစ္ကို ဖ်က္စီတတ္ပုံ (ဒဂုံ&nbsp; 
								၂၀-၁-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-22/02-UNyanissara-DVD22-21-1-2011.mp4">
								၂။ မိမိဘဝရပ္တည္မႈကို မိမိကိုယ္တိုင္တည္ေဆာက္ပါ 
								(ဘိုကေလး&nbsp; ၂၁-၁-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-22/03-UNyanissara-DVD22-24-1-2011.mp4">
								၃။ အာယုဒါန&nbsp; (ပုသိမ္&nbsp; ၂၄-၁-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-22/04-UNyanissara-DVD22-02-2-2011.mp4">
								၄။ ဘဝဆိုတာ ပင္လယ္နဲ႕တူတယ္&nbsp; (ေမွာဘီ&nbsp; 
								၂-၂-၂၀၁၁</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-22/05-UNyanissara-DVD22-25-2-2011.mp4">
								၅။ မြန္ျမတ္ေသာ အက်င့္&nbsp; (သနပ္ပင္&nbsp; 
								၂၅-၂-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 23</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-23/01-UNyanissara-DVD23.mp4">
								၁။ ၾသဝါဒ ပါတိေမာက္ (၁၉-၂-၂၀၁၁&nbsp; အလုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-23/02-UNyanissara-DVD23.mp4">
								၂။ ၿငိမ္ၿပီး ၿငိမ္းေနတဲ့ နိဗၺာန္မွာ ေနၾကပါ 
								(၂-၃-၂၀၁၁&nbsp; ဖ်ာပုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-23/03-UNyanissara-DVD23.mp4">
								၃။ ေပးရင္ေပါ့ ယူရင္ေလး (၃၁-၃-၂၀၁၁ သာေကတ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-23/04-UNyanissara-DVD23.mp4">
								၄။ အိုရင္..ျပင္ထားၾက&nbsp; (၃-၄-၃၀၁၁&nbsp; 
								အင္းစိန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 24</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-24/01-UNyanissara-DVD24.mp4">
								၁။ အျမတ္ဆုံးေက်ာင္း အလႈဒါန&nbsp; (၁၂-၁-၂၀၁၀ 
								လိႈင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-24/02-UNyanissara-DVD24.mp4">
								၂။ ဘဝျပည္႕စုံျခင္း၏ အေျခခံ အေၾကာင္းတရား 
								(၄-၃-၂၀၁၀&nbsp; ဟိုင္ႀကီးကၽြန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-24/03-UNyanissara-DVD24.mp4">
								၃။ ဘဝတစ္ခုလုံး၏ အျမတ္ဆုံးဥစၥာ(၂)ပါး&nbsp; 
								(၃၀-၃-၂၀၁၀ အိမ္မဲ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-24/04-UNyanissara-DVD24.mp4">
								၄။ မျဖစ္ခ်င္လို႕ က်င့္တာ&nbsp; (၁၃-၄-၂၀၁၁&nbsp; 
								စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 25</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-25/01-UNyanissara-DVD25.mp4">
								၁။ သာမေဏငယ္မ်ား၏ စြမ္းရည္ျပ&nbsp; (၁-၄-၂၀၁၁ 
								သန္လွ်င္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-25/02-UNyanissara-DVD25.mp4">
								၂။ ေကာင္းေသာအရပ္တြင္ လူျဖစ္ပါေစ (၃-၄-၂၀၁၁ 
								သန္လွ်င္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-25/03-UNyanissara-DVD25.mp4">
								၃။ အေၾကာင္းရွိလို႕ ျဖစ္တာ&nbsp; (၁၅-၂-၂၀၁၀&nbsp; 
								ေက်ာင္တံခါး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-25/04-UNyanissara-DVD25.mp4">
								၄။ ဘဝဝန္တမ္းႏွင့္ ဝန္တုပ္ (၂၈-၈-၂၀၀၉&nbsp; 
								ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 26</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-26/01-UNyanissara-DVD26.mp4">
								၁။ ပေသနဒီေကာသလမင္းႀကီး၏ အေမးေလးျဖာ(၁)&nbsp; 
								(၂၉-၄-၂၀၁၁&nbsp; ေရႊကူ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-26/02-UNyanissara-DVD26.mp4">
								၂။ ပေသနဒီေကာသလမင္းႀကီး၏ အေမးေလးျဖာ(၂)&nbsp; 
								(၂၉-၄-၂၀၁၁&nbsp; ေရႊကူ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-26/03-UNyanissara-DVD26.mp4">
								၃။ ဘဝလမ္းညႊန္ (၁)&nbsp; (၃၀-၄-၂၀၁၁&nbsp; 
								ဗန္းေမာ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၄။ ဘဝလမ္းညႊန္ (၂)&nbsp; 
								(၃၀-၄-၂၀၁၁&nbsp; ဗန္းေမာ္)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၅။ သာသနာ့အေမြခံ (၁) (၁-၅-၂၀၁၁ 
								ကူလုံေက်ာက္ဝိုင္း)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၆။ သာသနာ့အေမြခံ (၂) (၁-၅-၂၀၁၁ 
								ကူလုံေက်ာက္ဝိုင္း)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 27</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-27/01-UNyanissara-DVD27.mp4">
								၁။ ေအာင္ေဗာဓိမွာ ေအာင္ျမင္ၾကပါေစ (၁)&nbsp; 
								(၁၆-၂-၂၀၁၁&nbsp; ေတာင္ဒဂုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-27/02-UNyanissara-DVD27.mp4">
								၂။ ေအာင္ေဗာဓိမွာ ေအာင္ျမင္ၾကပါေစ (၂)&nbsp; 
								(၁၆-၂-၂၀၁၁&nbsp; ေတာင္ဒဂုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-27/03-UNyanissara-DVD27.mp4">
								၃။ ျဖားေယာင္းတိုင္း နားမေယာင္နဲ႕ (၁)&nbsp; 
								(၇-၃-၂၀၁၁&nbsp; ေပါင္းတည္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-27/04-UNyanissara-DVD27.mp4">၄။ ျဖားေယာင္းတိုင္း နားမေယာင္နဲ႕ (၂)&nbsp; 
								(၇-၃-၂၀၁၁&nbsp; ေပါင္းတည္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-27/05-UNyanissara-DVD27.mp4">၅။ သက္ေတာ္ (၇၄)ႏွစ္ျပည္႕ ဝိဇာတ 
								မဂၤလာ (၁၈-၃-၂၀၁၁ စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-27/06-UNyanissara-DVD27.mp4">၆။ သီတဂူ 
								အာေရာဂ်ဒါနေဆးရုံေတာ္ဖြင့္ပြဲ (၁၀-၂-၂၀၁၁ ထားဝယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 28</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-28/01-UNyanissara-DVD28.mp4">
								၁။ ေခါင္းေဆာင္တို႕၏ က်င့္စဥ္ - 
								သီတဂူကမာၻ႕ဗုဒၶတကၠသိုလ္ (ရန္ကုန္) ဖြင့္ပြဲ 
								အခမ္းအနား&nbsp; (၁၈-၆-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-28/02-UNyanissara-DVD28.mp4">
								၂။ စြန္႕လႊတ္ျခင္းမွ လြတ္ေျမာက္ျခင္းဆီငို႕&nbsp; 
								(၂၅-၄-၂၀၁၁&nbsp; စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-28/03-UNyanissara-DVD28.mp4">
								၃။ ဓမၼကိုၾကားနာရ၍ ကံေကာင္းၾကသူမ်ား&nbsp; 
								(၂၈-၃-၂၀၁၁&nbsp; ကသာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0" align="left">
<font size="4">****dhamma talks uploaded and published on 13 May 2012****</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD 29</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ကမာၻ႕ကုလသမဂၢ႒ာနခ်ဳပ္</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-29/01-UNyanissara-DVD29.mp4">၁။ ျဗဟၼစရိယ (အပိုင္း-၁)&nbsp; ၁-၇-၂၀၁၁ မႏ ၱေလး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-29/02-UNyanissara-DVD29.mp4">၂။ ျဗဟၼစရိယ (အပိုင္း-၂)&nbsp; ၃-၇-၂၀၁၁ မႏ ၱေလး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-29/03-UNyanissara-DVD29.mp4">၃။ ျဗဟၼစရိယ (အပိုင္း-၃)&nbsp; 
								၅-၇-၂၀၁၁ မႏ ၱေလး</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-29/04-UNyanissara-DVD29.mp4">၄။ ဓမၼဝိနယေဒသနာေတာ္ ၂-၅-၂၀၁၁ 
								နမ့္ခမ္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-29/05-UNyanissara-DVD29.mp4">၅။ ဗုဒၶေန႕ အမ္းအနာ (၁၆-၅-၂၀၁၁ 
								ကမာၻ႕ကုလသမဂၢ႒ာနခ်ဳပ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၀)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ႏွလုံးသားကိုျပင္</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-30/01-UNyanissara-DVD30.mp4">၁။ ႏွလုံးသားကိုျပင္ 
								(အင္ဒိုနီရွား)</a> 
								ေလဆိပ္အႀကိဳ (not dhamma talk)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-30/02-UNyanissara-DVD30.mp4">
								၂။ ႏွလုံးသားကိုျပင္ 
								(အင္ဒိုနီရွား)</a> 
								တရားပြဲ</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-30/03-UNyanissara-DVD30.mp4">
								၃။ ျဗဟၼစရိယ (၄) (ျဗဟၼစို 
								လူမႈေရးအသင္း ၁၂-၇-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-30/04-UNyanissara-DVD30.mp4">
								၄။ ဝါဆိုသကၤန္းကပ္ (သဲကုန္းအသင္း - 
								ရန္ကုန္ ၁၅-၆-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-30/05-UNyanissara-DVD30.mp4">
								၅။ ျဗဟၼစရိယ (၅) မုဒိတာ 
								(ေမာရိယမိသားစု - ၁၆-၇-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-30/06-UNyanissara-DVD30.mp4">
								၆။ ျဗဟၼစရိယ (၆) ဥေပကၡ 
								(မဟာဓမၼိကာရာမတိုက္ - ၁၇-၇-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ရုပ္သာအို၍ ဥာဏ္ပညာမအို</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-31/01-UNyanissara-DVD31.mp4">၁။ ဥာဏ္ထင္သူအတြက္ ဗုဒၶမိန္႕ခြန္း 
								(၁၆-၁၀-၂၀၁၁ - အမရပူရ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-31/02-UNyanissara-DVD31.mp4">၂။ တရားမွ်တျခင္း၊ 
								ၿငိမ္းခ်မ္းျခင္း၊ ညီညြတ္ျခင္းႏွင့္ 
								အတူလက္တြဲေနထိုင္ျခင္း (၈-၉-၂၀၁၁ - မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-31/03-UNyanissara-DVD31.mp4">၃။ အိုသည္႕တိုင္ေအာင္ 
								ေကာင္းမယ့္တရား (၁၄-၁၀-၂၀၁၁ - ေက်ာက္တန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-31/04-UNyanissara-DVD31.mp4">၄။ Character is Power (မဂၤလာဒုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-31/05-UNyanissara-DVD31.mp4">၅။ ရုပ္သာအို၍ ဥာဏ္ပညာ မအို (၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-31/06-UNyanissara-DVD31.mp4">၆။ ရုပ္သာအို၍ ဥာဏ္ပညာ မအို (၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">တရားမွ်တျခင္း၊ ၿငိမ္းခ်မ္းျခင္း၊ 
								ညီညြတ္ျခင္းႏွင့္ အတူလက္တြဲေနထိုင္ျခင္း</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-32/01-UNyanissara-DVD32.mp4">၁။ တရားမွ်တျခင္း၊ 
								ၿငိမ္းခ်မ္းျခင္း၊ ညီညြတ္ျခင္းႏွင့္ 
								အတူလက္တြဲေနထိုင္ျခင္း (၈-၉-၂၀၁၁ - မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-32/02-UNyanissara-DVD32.mp4">၂။ စိတ္ကိုယဥ္ေက်းေအာင္ ဆုံးမနည္း 
								(၁၂-၁၀-၂၀၁၁ -ေတာင္ဥကၠလာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-32/03-UNyanissara-DVD32.mp4">၃။ ဉာဏ္ထက္သူအတြက္ ဗုဒၶမိန္႕ခြန္း 
								(၁၆-၁၀-၂၀၁၁ - အမရပူရ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-32/04-UNyanissara-DVD32.mp4">၄။ အစြမ္းသတၱိငည္ ကိုယ္က်င့္တရား 
								(၂၀၁၁ - တမ္မေတာ္ေဆးတကၠသိုလ္၊ မဂၤလာဒုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-32/05-UNyanissara-DVD32.mp4">၅။ အာယုဒါန (ပုသိမ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၃)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ဓါတ္တူရာေပါင္း</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-33/01-UNyanissara-DVD33.mp4">၁။ ေဇတဝန္မွာ ျပန္ဆုံၾကပါစို႕ 
								(၁၂-၁၀-၂၀၁၁ - ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-33/02-UNyanissara-DVD33.mp4">၂။ အကန္းကမာၻကို ဥာဏ္မ်က္လုံး 
								ေပးသူ (၈-၁၁-၂၀၁၁ - မရမ္းကုန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-33/03-UNyanissara-DVD33.mp4">၃။ ခႏီ ၱ (၂၅-၁၁-၂၀၁၁ - ေတာင္ဒဂုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-33/04-UNyanissara-DVD33.mp4">၄။ ဓါတ္တူရာေပါင္း (၃-၁၂-၂၀၁၁ - 
								တာေမြ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၄)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ၿငိမ္းခ်မ္းေရး</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-34/01-UNyanissara-DVD34.mp4">၁။ ၿငိမ္းခ်မ္းေရး (၂၁-၁၁-၂၀၁၁ - 
								ဗိုလ္တေထာင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-34/02-UNyanissara-DVD34.mp4">၂။ မဟာေဗာဓိပင္ေအာက္က ဗုဒၶဂါယာ 
								English (၂-၁၂-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-34/03-UNyanissara-DVD34.mp4">၃။ ျမတ္ဗုဒၶ၏ ခႏီ ၱဝါဒ (၅-၁၂-၂၀၁၁ 
								- လသာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-34/04-UNyanissara-DVD34.mp4">၄။ ေဒါန၏ ၾသဝါဒ (၉-၁၂-၂၀၁၁ 
								-စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-34/05-UNyanissara-DVD34.mp4">၅။ ခႏီ ၱပါရမီ (၁၀-၁၂-၂၀၁၁ - 
								ကြမ္းၿခံကုန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၅)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ေဒါန၏တစ္ခြန္းေသာစကား</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-35/01-UNyanissara-DVD35.mp4">၁။ စိတ္ကိုယဥ္ေက်းေအာင္ဆုံးမၾက 
								(၁၂-၁၀-၂၀၁၁ ေတာင္ဥကၠလာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-35/02-UNyanissara-DVD35.mp4">၂။ ဗာဟိယသုတၱန္ တရားေတာ္ 
								(၁၂-၁-၂၀၁၁&nbsp;&nbsp; ျဖဴးမဟာစည္သာနာ့ရိပ္သာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-35/03-UNyanissara-DVD35.mp4">၃။ ေဒါနပုဏၰားဓါတ္ေတာ္ဝင္ခန္း 
								(၂၈-၁-၂၀၁၁)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-35/04-UNyanissara-DVD35.mp4">၄။ ဗုဒၶ၏ ခႏီ ၱတရား (၂၄-၁-၂၀၁၂ - 
								ဆူးေလေစတီ -ရာျပည္႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-35/05-UNyanissara-DVD35.mp4">
								၅။ ေဒါန၏ တစ္ခြန္းေသာစကား 
								(ေယာေက်ာင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">DVD အမွတ္စဥ္ (၃၆)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ဗုဒၶရတနာ</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-36/01-UNyanissara-DVD36.mp4">၁။ ဗုဒၶရတနာ (၁) (၂၂-၃-၂၀၁၁ - 
								ဖားကန္႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-36/02-UNyanissara-DVD36.mp4">၂။ ဗုဒၶရတနာ (၂) (၂၃-၃-၂၀၁၁ - 
								ဖားကန္႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-36/03-UNyanissara-DVD36.mp4">၃။ ဗုဒၶရတနာ (၃) (၂၃-၃-၂၀၁၁ - 
								ဖားကန္႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-36/04-UNyanissara-DVD36.mp4">၄။ ဗုဒၶရတနာ (၄) ဓမၼသည္ 
								အခ်ိန္တိုင္းတြင္ရွိသည္ (၂၄-၃-၂၀၁၁ - ဖားကန္႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္(၃၇)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-37/1-UNyanissara-DVD37.mp4">
								၁။ ေဒါနပုဏၰားေျပာေသာၿငိမ္းခ်မ္းေရးစကား 
								(၂၃.၁၂.၂၀၁၁-သဃၤန္းကၽြန္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-37/2-UNyanissara-DVD37.mp4">
								၂။ သည္းခံျခင္းႏွင့္ စြန္ ့လႊတ္ျခင္း (၂၉.၁.၂၀၁၂- 
								လမ္းမေတာ္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-37/3-UNyanissara-DVD37.mp4">
								၃။ေအာင္ျမင္ျခင္းအေၾကာင္း (၁၂.၂.၂၀၁၂- က်ိဳကၠဆံ)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-37/4-UNyanissara-DVD37.mp4">
								၄။ ေအာင္ျမင္ျခင္း(ေရႊဘံုသာေဆးအလွဴေတာ္) 
								(၁၈.၂.၂၀၁၂-ေရႊဘံုသာလမ္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-37/5-UNyanissara-DVD37.mp4">
								၅။ ေရႊတိဂံုေစတီေတာ္ျမတ္ႀကီး၏သမိုင္း (၁၉.၂.၂၀၁၂- 
								ျပည္သူ ့ဥယ်ာဥ္)</a><br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								အမွတ္စဥ္(၃၉)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-39/01-UNyanissara-DVD39.mp4">
								၁။ သတၱဌာန ခုနစ္ပတ္ျဖစ္စဥ္ ဗုဒၶ၀င္</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-39/02-UNyanissara-DVD39.mp4">
								၂။ သဘိယသုတၱန္ (၁) (မႏၲေလး)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-39/03-UNyanissara-DVD39.mp4">
								၃။ သဘိယသုတၱန္ (၂) (မႏၲေလး)</a><br>
								၄။ သဘိယသုတၱန္ (၃) (မႏၲေလး)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-39/05-UNyanissara-DVD39.mp4">
								၅။ သဘိယသုတၱန္ (၄) (မႏၲေလး)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-39/06-UNyanissara-DVD39.mp4">
								၆။ သဘိယသုတၱန္ (၅) (မႏၲေလး)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-39/07-UNyanissara-DVD39.mp4">
								၇။ သဘိယသုတၱန္ (၆) (မႏၲေလး)</a><br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								အမွတ္စဥ္(၄၀)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-40/01-UNyanissara-DVD40.mp4">
								၁။ ေႏြဦးေဆာင္းေႏွာင္း လတေပါင္း</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-40/02-UNyanissara-DVD40.mp4">
								၂။ တပို႔တြဲလျပည့္ ၾသ၀ါဒပါတိေမာက္အခါေတာ္ေန ့</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-40/03-UNyanissara-DVD40.mp4">
								၃။ ႏွစ္ခြန္းေသာစကား</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-40/04-UNyanissara-DVD40.mp4">
								၄။ ျမတ္ေရႊတိဂံု</a><br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								အမွတ္စဥ္(၄၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-41/01-UNyanissara-DVD41-2-3-2012.mp4">
								၁။ အဂၢဒါန သဗၺဒါန (၂.၃.၂၀၁၂-ၿမိဳင္ၿမိဳ ့)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-41/02-UNyanissara-DVD41-5-3-2012.mp4">
								၂။ ဓမၼ၀ိဒိႏွင့္ေအာင္ျမင္ႏိုင္ၾကပါေစ 
								(၅.၃.၂၀၁၂-မႏၲေလး)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-41/03-UNyanissara-DVD41-8-3-2012.mp4">
								၃။ ေအာင္ျမင္ျခင္းဟူသည္ (၈.၃.၂၀၁၂- မႏၲေလး)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-41/04-UNyanissara-DVD41-9-3-2012.mp4">
								၄။ အပၸမာဒ (၉.၃.၂၀၁၂- မႏၲေလး)</a><br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								အမွတ္စဥ္(၄၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-42/01-UNyanissara-DVD42.mp4">
								၁။ ရဟန္း၀တ္ရျခင္းအေၾကာင္းတရားေလးပါး (၂.၅.၂၀၁၂ - 
								ေဒါပံု)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-42/02-UNyanissara-DVD42.mp4">
								၂။ ဥပစာရာေထရီ၏အစြမ္းသတၱိ (၃.၅.၂၀၁၂ - မဂၤလာေစ်း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-42/03-UNyanissara-DVD42.mp4">
								၃။ ကဆုန္လျပည့္ဗုဒၶေန ့ (၅.၅.၂၀၁၂ - ဒဂံုၿမိဳ 
								့သစ္ေျမာက္ပိုင္း)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-42/04-UNyanissara-DVD42.mp4">
								၄။ အဆူဆူဆံုးမၾသ၀ါဒ (၁၀.၂.၂၀၁၂ - သီရိမဂၤလာေစ်း)</a><br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								အမွတ္စဥ္ (၄၃)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-43/01-UNyanissara-DVD43.mp4">
								၁။ စြမ္းေဆာင္ရွင္အမ်ိဳးသမီးမ်ား (၄.၅.၂၀၁၂ - 
								မဂၤလာေတာင္ညြန္႔)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-43/02-UNyanissara-DVD43.mp4">
								၂။ ဗဟုိစည္အထူးတရားပြဲ (၁၁.၅.၂၀၁၂)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-43/03-UNyanissara-DVD43.mp4">
								၃။ အပၸမာဒ (၁၃.၅.၂၀၁၂ - အင္းစိန္)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-43/04-UNyanissara-DVD43.mp4">
								၄။ ဘဝအရႈပ္ေတာ္ရွင္းႏိုင္ပါေစ (၃၁.၅.၂၀၁၂ - 
								ဒဂံုျမိဳ႕သစ္/အေရွ႕ပိုင္း)</a><br>
&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">****dhamma talks uploaded and 
								published on 23 March 2013****</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၄၄)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-44/01-UNyanissara-DVD44.mp4">၁။ ျမတ္စြာဘုရားေပးေသာ ၾသဝါဒ (၉-၂-၂၀၁၂ - 
								ဗိုလ္စိန္မွန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-44/02-UNyanissara-DVD44.mp4">၂။ ႂကြက္ေသတစ္ခု အရင္းျပဳ 
								(၁၈-၂-၂၀၁၂ - ေကာ့ေသာင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-44/03-UNyanissara-DVD44.mp4">၃။ သက္ေတာ္(၇၅)ႏွစ္ျပည္႕ 
								ဝိဇာတမဂၤလာ (၆-၃-၂၀၁၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-44/04-UNyanissara-DVD44.mp4">၄။ သက္ေတာ္(၇၅)ႏွစ္ျပည္႕ 
								ဝိဇာတမဂၤလာ (၇-၃-၂၀၁၂)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-44/05-UNyanissara-DVD44.mp4">၅။ ဘဝအရႈပ္ကို ဘယ္လိုရွင္းမလဲ 
								(၁၇-၅-၂၀၁၂ - သနပ္ပင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၄၅)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-45/01-UNyanissara-DVD45.mp4">၁။ ေဒါနၾသဝါဒ (၁၆-၂-၂၀၁၂ - ေကာ့ေသာင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-45/02-UNyanissara-DVD45.mp4">၂။ တံခိတၱေဒသနာ (၁၇-၂-၂၀၁၂ - 
								ေကာ့ေသာင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-45/03-UNyanissara-DVD45.mp4">၃။ ၿငိမ္းခ်မ္းေရးႏွင့္ ညီညြတ္ေရး 
								(၁-၇-၂၀၁၂ - ေတာ္ဝင္စင္တာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-45/04-UNyanissara-DVD45.mp4">၄။ ေရႊစည္းခုံ ေစတီေတာ္ 
								ေျမာက္ကၽြန္းသို႕ ႂကြပါၿပီး (၃၁-၇-၂၀၁၂ - 
								မရမ္းကုန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-45/05-UNyanissara-DVD45.mp4">၅။ သက္ေသတစ္ခု အရင္းျပဳ 
								(၁-၈-၂၀၁၂ 
								- လိႈင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၄၆)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-46/01-UNyanissara-DVD46.mp4">၁။ မြန္ျမတ္ေသာ ေအာင္ျမင္ျခင္း (၂၉-၂-၂၀၁၂ - 
								ပြင့္ျဖဴ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-46/02-UNyanissara-DVD46.mp4">၂။ ခြင့္လႊတ္ျခင္း၊ သည္းခံျခင္း၊ 
								ဝန္ခံျခင္း၊ မာန္ကို ေမ့ေဖ်ာက္ျခင္း (၃၀-၇-၂၀၁၁ - 
								စကၤာပူ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-46/03-UNyanissara-DVD46.mp4">၃။ ႏွလုံးသားရဲ႕ အရည္အျခင္း 
								(၃၁-၇-၂၀၁၁ - စကၤာပူ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-46/04-UNyanissara-DVD46.mp4">၄။ ေမတၱာဟူသည္ မိခင္စိတ္ထားမ်ိဳးပါ 
								(၁၅-၅-၂၀၁၂ - ေက်ာက္ႀကီး - ပဲခူး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၄၇)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">ဗိုလ္စိန္မွန္းသီတဂူ 
								အေထာက္အကူျပဳအဖြဲ႕ ဓမၼပူဇာ သဘငါတြင္ 
								ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-47/01-UNyanissara-DVD47.mp4">၁။ ဓမၼ အက်ိဳးေက်းဇူး (ဗိုလ္စိန္မွန္ - ဗဟန္း) 
								(ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-47/02-UNyanissara-DVD47.mp4">
								၂။ ဓမၼ အက်ိဳးေက်းဇူး (ဗိုလ္စိန္မွန္ - ဗဟန္း) 
								(ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-47/03-UNyanissara-DVD47.mp4">
								၃။ သာမဂၢီ သုခ (ဗိုလ္စိန္မွန္ - 
								ဗဟန္း) (ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-47/04-UNyanissara-DVD47.mp4">
								၄။ သာမဂၢီ သုခ (ဗိုလ္စိန္မွန္ - 
								ဗဟန္း) (ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-47/05-UNyanissara-DVD47.mp4">
								၅။ ဧရာဝတီမွာ ရြာတဲ့ ရတနာမိုး 
								(ဗိုလ္စိန္မွန္ - ဗဟန္း)
								</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-47/06-UNyanissara-DVD47.mp4">
								၆။ ျမတ္ဘုရားေပးေသာ ၾသဝါဒ&nbsp; 
								(ဗိုလ္စိန္မွန္ - ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၄၈)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-48/01-UNyanissara-DVD48.mp4">၁။ သည္းခံၾကပါ (၂၀-၂-၂၀၁၂ - တာခ်ီလိတ္) 
								(ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-48/01-UNyanissara-DVD48-2.mp4">၁။ သည္းခံၾကပါ (၂၀-၂-၂၀၁၂ - တာခ်ီလိတ္) 
								(ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-48/02-UNyanissara-DVD48.mp4">၂။ ဗာဟိယ မေထရ္ (၂၁-၂-၂၀၁၂ - 
								တာခ်ီလိတ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-48/03-UNyanissara-DVD48.mp4">၃။ ၾသဝါဒ အႏုေမာဒနာ (၃၁-၁၂-၂၀၁၀ - 
								ျမစ္ႀကီးနား)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-48/04-UNyanissara-DVD48.mp4">၄။ တိုက္ပြဲႏွင့္ ေအာင္ပြဲ 
								(၂၆-၁-၂၀၀၉ - ထိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-48/05-UNyanissara-DVD48.mp4">၅။ ဗုဒၶ၏ ရတနာ (၇-၅-၂၀၀၉ - 
								ၾကည္႕ျမင္တိုင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၄၉)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-49/01-UNyanissara-DVD49.mp4">၁။ ျမင့္ျမတ္ေသာ ေအာင္ျမင္းျခင္း (၂၆-၂-၂၀၁၂ - 
								ေအာင္သေျပလမ္း - ယုဇန ပလာဇာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-49/02-UNyanissara-DVD49.mp4">၂။ ဗုဒၶကို ဦးညႊတ္ျခင္းႏွင့္ 
								ဓမၼကိုၾကားရျခင္းသည္ ကံေကာင္းသည္ (၈-၁၀-၂၀၀၉ - 
								ပြင့္ျဖဴ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-49/03-UNyanissara-DVD49.mp4">၃။ ဗ်ႆန ငါးပါး (၃-၇-၂၀၀၈ - 
								ထိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၅၀)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-50/01-UNyanissara-DVD50.mp4">၁။ ေတာင္းပန္ျခင္းရဲ႕ ေက်းဇူး (ၾသဝါဒ) (၁၉-၂-၂၀၁၀ 
								- ထားဝယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-50/02-UNyanissara-DVD50.mp4">၂။ အခ်ိန္ႏွင့္ အလုပ္ (၂၅-၂-၂၀၁၃ - 
								သဃၤန္းကၽြန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-50/03-UNyanissara-DVD50.mp4">၃။ ရွင္သီဝီလိ ဝတၳဳ (၂၈-၉-၂၀၀၁ - 
								မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၅၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-51/01-UNyanissara-DVD51(1-9-2012A).mp4">၁။ ကမၼနိယာမ (၁-၉-၂၀၁၂ - ျမင္းၿခံ) 
								(ပ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-51/02-UNyanissara-DVD51(1-9-2012B).mp4">
								၂။ ကမၼနိယာမ (၁-၉-၂၀၁၂ - ျမင္းၿခံ) 
								(ဒု)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-51/03-UNyanissara-DVD51(3-9-2012).mp4">
								၃။ အရႈပ္ကို ဘယ္လိုရွင္းမလဲ 
								(၃-၉-၂၀၁၂ - မႏ ၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-51/04-UNyanissara-DVD51(27-9-2012).mp4">
								၄။ ကင္မြန္းေတာ္ရြာ ဓမၼဒူတ ခရီး 
								(၂၇-၉-၂၀၁၂ - စစ္ကိုင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၅၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-52/01-UNyanissara-DVD52.mp4">၁။ ခ်မ္းေျမ႕ေပ်ာ္ရႊင္စြာ ေနႏိုင္ၾကပါေစ 
								(၃၀-၁၁-၂၀၁၂ - လမ္းမေတာ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-52/02-UNyanissara-DVD52.mp4">၂။ အိမ္တြင္းေရးအရႈပ္ကို ဓမၼာျဖင့္ 
								ရႈင္းပါ (၃၁-၁၀-၂၀၁၂ - လမ္းမေတာ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-52/03-UNyanissara-DVD52.mp4">၃။ အကိထၳိဇာတ္ေတာ္ 
								(ေစတနာသမာၻရဝတ္အသင္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၅၃)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-53/01-UNyanissara-DVD53.mp4">၁။ ရန္ၿငိဳးေျပေၾကာင္း၊ အက်င့္ေကာင္း (၉-၁၁-၂၀၁၂ - 
								ေက်ာက္မဲ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-53/02-UNyanissara-DVD53.mp4">၂။ ေမတၱာ (၁) (၁၆-၁၁-၂၀၁၂ - 
								ေရႊဆည္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-53/03-UNyanissara-DVD53.mp4">၃။ ေမတၱာ (၂) (၁၇-၁၁-၂၀၁၂ - 
								က်ယ္ေဂါင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-53/04-UNyanissara-DVD53.mp4">၄။ သံသရာမွ လြတ္ေျမာက္ေၾကာင္း 
								(၂၄-၁၁-၂၀၁၂ - ပုဇြန္ေတာင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၅၄)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-54/01-UNyanissara-DVD54.mp4">
								<font size="4">၁။ အက်ိဳးရွိသည္၌ 
								ကၽြမ္းက်င္ၾကစမ္းပါ (၈-၁၂-၂၀၁၂ - ရန္ကင္း)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-54/02-UNyanissara-DVD54.mp4">
								<font size="4">၂။ ၾသဃထရနသုတၱံ (၂၅-၁၁-၂၀၁၂ - 
								တာေမြ)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-54/03-UNyanissara-DVD54.mp4">
								<font size="4">၃။ ျမတ္ဗုဒၶသရီပူဇာ (သာမည - ဘားအံ)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္ (၅၅)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-55/01-UNyanissara-DVD55.mp4">
								<font size="4">၁။ စိတ္ (၂၀-၁၂-၂၀၁၂ - 
								မဂၤလာေတာင္ညြန္႔)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-55/02-UNyanissara-DVD55.mp4">
								<font size="4">၂။ သစၥာတရားကို 
								ထိန္းသိမ္းေစာင့္ေရွာက္ျခင္း (၃-၁-၂၀၁၃- 
								သာသနာ့တကၠသိုလ္ - ရန္ကုန္)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-55/03-UNyanissara-DVD55.mp4">
								<font size="4">၃။ ေဒဝတိကသုတၱံ (၇-၁-၂၀၁၃ - 
								ေတာင္ဥကၠလာပ)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-55/04-UNyanissara-DVD55.mp4">
								<font size="4">၄။ အေကာင္းေလးပါး (၉-၁-၂၀၁၃ - 
								အင္းစိန္)</font></a></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">အမွတ္စဥ္(၅၆)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-56/01-UNyanissara-DVD56.mp4">၁။ ဗုဒၶဂါယာ မဟာေျမျမတ္၌ ပိဋကတ္သံုးပံုရြတ္ဖတ္ 
								ပူေဇာ္ပြဲ(၁) (၂-၁၂-၂၀၁၂ အိႏိၵယႏိုင္ငံ)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-56/02-UNyanissara-DVD56.mp4">၂။ ဗုဒၶဂါယာ မဟာေျမျမတ္၌ ပိဋကတ္သံုးပံုရြတ္ဖတ္ 
								ပူေဇာ္ပြဲ(၂) (၃-၁၂-၂၀၁၂ အိႏိၵယႏိုင္ငံ)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-56/03-UNyanissara-DVD56.mp4">၃။သာသနာေတာ္၌ 
								ေက်ာင္းတိုက္မ်ားျဖစ္ေပၚလာျခင္းအေၾကာင္း 
								(၇-၁၂-၂၀၁၂ အိႏိၵယႏိုင္ငံ)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၅၇)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/01-UNyanissara-DVD57.mp4">၁။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၃-၄-၂၀၁၃ နံနက္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/02-UNyanissara-DVD57.mp4">၂။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၃-၄-၂၀၁၃ ညေန)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/03-UNyanissara-DVD57.mp4">၃။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၄-၄-၂၀၁၃ နံနက္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/04-UNyanissara-DVD57.mp4">၄။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၄-၄-၂၀၁၃ ညေန)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/05-UNyanissara-DVD57.mp4">၅။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၅-၄-၂၀၁၃ နံနက္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/06-UNyanissara-DVD57.mp4">၆။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၅-၄-၂၀၁၃ ညေန)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/07-UNyanissara-DVD57.mp4">၇။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၆-၄-၂၀၁၃ နံနက္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/08-UNyanissara-DVD57.mp4">၈။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၆-၄-၂၀၁၃ ညေန)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/09-UNyanissara-DVD57.mp4">၉။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၇-၄-၂၀၁၃ နံနက္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-57/10-UNyanissara-DVD57.mp4">၁၀။ သႀကၤန္တြင္း သတိပ႒ာန္ (၁၇-၄-၂၀၁၃ ညေန)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၅၈)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-58/01-UNyanissara-DVD58-12-04-2013-ThinGanKyun.mp4">၁။ဉာဏ္ပညာၾကီးက်ယ္ျခင္း၏ အက်ဳိးေက်းဇူး (၁၂-၄-၂၀၁၃ 
								သဃၤန္းကၽြန္း)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-58/02-UNyanissara-DVD58-14-12-2012-MaYanGone.mp4">၂။ သတိတရားလက္ကိုင္ထား (၁၄-၁၂-၂၀၁၂ မရမ္းကုန္း)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-58/03-UNyanissara-DVD58-12-12-2012-DaGon.mp4">၃။ ပင္လယ္ႏွင့္တူေသာစိတ္ (၁၂-၁၂-၂၀၁၂ ဒဂံု/ေတာင္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-58/04-UNyanissara-DVD58-15-1-2013.mp4">၄။ ေလာကဓါတ္ တစ္ခုလံုး အျမတ္ဆံုးဥစၥာ (၁၅-၁-၂၀၁၃ 
								က်ဳိက္ထို)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၅၉)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-59/01-UNyanissara-DVD59.mp4">၁။ မဟာသာရဇာတ္ (၂-၄-၂၀၁၃ ပန္းဘဲတန္း)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-59/02-UNyanissara-DVD59.mp4">၂။ ဂုဏဇာတ္ေတာ္ (၂၉-၄-၂၀၁၃ မဂၤလာဒံု)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-59/03-UNyanissara-DVD59.mp4">၃။ တိတၳိရဇာတ္ေတာ္ (၃၀-၄-၂၀၁၃ ဗဟန္း)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၆၀)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-60/01-UNyanissara-DVD60.mp4">၁။ အမ်ဳိးဘာသာ သာသနာ ထိန္းသိမ္းေစာင့္ေရွာက္ေရး 
								ၾသ၀ါဒခံယူပြဲ - ေအာင္ဆန္းတပ္ဦးေက်ာင္း၊ေအာင္ဆန္း 
								(၂၇-၆-၂၀၁၃)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-60/02-UNyanissara-DVD60.mp4">၂။ မဟာသပယ အႏွစ္ခ်ဳပ္ - 
								သီတဂူကမာၻ႕ဗုဒၶတကၠသိုလ္(ရန္ကုန္)ဖြင့္ပြဲအခမ္းအနား 
								(၂၃-၆-၂၀၁၃)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-60/03-UNyanissara-DVD60.mp4">၃။ ေမ်ာက္၀င္ေနျပီ သတိထား - ဟသၤာတ (၄-၄-၂၀၁၃)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၆၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-61/01-UNyanissara-DVD61.mp4">၁။ ဗုဒၶသာသနာေတာ္၏အမ်ဳိးေကာင္းသမီးရတနာမ်ား 
								(၃၀-၆-၂၀၁၃ ဇမၺဴသီရိဗိမာန္ေတာ္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-61/02-UNyanissara-DVD61.mp4">၂။ ေမ်ာက္ဖမ္းၾကတဲ့ပြဲ (၂၈-၅-၂၀၁၃ သနပ္ပင္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-61/03-UNyanissara-DVD61.mp4">၃။ ေဗာဓိပင္ေအာက္ကတရား (၅-၁၂-၂၀၁၂ အိႏိၵယႏိုင္ငံ၊ 
								ဘီယာျပည္နယ္၊ဂယာၿမိဳ႕)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-61/04-UNyanissara-DVD61.mp4">၄။ သီတဂူ- က်ဳိက္ထိုအာေရာဂ်ဒါနေဆးရံုေတာ္ဖြင့္ပြဲ 
								အခမ္းအနားမွတ္တမ္း(၂၈-၅-၂၀၁၃ က်ဳိက္ထို)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-61/05-UNyanissara-DVD61.mp4">၅။ သီတဂူ(လွဆန္းယဥ္) 
								စကၡဳဒါနမ်က္စိေဆးရံုေတာ္ဖြင့္ပြဲႏွင့္ေရစက္ခ်အခမ္းအနား 
								(၇-၄-၂၀၁၃ ေမာ္လၿမိဳင္ကၽြန္းၿမိဳ႕နယ္)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								<br>
								အမွတ္စဥ္(၆၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-62/01-UNyanissara-DVD62.mp4">၁။ မဟာသာရဇာတ္ (ေက်ာက္ဆည္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-62/02-UNyanissara-DVD62.mp4">၂။ 
								ၿငိမ္းၿငိမ္းခ်မ္းခ်မ္းညီညီညြတ္ညြတ္အတူလက္တြဲေနထိုင္ေရး 
								(၂၆ဘီလမ္း)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-62/03-UNyanissara-DVD62.mp4">၃။ ေသလာေထရီ (၀မ္းတြင္းၿမိဳ႕နယ္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-62/04-UNyanissara-DVD62.mp4">၄။ အိုသည့္တိုင္ေအာင္ေကာင္းသည့္တရား(၄)ပါး 
								(စိုင္းျပင္ၾကီး)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-62/05-UNyanissara-DVD62.mp4">၅။ ၀ဇီရာေထရီ (သဲေတာ)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-62/06-UNyanissara-DVD62.mp4">၆။ အဓိပတိဦးကိုေလးရာျပည့္ (မႏၲေလး)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၆၃)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-63/01-UNyanissara-DVD63.mp4">၁။ ေမတၱာတရားေတာ္(၁) (၂၂-၈-၂၀၁၃ မႏၲေလး)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-63/02-UNyanissara-DVD63.mp4">၂။ ေမတၱာတရားေတာ္(၂) (၂၃-၈-၂၀၁၃ မႏၲေလး)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-63/03-UNyanissara-DVD63.mp4">၃။ ေမတၱာတရားေတာ္(၃) (၂၄-၈-၂၀၁၃ မႏၲေလး)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-63/04-UNyanissara-DVD63.mp4">၄။ ေမတၱာတရားေတာ္(၄) (၂၆-၈-၂၀၁၃ မႏၲေလး)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-63/05-UNyanissara-DVD63.mp4">၅။ ေမတၱာတရားေတာ္(၅) (၂၉-၈-၂၀၁၃ မႏၲေလး)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-63/06-UNyanissara-DVD63.mp4">၆။ ေမတၱာတရားေတာ္(၆) (၃၁-၈-၂၀၁၃ မႏၲေလး)</a><br>
								&nbsp;</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								အမွတ္စဥ္(၆၄)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4"><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-64/01-UNyanissara-DVD64.mp4">၁။ မဟာသမယအႏွစ္ခ်ဳပ္ (သီတဂူ ကမာၻ႕ဗုဒၶတကၠသိုလ္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-64/02-UNyanissara-DVD64.mp4">၂။ ၀ါဆိုသကၤန္းကပ္ (၂၂-၇-၂၀၁၃ သီတဂူ 
								ကမာၻ႕ဗုဒၶတကၠသိုလ္ )</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-64/03-UNyanissara-DVD64.mp4">၃။ ေမတၱာတရားေတာ္ (သီတဂူ ကမာၻ႕ဗုဒၶတကၠသိုလ္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-64/04-UNyanissara-DVD64.mp4">၄။ ဂရုဓမၼတရားေတာ္ (သီတဂူ ကမာၻ႕ဗုဒၶတကၠသိုလ္)</a><br>
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-64/05-UNyanissara-DVD64.mp4">၅။ ကထိန္အလွဴေတာ္ (၁၆-၁၀-၂၀၁၃ သီတဂူ 
								ကမာၻ႕ဗုဒၶတကၠသိုလ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၆၅)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-65/01-UNyanissara-DVD65.mp4">၁။ မလြန္ေစ်းဆန္ လွဴအသင္းႀကီး ဆြမ္းဆန္ေတာ္လွဴပြဲ 
								(၁၅-၉-၂၀၁၃ မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၂။ ေအာင္ျမင္ေၾကာင္းတရား (၄) ပါး (၂၅-၉-၂၀၁၃ 
								မႏၱေလး)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-65/03-UNyanissara-DVD65.mp4">၃။ သစၥာႏွင့္ ေမတၱာတရားေတာ္ (၄-၁၀၀၂၉၁၃ မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-65/04-UNyanissara-DVD65.mp4">၄။ ဗုဒၶ၏တရားေတာ္ျဖင့္ ၿငိမ္းခ်မ္းၾကပါေစ 
								(၁၁-၁၀-၂၀၁၃ မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-65/05-UNyanissara-DVD65.mp4">၅။ ၿငိမ္းခ်မ္းတဲ့ႏိုင္ငံေတာ္တစ္ခုအတြက္ 
								ေမွ်ာ္လင့္ခ်က္မ်ား (၁၂-၁၀-၂၀၁၃ မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၆၆)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-66/01-UNyanissara-DVD66.mp4">၁။ ဝါဆို သကၤန္းကပ္ (၁၆-၉-၂၀၁၃ - 
								သီတဂူဗုဒၶတကၠသိုလ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-66/02-UNyanissara-DVD66.mp4">၂။ ဝိပႆနာေဒသနာ (၂၂-၇-၂၀၁၃ - အမရပူရၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-66/03-UNyanissara-DVD66.mp4">၃။ ဝဇီရာေထရီ (၁-၈-၂၀၁၃ - သဲေတာၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-66/04-UNyanissara-DVD66.mp4">၄။ သစၥာနဲ႕ ေမတၱာ (ေခ်ာက္ၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၆၇)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-67/01-UNyanissara-DVD67.mp4">၁။ အပရိဟာနိယသုတၱန္ (၁၁-၁၁-၂၀၁၃ - ေတာင္ဒဂုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-67/02-UNyanissara-DVD67.mp4">၂။ ဧရာဝတီ စိတ္ဓါတ္ (၃၁-၁၂-၂၀၁၃ - ေျမာက္ဒဂုံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-67/03-UNyanissara-DVD67.mp4">၃။ အိုသည္႕တိုင္ေအာင္ ေကာင္းမည္႕ တရားေလးပါး 
								(၁၈-၁၂-၂၀၁၃ - ပန္းဘဲတန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၆၈)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-68/01-UNyanissara-DVD68.mp4">၁။ အမ်ိဳးဘာသာ သာသနာေစာင့္ေရွာက္ေရးအဖြဲ႕ 
								အထက္ျမန္မာျပည္ မႏၱေလးၿမိဳ႕ ဖြဲ႕စည္ျခင္းႏွင့္ 
								ၾသဝါဒ မိန္႕ခြန္း (၁၅-၁-၂၀၁၄ မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-68/02-UNyanissara-DVD68.mp4">၂။ ေလာကရဲ႕ အရႈပ္ (၈-၁၁-၂၀၁၃ - ေပါင္းတည္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-68/03-UNyanissara-DVD68.mp4">၃။ ေမ်ာက္ဖမ္းၾကရေအာင္ (၁၀-၁၁-၂၀၁၃- မရမ္းကုန္း၊ 
								ရန္ကုန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၆၉)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-69/DVD-69-Title-01-UNyanissara.mp4">
								၁။ ၿငိမ္းခ်မ္းေရး (၆-၁၀-၂၀၁၃ - သံတြဲ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-69/DVD-69-Title-02-UNyanissara.mp4">
								၂။ ေမ်ာက္ဖမ္းႏိုင္မွ အာလုံး လြတ္လပ္ၾပမယ္ 
								(၇-၁၀-၂၀၁၃ - သံတြဲ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-69/DVD-69-Title-03-UNyanissara.mp4">
								၃။ ပရိဟာနိယ အႏွစ္ခ်ဳပ္ (၁၈-၁၀-၂၀၁၃ - ရန္ကုန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-69/DVD-69-Title-04-UNyanissara.mp4">
								၄။ မဟာသက်မုနိရုပ္ပြားေတာ္ႀကီး (၂၂-၁၀-၂၀၁၃ - 
								ၾကည္႕ျမင္တိုင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၀)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-70/01-UNyanissara-DVD70.mp4">၁။ ဗုဒၶစာေပမွ ေတြ႕ရွိရေသာ ေရွးေခတ္ေဟာင္း 
								ပါလီမန္ဒီမိုကေရစီစနစ္ (မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-70/02-UNyanissara-DVD70.mp4">၂။ မိတ္ေကာင္းႏွင့္ စိတ္ေကာင္း (မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-70/03-UNyanissara-DVD70.mp4">၃။ ဓမၼဝိဒီ (မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-71/DVD-71-Title-01-UNyanissara.mp4">
								၁။ ဘဝကို ေလးနက္စြာေတြးတတ္သူ (ေရႊဘုံသာလမ္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-71/DVD-71-Title-02-UNyanissara.mp4">
								၂။ ေညာင္ပင္ေအာက္က အေျခခံစည္းမ်ဥ္း(ၾသဘာလမ္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-71/DVD-71-Title-03-UNyanissara-Ah-Kwint-Ah-Ray.mp4">
								၃။ အခြင့္အေရး (မတၱရာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-72/DVD-72-Title-01-UNyanissara.mp4">
								၁။ ၿငိမ္းခ်မ္းစြာေနေၾကာင္း အက်င့္ေကာင္း 
								(၃၀-၁-၂၀၁၄)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-72/DVD-72-Title-02-UNyanissara.mp4">
								၂။ မဂၤလာတရားေတာ္ (၂၁-၂-၂၀၁၄ - မဂၤလာေစ်း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-72/DVD-72-Title-03-UNyanissara.mp4">
								၃။ ၿငိမ္းခ်မ္း ညီညြတ္စြာ အားလုံး 
								လက္တြဲေနထိုင္သြားၾကေစ (မေကြးၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-72/DVD-72-Title-03-2-UNyanissara.mp4">
								၃-၂။ ၿငိမ္းခ်မ္း ညီညြတ္စြာ အားလုံး 
								လက္တြဲေနထိုင္သြားၾကေစ (မေကြးၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-72/DVD-72-Title-04-UNyanissara.mp4">
								၄။ ၿငိမ္းခ်မ္းေရး ညီညြတ္ေရးႏွင့္ 
								အတူလက္တြဲေနထိုင္ေရး (ေက်ာက္ဆည္ၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-72/DVD-72-Title-05-UNyanissara.mp4">
								၅။ ၿငိမ္းခ်မ္းေရး ညီညြတ္ေရးႏွင့္ 
								အတူလက္တြဲေနထိုင္ေရး ၁၃၀၀ျပည္႕ အေရးေတာ္ပုံ မႏ 
								ၱေလးအာဇာနည္(၁၇)ဦး (၇၅)ႏွစ္ျပည္႕ အထိမ္းအမွတ္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၃)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-73/DVD-73-Title-01-UNyanissara.mp4">
								၁။ သမၼဂၢီဂုဏ္ျပဳပူဇာ (၃၀-၁-၂၀၁၄ - ဗဟန္းၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-73/DVD-73-Title-02-UNyanissara.mp4">
								၂။ ေနတတ္ေအာင္ေနၾကပါ (၁-၄-၂၀၁၄ - ဒဂုံၿမိဳ႕နယ္၊ 
								ေယာမင္းႀကီးရပ္ကြက္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-73/DVD-73-Title-03-UNyanissara.mp4">
								၃။ ဘဝ၏ ရည္ရြယ္ခ်က္ (၇) ပါး (၆-၄-၂၀၁၄ - 
								စမ္းေခ်ာင္းၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-73/DVD-73-Title-04-UNyanissara.mp4">
								၄။ အရႈပ္အေထြး (၁၈-၂-၂၀၁၄ - ေဒါပုံၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၄)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၁။ သီတဂူဆရာေတာ္၏ မိန္႕ခြန္း၊ 
								ပၪၥမအႀကိမ္ ဂိုဏ္ေပါင္းစုံ သံဃာ့အစည္းအေဝး 
								(၁၂-၅-၂၀၁၄-&nbsp; ကမာၻေအး)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၂။ ကဆုန္လျပည္႕ ဗုဒၶေန႕ (၁၃-၅-၂၀၁၄ 
								- သီတဂးဗုဒၶတကၠသိုလ္၊ ရန္ကုန္)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">၃။ ကဆုန္လျပည္႕ ဗုဒၶေန႕ (၁၃-၅-၂၀၁၄ 
								- မဟာသႏိ ၱသုခေက်ာင္းတိုက္၊ ရန္ကုန္)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၅)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-75/DVD-75-Title-01-UNyanissara.mp4">
								၁။ ေဒဝဟိတသုတၱန္ (၈-၁၀-၂၀၁၄ - ဗဟန္းၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-75/DVD-75-Title-02-UNyanissara.mp4">
								၂။ သဗၺညဳေစတီယပူဇာ (၉-၁၀-၂၀၁၄ - 
								သဗၺညဳပထိုးေတာ္ႀကီး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-75/DVD-75-Title-03-UNyanissara.mp4">
								၃။ ဆုတ္ယုတ္လာေသာ ေခတ္ကို ေလ့လာသုံးသပ္ျခင္း 
								(၂၄-၁၀-၂၀၁၄ - ၾကည္႕ျမင္တိုင္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-75/DVD-75-Title-04-UNyanissara.mp4">
								၄။ သံေဝဂကထာ (၈-၁၀-၂၀၁၄ - သကၤန္းကၽြန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၆)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-76/DVD-76-Title-01-UNyanissara.mp4">
								၁။ ျမတ္စြာဘုရား၏ လက္စြဲတရား (၂၈-၉-၂၀၁၄ - 
								ေရႊဘိုၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-76/DVD-76-Title-02-UNyanissara.mp4">
								၂။ အပၸမာဒ (၂-၁၀-၂၀၁၄ - ဒီပဲယင္းၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-76/DVD-76-Title-03-UNyanissara.mp4">
								၃။ သံေဝဂကထာ (၂၈-၁၀-၂၀၁၄ - သကၤန္းကၽြန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-76/DVD-76-Title-04-UNyanissara.mp4">
								၄။ သီတဂူဆရာေတာ္ႏွင့္ ဗုဒၶဂယာ ဘုရားဖူးခရီးစဥ္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၇)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-77/DVD-77-Title-01-UNyanissara.mp4">
								၁။ မာဃႏွင့္ အပၸမာဒ (၄-၁၀-၂၀၁၄ - စကၤာပူႏိုင္ငံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-77/DVD-77-Title-02-UNyanissara.mp4">
								၂။ စိတ္ထိန္း (၅-၁၀-၂၀၁၄ - စကၤာပူႏိုင္ငံ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-77/DVD-77-Title-03-UNyanissara.mp4">
								၃။ ထိႆရဟန္းဝတၳဳ (၂၇-၁၁-၂၀၁၄)</a></font></p>
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
								<font size="4">
								အမွတ္စဥ္(၇၈)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-78/DVD-78-Title-01-UNyanissara.mp4">၁။ ဗုိလ္ခ်ဳပ္ေအာင္ဆန္း 
								ႏွစ္(၁၀၀)ျပည္႕ ေမြးေန႕တရားေတာ္ (၁၃-၂-၂၀၁၅) 
								နတ္ေမာက္ၿမိဳ႕</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-78/DVD-78-Title-02-UNyanissara.mp4">၂။ အရႈပ္အေထြး (၁၈-၂-၂၀၁၄) 
								ေဒါပုံၿမိဳ႕နယ္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-78/DVD-78-Title-03-UNyanissara.mp4">၃။ ဘာနဲ႕ ပူေဇာ္ၾကမွာလဲ 
								(၁၉-၁-၂၀၁၅) ဗဟန္း</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၇၉)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-79/DVD-79-Title-01-UNyanissara.mp4">၁။ ဗုဒၶဓမၼ (၁-၅-၂၀၁၅) Myanmar 
								Evant Part</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-79/DVD-79-Title-02-UNyanissara.mp4">၂။ ဝံသကလီရ ပေစၥကဗုဒၶ (၂၉-၄-၂၀၁၅) 
								မဂၤလာေတာင္ညြန္႕ၿမိဳ႕နယ္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-79/DVD-79-Title-03-UNyanissara.mp4">၃။ အနိဠက႑ပေစၥကဗုဒၶ ဗုဒၶဝင္ 
								(၂၀-၄-၂၀၁၅) ေဒါပုံၿမိဳ႕နယ္</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၈၀)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-80/01-UNyanissara-DVD80.mp4">၁။ ဘဝႀကီးပြားတိုးတက္ေၾကာင္း 
								(၇)ပါး (၃၁-၁၀-၂၀၁၅ - ဗဟန္းၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-80/02-UNyanissara-DVD80.mp4">၂။ စကဝတၱိသုတၱန္ (၃၀-၉-၂၀၁၅ - 
								မႏၱေလး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-80/03-UNyanissara-DVD80.mp4">
								၃။ သံဃာ တစ္ေသာင္း ပူေဇာ္ပြဲ</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-80/04-UNyanissara-DVD80.mp4">
								၄။ အမ်ိဳးေစာင့္ ဥပေဒေအာင္ပြဲတြင္ 
								ေဟာၾကားေသာ ၾသဝါဒ (၄-၁၀-၂၀၁၅ - ရန္ကုန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၈၁)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-81/01-UNyanissara-DVD81.mp4">၁။ အႏုေမာဒနာ တရားေတာ္ (၂၅-၁၁-၂၀၁၅ 
								- ယုဇနပလာဇာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-81/02-UNyanissara-DVD81.mp4">၂။ ပေစၥက ဗုဒၶဝင္ (၁) (၅-၁၂-၂၀၁၅ - 
								အင္းစိန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-81/03-UNyanissara-DVD81.mp4">၃။ ပေစၥက ဗုဒၶဝင္ (၂) (၆-၁၂-၂၀၁၅ - 
								အင္းစိန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၈၂)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-82/01-UNyanissara-DVD82.mp4">၁။ ေစတီထူပါ (ေျမာက္ဥကၠလာ)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-82/02-UNyanissara-DVD82.mp4">၂။ နဂၢဇိပေစၥက ဗုဒၶဝင္ (က်ိဳက္ထို)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-82/03-UNyanissara-DVD82.mp4">၃ သဗၺဳညဳတ (ရန္ကုန္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-82/04-UNyanissara-DVD82.mp4">၄။ ဓမၼေအာင္လံ (ဗဟန္း)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၈၃)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-83/01-UNyanissara-DVD83.mp4">၁။ (၂၉) ဆူေျမာက္ ပေစၥကဗုဒၶဝင္ 
								(၁၃-၁၀-၂၀၁၅ - အင္းစိန္ၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-83/02-UNyanissara-DVD83.mp4">၂။ အိုသည္႕တိုင္ေအာင္ ေကာင္းတဲ့ 
								တရားေလးပါး (၈-၄-၂၀၁၆ - ေရႊျပည္သာၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-83/03-UNyanissara-DVD83.mp4">၃။ ၾသဂသရတနသုတၱန္ (၂၃-၄-၂၀၁၆ - 
								ရန္ကုန္ၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								အမွတ္စဥ္(၈၄)</font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-84/01-UNyanissara-DVD84.mp4">၁။ ျမတ္ဗုဒၶ၏ ေနာက္တုံးေန႕ရက္မ်ား 
								(၂၁-၄-၂၀၁၆ - ပဲခူး)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-84/02-UNyanissara-DVD84.mp4">၂။ ေနနည္းသုံးပါး တရားေတာ္ 
								(က်ိဳက္ထိုၿမိဳ႕နယ္)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-84/03-UNyanissara-DVD84.mp4">၃။ ဓမၼေအာင္လံ (သထုံၿမိဳ႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<a href="http://dhammadownload.com/MP4Library/UNyanissara/DVD-84/04-UNyanissara-DVD84.mp4">၄။ ၾသဂသရနသုတၱန္ (ရန္ကုန္ၿမို႕)</a></font></p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0">
	ရန္ကုန္တိုင္းေဒသႀကီးအစိုးရအဖြဲ႕မွ ႀကီးမႈးက်င္းပေသာ ႏွစ္သစ္ကူး 
	တရားအလွဴေတာ္ဓမၼသဘင္</p>
<p style="margin-top: 0; margin-bottom: 0">
	<a href="http://dhammadownload.com/MP4Library/Dr-Nandamalabhivamsa/2018-newyear/001-Dr-Nandamalabhivamsa-2018-1-1-NewYear.mp4">






										<img src="images/Dr-Nandamalabhivamsa-small.gif" width="51" height="62" border="0"> 
	၁-၁-၂၀၁၈ ပါေမာကၡခ်ဳပ္ဆရာေတာ္ႀကီး ဘဒၵႏၲ ေဒါက္တာ နႏၵမာလာဘိဝံသ ေဟာၾကားေတာ္မူေသာ 
	မဂၤလာတရားႏွင့္အညီ ႏိုင္ငံသစ္တည္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0">
	<font size="5" color="#0000FF">
	<a href="http://dhammadownload.com/MP4Library/">
	<span style="font-family: Zawgyi-One">
	<img src="images/UNyanissara-small.gif" width="52" height="65" border="0"> </span>
	</a></font>
	<a href="http://dhammadownload.com/MP4Library/UNyanissara/2018-newyear/002-UNyanissara-2018-1-2-NewYear.mp4">
	၂-၁-၂၀၁၈ သီတဂူဆရာေတာ္ဘုရားႀကီး ဦးဥာဏိႆရ ေဟာၾကားေတာ္မူေသာ 
	အပရိဟာနိယသုတၱန္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0">
	<a href="http://dhammadownload.com/MP4Library/Ashin-Sandadika/2018-newyear/003-AshinSandadika-2018-1-3-NewYear.mp4">
										<img src="images/Ashin-Sandadika-small.gif" border="0"> 
	၃-၁-၂၀၁၈ အရွင္ဆႏၵာဓိက (ေရႊပါရမီေတာရ) ေဟာၾကားေတာ္မူေသာ ေမတၱာစာခ်ဳပ္ျဖင့္သာ 
	ထာဝရၿငိမ္းခ်မ္းေရးရႏိုင္သည္ တရားေတာ္</a></p>
<p style="margin-top: 0; margin-bottom: 0">
	&nbsp;</p>
<p style="margin-top: 0; margin-bottom: 0">
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
								<font size="4">
								<br>
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
<p style="margin-top: 0; margin-bottom: 0" align="left">
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
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font color="#800080">
	<span style="font-family: Times New Roman; font-size: 32pt">Sayadaw U 
	Nyanissara</span></font></div>

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

count = 1035        
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