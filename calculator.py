import re


def kongge(ss):
    return re.sub(" ", "", ss)


def kuohao(ss):
    return re.search("\([^()]*\)", ss).group()


def qkh(p):
    return re.sub("(.*)", "", p)


def jisuan(p):
    num = re.split("\D+", p)
    f = re.split("\d*", p)
    while "" in num:
        num.remove("")
    while "" in f:
        f.remove("")
    while "(" and ")" in f:
        f.remove("(")
        f.remove(")")
    # print(num, f)
    n1 = 0
    for i in range(0, len(f)):
        if f[i] == "*":
            n1 = int(num[i]) * int(num[i + 1])
            n1 = int(n1)
            # print(num[i] + f[i] + num[i + 1])
            p = p.replace(num[i] + f[i] + num[i + 1], str(n1))
            # print(p)
        if f[i] == "/":
            n1 = int(num[i]) / int(num[i + 1])
            n1 = int(n1)
            # print(num[i] + f[i] + num[i + 1])
            p = p.replace(num[i] + f[i] + num[i + 1], str(n1))
            # print(p)
    num = re.split("\D+", p)
    f = re.split("\d*", p)
    while "" in num:
        num.remove("")
    while "" in f:
        f.remove("")
    while "(" and ")" in f:
        f.remove("(")
        f.remove(")")
    for j in range(0, len(f)):
        if f[j] == "+":
            n1 = int(num[j]) + int(num[j + 1])
            n1 = int(n1)
            # print(num[j] + f[j] + num[j + 1])
            p = p.replace(num[j] + f[j] + num[j + 1], str(n1))
            # print(p)
        if f[j] == "-":
            n1 = int(num[j]) - int(num[j + 1])
            n1 = int(n1)
            # print(num[j] + f[j] + num[j + 1])
            p = p.replace(num[j] + f[j] + num[j + 1], str(n1))
            # print(p)
    while "(" and ")" in p:
        p = p.replace(p[0],"")
        p = p.replace(p[-1],"")
    return p


ss = input("请输入算式>>")
ss = kongge(ss)
while True:
    if ss.isdigit() == 1:
        print(ss)
        break
    if "(" not in ss and ss.isdigit() == 0:
        ss = jisuan(ss)
    else:
        p = kuohao(ss)
        # print(p)
        p1 = jisuan(p)
        ss = ss.replace(p,p1)


#出现负数——比较num与f的长度若f的长度>=num的长度，则含有负号
#找负号re 匹配"-"左右不都为数字的即为负号
#计算时将负号剔除再用索引