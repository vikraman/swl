
import web
from config import db
from utils import serialize

class history(object):
    def GET(self):
        data = web.input()
        url = data['url']
        ret = []
        if url:
            results = db.query('select ts, price from product join product_price where url=$url',
                    vars={'url':url})
            for result in results:
                ret.append((result['ts'], result['price']))
        return serialize(ret)
