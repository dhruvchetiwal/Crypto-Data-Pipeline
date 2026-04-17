import requests
import pandas as pd
import os

def extract_priceRatesINR() :
    url = 'https://open.er-api.com/v6/latest/USD'
    data = requests.get(url).json()
    price = round(data["rates"]["INR"] , 2)
    return price
    

def extract() :
    url = ('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    df = df[df['id'] == 'bitcoin']
    df = df[['id', 'symbol' , 'current_price' , 'market_cap' , 'high_24h' , 'low_24h','last_updated']]
    if os.path.exists('Data/Staging_File.csv'):
        if os.path.getsize('Data/Staging_File.csv') == 0:
            df.to_csv('Data/Staging_File.csv' , index=False , mode='a' , header=True)
        else :
            try:
                old_df = pd.read_csv('Data/Staging_File.csv')
                last_timeframe = old_df['last_updated'].max()
                df = df[df['last_updated'] > last_timeframe]
                df.to_csv('Data/Staging_File.csv' , index=False , mode='a' , header=False) 
            except Exception as e:
                raise('Something Wents Wrong In Extract File ' , e)
    else :
         df.to_csv('Data/Staging_File.csv' , index=False , mode='a' , header=True)

    print(f'Extracted {len(df)} row.')