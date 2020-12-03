class volume:
   def cal():
      """calculates volume of sphere"""
      from fractions import *
      import math

      r = input('enter radius ')

      #step1 = Fraction(4,3) * math.pi
      #print(step1)

      #step2 = int("%s%s%s" % (r,r,r))
      #print(step2)

      #V= 4.0/3.0*pi* r**3

      v = Fraction(4,3) * math.pi * (r**3)
      print("volume of sphere is : ", v)
   cal()
