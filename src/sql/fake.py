
import time
import datetime
from config import db

now = int(time.time())

T = 400
while T >= 0:
    d = datetime.datetime.fromtimestamp(now)
    if T < 200:
        price = 38999
    else:
        price = 37990
    db.insert('product_price',id=1,ts=d,price=price)
    now -= 86400
    T -= 1
