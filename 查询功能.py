def fetch():
    print("这是查询功能")
    print("用户数据是 %s" %data)
    with open("test","r")as read_test:
        for read_line in read_test:
            if read_line.strip() == data:
                tag = True
                continue
            if tag:
                print(read_line)



def add():
    pass

def change():
    pass

def delete():
    pass

if __name__ == "__main__":
    msg =''' 
    1: 查询
    2: 添加
    3: 修改
    4: 删除
    5: 退出
    
    '''
    msg_dic = {
        "1" : fetch,
        "2" : add,
        "3" : change,
        "4" : delete
    }
    while True:
        print(msg)
        choice = input("请输入您的选项").strip()
        if not choice :
            continue
        if choice == "5":
            break
        data = input("请输入您数据")
        if choice == "1":
            fetch()
        # if choice == "2":
        # if choice == "3":
        # if choice == "4":