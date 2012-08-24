
import web
import config
from config import render
from index import Index
from search import Search

urls = (
        r'/', 'Index',
        r'/search', 'Search',
        )

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()
