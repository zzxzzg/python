#! /usr/bin/env python3

#字典 即 map

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

#添加修改删除字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典

#键必须不可变，所以可以用数字，字符串或元组充当

# len(dict)
# 计算字典元素个数，即键的总数。

# str(dict)
# 输出字典以可打印的字符串表示。

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
str(dict)
# 输出 "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"

# type(variable)
# 返回输入的变量类型，如果变量是字典就返回字典类型。 <class 'dict'>
type(dict)

# 1	radiansdict.clear()
# 删除字典内所有元素

# 2	radiansdict.copy()
# 返回一个字典的浅复制

# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("新的字典为 : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" % str(dict))

# 4	radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值

# 5	key in dict
# 如果键在字典dict里返回true，否则返回false

# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组
# 一下输出 Value : dict_items([('Age', 7), ('Name', 'Runoob')])
dict = {'Name': 'Runoob', 'Age': 7}

print ("Value : %s" % dict.items())

# 7	radiansdict.keys()
# 以列表返回一个字典所有的键

# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

# 9	radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里

# 10	radiansdict.values()
# 以列表返回字典中的所有值
