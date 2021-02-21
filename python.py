statistics
  import cProfile
  def sum(): print(1+2)
  cProfile.run('sum()')

3
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 7aa14930-2430-11e7-807b-bd9de91b1602.py:2(sum)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

environment variables
import os
# Access all environment variables
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

current username.
import getpass print(getpass.getuser())
find local IP addresses

import socket s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) s.connect(("8.8.8.8", 80)) print(s.getsockname()[0]) s.close()

height and the width of console window.

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())

5) time (in seconds) for a Python method

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

6) absolute file path.

def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')
print("Absolute file path: ",absolute_file_path("test.txt"))

7) creation and modification date/times.

import os.path, time print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt"))) print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script
import sys print("This is the name/path of the script:"),sys.argv[0] print("Number of arguments:",len(sys.argv)) print("Argument List:",str(sys.argv))

find the available built-in modules.
import sys import textwrap module_name = ', '.join(sorted(sys.builtin_module_names)) print(textwrap.fill(module_name, width=70))

8) size of an object in bytes.
import sys str1 = "one" str2 = "four" str3 = "three" print() print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes") print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes") print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes") print()
 recursion limit.
import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()

9) sum over a container.
s = sum([10,20,30]) print("\nSum of the container: ", s) print()

test whether all numbers of a list is greater than a certain number

num = [2,3,4] print() print(all(x > 1 for x in num)) print(all(x > 4 for x in num)) print()
number of occurrence of a specific character in a string.
s = "The quick brown fox jumps over the lazy dog."
print()
print(s.count("q"))
print()

10) whether a file path is a file or a directory.

import os
path="abc.txt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)" )
print()

11) ASCII value of a character.

print()
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))
print()


12) size of a file.

import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()

print("\n%d+%d=%d" % (x, y, x+y))

13) get the identity of an object.

obj1 = object()
obj1_address = id(obj1)
print()
print(obj1_address)
print()

14) URL's content to the console.

from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")
result = conn.getresponse()
# retrieves the entire contents.
contents = result.read()
print(contents)

15) determine whether variable is defined or not.

try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")

16) program to retrieve file properties.

import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

17) numbers divisible by fifteen from a list using an anonymous function.

num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)

18) make file lists from current directory using a wildcard.

import glob
file_list = glob.glob('*.*')
print(file_list)

19) remove the first item from a specified list.

color = ["Red", "Black", "Green", "White", "Orange"]
print("\nOriginal Color: ",color)
del color[0]
print("After removing the first color: ",color)
print()

20) compute the product of a list of integers (without using for loop).

from functools import reduce
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)

21) Unicode characters

str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()

22) program to prove that two string variables of same value point same memory location.

str1 = "Python"
str2 = "Python"
 
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()

23) create a bytearray from a list.

print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()

24) program to format a specified string to limit the number of characters to 6.

str_num = "1234567890"
print()
print('%.6s' % str_num)
print()

25) display a floating number in specified numbers.

order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()

26) determine the largest and smallest integers, longs, floats.

import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 

27) sum of all counts in a collections.

import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))

28) program to check whether an integer fits in 64 bits.

int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())

29)  whether lowercase letters exist in a string.

str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))

30)  program to add trailing and leading zeroes to a string.

str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)

31) program to use double quotes to display strings.

import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

32) split a variable length string into variables.

var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)

33) program to calculate the time runs (difference between start and current time)of a program.

from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)

34) Write a Python program to input two integers in a single line.

print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)

35) Write a Python program to find files and skip directories of a given directory.

import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])

36) Write a Python program to extract single key-value pair of a dictionary in variables.

d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)

37) Write a Python program to convert true to 1 and false to 0.


x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)

38) Write a Python program to valid an IP address.

import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
	
39) Write a Python program to convert an integer to binary keep leading zeros.

x = 12
print(format(x, '08b'))
print(format(x, '010b'))

40) Write a python program to convert decimal to hexadecimal.

x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))

41) Write a Python program to find the operating system name, platform and platform release date.

import os, platform
print("Operating system name:")
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())

42) Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.

import struct
print(struct.calcsize("P") * 8)

43) Write a Python program to check whether a variable is integer or string.

print(isinstance(25,int) or isinstance(25,str))
print(isinstance([25],int) or isinstance([25],str))
print(isinstance("25",int) or isinstance("25",str))


44) Write a Python program to test if a variable is a list or tuple or a set.

#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')
45) Write a Python program to find the location of Python module sources.

import sys
print("\nList of directories in sys module:")
print(sys.path)
print("\nList of directories in os module:")
import os
print(os.path)

46) Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.

def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))

47) Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
 
 def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

48) Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

def sum_of_cubes(n):
  n -= 1
  total = 0
  while n > 0:
    total += n * n * n
    n -= 1
  return total
print("Sum of cubes: ",sum_of_cubes(3))

49) Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.

def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
          return False
          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));

product & 1 means check whether product is odd, because the last digit of binary representation of an odd number always is 1 while for an even number is 0.

Here's how to calculate 5 & 9:

1) transform 5 to binary representation (5)10 = (101)2

2) transform 9 to binary representation (9)10 = (1001)2

3) for every binary digit, & with two 1 is 1 otherwise 0. 



50) Python List reverse()
The reverse() method reverses the elements of the list.

ads via Carbon
No code required, set up in minutes! Flatfile Concierge turns data onboarding into a collaborative experience.
ADS VIA CARBON
The syntax of the reverse() method is:

list.reverse()
reverse() parameter
The reverse() method doesn't take any arguments.

Return Value from reverse()
The reverse() method doesn't return any value. It updates the existing list.

Example 1: Reverse a List
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)
Output

Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']
There are other several ways to reverse a list.

Example 2: Reverse a List Using Slicing Operator
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list  
#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)
Output

Original List: ['Windows', 'macOS', 'Linux']
Updated List: ['Linux', 'macOS', 'Windows']
Example 3: Accessing Elements in Reversed Order
If you need to access individual elements of a list in the reverse order, it's better to use reversed() function.

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)
Output

Linux
macOS
Windows