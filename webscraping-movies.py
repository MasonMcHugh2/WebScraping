
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


webpage = 'https://www.boxofficemojo.com/year/2024/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

tables = soup.findAll('table')
movie_table = tables[0]
rows = movie_table.findAll("tr")

print(movie_table)
##
##
##
##

