
import web
import config
from config import render
from index import index
from search import search
from history import history

urls = (
        r'/', 'index',
        r'/search', 'search',
        r'/history', 'history'
        )

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()
