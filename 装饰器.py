#装饰器的要求
#不改变函数源代码
#不改变函数调用方式



# import time
# def foo():
#     time.sleep(3)
#     print("来自foo")


# 仅使用高阶函数。   运行了两次，不合格
# def test(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print("foo运行时间是%s" %(stop_time-start_time))
#     return func
# foo = test(foo)
# foo()


#已实现但仍需要针对不同函数进行赋值，可优化
# def timmer(func):
#     def zs():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("foo运行时间是%s" %(stop_time-start_time))
#     return zs
# foo = timmer(foo)       #赋值操作
# foo()

# @timmer相当于
# foo = timmer(foo)
# foo()


# 考虑被修饰函数返回值
# def timmer(func):
#     def zs():
#         start_time = time.time()
#         res = func()
#         stop_time = time.time()
#         print("foo运行时间是%s" %(stop_time-start_time))
#         return res
#     return zs
#
# @timmer
# def foo():
#     time.sleep(3)
#     print("来自foo")
#     return 123
# rr = foo()
# print(rr)

# 考虑被修饰函数的参数
# def timmer(func):
#     def zs(*args,**kwargs): #
#         start_time = time.time()
#         res = func(*args,**kwargs) #
#         stop_time = time.time()
#         print("foo运行时间是%s" %(stop_time-start_time))
#         return res
#     return zs
#
# @timmer
# def foo():
#     time.sleep(3)
#     print("来自foo")
#     return 123
# rr = foo()
# print(rr)