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
        
    <div id="page-720" class="elements-box post-720 page type-page status-publish has-post-thumbnail hentry">
        <h5><span style="color: #339966;">သီတဂူဆရာေတာ္ အရွင္ဉာဏိႆရ | ေဟာၾကားေတာ္မူေသာ တရားေတာ္မ်ား စုစည္းမႈ (MP3)</span></h5>
<h5 style="text-align: left;"><a href="https://www.thitsarparamisociety.com/thitagusayadawunanissa-biography/"><span style="color: #3366ff;">သီတဂူဆရာေတာ္ အရွင္ဥာဏိႆရ၏ ေထရုပၸတၱိအက်ဥ္း</span></a></h5>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">ဆရာေတာ္ဘုရားႀကီးပရိတ္တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/01/002%20U%20Nyanissara%20D1%20Payeitgyi-12.mp3"><span style="color: #ffcc00;">ပရိတ္ႀကီး (၁၁) သုတ္၊ ပါဠိအနက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/01/001%20U%20Nyanissara%20D1%20DhammaSatKyar.mp3"><span style="color: #ffcc00;">ဓမၼစႀကၤာ၊ အနတၲလကၡဏသုတ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/01/003%20U%20Nyanissara%20D1%20PaHtanParLiDaw-AhNaeKaZarTin.mp3"><span style="color: #ffcc00;">ပ႒ာန္းပါဠိေတာ္၊ အေနကဇာတင္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/maharthamaya-sitagu-sayardawgyi.mp3"><span style="color: #ffcc00;">မဟာသမယသုတ္ တရားေတာ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">(၂၀၁ဂ) ခုႏွစ္တရားေတာ္အသစ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/21.11.2018.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတုိ႔ရဲ႕တရား (၂၁.၁၁.၂၀၁၈ – ေတာင္ငူ ေရႊဆံေတာ္ဘုရား) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/18.11.2018_pm.mp3"><span style="color: #ffcc00;">သိၾကားမင္းေမးေသာေမးခြန္း(၁၄)ခ်က္ (၁၈.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/18.11.2018_am.mp3"><span style="color: #ffcc00;">ကထိန္အလွဴေတာ္အႏုေမာဒနာတရားေတာ္ (၁၈.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/17.11.2018.mp3"><span style="color: #ffcc00;">အရွာမမွားေစဖို႔ တရားေတာ္ (၁၇.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/16.11.2018.mp3"><span style="color: #ffcc00;">သိၾကားမင္းေမးေသာေမးခြန္း(၁၄)ခ်က္ (၁၆.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/15.11.2018.mp3"><span style="color: #ffcc00;">အပၸမာဒတရားေတာ္ (၁၅.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/14.11.2018.mp3"><span style="color: #ffcc00;">ေမာရသုတၱန္ – ေမာရိယမင္းဆက္အေၾကာင္းတရားေတာ္ (၁၄.၁၁.၂၀၁၈ မႏၲေလး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/12.11.2018.mp3"><span style="color: #ffcc00;">ကထိန္အလွဴအႏုေမာဒနာ (၁၂.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/09.11.2018.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒအႏုေမာဒနာတရားေတာ္ (၁၁.၁၁.၂၀၁၈ ထိုင္၀မ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/04.11.2018.mp3"><span style="color: #ffcc00;">ပရိေယသနသုတၱံတရားေတာ္ (၀၄.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/03.11.2018.mp3"><span style="color: #ffcc00;">ကထိိန္အႏုေမာဒနာတရားေတာ္ (၀၃.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/02.11.2018.mp3"><span style="color: #ffcc00;">အပၸမာဒတရားေတာ္ (၀၂.၁၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Nov/01.11.2018.mp3"><span style="color: #ffcc00;">ျဗဟၼဇာလသုတၱံတရားေတာ္ (၀၃.၀၁.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/18.10.2018-pm.mp3"><span style="color: #ffcc00;">မနာလိုျခင္း ၀န္တိုျခင္း – ဣသာ မစၧရိယ တရားေတာ္(သကၠပဉွ သုတၱံ) (၁၈.၁၀.၂၀၁၈ ရမည္းသင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/18.10.2018-am.mp3"><span style="color: #ffcc00;">ဖားေအာက္ဆရာေတာ္ဘုရားၾကီး သီလေပး ႏွင့္ သီတဂူဆရာေတာ္ဘုရားၾကီး အႏုေမာဒနာတရားေတာ္ (ဓမၼာႏုဓမၼပဋိပႏၷ ႏွစ္ထပ္သိမ္ေတာ္ႀကီး အလွဴေတာ္မဂၤလာ) (၁၈.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/17.10.2018.mp3"><span style="color: #ffcc00;">သကၠပဉွ သုတၱံတရားေတာ္ (အနီဃာသီလရွင္တိုက္၊ မႏၲေလး) (၁၇.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/16.10.2018.mp3"><span style="color: #ffcc00;">ေရႊက်င္နိကာယ၀ိနည္းစာျပန္ပြဲ ၾသ၀ါဒတရားေတာ္ (၁၆.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/13.10.2018.mp3"><span style="color: #ffcc00;">သကၠပဉွ သုတၱံတရားေတာ္ (၁၃.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/12.10.2018.mp3"><span style="color: #ffcc00;">အလွဴေအာင္ပြဲအထိမ္းအမွတ္ အႏုေမာဒနာ တရားေတာ္ (၁၂.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/09.10.2018.mp3"><span style="color: #ffcc00;">ျမတ္္စြာဘုရားကိုမေမ့တဲ့ ပုဂၢိဳလ္တို႔၏အက်ိဳးေက်းဇူး – အပၸာမဒ၏ဂုဏ္သတၱိ (၉.၁၀.၂၀၁၈ မိတၳီလာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/08.10.2018.mp3"><span style="color: #ffcc00;">အရိွတရားႏွင့္အမွန္တရား (၈.၁၀.၂၀၁၈ တပ္မေတာ္နည္းပညာတကၠသုိလ္ ျပင္ဦးလြင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/07.10.2018.mp3"><span style="color: #ffcc00;">အပၸမာဒတရားလက္ကိုင္ထားတယ္ဆိုရင္ ဘ၀တုိးတတ္မႈေကာင္းေကာင္းရတယ္ (၇.၁၀.၂၀၁၈ စစ္တကၠသိုလ္ ျပင္ဦးလြင္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Oct/05.10.2018.mp3"><span style="color: #ffcc00;">ဥပစာလာေထရီအေၾကာငး္တရားေတာ္ (၅.၁၀.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/30.9.2018.mp3"><span style="color: #ffcc00;">နာနာတိတၳိယသုတံၱ တရားေတာ္ (၃၀.၉၂၀၁၈ စစ္ကိုင္း ထူပါရံုေစတီေတာ္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/29.9.2018.mp3"><span style="color: #ffcc00;">Special Dhamma Talk in English for S. N. Goenka’s Death Anniversary (29.9.2018)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/24.9.2018.mp3"><span style="color: #ffcc00;">ဂရုဓမၼတရားေတာ္ (၂၄.၉.၂၀၁၈ ေတာ္လသင္းလျပည့္ေန႔ – ဂရုဓမၼအခါေတာ္ေန႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/22.9.2018.mp3"><span style="color: #ffcc00;">၀ိေ၀ကသုခ (၁၈.၉.၂၀၁၈ မံုရြာ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/18.9.2018.mp3"><span style="color: #ffcc00;">အစြန္းမေရာက္ေစနဲ႔တရားေတာ္ (ေသလာေထရီအေၾကာင္း) (၁၈.၉.၂၀၁၈ ကူမဲ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/17.9.2018.mp3"><span style="color: #ffcc00;">၀ဇီရာေထရီအေၾကာင္းတရားေတာ္ အပိုင္း(၄) (၁၇.၉.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/16.9.2018.mp3"><span style="color: #ffcc00;">အနဳေမာဒနာတရားေတာ္ (ေရႊဘိုမလြန္ဆန္လွဴသင္း) (၁၆.၉.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/15.9.2018.mp3"><span style="color: #ffcc00;">၀ဇီရာေထရီအေၾကာင္းတရားေတာ္ အပိုင္း(၃) (၁၅.၉.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/14.9.2018.mp3"><span style="color: #ffcc00;">က႐ုဏာတရားေတာ္ (ေသာတာပန္ ဆီ အလွဴေတာ္ အႏုေမာဒနာ) (၁၄.၉.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/13.9.2018.mp3"><span style="color: #ffcc00;">၀ဇီရာေထရီအေၾကာင္းတရားေတာ္ အပိုင္း(၂) (၁၃.၉.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/11.9.2018.mp3"><span style="color: #ffcc00;">၀ဇီရာေထရီအေၾကာင္းတရားေတာ္ (၁) (၁၁.၉.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Sep/07.9.2018_MDY_Uni_BuddhaTeachingClass.mp3"><span style="color: #ffcc00;">ဒုတိယအၾကိမ္Buddha’s Teaching သင္တန္း  (၇.၉.၂၀၁၈) မႏၲေလး တကၠသိုလ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/28.8.2018.mp3"><span style="color: #ffcc00;">ေမတၱာအေၾကာင္း တရားေတာ္ (၂၈.၈.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/26.8.2018.mp3"><span style="color: #ffcc00;">ေမတၱာအခါေတာ္ေန႔တရားေတာ္ (၂၆.၈.၂၀၁၈ ၀ါေခါင္လျပည့္ေန႔)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/08.8.2018.mp3"><span style="color: #ffcc00;">သံေ၀ဂဥဒါန္းတရားေတာ္ (၈.၈.၂၀၁၈ – Novotel Hotel)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/05.8.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၅.၈.၂၀၁၈ ေရစၾကိဳ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/04.8.2018_pm.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၄.၈.၂၀၁၈ မႏၲေလး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/04.8.2018_anumawdanar.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၄.၈.၂၀၁၈ IBEC စစ္ကိုင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/01.8.2018_WarsoAwwWarDa_to_SagaingNuns.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၁.၈.၂၀၁၈) (စစ္ကိုင္းေတာင္ သီလရွင္ဆရာေလးမ်ား ၀ါဆိုသကၤန္းကပ္လွဴျခင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-Aug/30.8.2018_IBEC_Sagaing.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၃၀.၇.၂၀၁၈ IBEC )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-July/26.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၂၆.၇.၂၀၁၈ သီတဂူဗုဒၶတကၠသုိလ္ – စစ္ကိုင္း )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-July/25.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၂၅.၇.၂၀၁၈ သီတဂူဗုဒၶတကၠသုိလ္ – ေတာင္ငူ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-July/24.7.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာ တရားေတာ္ (၂၄.၇.၂၀၁၈ သီတဂူဗုဒၶတကၠသုိလ္ – ရန္ကုန္ )</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-July/01.7.2018.mp3"><span style="color: #ffcc00;">ေမတၱာဘာ၀နာ တရားေတာ္ (၁.၇၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-June/09.6.2018.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ – ေလာကနႏၵာေစတီေတာ္ ပုဂံ (၉.၆၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-June/01.6.2018-awwwarda-sitagubuddhauni-taungngu.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ – သီတဂူကမာၻ႔ဗုဒၶတကၠသိုလ္ ေတာင္ငူ ေက်ာင္းသားသစ္ၾကိဳဆိုပြဲ (၁.၆၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-May/31.5.2018-awwwarda-sitagubuddhauni-mdy.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ – သီတဂူကမာၻ႔ဗုဒၶတကၠသိုလ္ မႏၲေလး ေက်ာင္းသားသစ္ၾကိဳဆိုပြဲ (၃၁.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-May/30.5.2018-awwwarda-sitagubuddhauni-sagaing.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ – သီတဂူကမာၻ႔ဗုဒၶတကၠသိုလ္ စစ္ကိုင္း (၃၀.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-May/30.5.2018-awwwarda-sitagubuddhauni-ygn.mp3"><span style="color: #ffcc00;">ၾသ၀ါဒတရားေတာ္ – သီတဂူကမာၻ႔ဗုဒၶတကၠသိုလ္ ရန္ကုန္ (၂၉.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018-May/29.5.2018.mp3"><span style="color: #ffcc00;">မဟာသမယေန႔အထိမ္းအမွတ္တရားေတာ္ (၂၉.၅.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/01-06-2015-kyeemyatthaw-maharthamaya.mp3"><span style="color: #ffcc00;">မဟာသမယသုတ္အႏွစ္ခ်ဳပ္တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/2018/Sitagu%20Sayardaw/2018/25.4.2018.mp3"><span style="color: #ffcc00;"> မိဘေက်းဇူးဆပ္အထိမ္းအမွတ္တရားေတာ္ (၂၅.၀၄.၂၀၁၈) </span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/sitagu-24.4.2018.mp3"><span style="color: #ffcc00;"> အနဳေမာဒနာ တရားေတာ္ (၂၄.၀၄.၂၀၁၈ ဗိုလ္တေထာင္) </span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/23.4.2018-sitagu.mp3"><span style="color: #ffcc00;"> ခႏၱီးျမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာ တရားေတာ္ (၂၃.၀၄.၂၀၁၈) </span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/18.4.2018.mp3"><span style="color: #ffcc00;"> ေက်ာင္းေဆာင္ ေရစက္ခ် အနဳေမာဒနာ တရားေတာ္ (၁၈.၀၄.၂၀၁၈) </span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/01_14.4.2018.mp3"><span style="color: #ffcc00;"> အာသီဝိေသာပမသုတၱန္ တရားေတာ္ (၁) (၁၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/02_15.4.2018.mp3"><span style="color: #ffcc00;"> အာသီဝိေသာပမသုတၱန္ တရားေတာ္ (၂) (၁၅.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/03_16.4.2018.mp3"><span style="color: #ffcc00;"> အာသီဝိေသာပမသုတၱန္ တရားေတာ္ (၃) (၁၆.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/04_17.4.2018.mp3"><span style="color: #ffcc00;"> အာသီဝိေသာပမသုတၱန္ တရားေတာ္ (၄) (၁၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/13.4.2018-1.mp3"><span style="color: #ffcc00;"> ေရေဆး၍မရေသာအညစ္အေျကးမ်ား တရားေတာ္ (၁၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://www.thitsarparamisociety.com/wp-content/uploads/2018/04/12.4.2018.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာေဒႆနာ တရားေတာ္ (၁၂.၀၄.၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/11.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ (ရွင္ေရဝတ၊ ရွင္ေသာပါက၊ ရွင္ပ႑ိတ၊ ရွင္သံကိစၥ သာမေဏ) (၁၁.၄.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/10.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – ေသာပါကသာမေဏ (၁၀.၄.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/09.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – သံကိစၥသာမေဏ (၉.၄.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/08.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – သံကိစၥသာမေဏ (၈.၄.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/07.4.2018.mp3"><span style="color: #ffcc00;">ေသာပါကသာမေဏ၊ သံကိစၥသာမေဏ၊ ေရ၀တသာမေဏ၊ ပဏၰိတသာမေဏ (၇.၄.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/07.4.2018-am.mp3"><span style="color: #ffcc00;">ပဗၺဇၨအေမြ ရွင္သမေဏ အႏုေမာဒနာတရားေတာ္ (၇.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/06.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – နိေျဂာဓ သာမေဏ (၆.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/05.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – ေရ၀တ သာမေဏ (၅.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/04.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – ဝနဝါသီ တိႆ သာမေဏ (၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/03.4.2018.mp3"><span style="color: #ffcc00;">သာမေဏေက်ာ္တရားေတာ္ – သုမန သာမေဏ (၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/04.4.2018.mp3"><span style="color: #ffcc00;">ဝနဝါသီ တိႆ သာမေဏ (၄.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/03.4.2018.mp3"><span style="color: #ffcc00;">သုမန သာမေဏ (၃.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/02.4.2018.mp3"><span style="color: #ffcc00;">အဂတိတရား(၄) တရားေတာ္ (၂.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Apr/01.4.2018.mp3"><span style="color: #ffcc00;">သဂၤါယနာအေၾကာင္းတရားေတာ္ (၁.၄.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/26.3.2018.mp3"><span style="color: #ffcc00;">အိုလာျပီဆုိရင္ ဘာေကာင္းလဲ (ေကာသလမင္းၾကီးအေၾကာင္း) (၂၆.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/25.3.2018.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ (၂၅.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/24.3.2018.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတၱံတရားေတာ္ (၂၄.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/23.3.2018.mp3"><span style="color: #ffcc00;">သုခသာမေဏအေၾကာင္းတရားေတာ္ (၂၃.၃.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/21.3.2018.mp3"><span style="color: #ffcc00;">ေကာသလမင္းၾကီးအေၾကာင္းတရားေတာ္ (၂၁.၃.၂၀၁၈ မိုးကုတ္) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/20.3.2018.mp3"><span style="color: #ffcc00;">ပ႑ိတသာမေဏတရားေတာ္ (၂၀.၃.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/18.3.2018.mp3"><span style="color: #ffcc00;">ေရႊက်င္သာသနာပိုင္ပူေဇာ္ပြဲ အႏုေမာဒနာတရားေတာ္ (၁၈.၃.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/09.3.2018.mp3"><span style="color: #ffcc00;">ဗာဟိယသုတၱံတရားေတာ္ (၉.၃.၂၀၁၈ စစ္ကိုင္း) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/08.3.2108.mp3"><span style="color: #ffcc00;">ဗာဟိယသုတၱံတရားေတာ္ (၈.၃.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/06.3.2018.mp3"><span style="color: #ffcc00;">ေကာင္းမႈၾကီးေလးပါးတရားေတာ္ (၆.၃.၂၀၁၈ ေက်ာက္ဆည္) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/05.3.2018.mp3"><span style="color: #ffcc00;">မိဘမဲ့ ရွင္(၁၀၀)ရွင္ျပဳ အလွဴ အနဳေမာဒနာ တရားေတာ္(၅.၃.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/04.3.2018-mdy.mp3"><span style="color: #ffcc00;">ရွင္ျပနားသအလွဴ အႏုေမာဒနာတရားေတာ္ (ေကာသလမင္းၾကီးအေၾကာင္း)(၄.၃.၂၀၁၈ မႏၲေလး) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/04.3.3018-A.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္ႏွင့္ ဝိသုဒၶိမဂ္စာဝါ (ပထမေန႔ – ပ) (၄.၃.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/04.3.2018-B.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္ႏွင့္ ဝိသုဒၶိမဂ္စာဝါ (ပထမေန႔ – ဒု) (၄.၃.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Mar/03.3.2018.mp3"><span style="color: #ffcc00;">အႏုေမာဒနာတရားေတာ္ (၃.၃.၂၀၁၈ စစ္ကိုင္း) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/27.02.2018.mp3"><span style="color: #ffcc00;">ေဗာဇၩဂၤသုတ္ တရားေတာ္ (၂၇.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/26.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃေလးပါးတရားေတာ္ (၂၆.၂.၂၀၁၈ – ပဲခူး ေရႊေမာေဓာ) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/22.02.2018.mp3"><span style="color: #ffcc00;">သာမဂၢီတရားေတာ္ (၂၂.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/20.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတၱံတရားေတာ္ (၂၀.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/19.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတၱံတရားေတာ္ (၁၉.၂.၂၀၁၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/13.2.2018.mp3"><span style="color: #ffcc00;">ေလာကႀကီးသည္ လူတို႔၏ ဆရာသမား (၁၃.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/12.02.2018.mp3"><span style="color: #ffcc00;">အလုံျမိဳ႕နယ္၊ ဆင္မင္းရပ္ကြက္၊သိပၸံလမ္း မိသားစု ဓမၼသဘင္ (၁၂.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/11.02.2018.mp3"><span style="color: #ffcc00;">ဆြမ္းအလွဴႏွင့္ပတ္သက္ေသာအႏုေမာဒနာတရားေတာ္ (၁၁.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/10.02.2018.mp3"><span style="color: #ffcc00;">သုခသာမေဏ၀တၳဳ (၃) (၁၀.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/09.02.2018.mp3"><span style="color: #ffcc00;">သုခသာမေဏ၀တၳဳ (၂) (၉.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/07.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတၱံတရားေတာ္ (၇.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/06.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃေလးပါးတရားေတာ္ (၆.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/05.02.2018.mp3"><span style="color: #ffcc00;">သုခသာမေဏ၀တၳဳ (၁) (၅.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/04.02.2018.mp3"><span style="color: #ffcc00;">အာေရာဂ်ဒါန – အနာကင္းေၾကာင္းအလွဴေတာ္ (၄.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/03.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃေလးျဖာ ဘ၀သံသရာတရားေတာ္ (၃.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/02.02.2018.mp3"><span style="color: #ffcc00;">အိုသည္အထိေကာင့္တဲ့တရား – ေကာသမင္းၾကီးအေမးႏွင့္အေျဖ (၂.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Feb/01.02.2018.mp3"><span style="color: #ffcc00;">ၾသဃတရဏသုတၱံတရားေတာ္ (၁.၂.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/31.1.2018.mp3"><span style="color: #ffcc00;">ေစတီေတာ္မ်ားအေၾကာင္းၾသ၀ါဒတရားေတာ္ (၃၁.၀၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/29.1.2018.mp3"><span style="color: #ffcc00;">ဘဝပင္လယ္မွာ ကၽြန္းကေလးမ်ား တည္ေဆာက္ႏိုင္ပါေစ တရားေတာ္ (၂၉.၀၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/28.1.2018.mp3"><span style="color: #ffcc00;">အမွန္တရားရွာေဖြလွ်င္ အစြန္းမထြက္နဲ႔တရားေတာ္ (ေသလာေထရီ အေၾကာင္းတရားေတာ္) (၂၈.၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/27.1.2018.mp3"><span style="color: #ffcc00;">ေရာဟိတသသုတၱန္ တရားေတာ္ (သီတဂူအေထာက္ကူျပဳအဖြဲ႕)(၂၇.၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/26.1.2018.mp3"><span style="color: #ffcc00;">ဝဇီရာေထရီ အေၾကာင္း တရားေတာ္ (ရန္ကုန္) (၂၆.၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/25.1.2018.mp3"><span style="color: #ffcc00;">ဝဇီရာေထရီ အေၾကာင္း တရားေတာ္ (ဘားအံ) (၂၅.၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/24.1.2018.mp3"><span style="color: #ffcc00;">ေက်ာင္းအနုေမာဒနာ တရားေတာ္ (၂၄.၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/23.1.2018.mp3"><span style="color: #ffcc00;">ေမတၱာတရားေတာ္ (၂၃.၁.၂၀၁၈) မိေခ်ာင္းကုန္းေက်ာင္း၊ ျမဝတီတြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/22.1.2018.mp3"><span style="color: #ffcc00;">ကာသလ သုတၱန္ တရားေတာ္ (၂၂.၁.၂၀၁၈) သထံုျမိဳ႕တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/21.1.2018.mp3"><span style="color: #ffcc00;">ဝဇိရာေထရီ အေျကာင္း တရားေတာ္ (၂၁.၁.၂၀၁၈) က်ိဳက္ထိုျမိဳ႕တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/20.1.2018.mp3"><span style="color: #ffcc00;">ေသလာေထရီ အေျကာင္း တရားေတာ္ (၂၀.၁.၂၀၁၈) မြန္ျပည္နယ္ သိမ္ဇရပ္၊ မလြန္ဆန္လွဴအသင္းတြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/19.1.2018.mp3"><span style="color: #ffcc00;">ကာသလပုစၥာ တရားေတာ္ (၁၉.၁.၂၀၁၈) ျပည္လံုးခ်မ္းသာဘုရား၊ ဖ်ာပံုၿမိဳ႕ တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/17.1.2018.mp3"><span style="color: #ffcc00;">မဇၥ်ိမဂုဏ္ရည္ဆရာေတာ္ ၀ိဇာတပူဇာဓမၼသဘင္တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္ (၁၇.၁.၂၀၁၈) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/16.1.2018.mp3"><span style="color: #ffcc00;">ယာဆရာေတာ္ႀကီး ၀ိဇာတပူဇာဓမၼသဘင္တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္(၁၆.၁.၂၀၁၈) ေ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/15.1.2018.mp3"><span style="color: #ffcc00;">ေရာဟိတသသုတၱန္ တရားေတာ္(၁၅.၁.၂၀၁၈) တိုက္ႀကီးေက်ာင္း၊ ပုသိမ္ၿမိဳ႕ တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/13.1.2018.mp3"><span style="color: #ffcc00;">ေရာဟိတသသုတၱန္ တရားေတာ္ (၁၃.၁.၂၀၁၈) မဂၤလာေတာင္ၫြန္႔၊ ရန္ကုန္ၿမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/12.1.2018.mp3"><span style="color: #ffcc00;">ေရာဟိတသသုတၱန္ တရားေတာ္ (၁၂.၁.၂၀၁၈) ေဒါပံုျမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/11.1.2018.mp3"><span style="color: #ffcc00;">ေရာဟိတသသုတၱန္ တရားေတာ္ (၁၁.၁.၂၀၁၈) ေ၀ဠဳ၀န္လမ္း၊ စမ္ေခ်ာင္းျမိဳ႕နယ္ ရန္ကုန္ျမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/10.1.2018.mp3"><span style="color: #ffcc00;">တကၡဏသုတၱန္ တရားေတာ္ (၁၀.၁.၂၀၁၈) ေျမာက္ဒဂံုျမိဳ႕နယ္၊ ရန္ကုန္ျမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/8.1.2018.mp3"><span style="color: #ffcc00;">(၈.၁.၂၀၁၈) အင္းစိန္ျမိဳ႕နယ္၊ ရန္ကုန္ျမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/7.1.2018.mp3"><span style="color: #ffcc00;">(၇.၁.၂၀၁၈) ပုဇြန္ေတာင္ၿမိဳ႕နယ္၊ ရန္ကုန္ၿမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/5.1.2018.pm.mp3"><span style="color: #ffcc00;">(၅.၁.၂၀၁၈) ေမာရိယေဆးတိုက္၊ မႏၲေလးျမိဳ႕တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/5.1.2018.mp3"><span style="color: #ffcc00;">(၅.၁.၂၀၁၈) အႏုေမာဒနာတရား (ထူပါရံုေစတီေတာ္၊ စစ္ကိုင္းၿမိဳ႕)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/4.1.2018.pm.mp3"><span style="color: #ffcc00;">(၄.၁.၂၀၁၈) ေပါင္းလဲတိုက္၊ မႏၲေလးၿမိဳ႕ တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/4.1.2018.mp3"><span style="color: #ffcc00;"> (၄.၁.၂၀၁၈) (First Time) University of Mandalay Buddha’s Teaching Class</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/3.1.2018.mp3"><span style="color: #ffcc00;">ဇရာအေျကာင္း အနုေမာဒနာတရားေတာ္ (၃.၁.၂၀၁၈) မိတၳီလာၿမိဳ႕၊ ေရလယ္ေက်ာင္းတြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/2.1.2018.mp3"><span style="color: #ffcc00;">အပရိဟာနိယသုတၱန္ တရားေတာ္ (၂.၁.၂၀၁၈) ႏွစ္သစ္မဂၤလာ အထူးတရားပြဲ ရန္ကုန္ျမိဳ႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2018/Jan/1.1.2018.mp3"><span style="color: #ffcc00;">(၁.၁.၂၀၁၈) သိမ္ေတာ္ႀကီး၊ ပန္းဘဲတန္းတြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #339966;">(၂၀၁၇) ခုႏွစ္တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/31.12.2017.mp3"><span style="color: #ffcc00;">(၃၁.၁၂.၂၀၁ရ) ႏွစ္သစ္ႏွဳတ္ခြန္းဆက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/30.12.2017.mp3"><span style="color: #ffcc00;">(၃၀.၁၂.၂၀၁၇) ေရႊတိဂံုေစတီေတာ္ အေရွ႕မုဒ္တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/29.12.2017-sg.mp3"><span style="color: #ffcc00;">(၂၉.၁၂.၂၀၁၇) စင္ကာပူႏိုင္ငံ၊ Arena Clubတြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/28.12.2017.mp3"><span style="color: #ffcc00;">(၂၈.၁၂.၂၀၁၇) လိႈင္သာယာ၊ အမွတ္-၆ ရပ္ကြက္တြင္ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/27.12.2017.mp3"><span style="color: #ffcc00;">(၂၇.၁၂.၂၀၁ရ) စစ္ေတြၿမိဳ႕၊ သာသနာ့ဗိမာန္တြင္ ေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္ </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/14.12.2017.mp3"><span style="color: #ffcc00;">စူဠပႏၳက၀တၳဳ တရားေတာ္(သပိတ္က်င္းတပ္နယ္မိသားစုု) (၁၄.၁၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/29.11.2017.mp3"><span style="color: #ffcc00;">အိုသည့္တိုင္ ေကာင္းသည့္တရား (၂၉.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/24.11.2017.mp3"><span style="color: #ffcc00;">ဥပစာလာ သုတၱံတရားေတာ္ (၂) (၂၄.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/23.11.2017.mp3"><span style="color: #ffcc00;">ဇီ၀က၏အထုပၸတၱိ (၂၃.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/22.11.2017.mp3"><span style="color: #ffcc00;">သီလာသုတၱံတရားေတာ္ (၂၂.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/15.11.2017.mp3"><span style="color: #ffcc00;">ကရုဏာတရား (၁၅.၁၁.၂၀၁၇ – သစၥာပါရမီ နာေရးကူညီမႈအသင္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/13.11.2017.mp3"><span style="color: #ffcc00;">ဥပစာလာ သုတၱံတရားေတာ္ (၁) (၁၃.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/12.11.2017.mp3"><span style="color: #ffcc00;">မေကာင္းမႈေတြကိုခြာေရွာင္ျခင္း (၁၂.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/11.11.2017.mp3"><span style="color: #ffcc00;">မဟာဂႏၶာရံု ႏွစ္-၁၀၀ ျပည့္ (၁၁.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/8.11.2017.mp3"><span style="color: #ffcc00;">သီဟိုုဠ္ရွင္ဘုုရား ႏွစ္-၉၀ဝျပည့္တြင္ေဟာၾကားေတာ္မူေသာတရားေတာ္ (၈.၁၁.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/5.11.2017.mp3"><span style="color: #ffcc00;">ဇာတကပါဠိလာ ပေစၥကဗုဒၶါအေၾကာင္းတရားေတာ္ (၅.၁၁.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/4.11.2017.mp3"><span style="color: #ffcc00;">ပေစၥကဗုဒၶါအေၾကာင္းတရားေတာ္ (၄.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/3.11.2017.mp3"><span style="color: #ffcc00;">တန္ေဆာင္မုန္းလျပည့္ေန႔ တရားေတာ္ (၃.၁၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/9.11.2017.mp3"><span style="color: #ffcc00;">ညီၫြတ္ေရးအတြက္ သာမဂၢီတရားေတာ္ (၃၀.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/27.10.2017.mp3"><span style="color: #ffcc00;">သာမဂၢီရသ – ညီညြတ္ျခင္းဟာအရသာသိပ္ရိွတယ္တရားေတာ္ (၂၇.၁၀.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/25.10.2017.mp3"><span style="color: #ffcc00;">ျဗဟၼ၀ိဟာရီ ပေစၥကဗုဒၶါအေၾကာင္းတရားေတာ္ (၂၅.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/23.10.2017.mp3"><span style="color: #ffcc00;">ညီညြတ္ေရးနဲ႔ပတ္သက္ေသာအေၾကာင္းတရား တရားေတာ္ – ၂ (၂၃.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/22.10.2017.mp3"><span style="color: #ffcc00;">ညီညြတ္ေရးနဲ႔ပတ္သက္ေသာအေၾကာင္းတရား တရားေတာ္(၂၂.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/21.10.2017.mp3"><span style="color: #ffcc00;">အျပန္အလွန္မီွခိုၾက တရားေတာ္(၂၁.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/4.10.2017.mp3"><span style="color: #ffcc00;">စိတ္စြမ္းအား တရားေတာ္ (ဗထူးျမိဳ႕ – ၄.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/3.10.2017.mp3"><span style="color: #ffcc00;">ဆီမီးပူေဇာ္ပြဲအထိမ္းအမွတ္ ေဟာၾကားေပးေတာ္မူေသာ တရားေတာ္ (၃.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/2.10.2017.mp3"><span style="color: #ffcc00;">ေစတီတည္ထားကိုးကြယ္ရျခင္း (၂.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/2.10.2017_AM.mp3"><span style="color: #ffcc00;">သီတဂူတပည့္မိသားစုအား ေဟာၾကားအပ္ေသာ ၾသ၀ါဒတရားေတာ္ (၂.၁၀.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/28.9.2017.mp3"><span style="color: #ffcc00;">သံေ၀ဂစကားတစ္ခြန္း (၂၈.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/27.9.2017.mp3"><span style="color: #ffcc00;">အပၸမာဒတရားေတာ္ (၂၇.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/26.9.2017.mp3"><span style="color: #ffcc00;">ဥပစာလာေထရီႏွင့္ မာရ္နတ္တို႔ အျပန္အလွန္ေဆြးေႏြးခန္းတရားေတာ္ (၂၆.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/25.9.2017.mp3"><span style="color: #ffcc00;">ေသလာေထရီအေၾကာင္းတရားေတာ္ (၂၅.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/24.9.2017.mp3"><span style="color: #ffcc00;">ျမိဳ႕လွျမိဳ႕ ဓမၼသဘင္ (၂၄.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/23.9.2017.mp3"><span style="color: #ffcc00;">ဘ၀ဟာ ပင္လယ္နဲ႔တူသည္ တရားေတာ္ (၂၃.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/16.9.2017.mp3"><span style="color: #ffcc00;"> ဒဒၵဳဘဇာတ္ေတာ္ – (၂) (၁၆.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/15.9.2017.mp3"><span style="color: #ffcc00;">ကုိယ့္စားက်က္မွာ ကိုယ္ေနၾက တရားေတာ္ (၂) (သကုဏဂၣိသုတၱန္) – (၁၅.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/14.9.2017.mp3"><span style="color: #ffcc00;">ကုိယ့္စားက်က္မွာ ကိုယ္ေနၾက တရားေတာ္ (၁) (သကုဏဂၣိသုတၱန္) – (၁၄.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/13.9.2017.mp3"><span style="color: #ffcc00;"> ေတာ္သလင္းလျပည့္ေက်ာ္(၈)ရက္ ဥပုသ္ေန႔ဓမၼသဘင္ – (၁၃.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/12.9.2017.mp3"><span style="color: #ffcc00;"> ဒဒၵဳဘဇာတ္ေတာ္ (၁)- (၁၂.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/10.9.2017.mp3"><span style="color: #ffcc00;">ေနနည္းသံုးပါးတရားေတာ္ အပိုင္း (၄) – (၁၀.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/9.9.2017.mp3"><span style="color: #ffcc00;">အစြန္းမေရာက္ၾကေစႏွင့္ တရားေတာ္ – (၉.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/8.9.2017.mp3"><span style="color: #ffcc00;">ျဗဟၼ၀ိဟာရီ ပေစၥကဗုဒၶါအေၾကာင္းတရားေတာ္ (၂) – ခဂၢ၀ိသာဏသုတၱန္ – (၈.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/7.9.2017.mp3"><span style="color: #ffcc00;">ျဗဟၼ၀ိဟာရီ ပေစၥကဗုဒၶါအေၾကာင္းတရားေတာ္ (၁) – ခဂၢ၀ိသာဏသုတၱန္ – (၇.၉.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/6.9.2017.mp3"><span style="color: #ffcc00;">ေနနည္းသံုးပါးတရားေတာ္ အပိုင္း (၃) (ေ၀နာဂပုရသုတၱန္)– (၆.၉.၂၀၁၇) </span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/5.9.2017.mp3"><span style="color: #ffcc00;">ေတာ္သလင္းလျပည့္ေန႔(ဂ႐ုဓမၼအခါေတာ္ေန႔) (၅.၉.၂၀၁၇) သီတဂူဆရာေတာ္ဘုရားႀကီး၏ ေမတၱာတရားပြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/1.9.2017.mp3"><span style="color: #ffcc00;">ခဂၢ၀ိသာဏသုတၱန္ – (၁.၉.၂၀၁၇) မလြန္ေစ်းဆန္လွဴအသင္းသီတဂူဓမၼသဘင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/30.8.2017.mp3"><span style="color: #ffcc00;">(၄၀)ႀကိမ္ေျမာက္ ေက်ာက္ဆည္ၿမိဳ႕ မလြန္ဆန္လွဴသင္းေထာက္အဖြဲ႕ သီတဂူဓမၼသဘင္ – (၃၀.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/29.8.2017.mp3"><span style="color: #ffcc00;">ဥပုသ္ေန႔ဓမၼသဘင္ – (၂၉.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/25.8.2017.mp3"><span style="color: #ffcc00;">ေနနည္းသံုးပါးတရားေတာ္ အပိုင္း (၂) – (၂၅.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/24.8.2017.mp3"><span style="color: #ffcc00;">ေနနည္းသံုးပါးတရားေတာ္ အပိုင္း (၁) – (၂၄.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/22.8.2017.mp3"><span style="color: #ffcc00;">ေ၀နာဂပုရသုတၱန္ – (၂၂.၈.၂၀၁ရ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/21.8.2017.mp3"><span style="color: #ffcc00;">ေမတၱာတရားေတာ္ – (တတိယပိုင္း) (၂၁.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/21.8.2017_AM.mp3"><span style="color: #ffcc00;">ေတာင္႐ိုုးေပ်ာ္သီလရွင္ဆရာေလးတုိ႔အား ေဟာၾကားေသာ ၾသ၀ါဒတရားေတာ္ – (၂၁.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/18.8.2017.mp3"><span style="color: #ffcc00;">ျမတ္စြာဘုရား၏ေန႔စဥ္လုပ္ငန္းစဥ္ (၁၈.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/17.8.2017.mp3"><span style="color: #ffcc00;">ေမတၱာဘာ၀နာတရားေတာ္ (၁၇.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/15.8.2017.mp3"><span style="color: #ffcc00;">ေမတၱာတရားေတာ္ – (ဒုတိယပိုင္း) (၁၅.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/16.8.2017.mp3"><span style="color: #ffcc00;">ျမန္ေအာင္ေခ်ာင္း ေက်ာင္းလႊတ္ပူဇာ အႏုေမာဒနာတရားေတာ္(၁၆.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/7.8.2017.mp3"><span style="color: #ffcc00;">၀ါေခါင္လျပည့္ေန႔ ေမတၱာအခါေတာ္ေန႔တရားေတာ္ – ေမတၱာတရားေတာ္ (ပထမပိုင္း) (၇.၈.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/26.2.2017.mp3"><span style="color: #ffcc00;">ၾသဂသရနသုတၱန္ (၂၆.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/24.2.2017.mp3"><span style="color: #ffcc00;">သီတဂူစကၡဳဒါနေဆးရံုဖြင့္ ေအာင္ပြဲ (၂၄.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/23.2.2017.mp3"><span style="color: #ffcc00;">စူဠပႏၳက (စူဠပန္မေထရ္ ဝတၳဳ)&nbsp;(၂၃.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/22-2-2017.mp3"><span style="color: #ffcc00;">ရန္ကုန္ (၂၂.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/21.2.2017.mp3"><span style="color: #ffcc00;">(ေနပူကုန္းစံျပေက်းရြာ၊ ဝမ္းတြင္း) (၂၁.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/20-2-2017.mp3"><span style="color: #ffcc00;">အပၸမာဒ ပမၼာဒ တရားေတာ္(၂၀.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/10-2-2017.mp3"><span style="color: #ffcc00;">တိႆ ရဟန္းဝတၳဳတရားေတာ္ (၁၀.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/9-2-2017.mp3"><span style="color: #ffcc00;">သူေဌးႀကီးမ်ားအေၾကာင္ ၃ (၉.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/8-2-2017.mp3"><span style="color: #ffcc00;">သူေဌးႀကီးမ်ားအေၾကာင္း ၂ (၈.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/february/7-2-2017.mp3"><span style="color: #ffcc00;">သူေဌးႀကီးမ်ားအေၾကာင္ ၁ (၇.၂.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/24-1-2017.mp3"><span style="color: #ffcc00;">တာခ်ီလိတ္(၂၄.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/18-1-2017.mp3"><span style="color: #ffcc00;">ျမတ္စြာဘုုရားအား ပုုဏၰားေပးေသာ ေလနာေပ်ာက္ေဆး တရားေတာ္ (၁၈.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/17-1-2017.mp3"><span style="color: #ffcc00;">လူ႔ဘ၀တစ္ခုုလုုံး၏ အျမတ္ဆုုံးဥစၥာ သီလႏွင့္ ပညာ တရားေတာ္ (၁၇.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/15-1-2017.mp3"><span style="color: #ffcc00;">နဂၢဇိပေစၥကဗုုဒၶ တရားေတာ္ (၁၅.၁.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/8-1-2017.mp3"><span style="color: #ffcc00;">(၈.၁.၂၀၁၇) မဲေဆာက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/7-1-2017.mp3"><span style="color: #ffcc00;">(၇.၁.၂၀၁၇) ျမဝတီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/6-1-2017.mp3"><span style="color: #ffcc00;">ၿငိမ္းခ်မ္းေရး၏ ဖြင့္ၿဖိဳးတိုးတက္မႈ႕အထိုင္းအမွတ္ (၆.၁.၂၀၁၇) ျမဝတီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/5-1-2017.mp3"><span style="color: #ffcc00;">(၅.၁.၂၀၁၇) ဘားအံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/2-1-2017.mp3"><span style="color: #ffcc00;">စကၠဝတၱိသုတၱန္ (၂.၁.၂၀၁၇) ျပည္သူ႕ရင္ျပင္၊ ရန္ကုန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/newyear-2017.mp3"><span style="color: #ffcc00;">၂၀၁၇ခုုႏွစ္ ႏွစ္သစ္ၾသ၀ါဒကထာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/january/1-1-2017.mp3"><span style="color: #ffcc00;">(၁.၁.၂၀၁၇) စင္ကာပူ</span></a></p>
<h5><span style="color: #339966;">ေက်းဇူးေတာ္ရွင္ သီတဂူဆရာေတာ္ဘုရားႀကီး ေမြးေန႔ဓမၼသဘင္တြင္ ဆရာေတာ္ႀကီးမ်ားေဟာၾကားထားေသာ တရားေတာ္မ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/sitagu-sayarpayargyi-birthday-awwwardakahtar.mp3"><span style="color: #ffcc00;">သီတဂူဆရာေတာ္ဘုရားႀကီး ေမြးေန႔ၾသ၀ါဒကထာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/vipassana-damaryone-yaysatcha-anumawdanar.mp3"><span style="color: #ffcc00;">သီတဂူ သံေ၀ဇနိယဗိမာန္ေတာ္ႀကီး ေရစက္ခ်အလွဴေတာ္မဂၤလာ အႏုေမာဒနာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/8thday-sitagu-sayardawpayar.mp3"><span style="color: #ffcc00;">ေ၀လာမသုတၱန္တရားေတာ္ – သီတဂူဆရာေတာ္ဘုရားႀကီး – ဓမၼသဘင္ (ေနာက္ဆံုးည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/7thday-drdhammasami.mp3"><span style="color: #ffcc00;">မာတာယထာ ကရုဏာတရားေတာ္ – ေဒါက္တာဓမၼသာမိ – ဓမၼသဘင္ (သတၱမည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/6thday-parchoke-sayardawpayargyi.mp3"><span style="color: #ffcc00;">ဒိေ႒ဒိ႒မတၱံ ၀ိပႆနာက်င့္စဥ္ – ပါခ်ဳပ္ဆရာေတာ္ဘုရားႀကီး – ဓမၼသဘင္ (ဆ႒မည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/5thday-paauk-sayarpayargyi.mp3"><span style="color: #ffcc00;">ပဌမ ပဋိဂါမိသုတ္တရားေတာ္ – ဖားေအာ္ဆရာေတာ္ဘုရားႀကီး – ဓမၼသဘင္ (ပဥၥမည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/5thday-hlaingmaharsisayrdaw.mp3"><span style="color: #ffcc00;">လိွဴင္မဟာစည္ဆရာေတာ္ႀကီး တရားေတာ္ – ဓမၼသဘင္ (ပဥၥမည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/4thday-ashinsaykanena.mp3"><span style="color: #ffcc00;">ခ်မ္းျမသာယာရိွပါေစတရားေတာ္ – ဆရာေတာ္အရွင္ေဆကိႏၵ – ဓမၼသဘင္ (စတုတၳည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/3rdday-aungsan-sayardaw.mp3"><span style="color: #ffcc00;">ေအာင္ဆန္းဆရာေတာ္ႀကီး တရားေတာ္ – ဓမၼသဘင္ (တတိယည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/2ndday-tipitakadaya-myinchansayardaw.mp3"><span style="color: #ffcc00;">ေခါင္းေဆာင္ေကာင္းတို႔အရည္အေသြး – တိပိဋကဓရ ျမင္းျခံဆရာေတာ္ အရွင္ဂႏၶမာလာလကၤာရ – ဓမၼသဘင္ (ဒုတိယည)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/birthday-dhamma/1stday-shweminwan-maharsisayardaw-.mp3"><span style="color: #ffcc00;">သတိပ႒ာန္တရားေတာ္ – ေရႊမင္း၀ံ မဟာစည္ဆရာေတာ္ႀကီး – ဓမၼသဘင္ (ပထမည)</span></a></p>
<h5><span style="color: #339966;">အာနာပါနႆတိ သုတၱံသင္တန္း (၁-၆-၂၀၁၇ မွ ၇-၆-၂၀၁၇) (သီတဂူဗုဒၶတကၠသိုလ္)</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/001-01-06-2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – ပထမေန႔ – (၁.၆.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/002-02-06-2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – ဒုတိယေန႔ – (၂.၆.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/003-03.06.2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – တတိယေန႔ – (၃.၆.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/004-04.06.2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – စတုတၳေန႔ – (၄.၆.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/005-05-06-2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – ပဥၥမေန႔ – (၅.၆.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/006-06.06.2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – ဆ႒မေန႔ – (၆.၆.၂၀၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2017/June/007-07.06.2017.mp3"><span style="color: #ffcc00;">အာနာပါနႆတိ သုတၱံသင္တန္း – သတၱမေန႔ – (၇.၆.၂၀၁၇)</span></a></p>
<p>&nbsp;</p>
<h6><span style="color: #339966;">ဗုဒၶရတနာ႔ဂုဏ္ရည္တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/001%20U%20Nyanissara%20D26%204-1-2004%20BuddhaYatanaGoneYae%201.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၁) (၄-၁-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/002%20U%20Nyanissara%20D26%205-1-2004%20BuddhaYatanaGoneYae%202.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၂)<br>
(၅-၁-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/003%20U%20Nyanissara%20D26%206-1-2004%20BuddhaYatanaGoneYae%203.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၃) (၆-၁-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/004%20U%20Nyanissara%20D26%207-1-2004%20BuddhaYatanaGoneYae%204.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၄) (၇-၁-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/005%20U%20Nyanissara%20D26%208-1-2004%20BuddhaYatanaGoneYae%205.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၅) (၈-၁-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/006%20U%20Nyanissara%20D26%2010-1-2004%20BuddhaYatanaGoneYae%206.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၆) (၁၀-၁-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/007%20U%20Nyanissara%20D26%2011-1-2004%20BuddhaYatanaGoneYae%207.mp3"><span style="color: #ffcc00;">ဗုဒၶရတနာ႔ဂုဏ္ရည္(၇) (၁၁-၁-၂၀၀၄)</span></a></p>
<h6><span style="color: #339966;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0429-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0430-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0431-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0432-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0433-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0434-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0435-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0436-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0437-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0438-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶမပြင့္မွီကိုးကြြယ္မႈအေျခအေနတရား(၁၀)</span></a></p>
<h6><span style="color: #339966;">ဗုဒၶဝါဒအေျခခံတရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0418-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0419-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0420-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0421-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0422-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0423-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0424-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0425-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0426-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0427-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဝါဒအေျခခံတရားေတာ္(၁၀)</span></a></p>
<p>&nbsp;</p>
<h6><span style="color: #339966;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္းတရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/067%2020080812%20BuddhaWarDaHnintLuHmuYayLoteNgan%201.mp3"><span style="color: #ffcc00;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္း – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/068%2020080815%20BuddhaWarDaHnintLuHmuYayLoteNgan%202.mp3"><span style="color: #ffcc00;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္း – ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/069%2020080816%20BuddhaWarDaHnintLuHmuYayLoteNgan%203.mp3"><span style="color: #ffcc00;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္း – ၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/070%2020080817%20BuddhaWarDaHnintLuHmuYayLoteNgan%204.mp3"><span style="color: #ffcc00;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္း – ၄</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/071%2020080819%20BuddhaWarDaHnintLuHmuYayLoteNgan%205.mp3"><span style="color: #ffcc00;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္း – ၅</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/072%2020080820%20BuddhaWarDaHnintLuHmuYayLoteNgan%206.mp3"><span style="color: #ffcc00;">ဗုဒၶ၀ါဒႏွင့္ လူမႈေရးလုပ္ငန္း – ၆</span></a></p>
<h6><span style="color: #339966;">ဓမၼရတနာဂုဏ္ရည္တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0819-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာဂုဏ္ရည္ “၁” (စ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0821-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာဂုဏ္ရည္ “၁” (ဆံုး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0965-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာဂုဏ္ရည္ “၂” (စ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0966-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာဂုဏ္ရည္ “၂” (ဆံုး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0824-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာဂုဏ္ရည္ “၃” (စ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0825-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာဂုဏ္ရည္ “၃” (ဆံုး)</span></a></p>
<h6><span style="color: #339966;">သံဃာရတနာ့ဂုဏ္ရည္တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0866-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံဃာရတနာ့ဂုဏ္ရည္ “၁” (စ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0867-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံဃာရတနာ့ဂုဏ္ရည္ “၁” (ဆံုး)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0868-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံဃာရတနာဂုဏ္ရည္ “ ၄” (စ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0869-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံဃာရတနာဂုဏ္ရည္ “ ၄” (ဆံုး)</span></a></p>
<h6><span style="color: #339966;">ႏွစ္သစ္ကူးသတိပဌါန္တရာ</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0674-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0675-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0676-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0677-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0678-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0679-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0680-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0681-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0682-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0683-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0684-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0685-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0686-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ႏွစ္သစ္ကူးသတိပဌါန္တရား(၁၃)</span></a></p>
<h6><span style="color: #339966;">အာနာပါန၊ သတိပဌာန္တရား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0008-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာနာပါန၊ သတိပဌာန္တရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0009-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာနာပါန၊ သတိပဌာန္တရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0010-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာနာပါန၊ သတိပဌာန္တရား (၃)</span></a></p>
<h6><span style="color: #339966;">ေဝဒနာႏုပႆနာ သတိပဌာန္တရား</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0138-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေဝဒနာႏုပႆနာ သတိပဌာန္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0139-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေဝဒနာႏုပႆနာ သတိပဌာန္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0140-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေဝဒနာႏုပႆနာ သတိပဌာန္တရား(၃)</span></a></p>
<h6><span style="color: #339966;">မဂၤလာ့သုတၲန္တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/07/001%20U%20Nyanissara%20D9%2031-3-1980%20ManGaLaThoutTanNeedDan.mp3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္နိဒါန္း (၃၁-၃-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0216-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၁-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0217-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၁-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0218-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၂-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0219-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၂-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0220-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၃-၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0221-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၃-၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0222-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဂၤလာ့သုတၲန္တရားေတာ္ (၃-၃)</span></a></p>
<h6><span style="color: #339966;">ရတနာသုတ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0836-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရတနာသုတ္</span></a></p>
<h6><span style="color: #339966;">ေမတၱာသုတ္ တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0563-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာသုတ္ တရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0564-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာသုတ္ တရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0565-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာသုတ္ တရားေတာ္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0566-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာသုတ္ တရားေတာ္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0567-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာသုတ္ တရားေတာ္(၅)</span></a></p>
<h6><span style="color: #339966;">ေမာရသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0107-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမာရသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0108-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမာရသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">ဝိဘက္ေတာ္(၁၂)ပါးတရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0151-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0152-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0153-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0154-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0155-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0156-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0157-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0158-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0159-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0161-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0162-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိဘက္ေတာ္(၁၂)ပါး (၁၁)</span></a></p>
<h6><span style="color: #339966;">အပၸမာဒတရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0461-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပၸမာဒတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0462-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပၸမာဒတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0791-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာဒတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0792-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာဒတရား(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0793-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာဒတရား(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0794-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာဒတရား(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0795-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာဒတရား(၇)</span></a></p>
<h6><span style="color: #339966;">သံေဝဇနိယေလးဌာနတရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0391-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံေဝဇနိယေလးဌာန (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0392-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံေဝဇနိယေလးဌာန (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0393-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံေဝဇနိယေလးဌာန (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0394-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံေဝဇနိယေလးဌာန (၄)</span></a></p>
<h5><span style="color: #00ffff;">သုတၱန္တရားေတာ္မ်ား</span></h5>
<p>&nbsp;</p>
<h6><span style="color: #339966;">ကာမသုတၱန</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0059-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာမသုတၱန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0060-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာမသုတၱန္ (၂)</span></a></p>
<h6><span style="color: #339966;">ေကသမုတၲိသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0014-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကသမုတၲိသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0015-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကသမုတၲိသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0016-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကသမုတၲိသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">ေဂါဒိကသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0587-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဂါဒိကသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0588-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဂါဒိကသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0535-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဂါသိဂၤသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0536-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဂါသိဂၤသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">စကၠဝတၱိသုတ္ </span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/Singapore-19-9-15.mp3" target="_blank"><span style="color: #ffcc00;">စကၠဝတၱိသုတ္ – ခ်င္းျပည္နယ္အလွဴေတာ္ တရားပြဲ (စင္ကာပူ -၁၉.၉.၂၀၁၅) </span></a></p>
<h6><span style="color: #339966;">စူဠေဂါသိဂၤသုတၱန္ </span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0342-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဂါသိဂၤသုတၱန္ (၁) ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0343-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဂါသိဂၤသုတၱန္ (၁) ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0344-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဂါသိဂၤသုတၱန္ (၂) ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0345-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဂါသိဂၤသုတၱန္ (၂) ဒုတိယပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0346-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဂါသိဂၤသုတၱန္ (၃) ပထမပိုင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0347-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဂါသိဂၤသုတၱန္ (၃) ဒုတိယပိုင္း</span></a></p>
<h6><span style="color: #339966;">စူဠေဝဒလႅသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0028-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0029-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0030-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0031-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0032-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0033-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0034-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0035-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0036-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0037-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0038-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠေဝဒလႅသုတၱန္(၁၁)</span></a></p>
<h6><span style="color: #339966;">စူႏၵသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0992-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူႏၵသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0993-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူႏၵသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0994-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူႏၵသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0995-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူႏၵသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0996-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူႏၵသုတၱန္(၅)</span></a></p>
<h6><span style="color: #339966;">ဆေႏၵာဝါဒသုတၲန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0068-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဆေႏၵာဝါဒသုတၲန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0069-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဆေႏၵာဝါဒသုတၲန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0070-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဆေႏၵာဝါဒသုတၲန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0071-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဆေႏၵာဝါဒသုတၲန္(၄)</span></a></p>
<h6><span style="color: #339966;">ဇဋာသုတၲန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0353-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဇဋာသုတၲန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0354-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဇဋာသုတၲန္(၂)</span></a></p>
<h6><span style="color: #339966;">ဒ႒ဗၺသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0146-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒ႒ဗၺသုတၱန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0147-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒ႒ဗၺသုတၱန္ (၂)</span></a></p>
<h6><span style="color: #339966;">ေဒ၀ဟိတသုတၱန</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0980-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဒ၀ဟိတသုတၱန္</span></a></p>
<h6><span style="color: #339966;">ဒါ႐ုကၡေႏၶာပမသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0003-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါ႐ုကၡေႏၶာပမသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0004-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါ႐ုကၡေႏၶာပမသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0005-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါ႐ုကၡေႏၶာပမသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0006-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါ႐ုကၡေႏၶာပမသုတၱန္(၄)</span></a></p>
<h6><span style="color: #339966;">နႏၵ မာတာသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0072-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နႏၵ မာတာသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0073-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နႏၵ မာတာသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">နႏၵသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0103-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နႏၵသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0104-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နႏၵသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0105-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နႏၵသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">နိဗၺာနပတိသံယုတၲသုတၱန</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0361-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပထမနိဗၺာနပတိသံယုတၱသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0362-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပထမနိဗၺာနပတိသံယုတၱသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0363-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပထမနိဗၺာနပတိသံယုတၱသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0395-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒုတိကနိဗၺာနပတိသံယုတၲသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0396-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒုတိကနိဗၺာနပတိသံယုတၲသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0364-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တတိယနိဗၺာနပတိသံယုတၲသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0365-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တတိယနိဗၺာနပတိသံယုတၲသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">အနာထပိ႑ကသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0118-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပထမအနာထပိ႑ကသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0119-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပထမအနာထပိ႑ကသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0144-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒုတိယအနာထပိ႑ိကသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0145-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒုတိယအနာထပိ႑ိကသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">ပရိနိဗၺာန္နသုတ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0873-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပရိနိဗၺာန္နသုတ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0874-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပရိနိဗၺာန္နသုတ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0875-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပရိနိဗၺာန္နသုတ္ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0876-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပရိနိဗၺာန္နသုတ္ (၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0877-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပရိနိဗၺာန္နသုတ္ (၅)</span></a></p>
<h6><span style="color: #339966;">ပရိေယသနာသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0197-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပရိေယသနာသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0198-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပရိေယသနာသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0199-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပရိေယသနာသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">ပါဏီယာဟာရသုတၱန္တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0326-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါဏီယာဟာရသုတၱန္တရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0327-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါဏီယာဟာရသုတၱန္တရားေတာ္(၂)</span></a></p>
<h6><span style="color: #339966;">ပါရာသိသုတၱန္(</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0369-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ပထမပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0370-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ပထမပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0371-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ဒုတိယပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0372-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ဒုတိယပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0373-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(တတိယပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0374-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(တတိယပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0922-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(စတုတၳပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0923-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(စတုတၳပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0375-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ပဥၥမပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0376-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ပဥၥမပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0377-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ဆဌမပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0378-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ဆဌမပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0379-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(သတၲမပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0380-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(သတၲမပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0381-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(အဌမပုိင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0382-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(အဌမပုိင္း)-(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0383-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ေနာက္ဆံုးပိုင္း)-(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0384-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရာသိသုတၲန္(ေနာက္ဆံုးပိုင္း)-(၂)</span></a></p>
<h6><span style="color: #339966;">ေဖဏပိ႑ဴပမာသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0120-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0121-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0122-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0123-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0124-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0125-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0126-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0127-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0128-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0129-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0130-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0131-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0132-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0133-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0134-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0135-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0136-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0137-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဖဏပိ႑ဴပမာသုတၱန္(၁၈)</span></a></p>
<h6><span style="color: #339966;">ဗဟုဒီတရသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0001-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗဟုဒီတရသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0002-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗဟုဒီတရသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">ဘာရသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0358-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘာရသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0944-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘာရသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0945-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘာရသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0946-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘာရသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0947-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘာရသုတၱန္(၄)</span></a></p>
<h6><span style="color: #339966;">မနာပဒါယီသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0099-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မနာပဒါယီသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0100-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မနာပဒါယီသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">မဟာလိသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0076-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဟာလိသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0077-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဟာလိသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">မဟာသာလျဗဟၼဏသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0057-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဟာသာလျဗဟၼဏသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0058-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဟာသာလျဗဟၼဏသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">မာတိကာမာတာသုတၱန</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0208-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မာတိကာမာတာသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0209-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မာတိကာမာတာသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">မစၦရိယသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/006%20U%20Nyanissara%20D42-MitSaYeatYaThoutTan.mp3"><span style="color: #ffcc00;">မစၦရိယသုတၱန္ တရားေတာ္</span></a></p>
<h6><span style="color: #339966;">မုစလိႏၵသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0544-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုစလိႏၵသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0545-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုစလိႏၵသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">မုနိသုတၱန္(</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0017-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုနိသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0018-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုနိသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0019-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုနိသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">မုနိသုတၱန္ႏွင့္နႏၵသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0095-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုနိသုတၱန္ႏွင့္နႏၵသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0096-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုနိသုတၱန္ႏွင့္ နႏၵသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0097-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မုနိသုတၱန္ႏွင့္နႏၵသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">ေမတၱာေစေတာ္မုတၱိသတၱိသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0504-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာေစေတာ္မုတၱိသတၱိသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0505-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာေစေတာ္မုတၱိသတၱိသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">မဂၢသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0449-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0450-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0451-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">ရာဟုေလာဝါဒသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0243-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ရာဟုေလာဝါဒသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0244-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ရာဟုေလာဝါဒသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0245-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ရာဟုေလာဝါဒသုတၱန္(၃)</span></a></p>
<h6><span style="color: #339966;">ေရာဟိတႆသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0349-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရာဟိတႆသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0350-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရာဟိတႆသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">ေလာကသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/37/009%20U%20Nyanassara%20D43-LawKaSutta.mp3"><span style="color: #ffcc00;">ေလာကသုတၱန္</span></a></p>
<h6><span style="color: #339966;">၀ဋေပါတကဇာတကသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0109-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ဋေပါတကဇာတကသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0110-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ဋေပါတကဇာတကသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0111-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ဋေပါတကဇာတကသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">ဝနေရာပသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0513-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝနေရာပသုတၱန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0214-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝနေရာပသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0215-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝနေရာပသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">၀ကၠလိသုတၱန္ (သဒၵ ါဝိမုတၱ ဧတေဒဂ္)</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0182-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ကၠလိသုတၱန္ (သဒၵ ါဝိမုတၱ ဧတေဒဂ္)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0183-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ကၠလိသုတၱန္ (သဒၵ ါဝိမုတၱ ဧတေဒဂ္)(၂)</span></a></p>
<h6><span style="color: #339966;">၀ကၠလိသုတၱန္ (အဓိမာနိက)</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0180-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ကၠလိသုတၱန္ (အဓိမာနိက)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0181-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ကၠလိသုတၱန္ (အဓိမာနိက)(၂)</span></a></p>
<h6><span style="color: #339966;">ေဝလာမသုတၲန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0039-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေဝလာမသုတၲန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0040-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေဝလာမသုတၲန္ (၂)</span></a></p>
<h6><span style="color: #339966;">ေဝႆႏၲရာသတၲိသုတၲန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/25/006%20U%20Nyanissara%20D29%20WayThanThaYarThetTeatThoutTan.mp3"><span style="color: #ffcc00;">ေဝႆႏၲရာသတၲိသုတၲန္</span></a></p>
<h6><span style="color: #339966;">ဝမၼိကသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0397-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ပထမပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0398-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ပထမပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0399-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ပထမပုိင္း)(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0400-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ဒုတိယပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0401-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ဒုတိယပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0402-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ဒုတိယပုိင္း)(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0403-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(တတိယပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0404-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(တတိယပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0405-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(တတိယပုိင္း)(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0406-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(စတုတၳပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0407-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(စတုတၳပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0408-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ပဥၥမပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0409-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ပဥၥမပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0410-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ပဥၥမပုိင္း)(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0411-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ဆဌမပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0412-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(ဆဌမပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0413-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(သတၲမပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0414-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(သတၲမပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0415-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝမၼိကသုတၱန္(သတၲမပုိင္း)(၃)</span></a></p>
<h6><span style="color: #339966;">သာဓုသုတၱန</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0194-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာဓုသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0195-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာဓုသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">သာမညဖလသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0723-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာမညဖလသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0724-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာမညဖလသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">သာႏုသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0977-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာႏုသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0978-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာႏုသုတၱန္(၂)</span></a></p>
<h6></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%20Disc%202/007%20U%20Nyanissara%20D2%201-3-1978%20%20PoneNorWarDa%20Sutta.mp3"><span style="color: #ffcc00;">သုဒၶဟ သုတၱန္ (၁.၃.၁၉၇၈)</span></a></p>
<h6><span style="color: #339966;">သုဗၺဗုဒၶကုဋိသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0983-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဗၺဗုဒၶကုဋိသုတၱန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0984-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဗၺဗုဒၶကုဋိသုတၱန္ (၂)</span></a></p>
<h6><span style="color: #339966;">သုဘဒၵသတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0777-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဘဒၵသတၱန္တရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0778-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဘဒၵသတၱန္တရားေတာ္(၂)</span></a></p>
<h6><span style="color: #339966;">သကၠပဥွာသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0041-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0042-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0043-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0044-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0045-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0046-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0047-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0048-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0049-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0050-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0051-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0052-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0053-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၁၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0054-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠပဥွာသုတၱန္(၁၄)</span></a></p>
<h6><span style="color: #339966;">သကၠသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0611-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0612-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သကၠသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">သဂၤါေလာဝါဒသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0175-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0163-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0164-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0165-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0166-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0167-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0168-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0169-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0170-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0171-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၁၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0172-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၁၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0173-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၁၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0174-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဂၤါေလာဝါဒသုုတၱန္(၁၃)</span></a></p>
<h6><span style="color: #339966;">သတၱိသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0493-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သတၱိသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0494-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သတၱိသုုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">သဒၵါဝိမုတၱသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0957-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဒၵါဝိမုတၱသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0958-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဒၵါဝိမုတၱသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">သဒၶမၼပတိရူပကသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0212-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဒၶမၼပတိရူပကသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0213-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဒၶမၼပတိရူပကသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">သပၸဴရိသဒါနသုတၱန္ </span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/002%20U%20Nyanissara%20D42-ThaPuYeatTaDarNaThoutTan.mp3"><span style="color: #ffcc00;">သပၸဴရိသဒါနသုတၱန္ တရားေတာ္</span></a></p>
<h6><span style="color: #339966;">ေသာဏဒဏၭသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0671-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေသာဏဒဏၭသုတၱန္</span></a></p>
<h6><span style="color: #339966;">အနာထပိ႑ိေကာဝါဒသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0583-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အနာထပိ႑ိေကာဝါဒသုုတၱန္-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0584-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အနာထပိ႑ိေကာဝါဒသုတၱန္-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0585-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အနာထပိ႑ိေကာဝါဒသုုတၱန္-၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0586-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အနာထပိ႑ိေကာဝါဒသုုတၱန္-၄</span></a></p>
<h6><span style="color: #339966;">အနိစၥသုတၲန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0924-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အနိစၥသုတၲန္</span></a></p>
<h6><span style="color: #339966;">အဘိဏၰပစၥ၀ကိၡတဗၺသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0085-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏၰပစၥ၀ကိၡတဗၺသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0086-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏၰပဥၥ၀ကိၡတဗၺသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0087-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏၰပဥၥ၀ကိၡတဗၺသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0088-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏၰပဥၥ၀ကိၡတဗၺသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0089-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏွပစၥ၀ကၡိတဗၺသူတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0090-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏွပစၥ၀ကၡိတဗၺသူတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0091-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏွပစၥ၀ကၡိတဗၺသူတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0092-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏွပစၥ၀ကၡိတဗၺသူတၱန္(၄)</span></a></p>
<h6><span style="color: #339966;">အႆဇိသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0106-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဟိရာဇသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0192-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႆဇိသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0193-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႆဇိသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">အာတုမသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0858-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာတုမသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0859-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာတုမသုတၱန္(၂)</span></a></p>
<h6><span style="color: #339966;">အာဒိတၱသုတၱန္ တရားေတာ္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0926-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာဒိတၱသုတၱန္ တရားေတာ္</span></a></p>
<h6><span style="color: #339966;">အာသီဝိေသာပမာသုတၱန္ (၁)</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0020-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာသီဝိေသာပမာသုတၱန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0021-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာသီဝိေသာပမာသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0022-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာသီဝိေသာပမာသုတၱန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0023-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာသီဝိေသာပမာသုတၱန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0024-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာသီဝိေသာပမာသုတၱန္(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0025-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာသီဝိေသာပမာသုတၱန္(၆)</span></a></p>
<h6><span style="color: #339966;">ဧကာယနသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0452-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကာယနသုတၱန္(ဒုတိယပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0453-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကာယနသုတၱန္(ဒုတိယပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0454-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကာယနသုတၱန္(ဒုတိယပုိင္း)(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0455-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကာယနသုတၱန္(တတိယပုိင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0456-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကာယနသုတၱန္(တတိယပုိင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0457-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကာယနသုတၱန္(တတိယပုိင္း)(၃)</span></a></p>
<h6><span style="color: #339966;">ဧကၡဏသုတၱန္</span></h6>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0348-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧကၡဏသုတၱန္</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“က” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/35/007%20U%20Nyanissara%20D40-9-7-2001-%20KanDaSuTown.mp3"><span style="color: #ffcc00;">က႑ဆုေတာင္းခန္း (၉-၇-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0691-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကဆုန္လၿပည့္ဗုဒၶေန႔(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0692-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကဆုန္လၿပည့္ဗုဒၶေန႔(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0693-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကဆုန္လၿပည့္ဗုဒၶေန႔(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0716-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကဏွဆုေတာင္း-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0717-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကဏွဆုေတာင္း-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0285-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကတညဳတာ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0286-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကတညဳတာ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0761-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကတိယာနီ ဝတၳဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0762-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကတိယာနီ ဝတၳဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/026%2020021024%20KaTiYaNi.mp3"><span style="color: #ffcc00;">ကတိယာနီကုရရိကာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0972-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကထိန္အႏုေမာဒနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/008.mp3" target="_blank"><span style="color: #ffcc00;">ကထိန္ဓမၼသဘင္ အႏုေမာဒနာတရားေတာ္ (၃၁-၁၀-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/036%2020060902%20GanDarYaMinGyiEiThitSarTaYarSharPonTaw.mp3"><span style="color: #ffcc00;">ကႏၱာရမင္းၾကီး၏သစၥာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0933-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကမ ၻာ့အလွဆံုးတိုင္းျပည္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0934-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကမ ၻာ့အလွဆံုးတိုင္းျပည္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0917-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကမၻာ႔ဗုဒၶတကၠသိုလ္အဘိဓာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/003.mp3" target="_blank"><span style="color: #ffcc00;">ကရင္ျပည္နယ္မွၿငိမ္းခ်မ္းေရးတရားေတာ္ အပိုုင္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/074%2020080908%20KaRuNarDatASetMaPyatSayNelt.mp3"><span style="color: #ffcc00;">ကရုဏာဓါတ္အဆက္မျပတ္ေစနဲ႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/03/004%20U%20Nyanissara%20D3%208-3-1978%20KarMaZat.mp3"><span style="color: #ffcc00;">ကာမဇာတ္ တရား (၈-၃-၁၉၇၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/060%2020080308%20KarLaKaKarLaKoSarThi.mp3"><span style="color: #ffcc00;">ကာလက ကာလကိုယ္စားသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/16/004%20U%20Nyanissara%20D19%2016-1-1989%20KarLaTanBoe.mp3"><span style="color: #ffcc00;">ကာလတန္ဖိုး တရားေတာ္ (၁၆-၁-၁၉၈၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0771-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကာဠိဥရရကာတ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0772-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကာဠိဥရရကာတ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0759-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာဠီကုရရဂရိကာ ဝတၳဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0760-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာဠီကုရရဂရိကာ ဝတၳဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0298-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာေလနဓမၼသာကစၦာ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0299-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာေလနဓမၼသာကစၦာ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0287-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာေလနဓမၼသာဝန မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0288-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကာေလနဓမၼသာဝန မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0871-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကိသာေဂါတမီအပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0872-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကိသာေဂါတမီအပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0985-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကိႆ၀စဏရေသ့တရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0986-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကိႆ၀စဏရေသ့တရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0769-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကု႑လေကသီေထရီအပါဒါန္တရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0770-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကု႑လေကသီေထရီအပါဒါန္တရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0929-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုဒါလပ႑ိတဇာတ္ေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0200-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုဒါလပ႑ိတဇာတ္ႏွင့္သတိပဌါန္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0201-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုဒါလပ႑ိတဇာတ္ႏွင့္သတိပဌါန္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0202-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုဒါလပ႑ိတဇာတ္ႏွင့္သတိပဌါန္တရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0336-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုမ ၻာကာရဇာတ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0337-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုမ ၻာကာရဇာတ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0725-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုမုၿဒာေတြပြင့္တဲ့ည(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0726-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုမုၿဒာေတြပြင့္တဲ့ည(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0115-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုလသုတၱန္ႏွင့္ေကသ၀ဇာတ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0116-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုလသုတၱန္ႏွင့္ေကသ၀ဇာတ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0916-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ကုသိုလ္ဆိုတာဘာလဲ တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0658-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကာသတကၠီဝိမာနဝတၱဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0659-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကာသတကၠီဝိမာနဝတၱဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0471-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကာသလမင္း ဆင္ျခင္ရာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/45/003%20U%20Nyanissara%2026-Dec-2007.mp3"><span style="color: #ffcc00;">ေကာသလမင္းႀကီးရဲ႕ ေစာရႀကီးေတြ (၂၆-၁၀-၂၀၀၇) စင္ကာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/1009-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကံဏွဇာတ္ေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/1010-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကံဏွဇာတ္ေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0712-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကံဏွရေသ့ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0713-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကံဏွရေသ့ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0832-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကံျမင့္ဗုဒၶရတနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0738-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကံေကာင္းသူမ်ားတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0702-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကုိရင္ေလးေတြရဲ႔အသံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/26/005%20U%20Nyanissara%20D30%20KoeKawelChinNatBarTharTaYar.mp3"><span style="color: #ffcc00;">ကိုးကြယ္ၿခင္းႏွင္႔ဘာသာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/110%20KaungMu6Par.mp3"><span style="color: #ffcc00;">ေကာင္းမႈ ၆ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/37/002%20U%20Nyanissara%20D43-%20KongMhouKhuNitMyo.mp3"><span style="color: #ffcc00;">ေကာင္းမႈ(၇)မ်ိဳး တရာေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0833-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေကာင္းမႈ႔တန္ခိုးတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0834-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေကာင္းမႈ႔တန္ခိုးတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0928-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေကာင္းျခင္းသံုးျဖာေဒသနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0206-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကပ္ၾကီး(၃)ပါးတရားေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0207-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကပ္ၾကီး(၃)ပါးတရားေတာ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/16/003%20U%20Nyanissara%20D19%2021-4-1987%20KoKyintTayar.mp3"><span style="color: #ffcc00;">ကိုယ္က်င့္တရားေတာ္ (၂၁-၄-၁၉၈၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/111%20KoKyintTheitKharThiSinYeTharToeEiAYinAHnee%2020000209%20or%2020050209.mp3"><span style="color: #ffcc00;">ကိုယ္က်င့္သိကၡာသန္႕စင္သူတို႕၏အရင္းအႏွီး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0656-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ကိုယ္ေစာင့္တရားေလးပါးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/039%2020061104%20KoePaingNetKoeSarKyet.mp3"><span style="color: #ffcc00;">ကိုယ့္ပိုင္နက္ ကိုယ့္စားက်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0981-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်းဇူးတရားငါးပါး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0982-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်းဇူးတရားငါးပါး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0416-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်ာင္း၆၀ တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0417-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်ာင္း၆၀ တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0938-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်ာင္းတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0939-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်ာင္းတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0921-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေက်ာင္းအလွဴတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/002.mp3" target="_blank"><span style="color: #ffcc00;">ႀကီးက်ယ္ျမင့္ျမတ္ေသာမဟာသမယ</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“ခ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0448-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ခရီးသြားရျခင္းအက်ဳိးေက်းဇူး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0289-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ခႏၲီ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0290-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ခႏၲီ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0291-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ခႏၲီ မဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/079%2020081022%20KhanTi.mp3"><span style="color: #ffcc00;">ခႏၱီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0767-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ခုဇၨတၲရာဝတၴဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0768-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ခုဇၨတၲရာဝတၴဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0366-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ခုႏွစ္ေန႔ဗုဒၶ၀င္တရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0367-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ခုႏွစ္ေန႔ဗုဒၶ၀င္တရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0368-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ခုႏွစ္ေန႔ဗုဒၶ၀င္တရားေတာ္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0613-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ခ်မ္းသာသုခတရားေလးပါး (၁၁-၃-၁၉၉၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0318-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေခမံ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0319-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေခမံ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0320-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေခမံ မဂၤလာ(၃)</span></a></p>
<h5><span style="color: #00ffff;">“ဂ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><span style="color: #ff9900;"><a style="color: #ff9900;" href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/kayudamaFULLMOONDAYTAWTALIN.mp3">ဂ႐ုဓမၼတရားေတာ္</a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0855-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဂ႐ုဏာဘာဝနာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0856-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဂ႐ုဏာဘာဝနာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0857-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဂ႐ုဏာဘာဝနာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0667-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဂႏၻီရဥာဏ္ (၂၉-၃-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0276-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဂါရဝ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0277-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဂါရဝ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0278-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဂါရဝ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0112-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဂီလာနသုတၲန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0113-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဂီလာနသုတၲန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0727-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဂုဏ္ေပါင္းျခံဳလႊမ္းေက်ာင္းသခၤမ္းတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0728-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဂုဏ္ေပါင္းျခံဳလႊမ္းေက်ာင္းသခၤမ္းတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/061%2020080310%20GawTaMiPyawThawKanKaungThuMyar.mp3"><span style="color: #ffcc00;">ေဂါတမီေျပာေသာကံေကာင္းသူမ်ား</span></a></p>
<h5><span style="color: #00ffff;">“င” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/44/008%20UNyanissara%20NaKaungThuKaungMahOPE%205-11-2007.mp3"><span style="color: #ffcc00;">ငါေၾကာင့္ မဟုတ္၊ သူ႕ေၾကာင့္မဟုတ္ တရားေတာ္ (၅-၁၁-၂၀၀၇)</span></a></p>
<h5><span style="color: #00ffff;">“စ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/038%2020061012%20BiLoneHngetHnintSon.mp3"><span style="color: #ffcc00;">စကၠ၀တၱိသုတၱန္ – ၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/Singapore-19-9-15.mp3"><span style="color: #ffcc00;">စကၠဝတၱိသုတ္ – &nbsp;ခ်င္းျပည္နယ္အလွဴေတာ္ တရားပြဲ (စင္ကာပူ -၁၉.၉.၂၀၁၅)&nbsp;</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/024%2020020312%20SarLarHtayYi.mp3"><span style="color: #ffcc00;">စာလာေထရ္ရီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/049%2020071217%20SuLaPanHtaKaHtayRaAParDan.mp3"><span style="color: #ffcc00;">စူ႒ာ၀ဌာကေထရအပါဒါန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0184-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠပႏၱကေထရ္ရအပါဒါန္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0185-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠပႏၱကေထရ္ရအပါဒါန္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0927-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စူဠသုဘဒၵါဂုဏ္ရည္ျပတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0495-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">စိတၲသူၾကယ္အတၳဳပတၲိ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0496-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">စိတၲသူၾကယ္အတၳဳပတၲိ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0604-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စိတ္ကိုဆံုးမနည္း (၁၆-၁-၁၉၉၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/086%2020090426%20SatePyinNee.mp3"><span style="color: #ffcc00;">စိတ္ျပင္နည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0238-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စႏၵာဘေထရ္ရ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0239-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">စႏၵာဘေထရ္ရ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0608-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0609-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0853-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ(ကာကြယ္ၿခင္းငါးမ်ဳိး)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0854-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေစတိယပူဇာ(ကာကြယ္ၿခင္းငါးမ်ဳိး)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/056%2020080121%20CeTi4Par.mp3"><span style="color: #ffcc00;">ေစတီ ၄ပါး</span></a></p>
<h5><span style="color: #00ffff;">“ဆ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/096%2020091024%20SuTaungMaHmarSayNelt.mp3"><span style="color: #ffcc00;">ဆုေတာင္းမမွားေစနဲ႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0603-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဆြမ္းအႏုေမာဒနာ (ပုဏၰအမ်ိဳးသမီး) (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0605-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဆြမ္းအႏုေမာဒနာ (ပုဏၰာအမ်ိဳးသမီး) (၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“ဇ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/1008-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဇိနဒါနတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0294-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဇီ၀ကဝတၱဳတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0295-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဇီ၀ကဝတၱဳတရားေတာ္(၂)</span></a></p>
<h5><span style="color: #00ffff;">“ည” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/052%2020080105%20NyiNyutSwarKyintChinEiChanThar.mp3"><span style="color: #ffcc00;">ညီညြတ္စာက်င့္ျခင္း၏ခ်မ္းသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/034%2020060421%20NyiTawArNanDarYayKyiTawSetKhan_.mp3"><span style="color: #ffcc00;">ညီေတာ္ အာနႏၵာေရၾကည္ေတာ္ဆက္ခန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0266-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဥာတကာနဥၥသဂၤေဟာမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0267-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဥာတကာနဥၥသဂၤေဟာမဂၤလာ(၂)</span></a></p>
<h5><span style="color: #00ffff;">“တ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/023%2020010609%20KaHnaSuTaung.mp3"><span style="color: #ffcc00;">တဏွာဆုေတာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/13/001%20U%20Nyanissara%20D16%2027-6-1980%20TaPaMinGaLar.mp3"><span style="color: #ffcc00;">တပ မဂၤလာ (၂၇-၆-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/25/004%20U%20Nyanissara%20D29%20TaPhoatThaNatBaLiKaNyiNaung%2019-11-1980.mp3"><span style="color: #ffcc00;">တဖုႆႏွင့္ ဘလိကညီေနာင္ (၁၉-၁၁-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/089%2020090624%20TaYarNarYaChinThiKanKaungThi.mp3"><span style="color: #ffcc00;">တရားနာရျခင္းသည္ ကံေကာင္းသည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0797-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">တရားအက်ဥ္းခ်ဳပ္-၄ပါး (၂-၁၁-၂၀၀၃ Singapore)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0321-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တိရိယပါပၸဒေထရအပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0322-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တိရိယပါပၸဒေထရအပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0323-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တိရိယပါပၸဒေထရအပါဒါန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0948-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တိႆ သာမေဏတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0949-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တိႆ သာမေဏတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/084%2020090126%20TaitPweNeltAungPwe.mp3"><span style="color: #ffcc00;">တိုက္ပြဲႏွင့္ ေအာင္ပြဲ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/075%2020080910%20TinMarHmuTwayKoMyitTarPhyintShawtPar.mp3"><span style="color: #ffcc00;">တင္းမာမႈအေ၀းကိုေရႊ႕ပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/066%2020080721%20TaKhuTiThawLan.mp3"><span style="color: #ffcc00;">တစ္ခုတည္းေသာလမ္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0472-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တန္ဖိုး႐ွိေသာေလးဂါထာ တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0473-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">တန္ဖိုး႐ွိေသာေလးဂါထာ တရား(၂)</span></a></p>
<h5><span style="color: #00ffff;">“ထ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/046%2020071104%20HtanPinNgote%282%29.mp3" target="_blank"><span style="color: #ffcc00;">ထန္းပင္ငုတ္ တရားေတာ္</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/042%2020070306%20HtayRaWarDaMateSet.mp3"><span style="color: #ffcc00;">ေထရ၀ါဒမိတ္ဆက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0701-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒ သဂၤါယနာတင္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0519-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒဓမၼေအာင္လံတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0520-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒဓမၼေအာင္လံတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0521-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒဓမၼေအာင္လံတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0700-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒနိဒါန္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0687-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒမိတ္ဆက္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0688-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေထရဝါဒမိတ္ဆက္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/019%2019980116%20MayYiWotut-SaitPyuPyanNaeeTayar.mp3"><span style="color: #ffcc00;">ေထရီ၀တၳဳစိတ္ျပဳျပင္နည္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0709-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေထရ္ရဝါဒ (၂၆-၁-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/046%2020071104%20HtanPinNgote%282%29.mp3"><span style="color: #ffcc00;">ထန္းပင္ငုတ္တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0718-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ထုတ္ျပန္ျခင္းႏွင္႔ ဆြဲေဆာင္ျခင္း တရားေတာ္ (၂-၆-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/109%20Expression_Impression.mp3"><span style="color: #ffcc00;">ထုတ္ျပျခင္းႏွင့္ ေဖာ္ျပျခင္း</span></a></p>
<h5><span style="color: #00ffff;">“ဒ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0117-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဒကၡိဏဝိသုဒၶိေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0142-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါန(၃)ပါးတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0143-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါန(၃)ပါးတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0614-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါနကထာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0615-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါနကထာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/22/008%20U%20Nyanissara%20D25%20DarNaTheSitTypeYaTarHtetThe.mp3"><span style="color: #ffcc00;">ဒါနသည္စစ္တိုက္ရသည္ ထက္ခက္၏</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/02/002%20U%20Nyanissara%20D2%2020-11-1977%202pm%20DarNaAhNuMorDaNarKaHtar.mp3"><span style="color: #ffcc00;">ဒါနအႏုေမာဒနာကထာ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0261-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါနဥၥမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0262-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒါနဥၥမဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/051%2020080104%20DoteKhaEiLutMyawtYar.mp3"><span style="color: #ffcc00;">ဒုကၡ၏လြတ္ေျမာက္ရာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0885-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဒုလႅဘတရား(၅)ပါး</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“ဓ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0628-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဓမၼကထာ တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/058%2020080215%20DhammaKaHtiKaMaLayEiGonYay.mp3"><span style="color: #ffcc00;">ဓမၼကထိကမေလး၏ဂုဏ္ရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0264-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဓမၼစရိယမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0265-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဓမၼစရိယမဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0485-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼတန္ဘိုးတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0486-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼတန္ဘိုးတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0487-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼတန္ဘိုးတရားေတာ္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0439-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဒီပတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0440-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဒီပတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0739-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဒူတ ကိုး႒ာန (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0740-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဒူတ ကိုး႒ာန (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0741-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဒူတ ကိုး႒ာန (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0841-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼပူဇာတရား (ငါးက်မ္းျပန္)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0842-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼပူဇာတရား (ငါးက်မ္းျပန္)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0263-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼပူဇာေဒသနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0735-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼရတနာပူဇာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/10/003%20U%20Nyanissara%20D13%2029-4-1980%20DahmmaSaReeYa.mp3"><span style="color: #ffcc00;">ဓမၼာစရိယ (၂၉-၄-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0007-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼာဒါသ တရားေၾကးမံု (၁၁-၅-၁၉၇၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0601-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဳပေဒသဓမၼလမ္းညႊန္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0801-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဓမၼဳေဒၵသတရား(၄)ပါး (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0802-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဓမၼဳေဒၵသတရား(၄)ပါး (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0860-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဳေဒသေလးပါးတရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0861-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼဳေဒသေလးပါးတရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0935-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼေအာင္လံတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0936-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼေအာင္လံတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0937-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓမၼေအာင္လံတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0329-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓါတုဝိဘဇၨနတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0330-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓါတုဝိဘဇၨနတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0331-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဓါတုဝိဘဇၨနတရားေတာ္(၃)</span></a></p>
<h5><span style="color: #00ffff;">“န” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/080%2020081104%20NateBanSharNee.mp3" target="_blank"><span style="color: #ffcc00;">နိဗၺာန္ရွာနည္း တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0789-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နကုလမာတာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0790-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နကုလမာတာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/1011-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိကာယ္ၾသဝါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0074-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိဂ႑နာဋပုတၱဒိ႒ိ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0075-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိဂ႑နာဋပုတၱဒိ႒ိ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0531-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိဓိက႑တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0532-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိဓိက႑တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0351-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိဗၺာနပဥွာသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0352-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိဗၺာနပဥွာသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0308-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိဗၺာနသစၦိကိရိယာစ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0309-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိဗၺာနသစၦိကိရိယာစ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0310-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိဗၺာနသစၦိကိရိယာစ မဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/080%2020081104%20NateBanSharNee.mp3"><span style="color: #ffcc00;">နိဗၺာန္ရွာနည္း တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0186-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိယာမတရားႏွင့္အနတၱတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0187-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နိယာမတရားႏွင့္အနတၱတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0279-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိဝါတ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0280-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိဝါတ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0281-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိဝါတ မဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0082-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိေၿဂာဓ သာမေဏ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0083-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိေၿဂာဓ သာမေဏ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0084-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">နိေၿဂာဓ သာမေဏ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0976-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေန႕စဥ္သံုးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0554-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေနနည္း၃ပါးတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0555-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေနနည္း၃ပါးတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/113%20NaingGanPaingYaTaNrMyarSauntShoutYay.mp3"><span style="color: #ffcc00;">ႏိုင္ငံပိုင္ရတနာမ်ားေစာင့္ေရွာက္ေရး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0510-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">နတၱဓိဇာတ္ေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/062%2020080313%20NatPyayYawtKyaungKaungHmu.mp3"><span style="color: #ffcc00;">နတ္ျပည္ေရာက္ေၾကာင္းေကာင္းမႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0883-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေနာက္ဆုံးဆယ္လျမတ္ဗုဒၶ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0884-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေနာက္ဆုံးဆယ္လျမတ္ဗုဒၶ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0830-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေႏြဦးတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0831-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေႏြဦးတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/064%2020080422%20HnitHaungHnitThitThoneThatChet.mp3"><span style="color: #ffcc00;">ႏွစ္ေဟာင္းႏွစ္သစ္သံုးသပ္ခ်က္</span></a></p>
<h5><span style="color: #00ffff;">“ပ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/001.mp3" target="_blank"><span style="color: #ffcc00;">ပုုဂံၿမိဳ႕ ဇဗၼဴဒီပဗိမာန္မွာေဟာၾကားေတာ္မူခဲ့ေသာတရားေတာ္ (၀၁-၁၀-၂၀၁၆)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0055-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတ သာမေဏ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0056-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတ သာမေဏ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0223-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတာနဥၥေသဝနာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0224-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတာနဥၥေသဝနာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0225-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတာနဥၥေသဝနာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0226-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတာနဥၥေသဝနာ(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0227-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပ႑ိတာနဥၥေသဝနာ(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0078-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပကုဋကစ ၦာရနဒိ႒ိတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0079-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပကုဋကစ ၦာရနဒိ႒ိတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0668-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပညာကထာ တရား (၃-၄-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0710-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပညာမပါပြဲမျဖစ္ဘူး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0711-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပညာမပါပြဲမျဖစ္ဘူး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/020%2020000101%20PyinNyarShiParHmaPwePhyitThi.mp3"><span style="color: #ffcc00;">ပညာရွိပါမွပြဲျဖစ္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0011-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပဋိကူလမနသီကာရတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0012-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပဋိကူလမနသီကာရတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0013-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပဋိကူလမနသီကာရတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0942-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0943-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပဋိစၥသမုပၸါဒ္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0230-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပတိ႐ူပေဒသ၀ါေသာစ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0231-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပတိ႐ူပေဒသ၀ါေသာစ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0232-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပတိ႐ူပေဒသ၀ါေသာစ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/021%2020000329%20PaBitZaMinGaLar.mp3"><span style="color: #ffcc00;">ပဗၺဇၨမဂၤလာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0638-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပမာဒႏွင့္အပၸမာဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/28/008%20U%20Nyanissara%20D32%20PaYeatNateBanNatNateBanNa.mp3"><span style="color: #ffcc00;">ပရိနိဗၺာန္ႏွင့္နိဗၺာန္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0960-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပရိတၱတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0961-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပရိတၱတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0543-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပဥၥၥကၠဒါယကာဝတၱဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0742-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါတဠိပုတ္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0743-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါတဠိပုတ္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0240-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပါနိယဒါနွင့္သိပၸဥၥ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0241-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပါနိယဒါနွင့္သိပၸဥၥ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0242-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပါနိယဒါနွင့္သိပၸဥၥ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0904-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပါနိယဒါနွင့္သိပၸဥၥ(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0905-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပါနိယဒါနွင့္သိပၸဥၥ(၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0918-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါရမီ(၁၀)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0539-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပါေဝယကဆင္ၾကီးဥပမာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0256-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပုတၲဒါရႆသဂၤဟ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0257-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပုတၲဒါရႆသဂၤဟ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0258-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပုတၲဒါရႆသဂၤဟမဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0067-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပုေဏၰာဝါဒသုတၲန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0233-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပုေဗၺစကတပုညတာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0234-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပုေဗၺစကတပုညတာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0150-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပူဇနိယမဂၤလာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0228-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပူဇာစပူဇနိယ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0229-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ပူဇာစပူဇနိယ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0063-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပူရဏကႆဖတိတၴိၾကီး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0064-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ပူရဏကႆဖတိတၴိၾကီး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/035%2020060607%20PuZawHtikeThuKoPuZawChin.mp3"><span style="color: #ffcc00;">ပူေဇာ္ထိုက္သူကိုပူေဇာ္ျခင္း</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“ဖ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0641-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဖႏၵနဇာတ္ေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0642-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဖႏၵနဇာတ္ေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0176-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဖႏၵနသုတၱန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0177-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဖႏၵနသုတၱန္(၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“ဗ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0952-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗဟုပုတၱိကာေသာဏာေထရီအပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0954-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗဟုပုတၱိကာေသာဏာေထရီအပါဒါန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0953-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗဟုပုတၱိကေသာဏာေထရီအပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0515-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗဟုႆုတ ပေစၥက ဗုဒၶ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0514-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗဟႆုတ ပေစၥက ဗုဒၶ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0506-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာကုလ ဝတၳဳ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0507-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာကုလ ဝတၳဳ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/054%2020080112%20BarLaPanDiTaMateSet.mp3"><span style="color: #ffcc00;">ဗာလပ႑ိတမိတ္ဆက္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0508-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာဟိယအလုပ္ေပးတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0509-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာဟိယအလုပ္ေပးတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0235-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာဟုသစၥဥၥ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0236-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာဟုသစၥဥၥ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0237-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗာဟုသစၥဥၥ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0990-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေဗာဓိပူဇာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/007.mp3" target="_blank"><span style="color: #ffcc00;">ဗုဒၶစာေပမွ ေတြ႕ရွိရေသာေရွးေခတ္ေဟာင္းပါလီမန္ ဒီမိုကေရစီစနစ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/006.mp3" target="_blank"><span style="color: #ffcc00;">ဗုဒၶ ဓမၼတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0894-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶ၊ဓမၼ၊သံဃာ႕ လမ္းညႊန္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0895-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶ၊ဓမၼ၊သံဃာ႕ လမ္းညႊန္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0441-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶခရီးစဥ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0442-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶခရီးစဥ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0443-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶခရီးစဥ္ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0848-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶတရားေတာ္ႏွင့္ကမ ၻာ့ျငိမ္းခ်မ္းေရးတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0849-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶတရားေတာ္ႏွင့္ကမ ၻာ့ျငိမ္းခ်မ္းေရးတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0850-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶတရားေတာ္ႏွင့္ပညာေရး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0851-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶတရားေတာ္ႏွင့္ပညာေရး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0852-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶတရားေတာ္ႏွင့္ပညာေရး (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0533-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶဓမၼတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0534-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶဓမၼတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/009%20U%20Nyanissara%20D26%20BuddhaDhammaAhKyineChoke.mp3"><span style="color: #ffcc00;">ဗုဒၶဓမၼအက်ဥ္းခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0579-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶၿဖစ္စဥ္ႏွင့္ဓမၼၿဖစ္စဥ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0580-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶၿဖစ္စဥ္ႏွင့္ဓမၼၿဖစ္စဥ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0581-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶၿဖစ္စဥ္ႏွင့္ဓမၼၿဖစ္စဥ္ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0930-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာအစအမွန္သိျမင္ျခင္းက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/20/001%20U%20Nyanissara%20D23%2031-5-2000%20BuddhaBaThar-AhChayKhan.mp3"><span style="color: #ffcc00;">ဗုဒၶဘာသာအေျခခံတရား (၃၁-၅-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0359-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဘိေသကမဂၤလာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0360-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶဘိေသကမဂၤလာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/25/005%20U%20Nyanissara%20D29%20BuddhaBeatThayKaMinGaLar%208-2-1981.mp3"><span style="color: #ffcc00;">ဗုဒၶဘိေသကမဂၤလာ (၂၈-၂-၁၉၈၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/19/008%20U%20Nyanissara%20D22%2031-5-2000%205pm%20BuddhaWarDe.mp3"><span style="color: #ffcc00;">ဗုဒၶဝါဒီတရားေတာ္ (၃၁-၅-၂၀၀၀ ညေန ၆နာရီ)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0843-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာကာာကြယ္ေစာင့္ေ႐ွာက္ေရး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0844-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာကာာကြယ္ေစာင့္ေ႐ွာက္ေရး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0909-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶသာသနာၿပန္႔ပြါးေရး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0910-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶသာသနာၿပန္႔ပြါးေရး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0616-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာအက်ဥ္းခ်ဳပ (ပထမပိုင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0617-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာအက်ဥ္းခ်ဳပ္(ဒုတိယပိုင္း) (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0618-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာအက်ဥ္းခ်ဳပ္ (ဒုတိယပိုင္း)(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0619-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာအက်ဥ္းခ်ဳပ္ (ဒုတိယပိုင္း)(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0620-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာအက်ဥ္းခ်ဳပ္ (ဒုတိယပိုင္း)(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0840-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶသာသနာေတာ္တိုးတက္ေရး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0752-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶအသံတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0753-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶအသံတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0754-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗုဒၶအသံတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/040%2020061222%20BuddhaNoteThaTiBarWaNar.mp3"><span style="color: #ffcc00;">ဗုဒၶါနႆာတိသာသနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0444-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶႏုႆတိဘာဝနာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0445-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဗုဒၶႏုႆတိဘာဝနာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0643-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗႏၶနဇာတ္ေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0644-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗႏၶနဇာတ္ေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0203-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗ်ုုသနတရား(၅)ပါးတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0204-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗ်ုုသနတရား(၅)ပါးတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0205-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဗ်ုုသနတရား(၅)ပါးတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/18/002%20U%20Nyanissara%20D21%2013-12-1996%20ByanMaSarYaSutta.mp3"><span style="color: #ffcc00;">ျဗဟၥစါရသုတၲန္ တရားေတာ္ (၁၃-၁၂-၁၉၉)</span></a><br>
<a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0303-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ၿဗဟၼစရိယ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0304-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ၿဗဟၼစရိယ မဂၤလာ(၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“ဘ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/Singapore-20-9-15.mp3" target="_blank"><span style="color: #ffcc00;">ဘဝ၏အေျခခံအုတ္ျမစ္တရားေတာ္ (စင္ကာပူ – ၂၀.၉.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/094%2020090925%20BaWaKoANyiAHmyaShu.mp3"><span style="color: #ffcc00;">ဘ၀ကိုအညီအမွ်ရႈ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/047%2020071202%20BaWaSiMeeTaing.mp3"><span style="color: #ffcc00;">ဘ၀ဆီမီးတိုင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/018%2019960113%20BaWaYeeYwalChet3Myo.mp3"><span style="color: #ffcc00;">ဘ၀ရည္ရြယ္ခ်က္သံုးမ်ိဳး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/003%2019781031%20BuddaWetGiNaungNyi3Gyate.mp3"><span style="color: #ffcc00;">ဘဒၵ ၀ဂၢီညီေနာင္သံုးက်ိပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0093-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဘဒၵ၀ဂၢီညီေနာင္သုံးက်ိပ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0094-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဘဒၵ၀ဂၢီညီေနာင္သုံးက်ိပ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/24/004%20U%20Nyanissara%20D28%20BetGaWedGeeNaungNyiThongCha-31-10-1978.mp3"><span style="color: #ffcc00;">ဘဒၵ၀ဂၢီေနာင္ညီသုံးက်ိပ္ (၃၁-၁၀-၁၉၇၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/Singapore-20-9-15.mp3"><span style="color: #ffcc00;">ဘဝ၏အေျခခံအုတ္ျမစ္တရားေတာ္ (စင္ကာပူ – ၂၀.၉.၂၀၁၅)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0141-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဘဝတန္ဘိုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/001%20U%20Nyanissara%20D42-BarPayYinBarYaMaLae.mp3"><span style="color: #ffcc00;">ဘာေပးရင္ဘာရမလဲ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/083%2020090113%20BateKhuNiASaGawTaMiKa.mp3"><span style="color: #ffcc00;">ဘိကၡဳနီအစ ေဂါတမီက</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0654-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဘိကၡဳအပရိဟာနိယ(၇)ပါး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0655-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဘိကၡဳအပရိဟာနိယ(၇)ပါး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0549-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘုရားအဆူဆူတို႔၏အထာကတာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0550-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘုရားအဆူဆူတို႔၏အထာကတာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0546-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘုရားအဆူဆူတုိ႕သာသနာသံုးရပ္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0547-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘုရားအဆူဆူအဆံုးအမတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0606-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘုန္းကံၾကီးသူတုိ႔အတြက္သာသနာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0607-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဘုန္းကံၾကီးသူတုိ႔အတြက္သာသနာ(၂)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“မ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0540-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မေမ့အပ္တဲ့ေလးဌာနတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0446-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မရဏသတိကထာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0447-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မရဏသတိကထာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0870-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဟာသက်မုနိတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0061-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မကၡၡလိေဂါသာလဒိ႒ိတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0573-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မာဃဇာတ္ေတာ္ (အပၸမာဒ) (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0574-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မာဃဇာတ္ေတာ္ (အပၸမာဒ) (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0253-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မာတာပီတုဥပ႒ာနံ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0254-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မာတာပီတုဥပ႒ာနံ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0255-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မာတာပီတုဥပ႒ာနံ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0582-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မိလိႏၵႏွင္႔အသွ်င္နာဂေသန</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0576-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မီးကြင္းသစၥာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0672-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မူလပရိယာယတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0673-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မူလပရိယာယတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0689-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မူလပရိယာယတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0715-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မူလပရိယာယသုတၱန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0602-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမဃိယဝတၳဳ (စိတ္ျပဳျပင္နည္း) တရားေတာ္ (၁၆-၁-၁၉၉၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0478-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၲာစြမ္းရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0636-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၲာဘာဝနာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0637-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၲာဘာဝနာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/19/009%20U%20Nyanissara%20D22%2031-5-2000%20Metta%20AhNhitChoke.mp3"><span style="color: #ffcc00;">ေမတၲာအႏွစ္ခ်ဳပ္တရားေတာ္ (၃၁-၅-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0647-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာစြမ္းရည္ႏွင့္သုပူတိေထရ္ရအပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0648-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာစြမ္းရည္ႏွင့္သုပူတိေထရ္ရအပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0488-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/112%20MyitTarTaYar%20SweTaw.mp3"><span style="color: #ffcc00;">ေမတၱာတရားစြယ္ေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0697-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာတရားပြါးမ်ားနည္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0698-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာတရားပြါးမ်ားနည္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/078%2020081015%20MyitTarParRaMi.mp3"><span style="color: #ffcc00;">ေမတၱာပါရမီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/081%2020081110%20MyitTarChoneHmaLoneLaneMyi.mp3"><span style="color: #ffcc00;">ေမတၱာျခံဳမွလံုလိမ့္မည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0694-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေမတၱာအက်ိုဳးျပတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/076%2020080911%20MyitTarHnintPyinNyar.mp3"><span style="color: #ffcc00;">ေမတၱႏွင့္ပညာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0062-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မကၡၡလိေဂါသာလဒိ႒ိတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/043%2020070506%20Meggin8Par.mp3"><span style="color: #ffcc00;">မဂၢင္ ၈ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0465-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢဧကာယနႏွင့္နတံုမွာကာပိမာတာဝတ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0466-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢဧကာယနႏွင့္နတံုမွာကာပိမာတာဝတ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0467-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢဧကာယနႏွင့္နတံုမွာကာပိမာတာဝတ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0458-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢဧကာယနႏွင့္သဘာဝဓမၼ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0459-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢဧကာယနႏွင့္သဘာဝဓမၼ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0460-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဂၢဧကာယနႏွင့္သဘာဝဓမၼ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/006%20U%20Nyanissara%20D42-MitSaYeatYaThoutTan.mp3"><span style="color: #ffcc00;">မစၦရိယသုတၱန္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/091%2020090808%20MyitZiMaPaDiPaDar.mp3"><span style="color: #ffcc00;">မဇၥ်ိမပဋိပဒါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0274-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဇၨပါနာသံယေမာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0275-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">မဇၨပါနာသံယေမာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0538-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မဥၨိမဂုဏ္ရည္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0845-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မ်က္ေမွာက္ေခတ္ကမ ၻာ့အေျခအေနႏွင့္ဗုဒၶတရားေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0846-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မ်က္ေမွာက္ေခတ္ကမ ၻာ့အေျခအေနႏွင့္ဗုဒၶတရားေတာ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0847-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">မ်က္ေမွာက္ေခတ္ကမ ၻာ့အေျခအေနႏွင့္ဗုဒၶတရားေတာ္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0551-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၵ၏ေမတၱာတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0552-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၵ၏ေမတၱာတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0893-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ဘ၀လမ္းညႊန္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/22/005%20U%20Nyanissara%20D25%2010-10-2003%20MyatBuddhaEiWarKyutMaintKhon.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ ဝါကြ်တ္မိန္႔ခြန္း (၁၀-၁၀-၂၀၀၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/34/005%20U%20Nyanissara%20D39-%2011-12-1994%20-MyatBuddhaEiSwonYeePya.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏စြမ္းရည္ျပ (၁-၁၂-၁၉၉၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0796-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ဝါကြၽတ္မိန္႔ခြန္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/022%2020001213%20MyatBuddhaEiHtayYaWaDa.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶ၏ေထရ္ရ၀ါဒ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0731-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶခ်ီးမႊမ္းသည္႔ေကာင္းမႈတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0732-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶခ်ီးမႊမ္းသည္႔ေကာင္းမႈတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/20/004%20U%20Nyanissara%20D23%208-5-2001%20History%20Of%20Myat%20Buddha%201.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာ့ သမိုင္းတရားေတာ္(၁) (၈-၅-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/20/005%20U%20Nyanissara%20D23%2011-5-2001%20History%20Of%20Myat%20Buddha%202.mp3"><span style="color: #ffcc00;">ျမတ္ဗုဒၶသာသနာ့ သမိုင္းတရားေတာ္(၂) (၁၁-၅-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/37/007%20U%20Nyanissara%20D43-MyatPhaYarShweTeatGone.mp3"><span style="color: #ffcc00;">ျမတ္ဘုရားေရႊတဂုံ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0707-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ၿမတ္ဗုဒၶ၏ေထရ္ရဝါဒ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0708-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ၿမတ္ဗုဒၶ၏ေထရ္ရဝါဒ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0799-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ၿမတ္ဗုဒၶသရီပူဇာတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0800-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ၿမတ္ဗုဒၶသရီပူဇာတရား (၂)</span></a></p>
<h5><span style="color: #00ffff;">“ရ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0479-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရတနာငါးမ်ိဳးႏွင့္ဝိဟာရအာႏုေမာဒနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/053%2020080109%20YaTaNarMoe%20ShweBo.mp3"><span style="color: #ffcc00;">ရတနာမိုး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0838-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရတနာသံုးပါးတန္ခိုးတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0839-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရတနာသံုးပါးတန္ခိုးတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/1007-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရသေဘာဂဝတၱဏတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0575-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ရဟန္းတပါး၏တန္ဘုိးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0625-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရဟန္းတို႔၏ေအာင္လံတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0919-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရာဟုလာသုတၲန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/44/001%20UNyannssara-YarZorWarDaMinKyintTaYarSalPar%281%29.mp3"><span style="color: #ffcc00;">ရာေဇာဝါဒ (မင္းက်င္႔တရား၁၀ပါး) ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/44/002%20UNyannssara-YarZorWarDaMinKyintTaYarSalPar%282%29.mp3"><span style="color: #ffcc00;">ရာေဇာဝါဒ (မင္းက်င္႔တရား၁၀ပါး) ၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0553-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရာဇမလႅမင္းသား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0080-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေရာဟိနိမင္းသမီး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0081-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေရာဟိနိမင္းသမီး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0940-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရုကၡဓမၼဇာတ္ေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0941-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရုကၡဓမၼဇာတ္ေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0610-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ရွင္မဟာကႆဖမေထရ္၀ထၳဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0969-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရွင္ျပဳေမာဒနာတရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0970-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ရွင္ျပဳေမာဒနာတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0649-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">႐ွင္ရဟန္းတို႔၏ဂုဏ္ရည္္ျပ (မုနိသုတၱန္)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/15/001%20U%20Nyanissara%20D18%2029-10-1981%20ShweOweMhoutTaYar.mp3"><span style="color: #ffcc00;">ေ႐ႊအုိးျမဳပ္တရား (၂၉-၁၀-၁၉၈၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0511-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေ႐ႊေစတီဝတၱဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0512-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေ႐ႊေစတီဝတၱဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0964-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရႊဥမင္ဆရာေတာအႏၱိမပူဇာေရစက္ခ်တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0333-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရႊဥျမွဳပ္တရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0334-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရႊဥျမွဳပ္တရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0335-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေရႊဥျမွဳပ္တရားေတာ္(၃)</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“လ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0657-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">လတုကိကဇာတ္ေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0705-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">လတုကိကဇာတ္ေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0706-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">လတုကိကဇာတ္ေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0890-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">လသာတုန္းဗုိင္းငင္္္္တရားေတာ္္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0623-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">လာဇာေဒ၀ဒီတာဝတၱဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0624-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">လာဇာေဒ၀ဒီတာဝတၱဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/44/005%20UNyannssara-LakeKhaLayLoNayPar-17-09-2007.mp3"><span style="color: #ffcc00;">လိပ္ကေလးလိုေနပါ ၁၇-၉-၂၀၀၇</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/044%2020070917%20LateNeltTuAungNayPar.mp3"><span style="color: #ffcc00;">လိပ္နဲ႕တူေအာင္ေနပါ</span></a><br>
<a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0529-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">လူတို႔၏က်င့္ဝတ္တရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0530-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">လူတို႔၏က်င့္ဝတ္တရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/45/001%20UNyanissara%20LuMikeToatEiThoarYarLan-13-10-2007.mp3"><span style="color: #ffcc00;">လူမိုက္တို႔သြားရာလမ္း ၁၃-၁၀-၂၀၀၇</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/45/002%20U%20Nyanissara%2025-Dec-2007.mp3"><span style="color: #ffcc00;">လူမိုက္ေတြကိုပဲ စည္းရုံးလို႔ ေနေတာ့မယ္ (၂၅-၁၀-၂၀၀၇) စင္ကာပူ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/092%2020090922%20LuWiNee.mp3"><span style="color: #ffcc00;">လူ႕၀ိနည္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/35/003%20U%20Nyanissara%20D40-2-12-1999%20-LuBaWaAhDatePel.mp3"><span style="color: #ffcc00;">လူ႕ဘ၀အဓိပၸါယ္ (၂-၁၂-၁၉၉၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/17/006%20U%20Nyanissara%20D21%2016-4-1997%20AhMyatTaYar-LayPa.mp3"><span style="color: #ffcc00;">ေလးပါး တရားေတာ္(၁၆-၄-၁၉၉၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/37/005%20U%20Nyanissara%20D43-LawKaEatThaBall%202-10-2004.mp3"><span style="color: #ffcc00;">ေလာက၏သေဘာ (၂-၁၀-၂၀၀၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0862-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေလာကဓမၼတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0863-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေလာကဓမၼတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0311-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေလာကဓမၼနကမၸတိမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0312-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေလာကဓမၼနကမၸတိမဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/037%2020060929%20LawKaMyetLoneTaSuKwalPyawtChin.mp3"><span style="color: #ffcc00;">ေလာကမ်က္လံုးတစ္စံုကြယ္ေပ်ာက္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0959-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေလာကအေျကာင္းတရားေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0837-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေလာကအေၾကာင္းတရားေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0148-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေလာဟကုမ ီၻဇာတ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0149-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေလာဟကုမ ီၻဇာတ္(၂)</span></a></p>
<h5><span style="color: #00ffff;">“၀” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0744-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">၀ဇီယာေထရ္ရီ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0745-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">၀ဇီယာေထရ္ရီ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0484-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝိဒကဘဒၵဇာတ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/005.mp3" target="_blank"><span style="color: #ffcc00;">၀ံသကလီရပေစၥကဗုဒၶ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0246-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိနယသုသိကၡိတ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0247-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိနယသုသိကၡိတ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0316-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိရဇံ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0317-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဝိရဇံ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0779-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝိသာခါဝတၴဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0780-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝိသာခါဝတၴဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/37/003%20U%20Nyanissara%20D43-WeatHarYaAhNuMawDaNar.mp3"><span style="color: #ffcc00;">ဝိဟာရအႏုေမာဒနာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0798-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝိဟာရေနနည္းသုံးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0660-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝိဇၨာႏွင္႔စရဏတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0661-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဝိဇၨာႏွင္႔စရဏတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0577-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">၀ဋ္တကဇာတ္ေတာ္တရား</span></a></p>
<p>&nbsp;</p>
<h5><span style="color: #00ffff;">“သ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><span style="color: #ffcc00;"><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%20-%20%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f%3f.mp3"><span style="color: #ffcc00;">သာသနာကြယ္ေၾကာင္း တရားအေပါင္း</span></a></span></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0696-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သရဏဂံုအေျခခံ တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/20/006%20U%20Nyanissara%20D23%2023-5-2001%20ThaRaNaGoneThonePar.mp3"><span style="color: #ffcc00;">သရဏဂုံ(၃)ပါးတရားေတာ္ (၂၃-၅-၂၀၀၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/095%2020090930%20ThaDiPaHtan.mp3"><span style="color: #ffcc00;">သတိပဌာန္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0639-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သေမၼာဒမာနဇာတ္ေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0640-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သေမၼာဒမာနဇာတ္ေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0560-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဟသဟာရ “၄” ဂါထာတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0561-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဟသဟာရ “၄” ဂါထာတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0562-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဟသဟာရ “၄” ဂါထာတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0160-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဟသာရဟဂါထာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0065-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဥဏယေဗလ႒ဒိ႒ိတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0066-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဥဏယေဗလ႒ဒိ႒ိတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/063%2020080405%20TharMeggiThuKha.mp3"><span style="color: #ffcc00;">သမဂၢိသုခ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/073%2020080824%20ThaYetPinAwtKaKhanTi.mp3"><span style="color: #ffcc00;">သရက္ပင္ေအာက္က ခႏၱီ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0695-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သရဏဂံုအေျခခံ တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0296-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာမဏာနဥၥဒႆနံ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0297-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာမဏာနဥၥဒႆနံ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0785-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာမာဝတီဝတၴဳ – ၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0786-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာမာဝတီဝတၴဳ -၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0597-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာမေဏေက်ာ္ေလးပါး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0598-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာမေဏေက်ာ္ေလးပါး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0971-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာရသံုးပါးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0556-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာ၏အက်ဥ္းခ်ဳပ္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0557-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာ၏အက်ဥ္းခ်ဳပ္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0385-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာကြယ္ေၾကာင္းတရားအေပါင္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0386-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာကြယ္ေၾကာင္းတရားအေပါင္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0988-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာျပဳေမတၱာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0911-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သာသနာသံုးရပ္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0548-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာသံုးရပ္အက်ဥ္းခ်ဳပ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0962-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာေတာ္ၾကီးပြားေၾကာင္းတရား (၇)ပါး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0963-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သာသနာေတာ္ၾကီးပြားေၾကာင္းတရား (၇)ပါး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0765-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သိ႒ဓမၼအၿမတ္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0766-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သိ႒ဓမၼအၿမတ္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/028%2020021026%20ThitHtaDhammaPuZar.mp3"><span style="color: #ffcc00;">သိဌာဓမၼပူဇာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0899-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သိႀကားမင္း၏ခႏၲီစာတမ္း(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0900-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သိႀကားမင္း၏ခႏၲီစာတမ္း(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0664-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သီလကထာ တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0703-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီလတန္ဖိုးျပတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0704-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီလတန္ဖိုးျပတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/35/004%20U%20Nyanissar%20D40-%2019-5-2000%20-%20ThiLaThiLuTharTieToatEiBaWaTaYar.mp3"><span style="color: #ffcc00;">သီလသည္ လူသားတိုင္းတို႕၏ဘ၀ တရား (၁၉-၅-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0973-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီလအက်ိဳးျပတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0805-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီလႏွင့္ပညာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0662-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သီလႏွင္႔ပညာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0663-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သီလႏွင္႔ပညာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0528-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီဟပေစၥကဗုဒၶတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0525-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီဟပေစၥကဗုဒၶတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0526-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သီဟပေစၥကဗုဒၶတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0114-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သုခ(၄)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0541-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုခေလးပါးႏွင့္ဓမၼတန္ဖိုးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0542-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုခေလးပါးႏွင့္ဓမၼတန္ဖိုးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0763-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဇာတာဝတၴဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0764-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဇာတာဝတၴဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0338-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဇာတာဥပါသိကာတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0339-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဇာတာဥပါသိကာတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0989-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုတၱဗုဒၶပူဇာတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/030%2020030227%20ThotePaWarThar.mp3"><span style="color: #ffcc00;">သုပၸ၀ါသာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/008%20U%20Nyanissara%20D42-%20ThotBaBuddha.mp3"><span style="color: #ffcc00;">သုပၸဗုဒၶ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/31/001%20U%20Nyanissara%20D36%20ThoutPaWarThar%2027-2-2003.mp3"><span style="color: #ffcc00;">သုပၸဝါသာ (၂၇-၂-၂၀၀၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0775-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သုပၸိယ ဝတၳဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0776-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သုပၸိယ ဝတၳဳ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0773-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုပၸိယာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0774-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုပၸိယာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0248-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သုဘာသိတဝါစာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0249-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သုဘာသိတဝါစာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0250-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သုဘာသိတဝါစာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0645-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဘူတိေထရ္ရအပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0646-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုဘူတိေထရ္ရအပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0950-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုမနပန္းေတာ္ဆက္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0951-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သုမနပန္းေတာ္ဆက္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0502-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0503-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0468-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရား(၇)ပါး-၁</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0469-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရား(၇)ပါး-၂</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0470-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သူေတာ္ေကာင္းတရား(၇)ပါး-၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0746-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေသလာ ေထရ္ရီ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0747-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေသလာ ေထရ္ရီ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0292-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေသာ၀စႆတာ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0293-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ေသာ၀စႆတာ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/007%20U%20Nyanissara%20D42-ThawPaKaTharMaNae.mp3"><span style="color: #ffcc00;">ေသာကပါကသာမေဏ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0955-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေသာဏေထရီတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0956-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေသာဏေထရီတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0967-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေသာပါကမေဏတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0968-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေသာပါကမေဏတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/01/007%20U%20Nyanissara%20D1%207-4-1977%20ThanCateSaTharMaNae.mp3"><span style="color: #ffcc00;">သံကိစၥသာမေဏ တရားေတာ္ (၇-၄-၁၉၇၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0537-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံတဝိဟာရတရား (ခ်မ္းသာစြာေနနည္း)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0558-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သံေဝဂ ကထာ (&nbsp;၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0559-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သံေဝဂ ကထာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0912-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သံေဝဂ ဥာဏ္ႏွင္႔သံေဝဂ ဘာဝနာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0920-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သံုးဆယ္ခုႏွစ္(၃၇)မင္းႏွင္႔ဘိုးေတာ္မယ္ေတာ္မ်ား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/115%20ThinKhaTa.mp3"><span style="color: #ffcc00;">သခၤတ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0878-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သခၤတႏွင့္အသခၤတ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0879-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သခၤတႏွင့္အသခၤတ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/082%2020081114%20ThinKyarChinHnintThinYuChin.mp3"><span style="color: #ffcc00;">သင္ၾကားျခင္းႏွင့္ သင္ယူျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0328-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဥၨာလီေ႐ႊပလႅင္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/033%2020040214%20ThitSarMyitTarSwanYay.mp3"><span style="color: #ffcc00;">သစၥာ ေမတၱာဂုဏ္ရည္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0828-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သစၥာေမတၲာစြမ္းရည္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0829-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သစၥာေမတၲာစြမ္းရည္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/37/004%20U%20Nyanissara%20D43-%20ThitSarLayPar.mp3"><span style="color: #ffcc00;">သစၥာေလးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0887-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သစၥာေလးပါးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0987-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သစၥာေလးပါးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/003%20U%20Nyanissara%20D42-ThetTaHtaNaKhuNhitPetPyitSinBuddhaWon.mp3"><span style="color: #ffcc00;">သတၱဌာန ခုႏွစ္ပတ္ျဖစ္စဥ္ ဗုဒၶ၀င္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0736-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဒၵါႏွင္႔စာဂတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0737-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">သဒၵါႏွင္႔စာဂတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0098-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဒၶါႏွင္႔မစၦရိယတိုက္ပဲြ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0282-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သႏၲဳဌိမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0283-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သႏၲဳဌိမဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0284-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သႏၲဳဌိမဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/36/002%20U%20Nyanissara%20D42-ThaPuYeatTaDarNaThoutTan.mp3"><span style="color: #ffcc00;">သပၸဴရိသဒါနသုတၱန္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0729-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဗၺမဂၤလာတရားေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0730-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">သဗၺမဂၤလာတရားေတာ္ (၂)</span></a></p>
<h5><span style="color: #00ffff;">“အ” အကၡရာစဥ္ တရားတာ္ာမ်ား</span></h5>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2016/004.mp3" target="_blank"><span style="color: #ffcc00;">အနိဋက႑ပေစၥကဗုဒၶ ဗုဒၶ၀င္တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/057%2020080204%20AThuYarTaitPwe%285%29.mp3" target="_blank"><span style="color: #ffcc00;">အသူရာတုိက္ပြဲ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0489-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အ႐ွင္နာဂသိန္ႏွင့္အဘိဓမၼာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0490-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အ႐ွင္နာဂသိန္ႏွင့္အဘိဓမၼာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0757-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အ႐ွိတရားႏွင္႕အမွန္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0758-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အ႐ွိတရားႏွင္႕အမွန္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0864-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အ႐ွုပ္႐ွင္းတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0865-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အ႐ွုပ္႐ွင္းတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/055%2020080116%20AKanGaBar.mp3"><span style="color: #ffcc00;">အကန္းကမၻာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/059%2020080307%20AKanGaBarHmarNyanShiKyaSanPar.mp3"><span style="color: #ffcc00;">အကန္းကမၻာမွာဥာဏ္ရွိၾကစမ္းပါ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/29/005%20U%20Nyanissara%20D33%20AhKyintNatAhTheatPyinNyar%2031-1-2000.mp3"><span style="color: #ffcc00;">အက်င္႔ႏွင္႔အသိပညာ (၃၁-၁-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0891-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အခြင့္သာခိုက္လံု႔လစိုက္တရားေတာ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0892-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အခြင့္သာခိုက္လံု႔လစိုက္တရားေတာ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0979-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အခ်ိန္ကိုအသံုးခ်တတ္ေၾကာင္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/097%20AChainHmaAChainKoSarChin%20Australia%20Apr25.mp3"><span style="color: #ffcc00;">အခ်ိန္မွအခ်ိန္ကိုစားျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/041%2020070123%20AKateTi.mp3"><span style="color: #ffcc00;">အဂတိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0480-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အဂၤုလိမာလ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0481-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အဂၤုလိမာလ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0482-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အဂၤုလိမာလ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/087%2020090508%20InGuLiMarLaKanKaungSayThawAChet2Chet.mp3"><span style="color: #ffcc00;">အဂၤုလိမာလကံေကာင္းေစေသာအခ်က္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0527-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဂၢပူဇာတရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0889-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အစုန္္ႏွင္႔္အဆန္္တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0026-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဇိတေကသကဗၺလဒိ႒ိတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0027-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဇိတေကသကဗၺလဒိ႒ိတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0835-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အတြင္းမီးအျပင္မီးတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0901-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အတၲသမၼာပဏိဓိစ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0902-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အတၲသမၼာပဏိဓိစ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0903-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အတၲသမၼာပဏိဓိစ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/108%20ApPaMarDaThaDi.mp3"><span style="color: #ffcc00;">အပၸမာ ဒသတိ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0474-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပၸမာဒသတိပဌာန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0475-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပၸမာဒသတိပဌာန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0476-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပၸမာဒသတိပဌာန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0272-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာေဒါစဓေမၼတု(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0273-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အပၸမာေဒါစဓေမၼတု(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0669-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပမာဒတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0670-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အပမာဒတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0268-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အန၀ဇၨကမၼမဂၤလာ(၁) (၁-၅-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0269-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အန၀ဇၨကမၼမဂၤလာ(၂) (၁-၅-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0259-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အနာကုလာစကမၼႏၲာမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0260-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အနာကုလာစကမၼႏၲာမဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0896-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဏွၾသဝါဒတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0651-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဓမၼာတရားႏွင့္ ပဥၥကၠဒါယကဝတၱဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0650-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဓမၼာတရားႏွင့္ပဥၥကၠဒါယကာဝတၴဳ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/085%2020090424%20SpecialLectureOnAbhidhamma-Myr.mp3"><span style="color: #ffcc00;">အဘိဓမၼာအထူးပို႕ခ်ခ်က္ – ျမန္မာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0719-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဓမၼာႏွင္႔ဝိပႆနာတရားေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0720-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အဘိဓမၼာႏွင္႔ဝိပႆနာတရားေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0915-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အဘိုးအဘြားမ်ားအတြက္သံေဝဂတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/107%20APhoeAPhwarMyarATwetThanWaiGa.mp3"><span style="color: #ffcc00;">အျပံဳးအေပ်ာ္မ်ားအတြက္ သံေ၀ဂ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/44/004%20UNyannssara-AhMaint-01-07-2003.mp3"><span style="color: #ffcc00;">အမိန္႔ ၀၁-၀၇-၂၀၀၃</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/18/005%20U%20Nyanissara%20D21%2016-4-1997%20AhMyatLayPa.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးတရားေလးပါး (၁၆-၄-၁၉၉၇)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/19/007%20U%20Nyanissara%20D22%2029-3-2000%20AhMyatSoneOakSarTaYar%202Par.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးဥစၥာတရား၂ပါး (၂၉-၃-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0665-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးဥစၥာတရား၂ပါး(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0666-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အျမတ္ဆုံးဥစၥာတရား၂ပါး(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0622-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အျမတ္တရား(၄)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0621-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အျမတ္တရားေလးပါး တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0500-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အရဟံဗုဒၶႏုႆတိဘာဝနာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0501-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အရဟံဗုဒၶႏုႆတိဘာဝနာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0306-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အရိယာသစၥာနဒႆနံ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0307-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အရိယာသစၥာနဒႆနံ မဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0305-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အရိယာသစၥာနဒႆနံမဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0497-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အရွင္၀ဂႌသေထရ္ရပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0498-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အရွင္၀ဂႌသေထရ္ရပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0499-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အရွင္၀ဂႌသေထရ္ရပါဒါန္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0931-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အရွင္ဓမၼပါလဆုေတာင္းတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0932-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အရွင္ဓမၼပါလဆုေတာင္းတရား(၂)</span></a><br>
<a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/19/001%20U%20Nyanissara%20D22%2012-2-1998%20AshinMahaKatThaPaMaHtay.mp3"><span style="color: #ffcc00;">အရွင္မဟာကႆဖမေထရ္ ၀ထၳဳ (၁၂-၂-၁၉၉၈)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0428-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အရွင္ေဃာဓိကမေထရ္တရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/098%20AhShinNarGaTheinNatABhidhamma.mp3"><span style="color: #ffcc00;">အရွာနာဂသိန္ႏွင့္ အဘိဓမၼာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/077%2020081014%20AShiTaYarHnintAHmanTaYar.mp3"><span style="color: #ffcc00;">အရွိတရားႏွင့္ အမုန္းတရား</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/35/006%20U%20Nyanissara%20D40-21-10-2000-AhWaitZarMhaWaitZarThoat.mp3"><span style="color: #ffcc00;">အဝိဇၨာမွ ဝိဇၨာသို႕ (၂၁-၁၀-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0593-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အေ၀းဆံုးေသာအရာဝတၳဳ ႏွစ္မ်ိဳး တရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0594-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အေ၀းဆံုးေသာအရာဝတၳဳ ႏွစ္မ်ိဳး တရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/32/006%20U%20Nyanissara%20D37%20AwaySoneThawAhYarWouldHtooNyitMyo.mp3"><span style="color: #ffcc00;">အေ၀းဆံုးေသာအရာဝတၴဳ (၂) မ်ဳိး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0595-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေ၀းဆံုးေသာအရာႏွစ္မ်ိဳးတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0596-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေ၀းဆံုးေသာအရာႏွစ္မ်ိဳးတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0355-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေစလကႆပတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0356-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေစလကႆပတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0357-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေစလကႆပတရား(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0589-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေပ်ာ္ဆံုးေန႕တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0590-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေပ်ာ္ဆံုးေန႕တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0591-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေပ်ာ္ဆံုးေန႔တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0592-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေပ်ာ္ဆံုးေန႔တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/07/002%20U%20Nyanissara%20D9%201-4-1980%20AhThayWaLarSaBarLarNan.mp3"><span style="color: #ffcc00;">အေသဝနာစဗာလာနံ(၁) (၁-၄-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/07/003%20U%20Nyanissara%20D9%202-4-1980%20AhThayWaLarSaBarLarNan%202.mp3"><span style="color: #ffcc00;">အေသဝနာစဗာလာနံ(၂) (၂-၄-၁၉၈၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0491-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အသက္႐ွည္ေၾကာင္းမဟာဓမၼပါလဇာတ္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0492-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အသက္႐ွည္ေၾကာင္းမဟာဓမၼပါလဇာတ္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/057%2020080204%20AThuYarTaitPwe%285%29.mp3"><span style="color: #ffcc00;">အသူရာတုိက္ပြဲ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0313-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အေသာကံ မဂၤလာ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0314-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အေသာကံ မဂၤလာ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0315-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အေသာကံ မဂၤလာ(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0102-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႏု႐ုဒၶါသုတၲန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0101-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႏု႐ုဒၶါသုတၲန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/010%2019820225%20AhNhitKoePar.mp3"><span style="color: #ffcc00;">အႏွစ္ကိုးပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0629-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အႏွစ္သံုးပါးတရား (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0630-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အႏွစ္သံုးပါးတရား (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/29/004%20U%20Nyanissara%20D33%20ErPhyatTaYar%201-5-1999.mp3"><span style="color: #ffcc00;">အားၿဖည္႔တရားေတာ္ (၁-၅-၁၉၉၉)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0251-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာနႏၵာေထရအပါဒါန္ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0252-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာနႏၵာေထရအပါဒါန္ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/23/010%20U%20Nyanissara%20D26%20ArYuDeeKongMhut.mp3"><span style="color: #ffcc00;">အာယုဒီဃေကာင္းမႈ(၆)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0888-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာယုဒီဃေကာင္းမႈ႔(၆)ပါး</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0633-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာျဖည့္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0634-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အာျဖည့္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0270-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာရတီိရတီပါပါ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0271-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">အာရတီိရတီပါပါ(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0599-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေညာညနိသိတတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0600-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အေညာညနိသိတတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0974-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ေအာင္ဆုေတာင္းဂါထာ (အေနကဇာတင္တရား)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0516-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႏၱိမပူဇာသဓုကိဋနာေဒသနာေတာ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0517-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႏၱိမပူဇာသဓုကိဋနာေဒသနာေတာ္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0518-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အႏၱိမပူဇာသဓုကိဋနာေဒသနာေတာ္(၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0190-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အမၺပါလီေထရီအပါဒါန္ (၃)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0188-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အမၺပါလီေထရီအပါဒါန္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0189-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အမၺပါလီေထရီအပါဒါန္(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0191-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">အမၺပါလီေထရီအပါဒါန္(၄)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/114%20OhKweYayLaungMaPhyitSayNelt.mp3"><span style="color: #ffcc00;">အိုးကြဲေရေလာင္းမျဖစ္ေစနဲ႕</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/065%2020080717%20EainTawYarKaRuNar.mp3"><span style="color: #ffcc00;">အိမ္ေတာ္ရာ ကရုဏာ</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/35/005%20U%20Nyanissara%20D40-10-7-2000-AteTharNateMitSaYeatYaTaYar.mp3"><span style="color: #ffcc00;">ဣႆာႏွင့္ မစၦရိယ (၁၀-၇-၂၀၀၀)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/25/003%20U%20Nyanissara%20D29%20AllWaDaTaYar%2019-7-1980.mp3"><span style="color: #ffcc00;">ၾသဝါဒတရား (၁၉-၇-၁၉၈၀)</span></a><br>
<a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/2.7%20thidagu%20awyadaparlimonk.mp3"><span style="color: #ffcc00;">ၾသဝါဒ ပါတိေမာက္ တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0626-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ၾသဝါဒပါတိေမာက္တရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0627-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ၾသဝါဒပါတိေမာက္တရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/093%2020090923%20AuPyitKharPhyintBaWaKoAHlaSinChin.mp3" target="_blank"><span style="color: #ffcc00;">ဥေပကၡာျဖင့္ ဘ၀ကုိအလွဆင္ျခင္း တရားေတာ္</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0787-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဥတၱရာ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0788-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဥတၱရာ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0477-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဥတၱရနႏၵမာတာဝတၱဳ(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0750-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဥပစာလာ ေထရ္ရီ (၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0751-UNyanissara-MP3V2.MP3"><span style="color: #ffcc00;">ဥပစာလာေထရ္ရီ (၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0897-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဥယ်ာဥ္ၾကီးကုိေရေလာင္းပါတရား(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0898-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဥယ်ာဥ္ၾကီးကုိေရေလာင္းပါတရား(၂)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/093%2020090923%20AuPyitKharPhyintBaWaKoAHlaSinChin.mp3"><span style="color: #ffcc00;">ဥေပကၡာျဖင့္ ဘ၀ကိုအလွဆင္ျခင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/44/007%20UNyanissara%20A-KaRickMinGyiEiBaWaNeatGone%2030-10-2007.mp3"><span style="color: #ffcc00;">ဧကရာဇ္မင္းႀကီးရဲ႕ ဘ၀နိဂုံးတရားေတာ္ (၃၀-၁၀-၂၀၀၇) မႏၲေလးၿမိဳ႕ အေဝရာ ရာမ ရန္ကင္းေက်ာင္း</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/MP3%281000%29/0483-UNyanissara-MP3V2.mp3"><span style="color: #ffcc00;">ဧဒကဘဒၵဇာတ္(၁)</span></a></p>
<p><a href="https://media.thitsarparamisociety.com/mp3/Sitagu%20Sayardaw/DVD%28115%29/088%2020090509%20IrrawaddyHmarYwarDeMoe.mp3"><span style="color: #ffcc00;">ဧရာ၀တီမွာရြာတဲ့မိုး</span></a></p>
<p>&nbsp;</p>
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
    <div id="text-17" class="widget widget_text"><h3 class="widget-title">Feed Back</h3>			<div class="textwidget"><p align="justify">ဓမၼမိတ္ေဆြ အေပါင္းတို ့ မိမိတုိ ့၏ တရားစခန္း အခက္အခဲမ်ား၊ နာၾကား အၾကံျပဳ လိုေသာ တရားဓမၼမ်ား ၊ ေမးျမန္းလိုေသာ ဓမၼေမးခြန္းမ်ား ၊ website ၾကည့္ရွုနာၾကားရာ ၌ အခက္အခဲမ်ား ျဖစ္ေပၚပါက ေအာက္ပါ Form တြင္ ျဖည့္စြက္၍ ေပးပို႔ အႀကံျပဳၾကပါရန္ ေမတၱာရပ္ခံအပ္ပါသည္။</p>

    <!-- START JS for Form ID: 12786 -->
	<script type="text/javascript">
		jQuery(document).ready(function($) {
			
		jQuery("#preloader-npazeq").fadeOut(1500, function () {
			jQuery("#ecf-form-npazeq").fadeIn(300);
			});
			
			$( '.ladda-button' ).ladda( 'bind' );

			$(function() {
				
						
				// Validation
				$("#form-npazeq").validate(
				{					
					// Rules for form validation
					rules:
					{
					name0:{required: true},email1:{required: true,email: true},message2:{required: true,minlength: 10},
							
									
					},
										
					// Messages for form validation
					messages:
					{
					name0:{required: "This field is required"},email1:{required: "This field is required"},message2:{required: "This field is required"}					},					
					// Do not change code below
					errorPlacement: function(error, element) {
						error.insertAfter(element.parent());
						},
						
					submitHandler: function (form) {
										 ecf_onsubmit(jQuery('.form-npazeq'));
						 
						 						 
						 },
						 
					invalidHandler: function (form) {	
					  	$.ladda( 'stopAll' );
					 	},
						 
					onkeyup: false,
					onfocusout: false,
					onclick: false
					
				});
			});	
			
			
			/* Form Submit ( Ajax ) */
			function ecf_onsubmit(form){	

				if(form.attr('action')=='#'){
					
					data = {};
					eldat = [];
					data['action'] = 'ecf_deliver_mail';
					data['formid'] = '12786';
					data['security'] = '566f4940d3';
		
		
						
					jQuery('input, textarea', form).each(function(key){
						
						items = {};
						
						if (typeof $(this).data('type') === 'undefined') { return true; }
						

						
						items['type'] = $(this).data('type');
						items['label'] = $(this).data('label');
						items['value'] = this.value;
						items['name'] = this.name;

						eldat.push(items);
							
						}); // END  form).each(function(key){
							

													

						data['allelmnt'] = JSON.stringify(eldat);

						submitForm();
				
					return false;
					
				} // End if(form.attr('action')=='#'){
				
			} // End ecf_onsubmit 
			
			// Start submitForm		
			  function submitForm() {
				  
				jQuery.ajax({
					url: 'https://www.thitsarparamisociety.com/wp-admin/admin-ajax.php', 
					type: 'POST',
					dataType: 'json',
					data: data, 
					success: function(data) {
				
						if(data.Ok==true) {
									// success
							$("#form-npazeq").get(0).reset();	
								
							if(data.msg == 'redirect') {
								window.location = "http://";
								} else {
									notifyme('Your Message Submitted Successfully', 'n', 'success', 'left middle');
									}
		
							}
							else {
								$("#form-npazeq").get(0).reset();
								notifyme(data.msg, 'n', 'error', 'left middle');
								}
								
							$.ladda( 'stopAll' );	
									
							}
						});
						
										
					} // End submitForm
	
					
			// Notify	
			  function notifyme(msg, b, typ, pos) {
				  if (b == 'n') {
					  b = 'cf-submittednpazeq';
				  } else {
					 b = 'atcnpazeq';
				  }
				  
				  $("#"+b).gnotify(msg,{
					  style: "nbootstrap",
					  elementPosition: pos,
					  className: typ
					  });
					  
					  msg = null;
					  typ = null;
					  
					}

		});		
		</script>
    <!-- END JS for Form ID: 12786 -->
    
    
    	
    
<!-- START Form Markup for Form ID: 12786 -->
<div id="preloader-npazeq" class="ecfpreloader" style="display: none;"></div>   
    <div id="ecf-form-npazeq" class="ecf-body" style="">					
		<form method="post" enctype="multipart/form-data" action="#" id="form-npazeq" class="ecf-form form-npazeq" novalidate="novalidate">
        	<header>အႀကံျပဳစာ</header>    		<fieldset>	
    <section><label class="label">Name</label><label class="input"><input data-type="name" data-label="Name" id="name0" name="name0" type="text"></label></section><section><label class="label">Email</label><label class="input"><input data-type="email" data-label="Email" id="email1" name="email1" type="text"></label></section><section><label class="label">Message</label><label class="textarea"><textarea data-type="message" data-label="Message" id="message2" name="message2" rows="7"></textarea></label></section>      
        
				        
         
       		 </fieldset>
        		<footer>
                    <button data-style="slide-down" id="cf-submittednpazeq" class="ecfbutton ladda-button" type="submit" name="cf-submittednpazeq"><span class="ladda-label">SEND</span><span class="ladda-spinner"></span></button> 
				</footer>
			</form>
            
                        
            </div>  
<!-- END Form Markup for Form ID: 12786 -->
			
	
</div>
		</div></div>
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
	<input id="kopa_set_view_count_wpnonce" name="kopa_set_view_count_wpnonce" value="1094a2c343" type="hidden"><input id="kopa_set_user_rating_wpnonce" name="kopa_set_user_rating_wpnonce" value="ae3a3ac60f" type="hidden">	<!--[if lte IE 8]>
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
		<a href="/sitagu-sayardaw-mp3/?mode=list" class="view-list">
			<span class="screen-reader-text">List View</span>
		</a>
		<a href="/sitagu-sayardaw-mp3/?mode=grid" class="view-grid current">
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
<link rel="stylesheet" id="ecf-frontend-css-css" href="https://www.thitsarparamisociety.com/wp-content/plugins/contact-form-lite/css/frontend.css?ver=1.0.95" type="text/css" media="all">
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
var _wpPluploadSettings = {"defaults":{"runtimes":"html5,flash,silverlight,html4","file_data_name":"async-upload","url":"\/wp-admin\/async-upload.php","flash_swf_url":"https:\/\/www.thitsarparamisociety.com\/wp-includes\/js\/plupload\/plupload.flash.swf","silverlight_xap_url":"https:\/\/www.thitsarparamisociety.com\/wp-includes\/js\/plupload\/plupload.silverlight.xap","filters":{"max_file_size":"67108864b","mime_types":[{"extensions":"jpg,jpeg,jpe,gif,png,bmp,tiff,tif,ico,asf,asx,wmv,wmx,wm,avi,divx,flv,mov,qt,mpeg,mpg,mpe,mp4,m4v,ogv,webm,mkv,3gp,3gpp,3g2,3gp2,txt,asc,c,cc,h,srt,csv,tsv,ics,rtx,css,vtt,dfxp,mp3,m4a,m4b,ra,ram,wav,ogg,oga,mid,midi,wma,wax,mka,rtf,pdf,class,tar,zip,gz,gzip,rar,7z,psd,xcf,doc,pot,pps,ppt,wri,xla,xls,xlt,xlw,mdb,mpp,docx,docm,dotx,dotm,xlsx,xlsm,xlsb,xltx,xltm,xlam,pptx,pptm,ppsx,ppsm,potx,potm,ppam,sldx,sldm,onetoc,onetoc2,onetmp,onepkg,oxps,xps,odt,odp,ods,odg,odc,odb,odf,wp,wpd,key,numbers,pages"}]},"multipart_params":{"action":"upload-attachment","_wpnonce":"da479b7bae"}},"browser":{"mobile":false,"supported":true},"limitExceeded":false};
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
var _wpMediaViewsL10n = {"url":"URL","addMedia":"Add Media","search":"Search","select":"Select","cancel":"Cancel","update":"Update","replace":"Replace","remove":"Remove","back":"Back","selected":"%d selected","dragInfo":"Drag and drop to reorder media files.","uploadFilesTitle":"Upload Files","uploadImagesTitle":"Upload Images","mediaLibraryTitle":"Media Library","insertMediaTitle":"Insert Media","createNewGallery":"Create a new gallery","createNewPlaylist":"Create a new playlist","createNewVideoPlaylist":"Create a new video playlist","returnToLibrary":"\u2190 Return to library","allMediaItems":"All media items","allDates":"All dates","noItemsFound":"No items found.","insertIntoPost":"Insert into post","unattached":"Unattached","trash":"Trash","uploadedToThisPost":"Uploaded to this post","warnDelete":"You are about to permanently delete this item.\n  'Cancel' to stop, 'OK' to delete.","warnBulkDelete":"You are about to permanently delete these items.\n  'Cancel' to stop, 'OK' to delete.","warnBulkTrash":"You are about to trash these items.\n  'Cancel' to stop, 'OK' to delete.","bulkSelect":"Bulk Select","cancelSelection":"Cancel Selection","trashSelected":"Trash Selected","untrashSelected":"Untrash Selected","deleteSelected":"Delete Selected","deletePermanently":"Delete Permanently","apply":"Apply","filterByDate":"Filter by date","filterByType":"Filter by type","searchMediaLabel":"Search Media","noMedia":"No media files found.","attachmentDetails":"Attachment Details","insertFromUrlTitle":"Insert from URL","setFeaturedImageTitle":"Featured Image","setFeaturedImage":"Set featured image","createGalleryTitle":"Create Gallery","editGalleryTitle":"Edit Gallery","cancelGalleryTitle":"\u2190 Cancel Gallery","insertGallery":"Insert gallery","updateGallery":"Update gallery","addToGallery":"Add to gallery","addToGalleryTitle":"Add to Gallery","reverseOrder":"Reverse order","imageDetailsTitle":"Image Details","imageReplaceTitle":"Replace Image","imageDetailsCancel":"Cancel Edit","editImage":"Edit Image","chooseImage":"Choose Image","selectAndCrop":"Select and Crop","skipCropping":"Skip Cropping","cropImage":"Crop Image","cropYourImage":"Crop your image","cropping":"Cropping\u2026","suggestedDimensions":"Suggested image dimensions:","cropError":"There has been an error cropping your image.","audioDetailsTitle":"Audio Details","audioReplaceTitle":"Replace Audio","audioAddSourceTitle":"Add Audio Source","audioDetailsCancel":"Cancel Edit","videoDetailsTitle":"Video Details","videoReplaceTitle":"Replace Video","videoAddSourceTitle":"Add Video Source","videoDetailsCancel":"Cancel Edit","videoSelectPosterImageTitle":"Select Poster Image","videoAddTrackTitle":"Add Subtitles","playlistDragInfo":"Drag and drop to reorder tracks.","createPlaylistTitle":"Create Audio Playlist","editPlaylistTitle":"Edit Audio Playlist","cancelPlaylistTitle":"\u2190 Cancel Audio Playlist","insertPlaylist":"Insert audio playlist","updatePlaylist":"Update audio playlist","addToPlaylist":"Add to audio playlist","addToPlaylistTitle":"Add to Audio Playlist","videoPlaylistDragInfo":"Drag and drop to reorder videos.","createVideoPlaylistTitle":"Create Video Playlist","editVideoPlaylistTitle":"Edit Video Playlist","cancelVideoPlaylistTitle":"\u2190 Cancel Video Playlist","insertVideoPlaylist":"Insert video playlist","updateVideoPlaylist":"Update video playlist","addToVideoPlaylist":"Add to video playlist","addToVideoPlaylistTitle":"Add to Video Playlist","settings":{"tabs":[],"tabUrl":"https:\/\/www.thitsarparamisociety.com\/wp-admin\/media-upload.php?chromeless=1","mimeTypes":{"image":"Images","audio":"Audio","video":"Video"},"captions":true,"nonce":{"sendToEditor":"b1b1b3b463"},"post":{"id":0},"defaultProps":{"link":"file","align":"","size":""},"attachmentCounts":{"audio":1,"video":1},"embedExts":["mp3","ogg","wma","m4a","wav","mp4","m4v","webm","ogv","wmv","flv"],"embedMimes":{"mp3":"audio\/mpeg","ogg":"audio\/ogg","wma":"audio\/x-ms-wma","m4a":"audio\/mpeg","wav":"audio\/wav","mp4":"video\/mp4","m4v":"video\/mp4","webm":"video\/webm","ogv":"video\/ogg","wmv":"video\/x-ms-wmv","flv":"video\/x-flv"},"contentWidth":1190,"months":[{"year":"2018","month":"11","text":"November 2018"},{"year":"2018","month":"10","text":"October 2018"},{"year":"2018","month":"9","text":"September 2018"},{"year":"2018","month":"8","text":"August 2018"},{"year":"2018","month":"7","text":"July 2018"},{"year":"2018","month":"6","text":"June 2018"},{"year":"2018","month":"5","text":"May 2018"},{"year":"2018","month":"4","text":"April 2018"},{"year":"2018","month":"3","text":"March 2018"},{"year":"2018","month":"2","text":"February 2018"},{"year":"2017","month":"12","text":"December 2017"},{"year":"2017","month":"10","text":"October 2017"},{"year":"2017","month":"7","text":"July 2017"},{"year":"2017","month":"6","text":"June 2017"},{"year":"2017","month":"3","text":"March 2017"},{"year":"2017","month":"2","text":"February 2017"},{"year":"2016","month":"10","text":"October 2016"},{"year":"2016","month":"9","text":"September 2016"},{"year":"2016","month":"8","text":"August 2016"},{"year":"2016","month":"7","text":"July 2016"},{"year":"2016","month":"6","text":"June 2016"},{"year":"2016","month":"4","text":"April 2016"},{"year":"2016","month":"3","text":"March 2016"},{"year":"2016","month":"2","text":"February 2016"},{"year":"2016","month":"1","text":"January 2016"},{"year":"2015","month":"12","text":"December 2015"},{"year":"2015","month":"11","text":"November 2015"},{"year":"2015","month":"10","text":"October 2015"},{"year":"2015","month":"9","text":"September 2015"},{"year":"2015","month":"8","text":"August 2015"},{"year":"2015","month":"7","text":"July 2015"},{"year":"2015","month":"6","text":"June 2015"},{"year":"2015","month":"5","text":"May 2015"},{"year":"2015","month":"4","text":"April 2015"},{"year":"2015","month":"3","text":"March 2015"},{"year":"2015","month":"2","text":"February 2015"},{"year":"2015","month":"1","text":"January 2015"},{"year":"2014","month":"12","text":"December 2014"},{"year":"2014","month":"11","text":"November 2014"},{"year":"2014","month":"10","text":"October 2014"},{"year":"2014","month":"9","text":"September 2014"},{"year":"2014","month":"8","text":"August 2014"},{"year":"2014","month":"7","text":"July 2014"},{"year":"2014","month":"6","text":"June 2014"},{"year":"2014","month":"5","text":"May 2014"},{"year":"2014","month":"4","text":"April 2014"},{"year":"2014","month":"3","text":"March 2014"},{"year":"2014","month":"2","text":"February 2014"}],"mediaTrash":0}};
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
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contact-form-lite/js/jquery/jquery.validate.min.js?ver=1.0.95"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contact-form-lite/js/jquery/ladda/spin.js?ver=1.0.95"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contact-form-lite/js/jquery/notify.min.js?ver=1.0.95"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contact-form-lite/js/jquery/ladda/ladda.min.js?ver=1.0.95"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contact-form-lite/js/jquery/ladda/ladda.jquery.js?ver=1.0.95"></script>
<script type="text/javascript" src="https://www.thitsarparamisociety.com/wp-content/plugins/contus-video-gallery/js/playlist.min.js?ver=4.6.12"></script>
    



"""

soup = bs4(text, 'html.parser')


with open('titles_links.txt', 'w') as f:
    count = 1
    for key in soup.find_all('a'):
        if ".mp3" in key.get('href'):
            counter = '{:03d}'.format(count)
            f.write('{}.mp3|{}|{}\n'.format(counter, key.get('href'), ''.join(key.get_text().splitlines())) )
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