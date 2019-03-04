import pickle
import hashlib




class School:
    def __init__(self,num,name,locat,president):
        self.num = num
        self.name = name
        self.locat = locat
        self.president = president

    def save(self):
        #将单个学校的信息存到单个文件
        #打包——待实现
        with open(self.name,"wb") as f:
            pickle.dump(self,f)

    def save__(self):
        #将单个学校的信息存到单个文件
        #打包——待实现
        with open("学校目录","wb") as f:
            pickle.dump(self.name,f)


    def loads(self):
        return pickle.load(open(self.name,"rb"))

    def loads__(self):
        with open("学校目录","rb")as f:
            pickle.load(f)
    # def sch_dict(self):
    #     dic = {}
    #     dic[] = self.name
    #
    #
    # def store_sch_dict(self):
    #     with open("学校大全","wb") as g:
    #         pickle.dump(self,g)




class Curriculum(School):
    def __init__(self,name,price,period,school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school

        #继承School的save和loads

# s1 = School("tianyi","wuxi","smd")
# s1.save()
# s2 = School("nanwai","nanjing","xxx")
# s2.save()
# s3 = School("gifted_program","wuxi","xx")
# s3.save()


# school_obj1 = School.loads(s1)
# school_obj2 = School.loads(s2)
# school_obj3 = School.loads(s3)
# print(1,school_obj1.name,school_obj1.locat)
# print(2,school_obj2.name,school_obj2.locat)
# print(3,school_obj3.name,school_obj3.locat)



while True:
    #  创建学校
    if input("是否创建学校(y/n)")=="y":
        pass
    else:
        break
    sch_num = input("序号>>")
    sch_name = input("学校名称>>")
    sch_locat = input("学校地址>>")
    sch_pres =input("校长？>>?")
    s = School(sch_num,sch_name,sch_locat,sch_pres)
    s.save()
    s.save__()
    school_obj = School.loads(s)
    print("学校信息",school_obj.num,school_obj.name,school_obj.locat)
    if input("是否继续（y/n）")=="y":
        pass
    else:
        break
sch_dic = School.loads__(789)
print(sch_dic)





# msg = '''
# 1 tianyi wuxi smd
# 2 nanwai nanjing xxx
# 3 gifted_program wuxi xx
# '''
#
# while True:
#     创建课程
#     print(msg)
#     menu = {
#         "1": s1,
#         "2": s2,
#         "3": s3,
#     }
#     cho1 = input("选择学校>>")
#     ch_sch = menu[cho1]
#     ch2 = input("课程创建>>")
#     ch3 = input("费用>>")
#     ch4 = input("周期>>")
#     new_course = Curriculum(ch2,ch3,ch4,ch_sch)
#     print("课程【%s】地点【%s】" %(new_course.name,new_course.school.name))

