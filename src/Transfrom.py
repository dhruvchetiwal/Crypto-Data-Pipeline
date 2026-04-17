import pandas as pd
from sqlalchemy import text
def get_latest_timestamp(engine) :
        with engine.connect() as connection :
                result = connection.execute(text('SELECT MAX(last_updated) FROM CRYPTO_DATA'))
                last_time = result.scalar()
        return last_time

    

def transform(engine , price) : 
    df = pd.read_csv('Data/Staging_File.csv')
    df['last_updated'] = pd.to_datetime(df['last_updated']).dt.tz_localize(None)
    df['default_currency'] = "$"
    df['current_price'] = pd.to_numeric(df['current_price'])
    df['market_cap'] = pd.to_numeric(df['market_cap'])
    df['high_24h'] = pd.to_numeric(df['high_24h'])
    df['low_24h'] = pd.to_numeric(df['low_24h'])
    df['price_INR'] = df['current_price'] * price
    df = df.sort_values('last_updated' , ascending=False)
    df['id'] = df['id'].str.upper()
    df['price_change'] = df['high_24h'] - df['low_24h']
    df['price_changeINR']  = df['price_change'] * price 
    last_time = get_latest_timestamp(engine)
    last_time = pd.to_datetime(last_time)
    if last_time is not None:
        df = df[df['last_updated'] > last_time]
    df = df[['id', 'symbol', 'default_currency', 'current_price', 'market_cap' , 'high_24h' , 'low_24h' , 'price_change' , 'price_INR' , 'price_changeINR' , 'last_updated']]
    df = df.drop_duplicates(subset=['id' , 'last_updated'])
    return df