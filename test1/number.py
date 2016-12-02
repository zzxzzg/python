#! /usr/bin/env python3
import math
import random
# pi	数学常量 pi（圆周率，一般以π来表示）
# e	数学常量 e，e即自然常数（自然常数）

a = -10;
#abs 返回绝对值
print(abs(a))

#返回数字的上入整数，如math.ceil(4.1) 返回 5
print(math.ceil(4.1))

#返回e的x次幂(ex),如math.exp(x)
print(math.exp(1))

#返回数字的绝对值，如math.fabs(-10) 返回10.0
print(math.fabs(a))

#返回数字的下舍整数，如math.floor(4.9)返回 4
print(math.floor(4.1))

#log(value,base)
print(math.log(100,10))

#log10(x) 以10为基数的 x的对数
print(math.log10(100))

#max返回给定参数的最大值，参数可以为序列。
print(max(1,2,3,4,5))

#min返回给定参数的最小值，参数可以为序列

#modf 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
t = math.modf(5.6)
print(t[0])
print(t[1])

#pow(x,y) 返回 x**y

#round(x [,n])返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
print(10.345,1)

#sqrt(x) 返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
print(math.sqrt(4))

#choice(seq) 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
l = [3,4,51,6,4,8]
print(random.choice(l))

#randrange ([start,] stop [,step])
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。
# 使用 start 和 stop 还有step生成一个列表，在该列表中获取一个随机数
print(random.randrange(10,1000,2))

#seed([x]) 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

#shuffle(lst) 将序列的所有元素随机排序

#uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。


