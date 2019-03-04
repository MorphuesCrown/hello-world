current_dic = {"username":None,"login":False}
#
#
#
#
# def auth_func(func):
#     username = input("用户名>>")
#     passwd = input("密码>>")
#     def wrapper(*args,**kwargs):
#         if username == "morphues" and passwd =="123":
#             res = func(*args,**kwargs)
#             return res
#         else:
#             print("用户名或密码错误")
#     return wrapper
#
# @auth_func
# def shopping_car(name):
#     print("%s的购物车有%s,%s,%s" %(name,"wacom pyh-660","dth-1320","ako-f"))
# @auth_func
# def home(name,age):
#     print("欢迎来到%s的京东主页，已使用%s年" %(name,age))
#
#
# shopping_car("morphues")
# home("morphues",1)


user_list = [{"username": "morphues1", "passwd": "123"},
             {"username": "morphues2", "passwd": "456"},
             {"username": "morphues3", "passwd": "789"},
             ]


# 给装饰器添加参数

def auth_func(func):

        def wrapper(*args, **kwargs):
            if current_dic["username"] != None:
                res = func(*args, **kwargs)
                return res
            else:
                username = input("用户名>>")
                passwd = input("密码>>")
                for i in user_list:
                    if username == i["username"] and passwd == i["passwd"]:
                        res = func(*args, **kwargs)
                        return res
                    else:
                        pass

        return wrapper

@auth_func
def shopping_car(name):
    print("%s的购物车有%s,%s,%s" %(name,"wacom pyh-660","dth-1320","ako-f"))
@auth_func
def home(name,age):
    print("欢迎来到%s的京东主页，已使用%s年" %(name,age))


shopping_car("morphues")
home("morphues",1)
