#!/usr/bin/env python
#-*- coding : utf-8-*-
#python 3.5

'''读取json文件数据到数据库,再从数据库读取数据存储到json文件代码示例'''

__author__ = 'AJ Kipper'

import json
import pymongo

class JsonDataHandle(object):
    '''Json格式数据的读取和存储'''
    def __init__(self):
        #连接数据库初始化
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client.test

    #读取json文件数据存储进Mongo数据库
    def json_to_db(self):
        with open('data_a.json','r') as file_obj:
            #json.load( )方法为读取json数据
            json_data = json.load(file_obj)
            #由于json数据格式跟mongodb是一致的,所以可以直接插入
            self.db.myjson.insert(json_data)
            
    #读取Mongo数据库数据,存储到json文件
    def db_to_json(self):
        db_data = self.db.myjson.find()
        for item in db_data:
            #这段代码,可以查看mongodb数据的key,和去掉自带的_id值
            json_key = {i for i in item if i != '_id'}
            for key in json_key:
                print (key)
            #构建json格式数据
            json_data = {
                'programmers' : item['programmers'],
                'authors' : item['authors'],
                'musicians' : item['musicians']
            }
            with open('data_b.json','w') as file_obj:
                file_obj.write(json.dumps(json_data))
            #测试输出
            #print (json_data)

if __name__ == '__main__':
    test = JsonDataHandle()
    #调用相应的方法
    #test.json_to_db()
    #test.db_to_json()
