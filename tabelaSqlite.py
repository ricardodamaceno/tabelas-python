import pandas as pd
import sqlite3
import sqlalchemy


tabelas = pd.read_csv("fechamento-crediario-fake.csv", index_col=0, encoding="UTF-8")
 
 #nome do banco
conn =  sqlite3.connect("bancosqlite.db")

# tabelas.to_sql(name='tabelas', con= conn)

# cursor = conn.cursor()
