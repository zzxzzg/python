#! /usr/bin/env python3
import math

s = "hello world\n"
#函数返回一个用户易读的表达形式。
print(str(s))
#产生一个解释器易读的表达形式     repr() 函数可以转义字符串中的特殊字符
print(repr(s))

#rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
# 类似的方法, 如 ljust() 和 center()
# 另一个方法zfill(), 它会在数字的左边填充 0
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))


#str.format() 的基本使用如下
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
#括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
#在括号中的数字用于指向传入对象在 format() 中的位置，如下所示
print('{1} 和 {0}'.format('Google', 'Runoob'))

#如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print("{!a}".format('c'))

#可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

#传入一个字典, 然后使用方括号 '[]' 来访问键值
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
#也可以通过在 table 变量前使用 '**' 来实现相同的功能
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

#% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串
print('常量 PI 的值近似为：%5.3f。' % math.pi)




