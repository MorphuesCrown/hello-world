class china:
    "这是一个china类"
    party = "gcd"
    def __init__(self,name,age,texture):
        self.auth = name
        self.nianfeng = age
        self.zhidi = texture
    def ch1(self):
        print("%s使人热爱学习" %self.auth)
    def ch2(self):
        print("%s有%s年历史" %(self.auth,self.nanfeng))
# p1 = china("alex",18,"male")            #与下一行等价
# p1 = china.__init__(p1,"alex",18,male)  #与上一行等价
# s1 = china()   #实例化
# print(china.party)
# print(china.__dict__)   #查看属性字典
# china.ch1(1)            #与下一行等价
# china.__dict__["ch1"](1)#与上一行等价
p1 = china("mo",2000,"jade and earth")
print(p1.__dict__["nianfeng"])
p1.ch1()