import pandas as pd
import xlrd

workbook = xlrd.open_workbook('fechamento-crediario-fake.xls', ignore_workbook_corruption=True)
excel = pd.read_excel(workbook)
print(excel.head())
