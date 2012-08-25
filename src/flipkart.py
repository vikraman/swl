
import urllib2
from utils import clean_url

root = 'http://www.flipkart.com'
product = ('<div class="fk-product-thumb fkp-medium">','</div>')
link = ('<a href="','"')
img = ('<img src="','"')
name = ('<a title="','"')
price = ('<span class="price final-price">Rs. ','</span>')
cur_price = ('<span class="price final-price our fksk-our" id="fk-mprod-our-id">Rs.<span class="small-font"> </span>','</span>')

class flipkart(object):
    def search(self, query):
        ret = []
        if query == None or len(query) == 0:
            return ret

        url = root + '/search-all?query=' + query
        u = urllib2.urlopen(url)
        page = u.read()
        result = page.find(product[0])

        while result != -1:
            link_start  = page.find(link[0],  result+1) + len(link[0])
            link_end    = page.find(link[1],  link_start+1)
            img_start   = page.find(img[0],   link_end+1) + len(img[0])
            img_end     = page.find(img[1],   img_start+1)
            name_start  = page.find(name[0],  img_end+1) + len(name[0])
            name_end    = page.find(name[1],  name_start+1)
            price_start = page.find(price[0], name_end+1) + len(price[0])
            price_end   = page.find(price[1], price_start+1)
            result = page.find(product[0],    result+1)

            url = root + page[link_start:link_end]
            cleaned_url = clean_url(url)

            d = {'link':cleaned_url, 'img':page[img_start:img_end],
                    'name':page[name_start:name_end], 'price':int(page[price_start:price_end])}
            ret.append(d)

        u.close()
        return ret

    def get_price(self, url):
        if url == None or len(url) == 0:
            return None
        
        u = urllib2.urlopen(url)
        page = u.read()
        result = page.find(cur_price[0])
        if result == -1:
            return None
        cur_price_start = result + len(cur_price[0])
        cur_price_end   = page.find(cur_price[1], cur_price_start+1)

        return int(page[cur_price_start:cur_price_end])

