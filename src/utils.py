
import json
import datetime
import urllib2
from urllib import urlencode
from urlparse import urlparse, urlunparse, parse_qs

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def serialize(obj):
    return json.dumps(obj, cls=JSONEncoder)

def deserialize(obj):
    return json.JSONDecoder().decode(obj)

def clean_url(url):
    blacklist = ['ref'];
    urlobj = urlparse(url)
    query = parse_qs(urlobj.query)
    for item in blacklist:
        if query.get(item):
            del(query[item])
    urlobj = urlobj._replace(query=urlencode(query, True))
    return urlunparse(urlobj)

def yqlquery(query):
    root = 'http://query.yahooapis.com/v1/public/yql?'
    query = urlencode({'diagnostics':'true','format':'json','q':query})
    url = root + query
    u = urllib2.urlopen(url)
    return deserialize(u.read())

def keyfind(d,key):
    if key in d:
        yield d[key]
    for k in d:
        if isinstance(d[k], list):
            for i in d[k]:
                for j in keyfind(i,key):
                    yield j
