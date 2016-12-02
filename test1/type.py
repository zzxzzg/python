#! /usr/bin/env python3

#数据类型的转换，你只需要将数据类型作为函数名即可。
# int(x [,base])  将x转换为一个整数
# float(x)  将x转换到一个浮点数
# complex(real [,imag])   创建一个复数
# str(x)  将对象 x 转换为字符串
# repr(x) 将对象 x 转换为表达式字符串
# eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)    将序列 s 转换为一个元组
# list(s) 将序列 s 转换为一个列表
# set(s)  转换为可变集合
# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)    转换为不可变集合
# chr(x)  将一个整数转换为一个字符
# unichr(x)   将一个整数转换为Unicode字符
# ord(x)  将一个字符转换为它的整数值
# hex(x)  将一个整数转换为一个十六进制字符串
# oct(x)  将一个整数转换为一个八进制字符串

count = 1000
price = 100.0
name = "rio"
# count,price,name = 1000,100.0,"rio" 效果相同
print(count)
print(price)
print(name)
#删除变量
del count,price,name
#所有的基本数据类型
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
del a,b,c,d
# 相当于 int e = 2\4;
e = 2//4
# 2的5次方
f = 2**5

#字符串的截取的语法格式如下 变量[头下标:尾下标] -1表示最后一个字符的下标 实际上相当于 [ )的左闭合区间
str = 'Runoob'
print (str)           # 输出字符串
print (str[0:-1])     # 输出第一个个到倒数第二个的所有字符
print (str[0])        # 输出字符串第一个字符
print (str[2:5])      # 输出从第三个开始到第五个的字符
print (str[2:])       # 输出从第三个开始的后的所有字符
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 连接字符串

#使用 r 来禁止字符串转义
print('Ru\noob')
print(r'Ru\noob')

#列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
#和 字符串截取和下标方式相同
#与Python字符串不一样的是，列表中的元素是可以改变的
#str[0] = 'a' 错误，无法该表
list[0] = 0

#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开
#其实，可以把字符串看作一种特殊的元组。
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
#构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

#可以使用大括号({})或者 set()函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
if('Rose' in student) :
    print('Rose 在集合中')
else :
	print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素
a.add('k')

# Dictionary (map!!)  字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#构造函数 dict() 可以直接从键值对序列中构建字典如下：
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])


