#! /usr/bin/env python3

# 使用 elif替代 else if  ，去掉大括号，使用缩进来分割代码块

# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3


#注意冒号！！！
# while 判断条件：
#     语句

#另外，在Python中没有do..while循环。

# while还提供了else的语句配对，当不满足条件的时候运行else(只运行一次)
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")



# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for循环的一般格式如下：
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>



#如果你需要遍历数字序列，可以使用内置range()函数  for i in range(5)  for i in range(5,9)


# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例

while True:
    pass

