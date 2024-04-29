import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapter = random.randrange(1,22)
if chapter<10:
    chapter = '0'+str(chapter)
else:
    chapter = str(chapter)

webpage = 'https://ebible.org/asv/JHN'+chapter+'.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

page_verses = soup.findAll('div',class_='p')

my_verses =[]

for section_verses in page_verses:
    print(section_verses.text)