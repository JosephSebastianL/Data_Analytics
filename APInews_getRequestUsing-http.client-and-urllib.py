# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 01:14:31 2022

@author: JosephLsebastian
"""

import http.client, urllib.parse

conn = http.client.HTTPConnection('api.mediastack.com')
# All the endpoints in this section
 
# To fetch the top headlines
conn = http.client.HTTPConnection('newsapi.org')
# To fetch news articles
conn2 = http.client.HTTPConnection('newsapi.org')
# To retrieve the sources
conn3 = http.client.HTTPConnection('newsapi.org')


params = urllib.parse.urlencode({
    'access_key': '15048bcacdf74b239f2fc78e64960bf5',
    'categories': '-general',
    'sort': 'published_desc',
    'limit': 10,
    })

conn.request('GET', '/v2/top-headlines?{}'.format(params))

conn2.request('GET', '/v2/everything?{}'.format(params))

conn3.request('GET', '/v2/sources?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))