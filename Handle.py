# -*- coding: UTF-8 -*-

import sys
from datetime import datetime
import MongoUtil
import FileUtil

# 这个方法主要是将爬取到的数据追加到文件中，并把它添加到mongodb数据库中
def handle(resources_file_path, base_url, scratch_func):
    old_data = FileUtil.read(resources_file_path)
    new_data = scratch_func(base_url, old_data)
    #当爬取到新数据才会追加文件和添加数据库中
    if new_data:
        #在数据前添加日期，方便查看和其他查询操作
        date_new_data = "//" + datetime.now().strftime('%Y-%m-%d') + "\n" + "\n".join(new_data) + "\n"
        #将新数据追加至文件中
        FileUtil.append(resources_file_path, date_new_data)
        #将新数据添加至数据库中，默认关闭，放开则可以使用mongodb
        #MongoUtil.insert(resources_file_path, date_new_data)
    else:
        #如果没有新数据则打印日志
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '----', getattr(scratch_func, '__name__'), ": nothing to update ")
