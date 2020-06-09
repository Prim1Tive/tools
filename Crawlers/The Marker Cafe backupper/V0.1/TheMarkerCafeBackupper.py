from selenium import webdriver
import requests
import os
import io


banner = '''
[!] Firefox needs to be installed!
[!] geckodriver.exe needs to be in PATH (C:\webdrivers\geckodriver.exe)

Welcome to Themarker Caf`e backupper by Prim1Tive
press any key to continue.
'''
input(banner)
print('Please wait a sec...')

#### init
w = webdriver.Firefox(executable_path="c:\webdrivers\geckodriver.exe")

def init():
    while True:
        try:
            blog_num = int(input('Blog Number:\t'))
        except ValueError:
            print("Not an integer")
            continue
        if blog_num < 1:
            print('0 is not a Blog number')
        else:
            break
    savedir = mkdirchange()
    print(f'''\n Save Dir = '{savedir}'\n Blog number: {blog_num}''')
    return blog_num

#### Functions
def mkdirchange():
    savedir = "C:\\webcontent\\"
    try:
        os.chdir(savedir)
    except:
        os.mkdir(savedir)
        os.chdir(savedir)
    return savedir

def extract(blog_num):
    page = 0
    while True:
        r = requests.get(f"http://cafe.themarker.com/blog/{blog_num}/?p={page}")
        if "עדיין לא התפרסמו פוסטים בבלוג הזה." not in r.text:
            w.get(f"http://cafe.themarker.com/blog/{blog_num}/?p={page}")
            for count in range(1,12):
                name = w.find_element_by_css_selector(f"div.blog_entry:nth-child({count}) > h3:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text
                link = w.find_element_by_css_selector(f"div.blog_entry:nth-child({count}) > h3:nth-child(1) > span:nth-child(1) > a:nth-child(1)").get_attribute('href')
                r = requests.get(f"{link}")
                content = r.text
                name = name.split()
                saver(content, link)
        else:
            break
        page += 1

def saver(content,link):
    savedir = mkdirchange()
    try:
        os.chdir(savedir)
    except:
        os.mkdir(savedir)
        os.chdir(savedir)
    with io.open(f"{link.split('/')[4]}.html", "w", encoding="utf-8") as f:
        f.write(str(content))
        f.close()

#### main
def main():
        blog_num = init()
        extract(blog_num)

main()
# 16275