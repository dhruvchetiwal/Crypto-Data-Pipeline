import dotenv
import os
import sqlalchemy as sq

dotenv.load_dotenv()

SERVER  = os.getenv('SERVER')
DATABASE= os.getenv('DATABASE')
DATABASE2 = os.getenv('DATABASE2')
DRIVER= os.getenv('DRIVER')

masterengine = sq.create_engine(f"mssql+pyodbc://{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes")
cryptoengine = sq.create_engine(f"mssql+pyodbc://{SERVER}/{DATABASE2}?driver={DRIVER}&trusted_connection=yes")
