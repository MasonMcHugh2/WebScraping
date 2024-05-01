from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#import openpyxl as xl
#from openpyxl.styles import Font
import plotly.graph_objects as plt
import re
from plotly import offline

list_authors = []
list_quotes = []
list_tags = []

start_page = 1
for i in range(10):
    url = f'http://quotes.toscrape.com/page/{start_page}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url,headers=headers)
    page = urlopen(req).read()			
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.title
    #print(title.text)
    
    start_page += 1
    #print(url)
    
    quotes = soup.findAll('div',class_='quote')

    for quote in quotes:
        author = quote.findAll('small', class_='author')
        for name in author:
            list_authors.append(name.text)
        all_quotes = quote.find('span',class_='text')
        list_quotes.append(all_quotes.text)
        tags = quote.findAll('div',class_='tags')
        for tag in tags:
            all_tags = tag.findAll('a',class_='tag')
            for i in all_tags:
                list_tags.append(i.text)

#print(list_authors)
#print(list_quotes)
#print(list_tags)

dict_authors = {}

for author in list_authors:
    if author in dict_authors:
        dict_authors[author]+=1
    else:
        dict_authors[author] = 1

for item in dict_authors:
    print(f"Author: {item:25} Count: {dict_authors[item]}")

most_quotes = max(dict_authors, key=dict_authors.get)
least_quotes = min(dict_authors, key=dict_authors.get)
long_quote = max(list_quotes, key=len)
short_quote = min(list_quotes,key=len)

length = []
for quote in list_quotes:
    length.append(len(quote))
#print(length)

avg_length = sum(length)/len(length)

print()
print("Author Stats:")
print(f"Author with Most Quotes: {most_quotes}")
print(f"Author with Least Quotes: {least_quotes}")
print()

print("Quote Stats:")
print(f"Longest Quote: {long_quote}")
print()
print(f"Shortest Quote: {short_quote}")
print()
print(f"Average Length of Quote: {avg_length:.2f}")
print()

print('Tag Stats:')
dict_tags = {}
for tag in list_tags:
    if tag in dict_tags:
        dict_tags[tag] +=1
    else:
        dict_tags[tag] = 1

most_tag = max(dict_tags, key=dict_tags.get)
total_tags = len(dict_tags)
print(f'Most common tag: "{most_tag}"')
print(f"Amount of total tags: {total_tags}")
print()



#copy and paste from API
#for this assignment do authors and quotes for one graph and then tags and times used for the other


#Author and Quotes______________
top_authors = sorted(dict_authors, key=dict_authors.get, reverse=True)[:10]
top_quotes = [dict_authors[key] for key in top_authors]
data = [
    {
        'type': 'bar',
        'x': top_authors,
        'y':top_quotes,
        'marker':{
            'color':'rgb(60,100,150)',
            'line':{"width":1.5,'color':'rgb(25,25,25)'},
        },
        'opacity':0.6,
    }
]

my_layout = {
    'title':'Quotes by Authors',
    'xaxis':{"title":"Authors"},
    'yaxis':{'title':'Number of Quotes'}
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='python_quotes.html')


#Tags______________
top_tags = sorted(dict_tags, key=dict_tags.get, reverse=True)[:10]
top_tag_amounts = [dict_tags[key] for key in top_tags]
data = [
    {
        'type': 'bar',
        'x': top_tags,
        'y':top_tag_amounts,
        'marker':{
            'color':'rgb(60,100,150)',
            'line':{"width":1.5,'color':'rgb(25,25,25)'},
        },
        'opacity':0.6,
    }
]

my_layout = {
    'title':'Most Popular Tags by Author',
    'xaxis':{"title":"Tags"},
    'yaxis':{'title':'Count'}
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='python_tags.html')