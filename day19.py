

#-------------------------> pip <-------------------------

# pip : pip stands for preferred installer program,it contain   different python package
# package: it is a module that contain one or more module or other package
# module:a module that can install to our application is a package

# install package  using pip

# numpy: it is a fundamental package for scientific computing with python.
# -> it contain N-dimentonal array object
# -> sophisticated(broadcasting) function
# -> tools integrating c/c++
# -> useful linear algebra,fourier transform and random number capability

# (1) $- pip install numpy


import numpy
lst=[1,2,3,4,5]
np_arr=numpy.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr*2)
print(np_arr+2)

# pandas : it is a open source,BSD-licensed library,providing high performance,easy to use data structure and data analysis tool for python

# (2) ~$ pip install pandas

# web browser module: it help us to open any website no need to install package ,it already installed by default

import webbrowser
url_lst=[
    "http://www.python.org",
    "https://www.facebook.com",
    "https://www.google.com"
]
for url in url_lst:
    webbrowser.open_new_tab(url)

# => uninstall package

#    ~$ pip uninstall <package_name>

# => LIST PACKAGE  :

#    ~$ pip list

# => SHOW PACKAGE

#    ~$ pip show package_name

# => READING FROM URL

#    ~$ pip install requests

# -> get():to open a network and fetch data from url,it return responce
# -> status_code:after fatch data we can check statu of operation(success , failed)
# -> header:check header type
# -> text:extract text from the fetched responce object
# -> json:extract json data 

# but  internet connection require,(when net is connected delete the the comments)

# import requests
# url="https://www.w3.org/TR/PNG/iso_8859-1.txt"
# responce=requests.get(url)
# print(responce)
# print(responce.status_code)
# print(responce.headers)
# print(responce.text)
# o/p:
 
# <Response [404]>
# 404
# {'Date': 'Sun, 01 Jun 2025 02:57:10 GMT', 'Content-Type': 'text/html; charset=iso-8859-1', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'last-modified': 'Mon, 20 Jan 2025 21:48:19 GMT', 'x-backend': 'www-mirrors', 'x-request-id': '948b71202ffe2144', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': "frame-ancestors 'self' https://cms.w3.org/ https://cms-dev.w3.org/; upgrade-insecure-requests", 'CF-Cache-Status': 'BYPASS', 'Vary': 'Accept-Encoding', 'Server': 'cloudflare', 'CF-RAY': '948b71202ffe2144-BBI', 'Content-Encoding': 'gzip', 'alt-svc': 'h3=":443"; ma=86400'}
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
# <head>
#   <title>Error 404 - Not found</title>
#   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
#     <link rel="Help" href="/Help/" />
#   <link rel="stylesheet" href="/2008/site/css/minimum" type="text/css" media="all" />
#   <style type="text/css"  media="print, screen and (min-width: 481px)">@import url("/2008/site/css/advanced");</style>
#   <link href="/2008/site/css/minimum" rel="stylesheet" type="text/css" media="only screen and (max-width: 480px)" />
#   <meta name="viewport" content="width=device-width"/>
#   <link rel="stylesheet" href="/2008/site/css/print" type="text/css" media="print" />
#   <link rel="shortcut icon" href="/2008/site/images/favicon.ico" type="image/x-icon" />
#   </head>
# <body id="www-w3-org" class="w3c_public">
#  <div id="w3c_container">
#   <div id="w3c_mast"> <!-- #w3c_mast / Page top header -->
#    <h1 class="logo"><a tabindex="2" accesskey="1" href="/"><img src="/2008/site/images/logo-w3c-mobile-lg" width="90" height="53" alt="W3C" /></a>
#    <span class="alt-logo">W3C</span>
#    </h1>
#    <div id="w3c_nav">
#      <form action="https://www.w3.org/Help/search" method="get" enctype="application/x-www-form-urlencoded">
#        <!-- w3c_sec_nav is populated through js -->
#        <div class="w3c_sec_nav"><!-- --></div>
#            <ul class="main_nav"> <!-- Main navigation menu -->
#      <li class="first-item"><a href="/standards/">Standards</a></li><li><a href="/participate/">Participate</a></li><li><a href="/Consortium/membership">Membership</a></li><li class="last-item"><a href="/Consortium/">About W3C</a></li>
#        <li class="search-item">
#       <div id="search-form">
#        <input tabindex="3" class="text" name="q" value="" title="Search" />
#        <button id="search-submit" name="search-submit" type="submit"><img class="submit" src="/2008/site/images/search-button" alt="Search" width="21" height="17" /></button>
#       </div>
#     </li>
#    </ul>

#      </form>
#    </div>
#   </div> <!-- /end #w3c_mast -->

