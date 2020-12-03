def dif():
    """compares number to 17"""
    num = 17
    inum = input("Enter num ")
    res = int(inum) - (num)
    print(res)

    if res >= 0:
        res = res*2
        print("dif is doubled = ", res)
        #return res
    else:
        print("the number is less then 17")
dif()
