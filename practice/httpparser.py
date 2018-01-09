from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    dates = []
    titles = []
    locations = []

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        self.date_flag = 0
        self.title_flag = 0
        self.location_flag = 0
        self.events = []
        self.date = ""
        self.title = ""
        self.location = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1
        if tag == 'time' and self.flag == 1:
            self.date_flag = 1
        if tag == 'span' and self.flag == 1:
            self.location_flag = 1
        if tag == 'a' and self.flag == 1:
            self.title_flag = 1

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.flag == 1 and self.date_flag == 1:
            self.dates.append(data)
            self.date_flag = 0
        if self.flag == 1 and self.location_flag == 1:
            self.locations.append(data)
            self.location_flag = 0
        if self.flag == 1 and self.title_flag == 1:
            self.titles.append(data)
            self.title_flag = 0

parser = MyHTMLParser()
with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')
parser.feed(data)
dates = parser.dates
locations = parser.locations
titles = parser.titles
for x in range(len(dates)):
    print('----------------------------------------------------')
    print('时间：%s' % dates[x])
    print('地点：%s' % locations[x])
    print('主题：%s' % titles[x])

#Result

#----------------------------------------------------
#时间：22 Jan. – 24 Jan.
#地点： 2018
#主题：PyCascades 2018
#----------------------------------------------------
#时间：24 Jan. – 29 Jan.
#地点：Granville Island Stage, 1585 Johnston St, Vancouver, BC V6H 3R9, Canada
#主题：PyCon Cameroon 2018
#----------------------------------------------------
#时间：03 Feb. – 05 Feb.
#地点： 2018
#主题：FOSDEM 2018
#----------------------------------------------------
#时间：08 Feb. – 12 Feb.
#地点：Limbe, Cameroon
#主题：PyCon Pune 2018
#----------------------------------------------------
#时间：09 Feb. – 12 Feb.
#地点： 2018
#主题：PyCon Colombia 2018
#----------------------------------------------------
#时间：10 Feb. – 12 Feb.
#地点：ULB Campus du Solbosch, Av. F. D. Roosevelt 50, 1050 Bruxelles, Belgium
#主题：PyTennessee 2018
#----------------------------------------------------
#时间：16 Dec. – 17 Dec.
#地点： 2018
#主题：PyCon Pakistan
#----------------------------------------------------
#时间：09 Dec. – 10 Dec.
#地点：Pune, India
#主题：PyCon Indonesia 2017
