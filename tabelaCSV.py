import pandas as pd

tabelas = pd.read_csv("fechamento-crediario-fake.csv")

# print(tabelas[["Nome do Cliente", "E-mail do cliente"]].head())

print(tabelas.head)

# print(tabelas.loc[0])

# print(tabelas.loc[0:3])

# print(tabelas.loc[[0,1,2]])

# print(tabelas.loc[0:3, ["Nome do Cliente"]])