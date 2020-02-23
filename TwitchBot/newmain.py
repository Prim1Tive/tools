# Prim1Tive - Twitch bot v2.2
# V2 updates:
# Improved Driver installer
# Colors are back

# imports
from selenium import webdriver
import os
import subprocess
from time import sleep
from random import randint
from multiprocessing import Pool
from importlib import reload
import banner

# color script
def outer_func(color):
    def inner_func(msg):
        print(f'{color}{msg}')
    return inner_func
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')
PINK = outer_func('\033[95m')

# Load default vars
stream = None
top_streamer = 2
lst_streamer = 10
top_game = 2
lst_game = 10
follow_mod = ''
msg = ''
game_list = []
game_add = 2

# Load css selectors
login_btn = '.anon-user > div:nth-child(1) > button:nth-child(1)'
login_username = '#login-username'
login_password = '.anon-user > div:nth-child(1) > button:nth-child(1)'
login_login = '.anon-user > div:nth-child(1) > button:nth-child(1)'
follow_btn = '.follow-btn__follow-btn-container'
unfollow_btn = '.follow-btn__follow-btn > div:nth-child(1) > button:nth-child(1)'
rule_btn = 'button.tw-border-bottom-left-radius-large'
chat_area = 'textarea.tw-block'
chat_snd = '.tw-align-content-center > div:nth-child(3) > button:nth-child(1)'

def login(username, password):  # login automation, maybe auto grab auth from google/facebook automaticly someday amen
    if username and password == "bot":
        username = "Prim1Tivebox"
        password = "PC87P_GMU+2KcH9"
    elif username == 'cookie':  # in work
        print('in work..')
        try:  # page open WIP
            driver.add_cookie('%22authToken%22:%227e6i85gy2l7p2q0v9ux5n0z13d5to6%22%2C%22displayName%22:%22prim1tivebox%22%2C%22id%22:%22491023454%22%2C%22login%22:%22prim1tivebox%22%2C%22roles%22:{%22isStaff%22:false}%2C%22version%22:2')
            driver.get('https://www.twitch.tv/')
            sleep(3)
        except Exception as e:
            RED(f"[!] Error: {e}")
    if username != 'cookie' or 'bot':
        try:  # page open
            driver.get('https://www.twitch.tv/')
            sleep(3)
        except Exception as e:
            RED(f"[!] Error: {e}")

    try:
        PINK(driver.title)
        print(driver.current_url)
        login_btn = driver.find_element_by_css_selector('.anon-user > div:nth-child(1) > button:nth-child(1)').click()
        sleep(1)
        uname_inp = driver.find_element_by_css_selector("#login-username").send_keys(f'{username}')
        upass_inp = driver.find_element_by_css_selector('#password-input').send_keys(f'{password}')
        sleep(1)
        login_btn = driver.find_element_by_css_selector('div.tw-mg-t-2:nth-child(3) > button:nth-child(1)').click()
        sleep(1)
        YELLOW("")
        if input("\n[?] There are any Bot flagger?[y/n] - [reCAPTCHA and alike...]: ") == 'y' or 'Y':
            RED('')
            input(f'[!] ok then solve it... im not an AI you know... tell me when done... [press any key]')
    except Exception as e:
        RED(f"[!] Error: {e}")

def chatHandler(msg, follow_mod, stream, game):  # Handle chat
    if follow_mod == 'y' or 'Y' or '':  # Follow mod
        followMod(stream)
    try:  # send keys, also get chat rules popup open
        driver.find_element_by_css_selector(chat_area).send_keys(msg)
        sleep(1)
    except:
        RED("[!] Error: No Element found, Page didn't load?")
    try:  # check for rules
        driver.find_element_by_css_selector(rule_btn).click()  # if fail go except
        sleep(1)
        driver.find_element_by_css_selector(chat_area).send_keys(msg)  # if success send keys again
    except:
        GREEN('[+] No Rules Ⓐ')
    try:  # click send button
        driver.find_element_by_css_selector(chat_snd).click()
        GREEN(f"[+] Sending: {msg} to {stream[0]}on - {game[0]}")
        sleep(1)
    except:  # if it fails, probably 'followers chat'
        YELLOW(f"[!] Error: Chat for followers ONLY!, you need to follow {stream[0]}\n    (it take's some time even if you just followed this streamer. Follow mod might help)")
        RED(f"[!] Error Sending: {msg} to {stream[0]}on - {game[0]}")

