# -*- coding: utf-8 -*-
"""
作者：　terrychan
Blog: https://terrychan.org
# 说明：

"""
import os

import plyvel
import json
from tqdm import tqdm


class lvDb:
    """
    数据库
    plyvel
    https://plyvel.readthedocs.io/
    Plyvel is a fast and feature-rich Python interface to LevelDB.

    """

    def __init__(self, path="lv.db", prefix="default"):
        print(os.path.exists("db"))
        # if not os.path.exists("db"):
        #     os.mkdir(path)
        # self.db_path=os.path.join("db",path)
        self.rootdb = plyvel.DB(path, create_if_missing=True)
        # 默认加载 default
        self.load(prefix)

    def __del__(self):
        self.rootdb.close()
        del self.rootdb

    def load(self, prefix):
        """
        切换表前缀 类似表功能
        """
        prefix = self.tobytes(prefix)
        self.db = self.rootdb.prefixed_db(prefix)
        pass

    def keytobytes(self, data):
        """
        key数据转化为bytes
        """
        tp = type(data)
        # print(tp)
        if tp == str:
            return str.encode(data)
        elif tp == dict:
            return self.dict_bytes(data)
        else:
            return data

    def tobytes(self, data):
        """
        数据转化为bytes
        """
        tp = type(data)
        # print(tp)
        if tp == str:
            data = {"type": "str", "value": data}
        elif tp == dict:
            data = {"type": "dict", "value": data}
            # return self.dict_bytes(data)
        else:
            data = {"type": "None", "value": data}
            # return self.dict_bytes(data)
        print("data", data)
        return self.dict_bytes(data)

    def str_dict(self, data):
        """
        字符串转化为字典
        """
        data = json.loads(data)
        return data

    def dict_bytes(self, odict):
        """
        字典转化为bytes
        """
        # user_dict = {'name': 'dinesh', 'code': 'dr-01'}
        user_encode_data = json.dumps(odict, indent=2).encode('utf-8')
        return user_encode_data

    def put(self, key, value):
        """
        添加数据
        """
        key = self.keytobytes(key)
        # type(value)
        # data={
        #     "type":str(type(value)),
        #     "value":value
        #
        # }
        # print(dir(type(value)))
        # print(type(value).keys())
        # print(data)
        value = self.tobytes(value)
        self.db.put(key, value)

    def put_data(self, data):
        """
        批量保存
        data格式
        data=[('key','dddd')]
        """
        wb = self.db.write_batch()

        for key, value in tqdm(data):
            self.put(key, value)
            pass  #
        wb.write()

    def decode(self, data):
        return bytes.decode(data)

    def get(self, key, ):
        """
        获取数据
        """
        # with db.snapshot() as sn:
        key = self.keytobytes(key)
        # value=self.tobytes(value)
        value = self.db.get(key)
        # print(type(bytes.decode(value)))
        try:
            return self.str_dict(bytes.decode(value))
        except:
            return None

    def get_sn(self, key):
        """
        获取数据
        """
        with db.snapshot() as sn:
            key = self.tobytes(key)
            value = sn.get(key)
            return bytes.decode(value)

    def get_all(self):
        #         遍历键范围
        # 通过提供start和/或stop参数可以限制希望迭代器迭代的值的范围：

        # >>> for key, value in db.iterator(start=b'key-2', stop=b'key-4'):
        # ...     print(key)
        # ...
        # key-2
        # key-3
        # start和stop参数的任何组合都是可能的。例如，要从特定的开始键进行迭代直到数据库结束：

        # >>> for key, value in db.iterator(start=b'key-3'):
        # ...     print(key)
        # ...
        for key, value in self.db.iterator():
            # print(key)
            try:
                yield bytes.decode(key), self.get(key)
            except:
                yield None, None

    def delete(self, key):
        """
        删除数据
        """
        key = self.tobytes(key)
        return self.db.delete(key)


if __name__ == '__main__':

    db = lvDb()
    data = [('key', 'dddd'), ('key1', {"dsd": 3})]
    db.put_data(data)
    for it in db.get_all():
        print(it)

    pass
