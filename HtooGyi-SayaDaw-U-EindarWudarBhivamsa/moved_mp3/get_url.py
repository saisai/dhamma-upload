from bs4 import BeautifulSoup as bs4

text = """
<div style="position: absolute; width: 964px; height: 2070px; z-index: 21; left: 219px; top: 149px" id="layer24" font face="Zawgyi-One">
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
										<span style="FONT-WEIGHT: 700; FONT-FAMILY: Franklin Gothic Medium">
									Htoo Gyi
									SayaDaw </span></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									<font size="4">
									U Aeinda Wuda Bewon Tha</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font face="Zawgyi-One" size="4">
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4102;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153;&#4120;&#4143;&#4123;&#4140;&#4152;&#4224;&#4096;&#4142;&#4152;&#4175; &#4133;&#4117;&#4116;&#4141;&#4126;&#4123;&#4097;&#4150;<br>
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140;&#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153;&#4155;&#4117;&#4116;&#4153;&#4245;&#4117;&#4156;&#4140;&#4152;&#4145;&#4123;&#4152;&#4129;&#4118;&#4156;&#4146;&#4245;&#4097;&#4154;&#4147;&#4117;&#4153;&#4224;&#4096;&#4142;&#4152;&#4175; &#4116;&#4140;&#4122;&#4096;<br>
								<br>
								</font><font face="Zawgyi-One" size="5">
								&#4113;&#4144;&#4152;&#4224;&#4096;&#4142;&#4152;&#4102;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153; &#4133;&#4142;&#4152;&#4131;&#4239;&#4213;&#4140;&#4125;&#4143;&#4115;&#4140;&#4120;&#4141;&#4125;&#4150;&#4126;</font><font face="Zawgyi-One" size="4"><br>
								<br>
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140; &#4145;&#4103;&#4112;&#4125;&#4116;&#4153;&#4145;&#4096;&#4154;&#4140;&#4100;&#4153;&#4152;&#4112;&#4141;&#4143;&#4096;&#4153;<br>
								&#4126;&#4121;&#4140;&#4115;&#4141;&#4124;&#4121;&#4153;&#4152;&#4170; &#4113;&#4144;&#4152;&#4224;&#4096;&#4142;&#4152;&#4223;&#4121;&#4141;&#4147;&#4245; &#4129;&#4098;&#4196;&#4117;&#4144;&#4223;&#4121;&#4141;&#4147;&#4245;&#4116;&#4122;&#4153;<br>
								&#4127;&#4126;&#4196;&#4140;&#4112;&#4097;&#4123;&#4141;&#4143;&#4100;&#4153;&#4170; &#4135;&#4123;&#4140;&#4125;&#4112;&#4142;&#4112;&#4141;&#4143;&#4100;&#4153;&#4152;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">&#4160;&#4169;-&#4168;&#4165;&#4168;&#4161;&#4163;&#4169;&#4162;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">&#4160;&#4164;&#4164;-&#4163;&#4163;&#4160;&#4160;&#4161;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<font size="4">&#4160;&#4164;&#4164;-&#4163;&#4163;&#4162;&#4163;&#4166;</font><font face="Zawgyi-One" size="4"><br>
								<br>
								&#4145;&#4127;&#4140;&#4224;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4145;&#4126;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
&nbsp;</font></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								&nbsp;</p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b><font size="5">Dhamma Talk Audio</font></b></p>
								<p class="MsoNormal" style="margin-top: 0; margin-bottom: 0">
								<b>&nbsp;</b></p>
                                <p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font size="4">The following lists are 
									the high quality audio file in MP3 format.</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font size="4">Please be note that the 
									average file size for MP3 is about 70MBytes</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font size="4">and it may take time to 
									download.</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font size="4">If you are listening the 
									audio on-line, it is recommended to listen
									</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font size="4">the low bandwidth 
									window media 
									audio format. 
									<a href="HtooGyi-SayaDaw-U-EindarWudarBhivamsa-wma.htm">Please click here.</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
								<font face="Zawgyi-One" size="4">
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&nbsp;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;</font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									&nbsp;</p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/001-HtooGyi-SayaDaw-Alokpay-1.mp3">&#4161;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; - &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4102;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153;&#4224;&#4096;&#4142;&#4152;&#4175; 
									&#4133;&#4117;&#4116;&#4141;&#4126;&#4122; &#4155;&#4118;&#4101;&#4153;&#4117;&#4154;&#4096;&#4153;&#4123;&#4232; &#4123;&#4157;&#4100;&#4153;&#4152;&#4112;&#4121;&#4153;&#4152; (&#4161;)</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/002-HtooGyi-SayaDaw-Alokpay-2.mp3">&#4162;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; - &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4102;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153;&#4224;&#4096;&#4142;&#4152;&#4175; 
									&#4133;&#4117;&#4116;&#4141;&#4126;&#4122; &#4155;&#4118;&#4101;&#4153;&#4117;&#4154;&#4096;&#4153;&#4123;&#4232; &#4123;&#4157;&#4100;&#4153;&#4152;&#4112;&#4121;&#4153;&#4152; (&#4162;)</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/003-HtooGyi-SayaDaw-Alokpay-3.mp3">&#4163;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; - &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4102;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153;&#4224;&#4096;&#4142;&#4152;&#4175; 
									&#4133;&#4117;&#4116;&#4141;&#4126;&#4122; &#4155;&#4118;&#4101;&#4153;&#4117;&#4154;&#4096;&#4153;&#4123;&#4232; &#4123;&#4157;&#4100;&#4153;&#4152;&#4112;&#4121;&#4153;&#4152; (&#4163;)</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/004-HtooGyi-SayaDaw-Apetankhapaetnavanpwint.mp3">&#4164;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4164;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/005-HtooGyi-SayaDaw-Ariyamatgawijjar.mp3">
									&#4165;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4165;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/006-HtooGyi-SayaDaw-bawathocyinkatchyin.mp3">
									&#4166;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4166;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/007-HtooGyi-SayaDaw-HtwatmyoutyaAlokpay.mp3">
									&#4167;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4167;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/008-HtooGyi-SayaDaw-janapatsa.mp3">
									&#4168;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4168;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/009-HtooGyi-SayaDaw-Rintkyatseikhtar.mp3">
									&#4169;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4169;)&nbsp; 
									&#4123;&#4100;&#4153;&#4151;&#4096;&#4154;&#4096;&#4153;&#4101;&#4141;&#4112;&#4153;&#4113;&#4140;&#4152;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/010-HtooGyi-SayaDaw-Sakhonodapadi.mp3">
									&#4161;&#4160;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4160;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/011-HtooGyi-SayaDaw-Samasana2.mp3">
									&#4161;&#4161;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4161;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/012-HtooGyi-SayaDaw-Seitanupisana.mp3">
									&#4161;&#4162;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4162;) 
									&#4101;&#4141;&#4112;&#4209;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/013-HtooGyi-SayaDaw-Seitarnupathana.mp3">
									&#4161;&#4163;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4163;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/014-HtooGyi-SayaDaw-ShuywarponAlokpay.mp3">
									&#4161;&#4164;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4164;) 
									&#4123;&#4232;&#4117;&#4156;&#4140;&#4152;&#4117;&#4143;&#4150;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/015-HtooGyi-SayaDaw-Thamathana-1.mp3">
									&#4161;&#4165;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4165;)&nbsp;&nbsp;
									</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/016-HtooGyi-SayaDaw-ThatipahtanaBarwana.mp3">
									&#4161;&#4166;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4166;) 
									&#4126;&#4112;&#4141;&#4117;&#4242;&#4140;&#4116; &#4120;&#4140;&#4125;&#4116;&#4140;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/017-HtooGyi-SayaDaw-Thatipahtarnabawana.mp3">
									&#4161;&#4167;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4167;) 
									&#4126;&#4112;&#4141;&#4117;&#4242;&#4140;&#4116; &#4120;&#4140;&#4125;&#4116;&#4140;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/018-HtooGyi-SayaDaw-Thatipaxan.mp3">
									&#4161;&#4168;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4168;) 
									&#4126;&#4112;&#4141;&#4117;&#4242;&#4140;&#4116;&#4153;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/019-HtooGyi-SayaDaw-Waydananupathana.mp3">
									&#4161;&#4169;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;&#4169;) 
									&#4145;&#4125;&#4114;&#4116;&#4140;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0; TEXT-ALIGN: left">
									<font face="Zawgyi-One" size="4">
									<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://www.dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/AhLoakPay/020-HtooGyi-SayaDaw-YahtabutaNyan.mp3">
									&#4162;&#4160;&#4171; 
									&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4162;&#4160;) 
									&#4122;&#4113;&#4140;&#4120;&#4144;&#4112;&#4133;&#4140;&#4111;&#4153;</a></font></p>
								<p class="MsoTagline" style="MARGIN-TOP: 0px; TEXT-KASHIDA-SPACE: 50%; MARGIN-BOTTOM: 0px; TEXT-ALIGN: left">
								<font face="Zawgyi-One" size="4">
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<b><font size="5">MP3 DVD Disc 1</font></b></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4"><br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4145;&#4129;&#4140;&#4100;&#4153;&#4117;&#4116;&#4153;&#4152;&#4223;&#4121;&#4141;&#4147;&#4245; &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140;&#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153;&#4155;&#4117;&#4116;&#4153;&#4245;&#4117;&#4156;&#4140;&#4152;&#4145;&#4123;&#4152; &#4129;&#4118;&#4156;&#4146;&#4245;&#4097;&#4156;&#4146; &#4129;&#4121;&#4157;&#4112;&#4153;&#4153; (&#4163;&#4162;&#4169;)&#4121;&#4157; 
								&#4096;&#4154;&#4100;&#4153;&#4152;&#4117;&#4155;&#4117;&#4147;&#4124;&#4143;&#4117;&#4153;&#4129;&#4117;&#4153;&#4145;&#4126;&#4140; (&#4162;&#4162;)&#4224;&#4096;&#4141;&#4121;&#4153;&#4145;&#4155;&#4121;&#4140;&#4096;&#4153; 
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140; (&#4161;&#4160;)&#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152;&#4117;&#4156;&#4146; &#4172; 
								&#4145;&#4127;&#4140;&#4224;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4145;&#4126;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/001-HtooGyiSayadaw-8-6-2005-AM.mp3">
								&#4161;&#4171; &#4168;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4096;&#4121;&#4220;&#4230;&#4096;&#4112;&#4133;&#4140;&#4111;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4126;&#4101;&#4197;&#4140;&#4239;&#4143;&#4145;&#4124;&#4140;&#4121;&#4141;&#4096;&#4133;&#4140;&#4111;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/002-HtooGyiSayadaw-8-6-2005-PM.mp3">
								&#4162;&#4171; &#4168;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4145;&#4123;&#4157;&#4245;&#4145;&#4123;&#4152;&#4096;&#4141;&#4143;&#4145;&#4121;&#4157;&#4154;&#4140;&#4153;&#4117;&#4139; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/003-HtooGyiSayadaw-9-6-2005-AM.mp3">
								&#4163;&#4171; &#4169;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4096;&#4150;&#4112;&#4123;&#4140;&#4152;&#4175; &#4102;&#4116;&#4153;&#4152;&#4222;&#4096;&#4122;&#4153;&#4117;&#4150;&#4143; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/004-HtooGyiSayadaw-9-6-2005-PM.mp3">
								&#4164;&#4171; &#4169;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4096;&#4122;&#4153;&#4126;&#4144;&#4102;&#4122;&#4153;&#4126;&#4144; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/005-HtooGyiSayadaw-10-6-2005-AM.mp3">
								&#4165;&#4171; &#4161;&#4160;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4125;&#4107;&#4153;&#4121;&#4157;&#4140;&#4129;&#4223;&#4121;&#4146; &#4100;&#4123;&#4146;&#4121;&#4157;&#4140;&#4129;&#4117; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/006-HtooGyiSayadaw-10-6-2005-PM.mp3">
								&#4166;&#4171; &#4161;&#4160;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/007-HtooGyiSayadaw-11-6-2005-AM.mp3">
								&#4167;&#4171; &#4161;&#4161;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4126;&#4121;&#4100;&#4153;&#4145;&#4121;&#4156;&#4152;&#4123;&#4100;&#4153;&#4152; &#4096;&#4154;&#4140;&#4152;&#4101;&#4140;&#4152;&#4123;&#4100;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/008-HtooGyiSayadaw-11-6-2005-PM.mp3">
								&#4168;&#4171; &#4161;&#4161;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4123;&#4112;&#4116;&#4140;&#4101;&#4141;&#4116;&#4153;&#4145;&#4096;&#4154;&#4140;&#4096;&#4153; 
								&#4103;&#4122;&#4153;&#4145;&#4112;&#4140;&#4096;&#4153;&#4153;&#4222;&#4096;&#4123;&#4145;&#4129;&#4140;&#4100;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/009-HtooGyiSayadaw-12-6-2005-AM.mp3">
								&#4169;&#4171; &#4161;&#4162;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;-&#4165;&#4101;&#4100;&#4153;&#4152; &#4129;&#4124;&#4100;&#4153;&#4152;-&#4165;&#4097;&#4154;&#4096;&#4153; (&#4096;&#4121;&#4220;&#4230;&#4096;&#4112;&#4133;&#4140;&#4111;&#4153;&#4121;&#4157;&#4140; 
								&#4118;&#4143;&#4150;&#4152;&#4113;&#4140;&#4152;&#4145;&#4126;&#4140;&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;) &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/010-HtooGyiSayadaw-12-6-2005-PM.mp3">
								&#4161;&#4160;&#4171; &#4161;&#4162;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/011-HtooGyiSayadaw-13-6-2005-AM.mp3">
								&#4161;&#4161;&#4171; &#4161;&#4163;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;-&#4165;&#4101;&#4100;&#4153;&#4152; &#4129;&#4124;&#4100;&#4153;&#4152;-&#4165;&#4097;&#4154;&#4096;&#4153; &#4129;&#4102;&#4096;&#4153; 
								(&#4116;&#4140;&#4121;&#4153;&#4123;&#4143;&#4117;&#4153;&#4145;&#4117;&#4186;&#4121;&#4157;&#4140;&#4118;&#4143;&#4150;&#4152;&#4113;&#4140;&#4152;&#4145;&#4126;&#4140;&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153; &#4117;&#4133;&#4197;&#4096; 
								&#4114;&#4139;&#4122;&#4096;&#4117;&#4143;&#4241;&#4140;&#4152;&#4133;&#4117;&#4121;&#4140;&#4155;&#4117;) &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/012-HtooGyiSayadaw-13-6-2005-PM.mp3">
								&#4161;&#4162;&#4171; &#4161;&#4163;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4145;&#4226;&#4096;&#4156;&#4152;&#4112;&#4100;&#4153;&#4123;&#4100;&#4153; 
								&#4121;&#4098;&#4194;&#4100;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151;&#4102;&#4117;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/013-HtooGyiSayadaw-14-6-2005-AM.mp3">
								&#4161;&#4163;&#4171; &#4161;&#4164;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>(&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;-&#4165;&#4101;&#4100;&#4153;&#4152; &#4129;&#4124;&#4100;&#4153;&#4152;-&#4165;&#4097;&#4154;&#4096;&#4153; &#4129;&#4102;&#4096;&#4153; (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; 
								&#4145;&#4117;&#4186;&#4121;&#4157;&#4140;&#4118;&#4143;&#4150;&#4152;&#4113;&#4140;&#4152;&#4145;&#4126;&#4140;&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;) &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/014-HtooGyiSayadaw-14-6-2005-PM.mp3">
								&#4161;&#4164;&#4171; &#4161;&#4164;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - 
								&#4129;&#4141;&#4143;&#4145;&#4129;&#4140;&#4100;&#4153;&#4121;&#4100;&#4153;&#4152;&#4145;&#4129;&#4140;&#4100;&#4153;&#4145;&#4117;&#4139;&#4100;&#4153;&#4152;&#4222;&#4096;&#4117;&#4139;&#4145;&#4101; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/015-HtooGyiSayadaw-15-6-005-AM.mp3">
								&#4161;&#4165;&#4171; &#4161;&#4165;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;-&#4165;&#4101;&#4100;&#4153;&#4152; &#4129;&#4124;&#4100;&#4153;&#4152;-&#4165;&#4097;&#4154;&#4096;&#4153; &#4129;&#4102;&#4096;&#4153; 
								(&#4124;&#4096;&#4193;&#4111;&#4133;&#4140;&#4111;&#4153;&#4121;&#4157;&#4140;&#4118;&#4143;&#4150;&#4152;&#4113;&#4140;&#4152;&#4145;&#4126;&#4140;&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;) &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/016-HtooGyiSayadaw-15-6-2005-PM.mp3">
								&#4161;&#4166;&#4171; &#4161;&#4165;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4129;&#4112;&#4156;&#4122;&#4153;&#4129;&#4112;&#4140; &#4129;&#4121;&#4157;&#4112;&#4153;(&#4161;) 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/017-HtooGyiSayadaw-16-6-2005-AM.mp3">
								&#4161;&#4167;&#4171; &#4161;&#4166;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;-&#4165;&#4101;&#4100;&#4153;&#4152; &#4129;&#4124;&#4100;&#4153;&#4152;-&#4165;&#4097;&#4154;&#4096;&#4153; &#4129;&#4102;&#4096;&#4153; 
								(&#4126;&#4101;&#4197;&#4133;&#4140;&#4111;&#4153;&#4121;&#4157;&#4140;&#4118;&#4143;&#4150;&#4152;&#4113;&#4140;&#4152;&#4145;&#4126;&#4140;&#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;) &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/018-HtooGyiSayadaw-16-6-2005-PM.mp3">
								&#4161;&#4168;&#4171; &#4161;&#4166;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4129;&#4112;&#4156;&#4122;&#4153;&#4129;&#4112;&#4140; &#4129;&#4121;&#4157;&#4112;&#4153;(&#4162;) 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/019-HtooGyiSayadaw-17-6-2005-AM.mp3">
								&#4161;&#4169;&#4171; &#4161;&#4167;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- (&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								&#4145;&#4124;&#4140;&#4100;&#4153;&#4101;&#4140;&#4126;&#4141;&#4121;&#4153;&#4152; &#4121;&#4142;&#4152;&#4223;&#4100;&#4141;&#4121;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/020-HtooGyiSayadaw-17-6-2005-PM.mp3">
								&#4162;&#4160;&#4171; &#4161;&#4167;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4166; &#4129;&#4141;&#4121;&#4153;&#4112;&#4116;&#4153;&#4152;&#4123;&#4156;&#4140; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140; &#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151;&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153; 
								&#4155;&#4117;&#4116;&#4153;&#4245;&#4117;&#4156;&#4140;&#4152;&#4145;&#4123;&#4152; &#4129;&#4118;&#4156;&#4146;&#4245;&#4097;&#4154;&#4147;&#4117;&#4153;&#4224;&#4096;&#4142;&#4152;&#4172; 
								(&#4161;&#4160;)&#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152;&#4117;&#4156;&#4146;&#4112;&#4156;&#4100;&#4153; 
								&#4145;&#4127;&#4140;&#4224;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4145;&#4126;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/021-HtooGyiSayadaw-20-11-005-AM.mp3">
								&#4162;&#4161;&#4171; &#4162;&#4160;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4239;&#4143;&#4170; &#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121; 
								&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;) <br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/022-HtooGyiSayadaw-20-11-2005-PM.mp3">
								&#4162;&#4162;&#4171; &#4162;&#4160;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4124;&#4140;&#4155;&#4097;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4173; 
								&#4155;&#4117;&#4116;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4117;&#4139;&#4145;&#4101; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/023-HtooGyiSayadaw-21-11-2005-AM.mp3">
								&#4162;&#4163;&#4171; &#4162;&#4161;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4239;&#4143;&#4170; &#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121; 
								&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4162;) <br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/024-HtooGyiSayadaw-21-11-2005-PM.mp3">
								&#4162;&#4164;&#4171; &#4162;&#4161;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4097;&#4143;&#4123;&#4232; &#4097;&#4143;&#4223;&#4100;&#4141;&#4121;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/025-HtooGyiSayadaw-22-11-2005-AM.mp3">
								&#4162;&#4165;&#4171; &#4162;&#4162;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4160;&#4107;&#4153;&#4121;&#4157;&#4140;&#4129;&#4223;&#4121;&#4146; &#4100;&#4123;&#4146;&#4121;&#4157;&#4140;&#4129;&#4117; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/026-HtooGyiSayadaw-22-11-2005-PM.mp3">
								&#4162;&#4166;&#4171; &#4162;&#4162;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4101;&#4141;&#4112;&#4153;&#4175;&#4102;&#4116;&#4153;&#4222;&#4096;&#4122;&#4153;&#4117;&#4143;&#4150; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/027-HtooGyiSayadaw-23-11-2005-AM.mp3">
								&#4162;&#4167;&#4171; &#4162;&#4163;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4121;&#4100;&#4153;&#4145;&#4121;&#4156;&#4152;&#4123;&#4100;&#4153;&#4152; 
								&#4096;&#4154;&#4140;&#4152;&#4101;&#4140;&#4152;&#4123;&#4100;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/028-HtooGyiSayadaw-23-11-2005-PM.mp3">
								&#4162;&#4168;&#4171; &#4162;&#4163;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4129;&#4116;&#4112;&#4209;&#4121;&#4154;&#4096;&#4153;&#4124;&#4143;&#4150;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/029-HtooGyiSayadaw-24-11-2005-AM.mp3">
								&#4162;&#4169;&#4171; &#4162;&#4164;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4112;&#4209;&#4141;&#4239;&#4157;&#4100;&#4153;&#4151; &#4119;&#4154;&#4112;&#4209;&#4141; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/030-HtooGyiSayadaw-24-11-2005-PM.mp3">
								&#4163;&#4160;&#4171; &#4162;&#4164;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4145;&#4226;&#4096;&#4156;&#4152;&#4112;&#4100;&#4153;&#4123;&#4100;&#4153; &#4121;&#4098;&#4194;&#4100;&#4153;&#4116;&#4146;&#4245;&#4102;&#4117;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/031-HtooGyiSayadaw-25-11-2005-AM.mp3">
								&#4163;&#4161;&#4171; &#4162;&#4165;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4120;&#4160;&#4145;&#4123;&#4101;&#4096;&#4153;&#4239;&#4157;&#4100;&#4153; &#4115;&#4121;&#4220;&#4101;&#4096;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/032-HtooGyiSayadaw-25-11-2005-PM.mp3">
								&#4163;&#4162;&#4171; &#4162;&#4165;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4123;&#4112;&#4116;&#4140;&#4101;&#4141;&#4116;&#4153;&#4145;&#4096;&#4154;&#4140;&#4096;&#4153; 
								&#4103;&#4122;&#4153;&#4145;&#4112;&#4140;&#4096;&#4153;&#4112;&#4116;&#4153;&#4152; &#4096;&#4101;&#4140;&#4152; &#4123;&#4145;&#4129;&#4140;&#4100;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/033-HtooGyiSayadaw-26-11-2005-AM.mp3">
								&#4163;&#4163;&#4171; &#4162;&#4166;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4097;&#4239;&#4214;&#4140;&#4129;&#4101;&#4133;&#4153; 
								&#4133;&#4140;&#4111;&#4153;&#4160;&#4100;&#4153;&#4155;&#4118;&#4112;&#4153;&#4117;&#4143;&#4150; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/034-HtooGyiSayadaw-26-11-2005-PM.mp3">
								&#4163;&#4164;&#4171; &#4162;&#4166;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4145;&#4112;&#4124;&#4117;&#4112;&#4209;&#4103;&#4140;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/035-HtooGyiSayadaw-27-11-2005-AM.mp3">
								&#4163;&#4165;&#4171; &#4162;&#4167;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4116;&#4140;&#4113;&#4117;&#4141;&#4241;&#4141;&#4145;&#4096;&#4140;&#4160;&#4139;&#4114;&#4126;&#4143;&#4112;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/036-HtooGyiSayadaw-27-11-2005-PM.mp3">
								&#4163;&#4166;&#4171; &#4162;&#4167;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4145;&#4112;&#4124;&#4117;&#4112;&#4209;&#4103;&#4140;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/037-HtooGyiSayadaw-28-11-2005-AM.mp3">
								&#4163;&#4167;&#4171; &#4162;&#4168;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4160;&#4096;&#4192;&#4124;&#4141;&#4121;&#4145;&#4113;&#4123;&#4153;&#4160;&#4112;&#4211;&#4147; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/038-HtooGyiSayadaw-28-11-2005-PM.mp3">
								&#4163;&#4168;&#4171; &#4162;&#4168;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; </a>- &#4145;&#4112;&#4124;&#4117;&#4112;&#4209;&#4103;&#4140;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4163;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/039-HtooGyiSayadaw-29-11-2005-AM.mp3">
								&#4163;&#4169;&#4171; &#4162;&#4169;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; </a>- &#4124;&#4121;&#4153;&#4102;&#4143;&#4150;&#4152;&#4124;&#4157;&#4154;&#4100;&#4153;&#4123;&#4156;&#4140;&#4145;&#4112;&#4156;&#4245; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/040-HtooGyiSayadaw-29-11-2005-PM.mp3">
								&#4164;&#4160;&#4171; &#4162;&#4169;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116;</a> - &#4126;&#4101;&#4197;&#4133;&#4140;&#4111;&#4153;&#4121;&#4157;&#4140; 
								&#4133;&#4142;&#4152;&#4097;&#4141;&#4143;&#4096;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140; &#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151;&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153; 
								&#4155;&#4117;&#4116;&#4153;&#4245;&#4117;&#4156;&#4140;&#4152;&#4145;&#4123;&#4152; &#4129;&#4118;&#4156;&#4146;&#4245;&#4097;&#4154;&#4147;&#4117;&#4153;&#4224;&#4096;&#4142;&#4152;&#4172; 
								(&#4165;)&#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152;&#4117;&#4156;&#4146;&#4112;&#4156;&#4100;&#4153; 
								&#4145;&#4127;&#4140;&#4224;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4145;&#4126;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/041-HtooGyiSayadaw-7-9-2006-am.mp3">
								&#4164;&#4161;&#4171; &#4167;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4124;&#4121;&#4153;&#4152;&#4101;&#4133;&#4153; 
								&#4145;&#4123;&#4157;&#4245;&#4096;&#4223;&#4118;&#4101;&#4153;&#4117;&#4154;&#4096;&#4153;&#4170;&#4145;&#4116;&#4140;&#4096;&#4153;&#4096; &#4121;&#4098;&#4153;&#4170; &#4145;&#4122;&#4140;&#4116;&#4141;&#4145;&#4126;&#4140; &#4121;&#4116;&#4126;&#4141;&#4096;&#4140;&#4123; &#4116;&#4146;&#4244; 
								&#4117;&#4106;&#4140;&#4116;&#4146;&#4244; &#4129;&#4112;&#4144;&#4112;&#4144;&#4117;&#4139;&#4120;&#4146; &#4129;&#4102;&#4141;&#4143;&#4096;&#4141;&#4143; &#4123;&#4157;&#4100;&#4153;&#4152;&#4124;&#4100;&#4153;&#4152;&#4223;&#4097;&#4100;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/042-HtooGyiSayadaw-7-9-2006-3pm.mp3">
								&#4164;&#4162;&#4171; &#4167;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4120;&#4125;&#4222;&#4096;&#4142;&#4152; (&#4169;)&#4121;&#4154;&#4147;&#4141;&#4152;&#4170;&#4120;&#4125;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4097;&#4239;&#4214;&#4140;&#4170;&#4120;&#4125;&#4114;&#4143;&#4096;&#4193;&#4170;&#4097;&#4239;&#4214;&#4140; 
								&#4114;&#4143;&#4096;&#4193;&#4170;&#4145;&#4124;&#4140;&#4096;&#4142;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4170;&#4145;&#4124;&#4140;&#4096;&#4143;&#4112;&#4209;&#4123;&#4140;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4170;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/043-HtooGyiSayadaw-8-9-2006-am.mp3">
								&#4164;&#4163;&#4171; &#4168;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4150;&#4099;&#4140;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152; &#4129;&#4112;&#4156;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197; 
								&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171; (&#4161;)&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4124;&#4121;&#4153;&#4152;&#4101;&#4133;&#4153; 
								&#4121;&#4157;&#4140;&#4120;&#4143;&#4123;&#4140;&#4152;&#4096;&#4156;&#4122;&#4153; &#4145;&#4116;&#4112;&#4122;&#4153;&#4102;&#4141;&#4143;&#4112;&#4146;&#4151; &#4101;&#4156;&#4117;&#4153;&#4101;&#4156;&#4146;&#4097;&#4154;&#4096;&#4153;&#4096;&#4141;&#4143; 
								&#4145;&#4155;&#4118;&#4123;&#4157;&#4100;&#4153;&#4152;&#4170; (&#4162;)&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4124;&#4121;&#4153;&#4152;&#4101;&#4133;&#4153; &#4126;&#4106;&#4153; &#4133;&#4140;&#4111;&#4153;&#4101;&#4133;&#4153;&#4117;&#4122;&#4153;&#4112;&#4146;&#4151; 
								&#4124;&#4121;&#4153;&#4152;&#4101;&#4133;&#4153; &#4101;&#4156;&#4117;&#4153;&#4101;&#4156;&#4146;&#4097;&#4154;&#4096;&#4153;&#4153;&#4096;&#4141;&#4143; &#4145;&#4155;&#4118;&#4123;&#4157;&#4100;&#4153;&#4152;&#4170; (&#4163;) 
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4125;&#4139;&#4114; &#4096;&#4141;&#4143;&#4129;&#4115;&#4121;&#4220; &#4125;&#4139;&#4114;&#4124;&#4141;&#4143;&#4244;&#4101;&#4156;&#4117;&#4153;&#4101;&#4156;&#4146;&#4097;&#4154;&#4096;&#4153;&#4096;&#4141;&#4143; 
								&#4145;&#4155;&#4118;&#4123;&#4157;&#4100;&#4153;&#4152;&#4170;&quot;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/044-HtooGyiSayadaw-8-9-2006-3pm.mp3">
								&#4164;&#4164;&#4171; &#4168;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4112;&#4111;&#4157;&#4140;&#4113;&#4096;&#4153; &#4114;&#4141;&#4242;&#4141;&#4096; 
								&#4117;&#4141;&#4143;&#4145;&#4222;&#4096;&#4140;&#4096;&#4153;&#4118;&#4141;&#4143;&#4244;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4117;&#4150;&#4143;&#4171;&#4112;&#4111;&#4157;&#4143;&#4140;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4170; &#4126;&#4114;&#4213;&#4139;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4170; 
								&#4126;&#4150;&#4145;&#4125;&#4098;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4170; &#4126;&#4121;&#4140;&#4115;&#4141;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4170;&#4117;&#4106;&#4140;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4171; &#4097;&#4239;&#4214;&#4140; 
								&#4116;&#4141;&#4145;&#4123;&#4140;&#4145;&#4115;&#4139; &#4116;&#4141;&#4119;&#4218;&#4140;&#4116;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/045-HtooGyiSayadaw-9-9-2006-am.mp3">
								&#4164;&#4165;&#4171; &#4169;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4150;&#4099;&#4140;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;&#4129;&#4112;&#4156;&#4096;&#4153; &#4112;&#4123;&#4140;&#4152;&#4113;&#4141;&#4143;&#4100;&#4153; 
								&#4116;&#4106;&#4153;&#4152;&#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171; &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4102;&#4123;&#4140;&#4145;&#4112;&#4140;&#4153;&#4120;&#4143;&#4123;&#4140;&#4152;&#4222;&#4096;&#4142;&#4152;&#4175; 
								&#4116;&#4141;&#4119;&#4218;&#4140;&#4116;&#4153;&#4126;&#4156;&#4140;&#4152; &#4124;&#4121;&#4153;&#4152;&#4223;&#4117;&#4145;&#4223;&#4121;&#4117;&#4150;&#4143;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/046-HtooGyiSayadaw-9-9-2006-3pm.mp3">
								&#4164;&#4166;&#4171; &#4169;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171; 
								&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4100;&#4139;&#4152;&#4097;&#4143;&#4096;&#4141;&#4143; &#4129;&#4096;&#4154;&#4122;&#4153;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4171; &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4124;&#4121;&#4153;&#4152;&#4101;&#4133;&#4153; &#4126;&#4106;&#4153; 
								&#4133;&#4140;&#4111;&#4153;&#4101;&#4133;&#4153;&#4117;&#4122;&#4153; &#4125;&#4139;&#4114;&#4127;&#4143; &#4101;&#4156;&#4117;&#4153;&#4101;&#4156;&#4146;&#4097;&#4154;&#4096;&#4153;&#4129;&#4140;&#4152; &#4145;&#4155;&#4118;&#4123;&#4157;&#4100;&#4153;&#4152;&#4170;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/047-HtooGyiSayadaw-10-9-2006-am.mp3">
								&#4164;&#4167;&#4171; &#4161;&#4160;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4150;&#4099;&#4140;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;&#4129;&#4112;&#4156;&#4096;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4113;&#4141;&#4143;&#4100;&#4153;&#4116;&#4106;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171; 
								&#4123;&#4232;&#4096;&#4156;&#4100;&#4153;&#4152;&#4170;&#4123;&#4232;&#4096;&#4156;&#4096;&#4153;-&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4117;&#4150;&#4143;&#4171; 
								&#4101;&#4123;&#4143;&#4141;&#4096;&#4153;&#4145;&#4124;&#4152;&#4121;&#4154;&#4147;&#4141;&#4152;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4126;&#4106;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/048-HtooGyiSayadaw-10-9-2006-3pm.mp3">
								&#4164;&#4168;&#4171; &#4161;&#4160;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4239;&#4157;&#4100;&#4153;&#4151; &#4122;&#4157;&#4133;&#4153;&#4145;&#4126;&#4140; 
								&#4133;&#4117;&#4139;&#4116;&#4141;&#4126;&#4122;&#4121;&#4154;&#4140;&#4152;&#4171; &#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4145;&#4124;&#4152;&#4097;&#4143; &#4239;&#4157;&#4100;&#4153;&#4151; &#4114;&#4141;&#4242;&#4141;&#4223;&#4118;&#4147;&#4112;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/049-HtooGyiSayadaw-11-9-2006-am.mp3">
								&#4164;&#4169;&#4171; &#4161;&#4161;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140; (&#4164;) &#4117;&#4139;&#4152;&#4112;&#4123;&#4140;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/050-HtooGyiSayadaw-11-9-2006-3pm.mp3">
								&#4165;&#4160;&#4171; &#4161;&#4161;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- 
								&#4145;&#4120;&#4140;&#4101;&#4133;&#4153;(&#4167;)&#4117;&#4139;&#4152;&#4112;&#4123;&#4140;&#4152;&#4096;&#4141;&#4143;&#4118;&#4122;&#4153;&#4113;&#4140;&#4152;&#4223;&#4097;&#4100;&#4153;&#4152;&#4223;&#4118;&#4100;&#4153;&#4151;&#4170; &#4131;&#4145;&#4227;&#4239;&#4213; 
								(&#4166;)&#4117;&#4139;&#4152;&#4121;&#4145;&#4101;&#4140;&#4100;&#4153;&#4151;&#4101;&#4106;&#4153;&#4152;&#4120;&#4146; &#4129;&#4140;&#4152;&#4124;&#4150;&#4143;&#4152;&#4096;&#4141;&#4143; &#4121;&#4101;&#4156;&#4116;&#4153;&#4244;&#4124;&#4234;&#4112;&#4153;&#4120;&#4146; 
								&#4126;&#4112;&#4209;&#4125;&#4139;&#4121;&#4154;&#4140;&#4152;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140;&#4123;&#4140;&#4096;&#4141;&#4143;&#4121;&#4223;&#4121;&#4100;&#4153;&#4127;&#4143; 
								&#4126;&#4143;&#4223;&#4119;&#4127;&#4220;&#4140;&#4116;&#4112;&#4153;&#4126;&#4140;&#4152;&#4096;&#4141;&#4143;&#4145;&#4127;&#4140;&#4145;&#4126;&#4140; &#4126;&#4143;&#4112;&#4209;&#4116;&#4153;&#4112;&#4123;&#4140;&#4152; &#4133;&#4117;&#4121;&#4140;&#4223;&#4117;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140; &#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151;&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153; 
								&#4155;&#4117;&#4116;&#4153;&#4245;&#4117;&#4156;&#4140;&#4152;&#4145;&#4123;&#4152; &#4129;&#4118;&#4156;&#4146;&#4245;&#4097;&#4154;&#4147;&#4117;&#4153;&#4224;&#4096;&#4142;&#4152;&#4172; 
								(&#4165;)&#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152;&#4117;&#4156;&#4146;&#4112;&#4156;&#4100;&#4153; 
								&#4145;&#4127;&#4140;&#4224;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4145;&#4126;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/051-HtooGyiSayadaw-22-9-2006-am.mp3">
								&#4165;&#4161;&#4171; &#4162;&#4162;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4150;&#4099;&#4140;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;&#4129;&#4112;&#4156;&#4096;&#4153; 
								&#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171; &#4129;&#4115;&#4141;&#4096;&#4129;&#4124;&#4143;&#4117;&#4153;&#4096; &#4121;&#4098;&#4153;&#4123;&#4118;&#4141;&#4143;&#4244;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/052-HtooGyiSayadaw-22-9-2006-3pm.mp3">
								&#4165;&#4162;&#4171; &#4162;&#4162;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140; (&#4164;) &#4117;&#4139;&#4152;&#4112;&#4123;&#4140;&#4152;&#4171; 
								&#4129;&#4140;&#4152;&#4222;&#4096;&#4142;&#4152;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140;&#4170;&#4129;&#4140;&#4152;&#4145;&#4126;&#4152;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140; &#4096;&#4141;&#4143;&#4123;&#4157;&#4100;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/053-HtooGyiSayadaw-23-9-2006-am.mp3">
								&#4165;&#4163;&#4171; &#4162;&#4163;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4096;&#4154;&#4100;&#4153;&#4151;&#4101;&#4133;&#4153; 
								&#4106;&#4140;&#4112;&#4117;&#4123;&#4141;&#4133;&#4140; &#4126;&#4100;&#4153;&#4145;&#4117;&#4152;&#4123;&#4112;&#4140;&#4170; (&#4223;&#4118;&#4101;&#4153;)&#4096;&#4141;&#4143; &#4126;&#4141;&#4118;&#4141;&#4143;&#4244; 
								&#4170;&#4115;&#4121;&#4220;&#4096;&#4113;&#4141;&#4096;&#4121;&#4154;&#4140;&#4152; &#4175; &#4129;&#4115;&#4141;&#4096;&#4112;&#4140;&#4125;&#4116;&#4153; &#4171;&#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4120;&#4140;&#4126;&#4140;&#4123;&#4117;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/054-HtooGyiSayadaw-23-9-2006-3pm.mp3">
								&#4165;&#4164;&#4171; &#4162;&#4163;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;) 
								“&#4223;&#4118;&#4101;&#4153;&#4117;&#4154;&#4096;&#4153;&#4126;&#4121;&#4157;&#4154; &#4126;&#4097;&#4196; &#4139;&#4123;&#4170; &#4114;&#4143;&#4096;&#4193;&#4126;&#4101;&#4197;&#4140;&#4121;&#4157;&#4112;&#4153;” 
								&#4096;&#4119;&#4154;&#4140;&#4129;&#4140;&#4152;&#4123;&#4157;&#4100;&#4153;&#4152;&#4112;&#4121;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/055-HtooGyiSayadaw-24-9-2006-am.mp3">
								&#4165;&#4165;&#4171; &#4162;&#4164;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4121;&#4098;&#4153;&#4133;&#4140;&#4111;&#4153;&#4170;&#4118;&#4141;&#4143;&#4133;&#4140;&#4111;&#4153; 
								&#4123;&#4239;&#4141;&#4143;&#4100;&#4153;&#4223;&#4097;&#4100;&#4153;&#4152;&#4123;&#4157;&#4141;&#4170;&#4121;&#4123;&#4157;&#4141; &#4121;&#4141;&#4121;&#4141;&#4096;&#4141;&#4143;&#4122;&#4153;&#4096;&#4141;&#4143; &#4101;&#4101;&#4153;&#4145;&#4102;&#4152;&#4223;&#4097;&#4100;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/056-HtooGyiSayadaw-24-9-2006-3pm.mp3">
								&#4165;&#4166;&#4171; &#4162;&#4164;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140;&#4126;&#4141;&#4223;&#4117;&#4142;&#4152;&#4121;&#4157; &#4124;&#4157;&#4148;&#4117;&#4139;&#4171; 
								&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;(&#4165;)&#4097;&#4143;&#4171; &#4112;&#4111;&#4157;&#4140;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121;&#4113;&#4146;&#4121;&#4157;&#4140; &#4145;&#4116;&#4124;&#4141;&#4143;&#4244;&#4112;&#4111;&#4157;&#4140;&#4116;&#4122;&#4153;&#4145;&#4223;&#4121; 
								&#4129;&#4143;&#4117;&#4153;&#4097;&#4154;&#4147;&#4117;&#4153;&#4126;&#4144; &#4129;&#4124;&#4141;&#4143;&#4096;&#4154; &#4124;&#4157;&#4148;&#4112;&#4140;&#4145;&#4112;&#4140;&#4100;&#4153; “&#4100;&#4139;&#4151;&#4129;&#4124;&#4157;&#4148;” &#4114;&#4141;&#4242;&#4141;&#4112;&#4111;&#4157;&#4140; 
								&#4133;&#4142;&#4152;&#4101;&#4142;&#4152;&#4129;&#4124;&#4157;&#4148; &#4124;&#4157;&#4148;&#4117;&#4150;&#4143;&#4096;&#4141;&#4143; &#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/057-HtooGyiSayadaw-25-9-2006-am.mp3">
								&#4165;&#4167;&#4171; &#4162;&#4165;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4101;&#4141;&#4112;&#4209;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4171; 
								&#4100;&#4139;&#4126;&#4106;&#4153;&#4121;&#4143;&#4097;&#4154;&#4145;&#4126;&#4123;&#4121;&#4106;&#4153; &#4129;&#4097;&#4154;&#4141;&#4116;&#4153;&#4117;&#4141;&#4143;&#4100;&#4153;&#4152;&#4126;&#4140; &#4124;&#4141;&#4143;&#4145;&#4112;&#4140;&#4151;&#4126;&#4106;&#4153; 
								&#4101;&#4141;&#4112;&#4209;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;&#4171; <br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/058-HtooGyiSayadaw-25-9-2006-3pm.mp3">
								&#4165;&#4168;&#4171; &#4162;&#4165;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4121;&#4220;&#4140;&#4114;&#4141;&#4242;&#4141; (&#4165;) &#4121;&#4154;&#4147;&#4141;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/059-HtooGyiSayadaw-26-9-2006-am.mp3">
								&#4165;&#4169;&#4171; &#4162;&#4166;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4117;&#4139;&#4123;&#4121;&#4142;&#4102;&#4143;&#4222;&#4096;&#4142;&#4152;&#4117;&#4116;&#4153; ( &#4121;&#4098;&#4153;&#4133;&#4140;&#4111;&#4153; 
								&#4118;&#4141;&#4143;&#4133;&#4140;&#4111;&#4153; &#4116;&#4141;&#4119;&#4218;&#4140;&#4116;&#4153;&#4126;&#4141;&#4143;&#4244; &#4124;&#4157;&#4154;&#4100;&#4153;&#4223;&#4121;&#4116;&#4153;&#4101;&#4156;&#4140; &#4145;&#4123;&#4140;&#4096;&#4153;&#4123;&#4117;&#4139;&#4124;&#4141;&#4143;&#4175;) 
								&#4127;&#4144;&#4145;&#4126;&#4140;&#4102;&#4143;&#4145;&#4112;&#4140;&#4100;&#4153;&#4152;&#4096;&#4141;&#4143;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4171; &#4131;&#4145;&#4227;&#4239;&#4213; &#4106;&#4141;&#4157;&#4116;&#4106;&#4153;&#4152;&#4171; 
								&#4129;&#4116;&#4141;&#4101;&#4197;&#4170;&#4114;&#4143;&#4096;&#4193;&#4170;&#4129;&#4116;&#4112;&#4209; &#4096;&#4141;&#4143; &#4124;&#4096;&#4193;&#4111;&#4140;&#4113;&#4100;&#4153;&#4145;&#4129;&#4140;&#4100;&#4153;&#4123;&#4232;&#4116;&#4106;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/060-HtooGyiSayadaw-26-9-2006-3pm.mp3">
								&#4166;&#4160;&#4171; &#4162;&#4166;-&#4169;-&#4162;&#4160;&#4160;&#4166; </a>- &#4126;&#4101;&#4197;&#4140;(&#4164;)&#4117;&#4139;&#4152;&#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4171; 
								&#4125;&#4141;&#4117;&#4230;&#4116;&#4140;&#4112;&#4101;&#4153;&#4097;&#4154;&#4096;&#4153;&#4123;&#4232;&#4112;&#4141;&#4143;&#4100;&#4153;&#4152; &#4096;&#4141;&#4145;&#4124;&#4126;&#4140;&#4117;&#4139;&#4152;&#4117;&#4139;&#4152;&#4126;&#4156;&#4140;&#4152;&#4123;&#4100;&#4153;&#4152; 
								&#4129;&#4117;&#4216;&#4139;&#4122;&#4153;&#4112;&#4150;&#4097;&#4139;&#4152;&#4117;&#4141;&#4112;&#4153;&#4117;&#4150;&#4143;&#4171;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140; &#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151;&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153; 
								&#4155;&#4117;&#4116;&#4153;&#4245;&#4117;&#4156;&#4140;&#4152;&#4145;&#4123;&#4152; &#4129;&#4118;&#4156;&#4146;&#4245;&#4097;&#4154;&#4147;&#4117;&#4153;&#4224;&#4096;&#4142;&#4152;&#4172; 
								(&#4161;&#4160;)&#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152;&#4117;&#4156;&#4146;&#4112;&#4156;&#4100;&#4153; 
								&#4145;&#4127;&#4140;&#4224;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4145;&#4126;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/061-HtooGyiSayadaw-19-10-2006-7pm.mp3">
								&#4166;&#4161;&#4171; &#4161;&#4169;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106;&#4145;&#4116; </a>- (&#4166;) &#4242;&#4140;&#4116;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/062-HtooGyiSayadaw-20-10-2006-am.mp3">
								&#4166;&#4162;&#4171; &#4162;&#4160;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4117;&#4242;&#4140;&#4116;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171; 
								&#4097;&#4239;&#4214;&#4140;&#4151;&#4223;&#4118;&#4101;&#4153;&#4101;&#4133;&#4153;&#4222;&#4096;&#4142;&#4152;&#4129;&#4123;&#4157;&#4141;&#4116;&#4153;&#4129;&#4127;&#4143;&#4116;&#4153;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4129;&#4102;&#4096;&#4153;&#4121;&#4223;&#4117;&#4112;&#4153;&#4124;&#4106;&#4153;&#4145;&#4116;&#4117;&#4150;&#4143;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/063-HtooGyiSayadaw-20-10-2006-3pm.mp3">
								&#4166;&#4163;&#4171; &#4162;&#4160;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4117;&#4216;&#4121;&#4140;&#4145;&#4114;&#4116; &#4126;&#4121;&#4220;&#4140;&#4145;&#4114;&#4113;&#4171; 
								&#4223;&#4121;&#4112;&#4153;&#4101;&#4156;&#4140;&#4120;&#4143;&#4123;&#4140;&#4152;&#4175; &#4117;&#4113;&#4121;&#4102;&#4150;&#4143;&#4152;&#4101;&#4096;&#4140;&#4152;&#4239;&#4157;&#4100;&#4153;&#4151; &#4145;&#4116;&#4140;&#4096;&#4153;&#4102;&#4150;&#4143;&#4152;&#4101;&#4096;&#4140;&#4152;&#4170;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/064-HtooGyiSayadaw-20-10-2006-7pm.mp3">
								&#4166;&#4164;&#4171; &#4162;&#4160;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- 
								&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153;&#4145;&#4223;&#4097;&#4097;&#4150;&#4113;&#4117;&#4153;&#4102;&#4100;&#4153;&#4151;&#4123;&#4157;&#4100;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/065-HtooGyiSayadaw-21-10-2006-am.mp3">
								&#4166;&#4165;&#4171; &#4162;&#4161;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4117;&#4106;&#4112;&#4153;&#4097;&#4239;&#4214;&#4140;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4117;&#4123;&#4121;&#4112;&#4153;&#4097;&#4239;&#4214;&#4140;&#4170;&#4126;&#4150;&#4126;&#4123;&#4140;&#4129;&#4102;&#4096;&#4153;&#4102;&#4096;&#4153;&#4121;&#4157; &#4117;&#4101;&#4197;&#4122;&#4126;&#4112;&#4209;&#4141;&#4121;&#4154;&#4140;&#4152;&#4129;&#4145;&#4222;&#4096;&#4140;&#4100;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/066-HtooGyiSayadaw-21-10-2006-3pm.mp3">
								&#4166;&#4166;&#4171; &#4162;&#4161;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4114;&#4143;&#4096;&#4193;&#4126;&#4101;&#4197;&#4140;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4170; 
								&#4100;&#4123;&#4146;&#4222;&#4096;&#4142;&#4152;&#4123;&#4157;&#4101;&#4153;&#4113;&#4117;&#4153;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;(&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/067-HtooGyiSayadaw-21-10-2006-7pm.mp3">
								&#4166;&#4167;&#4171; &#4162;&#4161;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- &#4097;&#4239;&#4214;&#4140;&#4170; &#4129;&#4140;&#4122;&#4112;&#4116;&#4170; &#4115;&#4139;&#4112;&#4153;&#4170; &#4126;&#4101;&#4197;&#4140;&#4170; 
								&#4117;&#4107;&#4141;&#4101;&#4197; &#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153;&#4170;&#4129;&#4123;&#4144;&#4097;&#4150;&#4170; &#4129;&#4123;&#4144;&#4133;&#4140;&#4111;&#4153;&#4096;&#4141;&#4143; &#4129;&#4096;&#4154;&#4122;&#4153;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/068-HtooGyiSayadaw-22-10-2006-am.mp3">
								&#4166;&#4168;&#4171; &#4162;&#4162;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; -</a> &#4117;&#4101;&#4197;&#4122;&#4126;&#4112;&#4209;&#4141; &#4101;&#4156;&#4121;&#4153;&#4152;&#4129;&#4140;&#4152;&#4223;&#4118;&#4100;&#4153;&#4151; 
								&#4125;&#4107;&#4153; (&#4163;) &#4117;&#4139;&#4152;&#4124;&#4106;&#4153;&#4117;&#4150;&#4143;&#4171; &#4120;&#4125;&#4239;&#4157;&#4100;&#4153;&#4151;&#4097;&#4239;&#4214;&#4140; &#4121;&#4157;&#4140; &#4097;&#4239;&#4214;&#4140;&#4096; &#4129;&#4115;&#4141;&#4096;&#4096;&#4154;&#4171; 
								(&#4120;&#4125;&#4126;&#4150;&#4126;&#4123;&#4140;)&#4115;&#4121;&#4220;&#4126;&#4145;&#4120;&#4140;&#4096;&#4141;&#4143;&#4223;&#4121;&#4100;&#4153;&#4145;&#4129;&#4140;&#4100;&#4153;&#4222;&#4096;&#4106;&#4153;.<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/069-HtooGyiSayadaw-22-10-2006-3pm.mp3">
								&#4166;&#4169;&#4171; &#4162;&#4162;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- 
								&#4100;&#4123;&#4146;&#4222;&#4096;&#4142;&#4152;&#4123;&#4157;&#4101;&#4153;&#4113;&#4117;&#4153;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;(&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/070-HtooGyiSayadaw-22-10-2006-7pm.mp3">
								&#4167;&#4160;&#4171; &#4162;&#4162;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- &#4129;&#4123;&#4141;&#4122;&#4140; (&#4164;) &#4133;&#4142;&#4152;&#4129;&#4112;&#4156;&#4096;&#4153; 
								&#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121;&#4170; &#4117;&#4143;&#4113;&#4143;&#4103;&#4133;&#4153;(&#4164;)&#4133;&#4142;&#4152;&#4129;&#4112;&#4156;&#4096;&#4153; &#4129;&#4239;&#4143;&#4145;&#4124;&#4140;&#4121; &#4170;&#4121;&#4141;&#4121;&#4141;&#4112;&#4141;&#4143;&#4244;&#4126;&#4106;&#4153; 
								&#4117;&#4143;&#4113;&#4143;&#4103;&#4133;&#4153;&#4121;&#4141;&#4143;&#4244;&#4129;&#4098;&#4196;&#4139;(&#4161;&#4162;)&#4117;&#4139;&#4152;&#4223;&#4118;&#4100;&#4153;&#4151;&#4124;&#4106;&#4153;&#4145;&#4116;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/071-HtooGyiSayadaw-23-10-2006-am.mp3">
								&#4167;&#4161;&#4171; &#4162;&#4163;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4097;&#4154;&#4106;&#4153;&#4112;&#4141;&#4143;&#4100;&#4153;&#4096;&#4154;&#4147;&#4141;&#4152;&#4173; 
								&#4124;&#4106;&#4153;&#4117;&#4112;&#4153;&#4223;&#4117;&#4112;&#4153;(&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153;+&#4117;&#4242;&#4140;&#4116;&#4153;&#4152;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/072-HtooGyiSayadaw-23-10-2006-3pm.mp3">
								&#4167;&#4162;&#4171; &#4162;&#4163;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166;&#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4239;&#4143;&#4230;&#4122;&#4126;&#4145;&#4120;&#4140;&#4223;&#4118;&#4100;&#4153;&#4151; 
								&#4096;&#4141;&#4116;&#4153;&#4152;&#4145;&#4129;&#4140;&#4100;&#4153;&#4152;&#4145;&#4116;&#4145;&#4126;&#4140; 
								&#4129;&#4140;&#4126;&#4145;&#4125;&#4139;&#4112;&#4123;&#4140;&#4152;&#4121;&#4154;&#4140;&#4152;&#4096;&#4143;&#4116;&#4153;&#4097;&#4121;&#4153;&#4152;&#4145;&#4129;&#4140;&#4100;&#4153;&#4096;&#4154;&#4100;&#4153;&#4151;&#4222;&#4096;&#4150;&#4223;&#4097;&#4100;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/073-HtooGyiSayadaw-23-10-2006-7pm.mp3">
								&#4167;&#4163;&#4171; &#4162;&#4163;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>
								-&#4129;&#4098;&#4196;&#4139;(&#4161;&#4162;)&#4117;&#4139;&#4152;&#4129;&#4096;&#4154;&#4122;&#4153;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;(&#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121;&#4170;&#4129;&#4239;&#4143;&#4145;&#4124;&#4140;&#4121; 
								&#4124;&#4096;&#4196;&#4140;&#4129;&#4145;&#4222;&#4096;&#4140;&#4100;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/074-HtooGyiSayadaw-24-10-2006-am.mp3">
								&#4167;&#4164;&#4171; &#4162;&#4164;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4118;&#4230;&#4102;&#4144;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4170; 
								&#4118;&#4230;&#4145;&#4222;&#4096;&#4140;&#4100;&#4153;&#4151; &#4120;&#4143;&#4123;&#4140;&#4152;&#4129;&#4145;&#4124;&#4140;&#4100;&#4153;&#4152;&#4145;&#4112;&#4140;&#4153; &#4101;&#4101;&#4153;&#4101;&#4101;&#4153;&#4222;&#4096;&#4142;&#4152;&#4117;&#4100;&#4153; 
								&#4129;&#4123;&#4157;&#4096;&#4153;&#4112;&#4096;&#4156;&#4146; &#4129;&#4096;&#4154;&#4147;&#4141;&#4152;&#4116;&#4106;&#4153;&#4152; &#4223;&#4118;&#4101;&#4153;&#4123;&#4117;&#4143;&#4150;&#4171; &#4124;&#4144;&#4129;&#4121;&#4154;&#4140;&#4152; &#4126;&#4150;&#4145;&#4125;&#4098; 
								&#4123;&#4145;&#4101;&#4123;&#4116;&#4153; &#4121;&#4141;&#4121;&#4141;&#4223;&#4118;&#4101;&#4153;&#4097;&#4146;&#4151;&#4145;&#4126;&#4140; &#4126;&#4141;&#4125;&#4141;&#4120;&#4143;&#4123;&#4100;&#4153;&#4120;&#4125;&#4096;&#4141;&#4143;&#4143;&#4223;&#4117;&#4116;&#4153;&#4145;&#4127;&#4140;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/075-HtooGyiSayadaw-24-10-2006-3pm.mp3">
								&#4167;&#4165;&#4171; &#4162;&#4164;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4122;&#4113;&#4140;&#4120;&#4144;&#4112;&#4133;&#4140;&#4111;&#4153;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/076-HtooGyiSayadaw-24-10-2006-7pm.mp3">
								&#4167;&#4166;&#4171; &#4162;&#4164;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- 
								&#4101;&#4141;&#4112;&#4209;&#4140;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140;&#4126;&#4112;&#4141;&#4117;&#4242;&#4140;&#4116;&#4153;&#4123;&#4232;&#4116;&#4106;&#4153;&#4152;&#4171;&#4126;&#4112;&#4141;&#4117;&#4242;&#4140;&#4116;&#4153;(&#4164;)&#4121;&#4154;&#4147;&#4141;&#4152;&#4129;&#4096;&#4154;&#4122;&#4153;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/077-HtooGyiSayadaw-25-10-2006-am.mp3">
								&#4167;&#4167;&#4171; &#4162;&#4165;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- 
								&#4101;&#4141;&#4112;&#4209;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140;&#4123;&#4232;&#4121;&#4157;&#4112;&#4153;&#4117;&#4156;&#4140;&#4152;&#4116;&#4106;&#4153;&#4152;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/078-HtooGyiSayadaw-25-10-2006-3pm.mp3">
								&#4167;&#4168;&#4171; &#4162;&#4165;-&#4161;&#4160;&#4162;-&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- 
								&#4125;&#4141;&#4117;&#4216;&#4124;&#4229;&#4140;&#4126;(&#4161;&#4162;)&#4117;&#4139;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/079-HtooGyiSayadaw-25-10-2006-7pm.mp3">
								&#4167;&#4169;&#4171; &#4162;&#4165;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- 
								&#4112;&#4123;&#4140;&#4152;&#4123;&#4232;&#4121;&#4157;&#4112;&#4153;&#4117;&#4150;&#4143;&#4126;&#4100;&#4153;&#4222;&#4096;&#4140;&#4152;&#4223;&#4097;&#4100;&#4153;&#4152;(&#4161;)&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/080-HtooGyiSayadaw-26-10-2006-am.mp3">
								&#4168;&#4160;&#4171; &#4162;&#4166;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4143;&#4097;&#4145;&#4125;&#4114;&#4116;&#4140;&#4096;&#4141;&#4143; 
								&#4121;&#4123;&#4232;&#4120;&#4146;&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153;&#4096;&#4141;&#4143;&#4121;&#4123;&#4117;&#4153;&#4239;&#4141;&#4143;&#4100;&#4153;&#4171; 
								&#4102;-&#4101;&#4096;&#4192;&#4126;&#4143;&#4112;&#4209;&#4116;&#4153;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;(&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/081-HtooGyiSayadaw-26-10-2006-3pm.mp3">
								&#4168;&#4161;&#4171; &#4162;&#4166;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4113;&#4146;&#4096;&#4124;&#4144;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/082-HtooGyiSayadaw-26-10-2006-7pm..mp3">
								&#4168;&#4162;&#4171; &#4162;&#4166;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- 
								&#4112;&#4123;&#4140;&#4152;&#4123;&#4232;&#4121;&#4157;&#4112;&#4153;&#4117;&#4150;&#4143;&#4126;&#4100;&#4153;&#4222;&#4096;&#4140;&#4152;&#4223;&#4097;&#4100;&#4153;&#4152;(&#4162;)&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/083-HtooGyiSayadaw-27-10-2006-am.mp3">
								&#4168;&#4163;&#4171; &#4162;&#4167;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4102;-&#4101;&#4096;&#4192;&#4126;&#4143;&#4112;&#4209;&#4116;&#4153;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;(&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/084-HtooGyiSayadaw-27-10-2006-3pm.mp3">
								&#4168;&#4164;&#4171; &#4162;&#4167;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; -</a> 
								&#4126;&#4101;&#4197;&#4140;&#4126;&#4141;&#4118;&#4141;&#4143;&#4244;&#4129;&#4145;&#4123;&#4152;&#4129;&#4222;&#4096;&#4142;&#4152;&#4102;&#4150;&#4143;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/085-HtooGyiSayadaw-27-10-2006-7pm.mp3">
								&#4168;&#4165;&#4171; &#4162;&#4167;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4106; </a>- 
								&#4112;&#4123;&#4140;&#4152;&#4117;&#4156;&#4146;&#4223;&#4117;&#4142;&#4152;&#4102;&#4150;&#4143;&#4152;&#4170;&#4124;&#4157;&#4148;&#4114;&#4139;&#4116;&#4153;&#4152;&#4170;&#4126;&#4140;&#4115;&#4143;&#4145;&#4097;&#4186;&#4170;&#4129;&#4121;&#4157;&#4154;&#4145;&#4125;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/086-HtooGyiSayadaw-28-10-2006-am.mp3">
								&#4168;&#4166;&#4171; &#4162;&#4168;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- 
								&#4126;&#4150;&#4126;&#4123;&#4140;&#4097;&#4123;&#4142;&#4152;&#4126;&#4106;&#4153;&#4222;&#4096;&#4142;&#4152;&#4113;&#4156;&#4096;&#4153;&#4123;&#4117;&#4153;&#4124;&#4121;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/087-HtooGyiSayadaw-28-10-2006-3pm.mp3">
								&#4168;&#4167;&#4171; &#4162;&#4168;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- 
								&#4124;&#4154;&#4100;&#4153;&#4145;&#4126;&#4140;&#4129;&#4102;&#4141;&#4117;&#4153;&#4123;&#4157;&#4141;&#4145;&#4126;&#4140;&#4145;&#4223;&#4121;&#4156;&#4222;&#4096;&#4142;&#4152;&#4145;&#4124;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/088-HtooGyiSayadaw-29-10-2006-am.mp3">
								&#4168;&#4168;&#4171; &#4162;&#4169;-&#4161;&#4160;-&#4162;&#4160;&#4160;&#4166; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4239;&#4143;&#4145;&#4124;&#4140;&#4121;-&#4129;&#4101;&#4143;&#4116;&#4153;&#4124;&#4121;&#4153;&#4152;&#4170; 
								&#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121;-&#4129;&#4102;&#4116;&#4153;&#4124;&#4121;&#4153;&#4152;-&#4113;&#4156;&#4096;&#4153;&#4123;&#4117;&#4153;&#4124;&#4121;&#4153;&#4152;&#4170;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4129;&#4145;&#4121;&#4123;&#4141;&#4096;&#4116;&#4153;&#4170; &#4116;&#4122;&#4144;&#4152;&#4145;&#4122;&#4140;&#4096;&#4153;&#4223;&#4121;&#4141;&#4147;&#4245;&#4170; &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140;&#4123;&#4141;&#4117;&#4153;&#4126;&#4140; 
								(&#4165;) &#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152;&#4117;&#4156;&#4146;&#4112;&#4156;&#4100;&#4153; (July 31 to Aug 4, 2008) 
								&#4172; &#4145;&#4127;&#4140;&#4222;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4129;&#4117;&#4153;&#4145;&#4126;&#4140; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/089-HtooGyiSayadaw-26-7-2008.mp3">
								&#4168;&#4169;&#4171; &#4162;&#4166;-&#4167;-&#4162;&#4160;&#4160;&#4168; </a>&#4121;&#4141;&#4112;&#4153;&#4102;&#4096;&#4153; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/090-HtooGyiSayadaw-27-7-2008-2pm.mp3">
								&#4169;&#4160;&#4171; &#4162;&#4167;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4121;&#4141;&#4112;&#4153;&#4102;&#4096;&#4153; (&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/091-HtooGyiSayadaw-28-7-2008-7pm.mp3">
								&#4169;&#4161;&#4171; &#4162;&#4168;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- 
								&#4124;&#4140;&#4155;&#4097;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4173;&#4155;&#4117;&#4116;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4126;&#4144;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/092-HtooGyiSayadaw-29-7-2008-7pm.mp3">
								&#4169;&#4162;&#4171; &#4162;&#4169;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4129;&#4117;&#4141;&#4112;&#4153;&#4100;&#4139;&#4152;&#4117;&#4139;&#4152; &#4129;&#4117;&#4156;&#4100;&#4153;&#4151;&#4100;&#4139;&#4152;&#4117;&#4139;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/093-HtooGyiSayadaw-30-7-2008-7pm.mp3">
								&#4169;&#4163;&#4171; &#4163;&#4160;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- 
								&#4129;&#4096;&#4143;&#4116;&#4153;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4126;&#4106;&#4153;&#4151;&#4112;&#4123;&#4140;&#4152;-&#4106;&#4101;&#4097;&#4116;&#4153;&#4152;&#4118;&#4156;&#4100;&#4153;&#4151;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/094-HtooGyiSayadaw-31-7-2008-730am.mp3">
								&#4169;&#4164;&#4171; &#4163;&#4161;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- 
								&#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153;&#4129;&#4145;&#4123;&#4152;&#4224;&#4096;&#4142;&#4152;&#4117;&#4150;&#4143;&#4112;&#4123;&#4140;&#4152; <br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/095-HtooGyiSayadaw-31-7-2008-1300pm.mp3">
								&#4169;&#4165;&#4171; &#4163;&#4161;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/096-HtooGyiSayadaw-31-7-2008-1930pm.mp3">
								&#4169;&#4166;&#4171; &#4163;&#4161;-&#4167;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4145;&#4129;&#4140;&#4100;&#4153;&#4239;&#4141;&#4143;&#4100;&#4153;&#4126;&#4144;&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/097-HtooGyiSayadaw-1-8-2008-730am.mp3">
								&#4169;&#4167;&#4171; &#4161;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4116;&#4160;&#4121;&#4119;&#4143;&#4114;&#4214;&#4097;&#4111;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/098-HtooGyiSayadaw-1-8-2008-1300pm.mp3">
								&#4169;&#4168;&#4171; &#4161;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- 
								&#4112;&#4123;&#4140;&#4152;&#4101;&#4133;&#4153;&#4239;&#4157;&#4100;&#4153;&#4151;&#4124;&#4143;&#4117;&#4153;&#4100;&#4116;&#4153;&#4152;&#4101;&#4133;&#4153; (&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/099-HtooGyiSayadaw-1-8-2008-1930pm.mp3">
								&#4169;&#4169;&#4171; &#4161;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4117;&#4144;&#4117;&#4116;&#4153;&#4121;&#4232;&#4121;&#4157;&#4124;&#4156;&#4112;&#4153;&#4096;&#4100;&#4153;&#4152;&#4155;&#4097;&#4100;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/100-HtooGyiSayadaw-2-8-2008-730am.mp3">
								&#4161;&#4160;&#4160;&#4171; &#4162;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- 
								&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4121;&#4141;&#4143;&#4096;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152;&#4175;&#4129;&#4115;&#4141;&#4117;&#4216;&#4139;&#4122;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/101-HtooGyiSayadaw-2-8-2008-1300pm.mp3">
								&#4161;&#4160;&#4161;&#4171; &#4162;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- 
								&#4116;&#4141;&#4119;&#4218;&#4140;&#4116;&#4153;&#4126;&#4156;&#4140;&#4152;&#4124;&#4121;&#4153;&#4152;&#4155;&#4117;&#4145;&#4155;&#4121;&#4117;&#4150;&#4143;&#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/102-HtooGyiSayadaw-2-8-2008-1930pm.mp3">
								&#4161;&#4160;&#4162;&#4171; &#4162;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4126;&#4144;&#4112;&#4141;&#4143;&#4244;&#4145;&#4117;&#4152;&#4126;&#4121;&#4157;&#4154;&#4145;&#4096;&#4154;&#4116;&#4117;&#4153;&#4117;&#4139;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/103-HtooGyiSayadaw-3-8-2008-730am.mp3">
								&#4161;&#4160;&#4163;&#4171; &#4163;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4160;&#4107;&#4153;&#4126;&#4150;&#4126;&#4123;&#4140;&#4124;&#4106;&#4153;&#4117;&#4150;&#4143;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/104-HtooGyiSayadaw-3-8-2008-1300pm.mp3">
								&#4161;&#4160;&#4164;&#4171; &#4163;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4101;&#4141;&#4112;&#4209;&#4140;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140;&#4240;&#4232;&#4116;&#4106;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/105-HtooGyiSayadaw-3-8-2008-1930pm.mp3">
								&#4161;&#4160;&#4165;&#4171; &#4163;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4145;&#4225;&#4121;&#4156;&#4124;&#4140;&#4152; &#4145;&#4100;&#4156;&#4124;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/106-HtooGyiSayadaw-4-8-2008-730am.mp3">
								&#4161;&#4160;&#4166;&#4171; &#4164;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4121;&#4220;&#4098;&#4236;&#4100;&#4139;&#4152;&#4117;&#4139;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/107-HtooGyiSayadaw-4-8-2008-1930pm.mp3">
								&#4161;&#4160;&#4167;&#4171; &#4164;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4126;&#4101;&#4197;&#4133;&#4140;&#4111;&#4153;&#4172;&#4133;&#4142;&#4152;&#4097;&#4141;&#4143;&#4096;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152; 
								(&#4165;)&#4123;&#4096;&#4153; - &#4101;&#4097;&#4116;&#4153;&#4152;&#4126;&#4141;&#4121;&#4153;&#4152;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4129;&#4145;&#4121;&#4123;&#4141;&#4096;&#4116;&#4153;&#4170; &#4116;&#4122;&#4144;&#4152;&#4145;&#4122;&#4140;&#4096;&#4153;&#4223;&#4121;&#4141;&#4147;&#4245;&#4170; &#4121;&#4141;&#4143;&#4152;&#4096;&#4143;&#4112;&#4153;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140;&#4123;&#4141;&#4117;&#4153;&#4126;&#4140;&#4170; 
								(&#4161;&#4160;) &#4123;&#4096;&#4153;&#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152; (Aug 8 to 17, 2008) &#4172; 
								&#4145;&#4127;&#4140;&#4222;&#4096;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4144;&#4129;&#4117;&#4153;&#4145;&#4126;&#4140; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;&#4121;&#4154;&#4140;&#4152;<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/108-HtooGyiSayadaw-7-8-2008-1930pm.mp3">
								&#4161;&#4160;&#4168;&#4171; &#4167;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- (&#4161;&#4160;)&#4123;&#4096;&#4153; &#4101;&#4097;&#4116;&#4153;&#4152;&#4118;&#4156;&#4100;&#4153;&#4151;&#4112;&#4123;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/109-HtooGyiSayadaw-8-8-2008-0730am.mp3">
								&#4161;&#4160;&#4169;&#4171; &#4168;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/110-HtooGyiSayadaw-8-8-2008-1300pm.mp3">
								&#4161;&#4161;&#4160;&#4171; &#4168;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4155;&#4097;&#4097;&#4150; &#4113;&#4117;&#4153;&#4102;&#4100;&#4153;&#4151;&#4123;&#4157;&#4100;&#4153;&#4152; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/111-HtooGyiSayadaw-8-8-2008-1930pm.mp3">
								&#4161;&#4161;&#4161;&#4171; &#4168;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4155;&#4121;&#4112;&#4153;&#4119;&#4143;&#4114;&#4214;&#4121;&#4157;&#4140;&#4112;&#4121;&#4153;&#4152;&#4145;&#4112;&#4140;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/112-HtooGyiSayadaw-9-8-2008-0730am.mp3">
								&#4161;&#4161;&#4162;&#4171; &#4169;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4114;&#4143;&#4119;&#4218;&#4124;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140; &#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4119;&#4124;&#4160;&#4160;&#4141;&#4117;&#4230;&#4116;&#4140;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/113-HtooGyiSayadaw-9-8-2008-1300pm.mp3">
								&#4161;&#4161;&#4163;&#4171; &#4169;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- 
								&#4119;&#4143;&#4114;&#4214;&#4175;&#4240;&#4143;&#4117;&#4153;&#4126;&#4150;&#4124;&#4234;&#4100;&#4153;&#4151;&#4101;&#4096;&#4153;&#4240;&#4150;&#4143;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/114-HtooGyiSayadaw-9-8-2008-1930pm.mp3">
								&#4161;&#4161;&#4164;&#4171; &#4169;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4122;&#4113;&#4140;&#4120;&#4144;&#4112;&#4133;&#4140;&#4111;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/115-HtooGyiSayadaw-10-8-2008-0730am.mp3">
								&#4161;&#4161;&#4165;&#4171; &#4161;&#4160;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/116-HtooGyiSayadaw-10-8-2008-1300pm.mp3">
								&#4161;&#4161;&#4166;&#4171; &#4161;&#4160;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4100;&#4139;&#4152;&#4101;&#4100;&#4153;&#4152; 
								&#4129;&#4124;&#4100;&#4153;&#4152;&#4100;&#4139;&#4152;&#4097;&#4154;&#4096;&#4153; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/117-HtooGyiSayadaw-10-8-2008-1930pm.mp3">
								&#4161;&#4161;&#4167;&#4171; &#4161;&#4160;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4114;&#4141;&#4242;&#4141;&#4117;&#4122;&#4153;&#4118;&#4141;&#4143;&#4244; &#4129;&#4145;&#4123;&#4152;&#4224;&#4096;&#4142;&#4152;&#4117;&#4150;&#4143;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/118-HtooGyiSayadaw-11-8-2008-0730am.mp3">
								&#4161;&#4161;&#4168;&#4171; &#4161;&#4161;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4096;&#4143;&#4126;&#4141;&#4143;&#4124;&#4153;&#4112;&#4126;&#4096;&#4153; 
								&#4096;&#4143;&#4126;&#4141;&#4143;&#4124;&#4153;&#4112;&#4097;&#4154;&#4096;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/119-HtooGyiSayadaw-11-8-2008-1300pm.mp3">
								&#4161;&#4161;&#4169;&#4171; &#4161;&#4161;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4100;&#4139;&#4152;&#4101;&#4100;&#4153;&#4152; 
								&#4129;&#4124;&#4100;&#4153;&#4152;&#4100;&#4139;&#4152;&#4097;&#4154;&#4096;&#4153; (&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/120-HtooGyiSayadaw-11-8-2008-1930pm.mp3">
								&#4161;&#4162;&#4160;&#4171; &#4161;&#4161;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4129;&#4123;&#4141;&#4117;&#4153;&#4126;&#4150;&#4143;&#4152;&#4117;&#4139;&#4152; &#4116;&#4140;&#4152;&#4124;&#4106;&#4153;&#4117;&#4139;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/121-HtooGyiSayadaw-12-8-2008-0730am.mp3">
								&#4161;&#4162;&#4161;&#4171; &#4161;&#4162;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4096;&#4143;&#4126;&#4141;&#4143;&#4124;&#4153;&#4112;&#4126;&#4096;&#4153; 
								&#4129;&#4096;&#4143;&#4126;&#4141;&#4143;&#4124;&#4153;&#4112;&#4097;&#4154;&#4096;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/122-HtooGyiSayadaw-12-8-2008-1300pm.mp3">
								&#4161;&#4162;&#4162;&#4171; &#4161;&#4162;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4100;&#4139;&#4152;&#4101;&#4100;&#4153;&#4152; 
								&#4129;&#4124;&#4100;&#4153;&#4152;&#4100;&#4139;&#4152;&#4097;&#4154;&#4096;&#4153; (&#4163;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/123-HtooGyiSayadaw-12-8-2008-1930pm.mp3">
								&#4161;&#4162;&#4163;&#4171; &#4161;&#4162;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4135;&#4106;&#4153;&#4151;&#4126;&#4106;&#4153;&#4096;&#4141;&#4143; 
								&#4129;&#4141;&#4121;&#4153;&#4240;&#4157;&#4100;&#4153;&#4121;&#4121;&#4157;&#4112;&#4153;&#4116;&#4146;&#4244;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/124-HtooGyiSayadaw-13-8-2008-0730am.mp3">
								&#4161;&#4162;&#4164;&#4171; &#4161;&#4163;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4096;&#4143;&#4126;&#4141;&#4143;&#4124;&#4153;&#4112;&#4126;&#4096;&#4153; &#4121;&#4098;&#4153;&#4112;&#4097;&#4154;&#4096;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/125-HtooGyiSayadaw-13-8-2008-1300pm.mp3">
								&#4161;&#4162;&#4165;&#4171; &#4161;&#4163;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4100;&#4139;&#4152;&#4101;&#4100;&#4153;&#4152; 
								&#4129;&#4124;&#4100;&#4153;&#4152;&#4100;&#4139;&#4152;&#4097;&#4154;&#4096;&#4153; (&#4164;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/126-HtooGyiSayadaw-13-8-2008-1930pm.mp3">
								&#4161;&#4162;&#4166;&#4171; &#4161;&#4163;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4097;&#4143;&#4240;&#4232;&#4123;&#4100;&#4153; &#4097;&#4143;&#4223;&#4100;&#4141;&#4121;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/127-HtooGyiSayadaw-14-8-2008-0730am.mp3">
								&#4161;&#4162;&#4167;&#4171; &#4161;&#4164;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4118;&#4230;&#4102;&#4144;&#4152;&#4112;&#4123;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/128-HtooGyiSayadaw-14-8-2008-1300pm.mp3">
								&#4161;&#4162;&#4168;&#4171; &#4161;&#4164;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4129;&#4145;&#4121;&#4157;&#4140;&#4100;&#4153;&#4100;&#4139;&#4152;&#4101;&#4100;&#4153;&#4152; 
								&#4129;&#4124;&#4100;&#4153;&#4152;&#4100;&#4139;&#4152;&#4097;&#4154;&#4096;&#4153; (&#4165;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/129-HtooGyiSayadaw-14-8-2008-1930pm.mp3">
								&#4161;&#4162;&#4169;&#4171; &#4161;&#4164;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- 
								&#4223;&#4100;&#4141;&#4121;&#4153;&#4152;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140;&#4122;&#4140;&#4145;&#4126;&#4140;&#4116;&#4122;&#4153;&#4145;&#4155;&#4121; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/130-HtooGyiSayadaw-15-8-2008-0730am.mp3">
								&#4161;&#4163;&#4160;&#4171; &#4161;&#4165;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4123;&#4141;&#4122; &#4121;&#4098;&#4194; 
								&#4160;&#4141;&#4103;&#4200;&#4140;&#4113;&#4156;&#4096;&#4153;&#4123;&#4117;&#4153;&#4124;&#4121;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/131-HtooGyiSayadaw-15-8-2008-1300pm.mp3">
								&#4161;&#4163;&#4161;&#4171; &#4161;&#4165;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4120;&#4160;&#4103;&#4140;&#4112;&#4153;&#4126;&#4141;&#4121;&#4153;&#4152; 
								&#4097;&#4154;&#4147;&#4117;&#4153;&#4223;&#4100;&#4141;&#4121;&#4153;&#4152;&#4123;&#4140; &#4116;&#4141;&#4119;&#4218;&#4140;&#4116;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/132-HtooGyiSayadaw-15-8-2008-1930pm.mp3">
								&#4161;&#4163;&#4162;&#4171; &#4161;&#4165;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4126;&#4100;&#4153;&#4112;&#4116;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/133-HtooGyiSayadaw-16-8-2008-0730am.mp3">
								&#4161;&#4163;&#4163;&#4171; &#4161;&#4166;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4096;&#4150; &#4133;&#4140;&#4111;&#4153; &#4160;&#4141;&#4123;&#4141;&#4122;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/134-HtooGyiSayadaw-16-8-2008-1300pm.mp3">
								&#4161;&#4163;&#4164;&#4171; &#4161;&#4166;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- &#4124;&#4121;&#4153;&#4152;&#4102;&#4150;&#4143;&#4152;&#4124;&#4157;&#4154;&#4100;&#4153; 
								&#4240;&#4156;&#4140;&#4145;&#4112;&#4156;&#4245;&#4121;&#4106;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/135-HtooGyiSayadaw-16-8-2008-1930pm.mp3">
								&#4161;&#4163;&#4165;&#4171; &#4161;&#4166;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4106;&#4145;&#4116; </a>- 
								&#4223;&#4100;&#4141;&#4121;&#4153;&#4152;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140;&#4122;&#4140;&#4145;&#4126;&#4140;&#4116;&#4122;&#4153;&#4145;&#4155;&#4121; (&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/136-HtooGyiSayadaw-17-8-2008-0730am.mp3">
								&#4161;&#4163;&#4166;&#4171; &#4161;&#4167;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4116;&#4150;&#4096;&#4153; </a>- &#4101;&#4141;&#4112;&#4153;&#4117;&#4143;&#4112;&#4142;&#4152;&#4239;&#4157;&#4100;&#4153;&#4151; 
								&#4119;&#4143;&#4114;&#4214;&#4139;&#4239;&#4143;&#4230;&#4112;&#4141; &#4117;&#4156;&#4140;&#4152;&#4121;&#4154;&#4140;&#4152;&#4117;&#4150;&#4143;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/137-HtooGyiSayadaw-17-8-2008-1300pm.mp3">
								&#4161;&#4163;&#4167;&#4171; &#4161;&#4167;-&#4168;-&#4162;&#4160;&#4160;&#4168; &#4145;&#4116;&#4245;&#4124;&#4106;&#4153; </a>- (&#4161;&#4160;)&#4123;&#4096;&#4153; 
								&#4101;&#4097;&#4116;&#4153;&#4152;&#4126;&#4141;&#4121;&#4153;&#4152;&#4112;&#4123;&#4140;&#4152;<br>
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&#4113;&#4144;&#4152;&#4222;&#4096;&#4142;&#4152;&#4152;&#4223;&#4121;&#4141;&#4147;.&#4145;&#4103;&#4112;&#4125;&#4116;&#4153;&#4145;&#4096;&#4154;&#4140;&#4100;&#4153;&#4152; &#4145;&#4112;&#4140;&#4153;&#4112;&#4124;&#4100;&#4153;&#4152;&#4124; &#4112;&#4123;&#4140;&#4152;&#4101;&#4097;&#4116;&#4153;&#4152; 
								(&#4161;&#4160;)<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/138-HtooGyiSayadaw-Alokpay-22-9-2009-am.mp3">
								&#4161;&#4163;&#4168;&#4171; &#4162;&#4162;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/139-HtooGyiSayadaw-Lawkachanthar-22-9-2009-pm.mp3">
								&#4161;&#4163;&#4169;&#4171; &#4162;&#4162;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4145;&#4124;&#4140;&#4096;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140; (&#4161;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/140-HtooGyiSayadaw-Alokepay-23-8-2009-am-Thamathana.mp3">
								&#4161;&#4164;&#4160;&#4171; &#4162;&#4163;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/141-HtooGyiSayadaw-23-8-2009-TacarKhau-nete.mp3">
								&#4161;&#4164;&#4161;&#4171; &#4162;&#4163;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4145;&#4124;&#4140;&#4096;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140; (&#4162;)<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/142-HtooGyiSayadaw-Chanthar2-24-8-2009.mp3">
								&#4161;&#4164;&#4162;&#4171; &#4162;&#4164;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4239;&#4141; &#4209;&#4126;&#4143;&#4097;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/143-HtooGyiSayadaw-24-8-2009-Thatipaxan.mp3">
								&#4161;&#4164;&#4163;&#4171; &#4162;&#4164;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116;</a> - &#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/144-HtooGyiSayadaw-Apetankhapaetnavanpwint.mp3">
								&#4161;&#4164;&#4164;&#4171; &#4162;&#4165;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4123;&#4157;&#4101;&#4153;&#4117;&#4139;&#4152;&#4126;&#4142;&#4124;&#4145;&#4117;&#4152;&#4173; 
								&#4129;&#4116;&#4141;&#4101;&#4197;&#4170;&#4114;&#4143;&#4096;&#4193;&#4170;&#4129;&#4116;&#4112;&#4209; &#4124;&#4096;&#4193;&#4111;&#4145;&#4123;&#4152; (&#4163;)&#4117;&#4139;&#4152;&#4096;&#4141;&#4143;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4126;&#4106;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/145-HtooGyiSayadaw-25-8-2009-Amyaikchanthar.mp3">
								&#4161;&#4164;&#4165;&#4171; &#4162;&#4165;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4129;&#4223;&#4121;&#4141;&#4147;&#4096;&#4153;&#4097;&#4154;&#4121;&#4153;&#4152;&#4126;&#4140;&#4170;&#4125;&#4141;&#4117;&#4230;&#4116;&#4140;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/146-HtooGyiSayadaw-HtwatmyoutyaAlokpay.mp3">
								&#4161;&#4164;&#4166;&#4171; &#4162;&#4166;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4096;&#4141;&#4143;&#4122;&#4153;&#4151;&#4133;&#4140;&#4111;&#4153;&#4096;&#4141;&#4143;&#4122;&#4153;&#4101;&#4101;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/147-HtooGyiSayadaw-26-8-2009-Sulathawtapan.mp3">
								&#4161;&#4164;&#4167;&#4171; &#4162;&#4166;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4101;&#4144;&#4128;&#4145;&#4126;&#4140;&#4112;&#4117;&#4116;&#4153;&#4127;&#4144;&#4126;&#4106;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/148-HtooGyiSayadaw-Seitarnupathana.mp3">
								&#4161;&#4164;&#4168;&#4171; &#4162;&#4167;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4101;&#4141;&#4112;&#4209;&#4140;&#4239;&#4143;&#4117;&#4230;&#4116;&#4140; &#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/149-HtooGyiSayadaw-27-8-2009-Waydanarshu-khwar.mp3">
								&#4161;&#4164;&#4169;&#4171; &#4162;&#4167;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4145;&#4125;&#4114;&#4116;&#4140;&#4123;&#4232;&#4245;&#4117;&#4156;&#4140;&#4152;&#4116;&#4106;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/150-HtooGyiSayadaw-Thatipahtarnabawana.mp3">
								&#4161;&#4165;&#4160;&#4171; &#4162;&#4168;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4112;&#4141;&#4117;&#4242;&#4140;&#4116;&#4153;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/151-HtooGyiSayadaw-28-8-2009-nandakawwada.mp3">
								&#4161;&#4165;&#4161;&#4171; &#4162;&#4168;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- 
								&#4114;&#4141;&#4156;&#4127;&#4141;&#4112;&#4153;&#4170;&#4112;&#4141;&#4127;&#4141;&#4112;&#4153;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4126;&#4106;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/152-HtooGyiSayadaw-29-8-2009-BarwanaAlokeyay.mp3">
								&#4161;&#4165;&#4162;&#4171; &#4162;&#4169;-&#4168;-&#4162;&#4160;&#4160;&#4169;&#4116;&#4150;&#4096;&#4153; </a>- &#4129;&#4124;&#4143;&#4117;&#4153;&#4145;&#4117;&#4152;&#4112;&#4123;&#4140;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/153-HtooGyiSayadaw-29-8-2009-thatsanidan.mp3">
								&#4161;&#4165;&#4163;&#4171; &#4162;&#4169;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4126;&#4101;&#4197;&#4140;&#4116;&#4141;&#4114;&#4139;&#4116;&#4153;&#4152;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/154-HtooGyiSayadaw-Waydananupathana.mp3">
								&#4161;&#4165;&#4164;&#4171; &#4163;&#4160;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4116;&#4150;&#4096;&#4153; </a>- &#4126;&#4142;&#4124;&#4145;&#4117;&#4152;&#4173; &#4145;&#4125;&#4114;&#4116;&#4140; 
								&#4125;&#4141;&#4117;&#4230;&#4116;&#4140;&#4096;&#4141;&#4143;&#4123;&#4157;&#4100;&#4153;&#4152;&#4223;&#4117;&#4126;&#4106;&#4153;&#4171;<br>
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3DVD-01/155-HtooGyiSayadaw-30-8-2009-Thitsakeiksanyan.mp3">
								&#4161;&#4165;&#4165;&#4171; &#4163;&#4160;-&#4168;-&#4162;&#4160;&#4160;&#4169; &#4106;&#4145;&#4116; </a>- &#4126;&#4101;&#4197;&#4133;&#4140;&#4111;&#4153;&#4170;&#4096;&#4141;&#4101;&#4197;&#4133;&#4140;&#4111;&#4153;<br>
&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<br>
								~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
								&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<b><font size="5">MP3 Disc 1</font></b></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/001-U-EindarWudaebhivamsa-8-6-2005-AM.mp3">&#4161;&#4171; &#4168;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/002-U-EindarWudaebhivamsa-9-6-2005-AM.mp3">
								&#4162;&#4171; &#4169;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/003-U-EindarWudaebhivamsa-10-6-2005-AM.mp3">
								&#4163;&#4171; &#4161;&#4160;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/004-U-EindarWudaebhivamsa-11-6-2005-AM.mp3">
								&#4164;&#4171; &#4161;&#4161;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/005-U-EindarWudaebhivamsa-12-6-2005-AM.mp3">
								&#4165;&#4171; &#4161;&#4162;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/006-U-EindarWudaebhivamsa-13-6-2005-AM.mp3">
								&#4166;&#4171; &#4161;&#4163;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/007-U-EindarWudaebhivamsa-14-6-2005-AM.mp3">
								&#4167;&#4171; &#4161;&#4164;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/008-U-EindarWudaebhivamsa-15-6-005-AM.mp3">&#4168;&#4171; &#4161;&#4165;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/009-U-EindarWudaebhivamsa-16-6-2005-AM.mp3">
								&#4169;&#4171; &#4161;&#4166;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D1/010-U-EindarWudaebhivamsa-17-6-2005-AM.mp3">
								&#4161;&#4160;&#4171; &#4161;&#4167;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4"><br>
&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<b><font size="5">MP3 Disc </font></b>
								<font size="5"><b>2</b></font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/001-U-EindarWudaebhivamsa-8-6-2005-PM.mp3">
								&#4161;&#4171; &#4168;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/002-U-EindarWudaebhivamsa-9-6-2005-PM.mp3">
								&#4162;&#4171; &#4169;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/003-U-EindarWudaebhivamsa-10-6-2005-PM.mp3">
								&#4163;&#4171; &#4161;&#4160;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/004-U-EindarWudaebhivamsa-11-6-2005-PM.mp3">
								&#4164;&#4171; &#4161;&#4161;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/005-U-EindarWudaebhivamsa-12-6-2005-PM.mp3">
								&#4165;&#4171; &#4161;&#4162;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/006-U-EindarWudaebhivamsa-13-6-2005-PM.mp3">
								&#4166;&#4171; &#4161;&#4163;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/007-U-EindarWudaebhivamsa-14-6-2005-PM.mp3">
								&#4167;&#4171; &#4161;&#4164;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/008-U-EindarWudaebhivamsa-15-6-2005-PM.mp3">
								&#4168;&#4171; &#4161;&#4165;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/009-U-EindarWudaebhivamsa-16-6-2005-PM.mp3">
								&#4169;&#4171; &#4161;&#4166;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D2/010-U-EindarWudaebhivamsa-17-6-2005-PM.mp3"> 
								&#4161;&#4160;&#4171; &#4161;&#4167;-&#4166;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4140;&#4145;&#4124;&#4152;&#4117;&#4139;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4"><br>
								<br>
								<br>
&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<b><font size="5">MP3 Disc </font></b>
								<font size="5"><b>3</b></font>&nbsp;</p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/001-U-EindarWudaebhivamsa-20-11-2005-AM.mp3">&#4161;&#4171; &#4162;&#4160;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4129;&#4239;&#4143;&#4170; &#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;)</a> </font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/002-U-EindarWudaebhivamsa-20-11-2005-PM.mp3">&#4162;&#4171; &#4162;&#4160;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4124;&#4140;&#4155;&#4097;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4152;&#4173; 
								&#4155;&#4117;&#4116;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152;&#4145;&#4096;&#4140;&#4100;&#4153;&#4117;&#4139;&#4145;&#4101; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/003-U-EindarWudaebhivamsa-21-11-2005-AM.mp3">&#4163;&#4171; &#4162;&#4161;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4129;&#4239;&#4143;&#4170; &#4117;&#4107;&#4141;&#4145;&#4124;&#4140;&#4121; &#4117;&#4107;&#4141;&#4101;&#4197;&#4126;&#4121;&#4143;&#4117;&#4216;&#4139;&#4114;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4162;)</a> </font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/004-U-EindarWudaebhivamsa-21-11-2005-PM.mp3">&#4164;&#4171; &#4162;&#4161;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4097;&#4143;&#4123;&#4232; &#4097;&#4143;&#4223;&#4100;&#4141;&#4121;&#4153;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/005-U-EindarWudaebhivamsa-22-11-2005-AM.mp3">&#4165;&#4171; &#4162;&#4162;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4160;&#4107;&#4153;&#4121;&#4157;&#4140;&#4129;&#4223;&#4121;&#4146; &#4100;&#4123;&#4146;&#4121;&#4157;&#4140;&#4129;&#4117; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/006-U-EindarWudaebhivamsa-22-11-2005-PM.mp3">&#4166;&#4171; &#4162;&#4162;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4101;&#4141;&#4112;&#4153;&#4175;&#4102;&#4116;&#4153;&#4222;&#4096;&#4122;&#4153;&#4117;&#4143;&#4150; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/007-U-EindarWudaebhivamsa-23-11-2005-AM.mp3">&#4167;&#4171; &#4162;&#4163;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4126;&#4121;&#4100;&#4153;&#4145;&#4121;&#4156;&#4152;&#4123;&#4100;&#4153;&#4152; &#4096;&#4154;&#4140;&#4152;&#4101;&#4140;&#4152;&#4123;&#4100;&#4153;&#4152; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/008-U-EindarWudaebhivamsa-23-11-2005-PM.mp3">&#4168;&#4171; &#4162;&#4163;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4129;&#4116;&#4112;&#4209;&#4121;&#4154;&#4096;&#4153;&#4124;&#4143;&#4150;&#4152; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/009-U-EindarWudaebhivamsa-24-11-2005-AM.mp3">&#4169;&#4171; &#4162;&#4164;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4126;&#4112;&#4209;&#4141;&#4239;&#4157;&#4100;&#4153;&#4151; &#4119;&#4154;&#4112;&#4209;&#4141; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D3/010-U-EindarWudaebhivamsa-24-11-2005-PM.mp3">&#4161;&#4160;&#4171; &#4162;&#4164;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4145;&#4226;&#4096;&#4156;&#4152;&#4112;&#4100;&#4153;&#4123;&#4100;&#4153; &#4121;&#4098;&#4194;&#4100;&#4153;&#4116;&#4146;&#4245;&#4102;&#4117;&#4153; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4"><br>
&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4"><br>
&nbsp;</font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<b><font size="5">MP3 Disc 4</font></b></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/001-U-EindarWudaebhivamsa-25-11-2005-AM.mp3">
								&#4161;&#4171; &#4162;&#4165;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4120;&#4160;&#4145;&#4123;&#4101;&#4096;&#4153;&#4239;&#4157;&#4100;&#4153; &#4115;&#4121;&#4220;&#4101;&#4096;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/002-U-EindarWudaebhivamsa-25-11-2005-PM.mp3">
								&#4162;&#4171; &#4162;&#4165;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4123;&#4112;&#4116;&#4140;&#4101;&#4141;&#4116;&#4153;&#4145;&#4096;&#4154;&#4140;&#4096;&#4153; &#4103;&#4122;&#4153;&#4145;&#4112;&#4140;&#4096;&#4153;&#4112;&#4116;&#4153;&#4152; 
								&#4096;&#4101;&#4140;&#4152;&#4123;&#4145;&#4129;&#4140;&#4100;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/003-U-EindarWudaebhivamsa-26-11-2005-AM.mp3">
								&#4163;&#4171; &#4162;&#4166;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4097;&#4239;&#4214;&#4140;&#4129;&#4101;&#4133;&#4153; &#4133;&#4140;&#4111;&#4153;&#4160;&#4100;&#4153;&#4146;&#4155;&#4118;&#4112;&#4153;&#4117;&#4143;&#4150; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/004-U-EindarWudaebhivamsa-26-11-2005-PM.mp3">
								&#4164;&#4171; &#4162;&#4166;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4145;&#4112;&#4124;&#4117;&#4112;&#4209;&#4103;&#4140;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4161;)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/005-U-EindarWudaebhivamsa-27-11-2005-AM.mp3">
								&#4165;&#4171; &#4162;&#4167;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4129;&#4116;&#4140;&#4113;&#4117;&#4141;&#4241;&#4141;&#4145;&#4096;&#4140;&#4160;&#4139;&#4114;&#4126;&#4143;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/006-U-EindarWudaebhivamsa-27-11-2005-PM.mp3">
								&#4166;&#4171; &#4162;&#4167;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4145;&#4112;&#4124;&#4117;&#4112;&#4209;&#4103;&#4140;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4162;)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/007-U-EindarWudaebhivamsa-28-11-2005-AM.mp3">
								&#4167;&#4171; &#4162;&#4168;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4160;&#4096;&#4192;&#4124;&#4141;&#4121;&#4145;&#4113;&#4123;&#4153;&#4160;&#4112;&#4211;&#4147; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/008-U-EindarWudaebhivamsa-28-11-2005-PM.mp3">
								&#4168;&#4171; &#4162;&#4168;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4145;&#4112;&#4124;&#4117;&#4112;&#4209;&#4103;&#4140;&#4112;&#4153; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; (&#4163;)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/009-U-EindarWudaebhivamsa-29-11-2005-AM.mp3">
								&#4169;&#4171; &#4162;&#4169;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4116;&#4150;&#4096;&#4153; &#4124;&#4121;&#4153;&#4102;&#4143;&#4150;&#4152;&#4124;&#4157;&#4154;&#4100;&#4153;&#4123;&#4156;&#4140;&#4145;&#4112;&#4156;&#4245; &#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153; 
								(&#4161;)</a></font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4">
								<a title="To download to your hard disc, please right click and choose &quot;save target as&quot;." href="http://dhammadownload.com/MP3Library/
U-EindarWudaebhivamsa-HtooGyiSayadaw/MP3D4/010-U-EindarWudaebhivamsa-29-11-2005-PM.mp3">
								&#4161;&#4160;&#4171; &#4162;&#4169;-&#4161;&#4161;-&#4162;&#4160;&#4160;&#4165; &#4106;&#4145;&#4116; &#4126;&#4101;&#4197;&#4133;&#4140;&#4111;&#4153;&#4121;&#4157;&#4140; &#4133;&#4142;&#4152;&#4097;&#4141;&#4143;&#4096;&#4153;&#4155;&#4097;&#4100;&#4153;&#4152; 
								&#4112;&#4123;&#4140;&#4152;&#4145;&#4112;&#4140;&#4153;</a></font></p>
								<p align="left" style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								<font face="Zawgyi-One" size="4"><br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
								<br>
&nbsp;</font></p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
								<p style="MARGIN-TOP: 0px; MARGIN-BOTTOM: 0px">
								&nbsp;</p>
"""


soup = bs4(text, 'html.parser')

with open('titles_links.txt', 'w') as f:
    for key in soup.find_all('p'):
        if key.find('a'):
            t = '\t' * 10
            print(''.join(key.find('a').get_text().split('\n'+t)))
            
            
        #print('{}'.format(''.join(key.get('href').split(' '))))
        #print('{}'.format(''.join(key.get_text().split( ))))
        #f.write('{} {}\n'.format(key.get('href'), key.get_text()))
        #f.write('{} {}\n'.format(''.join(key.get('href').split( )), ''.join(key.get_text().split( ))))
        
"""
with open('file.txt', 'w') as f:
    for key in soup.find_all('a'):
        f.write('{}\n'.format(''.join(key.get('href').split( ))))

with open('titles.txt', 'w') as f:
    for key in soup.find_all('a'):        
        f.write('{}\n'.format(''.join(key.get_text().split( ))))        
"""


