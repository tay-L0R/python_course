import requests
import bs4
import numpy as np

link =  "http://books.toscrape.com/"
req = requests.get(link)
print(req.status_code)

html = bs4.BeautifulSoup(req.text, "lxml" )


names = []
h3_tags = html.find_all('h3')
print(len(h3_tags))
for i in h3_tags:
    names.append(i.find('a').get('title'))
    
for i in names:
    print(i)


prices = []   
div_tags = html.find_all('div', {"class" : "product_price"})
for i in div_tags:
    prices.append(float(i.find('p').text[2:]))
    
for i in prices:
    print(i)
 
 
ratings = []
li_tags = html.find_all('li', {'class' : "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
print(len(li_tags))
p_tags = []
for i in li_tags:
    p_tags.append(i.find('p').get('class'))
for i in p_tags:
    ratings.append(i[-1])
   
for i in ratings:
    print(i)
    


names = []
ratings = []
prices = []

for i in range(1, 51):
    req = requests.get("http://books.toscrape.com/catalogue/page-{}.html".format(i))
    html = bs4.BeautifulSoup(req.text, "lxml" )
    
    h3_tags = html.find_all('h3')
    for i in h3_tags:
        names.append(i.find('a').get('title'))
    
    div_tags = html.find_all('div', {"class" : "product_price"})
    for i in div_tags:
        prices.append(float(i.find('p').text[2:]))
    
    li_tags = html.find_all('li', {'class' : "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    p_tags = []
    for i in li_tags:
        p_tags.append(i.find('p').get('class'))
    for i in p_tags:
        ratings.append(i[-1])
    
import pandas as pd
books = pd.DataFrame(zip(names, ratings, prices), columns = ["Titles", "Ratings", "Prices"])
books.to_excel("Books.xlsx", index = False)
    