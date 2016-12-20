#! /usr/bin/env python3
import sys

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")

# try语句按照如下方式工作；
# 首先，执行try子句（在关键字try和关键字except之间的语句）
# 如果没有异常发生，忽略except子句，try子句执行后结束。
# 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。

#一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
  #except (RuntimeError, TypeError, NameError):

#最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



#try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


#Python 使用 raise 语句抛出一个指定的异常。
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')



#你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

#try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。 finally
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')