
from config import db

def fetch_prices(url):
    ret = []
    if url:
        results = db.query('select ts, price from product natural join product_price where url=$url',
                vars={'url':url})
        for result in results:
            ret.append((result['ts'], result['price']))
    return ret
