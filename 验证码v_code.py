import random

def v_code():
    res = ""
    for i in range(1,7):
        num = random.randint(0,9)
        alf = chr(random.randint(65,122))
        s = str(random.choice([num,alf]))
        res += s
    return res





print(v_code())