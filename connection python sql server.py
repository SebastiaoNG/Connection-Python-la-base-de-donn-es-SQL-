# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:16:41 2020

@author: sebastien ng
"""
import pandas as pd
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NANKUTA;'
                      'Database=WideWorldImporters;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#cursor.execute('SELECT * FROM WideWorldImporters.Sales.Customers')


requette = pd.read_sql_query('SELECT * FROM WideWorldImporters.Sales.Invoices',conn)
print(requette)
print(type(requette))

#
#for row in cursor:
#    print(row)
