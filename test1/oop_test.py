#! /usr/bin/env python3
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

class MyClass:
    """一个简单的类实例"""
    i = 12345
    __a = "私有变量"
    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

#因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
# def __init__(self):
#     self.data = []
#__init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上

#在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数


# class DerivedClassName(BaseClassName1,BaseClassName2):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
#需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，
# python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。



#重写
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')

class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法


# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 slef.__private_methods。


# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __str__ : 打印
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __div__: 除运算
# __mod__: 求余运算
# __pow__: 称方

#运算符重载
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
v1.x=3
print (v1 + v2)
print(v1.x)