def followMod(stream):  # click on follow
    try:
        sleep(1)
        driver.find_element_by_css_selector('.tw-c-background-accent-alt-2 > button:nth-child(1)').click()
        GREEN(f'[+] Successfully Followed {stream[0]}')

    except:
        YELLOW(f'[-] Already Following {stream[0]}')

def unFollowMod(stream):  # click on unfollow
    try:
        sleep(1)
        driver.find_element_by_css_selector('.follow-btn__follow-btn > div:nth-child(1) > button:nth-child(1)').click()
        GREEN(f'[+] Successfully UnFollowed {stream[0]}')
    except:
        YELLOW(f'[-] Not Following {stream[0]}')

def changeMenu(top_game, lst_game, top_streamer, lst_streamer, msg):
    os.system('cls')
    RED(banner.banner)
    PINK(banner.subBanner)
    changeMenu = f'''

     Change:
     1) Top Game        -   {top_game, lst_game}
     2) Top Streamer    -   {top_streamer, lst_streamer}
     3) Change Message  -   {msg}

    '''
    GREEN(changeMenu)
    menuChoose = input(f'{changeMenu}\t >\t')
    while True:
        if menuChoose == "1":
            top_game = input('[?] Top:\t')
            lst_game = input('[?] lst:\t')
            return top_game, lst_game
        elif menuChoose == "2":
            top_streamer = input('[?] Top:\t')
            lst_streamer = input('[?] lst:\t')
            return top_streamer, lst_streamer
        elif menuChoose == "3":
            msg = input('[?] msg:\t')
            return msg
        else:
            break

def checkforBan(): # check if user got sub ban (also real ban?)
    try:
        driver.find_element_by_css_selector(chat_area).send_keys(' ')
        driver.find_element_by_css_selector(chat_area).send_keys(Keys.ENTER)
        chat_ban = driver.find_element_by_css_selector('.tw-balloon--left')
        chat_ban.split('have')
        chat_ban = f'Ban is done in : {chat_ban[1]}'
        print(chat_ban.text)
    except:
        print('no ban')

def intervals(): # interval selection
    while True:
        try:
            interval = input('[?] Intervals in seconds [default = 0s]:\t') or 0
            interval = int(interval)
            print(f'[+] Sleep for: {interval} seconds after each message sending')
            return interval
        except:
            print(f'[!] Error: {interval} Not a number')

def intervals_start(interval):
    sleep(interval)

def drivers_install(): # web driver checker and isntaller

    # default vars for this func
    FOLDER = 'c:\webdrivers'
    FILE = 'geckodriver.exe'

    # starting
    print('''
    Starting Please wait for input!
    • if firefox is not installed you need to install it
    Quick link:
    https://www.mozilla.org/en-US/firefox/download/thanks/
    ''')

    # start
    print('----------Checking for webdriver--------------')

    # folder check
    ERRCODE, OUTPUT = subprocess.getstatusoutput('mkdir c:\webdrivers')
    if ERRCODE == 1:
        GREEN(f'[V] {FOLDER} Found!')
    elif ERRCODE == 0:
        RED(f'[X] Created {FOLDER}\ ')

    # file check
    ERRCODE, OUTPUT = subprocess.getstatusoutput('dir c:\webdrivers')
    if FILE in OUTPUT:
        GREEN(f'[V] {FILE} Found!')
    else:
        RED(f'[X] {FILE} Is missing from {FOLDER}\ ')
        YELLOW(f'[-] Trying to move {FILE}')
        ERRCODE, OUTPUT = subprocess.getstatusoutput('move geckodriver.exe C:\webdrivers\geckodriver.exe')
        sleep(2)
        if ERRCODE == 0:
            GREEN(f'[V] {FILE} Moved Successfully!')
        if ERRCODE == 1:
            RED(f'[X] {FILE} was not found in {FOLDER}\,\n\t please get the driver at: https://github.com/mozilla/geckodriver/releases/')
    print('----------------------------------------------')
    sleep(1)


