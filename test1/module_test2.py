#! /usr/bin/env python3

#一个模块被另一个程序第一次引入时，其主程序将运行。
# 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

print("module_test2 ____1")

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

def moduleFun1():
    print("moduleFun1")