#   <div id="w3c_main">
#     <div id="w3c_logo_shadow" class="w3c_leftCol">
#       <img height="32" alt="" src="/2008/site/images/logo-shadow" />
#     </div>
#    <div id="w3c_sidenavigation" class="w3c_leftCol">       <h2 class="offscreen">Site Navigation</h2>
#     <h3 class="category"><span class="ribbon"><a href="/Help/" title="Up to Help and FAQ">Help and FAQ <img src="/2008/site/images/header-link" alt="Header link" width="13" height="13" class="header-link"/></a></span></h3>
#        <ul class="theme">
#         <li><a href="/Help/Webmaster.html">FAQ about W3C Web Site</a></li>
#         <li><a href="/Consortium/siteindex.html">W3C Site Map</a></li>
#         <li><a href="/Help/Account/">W3C User Account Management</a></li>
#        </ul>
#        <br/>
#       </div>
#    <div class="w3c_mainCol">
#           <div id="w3c_crumbs">
#        <div id="w3c_crumbs_frame">
#         <ul class="bct"> <!-- .bct / Breadcrumbs -->
#           <li class="skip"><a tabindex="1" accesskey="2" title="Skip to content (e.g., when browsing via audio)" href="#w3c_content_body">Skip</a></li>
#           <li><a href="/">W3C</a>&#160;<span class="cr">&#x00bb;</span>&#160;</li>
#           <li><a href="/Consortium/">About&#160;W3C</a>&#160;<span class="cr">&#x00bb;</span>&#160;</li>
#           <li><a href="/Help/">Help&#160;and&#160;FAQ</a>&#160;<span class="cr">&#x00bb;</span>&#160;</li>
#           <li class="current">404 Not Found</li>
#         </ul>
#      </div>
#     </div>
#     <h1 class="title">Document not found</h1>
#     <div id="w3c_content_body">
#     <div class="line">

# <p class="intro tPadding">
#   Sorry, the document you requested is not available.
#   Here are some steps you may try to find the page you were
#   looking for:
# </p>
# <ol class="show_items">
#   <li>If you typed the URL by hand then please make sure that it is exactly
#   as it should be. Also check the capitalization and that you are using
#   forward slashes ( / ).</li>
#   <li>If you are looking for information on a particular subject, please
#   start on the <a href="https://www.w3.org/">W3C Home
#   page</a> or <a href="https://www.w3.org/Consortium/siteindex.html">Site
#   Map</a>.</li>
#   <li>Try searching the site using the search box at the top of this page.</li>
# </ol>

# <p>The <a href="https://www.w3.org/Help/Webmaster">W3C Webmaster FAQ</a> has
# answers to frequently asked questions about our site.</p>
#           </div> <!-- /end .line -->
#         </div> <!-- /end #w3c_content_body -->
#       </div> <!-- /end #w3c_mainCol -->
#     </div> <!-- end #w3c_main -->
#   </div> <!-- /end #w3c_container -->

# <div id="w3c_footer">
#   <div id="w3c_footer-inner">
#     <h2 class="offscreen">Footer Navigation</h2>
#     <div class="w3c_footer-nav">
#       <h3>Navigation</h3>
#       <ul class="footer_top_nav">
#        <li><a href="/">Home</a></li>
#        <li><a href="/standards/">Standards</a></li>
#        <li><a href="/participate/">Participate</a></li>
#        <li><a href="/Consortium/membership">Membership</a></li>
#        <li class="last-item"><a href="/Consortium/">About W3C</a></li>
#       </ul>
#     </div>
#     <div class="w3c_footer-nav">
#       <h3>Contact W3C</h3>
#       <ul class="footer_bottom_nav">
#            <li><a href="/Consortium/contact">Contact</a></li>
#            <li><a accesskey="0" href="/Help/">Help and FAQ</a></li>
#            <li><a href="/Consortium/sponsor/">Sponsor / Donate</a></li>
#            <li><a href="/Consortium/siteindex">Site Map</a></li>
#            <li><address id="w3c_signature"><a href="https://lists.w3.org/Archives/Public/site-comments/">Feedback</a></address></li>
#       </ul>
#     </div>
#     <div class="w3c_footer-nav">
#       <h3>W3C Updates</h3>
#       <ul class="footer_follow_nav">
#            <li>
#                    <a href="https://twitter.com/W3C" title="Follow W3C on Twitter"><img src="/2008/site/images/Twitter_bird_logo_2012.svg" alt="Twitter" class="social-icon" height="40"/></a>
#           </li>
#      </ul>
#     </div>
#     <!-- #footer address / page signature -->
#     <p class="copyright">Copyright &copy; 2025 <a href="https://www.w3.org/">World Wide Web Consortium</a>.
#     <abbr title="World Wide Web Consortium">W3C</abbr><sup>&reg;</sup>
#     <a href="https://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer">liability</a>,
#     <a href="https://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks">trademark</a> and
#     <a rel="license" href="https://www.w3.org/Consortium/Legal/copyright-software" title="W3C Software and Document License">permissive document license</a> rules apply.</p>

#   </div>
# </div><!-- /end #footer -->
# <div id="w3c_scripts">
#   <script type="text/javascript" src="/2008/site/js/main"></script>
# </div>

# </body>
# </html>

def add(*args):
    total=0
    for num in args:
        total+=num
    return total

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
import arithmetic
print(arithmetic.add(1,2,4,5))
print(arithmetic.sub(5,3))
print(arithmetic.mul(5,2))
import mymodule_ex1
print(mymodule_ex1.generate_fullname("arpit","mishra"))




from rich import print
print("[bold red]Error:[/bold red] something went wrong!")
print("[green]ya success[/green] task completed")
