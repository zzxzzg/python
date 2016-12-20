#! /usr/bin/env python3
# os 模块 提供了不少与操作系统相关联的函数

import glob
import sys
import re
from timeit import Timer
#glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
glob.glob('*.py')

#通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
# 例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
print(sys.argv)

#re模块为高级字符串处理提供了正则表达式工具。
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')


#math模块为浮点运算提供了对底层C函数库的访问


#以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile

#有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()


# doctest  测试模块