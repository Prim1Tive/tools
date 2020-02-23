from selenium import webdriver
from random import randint
from time import sleep
from selenium.webdriver import remote

driver = webdriver.Firefox()


driver.get('https://badoo.com')


like = 'div.encounters-actions__main-items:nth-child(2) > div:nth-child(1) > div:nth-child(1)'
unlike = 'div.encounters-actions__main-items:nth-child(2) > div:nth-child(2) > div:nth-child(1)'
def like():
    driver.find_element_by_css_selector(like).click()


def unlike():
    driver.find_element_by_css_selector(unlike).click()


def randomnedd():
    try:
        try:
            while True:
                chance = randint(1,100)
                if chance >= 75:
                   print(f"{chance}")
                   unlike()
                   sleep(0.5)
                else:
                    print(f'Chance! {chance}')
                    like()
                    sleep(0.5)
        except:
            sleep(2)
            print('Popup handler')
            driver.find_element_by_css_selector('div.btn:nth-child(2)').click()
    except:
        print('quited')



driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
import requests
c = {'name': 's1', 'value': 's1%3A9999%3Al0FK4SqKqOeCyPSUE01fXPUJRoWp5jX61hIihwVI', 'path': '/', 'domain': '.badoo.com', 'secure': False, 'httpOnly': True}, {'name': 'session_cookie_name', 'value': 's1', 'path': '/', 'domain': '.badoo.com', 'secure': False, 'httpOnly': True}, {'name': 'device_id', 'value': "01a6919a-919a-9aa1-a13a-3a417aba47de", 'path': '/', 'domain': '.badoo.com', 'secure': False, 'httpOnly': False, 'expiry': 4735989817}