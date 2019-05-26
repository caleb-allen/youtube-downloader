#!/usr/bin/env python3

#output new videos

import opml
import feedparser
import sys
from glob import glob
from pprint import pprint

if sys.version_info[0] < 3:
    raise Exception('Must be using Python 3')

from time import time, mktime, strptime
from datetime import datetime

if len(glob('last.txt')) == 0:
    f = open('last.txt', 'w')
    f.write(str(time()))
    f.close()

else:
    f = open('last.txt', 'r')
    content = f.read()
    f.close()

    outline = opml.parse('subs.xml')

    ptime = datetime.utcfromtimestamp(float(content))
    ftime = time()

    urls = []

    for i in range(0,len(outline[0])):
        urls.append(outline[0][i].xmlUrl)

    videos = []
    for i in range(0,len(urls)):
        # print('Parsing through channel '+str(i+1)+' out of '+str(len(urls)), end='\r')
        feed = feedparser.parse(urls[i])
        for j in range(0,len(feed['items'])):
            timef = feed['items'][j]['published_parsed']
            dt = datetime.fromtimestamp(mktime(timef))
            if dt > ptime:
                print(feed['items'][j]['link'])

    f = open('last.txt', 'w')
    f.write(str(ftime))
    f.close()
