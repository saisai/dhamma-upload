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
	<font color="#800080"><span style="font-size: 32pt">ေဒါက္တာစႏၵာဝရာဘိဝံသ</span></font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 596px; top: 4px;" id="layer23">
	<img src="images/Dr-Candavara-bhivamsa.gif" width="225" height="250" border="0"></div>






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















<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>






















<div style="position: absolute; width: 980px; height: 11148px; z-index: 21; left: 219px; top: 153px" id="layer24" font="" face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="5">Dr Candavara Bhivamsa</font><font size="4" face="WinTaungyi">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">Pro-Rector</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">International Theravada Buddhist</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">Missionary University, Yangon</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4" face="Zawgyi-One">
								ရန္ကုန္ၿမဳိ႕ အျပည္ျပည္ဆုိင္ရာေထရ၀ါဒ 
								ဗုဒၶသာသနာျပဳတကၠသုိလ္၏ ဒုတိယပါေမာကၡခ်ဳပ္ဆရာေတာ္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">ရန္ကုန္ၿမိဳ႕၊ မိုးကုတ္ ဝိပႆနာ 
								တရားစဥ္ႏွင့္ လုပ္ငန္းစဥ္ျပန္႕ပြားေရး 
								အဖြဲ႕ခ်ဳပ္ႀကီး၏ နာယက၊</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">က်ိဳကၠေလာ့ေစတီေတာ္ျမတ္ႀကီး၏ 
								ၾသဝါဒစရိယဆရာေတာ္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="5" face="Zawgyi-One">က်ဳိကၠေလာ့ 
								ဆရာေတာ္</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="6" face="Zawgyi-One">ေဒါက္တာ ဘဒၵႏၲ 
								စႏၵာဝရာဘိဝံသ<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4" face="Franklin Gothic Medium">M.A; Ph.D</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4" face="Zawgyi-One">ပထမေက်ာ္ ၊ 
								သာသနဓဇ ဓမၼာစရိယ၊ ေစတိယဂၤဏ ဓမၼာစရိယ၊ သက်သီဟ 
								ဓမၼာစရိယ၊ (သ.စ.အ ဓမၼာစရိယ)</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">အဂၢမဟာ ပ႑ိတ</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">အဂၢမဟာဂႏၲဝါစက ပ႑ိတ</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4">မဟာကမၼဌာနစရိယ</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								က်ိဳကၠေလာ့ ပရိယတၱိစာသင္တိုက္</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								မိုးကုတ္ဝိပႆနာ ဓမၼရိပ္သာ</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								က်ိဳကၠေလာ့ေစတီအနီး၊ မဂီလာဒုံ၊ ရန္ကုန္တိုင္း</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဖုန္း - ၀၉၄၅၀၀၅၃၉၁၅</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								၀၉၇၈၀၂၆၇၉၆၄</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								၀၉၄၂၃၃၆၅၁၅၇</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								email:
								<a href="mailto:kyaikkalott1949@gmail.com">
								kyaikkalott1949@gmail.com</a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<a href="http://kyaikkalot.org">
								http://kyaikkalot.org</a> </p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတာ္အား လွဴဒါန္းထားေသာ ဓမၼပူဇာမ်ားကို 
								အေျခခံလွ်က္ ဆရာေတာ္၏ ေမြူရပ္ဇညတိရြာျဖစ္ေသာ 
								ဧရာဝတီတိုင္း ဇလြန္ၿမိဳ႕နယ္ ျမစ္ဝေက်းရြာ၌ ပရဟိတ 
								ေဆးရုံ၊ ေဆးခန္းကို ေဆာက္လုပ္လွဴဒါန္းၿပီၚပါၿပီ။ 
								ယၡဳအခါ ေက်းလက္ေတာရြာမွ ေတာင္သူလယ္သမား 
								ေဒသခံမ်ားအတြက္ အခမဲ့ေဆးကုခန္း အစီအစဥ္ကို 
								စတင္ေဆာင္ရြက္ေနၿပီ ျဖစ္ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတာ္၏ ပရဟိတ က်န္းမာေရးေစာင့္ေရွာက္မႈ 
								လုပ္ငန္းမ်ား အရွည္သျဖင့္ ရပ္တည္ႏိုင္ရန္ 
								ေဆးပေဒသာပင္မ်ား လွဴဒါန္းလိုပါက ေအာက္ပါ 
								ဘဏ္အေကာင့္နံပါတ္ႏွင့္ တယ္လီဖုန္းနံပါတ္မ်ားသို႕ 
								ဆက္သြယ္လွဴဒါန္းႏိုင္ၾကပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								KBZ Bank Account Number: 021-301-02105857901</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတ္ာဖုန္း။&nbsp; ၀၉၄၅၀၀၅၃၉၁၅ ၊ 
								၀၉၇၈၀၂၆၇၉၆၄</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								AYA Bank Account Number: 0166222010002054</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဦးဝင္းျမင့္ (ျမစ္ဝ)၊ ၀၉၃၀၈၄၄၀၃၆၊ ၀၉၇၇၁၂၃၂၈၇၇</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဦးသိန္းစိုး (ျမစ္ဝ) ၊ ၀၉၃၀၈၄၄၀၃၆</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဦးခင္ဝင္း (ျမစ္ဝ)၊ ၀၉၄၅၅၀၇၅၂၇၅</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								**************************************************</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="5">ဆရာေတာ္၏ ေထရုပတၱိ အက်ဥ္း</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<br>
								ဘဒၵႏၲေဒါက္တာစႏၲာ၀ရာဘိ၀ံသ အရွင္သူျမတ္သည္၊ 
								ဖခမည္းေတာ္ ဦးသာဟန္ႏွင့္ မယ္ေတာ္ေဒၚျမတို႕မွ 
								(ေကာဇာသကၠရာဇ္ ၁၃၁၁ခုႏွစ္ တန္ေဆာင္မုန္းလဆန္း ၅ 
								ရက္)၊ ခရစ္ ၁၉၄၉ခု ေအာက္တုိဘာလ ၂၅ရက္ 
								(အဂၤါေန႔တြင္)၊ 
								ဧရာဝတီတိုင္း၊ ဇလြန္ၿမိဳ႕နယ္၊ ျမစ္ဝရြာ၌ မီးရႈးသန္႔စင္ဖြားျမင္ေတာ္မူသည္။ 
								သက္ေတာ္ ၁ဝ ႏွစ္သား အရြယ္တြင္ ႐ွင္သာမေဏ 
								အျဖစ္သို႕ေရာက္႐ွိခဲ့ၿပီး ရွင္သာမေဏ ဘ၀ျဖင့္ပင္ 
								ႏိုင္ငံေတာ္အစိုးရက က်င္းပေသာ ပထမျပန္စာေမးပဲြတြင္ 
								ပထမငယ္ ၊ ပထမလတ္၊ ပထမႀကီးတန္းတို႕ ကို 
								ေအာင္ျမင္ေတာ္ မူလွ်က္ ပထမႀကီးတန္းတြင္ 
								တစ္ႏိုင္ငံလံုး ပထမရ႐ွိ၍ ပထမေက်ာ္ ဘြဲ႕ကို 
								ဆြတ္ခူးရ႐ွိေတာ္ မူခဲ့ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								၁၉၆၉ခု ဧၿပီလတြင္ ဘဒၵႏၲေဇာတိပါလဆရာေတာ္ဘုရားႀကီး 
								ဥပဇၥ်ယ္ျပဳလွ်က္ ပဲခူးၿမိဳ႕ 
								ၾကခတ္ဝိုင္းပရိယတၲိစာသင္တိုက္ႀကီး၌ 
								ပစၥယာႏုဂၢဟဒါယကာႀကီးဦးေအာင္စိန္ ၊ေဒၚရႈရီတို႔၏ 
								အေထာက္အပံ့ျဖင့္ ရဟန္ အျဖစ္သို႕ ေရာက္႐ွိခဲ့ပါသည္။ 
								ပရိယတၱိစာေပ ပညာရပ္မ်ားကုိ 
								ျမန္မာႏုိင္ငံပရိယတၱိသာသနာေတာ္၌ ထင္ရွား 
								ေက်ာ္ၾကားေသာ ဟသၤာတၿမိဳ႕ မိုးေကာင္းေက်ာင္းတိုက္၊ 
								ျပည္ၿမိဳ႕ ေဇာတိကာရုံ ေက်ာင္းတုိက္၊ ပဲခူးၿမိဳ႕ 
								ၾကခတ္၀ုိင္းေက်ာင္းတိုက္၊ မႏၲေလးၿမိဳ႕ 
								မဟာဝိသုဒၶါရုံ ေက်ာင္းတိုက္ႀကီးႏွင့္ 
								မစိုးရိမ္ပါဠိတကၠသိုလ္ ေက်ာင္းတိုက္တို႔တြင္ 
								သင္ယူဆည္းပူးခဲ့ပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								သက္ေတာ္ ၃ဝႏွစ္အတြင္းတြင္ သာသနာေတာ္နယ္ပယ္၌ 
								လြန္စြာခက္ခဲနက္နဲ၍ ဂုဏ္ယူထုိက္ေသာ သာသနဓဇ 
								ဓမၼာစရိယ ေစတိယဂၤဏဓမၼာစရိယ သက်သီဟဓမၼာစရိယ 
								စာေမးပဲြမ်ားကို 
								အဆင့္ဆင့္ေအာင္ျမင္ေတာ္မူခဲ့ေလသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတာ္ သည္ ၁၉၉၃ ခုႏွစ္တြင္ သီရိလကၤာႏုိင္ငံ 
								Buddhist and Pali University မွ မဟာ၀ိဇၨာ (M.A) 
								ဘဲြ႕ထူး ဆြတ္ခူးရရွိေတာ္မူခ့ဲၿပီးေနာက္ 
								၂၀၀၃ခုႏွစ္တြင္ အိႏိၵယႏုိင္ငံ Sanskrit University 
								မွ ပါရဂူ (Ph.D) 
								ဘဲြ႕ကုိ ဆြတ္ခူးရရွိေတာ္မူသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတာ္သည္ ၁၉၈၆ မွ ၁၉၉၈ အထိ 
								ႏိိုင္ငံေတာ္ပရိယတၱိသာသနာ့တၠသိုလ္၌ ကထိကဆရာေတာ္၊ ပါေမာကၡဆရာေတာ္အျဖစ္တာ၀န္ထမ္းေဆာင္ေတာ္မူခ့ဲၿပီး 
								ယခုအခါ ရန္ကုန္ၿမိဳ႕ အျပည္ျပည္ဆုိင္ရာ 
								ေထရ၀ါဒဗုဒၶသာသနာျပဳ တကၠသိုလ္တြင္ 
								ဒုတိယပါေမာကၡခ်ဳပ္ ဆရာေတာ္အျဖစ္ 
								ထမ္းေဆာင္လ်က္ ရွိေလသည္။ ေဖာ္ျပပါ 
								သာသနာ့တာ၀န္မ်ားအျပင္ အျခားေသာ သာသနာေရးဆုိင္ရာ 
								လုပ္ငန္းေဆာင္တာမ်ား၌ မဂၤလာဒုံ 
								က်ဳိကၠေလာ့ေတာရေက်ာင္းတုိက္ ပဓာနနာယကဆရာေတာ္ 
								အျဖစ္ျဖင့္လည္းေကာင္း၊ 
								ရန္ကုန္ၿမိဳ႕မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး၏၀ိပသာနာနည္းစဥ္ဓမၼက်င့္စဥ္တရားစခန္းမ်ား၏ 
								နာယကဆရာေတာ္အျဖစ္ျဖင့္လည္းေကာင္း 
								တာ၀န္ယူထမ္းေဆာင္ေတာ္မူလ်က္ ရွိေလသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတာ္၏ သာသန၀န္ေဆာင္လုပ္ငန္းမ်ားတြင္ 
								ျပည္တြင္း-ျပည္ပမွ ဗုဒၶဓမၼသင္ယူဆည္းပူးၾကသူ 
								ေက်ာင္းသားေက်ာင္းသူမ်ားအား ဗုဒၶဓမၼဆိုင္ရာ 
								ဗဟုသုတပညာရပ္မ်ားကုိ လမ္းညႊန္ျပသဆိုဆုံးမေတာ္မူ၍ 
								သာသနာေတာ္အက်ဳိး၊ ေလာကအက်ဳိး 
								ရြက္ေဆာင္သည္ပိုးေတာ္မူသည္ ျဖစ္ေသာေၾကာင့္ 
								ႏိုင္ငံေတာ္မွ ဆက္ကပ္ေတာ္မူေသာ 
								သာသနာေရးဆုိင္ရာ ဂုဏ္ထူးဘဲြ႕ထူးျဖစ္သည့္ 
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								၂၀၀၁ခုႏွစ္တြင္ “မဟာဂႏၲ၀ါစက ပ႑ိတ” ဘဲြ႕၊ 
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								၂၀၀၃ခုႏွစ္တြင္ “အဂၢမဟာဂႏၲ၀ါစက ပ႑ိတ” ဘဲြ႕ႏွင့္ 
								</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								၂၀၀၇ခုႏွစ္တြင္ “မဟာကမၼဌာနစရိယ” ဘဲြ႕တုိ႕ကို 
								အပူေဇာ္ခံရရွိေတာ္မူေလသည္။ </p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								ဆရာေတာ္သည္ ပရိယတ္ ပဋိပတ္ စြယ္စံု ကြၽမ္းက်င္သည့္ 
								အားေလွ်ာ္စြာ က်ိဳကၠေလာ့ပရိယတၱၱိစာသင္တိုက္ 
								မိုးကုတ္၀ိပႆနာဓမၼ၌ၼ စာသင္သား သံဃာမ်ားအား 
								ပိဋကတ္က်မ္းစာမ်ား ပို႔ခ်ေပးၿခင္း၊ ေယာဂီမ်ားအား 
								တရားေဟာေပးၿခင္း၊ အၿပည္ၿပည္ဆိုင္ရာ ေထရ၀ါဒ 
								သာသနာၿပဳတကၶၠသိုလ္၌ ပိဋကတ္က်မ္းစာမ်ား 
								ပို႔ခ်ေပးၿခင္း၊ က်မ္းစာမ်ား စစ္ေဆးၿခင္း၊ 
								Meditation Class မ်ား၌ ၀ိပႆနာ တရားေဟာၿခင္း၊ 
								International Buddhist Conference 
								မ်ားသိူ႔တက္ေရာက္၍ စာတန္းမ်ားကို ဖတ္ၾကားျခင္းမ်ား 
								ေဆာင္ရြက္လ်က္ ႐ိွပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								က်ိဳကၠေလာ့ပရိယတၱၱိစာသင္တိုက္ မိုးကုတ္၀ိပႆနာဓမၼ၌ 
								တရားေဟာ၊ တရားၿပေပးၿခင္း၊ တစ္ႏွစ္လွ်င္ 
								အနည္းဆံုး(၅)ႀကိမ္ တရားစခန္းပြဲမ်ား 
								က်င့္ပေပးၿခင္းမ်ားကို ေဆာင္ရြက္လွ်က္႐ိွပါသည္။</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								**************************************************</p>







								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk Video</font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">********************************************************</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								သႀကၤန္တြင္း ၆ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း 
								(စကၤာပူႏိုင္ငံ)</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-12-01.mp4">
								၁၂-၄-၂၀၁၈ ေန႕လည္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-12-02.mp4">
								၁၂-၄-၂၀၁၈ ညေန သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-13-01.mp4">
								၁၃-၄-၂၀၁၈ ေန႕လည္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-13-02.mp4">
								၁၃-၄-၂၀၁၈ ညေန သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-14-01.mp4">
								၁၄-၄-၂၀၁၈ ေန႕လည္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-14-02.mp4">
								၁၄-၄-၂၀၁၈ ညေန သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-15-01.mp4">
								၁၅-၄-၂၀၁၈ ေန႕လည္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-15-02.mp4">
								၁၅-၄-၂၀၁၈ ညေန သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-16-01.mp4">
								၁၆-၄-၂၀၁၈ ေန႕လည္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Singapore-2018-04/Dr-Candavara-bhivamsa-2018-04-16-02.mp4">
								၁၆-၄-၂၀၁၈ ညေန သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="5">~~~~~~~~~~~~~~~~~~~~~~</font></p>
								<span class="userContent"><font size="6">
								ဇမၺဴသီရိဗိမာန္ ေဟာတရားမ်ား</font></span><span data-ft="{&quot;tn&quot;:&quot;K&quot;}" class="userContent"><font size="6">
			</font><br>
								</span><font size="5">~~~~~~~~~~~~~~~~~~~~~~</font><p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-21am.mp4">၂၁-၁၂-၂၀၁၆ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၂၁-၁၂-၂၀၁၆ ေန႕လည္ သစၥာတရား</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-22am.mp4">၂၂-၁၂-၂၀၁၆ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၂၂-၁၂-၂၀၁၆ ေန႕လည္ 
								သစၥာတရား</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၂၃-၁၂-၂၀၁၆ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-23pm.mp4">၂၃-၁၂-၂၀၁၆ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-24am.mp4">၂၄-၁၂-၂၀၁၆ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-24pm.mp4">၂၄-၁၂-၂၀၁၆ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-25am.mp4">၂၅-၁၂-၂၀၁၆ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2016-12/Dr-Candavara-bhivamsa-Zabyusiri-2016-12-25pm.mp4">၂၅-၁၂-၂၀၁၆ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-21am.mp4">၂၁-၁-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-21pm.mp4">၂၁-၁-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၂၂-၁-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-22.mp4">၂၂-၁-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၂၃-၁-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-23.mp4">၂၃-၁-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-24am.mp4">၂၄-၁-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-24pm.mp4">၂၄-၁-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-25am.mp4">၂၅-၁-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-01/Dr-Candavara-bhivamsa-Zabyusiri-2017-01-25pm.mp4">၂၅-၁-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-19am.mp4">၁၉-၂-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-19pm.mp4">၁၉-၂-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-20am.mp4">၂၀-၂-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-20pm.mp4">၂၀-၂-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-21pm.mp4">၂၁-၂-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-21pm.mp4">၂၁-၂-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-22am.mp4">၂၂-၂-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-22pm.mp4">၂၂-၂-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-23am.mp4">၂၃-၂-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-02/Dr-Candavara-bhivamsa-Zabyusiri-2017-02-23pm.mp4">၂၃-၂-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၇ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-17am.mp4">၁၇-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-17pm.mp4">၁၇-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-18am.mp4">၁၈-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-18pm.mp4">၁၈-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-19am.mp4">၁၉-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-19pm.mp4">၁၉-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-20am.mp4">၂၀-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-20pm.mp4">၂၀-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-21am.mp4">၂၁-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-23pm.mp4">၂၁-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-22am.mp4">၂၂-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-22pm.mp4">၂၂-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-23am.mp4">၂၃-၃-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-23pm.mp4">၂၃-၃-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-03/Dr-Candavara-bhivamsa-Zabyusiri-2017-03-29pm.mp4">
								၂၉-၃-၂၀၁၇ ည တရားပြဲ</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၆ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-04am.mp4">၄-၄-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-04pm.mp4">၄-၄-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-05am.mp4">၅-၄-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-05pm.mp4">၅-၄-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-06am.mp4">၆-၄-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-06pm.mp4">၆-၄-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-07am.mp4">၇-၄-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-07pm.mp4">၇-၄-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-08am.mp4">၈-၄-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-08pm.mp4">၈-၄-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-04/Dr-Candavara-bhivamsa-Zabyusiri-2017-04-09am.mp4">၉-၄-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၃ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-06am.mp4">၆-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-06pm.mp4">၆-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-07am.mp4">၇-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-07pm.mp4">၇-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-08am.mp4">၈-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-08pm.mp4">၈-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-14am.mp4">၁၄-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-14pm.mp4">၁၄-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-15am.mp4">၁၅-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-15pm.mp4">
								၁၅-၅-၂၀၁၇ ေန႕လည္ သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-16am.mp4">၁၆-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-16pm.mp4">၁၆-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-17am.mp4">၁၇-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-17pm.mp4">၁၇-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-18am.mp4">၁၈-၅-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-05/Dr-Candavara-bhivamsa-Zabyusiri-2017-05-18pm.mp4">၁၈-၅-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-06/Dr-Candavara-bhivamsa-Zabyusiri-2017-06-16am.mp4">၁၆-၆-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-06/Dr-Candavara-bhivamsa-Zabyusiri-2017-06-16pm.mp4">၁၆-၆-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-06/Dr-Candavara-bhivamsa-Zabyusiri-2017-06-18am.mp4">၁၈-၆-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-06/Dr-Candavara-bhivamsa-Zabyusiri-2017-06-18pm.mp4">၁၈-၆-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-06/Dr-Candavara-bhivamsa-Zabyusiri-2017-06-20am.mp4">၂၀-၆-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-06/Dr-Candavara-bhivamsa-Zabyusiri-2017-06-20pm.mp4">၂၀-၆-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-04am.mp4">၄-၇-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-04pm.mp4">၄-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-05am.mp4">၅-၇-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-05pm.mp4">၅-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-06am.mp4">၆-၇-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-06pm.mp4">၆-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-07am.mp4">
								၇-၇-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-07pm.mp4">
								၇-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-08am.mp4">၈-၇-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-08pm.mp4">၈-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-19am.mp4">
								၁၉-၇-၂၀၁၇ နံနက္ ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-19pm.mp4">၁၉-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-20am.mp4">၂၀-၇-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-07/Dr-Candavara-bhivamsa-Zabyusiri-2017-07-20pm.mp4">၂၀-၇-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-06am.mp4">၆-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-06pm.mp4">၆-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-07am.mp4">၇-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-07am.mp4">၇-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-08am.mp4">၈-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-08pm.mp4">၈-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-09am.mp4">၉-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-09pm.mp4">၉-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-10am.mp4">၁၀-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-10pm.mp4">၁၀-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-19am.mp4">၁၉-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-19pm.mp4">၁၉-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-20am.mp4">၂၀-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-20pm.mp4">၂၀-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-21am.mp4">၂၁-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-21pm.mp4">၂၁-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-22am.mp4">၂၂-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-22pm.mp4">၂၂-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-23am.mp4">၂၃-၈-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-08/Dr-Candavara-bhivamsa-Zabyusiri-2017-08-23pm.mp4">၂၃-၈-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								၅ ရက္ မီးၿငိမ္း အဓိ႒ာန္ တရားစခန္း</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-04am.mp4">၄-၉-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-04pm.mp4">၄-၉-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-05am.mp4">၅-၉-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-05pm.mp4">၅-၉-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-06am.mp4">၆-၉-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-06pm.mp4">၆-၉-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-07am.mp4">၇-၉-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-07pm.mp4">၇-၉-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-08am.mp4">၈-၉-၂၀၁၇ နံနက္ 
								ဝိပႆနာ အလုပ္ေပးတရား</a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/Zabyusiri/2017-09/Dr-Candavara-bhivamsa-Zabyusiri-2017-09-08pm.mp4">၈-၉-၂၀၁၇ ေန႕လည္ 
								သစၥာတရား</a></p>
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
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="5">~~~~~~~~~~~~~~~~~~~~~~</font></p>
			<span data-ft="{&quot;tn&quot;:&quot;K&quot;}" class="userContent">
			<font size="6">ပဋိစၥသမုပါဒ္ကို အဘိဓမၼာႏွင့္ ႏိႈင္းယွဥ္ေလ့လာျခင္း
			</font></span>
			<p>
			<span data-ft="{&quot;tn&quot;:&quot;K&quot;}" class="userContent">
			(၃)ရက္ အခ်ိန္ျပည္႕ အထူး သင္တန္း (in Singapore)<br>
			</span><font size="5">~~~~~~~~~~~~~~~~~~~~~~</font></p>
								<p>
			<br>
			October 12, 2013 (Saturday)<br>
			~~~~~~~~<br>
			<br>
			from 8:30am to 9:00am - registration<br>
			<br>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/001-Dr-Candavara-bhivamsa-2013-Oct-12-934am-to-11am.mp4">
			၁။ ပထမေန႕၁၂-၁၀-၁၃၊ နံနက္ပုိင္း ၉နာရီမွ ၁၁နာရီထိ (သင္တန္း)</a><br>
