import bs4 as bs
import urllib
import requests
import shutil
from get_all_links import get_all_links

def save_obj(obj,filename):
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(obj, out_file)

def save_images(img_urls):
    for name,url in img_urls.iteritems():
        response = requests.get(url, stream=True)
        print 'saving file: ',name
        save_obj(response.raw,'results/'+name)
        del response

def get_all_images(links):
    for link in links:
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

links = get_all_links('http://www.seriouseats.com/user/profile/Goodeaterkenji',2)
get_all_images(links)
