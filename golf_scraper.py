import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'https://wghof.devgado.com/category/memberpages/?sf_paged='



all_players = []

def grab_pages(page_number):
    r = requests.get(url+str(page_number))
    soup = BeautifulSoup(r.text, features="lxml")

    golfers = soup.find_all("div", {"data-widget_type": "ae-custom-field.default"})

    for golfer in golfers:
        
        try:
            newdict = {
                "name": golfer.find('a')['title'],
                "link": golfer.find('a')['href']
            }
            
            all_players.append(newdict)
        except:
            pass


all_hometowns = []
def grab_hometowns():
    df = pd.read_csv('all_golf_players3.csv')
    links = df['link']
    
    for link in links[:10]:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, features="lxml")
        
        divs = soup.select('h6:-soup-contains("Hometown")')
        parent_div = divs[0].parent.parent.parent
        hometown_divs = parent_div.find_all('div', {
            "data-widget_type": "text-editor.default"
        })
        #print(hometown_divs)
        

    for div in hometown_divs:
                    print(div.find_all('div', {
                    "class":"elementor-text-editor"
                    })[0].string)
                    

                    
                    #towndict = {"town" : hometown_divs}
                    #all_hometowns.append(towndict)
                    #print(towndict)
                    #dfd = pd.DataFrame(all_hometowns)
                    #dfd.to_csv('hometowns.csv', index=False)                    
        
def grab_all_golfers():
    for page in range(1,15):
        grab_pages(page)
        df = pd.DataFrame(all_players)
        
        print(df)
        df.to_csv('all_golf_players3.csv', index=False)


def grab_all_hometowns():
    for div in range(1,15):
        grab_pages(page)
        df = pd.DataFrame(all_players)
        
        print(df)
        df.to_csv('all_golf_players3.csv', index=False)



#grab_all_golfers()
grab_hometowns()
#grab_all_hometowns()



#dfh = pd.DataFrame(hometown_divs)
#dfh.to_csv('all_golf_players3.csv', index=False)
