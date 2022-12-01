import pandas as pd
import sqlalchemy
import re
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

tabelas = pd.read_csv("fechamento-crediario-fake.csv")
engine = sqlalchemy.create_engine('mysql://root:123456789@127.0.0.1:3306/seuDin', echo=True)
connection = engine.connect()
base = declarative_base()

class User(base):
    __tablename__ = "tst5"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    email = Column(String(100))

base.metadata.create_all(engine)

session = sessionmaker(bind=engine)

sessao = session()

x=0
if(sessao.query(User.name).first() == None):
    while x <  tabelas["Nome do Cliente"].size:
        a = tabelas["Nome do Cliente"][x]
        teste = tabelas.loc[x, ["Nome do Cliente", "E-mail do cliente"]]
        if(re.search('Ana', teste.values.item(0))):
            teste = teste.replace(a, 'p')
            sessao.add(User(name = teste.values.item(0), email= teste.values.item(1)))
        else:
            sessao.add(User(name = teste.values.item(0), email= teste.values.item(1)))
        x = x +1
    
sessao.commit()

#isso faz a pesquisa no banco de dados
# query = sessao.query(User.name, User.id).all()[:3]
# for s in query:
#     print(s)
