def dif(n):
    """compares number to 17"""
    num = 17
    #inum = input("Enter num ")
    res = int(n) - num
    print("dif is: ", res)

    if res >= 0:
        res = res*2
        print("dif is doubled = ", res)
        #return res
    else:
        print("the numb®er is less then 17 is: ", n)
#dif(n)

inum = input("enter number ")
#int(inum)
dif(inum)