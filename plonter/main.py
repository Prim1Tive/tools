from selenium import webdriver
from time import sleep
import os
import wget
import base64



def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

def download(bios,brand,model):
    path = f'./bios/{brand}'
    print(f"Downloading BIOS from link: {bios}\nTo Folder: {path}")
    wget.download(bios,bar=bar_custom,out=f'./bios/{brand.lower()}')

def folders():
    os.popen('mkdir bios').read()
    os.popen('mkdir bios\\asus').read()
    os.popen('mkdir bios\\asrock').read()
    os.popen('mkdir bios\\gigabyte').read()
    os.popen('mkdir bios\\msi').read()
    os.popen('mkdir bios\\biostar').read()

f = open('server.py','+w')
f.write(base64.decode("aW1wb3J0IGh0dHAuc2VydmVyCmltcG9ydCBzb2NrZXRzZXJ2ZXIKaW1wb3J0IHNvY2tldAoKZGVmIGdldF9pcF9hZGRyZXNz"\
                      "KCk6CiAgICBzID0gc29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfREdSQU0pCiAgICBzLmNvbm5l"\
                      "Y3QoKCI4LjguOC44IiwgODApKQogICAgcmV0dXJuIHMuZ2V0c29ja25hbWUoKVswXQpQT1JUPTgwMDAKSVAgPSBzdHIoZ2V0"\
                      "X2lwX2FkZHJlc3MoKSkKcHJpbnQoZid7SVB9OntQT1JUfScpCgpIYW5kbGVyID0gaHR0cC5zZXJ2ZXIuU2ltcGxlSFRUUFJl"\
                      "cXVlc3RIYW5kbGVyCgp3aXRoIHNvY2tldHNlcnZlci5UQ1BTZXJ2ZXIoKCIiLCBQT1JUKSwgSGFuZGxlcikgYXMgaHR0cGQ6"\
                      "CiAgICBwcmludCgic2VydmluZyBhdCBwb3J0IiwgUE9SVCkKICAgIGh0dHBkLnNlcnZlX2ZvcmV2ZXIoKQoK))"
f.close()

def crapdisposer():
    try:
        driver.switch_to_window(driver.window_handles[0])
        while True:
            try:
                driver.switch_to_window(driver.window_handles[1])
                driver.close()
            except:
                break
    except SyntaxError:
        print('')
    driver.switch_to_window(driver.window_handles[0])
    print('crap cleaned')

allowed = 'asus','gigabyte','asrock'

# - AM4 socket
am4 = "https://www.plonter.co.il/stores_slf/main.tmpl?slf=AMD%20Socket%20AM4"
driver = webdriver.Firefox(executable_path='c:/webdrivers/geckodriver.exe')
driver.get(am4)


# - get mobos

mn = []
mb = []
if input() == 'y':
    for count in range(1,100):
        try:
            crapdisposer()
            if driver.current_url != am4:
                driver.get(am4)
            brand = driver.find_element_by_css_selector(f'div.col-md-4:nth-child({count}) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1) > b:nth-child(1)').text
            model = driver.find_element_by_css_selector(f'div.col-md-4:nth-child({count}) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(2)').text
            if brand.lower() in allowed:
                driver.find_element_by_css_selector(f'div.col-md-4:nth-child({count}) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > input:nth-child(1)').click() # click on mobo plonter webpage
                driver.find_element_by_partial_link_text('דף מוצר').click()
                print(f"({count}) {brand} {model} Downloading...")
                sleep(5)
                print('Switching Window 1')
                driver.switch_to_window(driver.window_handles[1])
                print('Switched')
                sleep(5)
            # ASUS
            if brand.lower() == 'asus':
                driver.get(driver.current_url+"HelpDesk_Download/")
                sleep(5)
                print('Download page')
                driver.find_element_by_css_selector('.productSupportSubTab1 > li:nth-child(2)').click()
                if 'beta' in driver.find_element_by_css_selector('div.productSupportDriverBIOSBox:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)').text:
                    print('BETA VERSION!')
                bios = driver.find_element_by_css_selector('div.productSupportDriverBIOSBox:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2)').get_attribute('href')
                download(bios,brand,model)
            if brand.lower() == 'gigabyte':
                driver.get(driver.current_url+'support#support-dl-bios')
                sleep(5)
                print('Download page')
                bios = driver.find_element_by_css_selector('div.div-table-body-BIOS:nth-child(2) > div:nth-child(4) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)').get_attribute('href')
                download(bios,brand,model)
            if brand.lower() == 'asrock':
                driver.get(driver.current_url+"#BIOS")
                sleep(5)
                print('Download page')
                bios = driver.find_element_by_css_selector('#BIOS > table:nth-child(5) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)').get_attribute('href')
                download(bios,brand,model)
                # MORE DRIVERS.......
                print('What a plonter')
            if brand.lower() == 'msi':
                print('What a plonter')
            driver.implicitly_wait(1)
        except Exception as e:
            print('error ', e)
            driver.switch_to_window(driver.window_handles[0])
else:
    print('lel')