def menus(msg):
    os.system('cls')
    RED(banner.banner)
    PINK(banner.subBanner)
    menu = '''

     Mod:

     1) Stupid   -   Random streamers > msg                 c) Change Menu
     2) Single   -   Single streamer > msg
     3) by game  -   Random streamers by game > msg 
     4) UnFollow Everyone


    '''
    try:
        menuChoose = input(f'{menu}\t >\t')
        if menuChoose == "1":
            follow_mod = input("[?] Follow streamer? [y/n]:\t")  # == 'Y' or 'y' or '':
            Stupid(msg, follow_mod)
        elif menuChoose == "2":
            follow_mod = input("[?] Follow streamer? [y/n]:\t")  # == 'Y' or 'y' or '':
            streamer_name = input("[?] Streamer name:\t") or 'augustuwu'
            mints = input("[?] Intervals [30]:\t") or 30
            Single(streamer_name, mints)
        elif menuChoose == "3":
            follow_mod = input("[?] Follow streamer? [y/n]:\t")  # == 'Y' or 'y' or '':
            byGame(msg, follow_mod)
        elif menuChoose == "4":
            unFollowEveryOne()
        elif menuChoose == "c":
            changeMenu(top_game, lst_game, top_streamer, lst_streamer, msg)
            return top_game, lst_game, top_streamer, lst_streamer, msg
        elif menuChoose == '' or ' ':
            menus(msg)
        else:
            RED(f"[!] Error: Invalid selection '{menuChoose}'")  # before refresh to see the msg
            sleep(1)
            menus(msg)
    except Exception as e:
        RED(f'[!] {e}')
        menus(msg)


# Mods:-----------------------------------------------------------

def Stupid(msg, follow_mod):
    msg = input('[?] Your msg [ Hi! Great stream you got there ]:\t') or 'Hi! Great stream you got there'
    GREEN(f'[+] Your Message: {msg}')
    YELLOW("-_-_-_-_-_-_-_-_-_-LOGS_-_-_-_-_-_-_-_-_-_-")
    try:
        while True:
            try:
                try:  # page open
                    driver.get('https://www.twitch.tv/directory')
                    sleep(3)
                except Exception as e:
                    # print(f"[!] Error: page open | {e}")
                    sleep(3)
                try:  # choose random game
                    driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/main/div/div[3]/div/div/div/div[4]/div/div[1]/div[{randint(top_game, lst_game)}]/div/div/div/div/div[1]/div/a/div/div[5]/div/div/div/div/img').click()
                    sleep(3)
                    game = driver.title.split('- Twitch')
                except Exception as e:
                    # print(f"[!] Error: choose random game | {e}")
                    sleep(3)

                try:  # choose random streamer
                    driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/main/div/div[3]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[{randint(top_streamer,lst_streamer)}]/div/div/div/div/div[1]/a/div/div/div[5]/div[1]/div/div/div[2]/img').click()
                    sleep(3)
                    stream = driver.title.split('- Twitch')
                except Exception as e:
                    # print(f"[!] Error: choose random streamer | {e}")
                    sleep(3)
                chatHandler(msg, follow_mod, stream, game)
            except Exception as e:
                RED(f"[!] Error: Something went wrong | {e}")
                sleep(3)
            GREEN("[+] Next Stream.\n")
            sleep(1)
    except KeyboardInterrupt:
        RED('[!] Abort!')


def Single(streamer_name, mints):
    msg = input('[?] Your msg [ Hi! Great stream you got there ]:\t') or 'Hi! Great stream you got there'
    GREEN(f'[+] Your Message: {msg}')
    try:  # page open specific streamer
        driver.get(f'https://www.twitch.tv/{streamer_name}')
        stream = driver.title
        stream = stream.split('- Twitch')
        sleep(3)
    except Exception as e:
        # print(f"[!] Error: page open | {e}")
        sleep(3)
    try:
        while True:
            try:  # idiotic, please replace
                game
            except:
                game = stream
            chatHandler(msg, follow_mod, stream, game)
            try:
                sleep(int(mints))  # intervals
            except ValueError:
                YELLOW(f'[-] Value Error: {mints} is not a number')
                break
    except KeyboardInterrupt:
        RED('[!] Abort!')


