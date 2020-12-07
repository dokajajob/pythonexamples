def nn(n):

#    for i in range (0, len(n)):
#        n[i] = int(n[i])

    for i in n:
        if i >= 0:
          print (i)
        else:
          print (i * -1)

#nl = [1,-1,2,-2]
#l = []
#nl = input('enter string with negative numbers too ')
nl = [int(l) for l in input('enter numbers with negative too ').split()]
print("the list is: ", nl)
#print("result: ", nn(nl))
nn(nl)