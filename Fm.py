import os
import sys
import re
import time
import json
import requests
import random
import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
import os, time, uuid, requests
from multiprocessing.pool import ThreadPool
os.system("clear")
os.system("termux-setup-storage")
reload(sys)
sys.setdefaultencoding('utf-8')
H = '\x1b[1;90m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
T = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
ua_nokia = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
ua_xiaomi = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36'
ua_macos = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
ua_vivo = 'Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36'
ua_oppo = 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
ua_huawei = 'Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36'
ua_redmi4a = 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
ua_vivoy12 = 'Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'
ua_nokiax = 'NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
ua_asus = 'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
ua_galaxys10 = 'Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36'
ua_lenovo = 'Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36'
ua = random.choice([
    ua_nokia,
    ua_xiaomi,
    ua_samsung,
    ua_macos,
    ua_vivo,
    ua_oppo,
    ua_huawei,
    ua_redmi4a,
    ua_vivoy12,
    ua_nokiax,
    ua_asus,
    ua_galaxys10,
    ua_lenovo])
logo = """
   _____      _    _   _______  _     _   _____  
  (_____)    (_)  (_) (_______)(_)   (_) (_____) 
 (_)___(_)   (_)_(_)     (_)   (__)_ (_)(_)  ___ 
 (_______)   (____)      (_)   (_)(_)(_)(_) (___)
 (_)   (_)   (_) (_)   __(_)__ (_)  (__)(_)___(_)
 (_)   (_)   (_)  (_) (_______)(_)   (_) (_____) 
\033[1;95m-----------------------------------------------  
\033[1;37m(*) AUTHOR   :\033[1;97m IMTIAZ AKING
\033[1;37m(*) WHATSAPP :\033[1;37m 03237528063
\033[1;37m(*) TOLL TYPE: FILE MAKING
\033[1;37m(*) WARNING  : HEATERS MAKE ME FAMOUS 
\n\x1b[1;97m-----------------------------------------------\n\x1b[0;93m\x1b[1;42m       IMTIAZ AKING TOLLS FOR MAKE FILE        \x1b[0m\n-----------------------------------------------\n\x1b[0;97m \x1a IMTIAZ AKING BOLTE PUBLIC  \n\x1b[1;97m-----------------------------------------------\n\x1b[0;93m\x1b[1;41mMain To Is Vaste Chup Huun Ki Tamasha Na Bane   
Tu Samajhta Hai Mujhe Tujh Se Gila Kuch Bhi Nahi\x1b[0m\n-----------------------------------------------\n\x1b[0;97m \x1a 
"""
def Aking():
    os.system('clear')
    print logo
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;97m Make File'
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m2\x1b[1;91m]\x1b[1;97m Follow Owner'
    time.sleep(0.2)
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m0\x1b[1;91m]\x1b[1;97m Exit'
    time.sleep(0.2)
    print ''
    time.sleep(0.2)
    ok = raw_input('\x1b[1;91m[\x1b[1;97m?\x1b[1;91m]\x1b[1;97m Select: \x1b[1;92m')
    if ok == '':
        print '\x1b[1;91m[\x1b[1;97m!\x1b[1;91m] \x1b[1;97mWrong Input'
        AKing()
    elif ok == '1':
        login()
    elif ok == '2':
        os.system('xdg-open https://www.facebook.com/babar.tunio.71')
        time.sleep(3)
        Aking()
    elif ok == '3':
        print '\x1b[1;93m       SEE YOU AGAIN :)'
        sys.exit()


def login():

    os.system('clear')
    print logo
    try:
        ___token___ = raw_input('%s[%s~%s]%s Paste Token :%s ' % (B, P, B, P, K))
        if ___token___ in ('', ' '):
            exit('%s[%s!%s]%sPlease Put Token Bro' % (P, M, P, M))
        
        xwx = requests.get('https://graph.facebook.com/me/?access_token=%s' % ___token___).json()
        print''
        print '%s[%s*%s]%s WELCOME%s %s' % (B, P, B, P, H, xwx['name'].upper())
        time.sleep (5)
        open('login.txt', 'w').write(___token___)
        menu()
    except ConnectionError:
        exit('%s[%s!%s]%s INTERNET CONNECTION ERROR ' % (P, K, P, K))



def menu():
    os.system('clear')
    
    try:
        ___token___ = open('login.txt', 'r').read()
    except IOError:
        print ''
    print logo
    print 'Enter File Name'
    print 'Example: \x1b[1;32m/sdcard/AKING.txt'
    print ''
    file = raw_input('\x1b[1;97mFile Path: ')
    print 'Note  : \x1b[1;92m PASTE UID ONLY \x1b[1;33mWITHOUT NAME'
    id1 = raw_input('\x1b[1;97mid : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id1, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id2 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id2, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id3 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract                               ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id3, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id4 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id4, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id5 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id5, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id6 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id6, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id7 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id7, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id8 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id8, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id9 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id9, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id10 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id10, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id11 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id11, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id12 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id12, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id13 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id13, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id14 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id14, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id15 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id15, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id16 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id16, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id17 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id17, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id18 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id18, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id19 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id19, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id20 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id20, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id21 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id21, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id22 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id22, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id23 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id23, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id24 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id24, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id25 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id25, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id26 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id26, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id27 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id27, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id28 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id28, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id29 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id29, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id30 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id30, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id31 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id31, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id32 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id32, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id33 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id33, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id34 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id34, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id35 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id35, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id36 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id36, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id37 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id37, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id38 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id38, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id39 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id39, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id40 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id40, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id41 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id41, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id42 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id42, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id43 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id43, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id44 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id44, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id45 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id45, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id46 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id46, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id47 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id47, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id48 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id48, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id49 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id49, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id50 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id50, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id51 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id51, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id52 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id52, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id53 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id53, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id54 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id54, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id55 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id55, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id56 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id56, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id57 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id57, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id58 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id58, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id59 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id59, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id60 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id60, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id61 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id61, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id62 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id62, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id63 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id63, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id64 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id64, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id65 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id65, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id66 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id66, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id67 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id67, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id68 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id68, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id69 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id69, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id70 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id70, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id71 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id71, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id72 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id72, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id73 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id73, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id74 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id74, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
    id75 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id75, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id76 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id76, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id77 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id77, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id78 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id78, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id79 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id79, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id80 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id80, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'
        
    id81 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id81, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id82 = raw_input('\x1b[1;97mid : ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id82, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id83 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id83, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id84 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id84, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id85 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id85, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id86 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id86, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id87 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id87, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id88 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id88, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id89 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id89, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id90 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id90, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id91 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id91, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id92 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id92, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id93 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id93, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id94 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id94, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id95 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id95, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id96 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id96, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id97 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id97, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id98 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id98, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id99 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id99, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id100 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id100, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id101 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id101, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id102 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id102, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id103 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id103, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id104 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id104, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id105 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id105, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id106 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id106, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id107 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id107, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id108 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id108, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id109 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id109, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

    id110 = raw_input('\x1b[1;97mId \x1b[1;32mSucessfull Extract ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id110, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + '|' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;32mAccount Is Not Public'

        
     
    print '\n\x1b[1;97m-----------------------------------------------'
    print '\x1b[1;32m IDZ DUMP SUCCESSFULLY'
    print '\x1b[1;33m ENJOY BROTHER '
    raw_input('\x1b[1;34m PRESS ENTER TO BACK MENU')
    menu()
if __name__ == '__main__':
    os.system('git pull')
    Aking()