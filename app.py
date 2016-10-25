import bs4 as bs
import urllib

#make the soup
sauce = urllib.urlopen('http://www.seriouseats.com/2016/10/the-food-lab-how-to-bake-bacon-in-the-oven.html').read()
soup = bs.BeautifulSoup(sauce,'lxml')

#get all the img links
img_links = []
for img in soup.find_all('img'):
    link = img.attrs.get('data-src','')
    name = link.rsplit('/',1)[-1]
    img_links.append({name:link}) if link else None

print img_links
