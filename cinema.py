
"""
The page shown at the link below contains movies with some metadata of interest to our friend Quentin, a budding movie director.

https://www.listchallenges.com/100-must-see-movies-for-more-advanced-cinephiles

title
year
ranking
no_of_votes


Task
Using your preferred language and/or tools - write a program that parses this page and extracts the following data into two possible file formats

1 - A CSV file
2 - A HTML file with some style formatting applied - You can use a CSS framework like https://tailwindcss.com/docs to complete this task.


Include instructions on how to run your program including installing any dependencies.

Usage:

python cinema.py --format [ CSV | HTML ]

"""

import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd


def transform():
    
    titles=[]
    years = []
    rankings   = [] 
    nb_votes = []

    "il faut looper sur les 3 onglets du site, pas eu le temps"

    url = "https://www.listchallenges.com/100-must-see-movies-for-more-advanced-cinephiles"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    elements = soup.find_all('div', {"class" : "list-item view-small-image"})

    for element in elements:
        title = element.find_all('div', {'class' : 'item-name'})[0].text
        title = title.replace("\t","")
        title = title.replace("\r","")
        title = title.replace("\n","")
        date = title[-5:-1]
    
    
        titles.append(title[:len(title)-7])
        years.append(date)
    

    df = pd.DataFrame.from_dict({ 'Title' : titles,
                            'Year'  : years,
                            })

    df.to_csv('films.csv',index=False)


    
     pass
