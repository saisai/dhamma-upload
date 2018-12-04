from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 

<!-- Start dhammadownload menu top and side bar -->

 

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font color="#800080">
	<span style="font-family: Times New Roman; font-size: 32pt">Nyaungdon 
	Sayadaw </span></font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 540px; top: 10px;" id="layer23">
	<img src="images/Nyaungdon-Sayadaw-Bhaddanta-Jotika-Bhivamsa.gif" width="151" height="191" border="0"></div>

	
	




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







<div style="position: absolute; width: 1101px; height: 6396px; z-index: 21; left: 219px; top: 156px" id="layer24" font="" face="Zawgyi-One">
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<b><font size="5">Nyaungdon Sayadaw </font></b>
									</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<b><font size="5">Bhaddanta Jotika Bhivamsa</font></b><br>
						Sasanadaza Dhammacariya</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						Sasana pala Dhammacariya
									</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<font face="Zawgyi-One"><br><font size="5">ေညာင္တုန္း 
						ဆရာေတာ္</font></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<b><font size="6" face="Zawgyi-One">ဘဒၵႏ ၱေဇာတိကဘိဝံသ</font></b></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<font size="4" face="Zawgyi-One">သာသနဓဇဓမၼာစရိယ၊ </font>
									</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<font size="4" face="Zawgyi-One">သာသနပါလဓမၼာစရိယ၊</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<font size="4" face="Zawgyi-One">ဥဘေတာဝိဘဂၤဓရ</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<font face="Zawgyi-One"><font size="4">ေဟာၾကားေတာ္မူေသာ 
						တရားေတာ္မ်ား</font><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font>
									</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
						<font size="4" face="Zawgyi-One">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5" face="Zawgyi-One">Dhamma Talk 
									Video</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One">****dhamma talks uploaded and published on 
									29 March 2013****</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၁)<br>
&nbsp;</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ၾသစေၾတးလ်ႏိုင္ငံ၊ ဆစ္ဒနီၿမိဳ႕ 
									(ပါရမီရိပ္သာ) ၌ ေဟာၾကားပို႕ခ်ေတာ္မူသည္။</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4"><br>
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/01-NyaungDonSayadawBhaddhantaJotika-DVD01-20100408.mp4">၁။ ပါရမီ (၁၀)ပါး (၁) ၈-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/02-NyaungDonSayadawBhaddhantaJotika-DVD01-20100409.mp4">၂။ ပါရမီ (၁၀)ပါး (၂) ၉-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/03-NyaungDonSayadawBhaddhantaJotika-DVD01-20100410.mp4">၃။ ပါရမီ (၁၀)ပါး (၃) 
									၁၀-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/04-NyaungDonSayadawBhaddhantaJotika-DVD01-20100411.mp4">၄။ ပါရမီ (၁၀)ပါး (၄) 
									၁၁-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/05-NyaungDonSayadawBhaddhantaJotika-DVD01-20100412.mp4">၅။ ပါရမီ (၁၀)ပါး (၅) 
									၁၂-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/06-NyaungDonSayadawBhaddhantaJotika-DVD01-20100413.mp4">၆။ ပါရမီ (၁၀)ပါး (၆) 
									၁၃-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/07-NyaungDonSayadawBhaddhantaJotika-DVD01-20100414.mp4">၇။ ပါရမီ (၁၀)ပါး (၇) 
									၁၄-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/08-NyaungDonSayadawBhaddhantaJotika-DVD01-20100415.mp4">၈။ ပါရမီ (၁၀)ပါး (၈) 
									၁၅-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/09-NyaungDonSayadawBhaddhantaJotika-DVD01-20100416.mp4">၉။ ပါရမီ (၁၀)ပါး (၉) 
									၁၆-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/10-NyaungDonSayadawBhaddhantaJotika-DVD01-20100417.mp4">၁၀။ ပါရမီ (၁၀)ပါး (၁၀) 
									၁၇-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/11-NyaungDonSayadawBhaddhantaJotika-DVD01-20100418.mp4">၁၁။ ပါရမီ (၁၀)ပါး (၁၁) 
									၁၈-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-01/12-NyaungDonSayadawBhaddhantaJotika-DVD01-20100419.mp4">၁၂။ ပါရမီ (၁၀)ပါး (၁၂) 
									၁၉-၄-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၂)<br>
