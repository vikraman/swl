
import web
from config import db
from flipkart import flipkart
from utils import yqlquery, keyfind
from dbutils import fetch_prices

class product(object):
    def GET(self):
        data = web.input()
        url = data['url']
        ret = {}
        if url:
            results = db.select('product', what='name,url', where='url=$url', vars={'url':url})
            if len(results):
                result = results[0]
                ret['name'], ret['url'] = result['name'], result['url']
            
            query = "select * from contentanalysis.analyze where text='%s'" % ret['name']
            anal = yqlquery(query)
            try:
                entities = anal['query']['results']['entities']['entity']
                for entity in entities:
                    if entity['types']['type'].get('region'):
                        ret['region'] = entity['types']['type']['region']
                        break
            except (KeyError, TypeError, ValueError):
                ret['region'] = 'unknown'

            f = flipkart()
            ret['price'] = {'past':fetch_prices(url), 'present':f.get_price(url)}

        return ret
