# li = ["alex","eric","rain"]
# print("_".join(li))


# li =["alec","aric","Alex","Tony","rain"]
# tu =("alec","aric","Alex","Tony","rain")
# dic ={"k1":"alex","k2":"aric","k3":"Alex","k4":"Tony"}
# for item in li:
#     if item.startswith("a" or "A") and item.endswith("c"):
#         print(item)
# for item in tu:
#     if item.startswith("a" or "A") and item.endswith("c"):
#         print(item)
# for item in dic.values():
#     if item.startswith("a" or "A") and item.endswith("c"):
#         print(item)


# li = ["alex","eric","rain"]
# print(len(li))
# li.append("seven")
# print(li)


# li = ["hello", "seven", ["mon", ["h", "kelly"], "all"], 123, 446]
# print(li[2][1][1])
# li[2][2] = "ALL"
# print(li)


# tu = ("alex","eric","rain")
# num = len(tu)
# print(num)
# print(tu[1])
# print(tu[0:2])        # print(tu[0],tu[1])
# for elem in tu:
#     print(elem)
# for elem in tu:
#     print(tu.index(elem))
# for i,j in enumerate(tu,10):
#     print("%s,%s" %(i,j))


# tu = ("alex",[11,22,{"k1":"v1","k2":["age","name"],"k3":(11,22,33)},44])
# tu[1][2]["k2"].append("Seven")
# print(tu)


# dic ={"k1":"v1","k2":"v2","k3":[11,22,33]}
# for k in dic :
#     print(k)
# for v in dic.values():
#     print(v)
# for k,v in dic.items():
#     print(k,v)
# dic.update({"k4":"v4"})
# print(dic)
# dic["k1"] = "alex"
# print(dic)
# dic["k3"].append(44)
# print(dic)
# dic["k3"].insert(0,18)
# print(dic)


# s = "alex"
# s = list(s)
# print(s)
# s = tuple(s)
# print(s)
# li = ["alex","seven"]
# li = tuple(li)
# print(li)
# tu = ["alex","seven"]
# tu = list(tu)
# print(tu)
# dic = {}
# k = 10
# for v in li:
#     dic.update({k:v})
#     k += 1
# print(dic)


# dic = {"k1":[],"k2":[]}
# s = [11,22,33,44,55,66,77,88,99,90]
# for num in s :
#     if num > 66:
#         dic["k1"].append(num)
#     else :
#         dic["k2"].append(num)
# print(dic)


# li = ["手机", "电脑", "鼠标垫", "游艇"]
# dic = {}
# num = 1
# for goods in li:
#     dic.update({num: goods})
#     num += 1
# num -= 1
# ng = input("n_g>>")
# if ng != "":
#     num += 1
#     dic.update({num: ng})
# else:
#     pass
# cn = int(input("cn>>"))
# print(dic[cn])


# l1 = [11,22,33]
# l2 = [22,33,44]
# s1 = set(l1)
# s2 = set(l2)
# print(list(s1&s2))#交集
# print(list(s1-s2))
# print(list(s2-s1))
# print(list(s2^s1))#交叉补集


# for num in range(100,0,-1):
#     print(num)
# for num in range(1,101):
#     print(num)
# num = 0
# while num <=99:
#     num += 1
#     print(num)
# num = 101
# while num > 1:
#     num -= 1
#     print(num)


# f = input("fortune>>")
# goods = [{"name":"电脑","price":1999},
#          {"name":"鼠标","price":10},
#          {"name":"游艇","price":20},
#          {"name":"美女","price":998}
#     ]
# print(goods)
# p = input("purchase>>")
#####method_1#
# for x in goods:
#     if x["name"] == p:
#         cost = x["price"]
#         if cost <= int(f):
#             print("success")
#         else:
#             print("fail")
##### method_2#
# def func(x):
#     if x["name"]==p:
#         return x["price"]
#     else:
#         pass
# pd = list(filter(func,goods))
# pd = list(filter(lambda x:,goods))
# if int(pd[0]["price"]) <= int(f):
#     print("success")
# else:
#     print("fail")



# li = []
# for num in range(1,302):
#     li.append(("alex-%s"%num,"alex%s@live.com"%num,"pwd%s"%num))
# page = input("page>>")
# if page.isdecimal():
#     page = int(page)
#     max = page*10
#     min = page*10-10
#     for item in li[min:max]:
#         print(item)
# else:
#     print("格式错误")


# count = 0
# for i in range(1,9):
#     for j in range(i+1,9):
#         print("%s%s"%(i,j))
#         count += 1
# print(count)


# for i in range(1,10):
#     for j in range(i,10):
#         print("\t")
#         if j == 9:
#             print(str(i) + "*" + str(j) + "=" + str(i * j))
#         else:
#             print(str(i) + "*" + str(j) + "=" + str(i*j) , end=" ")


# nums = [2,7,11,15,1,8,7]
# for n1 in nums:
#     for n2 in nums:
#         if n1 + n2 == 9 and n1 <n2:
#             print((n1,n2))
#         else:
#             pass


# count = 0
# for g in range(1,20):
#     for m in range(1,33):
#         for x in range(1,100):
#             if g*5 + m*3 + x/3 == 100 and g + m + x ==100:
#                 count += 1
# print(count)