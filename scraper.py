import pandas as pd
import json

def get_prices():

    url = "https://oilprice.com/oil-price-charts/"

    scraper = pd.read_html(url)
    futures_and_index = scraper[0]
    
    li = []
    for index, row in futures_and_index.iterrows():
        li.append({row[1]: row[2]})
        
    return li


# get_prices()