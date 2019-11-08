#!Python 3
#GitScrape.py - scraper of git trendings saving 
# results in a .csv and as dataframe for pandas

import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

data = []

# Collect the github page
page = requests.get('https://github.com/trending')

soup = BeautifulSoup(page.text, 'html.parser')

#get repo list
repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_="Box-row")

oggi = date.today()
today = oggi.strftime("%y_%m_%d")
file = "github_trending_"+today+".csv"

# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file, 'w', newline=''))

#new row as header
f.writerow(['Developer', 'Repo Name', 'Num. of Stars', 'Language'])

for repo in repo_list:
    # find the first <a> tag and get the text. Split the text using '/' (%2F) to get an array with developer name and repo name
    dev, repo_name = repo.find('a')['href'][20::].split('%2F')
    stars = repo.find(class_='octicon octicon-star').parent.text.strip()
    language = repo.find('span', {'class': 'd-inline-block ml-0 mr-3'})
    if language is not None:
        language = language.text.strip()
    else:
        language = ('Not Specified')
    print('developer: ', dev)
    print('name: ', repo_name)
    print('stars: ', stars)
    print ('language: ', language)
    print('-----------------------')

    f.writerow([dev, repo_name, stars, language])

    datum = {'dev name': dev,
             'name': repo_name,
             'stars': stars,
             'language': language}
    
    data.append(datum)

#df = pd.DataFrame(data)
#df.head()
print("DONE!!!")    