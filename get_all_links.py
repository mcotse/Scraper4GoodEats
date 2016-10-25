import bs4 as bs
import urllib
import requests
import shutil
import time
from selenium import webdriver

# extend_page = number of times more is clicked to
# extend the content for more links
def get_all_links(link,extend_page):
    #fetch url with selenium
    driver = webdriver.PhantomJS()
    driver.get(link)

    #load more entries with JS
    for _ in range(extend_page):
        driver.execute_script('getMore("entries")')

    #wait for the page to load
    time.sleep(20)

    sauce = driver.page_source

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
            print link.string

    return urls