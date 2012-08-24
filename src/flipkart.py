
import urllib2

root = 'http://www.flipkart.com'
product = ('<div class="fk-product-thumb fkp-medium">','</div>')
link = ('<a href="','"')
img = ('<img src="','"')
price = ('<span class="price final-price">Rs. ','</span>')

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
            price_start = page.find(price[0], img_end+1) + len(price[0])
            price_end   = page.find(price[1], price_start+1)
            result = page.find(product[0],    result+1)

            d = {'link':root + page[link_start:link_end], 'img':page[img_start:img_end],
                    'price':int(page[price_start:price_end])}
            ret.append(d)

        u.close()
        return ret
