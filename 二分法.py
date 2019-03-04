li = [1, 3, 6, 56, 78, 90, 999, 7890]
x = int(input(">>"))
i = len(li)
j = 0
while (x < li[i - 1]):
    mid = i // 2
    if (x == li[mid]):
        print("yes")
        break
    elif (x > li[mid]):
        j = mid
    elif (x < li[mid]):
        i = mid
    if (i == j or i - j <= 1 or i - j >= 1 and li[i] != x):
        print("the element does not exist")
        break
