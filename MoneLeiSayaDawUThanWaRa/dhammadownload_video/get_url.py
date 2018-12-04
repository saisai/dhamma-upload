from bs4 import BeautifulSoup as bs4

text = """
<font face="Zawgyi-One">








 
 
 
 


<p>&nbsp;</p>
<p>&nbsp;</p>
 
 
 
 
<!-- Start dhammadownload menu top and side bar -->

<div style="position: absolute; width: 100px; height: 100px; z-index: 1; left: 7px; top: 4px;" id="layer21">
	<img src="images/Top-button-wt.gif" width="680" height="132" border="0"></div>
<div style="position: absolute; width: 506px; height: 63px; z-index: 2; left: 52px; top: 43px;" id="layer22" align="center">
	<font size="6" color="#800080"><span style="font-family: Times New Roman">
	MoneLei SayaDaw U ThanWaRa</span></font></div>
<div style="position: absolute; width: 100px; height: 100px; z-index: 20; left: 542px; top: 21px;" id="layer23">
	<img src="images/MoneLeiSayaDawUThanWaRa.gif" width="143" height="180" border="0"></div>







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
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
										<span style="FONT-WEIGHT: 700; FONT-FAMILY: Franklin Gothic Medium">
									MoneLei
									SayaDaw U ThanWaRa</span></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
<font face="Zawgyi-One"><font size="5">အေနာက္ဂန္႕ေဂါ မုံလယ္ဆရာေတာ္ 
ဘဒၵႏၲ သံ၀ရ<br>
</font>ေဟာႀကားေတာ္မူေသာတရားေတာ္မ်ား<br>
&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One">ပဲခူး၊ 
									၁၀-မိုင္ကုန္း၊ မုံလယ္ေတာရ ဓမၼရိပ္သာ</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font face="Zawgyi-One">ဖုန္း (၉၅) ၁-၂၄၇၅၇၆</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
										<font size="5" face="Zawgyi-One" color="#0000FF">
										<a href="MoneLeiSayaDawUThanWaRa-news.htm">
									မံုလယ္ေတာရ ဆရာေတာ္ဘုရားႀကီး မႏၲေလးၿမဳိ႕၌ 
									ခႏၶာဝန္ခ် ခ်ဳပ္ၿငိမ္းေတာ္မူ</a></font></p>
<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									**********************************</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								Biography of Agga-maha-Kamathana Cariya Monle 
								Sayadaw<br>
								Bhattanda Bhante Sanvara<br>
								(Mogok Vipassana Meditation Master)<br>
								<br>
								Monle Sayadaw was born on Friday 1am, on the 
								13th Wanning of Nattaw, year 1282 Myanmar 
								Burmese) Era at West Gangaw township. He was 
								named as Maung Wa Thein. Monle Sayadaw’s parents 
								were U Ngwe Tun and Daw Sae Yan. He is the third 
								child among the four siblings. His mother died 
								when he was three. <br>
								<br>
								At the age of fourteen, he was ordained as an 
								sāmanera (novice) under the guidance of his 
								preceptor, Moke-U-Kyaung Sayadaw U Thawbita with 
								the sponsorship of his step-mother - Daw Sae 
								Thawe. He was named sāmanera Ashin Sanvara. 
								After one year he left the sāmanerahood and 
								became a layman. He earned his living as a 
								salesperson. At the age of twenty-four he was 
								married to Daw Chit Myaing from Shone Shi 
								village. He had four children. His wife died 
								when he was the age of 46. He wanted to become a 
								monk even before his wife expired . He had 
								collected the accessories for monkshood and took 
								daily eight precepts since.<br>
								<br>
								After he had fulfilled his duties as a 
								responsible parent and when the children are 
								grown-up and settled, at the age of 56, he was 
								again ordained as an sāmanera under the guidance 
								of Sayadaw U Zagara. <br>
								<br>
								At the age of 57, Ashin Sanvara took higher 
								ordination under the instruction of his 
								preceptor Sayadaw U Thawbita. His higher 
								ordination was sponsored by U Aye Pe and Daw Ohn 
								Kyi. After six vasas, he took Mogok vipassana 
								training under guidance of two meditation 
								masters, Mingala-Kyaung-Taik Sayadaw U Dhamisara 
								of Mandalay Myo-haung, and Myo-Haung Taung-Pyin 
								Taik Sayadaw U Sunmana. <br>
								<br>
								He started his missionary work in April of 1990 
								in Yangon through the sponsorship of his 
								devotees Lt. Major Thet Shay, Dr Jenny Ko Gyi, U 
								Hla Myo and Daw Khin Win Maw. Si-Thu U Ko Gyi 
								and Daw Ahmar. Since then he came to Yangon 
								every year to conduct the meditation course. The 
								devotees temporary donated their residence and 
								compound as the meditation Hall and men and 
								women yogi’s quarters.<br>
								<br>
								Later on U Hla Myo and Daw Khin Win Maw donated 
								six acres of land at Inndagaw Say-mi-gone, Pegu 
								to establish “Monle Sasana Yeitha” meditation 
								center. <br>
								<br>
								Editor and Chief of Dhamma Pictorial Magazine 
								and “The Promotion of Kalayana Puthuzin 
								Association” invited Sayadaw to Yangon to give 
								meditation course every year. He continued to 
								spread Dhamma not only in Yangon but also in 
								Pegu, Mandalay, Taung gyi, Myitkyina and many 
								other cities in Myanmar. He had also traveled to 
								USA and Australia to give meditation courses.<br>
								<br>
								His permanent residence is at Inndagaw 
								Say-mi-gone Sasana Yeittha, Pegu where he gave 
								meditation courses since May of 1997. In 1999 
								Burmese Peace and Development Council honored 
								him Agga-maha Kamathana Cariya.<br>
								*****************************<br>
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<b><font size="6">Dhamma Talk Video</font></b></p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/MoneLeiSayaDawUThanWaRa-ZarPaNa-25-3-3-2011.mp4">
<font size="5">မုံလည္ေတာရ ဆရာေတာ္ဘုရားႀကီး၏ အဂၢိစ်ာပန အခမ္းအနား ဗီဒီယို မွတ္တမ္း</font></a></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
****dhamma talks uploaded and published on 10 August 2009****<font size="4" face="Zawgyi-One"><br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-5-8-2008-2PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၅-၈-၂၀၀၈ 
								ေနလည္၂နာရီ အိုးကဲြပန္းကန္ကြဲ ျဖစ္ပ်က္ဥပမာျပ 
								ခႏၶာဉာဏ္ေရာက္ဒိဌိျဖဳတ္တရားေတာ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-13-12-2008-3PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၃-၁၂-၂၀၀၈ 
								ညေန၃နာရီ ပရိညာသုံးပါး</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-13-12-2008-7PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၃-၁၂-၂၀၀၈ ည 
								၇နာရီ အဝိဇၨာႏွင့္ တဏွာ</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-14-12-2008-8AM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၄-၁၂-၂၀၀၈ 
								နံနက္ အာရုံမွနိမွ သဒၵါမွန္တယ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-14-12-2008-3PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၄-၁၂-၂၀၀၈ 
								ေန႕လည္၃နာရီ ခႏၶာ႕ ပဋိစၥသမုပၸါဒ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-14-12-2008-7PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၄-၁၂-၂၀၀၈ 
								ညေန၇နာရီ&nbsp; မယ္ပဋာအေၾကာင္းဥပမာျပ 
								ခႏၶာဉာဏ္ေရာက္ ဒိဌိျပဳတ္တရားေတာ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-15-12-2008-3PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၅-၁၂-၂၀၀၈ 
								ေန႕လည္၃နာရီ ခႏၶာငါးပါး သူသတ္ေယာက်ာၤး 
								(စုန္းမဥပမာျပ)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-15-12-2008-7PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၅-၁၂-၂၀၀၈ 
								ညေန၇နာရီ သကၠာယဒိဌိျပဳတ္ပုံ</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-6-4-2008-2PM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၆-၄-၂၀၀၈ ေန႕လည္၂နာရီ အဝိဇၨာဦးစီးပုံႏွင့္ 
								တဏွာဦးစီးပုံ ခႏၶာဉာဏ္ေရာက္ ဒိဌိျပဳတ္တရားေတာ္</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4" face="Zawgyi-One">
								<a href="http://dhammadownload.com//MP4Library/MoneLei/2008/MoneLeiSayaDawUThanWaRa-2-9-2008-AM.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၂-၉-၂၀၀၈ နံနက္၇နာရီ&nbsp; သီလေပးႏွင့္ ပညတ္ပရမတ္ 
								ခြဲျခားျပပုံ</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								*********************************************</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
****dhamma talks uploaded and published on 18 Nov 2011****</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">အလုပ္ေပးတရားေတာ္ (၁၅)ပုဒ္ </font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4"><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/01-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁။ အ၀ိဇၨာဦးစီးပံုႏွင့္တဏွာဦးစီးပံု</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/02-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၂။ အိုးကြဲ၊ပုဂံကြဲ၊ျဖစ္ပ်က္ဥပမာျပ</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/03-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၃။ ႏွလံုးသြင္းမွန္ပံုႏွင့္ႏွလံုးသြင္းမွားပံု</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/04-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၄။ အထင္ႏွင့္အယူအဆကိုပယ္တာ</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/05-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၅။ ၿမိဳ႕စြဲ၊အိမ္စြဲ၊လူစြဲ ဒိဌိျဖဳတ္</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/06-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၆။ ပဋိစၥသမုပၸါဒ္ျပတ္ပံုသံုးမ်ိဳးအေၾကာင္း</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/07-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၇။ ႏွလံုးသြင္းမွားတာႏွင့္မွန္တာ</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/08-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၈။ သီလေပးႏွင့္ပညတ္ပရမတ္ခြဲျပပံု</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/09-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၉။ ခ်စ္မုန္းမပါလင္ကြာမယားကြာ</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/10-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၀။ ေလာကသတိႆရဟန္းအေၾကာင္း</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/11-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၁။ မယ္ပဋာအေၾကာင္း</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/12-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၂။ မာဃလုလင္ႏွင့္သုဇာတာအေၾကာင္း</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/13-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၃။ ေစတနာအတိုင္းအက်ိဳးေပးပံု</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/14-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၄။ ရွင္စူဠပန္အေၾကာင္း</a><br>
								<a href="http://dhammadownload.com//MP4Library/MoneLei/DVD-01/15-MoneLeiSayadawGyi-DVD01.mp4" title="To download to your hard disc, please right click and choose &quot;save target as&quot;.">၁၅။ ဆြမ္းဒကာတိႆအေၾကာင္း</a><br>
								<br>
								<br>
								&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								*********************************************</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
****dhamma talks uploaded and published on 11 Nov 2012****</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">ေက်းဇူးေတာ္ရွင္ 
								မုံလည္ဆရာေတာ္ဘုရားႀကီး </font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">Thanti-Thitsar (LA) &amp; A.B.B.a 
								(NJ)</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">Meditation Centers, USA</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">L.A ၿမိဳ႕ သႏိ ၱသစၥာ ဝိပႆနာ 
								ဓမၼရိပ္သာ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">N.J ၿမိဳ႕ A.B.B.A 
								ဓမၼရိပ္သာတို႕တြင္</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">၂၀၀၅ ေမလ ၂၂ ရက္ေန႕မွ ေမလ ၃၁ 
								ရက္ေန႕ထိ</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-14-8am.mp4">
								၁၄-၀၅-၂၀၀၅ နံနက္ ၈နာရီ Thanti-Thitsar (LA)</a><br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-14-7pm.mp4">
								၁၄-၀၅-၂၀၀၅ ညေန ၇နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-15-2pm.mp4">
								၁၅-၀၅-၂၀၀၅ ေန႕လည္္ ၂နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-16-8am.mp4">
								၁၆-၀၅-၂၀၀၅ နံနက္ ၈နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-16-7pm.mp4">
								၁၆-၀၅-၂၀၀၅ ညေန ၇နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-17-2pm.mp4">
								၁၇-၀၅-၂၀၀၅ ေန႕လည္္ ၂နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-18-8am.mp4">
								၁၈-၀၅-၂၀၀၅ နံနက္ ၈နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-18-7pm.mp4">
								၁၈-၀၅-၂၀၀၅ ညေန ၇နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-19-2pm.mp4">
								၁၉-၀၅-၂၀၀၅ ေန႕လည္္ ၂နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-20-8am.mp4">
								၂၀-၀၅-၂၀၀၅ နံနက္ ၈နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-20-7pm.mp4">
								၂၀-၀၅-၂၀၀၅ ညေန ၇နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-21-2pm.mp4">
								၂၁-၀၅-၂၀၀၅ ေန႕လည္္ ၂နာရီ Thanti-Thitsar (LA)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px" align="left">
								<font size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP4Library/MoneLei/2005/Monleisayadawgyi-2005-05-22-1230pm.mp4">
								၂၂-၀၅-၂၀၀၅ ေန႕လည္္ ၁၂း၃၀ နာရီ Thanti-Thitsar 
								(LA)</a></font></p>
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
    
