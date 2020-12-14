import os
import sys

def gre(a, b,):

  ai = []
  bi = []
  bigger = 0

  for i in range(a):
      if a % (i + 1) == 0:
         ai.append(i + 1)
  print("ai is ",ai)

  for j in range(b):
      if b % (j + 1) == 0:
          bi.append(j + 1)
  print("bi is ",bi)

  common = set(ai).intersection(bi)
  common = list(common)
  print("common are: ", common)
  #print("bigger is: ", max(common))

  for f in common:
      if f > bigger:
          bigger = f
  else:
      pass

  return(bigger)


a = int(input("Enter first positive number "))
b = int(input("Enter second positive number "))

if a > 0 and b > 0:
    print("the biggest common number is ",gre(a,b))
else:
    print("enter positive numbers only")
    #os.execv(sys.argv[0], sys.argv)
    os.system("python greatest_GCD.py")
    #print("Restarting...")
    #time.sleep(0.2)  # 200ms to CTR+C twice