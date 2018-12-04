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

<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 36px;" id="layer22" align="center">
    <font style="font-size: 20pt" color="#800080">
	<span style="font-family: Times New Roman">Bamaw Sayadaw Dr. Kumarabhivamsa</span> </font>
</div>

<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 596px; top: 4px;" id="layer23">
    <img src="images/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa.gif" width="211" height="182" border="0">
</div>




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
<div style="position: absolute; width: 852px; height: 1832px; z-index: 21; left: 222px; top: 162px" id="layer24" font="" face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<span style="font-family: Franklin Gothic Medium; font-weight: 700">
									Bamaw Sayadaw</span></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									Dr. Bhaddanta Kumarabhivamsa</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<span style="font-family: Franklin Gothic Medium; font-weight: 700">
									Agga Maha Pandita, Agga Maha Ganthavacaka 
									Pandita</span></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px; text-kashida-space:50%" class="MsoTagline">
								<font size="4">
								<span style="font-family: Franklin Gothic Medium; font-weight: 700">Abhidhaja 
								Maha Rattha Guru</span></font></p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4" face="Zawgyi-One">သက်သီဟ ဝဋံသကာ၊ ပါဠိ သိေရာမဏီ၊ ဘီေအ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4" face="Zawgyi-One">အဘိဓဇအဂၢမဟာ သဒၶမၼေဇာတိကဓဇ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4" face="Zawgyi-One">အဂၢမဟာပ႑ိတ၊ အဂၢမဟာဂႏ ၳဝါစကပ႑ိတ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4">“အဘိဓဇ မဟာရ႒ဂုရု” </font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4" face="Zawgyi-One">နုိင္ငံေတာ္သံဃမဟာနာယကအဖြဲ႕ 
ဥကၠဌ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font size="4" face="Zawgyi-One">တိပိဋက နိကာယေက်ာင္းတုိက္ၾကီးမ်ား၏ 
စီမံအုပ္ခ်ဳပ္မႈ မဟာနာယက</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<b><font size="5" face="Zawgyi-One">ေက်းဇူးေတာ္ရွင္ (နဝမ) 
ဗန္းေမာ္ဆရာေတာ္ဘုရားၾကီး </font></b></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<b><font size="5" face="Zawgyi-One">ေဒါက္တာ ဘဒၵႏၲ ကုမာရာဘိဝံသ</font></b></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4" face="Zawgyi-One">
									ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<b><font size="5">
									<a href="images/bamaw-sayadaw-biography.pdf">Sayadaw's Biography</a></font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="images/Bamaw-Sayadaw-Gyi-smiling.jpg">
								<font size="5">Bamaw Sayadaw Gyi - Photo-1</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="images/Bamaw-Sayadaw-Gyi-Sitting.jpg">
								<font size="5">Bamaw Sayadaw Gyi - Photo-2</font></a></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<a href="images/Bamaw-Sayadaw-Gyi-Standing.jpg">
								<font size="5">Bamaw Sayadaw Gyi - Photo-3</font></a></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4"><a href="PaHtan-in-picture.htm">၂၄ပစၥည္း-ပဠာန္းရုပ္ၿပစုံ</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<img src="images/ebook/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/BamawSayadawDrBhaddantaKumarabhivamsa-PaTaMyarRaTuPuZarNhitGuNaPuZar.gif" width="161" height="103" border="0"> 
									<font size="4" face="Zawgyi-One">
									<a href="http://dhammadownload.com/File-Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/BamawSayadawDrBhaddantaKumarabhivamsa-PaTaMyarRaTuPuZarNhitGuNaPuZar.pdf">
									(နဝမ) ဗန္းေမာ္ဆရာေတာ္ ေဒါက္တာ ဘဒၵႏၲ 
									ကုမာရာဘိဝံသ၏ ပတၱျမားရတုႏွင့္ ဂုဏပူဇာ 
									သမိုင္းဝင္မွတ္တမ္း</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font size="4" face="Zawgyi-One">
								<img src="images/ebook/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/BamawSayadawDrBhaddantaKumarabhivamsa-HtayYeAhPaDanaDipani.gif" width="161" height="122" border="0">&nbsp;
								<a href="http://dhammadownload.com/File-Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/BamawSayadawDrBhaddantaKumarabhivamsa-HtayYeAhPaDanaDipani.pdf">
								ေထရီအပဒါနဒီပနီ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									*****************************************************</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<strong style="font-weight: 400">
									<font size="5" face="Zawgyi-One">Dhamma Talk 
									Video</font></strong></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
