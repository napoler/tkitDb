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


if __name__ == '__main__':
    db = LitDb()
    db.conn()
    db.create_table()
    db.add()
    db.save()
    db.close()
    pass
