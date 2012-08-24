
import web
import config
from config import render
from index import index
from search import search

urls = (
        r'/', 'index',
        r'/search', 'search',
        )

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()
