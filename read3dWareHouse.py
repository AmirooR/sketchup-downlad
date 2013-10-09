# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib2
from bs4 import BeautifulSoup
import numpy as np
from sklearn.externals import joblib

# <codecell>

url = 'http://sketchup.google.com/3dwarehouse/search?q=bus&styp=m&scoring=t&btnG=Search&reps=1&start=12'
req = urllib2.Request(url)
response = urllib2.urlopen(req)

# <codecell>

namesPage = response.read()
soup = BeautifulSoup(namesPage)

# <codecell>

ahrefs = soup.findAll('a')

# <codecell>

l = []

# <codecell>

i = 1;
for a in ahrefs:
    entry = str(a)
    if entry.find('class="dwnld"') != -1:
        l.append(a)
        down_url = 'http://sketchup.google.com'+a.get('href')
        req2 = urllib2.Request(down_url)
        response2 = urllib2.urlopen(req2)
        filename = response2.info()['Content-Disposition'].split('filename=')[1][1:-1]
        print 'Downloading %.1f KB to %s' % (int(response2.info()['Content-Length'])/1000.0, filename)
        page = response2.read()
        with open(filename,'wb') as f:
            f.write(page)

# <codecell>


