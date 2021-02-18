import requests
from bs4 import BeautifulSoup
import pprint

def find_forty_times_based_on_position_and_yards(plyposition, rushyards):
    runners1 =[]
    runners=[]
    times =[]
    search_years = ['00','01','02','03','04','05', '06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']
    for i in search_years:
        res = requests.get(f'https://www.pro-football-reference.com/years/20{i}/rushing.htm')
        soup1 = BeautifulSoup(res.text, 'html.parser')
        table = soup1.find_all('table')[0]
    
        for i,row in enumerate(table.find_all('tr')[2:]):
            position = row.find('td', attrs = {'data-stat':'pos'})
            if position is None:
                pass
            else:
                POS = position.getText()
                statsrow = row.find('td', attrs = {'data-stat' : 'rush_yds'})
                stats = statsrow.getText()
                if POS == str(plyposition) and int(stats) > int(rushyards):
                    dat = row.find('td', attrs = {'data-stat':'player'})
                    name = dat.a.getText()
                    runners1.append(name)
    runners2 = list(set(runners1))
    for player in runners2: 
        player1 = player.strip()
        runners.append(player1)
    
               
    
    for ath in runners:
        for i in search_years:
            res1= requests.get(f'https://www.pro-football-reference.com/draft/20{i}-combine.htm')
            soup2 = BeautifulSoup(res1.text, 'html.parser')
            table1= soup2.find_all('table')[0]
                
            for i, row in enumerate(table1.find_all('tr')[2:]):
                dat1 = row.find('a')
                if dat1 is None:
                    pass
                else:
                    name1 = dat1.getText()
                if ath == name1:
                    fortyrow = row.find('td', attrs = {'data-stat':'forty_yd'})
                    if fortyrow is None:
                        forty = 'No record'
                    else:
                        forty = fortyrow.getText()
                        capsule = (name1, forty)
                        times.append(capsule)              
    print(times)

find_forty_times_based_on_position_and_yards(plyposition= 'RB', rushyards=1000)