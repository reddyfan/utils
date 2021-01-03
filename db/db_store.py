"""
@Time ： 2021/1/3 16:53
@Auth ： Reddy
@File ：db_store.py
@Description : 数据库存储
"""
import pymongo

# 配置文件
# cfg =

class Mongo():
    def __init__(self):
        global cfg

        if cfg:
            print(cfg)
            self.conn = pymongo.MongoClient(host=cfg['ip'], port=cfg['mongo']['port'])
            print(type(self.conn))
            self.db = self.conn[cfg['mongo']['db']]
            self.db = self.db.authenticate(cfg['mongo']['auth']['name'], cfg['mongo']['auth']['passwd'])

    def use_db(self, db):
        self.db = self.conn[db]
        return self.db

    def insert(self, table, data):
        if type(data) == list:
            self.db[table].insert_many(data)
        elif type(data) == dict:
            self.db[table].insert_one(data)
        data.clear()
        print("插入完成")