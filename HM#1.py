import requests
import bs4

link = "https://www.billboard.com/charts/hot-100/"
req = requests.get(link)
print(req.status_code)

html = bs4.BeautifulSoup(req.text, "lxml")

titles = []
ul_tags = html.find_all("ul", {"class" : "lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"})
h3_tags = []
for i in ul_tags:
    h3_tags.append(i.find('h3'))
print(len(h3_tags))
for i in h3_tags:
    titles.append(i.text.strip())

for i in titles:
    print(i)
    

artists = []
span_tags = []
for i in ul_tags:
    span_tags.append(i.find('span'))
print(len(span_tags))
for i in span_tags:
    artists.append(i.text.strip())

for i in artists:
    print(i)


wks_on_charts = []
span_tags = []
for i in ul_tags:
    span_tags.append(i.find_all('span')[3])
print(len(span_tags))
for i in span_tags:
    wks_on_charts.append(int(i.text))
    
for i in wks_on_charts:
    print(i)
    
import pandas as pd
billboard = pd.DataFrame(zip(titles, artists, wks_on_charts), columns = ["Titles", "Artists", "Weeks on Charts"])
billboard.to_excel("Billboard.xlsx", index = False)

print(billboard)

    
    

