def list_comprehension():
    my_list = [4, 10, 3, 1, -4]
    # multiple every number in my_list by 2

    my_list_2 = []
    for num in my_list:
        my_list_2.append(num * 2)

    print(my_list_2)

    my_list_comp = [10 * num for num in my_list]
    print(my_list_comp)


import os
# Working with files (read and write)

# mode can be 'r' when the file will only be read, 
# 'w' for only writing (an existing file with the same name will be erased), 
# and 'a' opens the file for appending; any data written to the file is automatically added to the end. 
# 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

# path example:
# full path /home/daulet/dev/kbtu/pp2-spring-2020/week-2/week-3
# full path /tmp/example/pp2-spring-2020/week-2/week-3
# relative /pp2-spring-2020/week-2/week-3

# reading from file in relative path
def read():
    currentPath = os.getcwd() # path where program is running
    print(currentPath)

    # opening and managing resources
    with open(os.path.join(currentPath, 'week-2/data/numbers.txt'), 'r') as file:
        line = file.readline()
        nums = line.split(' ')
        print('This is a list of nums from file: {0}'.format(nums))
        numsSum = 0
        for num in nums:
            numsSum += int(num)
        print('Sum of nums is: {0}'.format(numsSum))
        return numsSum


# ensure that nums is a LIST
def write_to_file(nums: list):
    '''Write numbers from input list to file.

    Keyword arguments:
    nums -- list of numbers

    Returns: None

    '''
    current_path = os.getcwd()
    with open(os.path.join(current_path, 'week-2/data/even_numbers.txt'), 'w') as file:
        for num in nums:
            if (num % 2 == 0): # num is not a string
                file.write(str(num) + ' ')

# ensure that dir_path is a string
def show_files_and_dirs(dir_path: str):
    '''Show directories and files in current directory

    Keyword arguments:
    dir_path -- path of directory

    Returns: None

    '''

    with os.scandir(dir_path) as scan:
        for entry in scan:
            # print(entry.name)
            if (entry.is_file()): 
                print(entry.name)

    # subfolders = [ f.path for f in os.scandir(dir_path) if f.is_dir() ]
    # print(subfolders)

    # for root, dirs, files in os.walk(dir_path):
    #     print(root)
    #     print(dirs)
    #     print(files)

# F(n) = F(n - 1) + F(n - 2)
# 1, 1, (1 + 1) = 2, (1 + 2) = 3, (2 + 3) = 5, 8, 13, 21, 34, ...

#   1       1         2         3         5        8
# first, second
#           first second
#                   first     second
#                             first     second

# ensure that returned param is list
# max > 1

# pros: can get a full list, retrieve value by index
# cons: full list takes more space
def fib1(max: int)-> list:
    ans = []
    first = 0
    second = 1

    while(second < max):
        ans.append(second)
        first, second = second, first + second
    
    return ans

# generator
# pros: does not need much memory
# cons: cannot retrive value by index
def fib2(max: int):
    first = 0
    second = 1

    while(second < max):
        yield second
        first, second = second, first + second

def min_max(nums: list) -> tuple:
    return (min(nums), max(nums))


# bonus (1 point): how to make *args typed,
# example: i want args to be only int(s)
def args_example(*args):
    for arg in args:
        print(arg)


def kwargs_example(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('Key: {0}, value: {1}'.format(key, value))


# params: screen, keyboard, size, manufacturer
# CLASS is only a description
# object in an instance of a CLASS
class Notebook:
    # constructor method
    # self = this current object
    def __init__(self, screen: str, keyboard: str, size: int, manufacturer: str):
        self.screen = screen
        self.keyboard = keyboard
        self.size = size
        self.manufacturer = manufacturer

    def isBig(self) -> bool:
        return self.size > 14

class Fib:

    def __init__(self, maximum):
        self.maximum = maximum

    # iterator
    def __iter__(self):
        self.first = 0
        self.second = 1
        return self

    def __next__(self):
        ans = self.second
        if ans > self.maximum:
            raise StopIteration
        self.first, self.second = self.second, self.first + self.second
        return ans




if __name__ == '__main__':
    # list_comprehension()
    # result = read()
    # print(result)
    # write_to_file([8, 9, 5, -4, 100, 57, 72, 87, 44, 81])
    # show_files_and_dirs('/home/daulet/dev/kbtu/pp2-spring-2020')

    print(fib1(100))
    
    # for fibNumber in fib2(100):
    #     print(fibNumber)

    my_list = [8, 0, -5, 10, 43]

    (my_min, my_max) = min_max(my_list)
    #print('Min: {0}, Max: {1}'.format(my_min, my_max))


    # args_example(9, 0, 3, 'paiouqwer', 0.4)
    # kwargs_example(param1 = 'hello', param2 = 1990, param3 = 876)

    notebook1 = Notebook('wide', 'full-sized', 14, 'Lenovo')
    notebook2 = Notebook('normal', 'mini-sized', 17, 'Apple')

    notebook3 = ['wide', 'full-sized', 17, 'IBD'] # no class

    print(notebook1)
    print(notebook1.manufacturer)
    print(notebook2.manufacturer)
    print(notebook1.isBig())

    fib = Fib(1000)
    for fibNum in fib:
        print(fibNum)








