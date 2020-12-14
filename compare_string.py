def com(t,t1):

    for i in t:
        for j in t1:
            if i != j:
                print(i, j)
            else:
                pass


txt1 = input("enter first string ")
txt2 = input("second string ")
com(txt1,txt2)