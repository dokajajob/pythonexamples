def dif(n):
    """compares number to 1000 and 2000"""

    if int(n) > 100 and int(n) < 1000:
        print("num is between 100 and 1000 is: ", n)
    elif int(n) > 1000 and int(n) < 2000:
        print("num is between 1000 and 2000 is: ", n)
    else:
        print("num is not in range of 100 and 2000. num is: ", n)


inum = input("enter number ")
dif(inum)
