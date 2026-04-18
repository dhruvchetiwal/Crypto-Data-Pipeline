act_priceRatesINR()
        print(f'Current USD TO INR Price : {price}')
        clean_data = transform(cryptoengine , price)
        load(clean_data ,  cryptoengine)
        print('Data loaded To DataBase Successfully')
        print(f'PipeLine Executed Successfully......\nExecution time : {round(time.time() - current_time  , 2)}sec.')
    except Exception as e :
        print(f'Error Coming From Main Pipeline {e}')
        raise

if __name__ == '__main__' :
    pipeline()