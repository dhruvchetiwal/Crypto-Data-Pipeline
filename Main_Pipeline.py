from src.Extract import extract
from src.Extract import extract_priceRatesINR
from src.load import load
from src.Transfrom import get_latest_timestamp
from src.Transfrom import transform
from config import cryptoengine
from config import masterengine
from Data.Setup import createdb
import time

def pipeline() :
    try: 
        current_time  = time.time()
        print('Pipeline Started .... ')
        createdb(masterengine)
        print('Connecting To Api For Data And Transfering it to Staging Area')
        extract()
        print('Transforming the Data and loading to DataBase.....')
        get_latest_timestamp(cryptoengine)
        price = extract_priceRatesINR()
        clean_data = transform(cryptoengine , price)
        load(clean_data ,  cryptoengine)
        print('Data loaded To DataBase Successfully')
        print(f'PipeLine Executed Successfully......\nExecution time : {round(time.time() - current_time  , 2)}sec.')
    except Exception as e :
        print(f'Error Coming From Main Pipeline {e}')
        raise

if __name__ == '__main__' :
    pipeline()
