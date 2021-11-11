import sqlite3
import os

dbname ='Vending.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

#cur.execute('create table Edit (drinks string price integer amount integer)')

#Drinks
cur.execute('INSERT INTO Edit values("水",110,50)')
cur.execute('INSERT INTO Edit values("緑茶",140,50)')
cur.execute('INSERT INTO Edit values("炭酸水",150,50)')
cur.execute('INSERT INTO Edit values("レッドブル",210,50)')
cur.execute('INSERT INTO Edit values("コーラ",160,50)')

conn.commit()

cur.close()
conn.close()







