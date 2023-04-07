#Importing Python packages
import requests
import bs4 

#Making a request
link = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
req = requests.get(link)
print(req.status_code)

#Creating a BeautifulSoup object
html = bs4.BeautifulSoup(req.text, "lxml")

#Exporting HTML to a file(optional)
with open('html.txt', 'wb') as f:
    f.write(html.prettify('utf-8'))

#Searching HTML tree 
print(html.span)
span_tags = html.find_all('span')
span_tag = html.find('span')
print(span_tag) 

print(html.find('my'))

h2_tags = html.find_all('h2')
for i in h2_tags:
    print(i.text.split('[')[0])

#for i in h2_tags:
    #print(i.text)

print(span_tags[1])
print(html.find_all('span', {'class' : 'mw-headline', 'id' : 'History'}))

#Working with links
print(html.find_all('a')[1].get('href'))

#getting rid of all empty links through a list comprehension
a_tags = html.find_all('a')
href_values = []
for i in a_tags:
    href_values.append(i.get('href'))
ok_href_values = []
for i in href_values:
    if i != None:
        ok_href_values.append(i)



#abs links
from urllib.parse import urljoin
abs_links = []
for i in ok_href_values:
    abs_links.append(urljoin(link,i))

#internal links
texts = []
for i in abs_links[:10]:
    print('Link {}'.format(i))
    req = requests.get(i)
    if req.status_code == 200:
        html = bs4.BeautifulSoup(req.text, "lxml")
        p_tags = html.find_all('p')
        texts_i = []
        for j in p_tags:
            text = j.text
            texts_i.append(text)
    texts.append(' '.join(texts_i))


import pandas
data = pandas.DataFrame(zip(abs_links[:10], texts), columns = ['link', 'text'])
data.to_excel("my_texts.xlsx", index = False)          

print(data)