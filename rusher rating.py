

def rusher_rating (att,yds,tds,fumb):
    a = (yds/att)*.25
    b = (tds/att)*33.33
    c = 2.375 - (fumb/att*22.95)
    rusher_rating1 = [(a+b+c)/4.5]*100
    print(rusher_rating1)
    
ratinglist = []

import requests
from bs4 import BeautifulSoup
import pprint


search_years = []
for i in range (1970, 2020):
    search_years.append(str(i))
for i in search_years:    
    res1= requests.get(f'https://www.pro-football-reference.com/years/{i}/rushing.htm')
    soup2 = BeautifulSoup(res1.text, 'html.parser')
    table1= soup2.find_all('table')[0]
    
    for i, row in enumerate(table1.find_all('tr')[2:]):
        dat1 = row.find('a')
        if dat1 is None: 
            pass
        else:
            name1 = dat1.getText()
        attempts = row.find('td', attrs = {'data-stat':'rush_att'})
        if attempts is None:
            pass
        else:
            att = attempts.getText()
            if att == '':
                attn = 0
            else:
                attn = float(att)
        yards = row.find('td', attrs = {'data-stat':'rush_yds'})
        if yards is None:
            pass
        else:
            yds = yards.getText()
            if yds == '':
                ydsn = 0
            else:
                ydsn = float(yds)
        touchdowns = row.find('td', attrs = {'data-stat':'rush_td'})
        if touchdowns is None:
            pass
        else:
            tds = touchdowns.getText()
            if tds == '':
                tdsn = 0
            else:
                tdsn = float(tds)
        fumbles = row.find('td', attrs = {'data-stat':'fumbles'})
        if fumbles is None:
            pass
        else:
            fumble = fumbles.getText()
            if fumble == '':
                fumbn = 0
            else:
                fumbn = float(fumble)
        if ydsn > 1999: 
            a = (ydsn/attn)*.25
            b = (tdsn/attn)*33.33
            c = 2.375 - (fumbn/attn*22.95)
            rating = ((a+b+c)/4.5)*100
            capsule = (name1, rating)
            ratinglist.append(capsule)
            
pprint.pprint(ratinglist)