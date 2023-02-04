import math
from functools import lru_cache


@lru_cache(maxsize=5)
def fib(integer):
    if integer == 0:
        return 1
    elif integer == 1:
        return 1
    else:
        print(f'fib {integer} is applied...')
        return fib(integer-1) + fib(integer-2)


fib(100)

#this line is to make changes
#xyzxyzabc


def func2(*args):
    return sum(args)


print(func2(3, 4, 5, 6))


#another change is done


#sjkfnsbfhs

#do some extra jobs
for i in range(0, 100):
    print(f'{i}, step executed')
"""""
with open("/Users/hasanegetunc/PycharmProjects/pythonProject3/file1.csv", "w") as f:
    f.write("i\t, fib\t, fact\t, gcd,\n")
    for i in range(0, 100):
        f.write(",\t".join([str(i), str(fib(i)), str(math.factorial(i)), str(math.gcd(math.factorial(i), fib(i)))]))
        f.write("\n")


def decorate_to_rff(function):
    def inner(file_name, *args):
        if args[0] < 0:
            raise ValueError('Argument must be at least 0')
        elif args[0] < 100:
            with open(file_name) as file:
                next(file)
                target_list = []
                for row in file:
                    content = row.split(',\t')
                    content = [c.strip(',\n') for c in content]
                    target_list.append(int(content[args[1]]))
                return target_list[args[0]]
        else:
            return function(args[0])
    return inner


@decorate_to_rff
def proper_gcd(integer):
    return math.gcd(math.factorial(i), fib(i))


fib_updated = decorate_to_rff(fib)
math_factorial_updated = decorate_to_rff(math.factorial)
"""

""""
def fib2(integer, fileName):
    with open(fileName) as file:
        next(file)
        target_list = []
        for row in file:
            content = row.split(',\t')
            content = [c.strip(',\n') for c in content]
            target_list.append(int(content[1]))

    if integer < 0:
        raise ValueError('Argument must be at least 0')
    elif integer < 100:
        return target_list[integer]
    else:
        return fib(integer)
"""
"""
while True:
    intV = input("Enter the integer val(q to quit) ")
    if intV.casefold() == 'q'.casefold():
        break
    else:
        intV = int(intV)
        print(f"Fib {intV} is:", fib_updated("/Users/hasanegetunc/PycharmProjects/pythonProject3/file1.csv", intV, 1))
        print(f"Fact {intV} is:", math_factorial_updated("/Users/hasanegetunc/PycharmProjects/pythonProject3/file1.csv",
                                                         intV, 2))
        print(f"Gcd {intV} is:", proper_gcd("/Users/hasanegetunc/PycharmProjects/pythonProject3/file1.csv", intV, 3))
"""
#file end of statement
