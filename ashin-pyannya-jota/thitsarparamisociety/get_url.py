from bs4 import BeautifulSoup as bs4

text = """


<header id="page-header">

    <div id="header-top">

        <div class="wrapper clearfix">

            <div id="logo-image">

            
                <a href="https://www.thitsarparamisociety.com"><img src="https://www.thitsarparamisociety.com/wp-content/uploads/2017/03/Banner-1.jpg" alt="Thitsarparami Buddhist Society | Dhamma mp3 Download"></a>

            
            </div>

            <div id="header-left" class="clearfix">

                <ul class="socials-link clearfix">

                    


                    


                    


                    


                    


                    
                </ul>

                <!-- socials-link -->



                
                    

            </div>

            <!-- header-left -->

        </div>

        <!-- wrapper -->

    </div>

    <!-- header-top -->

    <div id="header-bottom">

        <div class="wrapper clearfix">

            <nav id="main-nav">

            <ul id="main-menu" class="menu clearfix sf-js-enabled sf-arrows"><li class="menu-home-item"><a data-icon="" href="https://www.thitsarparamisociety.com"></a></li><li id="menu-item-34" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-34"><a href="https://www.thitsarparamisociety.com/">မူလစာမ်က္ႏွာ</a></li>
<li id="menu-item-13" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-13"><a href="https://www.thitsarparamisociety.com/%e1%80%9e%e1%80%85%e1%81%a5%e1%80%ac%e1%80%95%e1%80%ab%e1%80%9b%e1%80%99%e1%80%ae/" class="sf-with-ul">သစၥာပါရမီ</a>
<ul class="sub-menu" style="display: none;">
	<li id="menu-item-73" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-73"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%9b%e1%80%ac%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9-%e1%80%a1%e1%80%90%e1%81%b3%e1%80%b3%e1%80%95/">သစၥာပါရမီ ဆရာေတာ္ ေဒါက္တာ အရွင္ဇယ်တိႆ  ေထ႐ုပၸတၱိ</a></li>
	<li id="menu-item-14" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14"><a href="https://www.thitsarparamisociety.com/thitsarparami/">စကၤာပူႏုိင္ငံ၊ သစၥာပါရမီရိပ္သာ မုိးကုတ္ဝိပႆနာ ျပည္ပအဖြဲ႕ခြဲ (၁) ျဖစ္ေပၚလာျခင္းအေၾကာင္း</a></li>
	<li id="menu-item-86" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-86"><a href="https://www.thitsarparamisociety.com/dr-ashinjayatissa/">ဆရာေတာ္ MP3 တရားေတာ္မ်ား</a></li>
	<li id="menu-item-316" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-316"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%9b%e1%80%ac%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9-%e1%80%9b%e1%80%af%e1%80%95%e1%80%b9%e1%80%9e%e1%80%b6-%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9/">ဆရာေတာ္ ရုပ္သံ တရားေတာ္မ်ား</a></li>
	<li id="menu-item-87" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-87"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%9b%e1%80%ac%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9-%e1%80%85%e1%80%ac%e1%80%a1%e1%80%af%e1%80%95%e1%80%b9/">ဆရာေတာ္ ဓမၼစာအုပ္မ်ား</a></li>
	<li id="menu-item-72" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-72"><a href="https://www.thitsarparamisociety.com/%e1%80%99%e1%80%ad%e1%80%af%e1%80%b8%e1%80%80%e1%80%af%e1%80%90%e1%80%b9-%e1%80%a1%e1%80%90%e1%81%b3%e1%80%b3%e1%80%95/">ေက်းဇူးေတာ္ရွင္ မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး၏ ေထရုပၸတၱိအက်ဥ္း</a></li>
</ul>
</li>
<li id="menu-item-20" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-20"><a href="https://www.thitsarparamisociety.com/%e1%80%93%e1%80%99%e1%81%bc-%e1%80%a5%e1%80%9a%e1%80%ba%e1%80%ac%e1%80%a5%e1%80%b9/" class="sf-with-ul">တရားေတာ္မ်ား</a>
<ul class="sub-menu" style="display: none;">
	<li id="menu-item-50" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-50"><a href="https://www.thitsarparamisociety.com/mp3-%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9/">MP3 တရားေတာ္မ်ား</a></li>
	<li id="menu-item-43" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43"><a href="https://www.thitsarparamisociety.com/%e1%80%9b%e1%80%af%e1%80%95%e1%80%b9%e1%80%9e%e1%80%b6%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9/">ရုပ္သံ တရားေတာ္မ်ား</a></li>
</ul>
</li>
<li id="menu-item-5783" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-5783"><a href="https://www.thitsarparamisociety.com/%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%85%e1%80%ac%e1%80%a1%e1%80%af%e1%80%95%e1%80%b9%e1%80%99%e1%80%ba%e1%80%ac%e1%80%b8/" class="sf-with-ul">တရားစာအုပ္မ်ား</a>
<ul class="sub-menu" style="display: none;">
	<li id="menu-item-1312" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1312"><a href="https://www.thitsarparamisociety.com/%e1%80%9b%e1%80%af%e1%80%95%e1%80%b9%e1%80%85%e1%80%b6%e1%80%af%e1%80%97%e1%80%af%e1%80%92%e1%81%b6%e1%80%9e%e1%80%ac%e1%80%9e%e1%80%94%e1%80%ac%e1%80%9d%e1%80%84%e1%80%b9/">ရုပ္စံုဗုဒၶသာသနာဝင္</a></li>
	<li id="menu-item-13132" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-13132"><a href="http://www.thitsarparamisociety.com/?p=35">တရား စာအုပ္မ်ား</a></li>
</ul>
</li>
<li id="menu-item-127" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-127"><a href="https://www.thitsarparamisociety.com/live/">တိုက္ရိုက္ထုတ္လႊင့္မႈ</a></li>
<li id="menu-item-6462" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6462"><a href="https://www.thitsarparamisociety.com/24hrs-radio/">၂၄နာရီ ေရဒီယို</a></li>
<li id="menu-item-108" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-108"><a href="https://www.thitsarparamisociety.com/%e1%80%80%e1%80%af%e1%80%9e%e1%80%ad%e1%80%af%e1%80%9c%e1%80%b9-%e1%80%95%e1%80%b6%e1%80%af%e1%80%9b%e1%80%ad%e1%80%95%e1%80%b9%e1%80%99%e1%80%ba%e1%80%ac%e1%80%b8/">ကုသိုလ္ ပံုရိပ္မ်ား</a></li>
<li id="menu-item-107" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-107"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%80%e1%80%b9%e1%80%9e%e1%80%bc%e1%80%9a%e1%80%b9%e1%80%9b%e1%80%94%e1%80%b9/">ဆက္သြယ္ရန္</a></li>
</ul><div id="mobile-menu" class="menu-%e1%80%9e%e1%80%85%e1%81%a5%e1%80%ac%e1%80%95%e1%80%ab%e1%80%9b%e1%80%99%e1%80%ae-container"><span>Menu</span><ul id="toggle-view-menu"><li class="clearfix"><h3><a href="https://www.thitsarparamisociety.com">Home</a></h3></li><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-34 clearfix"><h3><a href="https://www.thitsarparamisociety.com/">မူလစာမ်က္ႏွာ</a></h3></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-13 clearfix"><h3><a href="https://www.thitsarparamisociety.com/%e1%80%9e%e1%80%85%e1%81%a5%e1%80%ac%e1%80%95%e1%80%ab%e1%80%9b%e1%80%99%e1%80%ae/">သစၥာပါရမီ</a></h3>
<span>+</span><div class="clear"></div><div class="menu-panel clearfix"><ul>	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-73"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%9b%e1%80%ac%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9-%e1%80%a1%e1%80%90%e1%81%b3%e1%80%b3%e1%80%95/">သစၥာပါရမီ ဆရာေတာ္ ေဒါက္တာ အရွင္ဇယ်တိႆ  ေထ႐ုပၸတၱိ</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14"><a href="https://www.thitsarparamisociety.com/thitsarparami/">စကၤာပူႏုိင္ငံ၊ သစၥာပါရမီရိပ္သာ မုိးကုတ္ဝိပႆနာ ျပည္ပအဖြဲ႕ခြဲ (၁) ျဖစ္ေပၚလာျခင္းအေၾကာင္း</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-86"><a href="https://www.thitsarparamisociety.com/dr-ashinjayatissa/">ဆရာေတာ္ MP3 တရားေတာ္မ်ား</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-316"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%9b%e1%80%ac%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9-%e1%80%9b%e1%80%af%e1%80%95%e1%80%b9%e1%80%9e%e1%80%b6-%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9/">ဆရာေတာ္ ရုပ္သံ တရားေတာ္မ်ား</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-87"><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%9b%e1%80%ac%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9-%e1%80%85%e1%80%ac%e1%80%a1%e1%80%af%e1%80%95%e1%80%b9/">ဆရာေတာ္ ဓမၼစာအုပ္မ်ား</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-72"><a href="https://www.thitsarparamisociety.com/%e1%80%99%e1%80%ad%e1%80%af%e1%80%b8%e1%80%80%e1%80%af%e1%80%90%e1%80%b9-%e1%80%a1%e1%80%90%e1%81%b3%e1%80%b3%e1%80%95/">ေက်းဇူးေတာ္ရွင္ မိုးကုတ္ဆရာေတာ္ဘုရားႀကီး၏ ေထရုပၸတၱိအက်ဥ္း</a></li>
</ul></div>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-20 clearfix"><h3><a href="https://www.thitsarparamisociety.com/%e1%80%93%e1%80%99%e1%81%bc-%e1%80%a5%e1%80%9a%e1%80%ba%e1%80%ac%e1%80%a5%e1%80%b9/">တရားေတာ္မ်ား</a></h3>
<span>+</span><div class="clear"></div><div class="menu-panel clearfix"><ul>	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-50"><a href="https://www.thitsarparamisociety.com/mp3-%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9/">MP3 တရားေတာ္မ်ား</a></li>
	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43"><a href="https://www.thitsarparamisociety.com/%e1%80%9b%e1%80%af%e1%80%95%e1%80%b9%e1%80%9e%e1%80%b6%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%b1%e1%80%90%e1%80%ac%e1%80%b9/">ရုပ္သံ တရားေတာ္မ်ား</a></li>
</ul></div>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-5783 clearfix"><h3><a href="https://www.thitsarparamisociety.com/%e1%80%90%e1%80%9b%e1%80%ac%e1%80%b8%e1%80%85%e1%80%ac%e1%80%a1%e1%80%af%e1%80%95%e1%80%b9%e1%80%99%e1%80%ba%e1%80%ac%e1%80%b8/">တရားစာအုပ္မ်ား</a></h3>
<span>+</span><div class="clear"></div><div class="menu-panel clearfix"><ul>	<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1312"><a href="https://www.thitsarparamisociety.com/%e1%80%9b%e1%80%af%e1%80%95%e1%80%b9%e1%80%85%e1%80%b6%e1%80%af%e1%80%97%e1%80%af%e1%80%92%e1%81%b6%e1%80%9e%e1%80%ac%e1%80%9e%e1%80%94%e1%80%ac%e1%80%9d%e1%80%84%e1%80%b9/">ရုပ္စံုဗုဒၶသာသနာဝင္</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-13132"><a href="http://www.thitsarparamisociety.com/?p=35">တရား စာအုပ္မ်ား</a></li>
</ul></div>
</li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-127 clearfix"><h3><a href="https://www.thitsarparamisociety.com/live/">တိုက္ရိုက္ထုတ္လႊင့္မႈ</a></h3></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6462 clearfix"><h3><a href="https://www.thitsarparamisociety.com/24hrs-radio/">၂၄နာရီ ေရဒီယို</a></h3></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-108 clearfix"><h3><a href="https://www.thitsarparamisociety.com/%e1%80%80%e1%80%af%e1%80%9e%e1%80%ad%e1%80%af%e1%80%9c%e1%80%b9-%e1%80%95%e1%80%b6%e1%80%af%e1%80%9b%e1%80%ad%e1%80%95%e1%80%b9%e1%80%99%e1%80%ba%e1%80%ac%e1%80%b8/">ကုသိုလ္ ပံုရိပ္မ်ား</a></h3></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-107 clearfix"><h3><a href="https://www.thitsarparamisociety.com/%e1%80%86%e1%80%80%e1%80%b9%e1%80%9e%e1%80%bc%e1%80%9a%e1%80%b9%e1%80%9b%e1%80%94%e1%80%b9/">ဆက္သြယ္ရန္</a></h3></li>
</ul></div>
            </nav>

            <!-- main-nav -->

            <div class="search-box clearfix">



                


            </div>

            <!--search-box-->

        </div>

        <!-- wrapper -->

    </div>

    <!-- header-bottom -->

</header>

<!-- page-header -->



<div id="main-content">

    <div class="wrapper clearfix">
<div class="col-a">
        
    <div id="page-7741" class="elements-box post-7741 page type-page status-publish hentry">
        <h5><span style="color: #339966;">ဓမၼဒူတ အရွင္ပညာေဇာတ (ေတာင္စြန္း) ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား စုစည္းမွု (MP3)</span></h5>
<p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/01-DhammaDutaAshinPyannaJota%20PyoneThayMatThay.mp3"><span style="color: #ff9900;">၁။ ၿပံဳးေသမဲ့ေသ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/02-DhammaDutaAshinPyannaJota%20NhaLoneThwinMhanMhaNibbanYa.mp3"><span style="color: #ff9900;">၂။ ႏွလုံးသြင္းမွန္မွ နိဗၺာန္ရ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/03-DhammaDutaAshinPyannaJota%20PhaYarPwintYaKoung.mp3"><span style="color: #ff9900;">၃။ ဘုရားပြင့္ရေၾကာင္း</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/04-DhammaDutaAshinPyannaJota%20VippasanaMaKhetDarNaKhet.mp3"><span style="color: #ff9900;">၄။ ၀ိပႆနာမခက္ ဒါနခက္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/05-DhammaDutaAshinPyannaJota%20AhSheatMharKaTaYarMaYa.mp3"><span style="color: #ff9900;">၅။ အေရွ႕မွားက တရားမရ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/06-DhammaDutaAshinPyannaJota%20BaTaYarLonMhaKongTaNee.mp3"><span style="color: #ff9900;">၆။ ဘယ္တရားလြန္မွ ေကာင္းသနည္း</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/07-DhammaDutaAshinPyannaJota%20MoeaSoeLayKongKoTwinHlaung.mp3"><span style="color: #ff9900;">၇။ ေႁမြဆိုးေလးေကာင္ ကိုယ္တြင္းေလွာင္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/08-DhammaDutaAshinPyannaJota%20ThaKhinTaHleaKuanTaHlea.mp3"><span style="color: #ff9900;">၈။ သခင္တလွၫ့္ကြၽန္တလွၫ့္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/09-DhammaDutaAshinPyannaJota%20ThayMinNatSitKhinPwe.mp3"><span style="color: #ff9900;">၉။ ေသမင္းႏွင့္ စစ္ခင္းပြဲ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/10-DhammaDutaAshinPyannaJota%20ThayYoarThoarThawKhanDar.mp3"><span style="color: #ff9900;">၁၀။ ေသရြာသြားခႏၶာ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/11-DhammaDutaAshinPyannaJota%20WouldKyutLayMhaNaibanYa.mp3"><span style="color: #ff9900;">၁၁။ ၀ဋ္ကြၽတ္ေလမွ နိဗၺာန္ရ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/12-DhammaDutaAshinPyannaJota%20YokMyatThanThaYarHletLaiShar.mp3"><span style="color: #ff9900;">၁၂။ ယုတ္ျမတ္သံသရာလွၫ့္လည္ရွာ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/13-DhammaDutaAshinPyannaJota%20AteChinNoeChin.mp3"><span style="color: #ff9900;">၁၃။ အိပ္ျခင္းႏိုးျခင္း</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/14-DhammaDutaAshinPyannaJota%20KaBarAhsaNhitThaTaWarAhSa.mp3"><span style="color: #ff9900;">၁၄။ ကမၻာအစႏွင့္ သတၲ၀ါအစ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/15-DhammaDutaAshinPyannaJota%20KaungHluDanYaKyoPhaLa.mp3"><span style="color: #ff9900;">၁၅။ ေက်ာင္းလႈဒါန္းရက်ိဳးဖလ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/16-DhammaDutaAshinPyannaJota%20KoeKoKoeMyarChitParYatLah.mp3"><span style="color: #ff9900;">၁၆။ ကိုယ့္ကိုကိုယ္မ်ား ခ်စ္ပါရဲ႕လား</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/17-DhammaDutaAshinPyannaJota%20HluKyoThiMhaThetSonkHlu.mp3"><span style="color: #ff9900;">၁၇။ လႈက်ိဳးသိမွ သက္စြန္႕လႈ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/18-DhammaDutaAshinPyannaJota%20NharPhyarWinLyinThaTeatShin.mp3"><span style="color: #ff9900;">၁၈။ နာဖ်ား၀င္လွ်င္ သတိယွဥ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/19-DhammaDutaAshinPyannaJota%20NyeSetYarYarTetThi.mp3"><span style="color: #ff9900;">၁၉။ နီးစပ္ရာပါတတ္သည္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/20-DhammaDutaAshinPyannaJota%20SwonSarSinChinYan.mp3"><span style="color: #ff9900;">၂၀။ ဆြမ္းစားဆင္ျခင္ရန္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/21-DhammaDutaAshinPyannaJota%20AhTuMaSheatLayParTaYar.mp3"><span style="color: #ff9900;">၂၁။ အတုမရွိေလးပါး</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/22-DhammaDutaAshinPyannaJota%20BelThuToatKaKoeSounkKyat.mp3"><span style="color: #ff9900;">၂၂။ ဘယ္သူတို႕က ကိုယ္ေစာင့္ၾကပ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/23-DhammaDutaAshinPyannaJota%20KhanDarGyiThiBelThoarNaeLae.mp3"><span style="color: #ff9900;">၂၃။ ခႏၶာႀကီးသည္ ဘယ္သြားေနလဲ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/24-DhammaDutaAshinPyannaJota%20KuThoThiLaBelKyoYa.mp3"><span style="color: #ff9900;">၂၄။ ကုသိုလ္သီလ ဘယ္က်ိဳးရ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/25-DhammaDutaAshinPyannaJota%20LenShinLayMhaShootPhourYa.mp3"><span style="color: #ff9900;">၂၅။ လမ္းရွင္းေလမွ ရႈပြားရ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/26-DhammaDutaAshinPyannaJota%20TheeKhanKyintHarMyatSonePar.mp3"><span style="color: #ff9900;">၂၆။ သည္းခံက်င့္ဟာ ျမတ္ဆုံးပါ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/27-DhammaDutaAshinPyannaJota%20ThinKharNhitLakhaNar.mp3"><span style="color: #ff9900;">၂၇။ သခၤါရႏွင့္ လကၡဏာ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/28-DhammaDutaAshinPyannaJota%20YaeChoChinNhitThetThetLyot.mp3"><span style="color: #ff9900;">၂၈။ ေရခ်ိဳးျခင္းႏွင့္ သက္သတ္လြတ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/29-DhammaDutaAshinPyannaJota%20DhaNaParLaThuHtay.mp3"><span style="color: #ff9900;">၂၉။ ဓနပါလသူေ႒း</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/30-DhammaDutaAshinPyannaJota%20KhanDaThoarLan.mp3"><span style="color: #ff9900;">၃၀။ ခႏၶာ႕သြားရာလမ္း</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/31-DhammaDutaAshinPyannaJota%20KyaeTinShinBaYinSet.mp3"><span style="color: #ff9900;">၃၁။ ေျကြးတင္ရွင္ ဘုရင္ဆပ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/32-DhammaDutaAshinPyannaJota%20KyiePwarKaungYar(7)Pyhar.mp3"><span style="color: #ff9900;">၃၂။ ႀကီးပြားေၾကာင္းရာ (၇)ျဖာ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/33-DhammaDutaAshinPyannaJota%20NaungTa(10)Par.mp3"><span style="color: #ff9900;">၃၃။ ေနာင္တ (၁၀)ပါး</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/34-DhammaDutaAshinPyannaJota%20ChanTharThetShayNyee.mp3"><span style="color: #ff9900;">၃၄။ ခ်မ္းသာသက္ရွည္နည္း</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/35-DhammaDutaAshinPyannaJota%20SanYouSaYarKhanDeeMingala.mp3"><span style="color: #ff9900;">၃၅။ စံယူစရာ ခႏၲီမဂၤလာ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/36-DhammaDutaAshinPyannaJota%20TaikPweNhitMyo.mp3"><span style="color: #ff9900;">၃၆။ တိုက္ပြဲႏွစ္မ်ိဳး</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/37-DhammaDutaAshinPyannaJota%20ThetPuZawKaThetKhanYa.mp3"><span style="color: #ff9900;">၃၇။ သတ္ပူေဇာ္က အသတ္ခံရ</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD1/38-DhammaDutaAshinPyannaJota%20ThayMinThaMan(5)Oo.mp3"><span style="color: #ff9900;">၃၈။ ေသမင္းတမန္(၅)ဦး</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTu MaMayeTu(1)A.mp3"><span style="color: #ff9900;">၃၉။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၁)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTu MaMayeTu(2)A.mp3"><span style="color: #ff9900;">၄၀။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၂)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTu MaMayeTu(3)A.mp3"><span style="color: #ff9900;">၄၁။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၃)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTu MaMayeTu(4)A.mp3"><span style="color: #ff9900;">၄၂။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTuMaMayeTu.(5)A.mp3"><span style="color: #ff9900;">၄၃။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၅)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTuMaMayeTu.(6)A.mp3"><span style="color: #ff9900;">၄၄။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၆)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTuMaMayeTu.(7).mp3"><span style="color: #ff9900;">၄၅။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၇)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTuMaMayeTu.(8)A.mp3"><span style="color: #ff9900;">၄၆။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၈)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTuMaMayeTu.(9).mp3"><span style="color: #ff9900;">၄၇။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၉)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/1-MaeThuMaMaeThu/MayeTuMaMayeTu.(10).mp3"><span style="color: #ff9900;">၄၈။ ေမ့သူမေမ့သူအလုပ္ေပးတရားေတာ္ (၁၀)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/BarKyountDanTainkYaPartalae%20%20%20(A).mp3"><span style="color: #ff9900;">၄၉။ ဘာေၾကာင့္ဒဏ္သင့္ရလဲအလုပ္ေပးတရားေတာ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(1)A.mp3"><span style="color: #ff9900;">၅၀။ ေမြးေမေမတၱာတရားေတာ္ (၁)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(2)A.mp3"><span style="color: #ff9900;">၅၁။ ေမြးေမေမတၱာတရားေတာ္ (၂)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(3)A.mp3"><span style="color: #ff9900;">၅၂။ ေမြးေမေမတၱာတရားေတာ္ (၃)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(4)A.mp3"><span style="color: #ff9900;">၅၃။ ေမြးေမေမတၱာတရားေတာ္ (၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(5)A.mp3"><span style="color: #ff9900;">၅၄။ ေမြးေမေမတၱာတရားေတာ္ (၅)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(6)A.mp3"><span style="color: #ff9900;">၅၅။ ေမြးေမေမတၱာတရားေတာ္ (၆)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(7)A.mp3"><span style="color: #ff9900;">၅၆။ ေမြးေမေမတၱာတရားေတာ္ (၇)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(8)A.mp3"><span style="color: #ff9900;">၅၇။ ေမြးေမေမတၱာတရားေတာ္ (၈)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/2-MwoeMaeMitter/MwoeMae Mittar(9) A.mp3"><span style="color: #ff9900;">၅၈။ ေမြးေမေမတၱာတရားေတာ္ (၉)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/LynSwarNaveVanYoukKyawn A.mp3"><span style="color: #ff9900;">၅၉။ လွ်င္စြာနိဗၺာန္ေရာက္ေၾကာင္းအလုပ္ေပးတရားေတာ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (1)A.mp3"><span style="color: #ff9900;">၆၀။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (၁)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (2)A.mp3"><span style="color: #ff9900;">၆၁။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (၂)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (3)A.mp3"><span style="color: #ff9900;">၆၂။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (၃)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://www.thitsarparamisociety.com/wp- content/uploads/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (4)A.mp3"><span style="color: #ff9900;">၆၃။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (5)A.mp3"><span style="color: #ff9900;">၆၄။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (၅)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (6)A.mp3"><span style="color: #ff9900;">၆၅။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (၆)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/NgarToePyarBarMyarPueCaeTaLae (7)A.mp3"><span style="color: #ff9900;">၆၆။ ငါတိုဘုရားဘာမ်ားလုပ္ခဲ့လဲတရားေတာ္ (ရ)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/TanTaYarWaet A.mp3"><span style="color: #ff9900;">၆၇။ သံသရာ၀ဋ္အလုပ္ေပးတရားေတာ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/3/ThuTawKaungHnanThuYoutMar(TaTiPay).mp3"><span style="color: #ff9900;">၆၈။ သူေတာ္ေကာင္းဟန္သူယုတ္မာ(သတိေပး)တရားေတာ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(01) A.mp3"><span style="color: #ff9900;">၆၉။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၁)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(02)%20%20A.mp3"><span style="color: #ff9900;">၇၀။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၂)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(03)%20%20%20A.mp3"><span style="color: #ff9900;">၇၁။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၃)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(04)%20%20%20A.mp3"><span style="color: #ff9900;">၇၂။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(05)%20%20A.mp3"><span style="color: #ff9900;">၇၃။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၅)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(06)%20%20%20A.mp3"><span style="color: #ff9900;">၇၄။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၆)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(07)%20%20A.mp3"><span style="color: #ff9900;">၇၅။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၇)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(07)%20%20A.mp3"><span style="color: #ff9900;">၇၆။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၈)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(09)%20%20A.mp3"><span style="color: #ff9900;">၇၇။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၉)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/4/ShinTiWaLi(10)%20%20A.mp3"><span style="color: #ff9900;">၇၈။ ရွင္သီ၀လိအထုပ္ပတၱိအေၾကာင္းအရာတရားေတာ္(၁၀)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/5/AYouePwatChin TaYarWin A.mp3"><span style="color: #ff9900;">၈၉။ အရူးေပ်ာက္ခ်င္တရား၀င္အလုပ္ေပးတရားေတာ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/5/BalAkharDarNaHnanMaPyaw BalAkharPyawLae A.mp3"><span style="color: #ff9900;">၈၀။ ဘယ္အခါဒါနႏွင့္မေပ်ာ္ ဘယ္အခါေပ်ာ္လဲတရားေတာ္</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/5/BarHiYaKoHawKyarYaHanDarFatKhan A.mp3"><span style="color: #ff9900;"><span style="color: #ff9900;">၈၁။ ဘာဟိရအားေဟာၾကားရဟႏၲာျဖစ္ေၾကာင္းတရားေတာ္</span></span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/5/KhaeMarMiPhaYar YaHanTarPhytKhan (1)A.mp3"><span style="color: #ff9900;">၈၂။ ေခမာမိဖုရားရဟႏၲာျဖစ္ခန္းတရားေတာ္ (၁)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/5/KhaeMarMiPhaYar YaHanTarPhytKhan (2)A.mp3"><span style="color: #ff9900;">၈၃။ ေခမာမိဖုရားရဟႏၲာျဖစ္ခန္းတရားေတာ္ (၂)</span></a></span></p>
<p><span style="color: #ff9900;"> </span></p>
<p><span style="color: #339966;">ဘုရားရွင္မဟာလကၡဏာေတာ္(၃၂)ပါး တရားေတာ္မ်ား</span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD2/DhammadutaAshinPyinnyaJota-32ParLetKhanartaw-Part(1).mp3"><span style="color: #ff9900;">၁။ တရားေတာ္-အပိုင္း(၁)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD2/DhammadutaAshinPyinnyaJota-32ParLetKhanartaw-Part(2).mp3"><span style="color: #ff9900;">၂။ တရားေတာ္-အပိုင္း(၂)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD2/DhammadutaAshinPyinnyaJota-32ParLetKhanartaw-Part(3).mp3"><span style="color: #ff9900;">၃။ တရားေတာ္-အပိုင္း(၃)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD2/DhammadutaAshinPyinnyaJota-32ParLetKhanartaw-Part(4).mp3"><span style="color: #ff9900;">၄။ တရားေတာ္-အပိုင္း(၄)</span></a></span></p>
<p><span style="color: #ff9900;"><a href="https://media.thitsarparamisociety.com/mp3/Dhammaduta-Ashin-Pyinarzawta(taungson)/DVD2/DhammadutaAshinPyinnyaJota-32ParLetKhanartaw-Part(5).mp3"><span style="color: #ff9900;">၅။ တရားေတာ္-အပိုင္း(၅)</span></a></span></p>
    </div>

    <div class="border-box">
        <div class="wrap-page-links clearfix">
            <div class="page-links">
                            </div><!--page-links-->
        </div><!--wrap-page-links-->
        <div class="clear"></div>
    </div><!-- border-box -->

    
</div>
<!-- col-a -->
<div class="sidebar col-b widget-area-2">
    </div>
<!-- col-b -->
<div class="clear"></div>
    
    </div> <!-- wrapper -->
</div> <!-- main-content -->

<div id="bottom-sidebar">
    <div class="wrapper">
        <header>
            <div id="bottom-logo">
                <a href="https://www.thitsarparamisociety.com">
                    Thitsarparami Buddhist Society | Dhamma mp3 Download                </a>
            </div>
            <p id="back-top">
                <a href="#top"></a>
            </p>
            <!-- back-top -->
        </header>
        <div class="row-fluid">
             
                <div class="span3">
                    <div id="text-7" class="widget widget_text"><h3 class="widget-title">ဓမၼ  ဆံုးမစာမ်ား</h3>			<div class="textwidget"><p>မေကာင္းမႈေရွာင္၊ ေကာင္းမႈေဆာင္၊ ျဖဴအာင္ စိတ္ကိုထား၊<br>
ဘုရားအဆူဆူ၊ မိန္႔ေတာ္မူ၊ အတူတူ ထိုတရား...<br>
<br><a href="http://www.thitsarparamisociety.com/%E1%80%93%E1%80%99%E1%81%BC-%E1%80%86%E1%80%B6%E1%80%AF%E1%80%B8%E1%80%99%E1%80%85%E1%80%AC%E1%80%99%E1%80%BA%E1%80%AC%E1%80%B8/">ဆက္လက္ဖတ္ရႈရန္</a></p>
</div>
		</div>                </div>
             
                <div class="span3">
                    <div id="kopa_widget_text-44" class="widget kopa_widget_text"><h3 class="widget-title">ဗုဒၶဘာသာေျခခံ</h3>        <p>*အမည္- (သိဒၶတၳ) ေဂါတမ</p>
<p>*ခမည္းေတာ္ – သုေဒၶါဒန ေဂါတမ မင္းၾကီး</p>
<p>*မယ္ေတာ္ – မိဖုရား မဟာ မာယာ (ေမြးဖြားျပီး ခုႏွစ္ရက္အၾကာတြင္ေသဆံုးသည္)<br>
<br><a href="http://www.thitsarparamisociety.com/general-knowledge-for-buddhism/">ဆက္လက္ဖတ္ရႈရန္</a></p>
        </div>                </div>
             
                <div class="span3">
                    <div id="kopa_widget_text-57" class="widget kopa_widget_text"><h3 class="widget-title">Thitsarparami App</h3>        <span style="color: #ffffff;">သစၥာပါရမီ Andorid App အသစ္အား Play Store အေကာင့္မရွိသူမ်ား ေဒါင္းလိုပါက ေအာက္ပါပံုအားႏွိပ္ပါ 

<a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/06/DhammaThitsar-release.apk"><img src="https://www.thitsarparamisociety.com/wp-content/uploads/2018/06/get-it-on-android.png"></a>
        </span></div>                </div>
             
                <div class="span3">
                    <div id="search-2" class="widget widget_search"><h3 class="widget-title">ရွာေဖြရန္</h3><form action="https://www.thitsarparamisociety.com" class="search-form clearfix" method="get">
    <input onblur="if (this.value == '')
        this.value = this.defaultValue;" onfocus="if (this.value == this.defaultValue)
        this.value = '';" value="Enter keyworks" name="s" class="search-text" type="text">
    <input value="Go" class="search-submit" type="submit">
</form></div>                </div>
                    </div>
        <!-- row-fluid -->
    </div>
    <!-- wrapper -->
</div>
<!-- bottom-sidebar-->

<footer id="page-footer">
    <div class="wrapper clearfix">
        
        <div id="copyright"><p>Copyright 2014 – Thitsarparami Society. All Rights Reserved.</p>
</div>
        
                
    </div>
    <!-- wrapper -->
</footer>
<!-- page-footer -->

	<script type="text/javascript">
    var pluginUrl = 'https://www.thitsarparamisociety.com/wp-content/plugins/contus-video-gallery/';
	</script>
	<input id="kopa_set_view_count_wpnonce" name="kopa_set_view_count_wpnonce" value="e4cb3c783f" type="hidden"><input id="kopa_set_user_rating_wpnonce" name="kopa_set_user_rating_wpnonce" value="636b4aeec5" type="hidden">	<!--[if lte IE 8]>
	<style>
		.attachment:focus {
			outline: #1e8cbe solid;
		}
		.selected.attachment {
			outline: #1e8cbe solid;
		}
	</style>
	<![endif]-->
	<script type="text/html" id="tmpl-media-frame">
		<div class="media-frame-menu"></div>
		<div class="media-frame-title"></div>
		<div class="media-frame-router"></div>
		<div class="media-frame-content"></div>
		<div class="media-frame-toolbar"></div>
		<div class="media-frame-uploader"></div>
	</script>

	<script type="text/html" id="tmpl-media-modal">
		<div class="media-modal wp-core-ui">
			<button type="button" class="button-link media-modal-close"><span class="media-modal-icon"><span class="screen-reader-text">Close media panel</span></span></button>
			<div class="media-modal-content"></div>
		</div>
		<div class="media-modal-backdrop"></div>
	</script>

	<script type="text/html" id="tmpl-uploader-window">
		<div class="uploader-window-content">
			<h1>Drop files to upload</h1>
		</div>
	</script>

	<script type="text/html" id="tmpl-uploader-editor">
		<div class="uploader-editor-content">
			<div class="uploader-editor-title">Drop files to upload</div>
		</div>
	</script>

	<script type="text/html" id="tmpl-uploader-inline">
		<# var messageClass = data.message ? 'has-upload-message' : 'no-upload-message'; #>
		<# if ( data.canClose ) { #>
		<button class="close dashicons dashicons-no"><span class="screen-reader-text">Close uploader</span></button>
		<# } #>
		<div class="uploader-inline-content {{ messageClass }}">
		<# if ( data.message ) { #>
			<h2 class="upload-message">{{ data.message }}</h2>
		<# } #>
					<div class="upload-ui">
				<h2 class="upload-instructions drop-instructions">Drop files anywhere to upload</h2>
				<p class="upload-instructions drop-instructions">or</p>
				<button type="button" class="browser button button-hero">Select Files</button>
			</div>

			<div class="upload-inline-status"></div>

			<div class="post-upload-ui">
				
				<p class="max-upload-size">Maximum upload file size: 64 MB.</p>

				<# if ( data.suggestedWidth && data.suggestedHeight ) { #>
					<p class="suggested-dimensions">
						Suggested image dimensions: {{data.suggestedWidth}} &times; {{data.suggestedHeight}}
					</p>
				<# } #>

							</div>
				</div>
	</script>

	<script type="text/html" id="tmpl-media-library-view-switcher">
		<a href="/ashin-pyannya-jota/?mode=list" class="view-list">
			<span class="screen-reader-text">List View</span>
		</a>
		<a href="/ashin-pyannya-jota/?mode=grid" class="view-grid current">
			<span class="screen-reader-text">Grid View</span>
		</a>
	</script>

	<script type="text/html" id="tmpl-uploader-status">
		<h2>Uploading</h2>
		<button type="button" class="button-link upload-dismiss-errors"><span class="screen-reader-text">Dismiss Errors</span></button>

		<div class="media-progress-bar"><div></div></div>
		<div class="upload-details">
			<span class="upload-count">
				<span class="upload-index"></span> / <span class="upload-total"></span>
			</span>
			<span class="upload-detail-separator">&ndash;</span>
			<span class="upload-filename"></span>
		</div>
		<div class="upload-errors"></div>
	</script>

	<script type="text/html" id="tmpl-uploader-status-error">
		<span class="upload-error-filename">{{{ data.filename }}}</span>
		<span class="upload-error-message">{{ data.message }}</span>
	</script>

	<script type="text/html" id="tmpl-edit-attachment-frame">
		<div class="edit-media-header">
			<button class="left dashicons <# if ( ! data.hasPrevious ) { #> disabled <# } #>"><span class="screen-reader-text">Edit previous media item</span></button>
			<button class="right dashicons <# if ( ! data.hasNext ) { #> disabled <# } #>"><span class="screen-reader-text">Edit next media item</span></button>
		</div>
		<div class="media-frame-title"></div>
		<div class="media-frame-content"></div>
	</script>

	<script type="text/html" id="tmpl-attachment-details-two-column">
		<div class="attachment-media-view {{ data.orientation }}">
			<div class="thumbnail thumbnail-{{ data.type }}">
				<# if ( data.uploading ) { #>
					<div class="media-progress-bar"><div></div></div>
				<# } else if ( 'image' === data.type && data.sizes && data.sizes.large ) { #>
					<img class="details-image" src="{{ data.sizes.large.url }}" draggable="false" alt="" />
				<# } else if ( 'image' === data.type && data.sizes && data.sizes.full ) { #>
					<img class="details-image" src="{{ data.sizes.full.url }}" draggable="false" alt="" />
				<# } else if ( -1 === jQuery.inArray( data.type, [ 'audio', 'video' ] ) ) { #>
					<img class="details-image icon" src="{{ data.icon }}" draggable="false" alt="" />
				<# } #>

				<# if ( 'audio' === data.type ) { #>
				<div class="wp-media-wrapper">
					<audio style="visibility: hidden" controls class="wp-audio-shortcode" width="100%" preload="none">
						<source type="{{ data.mime }}" src="{{ data.url }}"/>
					</audio>
				</div>
				<# } else if ( 'video' === data.type ) {
					var w_rule = '';
					if ( data.width ) {
						w_rule = 'width: ' + data.width + 'px;';
					} else if ( wp.media.view.settings.contentWidth ) {
						w_rule = 'width: ' + wp.media.view.settings.contentWidth + 'px;';
					}
				#>
				<div style="{{ w_rule }}" class="wp-media-wrapper wp-video">
					<video controls="controls" class="wp-video-shortcode" preload="metadata"
						<# if ( data.width ) { #>width="{{ data.width }}"<# } #>
						<# if ( data.height ) { #>height="{{ data.height }}"<# } #>
						<# if ( data.image && data.image.src !== data.icon ) { #>poster="{{ data.image.src }}"<# } #>>
						<source type="{{ data.mime }}" src="{{ data.url }}"/>
					</video>
				</div>
				<# } #>

				<div class="attachment-actions">
					<# if ( 'image' === data.type && ! data.uploading && data.sizes && data.can.save ) { #>
					<button type="button" class="button edit-attachment">Edit Image</button>
					<# } #>
				</div>
			</div>
		</div>
		<div class="attachment-info">
			<span class="settings-save-status">
				<span class="spinner"></span>
				<span class="saved">Saved.</span>
			</span>
			<div class="details">
				<div class="filename"><strong>File name:</strong> {{ data.filename }}</div>
				<div class="filename"><strong>File type:</strong> {{ data.mime }}</div>
				<div class="uploaded"><strong>Uploaded on:</strong> {{ data.dateFormatted }}</div>

				<div class="file-size"><strong>File size:</strong> {{ data.filesizeHumanReadable }}</div>
				<# if ( 'image' === data.type && ! data.uploading ) { #>
					<# if ( data.width && data.height ) { #>
						<div class="dimensions"><strong>Dimensions:</strong> {{ data.width }} &times; {{ data.height }}</div>
					<# } #>
				<# } #>

				<# if ( data.fileLength ) { #>
					<div class="file-length"><strong>Length:</strong> {{ data.fileLength }}</div>
				<# } #>

				<# if ( 'audio' === data.type && data.meta.bitrate ) { #>
					<div class="bitrate">
						<strong>Bitrate:</strong> {{ Math.round( data.meta.bitrate / 1000 ) }}kb/s
						<# if ( data.meta.bitrate_mode ) { #>
						{{ ' ' + data.meta.bitrate_mode.toUpperCase() }}
						<# } #>
					</div>
				<# } #>

				<div class="compat-meta">
					<# if ( data.compat && data.compat.meta ) { #>
						{{{ data.compat.meta }}}
					<# } #>
				</div>
			</div>

			<div class="settings">
				<label class="setting" data-setting="url">
					<span class="name">URL</span>
					<input type="text" value="{{ data.url }}" readonly />
				</label>
				<# var maybeReadOnly = data.can.save || data.allowLocalEdits ? '' : 'readonly'; #>
								<label class="setting" data-setting="title">
					<span class="name">Title</span>
					<input type="text" value="{{ data.title }}" {{ maybeReadOnly }} />
				</label>
								<# if ( 'audio' === data.type ) { #>
								<label class="setting" data-setting="artist">
					<span class="name">Artist</span>
					<input type="text" value="{{ data.artist || data.meta.artist || '' }}" />
				</label>
								<label class="setting" data-setting="album">
					<span class="name">Album</span>
					<input type="text" value="{{ data.album || data.meta.album || '' }}" />
				</label>
								<# } #>
				<label class="setting" data-setting="caption">
					<span class="name">Caption</span>
					<textarea {{ maybeReadOnly }}>{{ data.caption }}</textarea>
				</label>
				<# if ( 'image' === data.type ) { #>
					<label class="setting" data-setting="alt">
						<span class="name">Alt Text</span>
						<input type="text" value="{{ data.alt }}" {{ maybeReadOnly }} />
					</label>
				<# } #>
				<label class="setting" data-setting="description">
					<span class="name">Description</span>
					<textarea {{ maybeReadOnly }}>{{ data.description }}</textarea>
				</label>
				<label class="setting">
					<span class="name">Uploaded By</span>
					<span class="value">{{ data.authorName }}</span>
				</label>
				<# if ( data.uploadedToTitle ) { #>
					<label class="setting">
						<span class="name">Uploaded To</span>
						<# if ( data.uploadedToLink ) { #>
							<span class="value"><a href="{{ data.uploadedToLink }}">{{ data.uploadedToTitle }}</a></span>
						<# } else { #>
							<span class="value">{{ data.uploadedToTitle }}</span>
						<# } #>
					</label>
				<# } #>
				<div class="attachment-compat"></div>
			</div>

			<div class="actions">
				<a class="view-attachment" href="{{ data.link }}">View attachment page</a>
				<# if ( data.can.save ) { #> |
					<a href="post.php?post={{ data.id }}&action=edit">Edit more details</a>
				<# } #>
				<# if ( ! data.uploading && data.can.remove ) { #> |
											<button type="button" class="button-link delete-attachment">Delete Permanently</button>
									<# } #>
			</div>

		</div>
	</script>

	<script type="text/html" id="tmpl-attachment">
		<div class="attachment-preview js--select-attachment type-{{ data.type }} subtype-{{ data.subtype }} {{ data.orientation }}">
			<div class="thumbnail">
				<# if ( data.uploading ) { #>
					<div class="media-progress-bar"><div style="width: {{ data.percent }}%"></div></div>
				<# } else if ( 'image' === data.type && data.sizes ) { #>
					<div class="centered">
						<img src="{{ data.size.url }}" draggable="false" alt="" />
					</div>
				<# } else { #>
					<div class="centered">
						<# if ( data.image && data.image.src && data.image.src !== data.icon ) { #>
							<img src="{{ data.image.src }}" class="thumbnail" draggable="false" alt="" />
						<# } else { #>
							<img src="{{ data.icon }}" class="icon" draggable="false" alt="" />
						<# } #>
					</div>
					<div class="filename">
						<div>{{ data.filename }}</div>
					</div>
				<# } #>
			</div>
			<# if ( data.buttons.close ) { #>
				<button type="button" class="button-link attachment-close media-modal-icon"><span class="screen-reader-text">Remove</span></button>
			<# } #>
		</div>
		<# if ( data.buttons.check ) { #>
			<button type="button" class="button-link check" tabindex="-1"><span class="media-modal-icon"></span><span class="screen-reader-text">Deselect</span></button>
		<# } #>
		<#
		var maybeReadOnly = data.can.save || data.allowLocalEdits ? '' : 'readonly';
		if ( data.describe ) {
			if ( 'image' === data.type ) { #>
				<input type="text" value="{{ data.caption }}" class="describe" data-setting="caption"
					placeholder="Caption this image&hellip;" {{ maybeReadOnly }} />
			<# } else { #>
				<input type="text" value="{{ data.title }}" class="describe" data-setting="title"
					<# if ( 'video' === data.type ) { #>
						placeholder="Describe this video&hellip;"
					<# } else if ( 'audio' === data.type ) { #>
						placeholder="Describe this audio file&hellip;"
					<# } else { #>
						placeholder="Describe this media file&hellip;"
					<# } #> {{ maybeReadOnly }} />
			<# }
		} #>
	</script>

	<script type="text/html" id="tmpl-attachment-details">
		<h2>
			Attachment Details			<span class="settings-save-status">
				<span class="spinner"></span>
				<span class="saved">Saved.</span>
			</span>
		</h2>
		<div class="attachment-info">
			<div class="thumbnail thumbnail-{{ data.type }}">
				<# if ( data.uploading ) { #>
					<div class="media-progress-bar"><div></div></div>
				<# } else if ( 'image' === data.type && data.sizes ) { #>
					<img src="{{ data.size.url }}" draggable="false" alt="" />
				<# } else { #>
					<img src="{{ data.icon }}" class="icon" draggable="false" alt="" />
				<# } #>
			</div>
			<div class="details">
				<div class="filename">{{ data.filename }}</div>
				<div class="uploaded">{{ data.dateFormatted }}</div>

				<div class="file-size">{{ data.filesizeHumanReadable }}</div>
				<# if ( 'image' === data.type && ! data.uploading ) { #>
					<# if ( data.width && data.height ) { #>
						<div class="dimensions">{{ data.width }} &times; {{ data.height }}</div>
					<# } #>

					<# if ( data.can.save && data.sizes ) { #>
						<a class="edit-attachment" href="{{ data.editLink }}&amp;image-editor" target="_blank">Edit Image</a>
					<# } #>
				<# } #>

				<# if ( data.fileLength ) { #>
					<div class="file-length">Length: {{ data.fileLength }}</div>
				<# } #>

				<# if ( ! data.uploading && data.can.remove ) { #>
											<button type="button" class="button-link delete-attachment">Delete Permanently</button>
									<# } #>

				<div class="compat-meta">
					<# if ( data.compat && data.compat.meta ) { #>
						{{{ data.compat.meta }}}
					<# } #>
				</div>
			</div>
		</div>

		<label class="setting" data-setting="url">
			<span class="name">URL</span>
			<input type="text" value="{{ data.url }}" readonly />
		</label>
		<# var maybeReadOnly = data.can.save || data.allowLocalEdits ? '' : 'readonly'; #>
				<label class="setting" data-setting="title">
			<span class="name">Title</span>
			<input type="text" value="{{ data.title }}" {{ maybeReadOnly }} />
		</label>
				<# if ( 'audio' === data.type ) { #>
				<label class="setting" data-setting="artist">
			<span class="name">Artist</span>
			<input type="text" value="{{ data.artist || data.meta.artist || '' }}" />
		</label>
				<label class="setting" data-setting="album">
			<span class="name">Album</span>
			<input type="text" value="{{ data.album || data.meta.album || '' }}" />
		</label>
				<# } #>
		<label class="setting" data-setting="caption">
			<span class="name">Caption</span>
			<textarea {{ maybeReadOnly }}>{{ data.caption }}</textarea>
		</label>
		<# if ( 'image' === data.type ) { #>
			<label class="setting" data-setting="alt">
				<span class="name">Alt Text</span>
				<input type="text" value="{{ data.alt }}" {{ maybeReadOnly }} />
			</label>
		<# } #>
		<label class="setting" data-setting="description">
			<span class="name">Description</span>
			<textarea {{ maybeReadOnly }}>{{ data.description }}</textarea>
		</label>
	</script>

	<script type="text/html" id="tmpl-media-selection">
		<div class="selection-info">
			<span class="count"></span>
			<# if ( data.editable ) { #>
				<button type="button" class="button-link edit-selection">Edit Selection</button>
			<# } #>
			<# if ( data.clearable ) { #>
				<button type="button" class="button-link clear-selection">Clear</button>
			<# } #>
		</div>
		<div class="selection-view"></div>
	</script>

	<script type="text/html" id="tmpl-attachment-display-settings">
		<h2>Attachment Display Settings</h2>

		<# if ( 'image' === data.type ) { #>
			<label class="setting">
				<span>Alignment</span>
				<select class="alignment"
					data-setting="align"
					<# if ( data.userSettings ) { #>
						data-user-setting="align"
					<# } #>>

					<option value="left">
						Left					</option>
					<option value="center">
						Center					</option>
					<option value="right">
						Right					</option>
					<option value="none" selected>
						None					</option>
				</select>
			</label>
		<# } #>

		<div class="setting">
			<label>
				<# if ( data.model.canEmbed ) { #>
					<span>Embed or Link</span>
				<# } else { #>
					<span>Link To</span>
				<# } #>

				<select class="link-to"
					data-setting="link"
					<# if ( data.userSettings && ! data.model.canEmbed ) { #>
						data-user-setting="urlbutton"
					<# } #>>

				<# if ( data.model.canEmbed ) { #>
					<option value="embed" selected>
						Embed Media Player					</option>
					<option value="file">
				<# } else { #>
					<option value="none" selected>
						None					</option>
					<option value="file">
				<# } #>
					<# if ( data.model.canEmbed ) { #>
						Link to Media File					<# } else { #>
						Media File					<# } #>
					</option>
					<option value="post">
					<# if ( data.model.canEmbed ) { #>
						Link to Attachment Page					<# } else { #>
						Attachment Page					<# } #>
					</option>
				<# if ( 'image' === data.type ) { #>
					<option value="custom">
						Custom URL					</option>
				<# } #>
				</select>
			</label>
			<input type="text" class="link-to-custom" data-setting="linkUrl" />
		</div>

		<# if ( 'undefined' !== typeof data.sizes ) { #>
			<label class="setting">
				<span>Size</span>
				<select class="size" name="size"
					data-setting="size"
					<# if ( data.userSettings ) { #>
						data-user-setting="imgsize"
					<# } #>>
											<#
						var size = data.sizes['thumbnail'];
						if ( size ) { #>
							<option value="thumbnail" >
								Thumbnail &ndash; {{ size.width }} &times; {{ size.height }}
							</option>
						<# } #>
											<#
						var size = data.sizes['medium'];
						if ( size ) { #>
							<option value="medium" >
								Medium &ndash; {{ size.width }} &times; {{ size.height }}
							</option>
						<# } #>
											<#
						var size = data.sizes['large'];
						if ( size ) { #>
							<option value="large" >
								Large &ndash; {{ size.width }} &times; {{ size.height }}
							</option>
						<# } #>
											<#
						var size = data.sizes['full'];
						if ( size ) { #>
							<option value="full"  selected='selected'>
								Full Size &ndash; {{ size.width }} &times; {{ size.height }}
							</option>
						<# } #>
									</select>
			</label>
		<# } #>
	</script>

	<script type="text/html" id="tmpl-gallery-settings">
		<h2>Gallery Settings</h2>

		<label class="setting">
			<span>Link To</span>
			<select class="link-to"
				data-setting="link"
				<# if ( data.userSettings ) { #>
					data-user-setting="urlbutton"
				<# } #>>

				<option value="post" <# if ( ! wp.media.galleryDefaults.link || 'post' == wp.media.galleryDefaults.link ) {
					#>selected="selected"<# }
				#>>
					Attachment Page				</option>
				<option value="file" <# if ( 'file' == wp.media.galleryDefaults.link ) { #>selected="selected"<# } #>>
					Media File				</option>
				<option value="none" <# if ( 'none' == wp.media.galleryDefaults.link ) { #>selected="selected"<# } #>>
					None				</option>
			</select>
		</label>

		<label class="setting">
			<span>Columns</span>
			<select class="columns" name="columns"
				data-setting="columns">
									<option value="1" <#
						if ( 1 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						1					</option>
									<option value="2" <#
						if ( 2 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						2					</option>
									<option value="3" <#
						if ( 3 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						3					</option>
									<option value="4" <#
						if ( 4 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						4					</option>
									<option value="5" <#
						if ( 5 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						5					</option>
									<option value="6" <#
						if ( 6 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						6					</option>
									<option value="7" <#
						if ( 7 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						7					</option>
									<option value="8" <#
						if ( 8 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						8					</option>
									<option value="9" <#
						if ( 9 == wp.media.galleryDefaults.columns ) { #>selected="selected"<# }
					#>>
						9					</option>
							</select>
		</label>

		<label class="setting">
			<span>Random Order</span>
			<input type="checkbox" data-setting="_orderbyRandom" />
		</label>

		<label class="setting size">
			<span>Size</span>
			<select class="size" name="size"
				data-setting="size"
				<# if ( data.userSettings ) { #>
					data-user-setting="imgsize"
				<# } #>
				>
									<option value="thumbnail">
						Thumbnail					</option>
									<option value="medium">
						Medium					</option>
									<option value="large">
						Large					</option>
									<option value="full">
						Full Size					</option>
							</select>
		</label>
	</script>

	<script type="text/html" id="tmpl-playlist-settings">
		<h2>Playlist Settings</h2>

		<# var emptyModel = _.isEmpty( data.model ),
			isVideo = 'video' === data.controller.get('library').props.get('type'); #>

		<label class="setting">
			<input type="checkbox" data-setting="tracklist" <# if ( emptyModel ) { #>
				checked="checked"
			<# } #> />
			<# if ( isVideo ) { #>
			<span>Show Video List</span>
			<# } else { #>
			<span>Show Tracklist</span>
			<# } #>
		</label>

		<# if ( ! isVideo ) { #>
		<label class="setting">
			<input type="checkbox" data-setting="artists" <# if ( emptyModel ) { #>
				checked="checked"
			<# } #> />
			<span>Show Artist Name in Tracklist</span>
		</label>
		<# } #>

		<label class="setting">
			<input type="checkbox" data-setting="images" <# if ( emptyModel ) { #>
				checked="checked"
			<# } #> />
			<span>Show Images</span>
		</label>
	</script>

	<script type="text/html" id="tmpl-embed-link-settings">
		<label class="setting link-text">
			<span>Link Text</span>
			<input type="text" class="alignment" data-setting="linkText" />
		</label>
		<div class="embed-container" style="display: none;">
			<div class="embed-preview"></div>
		</div>
	</script>

	<script type="text/html" id="tmpl-embed-image-settings">
		<div class="thumbnail">
			<img src="{{ data.model.url }}" draggable="false" alt="" />
		</div>

					<label class="setting caption">
				<span>Caption</span>
				<textarea data-setting="caption" />
			</label>
		
		<label class="setting alt-text">
			<span>Alt Text</span>
			<input type="text" data-setting="alt" />
		</label>

		<div class="setting align">
			<span>Align</span>
			<div class="button-group button-large" data-setting="align">
				<button class="button" value="left">
					Left				</button>
				<button class="button" value="center">
					Center				</button>
				<button class="button" value="right">
					Right				</button>
				<button class="button active" value="none">
					None				</button>
			</div>
		</div>

		<div class="setting link-to">
			<span>Link To</span>
			<div class="button-group button-large" data-setting="link">
				<button class="button" value="file">
					Image URL				</button>
				<button class="button" value="custom">
					Custom URL				</button>
				<button class="button active" value="none">
					None				</button>
			</div>
			<input type="text" class="link-to-custom" data-setting="linkUrl" />
		</div>
	</script>

	<script type="text/html" id="tmpl-image-details">
		<div class="media-embed">
			<div class="embed-media-settings">
				<div class="column-image">
					<div class="image">
						<img src="{{ data.model.url }}" draggable="false" alt="" />

						<# if ( data.attachment && window.imageEdit ) { #>
							<div class="actions">
								<input type="button" class="edit-attachment button" value="Edit Original" />
								<input type="button" class="replace-attachment button" value="Replace" />
							</div>
						<# } #>
					</div>
				</div>
				<div class="column-settings">
											<label class="setting caption">
							<span>Caption</span>
							<textarea data-setting="caption">{{ data.model.caption }}</textarea>
						</label>
					
					<label class="setting alt-text">
						<span>Alternative Text</span>
						<input type="text" data-setting="alt" value="{{ data.model.alt }}" />
					</label>

					<h2>Display Settings</h2>
					<div class="setting align">
						<span>Align</span>
						<div class="button-group button-large" data-setting="align">
							<button class="button" value="left">
								Left							</button>
							<button class="button" value="center">
								Center							</button>
							<button class="button" value="right">
								Right							</button>
							<button class="button active" value="none">
								None							</button>
						</div>
					</div>

					<# if ( data.attachment ) { #>
						<# if ( 'undefined' !== typeof data.attachment.sizes ) { #>
							<label class="setting size">
								<span>Size</span>
								<select class="size" name="size"
									data-setting="size"
									<# if ( data.userSettings ) { #>
										data-user-setting="imgsize"
									<# } #>>
																			<#
										var size = data.sizes['thumbnail'];
										if ( size ) { #>
											<option value="thumbnail">
												Thumbnail &ndash; {{ size.width }} &times; {{ size.height }}
											</option>
										<# } #>
																			<#
										var size = data.sizes['medium'];
										if ( size ) { #>
											<option value="medium">
												Medium &ndash; {{ size.width }} &times; {{ size.height }}
											</option>
										<# } #>
																			<#
										var size = data.sizes['large'];
										if ( size ) { #>
											<option value="large">
												Large &ndash; {{ size.width }} &times; {{ size.height }}
											</option>
										<# } #>
																			<#
										var size = data.sizes['full'];
										if ( size ) { #>
											<option value="full">
												Full Size &ndash; {{ size.width }} &times; {{ size.height }}
											</option>
										<# } #>
																		<option value="custom">
										Custom Size									</option>
								</select>
							</label>
						<# } #>
							<div class="custom-size<# if ( data.model.size !== 'custom' ) { #> hidden<# } #>">
								<label><span>Width <small>(px)</small></span> <input data-setting="customWidth" type="number" step="1" value="{{ data.model.customWidth }}" /></label><span class="sep">&times;</span><label><span>Height <small>(px)</small></span><input data-setting="customHeight" type="number" step="1" value="{{ data.model.customHeight }}" /></label>
							</div>
					<# } #>

					<div class="setting link-to">
						<span>Link To</span>
						<select data-setting="link">
						<# if ( data.attachment ) { #>
							<option value="file">
								Media File							</option>
							<option value="post">
								Attachment Page							</option>
						<# } else { #>
							<option value="file">
								Image URL							</option>
						<# } #>
							<option value="custom">
								Custom URL							</option>
							<option value="none">
								None							</option>
						</select>
						<input type="text" class="link-to-custom" data-setting="linkUrl" />
					</div>
					<div class="advanced-section">
						<h2><button type="button" class="button-link advanced-toggle">Advanced Options</button></h2>
						<div class="advanced-settings hidden">
							<div class="advanced-image">
								<label class="setting title-text">
									<span>Image Title Attribute</span>
									<input type="text" data-setting="title" value="{{ data.model.title }}" />
								</label>
								<label class="setting extra-classes">
									<span>Image CSS Class</span>
									<input type="text" data-setting="extraClasses" value="{{ data.model.extraClasses }}" />
								</label>
							</div>
							<div class="advanced-link">
								<div class="setting link-target">
									<label><input type="checkbox" data-setting="linkTargetBlank" value="_blank" <# if ( data.model.linkTargetBlank ) { #>checked="checked"<# } #>>Open link in a new tab</label>
								</div>
								<label class="setting link-rel">
									<span>Link Rel</span>
									<input type="text" data-setting="linkRel" value="{{ data.model.linkClassName }}" />
								</label>
								<label class="setting link-class-name">
									<span>Link CSS Class</span>
									<input type="text" data-setting="linkClassName" value="{{ data.model.linkClassName }}" />
								</label>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</script>

	<script type="text/html" id="tmpl-image-editor">
		<div id="media-head-{{ data.id }}"></div>
		<div id="image-editor-{{ data.id }}"></div>
	</script>

	<script type="text/html" id="tmpl-audio-details">
		<# var ext, html5types = {
			mp3: wp.media.view.settings.embedMimes.mp3,
			ogg: wp.media.view.settings.embedMimes.ogg
		}; #>

				<div class="media-embed media-embed-details">
			<div class="embed-media-settings embed-audio-settings">
				<audio style="visibility: hidden"
	controls
	class="wp-audio-shortcode"
	width="{{ _.isUndefined( data.model.width ) ? 400 : data.model.width }}"
	preload="{{ _.isUndefined( data.model.preload ) ? 'none' : data.model.preload }}"
	<#
	if ( ! _.isUndefined( data.model.autoplay ) && data.model.autoplay ) {
		#> autoplay<#
	}
	if ( ! _.isUndefined( data.model.loop ) && data.model.loop ) {
		#> loop<#
	}
	#>
>
	<# if ( ! _.isEmpty( data.model.src ) ) { #>
	<source src="{{ data.model.src }}" type="{{ wp.media.view.settings.embedMimes[ data.model.src.split('.').pop() ] }}" />
	<# } #>

	<# if ( ! _.isEmpty( data.model.mp3 ) ) { #>
	<source src="{{ data.model.mp3 }}" type="{{ wp.media.view.settings.embedMimes[ 'mp3' ] }}" />
	<# } #>
	<# if ( ! _.isEmpty( data.model.ogg ) ) { #>
	<source src="{{ data.model.ogg }}" type="{{ wp.media.view.settings.embedMimes[ 'ogg' ] }}" />
	<# } #>
	<# if ( ! _.isEmpty( data.model.wma ) ) { #>
	<source src="{{ data.model.wma }}" type="{{ wp.media.view.settings.embedMimes[ 'wma' ] }}" />
	<# } #>
	<# if ( ! _.isEmpty( data.model.m4a ) ) { #>
	<source src="{{ data.model.m4a }}" type="{{ wp.media.view.settings.embedMimes[ 'm4a' ] }}" />
	<# } #>
	<# if ( ! _.isEmpty( data.model.wav ) ) { #>
	<source src="{{ data.model.wav }}" type="{{ wp.media.view.settings.embedMimes[ 'wav' ] }}" />
	<# } #>
	</audio>

				<# if ( ! _.isEmpty( data.model.src ) ) {
					ext = data.model.src.split('.').pop();
					if ( html5types[ ext ] ) {
						delete html5types[ ext ];
					}
				#>
				<label class="setting">
					<span>SRC</span>
					<input type="text" disabled="disabled" data-setting="src" value="{{ data.model.src }}" />
					<button type="button" class="button-link remove-setting">Remove audio source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.mp3 ) ) {
					if ( ! _.isUndefined( html5types.mp3 ) ) {
						delete html5types.mp3;
					}
				#>
				<label class="setting">
					<span>MP3</span>
					<input type="text" disabled="disabled" data-setting="mp3" value="{{ data.model.mp3 }}" />
					<button type="button" class="button-link remove-setting">Remove audio source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.ogg ) ) {
					if ( ! _.isUndefined( html5types.ogg ) ) {
						delete html5types.ogg;
					}
				#>
				<label class="setting">
					<span>OGG</span>
					<input type="text" disabled="disabled" data-setting="ogg" value="{{ data.model.ogg }}" />
					<button type="button" class="button-link remove-setting">Remove audio source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.wma ) ) {
					if ( ! _.isUndefined( html5types.wma ) ) {
						delete html5types.wma;
					}
				#>
				<label class="setting">
					<span>WMA</span>
					<input type="text" disabled="disabled" data-setting="wma" value="{{ data.model.wma }}" />
					<button type="button" class="button-link remove-setting">Remove audio source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.m4a ) ) {
					if ( ! _.isUndefined( html5types.m4a ) ) {
						delete html5types.m4a;
					}
				#>
				<label class="setting">
					<span>M4A</span>
					<input type="text" disabled="disabled" data-setting="m4a" value="{{ data.model.m4a }}" />
					<button type="button" class="button-link remove-setting">Remove audio source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.wav ) ) {
					if ( ! _.isUndefined( html5types.wav ) ) {
						delete html5types.wav;
					}
				#>
				<label class="setting">
					<span>WAV</span>
					<input type="text" disabled="disabled" data-setting="wav" value="{{ data.model.wav }}" />
					<button type="button" class="button-link remove-setting">Remove audio source</button>
				</label>
				<# } #>
				
				<# if ( ! _.isEmpty( html5types ) ) { #>
				<div class="setting">
					<span>Add alternate sources for maximum HTML5 playback:</span>
					<div class="button-large">
					<# _.each( html5types, function (mime, type) { #>
					<button class="button add-media-source" data-mime="{{ mime }}">{{ type }}</button>
					<# } ) #>
					</div>
				</div>
				<# } #>

				<div class="setting preload">
					<span>Preload</span>
					<div class="button-group button-large" data-setting="preload">
						<button class="button" value="auto">Auto</button>
						<button class="button" value="metadata">Metadata</button>
						<button class="button active" value="none">None</button>
					</div>
				</div>

				<label class="setting checkbox-setting">
					<input type="checkbox" data-setting="autoplay" />
					<span>Autoplay</span>
				</label>

				<label class="setting checkbox-setting">
					<input type="checkbox" data-setting="loop" />
					<span>Loop</span>
				</label>
			</div>
		</div>
	</script>

	<script type="text/html" id="tmpl-video-details">
		<# var ext, html5types = {
			mp4: wp.media.view.settings.embedMimes.mp4,
			ogv: wp.media.view.settings.embedMimes.ogv,
			webm: wp.media.view.settings.embedMimes.webm
		}; #>

				<div class="media-embed media-embed-details">
			<div class="embed-media-settings embed-video-settings">
				<div class="wp-video-holder">
				<#
				var w = ! data.model.width || data.model.width > 640 ? 640 : data.model.width,
					h = ! data.model.height ? 360 : data.model.height;

				if ( data.model.width && w !== data.model.width ) {
					h = Math.ceil( ( h * w ) / data.model.width );
				}
				#>

				<#  var w_rule = '', classes = [],
		w, h, settings = wp.media.view.settings,
		isYouTube = isVimeo = false;

	if ( ! _.isEmpty( data.model.src ) ) {
		isYouTube = data.model.src.match(/youtube|youtu\.be/);
		isVimeo = -1 !== data.model.src.indexOf('vimeo');
	}

	if ( settings.contentWidth && data.model.width >= settings.contentWidth ) {
		w = settings.contentWidth;
	} else {
		w = data.model.width;
	}

	if ( w !== data.model.width ) {
		h = Math.ceil( ( data.model.height * w ) / data.model.width );
	} else {
		h = data.model.height;
 	}

	if ( w ) {
		w_rule = 'width: ' + w + 'px; ';
	}

	if ( isYouTube ) {
		classes.push( 'youtube-video' );
	}

	if ( isVimeo ) {
		classes.push( 'vimeo-video' );
	}

#>
<div style="{{ w_rule }}" class="wp-video">
<video controls
	class="wp-video-shortcode {{ classes.join( ' ' ) }}"
	<# if ( w ) { #>width="{{ w }}"<# } #>
	<# if ( h ) { #>height="{{ h }}"<# } #>
	<#
		if ( ! _.isUndefined( data.model.poster ) && data.model.poster ) {
			#> poster="{{ data.model.poster }}"<#
		} #>
		preload="{{ _.isUndefined( data.model.preload ) ? 'metadata' : data.model.preload }}"<#
	 if ( ! _.isUndefined( data.model.autoplay ) && data.model.autoplay ) {
		#> autoplay<#
	}
	 if ( ! _.isUndefined( data.model.loop ) && data.model.loop ) {
		#> loop<#
	}
	#>
>
	<# if ( ! _.isEmpty( data.model.src ) ) {
		if ( isYouTube ) { #>
		<source src="{{ data.model.src }}" type="video/youtube" />
		<# } else if ( isVimeo ) { #>
		<source src="{{ data.model.src }}" type="video/vimeo" />
		<# } else { #>
		<source src="{{ data.model.src }}" type="{{ settings.embedMimes[ data.model.src.split('.').pop() ] }}" />
		<# }
	} #>

	<# if ( data.model.mp4 ) { #>
	<source src="{{ data.model.mp4 }}" type="{{ settings.embedMimes[ 'mp4' ] }}" />
	<# } #>
	<# if ( data.model.m4v ) { #>
	<source src="{{ data.model.m4v }}" type="{{ settings.embedMimes[ 'm4v' ] }}" />
	<# } #>
	<# if ( data.model.webm ) { #>
	<source src="{{ data.model.webm }}" type="{{ settings.embedMimes[ 'webm' ] }}" />
	<# } #>
	<# if ( data.model.ogv ) { #>
	<source src="{{ data.model.ogv }}" type="{{ settings.embedMimes[ 'ogv' ] }}" />
	<# } #>
	<# if ( data.model.wmv ) { #>
	<source src="{{ data.model.wmv }}" type="{{ settings.embedMimes[ 'wmv' ] }}" />
	<# } #>
	<# if ( data.model.flv ) { #>
	<source src="{{ data.model.flv }}" type="{{ settings.embedMimes[ 'flv' ] }}" />
	<# } #>
		{{{ data.model.content }}}
</video>
</div>

				<# if ( ! _.isEmpty( data.model.src ) ) {
					ext = data.model.src.split('.').pop();
					if ( html5types[ ext ] ) {
						delete html5types[ ext ];
					}
				#>
				<label class="setting">
					<span>SRC</span>
					<input type="text" disabled="disabled" data-setting="src" value="{{ data.model.src }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.mp4 ) ) {
					if ( ! _.isUndefined( html5types.mp4 ) ) {
						delete html5types.mp4;
					}
				#>
				<label class="setting">
					<span>MP4</span>
					<input type="text" disabled="disabled" data-setting="mp4" value="{{ data.model.mp4 }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.m4v ) ) {
					if ( ! _.isUndefined( html5types.m4v ) ) {
						delete html5types.m4v;
					}
				#>
				<label class="setting">
					<span>M4V</span>
					<input type="text" disabled="disabled" data-setting="m4v" value="{{ data.model.m4v }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.webm ) ) {
					if ( ! _.isUndefined( html5types.webm ) ) {
						delete html5types.webm;
					}
				#>
				<label class="setting">
					<span>WEBM</span>
					<input type="text" disabled="disabled" data-setting="webm" value="{{ data.model.webm }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.ogv ) ) {
					if ( ! _.isUndefined( html5types.ogv ) ) {
						delete html5types.ogv;
					}
				#>
				<label class="setting">
					<span>OGV</span>
					<input type="text" disabled="disabled" data-setting="ogv" value="{{ data.model.ogv }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.wmv ) ) {
					if ( ! _.isUndefined( html5types.wmv ) ) {
						delete html5types.wmv;
					}
				#>
				<label class="setting">
					<span>WMV</span>
					<input type="text" disabled="disabled" data-setting="wmv" value="{{ data.model.wmv }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
				<# if ( ! _.isEmpty( data.model.flv ) ) {
					if ( ! _.isUndefined( html5types.flv ) ) {
						delete html5types.flv;
					}
				#>
				<label class="setting">
					<span>FLV</span>
					<input type="text" disabled="disabled" data-setting="flv" value="{{ data.model.flv }}" />
					<button type="button" class="button-link remove-setting">Remove video source</button>
				</label>
				<# } #>
								</div>

				<# if ( ! _.isEmpty( html5types ) ) { #>
				<div class="setting">
					<span>Add alternate sources for maximum HTML5 playback:</span>
					<div class="button-large">
					<# _.each( html5types, function (mime, type) { #>
					<button class="button add-media-source" data-mime="{{ mime }}">{{ type }}</button>
					<# } ) #>
					</div>
				</div>
				<# } #>

				<# if ( ! _.isEmpty( data.model.poster ) ) { #>
				<label class="setting">
					<span>Poster Image</span>
					<input type="text" disabled="disabled" data-setting="poster" value="{{ data.model.poster }}" />
					<button type="button" class="button-link remove-setting">Remove poster image</button>
				</label>
				<# } #>
				<div class="setting preload">
					<span>Preload</span>
					<div class="button-group button-large" data-setting="preload">
						<button class="button" value="auto">Auto</button>
						<button class="button" value="metadata">Metadata</button>
						<button class="button active" value="none">None</button>
					</div>
				</div>

				<label class="setting checkbox-setting">
					<input type="checkbox" data-setting="autoplay" />
					<span>Autoplay</span>
				</label>

				<label class="setting checkbox-setting">
					<input type="checkbox" data-setting="loop" />
					<span>Loop</span>
				</label>

				<label class="setting" data-setting="content">
					<span>Tracks (subtitles, captions, descriptions, chapters, or metadata)</span>
					<#
					var content = '';
					if ( ! _.isEmpty( data.model.content ) ) {
						var tracks = jQuery( data.model.content ).filter( 'track' );
						_.each( tracks.toArray(), function (track) {
							content += track.outerHTML; #>
						<p>
							<input class="content-track" type="text" value="{{ track.outerHTML }}" />
							<button type="button" class="button-link remove-setting remove-track">Remove video track</button>
						</p>
						<# } ); #>
					<# } else { #>
					<em>There are no associated subtitles.</em>
					<# } #>
					<textarea class="hidden content-setting">{{ content }}</textarea>
				</label>
			</div>
		</div>
	</script>

	<script type="text/html" id="tmpl-editor-gallery">
		<# if ( data.attachments.length ) { #>
			<div class="gallery gallery-columns-{{ data.columns }}">
				<# _.each( data.attachments, function( attachment, index ) { #>
					<dl class="gallery-item">
						<dt class="gallery-icon">
							<# if ( attachment.thumbnail ) { #>
								<img src="{{ attachment.thumbnail.url }}" width="{{ attachment.thumbnail.width }}" height="{{ attachment.thumbnail.height }}" alt="" />
							<# } else { #>
								<img src="{{ attachment.url }}" alt="" />
							<# } #>
						</dt>
						<# if ( attachment.caption ) { #>
							<dd class="wp-caption-text gallery-caption">
								{{{ data.verifyHTML( attachment.caption ) }}}
							</dd>
						<# } #>
					</dl>
					<# if ( index % data.columns === data.columns - 1 ) { #>
						<br style="clear: both;">
					<# } #>
				<# } ); #>
			</div>
		<# } else { #>
			<div class="wpview-error">
				<div class="dashicons dashicons-format-gallery"></div><p>No items found.</p>
			</div>
		<# } #>
	</script>

	<script type="text/html" id="tmpl-crop-content">
		<img class="crop-image" src="{{ data.url }}" alt="Image crop area preview. Requires mouse interaction.">
		<div class="upload-errors"></div>
	</script>

	<script type="text/html" id="tmpl-site-icon-preview">
		<h2>Preview</h2>
		<strong aria-hidden="true">As a browser icon</strong>
		<div class="favicon-preview">
			<img src="https://www.thitsarparamisociety.com/wp-admin/images/browser.png" class="browser-preview" width="182" height="" alt="" />

			<div class="favicon">
				<img id="preview-favicon" src="{{ data.url }}" alt="Preview as a browser icon"/>
			</div>
			<span class="browser-title" aria-hidden="true">Thitsarparami Buddhist Society | Dhamma mp3 Download</span>
		</div>

		<strong aria-hidden="true">As an app icon</strong>
		<div class="app-icon-preview">
			<img id="preview-app-icon" src="{{ data.url }}" alt="Preview as an app icon"/>
		</div>
	</script>

	<link rel="stylesheet" id="wpad_style_front-css" href="https://www.thitsarparamisociety.com/wp-content/plugins/wp-advance-comment/css/frontend-style.css?ver=4.6.12" type="text/css" media="all">
<link rel="stylesheet" id="wpad-ui-jquery-css" href="https://www.thitsarparamisociety.com/wp-content/plugins/wp-advance-comment/css/jquery-ui.css?ver=1.0.0" type="text/css" media="">
<link rel="stylesheet" id="wpad-ui-css" href="https://www.thitsarparamisociety.com/wp-content/plugins/wp-advance-comment/css/jquery-dialog.css?ver=1.0.0" type="text/css" media="">
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/file-manager/js/front-script.js?ver=1.0.0"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/underscore.min.js?ver=1.8.3"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/shortcode.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/backbone.min.js?ver=1.2.3"></script>
<script type="text/javascript">
/* <![CDATA[ */
var _wpUtilSettings = {"ajax":{"url":"\/wp-admin\/admin-ajax.php"}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/wp-util.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/wp-backbone.min.js?ver=4.6.12"></script>
<script type="text/javascript">
/* <![CDATA[ */
var _wpMediaModelsL10n = {"settings":{"ajaxurl":"\/wp-admin\/admin-ajax.php","post":{"id":0}}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/media-models.min.js?ver=4.6.12"></script>
<script type="text/javascript">
/* <![CDATA[ */
var pluploadL10n = {"queue_limit_exceeded":"You have attempted to queue too many files.","file_exceeds_size_limit":"%s exceeds the maximum upload size for this site.","zero_byte_file":"This file is empty. Please try another.","invalid_filetype":"This file type is not allowed. Please try another.","not_an_image":"This file is not an image. Please try another.","image_memory_exceeded":"Memory exceeded. Please try another smaller file.","image_dimensions_exceeded":"This is larger than the maximum size. Please try another.","default_error":"An error occurred in the upload. Please try again later.","missing_upload_url":"There was a configuration error. Please contact the server administrator.","upload_limit_exceeded":"You may only upload 1 file.","http_error":"HTTP error.","upload_failed":"Upload failed.","big_upload_failed":"Please try uploading this file with the %1$sbrowser uploader%2$s.","big_upload_queued":"%s exceeds the maximum upload size for the multi-file uploader when used in your browser.","io_error":"IO error.","security_error":"Security error.","file_cancelled":"File canceled.","upload_stopped":"Upload stopped.","dismiss":"Dismiss","crunching":"Crunching\u2026","deleted":"moved to the trash.","error_uploading":"\u201c%s\u201d has failed to upload."};
var _wpPluploadSettings = {"defaults":{"runtimes":"html5,flash,silverlight,html4","file_data_name":"async-upload","url":"\/wp-admin\/async-upload.php","flash_swf_url":"https:\/\/www.thitsarparamisociety.com\/wp-includes\/js\/plupload\/plupload.flash.swf","silverlight_xap_url":"https:\/\/www.thitsarparamisociety.com\/wp-includes\/js\/plupload\/plupload.silverlight.xap","filters":{"max_file_size":"67108864b","mime_types":[{"extensions":"jpg,jpeg,jpe,gif,png,bmp,tiff,tif,ico,asf,asx,wmv,wmx,wm,avi,divx,flv,mov,qt,mpeg,mpg,mpe,mp4,m4v,ogv,webm,mkv,3gp,3gpp,3g2,3gp2,txt,asc,c,cc,h,srt,csv,tsv,ics,rtx,css,vtt,dfxp,mp3,m4a,m4b,ra,ram,wav,ogg,oga,mid,midi,wma,wax,mka,rtf,pdf,class,tar,zip,gz,gzip,rar,7z,psd,xcf,doc,pot,pps,ppt,wri,xla,xls,xlt,xlw,mdb,mpp,docx,docm,dotx,dotm,xlsx,xlsm,xlsb,xltx,xltm,xlam,pptx,pptm,ppsx,ppsm,potx,potm,ppam,sldx,sldm,onetoc,onetoc2,onetmp,onepkg,oxps,xps,odt,odp,ods,odg,odc,odb,odf,wp,wpd,key,numbers,pages"}]},"multipart_params":{"action":"upload-attachment","_wpnonce":"fdc038cd58"}},"browser":{"mobile":false,"supported":true},"limitExceeded":false};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/plupload/wp-plupload.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/jquery/ui/core.min.js?ver=1.11.4"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/jquery/ui/widget.min.js?ver=1.11.4"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/jquery/ui/mouse.min.js?ver=1.11.4"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/jquery/ui/sortable.min.js?ver=1.11.4"></script>
<script type="text/javascript">
/* <![CDATA[ */
var mejsL10n = {"language":"en-US","strings":{"Close":"Close","Fullscreen":"Fullscreen","Turn off Fullscreen":"Turn off Fullscreen","Go Fullscreen":"Go Fullscreen","Download File":"Download File","Download Video":"Download Video","Play":"Play","Pause":"Pause","Captions\/Subtitles":"Captions\/Subtitles","None":"None","Time Slider":"Time Slider","Skip back %1 seconds":"Skip back %1 seconds","Video Player":"Video Player","Audio Player":"Audio Player","Volume Slider":"Volume Slider","Mute Toggle":"Mute Toggle","Unmute":"Unmute","Mute":"Mute","Use Up\/Down Arrow keys to increase or decrease volume.":"Use Up\/Down Arrow keys to increase or decrease volume.","Use Left\/Right Arrow keys to advance one second, Up\/Down arrows to advance ten seconds.":"Use Left\/Right Arrow keys to advance one second, Up\/Down arrows to advance ten seconds."}};
var _wpmejsSettings = {"pluginPath":"\/wp-includes\/js\/mediaelement\/"};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/mediaelement/mediaelement-and-player.min.js?ver=2.22.0"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/mediaelement/wp-mediaelement.min.js?ver=4.6.12"></script>
<script type="text/javascript">
/* <![CDATA[ */
var _wpMediaViewsL10n = {"url":"URL","addMedia":"Add Media","search":"Search","select":"Select","cancel":"Cancel","update":"Update","replace":"Replace","remove":"Remove","back":"Back","selected":"%d selected","dragInfo":"Drag and drop to reorder media files.","uploadFilesTitle":"Upload Files","uploadImagesTitle":"Upload Images","mediaLibraryTitle":"Media Library","insertMediaTitle":"Insert Media","createNewGallery":"Create a new gallery","createNewPlaylist":"Create a new playlist","createNewVideoPlaylist":"Create a new video playlist","returnToLibrary":"\u2190 Return to library","allMediaItems":"All media items","allDates":"All dates","noItemsFound":"No items found.","insertIntoPost":"Insert into post","unattached":"Unattached","trash":"Trash","uploadedToThisPost":"Uploaded to this post","warnDelete":"You are about to permanently delete this item.\n  'Cancel' to stop, 'OK' to delete.","warnBulkDelete":"You are about to permanently delete these items.\n  'Cancel' to stop, 'OK' to delete.","warnBulkTrash":"You are about to trash these items.\n  'Cancel' to stop, 'OK' to delete.","bulkSelect":"Bulk Select","cancelSelection":"Cancel Selection","trashSelected":"Trash Selected","untrashSelected":"Untrash Selected","deleteSelected":"Delete Selected","deletePermanently":"Delete Permanently","apply":"Apply","filterByDate":"Filter by date","filterByType":"Filter by type","searchMediaLabel":"Search Media","noMedia":"No media files found.","attachmentDetails":"Attachment Details","insertFromUrlTitle":"Insert from URL","setFeaturedImageTitle":"Featured Image","setFeaturedImage":"Set featured image","createGalleryTitle":"Create Gallery","editGalleryTitle":"Edit Gallery","cancelGalleryTitle":"\u2190 Cancel Gallery","insertGallery":"Insert gallery","updateGallery":"Update gallery","addToGallery":"Add to gallery","addToGalleryTitle":"Add to Gallery","reverseOrder":"Reverse order","imageDetailsTitle":"Image Details","imageReplaceTitle":"Replace Image","imageDetailsCancel":"Cancel Edit","editImage":"Edit Image","chooseImage":"Choose Image","selectAndCrop":"Select and Crop","skipCropping":"Skip Cropping","cropImage":"Crop Image","cropYourImage":"Crop your image","cropping":"Cropping\u2026","suggestedDimensions":"Suggested image dimensions:","cropError":"There has been an error cropping your image.","audioDetailsTitle":"Audio Details","audioReplaceTitle":"Replace Audio","audioAddSourceTitle":"Add Audio Source","audioDetailsCancel":"Cancel Edit","videoDetailsTitle":"Video Details","videoReplaceTitle":"Replace Video","videoAddSourceTitle":"Add Video Source","videoDetailsCancel":"Cancel Edit","videoSelectPosterImageTitle":"Select Poster Image","videoAddTrackTitle":"Add Subtitles","playlistDragInfo":"Drag and drop to reorder tracks.","createPlaylistTitle":"Create Audio Playlist","editPlaylistTitle":"Edit Audio Playlist","cancelPlaylistTitle":"\u2190 Cancel Audio Playlist","insertPlaylist":"Insert audio playlist","updatePlaylist":"Update audio playlist","addToPlaylist":"Add to audio playlist","addToPlaylistTitle":"Add to Audio Playlist","videoPlaylistDragInfo":"Drag and drop to reorder videos.","createVideoPlaylistTitle":"Create Video Playlist","editVideoPlaylistTitle":"Edit Video Playlist","cancelVideoPlaylistTitle":"\u2190 Cancel Video Playlist","insertVideoPlaylist":"Insert video playlist","updateVideoPlaylist":"Update video playlist","addToVideoPlaylist":"Add to video playlist","addToVideoPlaylistTitle":"Add to Video Playlist","settings":{"tabs":[],"tabUrl":"https:\/\/www.thitsarparamisociety.com\/wp-admin\/media-upload.php?chromeless=1","mimeTypes":{"image":"Images","audio":"Audio","video":"Video"},"captions":true,"nonce":{"sendToEditor":"4099a95c89"},"post":{"id":0},"defaultProps":{"link":"file","align":"","size":""},"attachmentCounts":{"audio":1,"video":1},"embedExts":["mp3","ogg","wma","m4a","wav","mp4","m4v","webm","ogv","wmv","flv"],"embedMimes":{"mp3":"audio\/mpeg","ogg":"audio\/ogg","wma":"audio\/x-ms-wma","m4a":"audio\/mpeg","wav":"audio\/wav","mp4":"video\/mp4","m4v":"video\/mp4","webm":"video\/webm","ogv":"video\/ogg","wmv":"video\/x-ms-wmv","flv":"video\/x-flv"},"contentWidth":1190,"months":[{"year":"2018","month":"11","text":"November 2018"},{"year":"2018","month":"10","text":"October 2018"},{"year":"2018","month":"9","text":"September 2018"},{"year":"2018","month":"8","text":"August 2018"},{"year":"2018","month":"7","text":"July 2018"},{"year":"2018","month":"6","text":"June 2018"},{"year":"2018","month":"5","text":"May 2018"},{"year":"2018","month":"4","text":"April 2018"},{"year":"2018","month":"3","text":"March 2018"},{"year":"2018","month":"2","text":"February 2018"},{"year":"2017","month":"12","text":"December 2017"},{"year":"2017","month":"10","text":"October 2017"},{"year":"2017","month":"7","text":"July 2017"},{"year":"2017","month":"6","text":"June 2017"},{"year":"2017","month":"3","text":"March 2017"},{"year":"2017","month":"2","text":"February 2017"},{"year":"2016","month":"10","text":"October 2016"},{"year":"2016","month":"9","text":"September 2016"},{"year":"2016","month":"8","text":"August 2016"},{"year":"2016","month":"7","text":"July 2016"},{"year":"2016","month":"6","text":"June 2016"},{"year":"2016","month":"4","text":"April 2016"},{"year":"2016","month":"3","text":"March 2016"},{"year":"2016","month":"2","text":"February 2016"},{"year":"2016","month":"1","text":"January 2016"},{"year":"2015","month":"12","text":"December 2015"},{"year":"2015","month":"11","text":"November 2015"},{"year":"2015","month":"10","text":"October 2015"},{"year":"2015","month":"9","text":"September 2015"},{"year":"2015","month":"8","text":"August 2015"},{"year":"2015","month":"7","text":"July 2015"},{"year":"2015","month":"6","text":"June 2015"},{"year":"2015","month":"5","text":"May 2015"},{"year":"2015","month":"4","text":"April 2015"},{"year":"2015","month":"3","text":"March 2015"},{"year":"2015","month":"2","text":"February 2015"},{"year":"2015","month":"1","text":"January 2015"},{"year":"2014","month":"12","text":"December 2014"},{"year":"2014","month":"11","text":"November 2014"},{"year":"2014","month":"10","text":"October 2014"},{"year":"2014","month":"9","text":"September 2014"},{"year":"2014","month":"8","text":"August 2014"},{"year":"2014","month":"7","text":"July 2014"},{"year":"2014","month":"6","text":"June 2014"},{"year":"2014","month":"5","text":"May 2014"},{"year":"2014","month":"4","text":"April 2014"},{"year":"2014","month":"3","text":"March 2014"},{"year":"2014","month":"2","text":"February 2014"}],"mediaTrash":0}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/media-views.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/media-editor.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/media-audiovideo.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/superfish.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/retina.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/bootstrap.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.flexslider-min.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/tweetable.jquery.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.timeago.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.prettyPhoto.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.carouFredSel-6.0.4-packed.js?ver=6.0.4"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.exposure.js?ver=1.0.1"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.form.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.validate.min.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/modernizr-transitions.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/jquery.masonry.min.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/set-view-count.js"></script>
<script type="text/javascript">
/* <![CDATA[ */
var kopa_custom_front_localization = {"validate":{"form":{"submit":"Submit","sending":"Sending..."},"name":{"required":"Please enter your name.","minlength":"At least {0} characters required."},"email":{"required":"Please enter your email.","email":"Please enter a valid email."},"url":{"required":"Please enter your url.","url":"Please enter a valid url."},"message":{"required":"Please enter a message.","minlength":"At least {0} characters required."}}};
/* ]]> */
</script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/themes/musica/js/custom.js"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/comment-reply.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-includes/js/wp-embed.min.js?ver=4.6.12"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/wp-advance-comment/js/jquery-ui.min.js?ver=1.0.0"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contus-video-gallery/js/playlist.min.js?ver=4.6.12"></script>
    



"""

soup = bs4(text, 'html.parser')


with open('titles_links.txt', 'w') as f:
    count = 1
    for key in soup.find_all('a'):
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), key.get_text()))
            #f.write('{}\n'.format(key.get_text()))
            count += 1
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