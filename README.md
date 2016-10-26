## Scraper4GoodEats
A scraper to get all the amazing images from Kenji@FoodLab's Posts
Can be applied to any profile at GoodEats
Utilizes Selenium,PhantomJS(or firefox) and beautifulSoup4

### Usage
 - Ensure PhantomJS or Firefox is installed
 - Setup a virtualenv and activate it
 - Run `pip install requirements.txt`
 - Run scraper/app.py with 2 arguments following:
   - args0: url
   - args1: number of times the more button is executed (more posts to scrape)
 - Example `python scraper/app.py link 20`
