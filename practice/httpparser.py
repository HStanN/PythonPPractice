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