&nbsp;</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ၾသစေၾတးလ်ႏိုင္ငံ၊ ဆစ္ဒနီၿမိဳ႕ 
									(ပါရမီရိပ္သာ) ၌ ေဟာၾကားပို႕ခ်ေတာ္မူသည္။</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4"><br>
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/01-NyaungDonSayadawBhaddhantaJotika-DVD02--20100113.mp4">၁။ အဘိဓမၼာ (၁) ၁၃-၁-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/02-NyaungDonSayadawBhaddhantaJotika-DVD02--20100120.mp4">၂။ အဘိဓမၼာ (၂) ၂၀-၁-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/03-NyaungDonSayadawBhaddhantaJotika-DVD02--20100121.mp4">၃။ အဘိဓမၼာ (၃) ၂၁-၁-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/04-NyaungDonSayadawBhaddhantaJotika-DVD02--20100127.mp4">၄။ အဘိဓမၼာ (၄) ၂၇-၁-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/05-NyaungDonSayadawBhaddhantaJotika-DVD02--20100128.mp4">၅။ အဘိဓမၼာ (၅) ၂၈-၁-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/06-NyaungDonSayadawBhaddhantaJotika-DVD02--20100306.mp4">၆။ အဘိဓမၼာ (၆) ၆-၃-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/07-NyaungDonSayadawBhaddhantaJotika-DVD02--20100307.mp4">၇။ အဘိဓမၼာ (၇) ၇-၃-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-02/08-NyaungDonSayadawBhaddhantaJotika-DVD02--T20100214.mp4">၈။ ဘဝအလုပ္ေပး&nbsp; ၁၄-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၃)<br>
&nbsp;</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ၾသစေၾတးလ်ႏိုင္ငံ၊ ဆစ္ဒနီၿမိဳ႕ 
									(ပါရမီရိပ္သာ) ၌ ေဟာၾကားပို႕ခ်ေတာ္မူသည္။</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4"><br>
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/01-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁။ ၿငိမ္းခ်မ္းေရး၊ လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး 
									(၁) ၁၁-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/02-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၂။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၂) ၁၂-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/03-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၃။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၃) ၁၃-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/04-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၄။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၄) ၁၄-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/05-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၅။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၅) ၁၅-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/06-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၆။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၆) ၁၇-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/07-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၇။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၇) ၁၈-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/08-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၈။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၈) ၁၉-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/09-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၉။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၉) ၂၀-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/10-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၀။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၀) ၂၁-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/11-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၁။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၁) ၂၂-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/12-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၂။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၂) ၂၃-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/13-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၃။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၃) ၂၄-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/14-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၄။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၄) ၂၅-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/15-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၅။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၅) ၂၆-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/16-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၆။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၆) ၂၇-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/17-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၇။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၇) ၂၈-၂-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/18-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၈။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၈) ၁-၃-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/19-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၁၉။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၁၉) ၂-၃-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/20-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၂၀။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၂၀) ၃-၃-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-03/21-NyaungDonSayadawBhaddhantaJotika-DVD03.mp4">၂၁။ ၿငိမ္းခ်မ္းေရး၊ 
									လြတ္ေျမာက္ေရး၊ ခ်မ္းသာေရး (၂၁) ၄-၃-၂၀၁၀</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၄)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-04/01-NyaungDonSayadawBhaddhantaJotika-DVD04.mp4">၁။ ေနာက္ဆုံးရလဒ္ (၁) ( 
									၁၅-၂-၂၀၁၂ - မဂၤလာဗ်ဴဟာ )</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-04/02-NyaungDonSayadawBhaddhantaJotika-DVD04.mp4">၂။ ေနာက္ဆုံးရလဒ္ (၂) ( 
									၁၆-၂-၂၀၁၂ - မဂၤလာဗ်ဴဟာ )</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-04/03-NyaungDonSayadawBhaddhantaJotika-DVD04.mp4">၃။ ေနာက္ဆုံးရလဒ္ (၃) ( 
									၁၉-၂-၂၀၁၂ - မဂၤလာဗ်ဴဟာ )</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-04/04-NyaungDonSayadawBhaddhantaJotika-DVD04.mp4">၄။ ေနာက္ဆုံးရလဒ္ (၄) ( 
									၂၀-၂-၂၀၁၂ - မဂၤလာဗ်ဴဟာ )</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-04/05-NyaungDonSayadawBhaddhantaJotika-DVD04.mp4">၅။ ေနာက္ဆုံးရလဒ္ (၅) ( 
									၂၂-၂-၂၀၁၂ - မဂၤလာဗ်ဴဟာ )</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-04/06-NyaungDonSayadawBhaddhantaJotika-DVD04.mp4">၆။ ေနာက္ဆုံးရလဒ္ (၆) ( 
									၂၃-၂-၂၀၁၂ - မဂၤလာဗ်ဴဟာ )</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၅)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/01-NyaungDonSayadawBhaddhantaJotika-DVD05(6-6-2012)Zarite6par.mp4">၁။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၁) (၆-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/02-NyaungDonSayadawBhaddhantaJotika-DVD05(6-6-2012)Zarite6par.mp4">၂။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၂) (၇-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/03-NyaungDonSayadawBhaddhantaJotika-DVD05(13-6-2012)Zarite6par.mp4">၃။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၃) (၁၃-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/04-NyaungDonSayadawBhaddhantaJotika-DVD05(13-6-2012)Zarite6par.mp4">၄။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၄) (၁၄-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/05-NyaungDonSayadawBhaddhantaJotika-DVD05(20-6-2012)Zarite6par.mp4">၅။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၅) (၂၀-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/06-NyaungDonSayadawBhaddhantaJotika-DVD05(21-6-2012)Zarite6par.mp4">၆။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၆) (၂၁-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/07-NyaungDonSayadawBhaddhantaJotika-DVD05(27-6-2012)Zarite6par.mp4">၇။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၇) (၂၇-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-05/08-NyaungDonSayadawBhaddhantaJotika-DVD05(28-6-2012)Zarite6par.mp4">၈။ စရိုက္ (၆) ပါး သေဘာတရား 
									(၈) (၂၈-၆-၂၀၁၂ - မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၇)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-07/01-NyaungDonSayadawBhaddhantaJotika-DVD07.mp4">၁။ သစၥာေလးပါး (အမွားနဲ႕ 
									အမွန္၊ အမွန္နဲ႕ အမွား) (၁) (၂၅-၁၀-၂၀၁၀ - 
									မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-07/02-NyaungDonSayadawBhaddhantaJotika-DVD07.mp4">၂။ သစၥာေလးပါး (အမွားနဲ႕ 
									အမွန္၊ အမွန္နဲ႕ အမွား) (၂) (၂၆-၁၀-၂၀၁၀ - 
									မဂၤလာဗ်ဴဟာ)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-07/03-NyaungDonSayadawBhaddhantaJotika-DVD07.mp4">၃။ သစၥာေလးပါး (အမွားနဲ႕ 
									အမွန္၊ အမွန္နဲ႕ အမွား) (၃) (၂၅-၁၀-၂၀၁၀ - 
									ရွင္သာမေဏဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-07/04-NyaungDonSayadawBhaddhantaJotika-DVD07.mp4">၄။ သစၥာေလးပါး (အမွားနဲ႕ 
									အမွန္၊ အမွန္နဲ႕ အမွား) (၄) (၂၆-၁၀-၂၀၁၀ - 
									ရွင္သာမေဏဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၈)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-08/01-NyaungDonSayadawBhaddhantaJotika-DVD08.mp4">၁။ ဗုဒၶသာသနာ သိမွတ္စရာ (၁) 
									(၂-၆-၂၀၁၀ - ရွင္သာမေဏ ဓမၼဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-08/02-NyaungDonSayadawBhaddhantaJotika-DVD08.mp4">၂။ ဗုဒၶသာသနာ သိမွတ္စရာ (၂) 
									(၄-၆-၂၀၁၀ - ရွင္သာမေဏ ဓမၼဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-08/03-NyaungDonSayadawBhaddhantaJotika-DVD08.mp4">၃။ ဗုဒၶသာသနာ သိမွတ္စရာ (၃) 
									(၉-၆-၂၀၁၀ - ရွင္သာမေဏ ဓမၼဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-08/04-NyaungDonSayadawBhaddhantaJotika-DVD08.mp4">၄။ ဗုဒၶသာသနာ သိမွတ္စရာ (၄) 
									(၁၁-၆-၂၀၁၀ - ရွင္သာမေဏ ဓမၼဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-08/05-NyaungDonSayadawBhaddhantaJotika-DVD08.mp4">၅။ ဗုဒၶသာသနာ သိမွတ္စရာ (၅) 
									(၁၅-၆-၂၀၁၀ - ရွင္သာမေဏ ဓမၼဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-08/06-NyaungDonSayadawBhaddhantaJotika-DVD08.mp4">၆။ ဗုဒၶသာသနာ သိမွတ္စရာ (၆) 
									(၁၆-၆-၂၀၁၀ - ရွင္သာမေဏ ဓမၼဗိမာန္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၁၀)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-10/01-NyaungDonSayadawBhaddhantaJotika-DVD10.mp4">၁။ တရားအျမင္ ရွိေစခ်င္ (၁) 
									(၂၀-၃-၂၀၁၁ - ကံျမင့္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-10/02-NyaungDonSayadawBhaddhantaJotika-DVD10.mp4">၂။ တရားအျမင္ ရွိေစခ်င္ (၂) 
									(၂၁-၃-၂၀၁၁ - ကံျမင့္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-10/03-NyaungDonSayadawBhaddhantaJotika-DVD10.mp4">၃။ တရားအျမင္ ရွိေစခ်င္ (၃) 
									(၂၂-၃-၂၀၁၁ - ကံျမင့္)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၁၁)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အရွင္သာမေဏဗိမာန္ (ဗဟန္း) ၌ 
									ေဟာၾကားပို႕ခ်ေတာ္မူသည္။</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/01-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110903).mp4">၁။ နိဒါန္း (၃-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/02-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110904).mp4">၂။ အဓိပတိသုံးပါႏွင့္ 
									ေဟတုပစၥည္း (၁) (၄-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/03-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110910).mp4">၃။ ေဟတုပစၥည္း(၂) ႏွင့္ 
									အာရမဏပစၥည္း (၁) (၁၀-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/04-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110911).mp4">၄။ အာရမဏပစၥည္း(၂) (၁၁-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/05-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110917).mp4">၅။ အာရမဏပစၥည္း (၃) 
									(၁၇-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/06-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110918).mp4">၆။ အာရမဏပစၥည္း (နိဂုံး) 
									(၁၈-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/07-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110924).mp4">၇။ အဓိပတိပစၥည္း (၁) 
									(၂၄-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/08-NyaungDonSayadawBhaddhantaJotika-DVD11-(20110925).mp4">၈။ အဓိပတိပစၥည္း (၂) 
									(၂၅-၉-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/09-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111001).mp4">၉။ အနႏ​ ၱရပစၥည္း (၁-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/10-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111002).mp4">၁၀။ အနႏ​ ၱရပစၥည္း ႏွင့္ 
									သမၼနတၱရပစၥည္း (၂-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/11-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111008).mp4">၁၁။ သဟဇာတပစၥည္း (၈-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/12-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111009).mp4">၁၂။ အညမည ပစၥည္း (၉-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/13-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111023).mp4">၁၃။ အညမည၊ သမၼယုတၱ၊ ဝိပယုတၱ 
									ပစၥည္းမ်ား (၂၃-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/14-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111029).mp4">၁၄။ နိႆယ ပစၥည္း၊ ဥပနိႆယပစၥည္း 
									(၂၉-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/15-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111030).mp4">၁၅။ နိႆယ၊ ပုေရဇာတ၊ 
									ဥပနိႆယပစၥည္း (ပ) (၃၀-၁၀-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/16-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111106).mp4">၁၆။ ဥပနိႆယ ပစၥည္း (ဒု) 
									(၆-၁၁-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/17-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111112).mp4">၁၇။ ပုေရဇာတ ပစာၦဇၾတ 
									ပစၥည္းႏွင့္ အာေသဝန၊ ကမၼ ဝိပါက ပစၥည္း 
									(၁၂-၁၁-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/18-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111113).mp4">၁၈။ ကမၼပစၥည္းႏွင့္ ဝိပါက 
									ပစၥည္း (၁၃-၁၁-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/19-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111126).mp4">၁၉။ ဝိပါက၊ အာဟာရ ဣႃႏၵိယ၊ စ်ာန 
									ပစၥည္း (၂၆-၁၁-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/20-NyaungDonSayadawBhaddhantaJotika-DVD11-(20111127).mp4">၂၀။ မဂၢ၊ သမၼယုတၱ၊ အထၳိ၊ နထၱိ၊ 
									ပစၥည္းႏွင့္ ဝိဂတ၊ အဝိဂတ ပစၥည္း (၂၇-၁၁-၂၀၁၁)</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/NyaungDon-Sayadaw-Bhaddhanta-Jotika-Bhivamsa/DVD-11/21-NyaungDonSayadawBhaddhantaJotika-DVD11-(201111202).mp4">၂၁။ သင္တန္းသား။သင္တန္းသူမ်ား 
									သီတင္ကၽြတ္ ပူေဇာ္ကန္ေတာ့ပြဲ</a></font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အမွတ္စဥ္ (၁၂)</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">လက္ေတြ႕ အသုံးခ် ဓမၼစႀကၤာ 
									တရားေတာ္မ်ား</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ရွင္သာမေဏ ဓမၼဗိမာန္တြင္ 
									၃-၈-၂၀၀၉ မွ ၂၂-၁၀-၂၀၀၉ ထိ ေဟာၾကား 
									ပို႕ခ်ေတာ္မူသည္။</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အပိုင္း ၉၇ ပိုင္း</font></p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
						<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">၁။</font></p>
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
    
