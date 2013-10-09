# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import numpy as np
from sklearn.externals import joblib
import os.path

def downloadAllModels( query_word, num_pages):
	for i in range(num_pages):
		print 'Downloading page %d' % (i+1)
		downloadModelWithPage( query_word, i)

def downloadModelWithPage( query_word, num_page):
	url = 'http://sketchup.google.com/3dwarehouse/search?q='+query_word+'&styp=m&scoring=t&btnG=Search&reps=1&start='+str( num_page*12)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	namesPage = response.read()
	soup = BeautifulSoup(namesPage)
	ahrefs = soup.findAll('a')

	i = 1;
	for a in ahrefs:
    		entry = str(a)
    		if entry.find('class="dwnld"') != -1:
        		down_url = 'http://sketchup.google.com'+a.get('href')
        		req2 = urllib2.Request(down_url)
        		response2 = urllib2.urlopen(req2)
        		filename = response2.info()['Content-Disposition'].split('filename=')[1][1:-1]
			if os.path.isfile(filename):
				print 'File: %s already exists' % (filename)
			else:
				file_size = int(response2.info()['Content-Length'])
        			print 'Downloading %.1f KB to %s ...' % (file_size/1000.0, filename)

				f = open(filename, 'wb')
				file_size_dl = 0
				block_size = 8192
				while True:
					buffer = response2.read(block_size)
					if not buffer:
						break

					file_size_dl += len(buffer)
					f.write(buffer)
					status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl* 100. / file_size)
					status = status + chr(8)*(len(status)+1)
					print status,
				f.close()
#	page = response2.read()
#       			with open(filename,'wb') as f:
#           				f.write(page)


if __name__ == '__main__':
	downloadAllModels('aeroplane',1)
