
import web
from config import db
from utils import serialize
from dbutils import fetch_prices

class history(object):
    def GET(self):
        data = web.input()
        url = data['url']
        ret = []
        if url:
            ret = fetch_prices(url)
        return serialize(ret)
