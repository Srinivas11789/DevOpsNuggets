"""
 *** Brute Force Python Script ***

- Reference: https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python

"""

import itertools
import urllib2

url = "http://127.0.0.1/rate/3"


for item in itertools.product(range(10), repeat=6):
        try:
	    response = urllib2.urlopen(url)
            print "Got response for: "+str(item)
        except:
            print "Rate limited for: "+str(item)
