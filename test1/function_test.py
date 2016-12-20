#! /usr/bin/env python3

# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
#Python 定义函数使用 def 关键字，一般格式如下
# def 函数名（参数列表）:
#     函数体

#在 Python 中，所有参数（变量）都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

# 调用函数时可使用的正式参数类型：
# 必需参数
# 关键字参数
# 默认参数
# 不定长参数

def printinfo( name, age = 35):
   "打印任何传入的字符串"
   print ("名字: ", name);
   print ("年龄: ", age);
   return;

# 必需参数
printinfo("gaga",50)

# 关键字参数
# 关键字参数允许函数调用时参数的顺序与声明时不一致
printinfo(age=50,name="gaga")

# 默认参数
printinfo(name="gaga")

#不定长参数
# 放在函数最后，使用 *开头，var是一个元组
def printinfo2( name, age = 35,*var):
    print("输出: ")
    print("名字: ", name);
    print("年龄: ", age);
    print(var)
    return;

printinfo2("gaga",50,1,2,3,4,5,6)


#lambda 来创建匿名函
#lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2;
print ("相加后的值为 : ", sum( 10, 20 ))



