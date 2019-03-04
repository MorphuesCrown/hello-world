# def recur(n1,n2):
#     print(n1+n2)
#     return recur(n2,n1+n2)
# recur(0,1)



n1 = 0
n2 = 1
for i in range(10):
    print(n1+n2)
    n1 , n2 = n2 , n1+n2
