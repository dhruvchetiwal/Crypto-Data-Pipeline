import pandas as pd
from sqlalchemy  import types
def load(df , engine) : 
    try:
        df.to_sql('crypto_data' 
              , con=engine
              ,index=False
              ,if_exists='append', 
              method='multi',
              dtype={
               'last_updated': types.DateTime()
              })
    except Exception as e :
        print('Error Coming From Load' , e)
        raise
    
    
