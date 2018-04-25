# -*- coding: UTF-8 -*-
import conf_dev
import conf_test
import platform
import os


# 判断当前的系统是windows系统还是linux系统，以此判断是开发环境还是测试环境
platform_os = platform.system()
config = conf_dev
if (platform_os == 'Linux'):
    config = conf_test
# path
data_root_path = config.data_root_path


# 加载旧数据，比较新数据是否已存在旧数据中，如果不存在则存入数据
def read(resources_file_path, encode='utf-8'):
    file_path = data_root_path + resources_file_path
    if not os.path.exists(file_path):
        return []
    outputs = []
    for line in open(file_path, encoding=encode):
        if not line.startswith("//"):
            outputs.append(line.strip('\n').split(',')[-1])
    return outputs


# 将爬取到的新数据添加到旧文件中
def append(resources_file_path, data, encode='utf-8'):
    file_path = data_root_path + resources_file_path
    #因为open只能新建文件而不能新建目录，所以在追加之前需要做一次判断
    if not os.path.exists(data_root_path):
        os.makedirs(data_root_path)
    with open(file_path, 'a', encoding=encode) as f:
        f.write(data)
    f.close
