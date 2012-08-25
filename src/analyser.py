
import re
import datetime

def mean(l):
    if not l:
        return 0
    return float(sum(l))/len(l)

def variance(l):
    if not l:
        return 0
    m = mean(l)
    s = 0
    for i in l:
        s += (i - m)*(i - m)
    return float(s)/len(l)

def monthly_variance(p):
    l = len(p)
    s = sorted(p)
    dt = lambda s:datetime.datetime(*map(int, re.split('[^\d]', s)[:-1]))
    first_day = dt(s[0][0])
    last_day  = dt(s[l-1][0])
    begin = [first_day.year, first_day.month]
    end   = [last_day.year,  last_day.month]
    cur = begin
    months = []
    variances = []
    si = 0
    while cur <= end:
        months.append([cur[0],cur[1]])
        d = dt(s[si][0])
        l = []
        while d.year == cur[0] and d.month == cur[1]:
            if si >= len(s):
                break
            d = dt(s[si][0])
            l.append(s[si][1])
            si += 1
        variances.append(variance(l))

        cur[1] += 1
        if cur[1] > 12:
            cur[1] -= 12
            cur[0] += 1

    return variances

def order(p, error=0):
    state = ['decreasing', 'increasing', 'constant', 'varying']
    l = len(p)
    if l <= 1:
        return state[0]
    pp = zip(p,p[1:])
    if all(x < y for x,y in pp):
        return state[0]
    if all(x > y for x,y in pp):
        return state[1]
    if all(x == y for x,y in pp):
        return state[2]
    return state[3]
