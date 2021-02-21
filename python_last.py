1) Write a Python program to find out the number of CPUs using.

Sample Solution:-

Python Code:

import multiprocessing
print(multiprocessing.cpu_count())


2) statistics
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

3) environment variables
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

4) current username.
import getpass print(getpass.getuser())

5) find local IP addresses

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

51) Python List insert()
The list insert() method inserts an element to the list at the specified index.




The syntax of the insert() method is

list.insert(i, elem)
Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.

insert() Parameters
The insert() method takes two parameters:

index - the index where the element needs to be inserted
element - this is the element to be inserted in the list
Notes:

If index is 0, the element is inserted at the beginning of the list.
If index is 3, the element is inserted after the 3rd element. Its position will be 4th.
Return Value from insert()
The insert() method doesn't return anything; returns None. It only updates the current list.

Example 1: Inserting an Element to the List
# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')

print('Updated List:', vowel)
Output

Updated List: ['a', 'e', 'i', 'o', 'u']
Example 2: Inserting a Tuple (as an Element) to the List
mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List:', mixed_list)
Output

Updated List: [{1, 2}, (3, 4), [5, 6, 7]]

52) Python List copy()
The copy() method returns a shallow copy of the list.


No code required, set up in minutes! Flatfile Concierge turns data onboarding into a collaborative experience.

A list can be copied using the = operator. For example,

old_list = [1, 2, 3]
​new_list = old_list
The problem with copying lists in this way is that if you modify new_list, old_list is also modified. It is because the new list is referencing or pointing to the same old_list object.

old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
Output

Old List: [1, 2, 3, 'a']
New List: [1, 2, 3, 'a']
However, if you need the original list unchanged when the new list is modified, you can use the copy() method.

Related tutorial: Python Shallow Copy Vs Deep Copy

The syntax of the copy() method is:

new_list = list.copy()
copy() parameters
The copy() method doesn't take any parameters.

Return Value from copy()
The copy() method returns a new list. It doesn't modify the original list.

Example 1: Copying a List
# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()

print('Copied List:', new_list)
Output

Copied List: ['cat', 0, 6.7]
If you modify the new_list in the above example, my_list will not be modified.

Example 2: Copy List Using Slicing Syntax
# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)
Output

Old List: ['cat', 0, 6.7]
New List: ['cat', 0, 6.7, 'dog']

53) Python List append()
The append() method adds an item to the end of the list.


No code required, set up in minutes! Flatfile Concierge turns data onboarding into a collaborative experience.

The syntax of the append() method is:

list.append(item)
append() Parameters
The method takes a single argument

item - an item to be added at the end of the list
The item can be numbers, strings, dictionaries, another list, and so on.

Return Value from append()
The method doesn't return any value (returns None).

Example 1: Adding Element to a List
# animals list
animals = ['cat', 'dog', 'rabbit']

# 'guinea pig' is appended to the animals list
animals.append('guinea pig')

# Updated animals list
print('Updated animals list: ', animals)
Output

Updated animals list:  ['cat', 'dog', 'rabbit', 'guinea pig']
Example 2: Adding List to a List
# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to the animals list
animals.append(wild_animals)

print('Updated animals list: ', animals)
Output

Updated animals list:  ['cat', 'dog', 'rabbit', ['tiger', 'fox']]
It is important to notice that, a single item (wild_animals list) is added to the animals list in the above program.

If you need to add items of a list to another list (rather than the list itself), use the extend() method.

54) Python List count()
The count() method returns the number of times the specified element appears in the list.


Build Modern Messaging Experiences in Minutes. Try Pro Features. 30-Day Free Trial!

The syntax of the count() method is:

list.count(element)
count() Parameters
The count() method takes a single argument:

element - the element to be counted
Return value from count()
The count() method returns the number of times element appears in the list.

Example 1: Use of count()
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
Output

The count of i is: 2
The count of p is: 0
Example 2: Count Tuple and List Elements Inside List
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

Output

The count of ('a', 'b') is: 2
The count of [3, 4] is: 1

55) Python List remove()
The remove() method removes the first matching element (which is passed as an argument) from the list.


Benchmarking the Cloud: AWS vs GCP vs Azure. Read the 2021 Cloud Report ->

The syntax of the remove() method is:

list.remove(element)
remove() Parameters
The remove() method takes a single element as an argument and removes it from the list.
If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
Return Value from remove()
The remove() doesn't return any value (returns None).

Example 1: Remove element from the list
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)
Output

Updated animals list:  ['cat', 'dog', 'guinea pig']
Example 2: remove() method on a list having duplicate elements
If a list contains duplicate elements, the remove() method only removes the first matching element.

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals)
Output

Updated animals list:  ['cat', 'dog', 'guinea pig', 'dog']
Here, only the first occurrence of element 'dog' is removed from the list.

Example 3: Deleting element that doesn't exist
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)
Output

Traceback (most recent call last):
  File ".. .. ..", line 5, in <module>
    animal.remove('fish')
ValueError: list.remove(x): x not in list
Here, we are getting an error because the animals list doesn't contain 'fish'.

