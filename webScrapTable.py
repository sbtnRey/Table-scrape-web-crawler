from bs4 import BeautifulSoup
import requests
import pandas as pd

# set url to the website that needs to be scraped
url = ""
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# Must find table values to scrap, copy and paste Xpath from the website using web developer tools
table = soup.find_all('table')[1]
rows = table.find_all('tr')[2:]

data = {
    'items' : []
}

for row in rows:
    cols = row.find_all('td')
    data['items'].append( cols[0].get_text() )

itemData = pd.DataFrame( data )
items.to_csv("items.txt")
