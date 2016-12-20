#! /usr/bin/env python3
#import 当我们使用import语句的时候，就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。

#Python的from语句让你从模块中导入一个指定的部分到当前命名空间中
# from modname import name1[, name2[, ... nameN]]
import sys
import function_test
from function_test import printinfo

# 包，只有在文件夹下存在__init__.py的文件夹才会被当做是包
import package1.module_test3
from package1 import *

# sys.path 输出是一个列表，其中第一项是空串''，代表当前目录
sys.path

#如果你打算经常使用一个函数，你可以把它赋给一个本地的名称
path = sys.path


function_test.printinfo("gaga",50)
printinfo("hahha",33)

#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
print(dir(function_test))
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
print(dir())





