import requests
from bs4 import BeautifulSoup
import os, io
from lxml import html
import colorama
colorama.init()

def outer_func(color):

    def inner_func(msg):
        print(f"{color}{msg}")

    return inner_func

GREEN = outer_func('\x1b[92m')
YELLOW = outer_func('\x1b[93m')
RED = outer_func('\x1b[91m')

savedir = os.getcwd()

def init():
    banner = "\nWelcome to Themarker Caf`e backupper 0.4 by Prim1Tive\npress ENTER to continue or 'c' to show credits.\n"
    if input(banner) == 'c':
        print(
            '\nThis Program was written By Prim1Tive - Michael A.\nGitHub -    https://github.com/Prim1Tive\nLinkedin -  https://www.linkedin.com/in/michael-azoulay-534651182/\n')
    GREEN('')
    blog_num = input('Blog Number:\t')
    print(f"\n\tSave Dir = {savedir}\n\tBlog number: {blog_num}")
    r = requests.get(f"http://cafe.themarker.com/blog/{blog_num}/")
    data = r.text
    return (blog_num, r)

def mkdirchange(savedir):
    try:
        os.chdir(savedir)
    except:
        os.mkdir(savedir)
        os.chdir(savedir)
    else:
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
        link.append(c[num])
        num += 4

    return link

def extract(blog_num):
    total = 1
    page = 0
    while True:
        r = requests.get(f"http://cafe.themarker.com/blog/{blog_num}/?p={page}")
        if "עדיין לא התפרסמו פוסטים בבלוג הזה." in r.text:
            GREEN("-----------DONE-----------")
            stats(page, total, blog_num)
            break
        elif page == 0:
            link = firstpage(blog_num)
        else:
            link = postlinks(blog_num, page)
        article = 0
        while True:
            try:
                # link = checkiflink(link)
                r = requests.get(f"{link[0]}")
                content = r.text
                saver(content, link, total)
                article += 1
                total += 1
            except Exception as e:
                if article != 12:
                    YELLOW(f"[!] Not all articles has been downloaded!")
                    RED(f"[+] Page {page + 1}\n[+] Articles {article}/12\n")
                else:
                    GREEN(f"[+] Page {page + 1}\n[+] Articles {article}/12\n")
                article = 0
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
            link.append(c[num])
            num += 4
    except:
        pass
    return link

def saver(content, link, total):
    with io.open(f"{link[0].split('/')[4]}.html", 'w', encoding='utf-8') as (f):
        f.write(str(content))
        f.close()
    GREEN(f"[+] {link[0]} has been backedup | total {total}")
    link.remove(link[0])

def checkiflink(link):
    if link[0:31] == 'http://cafe.themarker.com/post/':
        pass
    else:
        print(f"[!] {link[0]} is not valid | error code: 01 | can be false negative |", e)
        link.remove(link[0])
    return link

def clearposttitle(link):
    while link[(-1)] == 'post_title':
        link.remove(link[(-1)])

def main():
    blog_num, r = init()
    extract(blog_num)
    return blog_num

def table(name, topic, time, date):
    time = ''
    date = ''
    format = []
    format.append(f"{name}\t{topic}\t{time}\t{date}\n")
    print(format)

def stats(page, total, blog_num):
    GREEN(f"\n----Statistic and info----\n 1   Blog Number:\t{blog_num}\n 2   Total Articales Downloaded:\t{total}\n 3   Number Of Pages:\t{page}\n 4   Blog Link:\thttp://cafe.themarker.com/blog/{blog_num}\n 5   Saved Location: {os.getcwd()}\n\n    ")

while True:
    try:
        blog_num = main()
    except IndexError:
        RED('\n-------------------\n[!] Blog number is not valid.\n\nCommon reasons that could happen:\n\tblog is disabled / not yet created\n\tblog is private\n\tblog has been removed\n\tyou supplied a bad blog number, please read the instructions.')
    except Exception as e:
        try:
            RED(f'\n-------------------\n[!] Failed! lets try again. \n\nerror:\t{e}')
        finally:
            e = None
            del e