****dhamma talk uploaded and published on 23 Jan 2011****</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">DVD02</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Abhidhamma/001-bamawsayadawgyi-abhidhamma-thingeo-weehteet-5-10-2010.mp4">၁။ အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း(၁) ၅-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Abhidhamma/002-bamawsayadawgyi-abhidhamma-thingeo-weehteet-6-10-2010.mp4">၂။ အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း(၂) ၆-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Abhidhamma/003-bamawsayadawgyi-abhidhamma-thingeo-weehteet-7-10-2010.mp4">၃။ အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း(၃) ၇-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Abhidhamma/004-bamawsayadawgyi-abhidhamma-thingeo-weehteet-4-11-2010.mp4">၄။ အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း(၄) ၄-၁၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Abhidhamma/005-bamawsayadawgyi-abhidhamma-thingeo-weehteet-5-11-2010.mp4">၅။ အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း(၅) ၅-၁၁-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Abhidhamma/006-bamawsayadawgyi-abhidhamma-thingeo-weehteet-6-11-2010.mp4">၆။ အဘိဓမၼာ သၿဂႋဳလ္ ဝီထိသင္တန္း(၆) ၆-၁၀-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">DVD</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">ပဋိစၥသမုပၸါဒ္သင္တန္း</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/001-bamawsayadawgyi-paticcasamupa(1)-15-5-2010.mp4">၁။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၁) ၁၅-၅-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/002-bamawsayadawgyi-paticcasamupa(2)-16-5-2010.mp4">၂။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၂) ၁၆-၅-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/003-bamawsayadawgyi-paticcasamupa(3)-17-5-2010.mp4">၃။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၃) ၁၇-၅-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/004-bamawsayadawgyi-paticcasamupa(4)-18-5-2010.mp4">၄။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၄) ၁၈-၅-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/005-bamawsayadawgyi-paticcasamupa(5)-19-5-2010.mp4">၅။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၅) ၁၉-၅-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/006-bamawsayadawgyi-paticcasamupa(6)-20-5-2010.mp4">၆။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၆) ၂၀-၅-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/007-bamawsayadawgyi-paticcasamupa(7)-11-7-2010.mp4">၇။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၇) ၁၁-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/008-bamawsayadawgyi-paticcasamupa(8)-13-7-2010.mp4">၈။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၈) ၁၃-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/009-bamawsayadawgyi-paticcasamupa(9)-14-7-2010.mp4">၉။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၉) ၁၄-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/010-bamawsayadawgyi-paticcasamupa(10)-15-7-2010.mp4">၁၀။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၁၀) ၁၅-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/011-bamawsayadawgyi-paticcasamupa(11)-16-7-2010.mp4">၁၁။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၁၁) ၁၆-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/012-bamawsayadawgyi-paticcasamupa(12)-17-7-2010.mp4">၁၂။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၁၂) 
									၁၇-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/013-bamawsayadawgyi-paticcasamupa(13)-18-7-2010.mp4">၁၃။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၁၃) 
									၁၈-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Paticcasamupada/014-BamawSayadawGyi-Paticcasamupa(14)-19-7-2010.mp4">၁၄။ ပဋိစၥသမုပၸါဒ္သင္တန္း(၁၄) 
									၁၉-၇-၂၀၁၀</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Zawgyi-One">စကၤာပူႏိုင္ငံ 
								INFORMATICS CAMPUS ၌ ေဟာၾကား ေသာ တရားေတာ္မ်ား</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="5" face="Zawgyi-One"><br>
								</font>
								<font size="4" face="Zawgyi-One">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-20-3-2010.mp4">20-3-2010 ပ႒ာန္းတရားေတာ္ အပိုင္း(၁) 
								ဗန္းေမာ္ဆရာေတာ္ႀကီး
								</a> <br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-20-3-2010-part2.mp4">20-3-2010 ပ႒ာန္းတရားေတာ္ အပိုင္း(၂) 
								ဗန္းေမာ္ဆရာေတာ္ႀကီး</a><br>
								<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-21-3-2010.mp4">21-3-2010 အပၸါယ္တံခါးပိတ္ တရားေတာ္ - 
								ဗန္းေမာ္ဆရာေတာ္ႀကီး</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-27-3-2010.mp4">27-3-2010 ပ႒ာန္းတရားေတာ္ အပိုင္း(၃) 
								ဗန္းေမာ္ဆရာေတာ္ႀကီး</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-28-3-2010.mp4">28-3-2010 ပ႒ာန္းတရားေတာ္ အပိုင္း(၄) 
								ဗန္းေမာ္ဆရာေတာ္ႀကီး</a></font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-28-3-2010-pahtanprayer.mp4">28-3-2010 ကမၻာ့ပဌာန္းပူေဇာ္ပြဲၾကီး</a> - 
								ဗန္းေမာ္ဆရာေတာ္ႀကီး အမွဴးျပဳေသာ သံဃာေတာ္ 
								အရွင္ျမတ္မ်ားႏွင့္ လူပရိသတ္တုိ႔ အတူတကြ 
								ပြားမ်ားရြတ္ဖတ္ျခင္း</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
