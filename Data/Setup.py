import sqlalchemy as sq 

def createdb(engine) :
    with engine.connect().execution_options(isolation_level='AUTOCOMMIT') as connection :
        connection.execute(sq.text("""
        IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'crypto')
        BEGIN
            CREATE DATABASE crypto
        END
        """))
    print('DataBase WorkDone Successfully.....')