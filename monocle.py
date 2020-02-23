import requests
import socket
import time

#-----------------------
#color script

def outer_func(color):
    def inner_func(msg):
        print(f'{color}{msg}')
    return inner_func

GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')

#-----------------------
'''
# future

roblox = f'https://www.roblox.com/user's/1132851591/profile

'''

uname = input("UserName to monocle:\t")

# about
ebay = f'https://www.ebay.com/usr/{uname}'
giphy = f'https://giphy.com/explore/{uname}'
imgur = f'https://imgur.com/user/{uname}'
gravatar = f'https://en.gravatar.com/{uname}'
askfm = f'https://ask.fm/{uname}'
spotify = f'https://open.spotify.com/user/{uname}'
steam = f'https://steamcommunity.com/id/{uname}'
A500px = f'https://500px.com/{uname}'
youpic = f'https://youpic.com/photographer/{uname}/'
itchio = f'https://{uname}.itch.io'
aboutme = f'https://about.me/{uname}'
btcforum = f'https://bitcoinforum.com/profile/{uname}'
tripadvisor = f'https://www.tripadvisor.com/members/{uname}'
vsco = f'https://vsco.co/{uname}/images'
wiki = f'https://en.wikipedia.org/wiki/User:{uname}'
bandcamp = f'https://bandcamp.com/{uname}'
A9gag = f'https://9gag.com/u/{uname}'

# social
facebook = f'https://www.facebook.com/{uname}'
instagram = f'https://www.instagram.com/{uname}/'
youtube  = f'https://www.youtube.com/user/{uname}'
twitch = f'https://www.twitch.tv/{uname}'
tumbler = f'https://{uname}.tumblr.com/'
linkedin = f'https://il.linkedin.com/pub/dir?firstName={uname}&lastName=&trk=people-guest_people-search-bar_search-submit'
telegram = f'https://t.me/{uname}'
fliker = f'https://www.flickr.com/people/{uname}'
tiktok = f'https://www.tiktok.com/@{uname}'
pinterest = f'https://www.pinterest.com/{uname}/'
kik = f'https://ws2.kik.com/user/{uname}'

# dating
tinder = f'https://www.gotinder.com/@{uname}'
meetme = f'https://www.meetme.com/{uname}'

# coding
github = f'https://github.com/{uname}'
gitlab = f'https://gitlab.com/{uname}'
codepen = f'https://codepen.io/{uname}'
pastebin = f'https://pastebin.com/u/{uname}'
codecademy = f'https://www.codecademy.com/{uname}'


#------------------------



WEBSITES = [ebay,giphy,imgur,gravatar,askfm,spotify,steam,A500px,youpic,itchio,
            aboutme,btcforum,tripadvisor,vsco,wiki,bandcamp,A9gag,facebook,
            instagram,youtube,twitch,tumbler,telegram,linkedin,fliker,tiktok,
            pinterest,kik,tinder,meetme,github,gitlab,codepen,pastebin,codecademy]




def search():
    GREEN(f'[+] Searching for:\t{uname}')
    match = True
    FAILED = []
    SUCCESS = []
    try:
        for url in WEBSITES:
            requests.Timeout(0.5)
            r = requests.get(url)
            #r.close()
            if r.status_code == 200:
                GREEN(f"[+] {r.status_code}! {url} - Valid! ")
                SUCCESS.append(url)
            elif r.status_code != 200:
                RED(f"[-] {r.status_code}! {url} -  Failed! maybe this is a false positive")
                FAILED.append(url)
    except Exception as e:
        RED(f'Error has occurred {e}')



    YELLOW(f'[X] TOTAL = {len(WEBSITES)}')
    YELLOW(f'[X] SUCCESS = {len(SUCCESS)}')
    YELLOW(f'[X] FAILED = {len(FAILED)}')

    if (input('Show "SUCCESS" websites?:[y\\n]\t')) == 'Y' or 'y':
        print(SUCCESS)

search()