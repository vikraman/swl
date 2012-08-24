
from config import render_html

class Index(object):
    def GET(self):
        return render_html('Hola, welcome to Smart Wish Lists!')
