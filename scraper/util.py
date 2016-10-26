import bs4 as bs
import urllib
import requests
import shutil
import time
import signal
import os
from selenium import webdriver

# extend_page = number of times more is clicked to
# extend the content for more links
def get_all_links(link,extend_page,web_driver='firefox'):

    #setup selenium driver
    if web_driver == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.PhantomJS()
    driver.get(link)

    #load more entries with JS
    for _ in range(extend_page):
        driver.execute_script('getMore("entries")')
        time.sleep(1)
    #Wait for the page to load


    sauce = driver.page_source

    #kill the Selenium driver after being used
    driver.service.process.send_signal(signal.SIGTERM)
    driver.quit()

    # make the soup
    soup = bs.BeautifulSoup(sauce,'lxml')
    run = False
    urls = []
    for link in soup.find_all('a'):
        if link.string == 'The Food Lab' or link.string == 'More':
            run = not run
            continue
        if link.string and run:
            urls.append(link.attrs.get('href',''))

    return urls

def save_obj(obj,filename):
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(obj, out_file)

def save_images(img_urls):
    for name,url in img_urls.iteritems():
        if os.path.exists('./results/'+name):
            print 'file %s already exists! skipping...' % (name,)
            continue
        response = requests.get(url, stream=True)
        print 'saving file: ',name
        save_obj(response.raw,'./results/'+name)
        del response

def get_all_images(link):
    # make the soup
    sauce = urllib.urlopen(link).read()
    soup = bs.BeautifulSoup(sauce,'lxml')

    #get all the img links in the page
    img_urls = {}
    for img in soup.find_all('img'):
        url = img.attrs.get('data-src','')
        name = url.rsplit('/',1)[-1]
        if url and url.find('thumb') == -1:
            img_urls[name]=url

    save_images(img_urls)
