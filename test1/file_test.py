#! /usr/bin/env python3

import pickle
import pprint

#open() 将会返回一个 file 对象
#open(filename, mode)
#mode决定了打开文件的模式
# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
f = open("/tmp/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

f.flush()

# 关闭打开的文件
f.close()

#  f.read(size)  这将读取一定数目的数据, 然后作为字符串或字节对象返回
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回

# f.flush()  刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。


f = open("/tmp/foo.txt", "r")
#读取10个字符，包括中英文空格，都算一个字符
s = f.read(10)
print(s)

f.close()

f = open("/tmp/foo.txt", "r+")
print ("文件名为: ", f.name)

# 截取10个字节
# 截取文件，截取的字节通过size指定，默认为当前文件位置。
# 会修改文件的
f.truncate(10)

str = f.read()
print ("读取数据: %s" % (str))

# 关闭文件
f.close()

#f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。


#f.readlines() 将返回该文件中包含的所有行。
#如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
#返回的是一个list

#另一种方式是迭代一个文件对象然后读取每行
f = open("/tmp/foo.txt", "r")
for line in f:
    print(line, end='')
f.close()

print ("文件名为: ", f.name)


#f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。



#f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数

#如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数
#from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾


#当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常

#file.fileno()
#返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。


# file.isatty()
# 如果文件连接到一个终端设备返回  True，否则返回False。

# file.next()
# 返回文件下一行。



# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# pickle.dump(obj, file, [,protocol])

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
#ickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()