#! /usr/bin/env python3

import sys

#迭代器，和java c++ 原理基本差不多
list = ["1","2","3","4"]
it = iter(list)
print(next(it))

#yield 的函数被称为生成器
#在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a    #返回a的值，并且暂停运行，保存当前信息
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")   #调用了next， f 继续从yield之后开始运行
    except StopIteration:
        sys.exit()