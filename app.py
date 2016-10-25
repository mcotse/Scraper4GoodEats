import bs4 as bs
import urllib
import requests
import shutil

#make the soup
sauce = urllib.urlopen('http://www.seriouseats.com/2016/10/the-food-lab-how-to-bake-bacon-in-the-oven.html').read()
soup = bs.BeautifulSoup(sauce,'lxml')

#get all the img links
img_urls = {}
for img in soup.find_all('img'):
    url = img.attrs.get('data-src','')
    name = url.rsplit('/',1)[-1]
    if url:
        img_urls[name]=url

# print img_urls
for name,url in img_urls.iteritems():
    response = requests.get(url, stream=True)
    with open('results/'+name, 'wb') as out_file:
        print 'getting file: ',name
        shutil.copyfileobj(response.raw, out_file)
    del response
