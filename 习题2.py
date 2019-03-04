# def pd(str):
#     capital = 0
#     lower = 0
#     digit = 0
#     for item in str:
#         if item.isupper() == 1:
#             capital += 1
#         if item.islower() == 1:
#             lower += 1
#         if item.isdigit() == 1:
#             digit += 1
#     return {"capital":capital,"lower":lower,"digit":digit}
# print(pd("Alex123"))


# def func(*y,**z):
#     print(y,z)
# func(*[1,2,3,4,5],{"name":"alex","age":19})


def func(*y,**z):
    print(y,z)
func(*[1,2,3,4,5],**{"name":"alex","age":19})



