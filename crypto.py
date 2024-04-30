from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


url = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url,headers=headers)
page = urlopen(req).read()			
soup = BeautifulSoup(page, 'html.parser')

title = soup.title
print(title.text)

currency = soup.findAll("td")
i = 1
stock = 1
for row in currency[1:6]:
    name = currency[i+1].text
    price = float(currency[i+2].text.strip('$').replace(',',''))
    change = float(currency[i+4].text.strip('%'))

    #price = round(price,2)

    corr_price = price+((price*change)/100)
    corr_price = round(corr_price,2)

    print()
    print(f"Stock #: {stock}")
    print(f"Name: {name}")
    print(f"Current Price: ${price:,.2f}")
    print(f"%Change: {change}%")
    print(f"Corresponding Price: ${corr_price:,}")
    i += 11
    stock +=1