def byGame(msg, follow_mod):

    # default vars for this func
    games = []
    game_add = 2
    count = 0
    msg = input('[?] Your msg [ Hi! Great stream you got there ]:\t') or 'Hi! Great stream you got there'

    try:
        while True:
            interval = 0
            interval = input('[?] Intervals in seconds [default = 0s]:\t') or 0
            print(f'[+] Sleep for: {interval} seconds after each message Sent')
            break
            # return intervals
    except:
        print(f'[!] Error: {interval} Not a number')

    GREEN(f'[+] Your Message: {msg}')
    YELLOW("-_-_-_-_-_-_-_-_-_-LOGS_-_-_-_-_-_-_-_-_-_-")
    try:
        try:  # page open
            driver.get('https://www.twitch.tv/directory')
            sleep(3)
        except Exception as e:
            print(f"[!] Error: page open | {e}")
            RED(f"[!] Error: page didn't open")
            sleep(3)
        GREEN(f'[+] Creating list')
        while True:  # Creating an updated list for all games
            try:
                # games.append(driver.find_element_by_css_selector(f'.tw-tower > div:nth-child({game_add}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > h3:nth-child(1)').get_attribute('title'))
                game_list.append(driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div/div[4]/div/div[1]/div[{game_add}]/div/div/div/div/div[1]/div/div/div/div/span/a/h3').get_attribute('title'))
                game_add += 1
            except Exception as e:
                GREEN('[+] Finished.')
                break
        print('-_-_-_-_-_-_-_-_-_-Games-_-_-_-_-_-_-_-_-_-')
        for games in game_list:  # print list
            count += 1
            print(f'[{count}] - {games}')
        print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        while True:  # select game
            try:
                game_select = int(input('\t >\t')) + 1
                if game_select <= 1 or '':
                    game_select = 2
                break
            except ValueError:
                print("[!] Error: Invalid number")
        try:  # execute game selection
            driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/main/div/div[3]/div/div/div/div[4]/div/div[1]/div[{game_select}]/div/div/div/div/div[1]/div/a/div/div[5]/div/div/div/div/img').click()
            sleep(3)
            game = driver.title.split('- Twitch')
            game_url = driver.current_url
        except:
            print(f"[!] Error: Didnt work, The number {game_select} is not Valid")
        finally:
            while True:
                try:  # choose random streamer
                    driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/main/div/div[3]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[{randint(top_streamer,lst_streamer)}]/div/div/div/div/div[1]/a/div/div/div[5]/div[1]/div/div/div[2]/img').click()
                    sleep(3)
                    stream = driver.title.split('- Twitch')
                except Exception as e:
                    print(f"[!] Error: choose random streamer | {e}")
                    sleep(3)
                finally:
                    chatHandler(msg, follow_mod, stream, game)
                try:  # reopen game page
                    driver.get(game_url)
                    sleep(3)
                except Exception as e:
                    # print(f"[!] Error: page open | {e}")
                    RED(f"[!] Error: page didn't open | {e}")
                    sleep(3)
    except Exception as e:
        RED(f"[!] Error: byGame() Something went wrong | {e}")

def unFollowEveryOne():
    while True:
        driver.get('https://www.twitch.tv/directory/following/channels')
        sleep(3)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/main/div[1]/div[3]/div/div/div/div/div[4]/div[1]/div/div/div[3]/div/div[2]/a/div/figure/img').click()
            sleep(3)
            try:
                stream = driver.title.split('- Twitch')
                unFollowMod(stream)
            except Exception as e:
                RED(f'[!] Error: {e}')
        except:
            GREEN('[+] No remaining streamers to unfollow')
            break

def login_handler():
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    username = input('[?] Username:\t')
    password = input('[?] Password:\t')
    YELLOW("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    YELLOW(
        "[-] Info: If Login Fails, try to login by yourself\n    If not logged in it will create false positive results")
    YELLOW("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    GREEN("\n[+] Working...\n")
    login(username, password)



# ----------------------------------------------------------


def startup():
    os.system('cls')
    drivers_install()
    login_handler()

def main():
    while True:
        RED(banner.banner)
        PINK(banner.subBanner)
        menus(msg)

driver = webdriver.Firefox(executable_path=r'C:\webdrivers\geckodriver.exe')
startup()
main()