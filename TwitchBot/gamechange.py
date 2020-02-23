'''

https://dashboard.twitch.tv/u/prim1tive/stream-manager

.quick-actions > div:nth-child(1) > button:nth-child(1) # edit
div.tw-mg-b-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > textarea:nth-child(1) # box
button.tw-align-items-center:nth-child(2) # btn


in work!!
'''

import os
from time import sleep
from selenium import webdriver

def login(username, password):  # login automation, maybe auto grab auth from google automaticly someday amen
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

edit_btn = '.quick-actions > div:nth-child(1) > button:nth-child(1)' # css
txt_box = '//*[@id="dropdown-search-input"]' # xpath
done_btn = 'button.tw-align-items-center:nth-child(2)' # css

driver = webdriver.Firefox(executable_path=r'C:\webdrivers\geckodriver.exe')

URL = f'https://dashboard.twitch.tv/u/{username}/stream-manager'

driver.get(URL)

sleep(3)

game_playing = "Tom Clancy's Rainbow Six: Siege"
# .send_keys(game_playing)

driver.find_element_by_css_selector(edit_btn).click()
sleep(1)
driver.find_element_by_xpath('//*[@id="dropdown-search-input"]').send_keys(game_playing)
sleep(1)
driver.find_element_by_css_selector(done_btn).click()

try:
    os.system('tasklist')
except:
    print()
games = 'RainbowSix.exe' , 'csgo.exe'

prossess = os.popen('tasklist').read()
prossess = prossess.split('\n')
if games in prossess:
    print('ok')
