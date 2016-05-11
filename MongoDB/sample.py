#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Python 2.7.10

'''Basic use for PyMongo Module'''

__author__ = 'AJ Kipper'

import pymongo

#连接数据库，参数分别是HOST和PORT
client = pymongo.MongoClient("localhost", 27017)

#选择数据库名字，如果不存在会新建一个
db = client.MyBlog

#定义一个dict类型数据post
post = {
    'title':'My Blog',
    'content':'This is a test!'
}

#新建一个Collection名字叫posts，并插入post字典
db.posts.insert(post)

#把post数据读取出来
for item in db.posts.find():
	print ('%s , %s' % (item['title'],item['content']))