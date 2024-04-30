from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
import plotly.graph_objects as plt
import re


url = 'http://quotes.toscrape.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url,headers=headers)
page = urlopen(req).read()			
soup = BeautifulSoup(page, 'html.parser')

title = soup.title
print(title.text)