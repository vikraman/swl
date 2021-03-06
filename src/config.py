
import os
import sys
import web
from dbconfig import DBConfig

rootdir = os.path.abspath(os.path.dirname(__file__)) + '/'

dbconfig = DBConfig(rootdir + 'db.cfg').get_config()
db = web.database(
        dbn='mysql',
        db=dbconfig['DB'],
        user=dbconfig['USER'],
        pw=dbconfig['PASS']
        )

render = web.template.render(rootdir + 'templates/', base='layout')
render_html = lambda message: '<html><body>%s</body></html>'%message
