from sqlalchemy import create_engine#Don't mix the "import" below in one line.
from sqlalchemy import Table, MetaData#This import should be one line

# Set up an enigne interface for the database
engine = create_engine(
    "postgresql+psycopg2://YXiong:X4Rw-#0AB1925(8@DOTQASIMSPGSQL1.dot.nycnet:5432/sims")
# engine=create_engine('postgresql+psycopg2://YXiong:X4Rw-#0AB1925(8@127.0.0.1:62798/browser/')


# Set up a metadata object
metadata = MetaData()#Option1; Option2: metadata = MetaData(engine)

stmt = 

connection = engine.connect()
results= connection.execute(stmt).fetchall()

# # Create a table object
# assets = Table('assets', metadata, autoload=True, autoload_with=engine)
# print(repr(assets))