# -*- coding: utf-8 -*-
"""
作者：　terrychan
Blog: https://terrychan.org
# 说明：
https://docs.python.org/3/library/sqlite3.html
"""
import os
import sqlite3
import pandas


class LitDb:
    def __init__(self):
        self.db = None
        self.cursor = None
        self.db_path = os.path.join(os.path.dirname(__file__), 'lit.db')

    def conn(self):
        """
        conn db


        :return:
        """
        self.db = sqlite3.connect(self.db_path)
        self.cursor = self.db.cursor()

    def save(self):
        self.db.commit()

    def close(self):
        """
        closs db
        :return:
        """
        self.db.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

    def add(self):
        self.cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    def get_item(self):
        for row in self.cursor.execute('SELECT * FROM stocks ORDER BY price'):
            yield row
    def csv_to_sql(self,csv_file,db_name="csv_import"):
        df = pandas.read_csv(csv_file)
        df.to_sql(db_name, self.db, if_exists='replace', index=False)


if __name__ == '__main__':
    db = LitDb()
    db.conn()
    # db.create_table()
    db.add()
    db.save()
    for it in db.get_item():
        print(it)

    db.close()
    pass
