
import web
from config import db
from flipkart import flipkart
from utils import yqlquery, serialize
from dbutils import fetch_prices
from analyser import monthly_variance, order

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
            past_prices = fetch_prices(url)
            cur_price   = f.get_price(url)
            ret['price'] = {'past':past_prices, 'present':cur_price}

            prices = map(lambda x:x[1],past_prices)
            price_trend = order(prices)
            variances = monthly_variance(past_prices)
            variance_trend = order(variances)
            ret['trend'] = {'price':[price_trend,prices],'variance':[variance_trend,variances]}

        return serialize(ret)
