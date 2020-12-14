def diff(l1,l2):


    #print(set(l1) - set(l2))
    #print(set(l2) - set(l1))
    l1 = set(l1)
    l2 = set(l2)
    print(l1.difference(l2))

l1 = input("enter list 1 ")
l2 = input("enter list 2 ")
diff(l1,l2)
