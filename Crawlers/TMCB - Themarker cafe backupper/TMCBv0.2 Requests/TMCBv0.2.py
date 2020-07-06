import requests
from bs4 import BeautifulSoup
import os
import io

'''
error codes:

01: url is not valid
related to extract(blog_num) function

'''


banner = '''
[!] Firefox needs to be installed!
[!] geckodriver.exe needs to be in PATH (C:\webdrivers\geckodriver.exe)

Welcome to Themarker Caf`e backupper by Prim1Tive
press ENTER to continue.
'''
input(banner)
print('Please wait a sec...')


### func

def init():
    blog_num = input('Blog Number:\t')
    savedir = mkdirchange()
    print(f'''\n Save Dir = '{savedir}'\n Blog number: {blog_num}''')
    r = requests.get(f'http://cafe.themarker.com/blog/{blog_num}/')
    data = r.text
    return blog_num, r


def mkdirchange():
    savedir = "C:\\webcontent\\"
    try:
        os.chdir(savedir)
    except:
        os.mkdir(savedir)
        os.chdir(savedir)
    return savedir

def firstpage(blog_num):
    r = requests.get(f"http://cafe.themarker.com/blog/{blog_num}/")
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find_all(class_='post_title')
    a = str(soup).split('<a')
    b = str(a).split('href=')
    c = str(b).split('"')
    num = 3
    link = []
    while num < 51:
        link.append((c[num]))
        num += 4
    return link

def extract(blog_num):
    total = 1
    page = 0
    while True:
        r = requests.get(f"http://cafe.themarker.com/blog/{blog_num}/?p={page}")
        if "עדיין לא התפרסמו פוסטים בבלוג הזה." in r.text:
            print("DONE")
            break
        elif page == 0:
            link = firstpage(blog_num)
        else:
            link = postlinks(blog_num, page)
        counter = 0
        while True:
            try:
                # link = checkiflink(link)
                r = requests.get(f"{link[0]}")
                counter += 1
                content = r.text
                saver(content, link, total)
                total += 1
            except Exception as e:
                print(f"[+] Page {page + 1}")
                break
        page += 1

def postlinks(blog_num, page):
    try:
        r = requests.get(f"http://cafe.themarker.com/blog/{blog_num}/?p={page}")
        soup = BeautifulSoup(r.text, 'html.parser')
        soup = soup.find_all(class_='post_title')
        a = str(soup).split('<a')
        b = str(a).split('href=')
        c = str(b).split('"')
        num = 3
        link = []
        while num < 51:
            link.append((c[num]))
            num += 4
        # clearposttitle(link)
    except:
        pass
    return link

def saver(content,link,total):
    savedir = mkdirchange()
    try:
        os.chdir(savedir)
    except:
        os.mkdir(savedir)
        os.chdir(savedir)
    with io.open(f"{link[0].split('/')[4]}.html", "w", encoding="utf-8") as f:
        f.write(str(content))
        f.close()
    print(f'[+] {link[0]} has been backedup | total {total}')
    link.remove(link[0])

def checkiflink(link):
     if link[0:31] == "http://cafe.themarker.com/post/":
         pass
     else:
         print(f'[!] {link[0]} is not valid | error code: 01 | can be false negative |', e)
         link.remove(link[0])
     return link

def clearposttitle(link):
    while link[-1] == "post_title":
        link.remove(link[-1])

### main

def main():
    blog_num, r = init()
    extract(blog_num)

main()