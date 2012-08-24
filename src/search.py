
import web
from flipkart import flipkart
from utils import serialize

class search(object):
    def GET(self):
        data = web.input(query='')
        f = flipkart()
        ret = f.search(data['query'])
        return serialize(ret)