&nbsp;</p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/002-Dr-candavara-bhivamsa-2013-oct-12-q-%201120-to-1140am.mp4">
			၂။ ပထမေန႕၁၂-၁၀-၁၃၊&nbsp; နံနက္ပုိင္း ၁၁ နာရီမွ ၁၁း၂၀ နာရီအထိ (အေမး 
			အေျဖ)</a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/003-Dr-candavara-bhivamsa-2013-oct-12-133pm-to-3pm.mp4">၃။ ပထမေန႕ ၁၂-၁၀-၂၀၁၃၊ ေန႕လည္ပိုင္း 
			၁း၃၀နာရီမ ၃နာရီ </a> </p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/004-Dr-candavara-bhivamsa-2013-oct-12-q&amp;a-4pm-to-415pm.mp4">
			၄။ ပထမေန႕ ၁၂-၁၀-၂၀၁၃၊ ညေနပိုင္း ၄နာရီမွ ၄း၁၅နာရီ (အေမး အေျဖ)</a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/005-Dr-candavara-bhivamsa-2013-oct-12-415-pm-to-6pm.mp4">
			၅။ ပထမေန႕ ၁၂-၁၀-၂၀၁၃၊ ညေနပိုင္း ၄း၁၅ နာရီမွ ၆နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/006-Dr-candavara-bhivamsa-2013-oct-13-3pm-to-4pm.mp4">
			၆။ ဒုတိယေန႕ ၁၃-၁၀-၂၀၁၃၊ ညေနပိုင္း ၃ နာရီမွ ၄ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/007-Dr-candavara-bhivamsa-2013-oct-13-4pm-to-5pm.mp4">
			၇။ ဒုတိယေန႕ ၁၃-၁၀-၂၀၁၃၊ ညေနပိုင္း ၄ နာရီမွ ၅ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/008-Dr-candavara-bhivamsa-2013-oct-13-608pm-to-736pm.mp4">
			၈။ ဒုတိယေန႕ ၁၃-၁၀-၂၀၁၃၊ ညေနပိုင္း ၆ နာရီမွ ၇း၃၀ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/009-Dr-candavara-bhivamsa-2013-oct-13-8pm-to-9pm.mp4">
			၉။ ဒုတိယေန႕ ၁၃-၁၀-၂၀၁၃၊ ညပိုင္း ၈ နာရီမွ ၉ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/010-Dr-candavara-bhivamsa-2013-oct-15-830am-to-1030am.mp4">
			၁၀။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ နံနက္ပိုင္း ၈း၃၀ နာရီမွ ၁၀း၃၀ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/011-Dr-candavara-bhivamsa-2013-oct-15-1030am-to-1130am.mp4">
			၁၁။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ နံနက္ပိုင္း ၁၀း၃၀ နာရီမွ ၁၁း၃၀ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/012-Dr-candavara-bhivamsa-2013-oct-15-1pm-to-3pm.mp4">
			၁၂။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ ညေနပိုင္း ၁ နာရီမွ ၃ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/013-Dr-candavara-bhivamsa-2013-oct-15-qa-3pm-to-345pm.mp4">
			၁၃။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ ညေနပိုင္း ၃ နာရီမွ ၃း၄၅ နာရီ (အေမး အေျဖ)</a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/014-Dr-candavara-bhivamsa-2013-oct-15-qa-415pm-to-5pm.mp4">
			၁၄။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ ညေနပိုင္း ၄း၁၅ နာရီမွ ၅ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/015-Dr-candavara-bhivamsa-2013-oct-15-5pm-to-625pm.mp4">
			၁၅။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ ညေနပိုင္း ၅ နာရီမွ ၆း၂၅ နာရီ </a></p>
								<p>
			<a href="http://dhammadownload.com/MP4Library/Kyaikkalot-Sayadaw-Dr-Candavara-bhivamsa/TheStudyOfPratityasamutpadaInComparisonWithAbhidhamma/016-Dr-candavara-bhivamsa-2013-oct-15-726pm-to-851pm.mp4">
			၁၆။ တတိယေန႕ ၁၅-၁၀-၂၀၁၃၊ ညေနပိုင္း ၇း၂၆ နာရီမွ ၈း၅၀ နာရီ </a></p>
								<p>
			&nbsp;</p>
								<p>
			001-Dr-Candavara-bhivamsa-2013-Oct-12-934am-to-11am.mp4 </p>
								<p>
			002-Dr-candavara-bhivamsa-2013-oct-12-q- 1120-to-1140am.mp4</p>
								<p>
			003-Dr-candavara-bhivamsa-2013-oct-12-133pm-to-3pm.mp4</p>
								<p>
			004-Dr-candavara-bhivamsa-2013-oct-12-q&amp;a-4pm-to-415pm.mp4</p>
								<p>
			005-Dr-candavara-bhivamsa-2013-oct-12-415-pm-to-6pm.mp4</p>
								<p>
			006-Dr-candavara-bhivamsa-2013-oct-13-3pm-to-4pm.mp4</p>
								<p>
			007-Dr-candavara-bhivamsa-2013-oct-13-4pm-to-5pm.mp4</p>
								<p>
			008-Dr-candavara-bhivamsa-2013-oct-13-608pm-to-736pm.mp4</p>
								<p>
			009-Dr-candavara-bhivamsa-2013-oct-13-8pm-to-9pm.mp4</p>
								<p>
			010-Dr-candavara-bhivamsa-2013-oct-15-830am-to-1030am.mp4</p>
								<p>
			011-Dr-candavara-bhivamsa-2013-oct-15-1030am-to-1130am.mp4</p>
								<p>
			012-Dr-candavara-bhivamsa-2013-oct-15-1pm-to-3pm.mp4</p>
								<p>
			013-Dr-candavara-bhivamsa-2013-oct-15-qa-3pm-to-345pm.mp4</p>
								<p>
			014-Dr-candavara-bhivamsa-2013-oct-15-qa-415pm-to-5pm.mp4</p>
								<p>
			015-Dr-candavara-bhivamsa-2013-oct-15-5pm-to-625pm.mp4</p>
								<p>
			016-Dr-candavara-bhivamsa-2013-oct-15-726pm-to-851pm.mp4</p>
								<p>
			&nbsp;</p>
								<p>
			&nbsp;</p>
								<p>
			&nbsp;</p>
								<p>
			<br>
			၂။ ပထမေန႕၁၂-၁၀-၁၃၊&nbsp; နံနက္ပုိင္း ၁၁ နာရီမွ ၁၁း၂၀ နာ<br>
			<a href="http://youtu.be/L9mOvdkUnm0">http://youtu.be/L9mOvdkUnm0</a>&nbsp; <br>
			<br>
			from 11:00am to 12:15pm - Break<br>
			From12:15pm to 1:pm - lunch<br>
			<br>
			ပထမေန႕၁၂-၁၀-၁၃ ဒုတိယအခ်ိန္ from 1pm to 3pm - Lecturer 2<br>
			<a href="http://youtu.be/ce00473CqoA">http://youtu.be/ce00473CqoA</a>&nbsp; <br>
			<br>
			from 3pm to 3:30pm - Break<br>
			<br>
			ပထမေန႕၁၂-၁၀-၁၃ တတိယအခ်ိန္-ငါေသရင္-ဘာၿဖစ္မလဲ from 3:30pm to 5:30pm - 
			Lecturer 3<br>
			<a href="http://youtu.be/rz4I9HuHlsY">http://youtu.be/rz4I9HuHlsY</a>&nbsp; <br>
			<br>
			from 5:30pm to 6:30pm - Break<br>
			from 6:30pm to 7pm - Q&amp;A<br>
			<br>
			October 13, 2013 (Sunday)<br>
			~~~~~~~~<br>
			<br>
			from 2:30pm to 3:00 pm - registration<br>
			<br>
			ဒုတိယေန႕၁၃-၁၀-၁၃-ပထမပုိင္း from 3pm to 5pm - Lecture 1<br>
			<a href="http://youtu.be/KkwKZE7UG2M">http://youtu.be/KkwKZE7UG2M</a>&nbsp; <br>
			<br>
			from 5pm to 5:30pm - break<br>
			from 5:30pm to 7:30pm - lecture 2<br>
			from 7:30pm to 8:30pm - break<br>
			&nbsp;</p>
								<p>
			ဒုတိယေန႕၁၃-၁၀-၁၃-ပထမပုိင္း </p>
								<p>
			from 8:30pm to 9pm - Q&amp;A<br>
			<a href="https://www.youtube.com/watch?v=YYca0xFwqOM">
			https://www.youtube.com/watch?v=YYca0xFwqOM</a>
			<br>
			<br>
			October 15, 2013 (Tuesday)<br>
			~~~~~~~~<br>
			from 8:30am to 9:00am - registration<br>
			from 9am to 11am - Lecturer 1<br>
			from 11:00am to 12:15pm - Break<br>
			From12:15pm to 1:pm - lunch<br>
			from 1pm to 3pm - Lecturer 2<br>
			from 3pm to 3:30pm - Break<br>
			from 3:30pm to 5:30pm - Lecturer 3<br>
			from 5:30pm to 6:30pm - Break<br>
			from 6:30pm to 7pm - Q&amp;A<br>
			<br>
			<br>
			တတိယေန႕၁၅-၁၀-၁၃ အေမး-အေၿဖမ်ား စုစည္းတင္ျပခ်က္<br>
			<a href="http://www.youtube.com/watch?v=xm260_-5Jl8&amp;feature=share&amp;list=UU8CK874e7ksjNPvS2oi9Qng">http://www.youtube.com/watch?v=xm260_-5Jl8&amp;feature=share&amp;list=UU8CK874e7ksjNPvS2oi9Qng</a> <br>
			<br>
			<br>
			<br>
			<br>
			<br>
			<br>
