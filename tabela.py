import pandas as pd
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

tabelas = pd.read_csv("fechamento-crediario-fake.csv")
engine = sqlalchemy.create_engine('mysql://root:15491549@127.0.0.1:3306/seuDin', echo=True)
connection = engine.connect()
base = declarative_base()

class User(base):
    __tablename__ = "nomeComEmail"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    email = Column(String(100))

base.metadata.create_all(engine)
# base.metadata.create_all(engine)

session = sessionmaker(bind=engine)

sessao = session()

x=0
if(sessao.query(User.name).first() == ""):
    while x <  tabelas["Nome do Cliente"].size:
        teste = tabelas.loc[x, ["Nome do Cliente", "E-mail do cliente"]]
        sessao.add(User(name = teste.values.item(0), email= teste.values.item(1)))
        x = x +1
    
sessao.commit()

#isso faz a pesquisa no banco de dados
query = sessao.query(User.name, User.id).all()[:3]
for s in query:
    print(s)
