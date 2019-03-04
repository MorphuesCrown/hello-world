# print(abs(-1))#绝对值

# print(all([1,2,"1"]))  #True
# all(序列)
# 0,none,空的bool值为False

# name = "你好"
# print(bytes(name,encoding="utf-8"))
# print(bytes(name,encoding="utf-8").decode("utf-8"))
# print(bytes(name,encoding="gbk"))
# print(bytes(name,encoding="gbk").decode("gbk"))#decode默认"utf-8"
# print(bytes(name,encoding="ascii"))#ascii码不能编码中文


# print(divmod(10,3))#输出(3, 1)商与余数   #应用：百度搜索结果分页

# dic_str = "{ 'name':'alex' }"  #这是个字符串
# print(eval(dic_str))  #eval：将字符串中的数据类型提出
# print(eval("3+4-1*1000"))#eval:还可将""内的式子计算出来


# print(bin(10))#十进制转二进制
# print(hex(12))#十进制转16进制
# print(oct(12))#十进制转8进制

# print(isinstance(1,int))#判断数据的类型

# print(globals())#打印全局变量
# print(locals())#打印局部变量


# sorted()

# dic = {"name":"alex","age":"18","gender":"none"}
# li = zip(dic.keys(),dic.values())   #zip的对象要求可迭代
# print(list(li))     #zip一一对应打包成元组

####？？？？？？？zip出来的数据类型是什么

# li = ["alex","more","less"]       #例如比较"alex"与"more"时先比较"a"与"m"（根据ascii码先后顺序）如果比较出大小则后面就不会进行比较
# print(max(li))        #max,min比较本质是for循环


###文件操作
# f = open("morphues",encoding="utf-8")   #encoding别忘了
# data = f.read()
# #data = f.readlines()#读出，存为列表
# print(data)
# f.close()           #文件操作  关闭文件

# f = open("morphuesC","w",encoding="utf-8")  #此过程相当于创建一个新文档，如有与其重名的文档，则覆盖之
# f.write("123456\n")
# f.write("234567\n")
# f.close()

# f = open("morphuesC","a",encoding="utf-8")  #追加的形式写，写到文件最后


# with open("morphuesC","r") as f1,\
#     open("morphuesC","r") as f2:


# f = open("morphuesC","wb")  #b的方式不能指定编码
# f.write(bytes("111\n",encoding="utf-8"))
# #处理光标
# f.tell()        #获得光标位置
# f.seek(0)       #移动光标到指定位置