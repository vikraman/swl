
import web
import config
from config import render
from index import index
from search import search
from history import history
from product import product

urls = (
        r'/', 'index',
        r'/search', 'search',
        r'/history', 'history',
        r'/product', 'product'
        )

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()