If you need to delete elements based on the index (like the fourth element), you can use the pop() method.
Also, you can use the Python del statement to remove items from the list.

56) Python List pop()
The pop() method removes the item at the given index from the list and returns the removed item.


Octopus Deploy simplifies even the most complex deployments & IT ops automation tasks. Get started free.

The syntax of the pop() method is:

list.pop(index)
pop() parameters
The pop() method takes a single argument (index).
The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.
Return Value from pop()
The pop() method returns the item present at the given index. This item is also removed from the list.

Example 1: Pop item at the given index from the list
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)
Output

Return Value: French
Updated List: ['Python', 'Java', 'C++', 'C']
Note: Index in Python starts from 0, not 1.

If you need to pop the 4th element, you need to pass 3 to the pop() method.

Example 2: pop() without an index, and for negative indices
# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:') 
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)
Output

When index is not passed:
Return Value: C
Updated List: ['Python', 'Java', 'C++', 'Ruby']

When -1 is passed:
Return Value: Ruby
Updated List: ['Python', 'Java', 'C++']

When -3 is passed:
Return Value: Python
Updated List: ['Java', 'C++']
If you need to remove the given item from the list, you can to use the remove() method.

And, you can use the del statement to remove an item or slices from the list.

57) Python List sort()
The sort() method sorts the elements of a given list in a specific ascending or descending order.


Benchmarking the Cloud: AWS vs GCP vs Azure. Read the 2021 Cloud Report ->

The syntax of the sort() method is:

list.sort(key=..., reverse=...)
Alternatively, you can also use Python's built-in sorted() function for the same purpose.

sorted(list, key=..., reverse=...)
Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

sort() Parameters
By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

reverse - If True, the sorted list is reversed (or sorted in Descending order)
key - function that serves as a key for the sort comparison
Return value from sort()
The sort() method doesn't return any value. Rather, it changes the original list.

If you want a function to return the sorted list rather than change the original list, use sorted().

Example 1: Sort a given list
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)
Output

Sorted list: ['a', 'e', 'i', 'o', 'u']
Sort in Descending order
The sort() method accepts a reverse parameter as an optional argument.

Setting reverse = True sorts the list in the descending order.

list.sort(reverse=True)
Alternately for sorted(), you can use the following code.

sorted(list, reverse=True)
Example 2: Sort the list in Descending order
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)
Output

Sorted list (in Descending): ['u', 'o', 'i', 'e', 'a']
Sort with custom function using key
If you want your own implementation for sorting, the sort() method also accepts a key function as an optional parameter.

Based on the results of the key function, you can sort the given list.

list.sort(key=len)
Alternatively for sorted:

sorted(list, key=len)
Here, len is the Python's in-built function to count the length of an element.

The list is sorted based on the length of each element, from lowest count to highest.

We know that a tuple is sorted using its first parameter by default. Let's look at how to customize the sort() method to sort using the second element.

Example 3: Sort the list using key
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
Output

Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]
Let's take another example. Suppose we have a list of information about the employees of an office where each element is a dictionary.

We can sort the list in the following way:

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')
Output

[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]
Here, for the first case, our custom function returns the name of each employee. Since the name is a string, Python by default sorts it using the alphabetical order.

For the second case, age (int) is returned and is sorted in ascending order.

For the third case, the function returns the salary (int), and is sorted in the descending order using reverse = True.

It is a good practice to use the lambda function when the function can be summarized in one line. So, we can also write the above program as:

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')
Output

[{'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}]

[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]

[{'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'John Hopkins', 'age': 18, 'salary': 1000}]
To learn more about lambda functions, visit Python Lambda Functions.

58) Python List clear()
The clear() method removes all items from the list.




The syntax of clear() method is:

list.clear()
clear() Parameters
The clear() method doesn't take any parameters.

Return Value from clear()
The clear() method only empties the given list. It doesn't return any value.

Example 1: Working of clear() method
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)
Output

List: []
Note: If you are using Python 2 or Python 3.2 and below, you cannot use the clear() method. You can use the del operator instead.

Example 2: Emptying the List Using del
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)
Output

List: []
Visit this page to learn how del operator works in Python.

59) Python List index()
The index() method returns the index of the specified element in the list.


Students and Teachers, save up to 60% on Adobe Creative Cloud.

The syntax of the list index() method is:

list.index(element, start, end)
list index() parameters
The list index() method can take a maximum of three arguments:

element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index
Return Value from List index()
The index() method returns the index of the given element in the list.
If the element is not found, a ValueError exception is raised.
Note: The index() method only returns the first occurrence of the matching element.

Example 1: Find the index of the element
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
Output

The index of e: 1
The index of i: 2
Example 2: Index of the Element not Present in the List
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of'p' is vowels
index = vowels.index('p')
print('The index of p:', index)
Output

ValueError: 'p' is not in list
Example 3: Working of index() With Start and End Parameters
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)   # Error!
print('The index of i:', index)
Output

The index of e: 1
The index of i: 6
Traceback (most recent call last):
  File "*lt;string>", line 13, in 
ValueError: 'i' is not in list