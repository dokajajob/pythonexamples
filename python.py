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