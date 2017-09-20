import xml.etree.ElementTree as ET
import urllib2
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
resp = urllib2.urlopen(url)
f = open('data.xml','wb')
f.write(resp.read())
f.close()
f = open('data.xml','r')
tree = ET.parse('data.xml').getroot()
for item in tree.findall('.//item'):
    print item.find('title').text
    if isinstance(item.find('description').text, str):
        print item.find('description').text.encode('utf-8','ignore')
    print item.find('link').text
    print "----------------------------"
