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

    def close(self):
        """
        closs db
        :return:
        """
        self.db.close()


if __name__ == '__main__':
    db=LitDb()
    pass
