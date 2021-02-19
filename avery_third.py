def third_out(numbers):
    i = 0
    print(numbers)
    while len(numbers) > 0:
        for number in range(len(numbers)):
          i += 1
          if i == 3:
            print(number)
            del numbers[number]
            print(numbers)
            i = 0


abc = list(range(10))
#abc = input("Enter list of numbers ")
#abc = abc.split()
third_out(abc)