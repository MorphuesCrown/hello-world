# scq = (i for i in range(10))
# print(list(scq))


# def test():
#     yield "son"     #return
#     yield "grandson"
#     yield "grandgrandson"
# res = test()
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())


# def produce_baozi():
#     res = []
#     for i in range(100):
#         res.append("baozi%s" %i)
#     return res
# baozi_list = produce_baozi()
# print(baozi_list)


# def produce_baozi():
#     for i in range(100):
#         yield ("baozi%s" %i)
# baozi_list = produce_baozi()
# bz1 = baozi_list.__next__()
# # 加代码
# bz2 = baozi_list.__next__()
# #加代码
# bz3 = baozi_list.__next__()
# #加代码
# bz4 = baozi_list.__next__()
# #此过程相当于for循环，且优势在于每取出一个元素都可立即对其进行操作无需等所有元素取完


def get_population():
    with open("人口普查","r",encoding="utf-8") as f:
        for i in f:
            yield i
g = get_population()
# for i in g:
#     print(int(eval(i)["population"]))
# # print(g.__next__()["population"])#看似是字典其实文件的返回值都是str
# g_d = eval(g.__next__())
# print(g_d["population"])

# res = ""
# for p in g:
#     p_dic = eval(p)
#     print(p_dic["population"])
#     res += p_dic["population"]
# print(res)

# all_pop = sum(int(eval(i)["population"]) for i in g)
# print(all_pop)



