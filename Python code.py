import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:mehnazria321@localhost/Project_1'
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size','image_link', 'museum_hours','museum','product_size', 'subject', 'work']

for file in files:

    df = pd.read_csv(f'C:/Users/AASHIK/OneDrive/Documents/SQL projects/Project_1/CSV Files/{file}.csv')
    df.to_sql(file, con=conn, if_exists = 'replace', index=False)