<p class="MsoTagline" style="text-align: left; text-kashida-space: 50%; margin-top:0; margin-bottom:0">
****dhamma talk uploaded and published on 11 Dec 2010****</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/001-bamaw-sayadawgyi-pahtan-part(1-1)-26-9-2010.mp4">၂၆-၉-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (ပထမပိုင္း)</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/002-bamaw-sayadawgyi-pahtan-part(1-2)-26-9-2010.mp4">၂၆-၉-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (ဒုတိယပိုင္း)</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/003-bamaw-sayadawgyi-pahtan-part(1)-26-9-2010.mp4">၂၆-၉-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၁) 
									ေဟတုပစၥေယာ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/004-bamaw-sayadawgyi-pahtan-part(2)-27-9-2010.mp4">၂၇-၉-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၂) 
									အာရမၼဏပစၥေယာ၊ အဓိပတိပစၥေယာ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/005-bamaw-sayadawgyi-pahtan-part(3)-27-9-2010.mp4">၂၇-၉-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၃) အနႏ 
									ၱရပစၥေယာ၊ သမနႏ ၱရပစၥေယာ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/006-bamaw-sayadawgyi-pahtan-part(4)-29-9-2010.mp4">၂၉-၉-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၄) 
									သဟဇာတပစၥေယာ၊ အညမညပစၥေယာ၊ နိႆယပစၥေယာ၊ 
									ဥပနိႆယပစၥေယာ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/007-bamaw-sayadawgyi-pahtan-part(5)-1-10-2010.mp4">၁-၁၀-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၅) 
									ပုေရဇာတပစၥေယာ၊ ပစ ၦဇာတပစၥေယာ၊ အာေသဝနပစၥေယာ၊ 
									ကမၼပစၥေယာ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/008-bamaw-sayadawgyi-pahtan-part(6)-1-10-2010.mp4">၁-၁၀-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၆) 
									ဝိပါကပစၥေယာ၊ အာဟာရပစၥေယာ၊ ဣႁႏိၵယပစၥေယာ၊ စ်ာန 
									ပစၥေယာ၊ မဂၢပစၥေယာ</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/Pahtan-Oct-2010/009-bamaw-sayadawgyi-pahtan-part(7)-2-10-2010.mp4">၂-၁၀-၂၀၁၀ ပ႒ာန္းတရားေတာ္ (အပိုင္း-၇) 
									သမၼယုတၱပစၥေယာ၊ ဝိပၸယုတၱပစၥေယာ၊ အတၳိပစၥေယာ၊ 
									နတၳိပစၥေယာ၊ ဝိဂတပစၥေယာ၊ အဝိဂတပစၥေယာ-တိ။</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									**************************************************</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5" face="Zawgyi-One">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawdrbhaddantakumarabhivamsa-11-12-2009.mp4">၁၁-၁၂-၂၀၀၉ အပၸါယ္ပိတ္ တရားေတာ္</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5" face="Zawgyi-One">
									<a href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawdrbhaddantakumarabhivamsa-8-1-2010.mp4">၈-၁-၂၀၁၀ နိဗၺာန္တံခါးဖြင့္ တရားေတာ္</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
																			<div class="article-content">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="5">DVD</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
																			</div>
																			<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
																			<font size="4" face="Zawgyi-One">
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/001-Bamaw-Sayadaw-Pahtan24Pyitsee(Prayer)-01.mp4">၁။ 
																			၄-၂-၂၀၁၀ 
																			ပဌာန္းေဒသနာ 
																			၀တ္ရြတ္စဥ္ 
																			တရားေတာ္(၁)</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
																			<font size="4" face="Zawgyi-One">
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/001-Bamaw-Sayadaw-Pahtan24Pyitsee(Prayer)-02.mp4">၁။ 
																			၄-၂-၂၀၁၀ 
																			ပဌာန္းေဒသနာ 
																			၀တ္ရြတ္စဥ္ 
																			တရားေတာ္(၂)</a><br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/002-Bamaw-Sayadaw-Mahathatipahtana(Prayer)-01.mp4">၂။ ၅-၂-၂၀၁၀ မဟာသတိပ႒ာနသုတ္ ၀တ္ရြတ္စဥ္ 
									တရားေတာ္</a><br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/003-Bamaw-Sayadaw-ClosingDoorToTheStatesOfDeprivation-11-12-2009.mp4">
																			၃။ ၁၁-၁၂-၂၀၀၉ အပၸါယ္ပိတ္ တရားေတာ္
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/004-Bamaw-Sayadaw-OpeningDoorToNibban-8-1-2010.mp4">
																			၄။ ၈-၁-၂၀၁၀ နိဗၺာန္တံခါးဖြင့္ တရားေတာ္</a><br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/005-Bamaw-Sayadaw-MaweGyiLayKaung-22-12-2008.mp4">
																			၅။ ၂၂-၁၂-၂၀၀၈ ေႁမြႀကီးေလးေကာင္ ဥပမာျပ 
									တရားေတာ္</a><br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/006-Bamaw-Sayadaw-YoneMinEiZetTawOoPaMarPya-23-12-2008.mp4">
																			၆။ ၂၃-၁၂-၂၀၀၈ ယုန္မင္း၏ဇာတ္ေတာ္ ဥပမာျပ 
									တရားေတာ္
																			</a>
																			<br>
																			<br>ျမတ္ပဌာန္းေဒသနာႏွင့္ ဝိပႆနာဥာဏ္စဥ္ 
									တရားေတာ္မ်ား<br>ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									ေအာင္ခ်မ္းသာရပ္ကြက္ သီရိမဂၤလာလမ္း 
																			<br>ကံျမင့္ေက်ာင္းတိုက္ ဓမၼာရုံ တြင္ေဟာၾကားသည္<br>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/007-BamawSayadaw-Pahtan24Pyitsee-Part1-5-6-2009.mp4">၇။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၁) ၅-၆-၂၀၀၉
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/008-BamawSayadaw-Pahtan24Pyitsee-Part2-6-6-2009.mp4">၈။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၂) ၆-၆-၂၀၀၉
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/009-BamawSayadaw-Pahtan24Pyitsee-Part3-7-6-2009.mp4">၉။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၃) ၇-၆-၂၀၀၉
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/010-BamawSayadaw-Pahtan24Pyitsee-Part4-8-6-2009.mp4">၁၀။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၄) ၈-၆-၂၀၀၉
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/011-BamawSayadaw-Pahtan24Pyitsee-Part5-9-6-2009.mp4">၁၁။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၅) ၉-၆-၂၀၀၉
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/012-BamawSayadaw-Pahtan24Pyitsee-Part6-10-6-2009.mp4">၁၂။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၆) 
									၁၀-၆-၂၀၀၉ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/013-BamawSayadaw-Pahtan24Pyitsee-Part7-11-6-2009.mp4">၁၃။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၇) 
									၁၁-၆-၂၀၀၉ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/014-BamawSayadaw-Pahtan24Pyitsee-Part8-12-6-2009.mp4">၁၄။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၈) 
									၁၂-၆-၂၀၀၉ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/015-BamawSayadaw-Pahtan24Pyitsee-Part9-13-6-2009.mp4">၁၅။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၉) 
									၁၃-၆-၂၀၀၉ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/016-BamawSayadaw-Pahtan24Pyitsee-Part10-14-6-2009.mp4">၁၆။ ပဌာန္းေဒသနာ တရားေတာ္ အပိုင္း(၁၀) 
									၁၄-၆-၂၀၀၉ 
																			</a>
																			<br>
																			<br>မဟာသတိပ႒ာနသုတ္ တရားေတာ္မ်ား<br>ရန္ကုန္တိုင္း စမ္းေခ်ာင္းၿမိဳ႕နယ္ 
									ေအာင္ခ်မ္းသာရပ္ကြက္ သီရိမဂၤလာလမ္း 
																			<br>ကံျမင့္ေက်ာင္းတိုက္ ဓမၼာရုံ တြင္ေဟာၾကားသည္<br>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/017-Bamaw-Sayadaw-Mahathatipahtana-23-1-2010.mp4">၁၇။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁) 
									၂၃-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/018-Bamaw-Sayadaw-Mahathatipahtana-24-1-2010.mp4">၁၈။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂) 
									၂၄-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/019-Bamaw-Sayadaw-Mahathatipahtana-25-1-2010.mp4">၁၉။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၃) 
									၂၅-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/020-Bamaw-Sayadaw-Mahathatipahtana-26-1-2010.mp4">၂၀။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၄) 
									၂၆-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/021-Bamaw-Sayadaw-Mahathatipahtana-27-1-2010.mp4">၂၁။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၅) 
									၂၇-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/022-Bamaw-Sayadaw-Mahathatipahtana-28-1-2010.mp4">၂၂။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၆) 
									၂၈-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/023-Bamaw-Sayadaw-Mahathatipahtana-30-1-2010.mp4">၂၃။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၇) 
									၃၀-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/024-Bamaw-Sayadaw-Mahathatipahtana-31-1-2010.mp4">၂၄။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၈) 
									၃၁-၁-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/025-Bamaw-Sayadaw-Mahathatipahtana-1-2-2010.mp4">၂၅။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၉) 
									၁-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/026-Bamaw-Sayadaw-Mahathatipahtana-2-2-2010.mp4">၂၆။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၀) 
									၂-၂-၂၀၁၀</a><br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/027-Bamaw-Sayadaw-Mahathatipahtana-6-2-2010.mp4">၂၇။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၁) 
									၃-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/028-Bamaw-Sayadaw-Mahathatipahtana-6-2-2010.mp4">၂၈။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၂) 
									၆-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/029-Bamaw-Sayadaw-Mahathatipahtana-7-2-2010.mp4">၂၉။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၃) 
									၇-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/030-Bamaw-Sayadaw-Mahathatipahtana-8-2-2010.mp4">၃၀။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၄) 
									၈-၂-၂၀၁၀ 
																			</a>
																			<br>
																			၃၁။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၅) 
									၉-၂-၂၀၁၀ 
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/032-Bamaw-Sayadaw-Mahathatipahtana-10-2-2010.mp4">၃၂။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၆) 
									၁၀-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/033-Bamaw-Sayadaw-Mahathatipahtana-11-2-2010.mp4">၃၃။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၇) 
									၁၁-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/034-Bamaw-Sayadaw-Mahathatipahtana-12-2-2010.mp4">၃၄။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၈) 
									၁၂-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/035-bamaw-sayadaw-mahathatipahtana-13-2-2010.mp4">၃၅။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၁၉) 
									၁၃-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/036-bamaw-sayadaw-mahathatipahtana-14-2-2010.mp4">၃၆။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂၀) 
									၁၄-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/037-bamaw-sayadaw-mahathatipahtana-15-2-2010.mp4">၃၇။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂၁) 
									၁၅-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/038-bamaw-sayadaw-mahathatipahtana-16-2-2010.mp4">၃၈။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂၂) 
									၁၆-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/039-bamaw-sayadaw-mahathatipahtana-17-2-2010.mp4">၃၉။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂၃) 
									၁၇-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/040-bamaw-sayadaw-mahathatipahtana-18-2-2010.mp4">၄၀။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂၄) 
									၁၈-၂-၂၀၁၀ 
																			</a>
																			<br>
																			<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/041-bamaw-sayadaw-mahathatipahtana-19-2-2010.mp4">၄၁။ မဟာသတိပ႒ာနသုတ္ တရားေတာ္ အပိုင္း(၂၅) 
									၁၉-၂-၂၀၁၀ 
																			</a>
																			<br>
																			&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/Bamaw-Sayadaw-Dr-Bhaddanta-Kumarabhivamsa/old/Bamawsayadawgyi-24-12-2010-thanbuddhaygarhtartaw.mp4">၂၄-၁၂-၂၀၁၀ သဗၺဳေဒၶ ဂါထာေတာ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One"><br>
								&nbsp;</font></p>
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
    
