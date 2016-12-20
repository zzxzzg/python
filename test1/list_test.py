#! /usr/bin/env python3

#可以使用 del 语句来删除列表的的元素，如下实例：
list = ['Google', 'Runoob', 1997, 2000]
print (list)
del list[2]
print ("删除第三个元素 : ", list)

#* 号用于重复列表
print(['HI']*4)

# 1	len(list)
# 列表元素个数

# 2	max(list)
# 返回列表元素最大值

# 3	min(list)
# 返回列表元素最小值

# 4	list(seq)
# 将元组转换为列表

# 1	list.append(obj)
# 在列表末尾添加新的对象

# 2	list.count(obj)
# 统计某个元素在列表中出现的次数

# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置

# 5	list.insert(index, obj)
# 将对象插入列表

# 6	list.pop(obj=list[-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项

# 8	list.reverse()
# 反向列表中元素
list1 = ['123','456','asd']
list1.reverse()
print(list1)

# 9	list.sort([func])
# 对原列表进行排序

# 10	list.clear()
# 清空列表

# 11	list.copy()
#复制列表



#列表推导式
#通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
vec = [2, 4, 6]
vec2 = [3*x for x in vec]
print(vec2)

vec3 = [[x, x**2] for x in vec]
print(vec3)

#我们可以用 if 子句作为过滤器
vec4 = [3*x for x in vec if x > 3]