&nbsp;</p>
								<p>
			&nbsp;</p>
								<p>
			<span class="text_exposed_show">October 12, 2013 (Saturday)<br>
			~~~~~~~~</span></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p>
			<span class="text_exposed_show">from 8:30am to 9:00am - registration<br>
			&nbsp;</span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://youtu.be/hhaRAHsbUNw">ပထမေန႕၁၂-၁၀-၁၃ နံနက္ပုိင္း 
			၁း-၃
			from 9am to 11am - Lecturer 1</a></span></p>
								<p>
			<a href="http://youtu.be/hhaRAHsbUNw">http://youtu.be/hhaRAHsbUNw</a> </p>
								<p>
			&nbsp;</p>
								<p>
			<span class="text_exposed_show">ပထမေန႕၁၂-၁၀-၁၃ နံနက္ပုိင္း၁း-၃၀
			</span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://youtu.be/L9mOvdkUnm0">http://youtu.be/L9mOvdkUnm0</a>
			</span></p>
								<p>
			<span class="text_exposed_show"><br>
			from 11:00am to 12:15pm - Break<br>
			From12:15pm to 1:pm - lunch</span></p>
								<p>
			<span class="text_exposed_show"><br>
			<a href="http://youtu.be/ce00473CqoA">ပထမေန႕၁၂-၁၀-၁၃ ဒုတိယအခ်ိန္
			from 1pm to 3pm - Lecturer 2</a></span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://youtu.be/ce00473CqoA">http://youtu.be/ce00473CqoA</a>
			</span></p>
								<p>
			<span class="text_exposed_show"><br>
			from 3pm to 3:30pm - Break</span></p>
								<p>
			<span class="text_exposed_show"><br>
			<a href="http://youtu.be/rz4I9HuHlsY">ပထမေန႕၁၂-၁၀-၁၃ 
			တတိယအခ်ိန္-ငါေသရင္-ဘာၿဖစ္မလဲ
			from 3:30pm to 5:30pm - Lecturer 3</a></span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://youtu.be/rz4I9HuHlsY">http://youtu.be/rz4I9HuHlsY</a> </span></p>
								<p>
			<span class="text_exposed_show"><br>
			from 5:30pm to 6:30pm - Break<br>
			from 6:30pm to 7pm - Q&amp;A<br>
			<br>
			October 13, 2013 (Sunday)<br>
			~~~~~~~~<br>
			<br>
			from 2:30pm to 3:00 pm - registration<br>
			&nbsp;</span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://youtu.be/KkwKZE7UG2M">ဒုတိယေန႕၁၃-၁၀-၁၃-ပထမပုိင္း
			from 3pm to 5pm - Lecture 1</a></span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://youtu.be/KkwKZE7UG2M">http://youtu.be/KkwKZE7UG2M</a>
			</span></p>
								<p>
			<span class="text_exposed_show"><br>
			from 5pm to 5:30pm - break<br>
			from 5:30pm to 7:30pm - lecture 2<br>
			from 7:30pm to 8:30pm - break<br>
			from 8:30pm to 9pm - Q&amp;A<br>
			&nbsp;</span></p>
								<p>
			<span class="text_exposed_show">
			<br>
			October 15, 2013 (Tuesday)<br>
			~~~~~~~~<br>
			from 8:30am to 9:00am - registration<br>
			from 9am to 11am - Lecturer 1<br>
			from 11:00am to 12:15pm - Break<br>
			From12:15pm to 1:pm - lunch<br>
			from 1pm to 3pm - Lecturer 2<br>
			from 3pm to 3:30pm - Break<br>
			from 3:30pm to 5:30pm - Lecturer 3<br>
			from 5:30pm to 6:30pm - Break<br>
			from 6:30pm to 7pm - Q&amp;A<br>
			<br>
&nbsp;</span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://www.youtube.com/watch?v=xm260_-5Jl8&amp;feature=share&amp;list=UU8CK874e7ksjNPvS2oi9Qng">
			တတိယေန႕၁၅-၁၀-၁၃ အေမး-အေၿဖမ်ား စုစည္းတင္ျပခ်က္</a></span></p>
								<p>
			<span class="text_exposed_show">
			<a href="http://www.youtube.com/watch?v=xm260_-5Jl8&amp;feature=share&amp;list=UU8CK874e7ksjNPvS2oi9Qng">
			http://www.youtube.com/watch?v=xm260_-5Jl8&amp;feature=share&amp;list=UU8CK874e7ksjNPvS2oi9Qng</a></span></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
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
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/Dr-Nandamalabhivamsa/MP3Disc01/042-DrNandamalabhivamsa-12-7-2008Singapore.mp3">
								<br>
&nbsp;</a></font></p>
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
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
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
    
