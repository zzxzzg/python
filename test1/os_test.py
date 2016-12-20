#! /usr/bin/env python3

import os
import sys, stat
#os 模块提供了非常丰富的方法用来处理文件和目录

#检验权限模式
#os.access(path, mode);
# path -- 要用来检测是否有访问权限的路径。
# mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
# os.F_OK: 作为access()的mode参数，测试path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
#如果允许访问返回 True , 否则返回False。

ret = os.access("/tmp/foo.txt", os.F_OK)

#os.chdir(path)
#改变当前工作目录


#设置路径的标记为数字标记。多个标记可以使用 OR 来组合起来。只支持在 Unix 下使用。
# flags -- 可以是以下值：
# stat.UF_NODUMP: 非转储文件
# stat.UF_IMMUTABLE: 文件是只读的
# stat.UF_APPEND: 文件只能追加内容
# stat.UF_NOUNLINK: 文件不可删除
# stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
# stat.SF_ARCHIVED: 可存档文件(超级用户可设)
# stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
# stat.SF_APPEND: 文件只能追加内容(超级用户可设)
# stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
# stat.SF_SNAPSHOT: 快照文件(超级用户可设)
#os.chflags(path, flags)


#os.chmod() 方法用于更改文件或目录的权限
# flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
# stat.S_IXOTH: 其他用户有执行权0o001
# stat.S_IWOTH: 其他用户有写权限0o002
# stat.S_IROTH: 其他用户有读权限0o004
# stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
# stat.S_IXGRP: 组用户有执行权限0o010
# stat.S_IWGRP: 组用户有写权限0o020
# stat.S_IRGRP: 组用户有读权限0o040
# stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
# stat.S_IXUSR: 拥有者具有执行权限0o100
# stat.S_IWUSR: 拥有者具有写权限0o200
# stat.S_IRUSR: 拥有者具有读权限0o400
# stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
# stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
# stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
# stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读
os.chmod("/tmp/foo.txt", stat.S_IXGRP)

#os.chroot(path) 改变当前进程的根目录，使用该函数需要管理员权限

# os.close(fd)
# 关闭文件描述符 fd

# os.closerange(fd_low, fd_high)
# 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略

# os.dup(fd)
# 复制文件描述符

# os.dup2(fd, fd2)
# 将一个文件描述符 fd 复制到另一个 fd2

# os.fchdir(fd)
# 通过文件描述符改变当前工作目录


# os.fchmod(fd, mode)
# 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限(参见 os.chmod)。

# os.fchown(fd, uid, gid)
# 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。

# os.fdopen(fd[, mode[, bufsize]])
# 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象  mode参数可以指定『r,w,a,r+,w+,a+,b』等
# bufsize -- 可选，指定返回的文件对象是否带缓冲：buffersize=0，表示没有带缓冲；bufsize=1
# bufsize=正数，表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。

#os.fpathconf(fd, name)
#返回一个打开的文件的系统配置信息。
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )
print ("%s" % os.pathconf_names)
# 获取最大文件连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print ("文件最大连接数为 :%d" % no)
# 获取文件名最大长度
no = os.fpathconf(fd, 'PC_NAME_MAX')
print ("文件名最大长度为 :%d" % no)
# 关闭文件
os.close(fd)

#os.fstat(fd) os.fstatvfs() 方法用于返回文件描述符fd的状态
#具体返回内容有区别，用到时查吧

#os.fsync() 方法强制将文件描述符为fd的文件写入硬盘。
#如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()), 确保与f相关的所有内存都写入了硬盘.



