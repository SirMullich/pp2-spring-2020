import os
from pathlib import Path

# lists
def working_with_lists():
    a_list = ['just', 'another', 'cool', 'list', 'here']
    print(a_list[0])
    print(a_list[2])
    print(a_list[-1])
    print(a_list[1:3])
    print(a_list[2:])
    print(a_list[:-3])

# entries = os.scandir('/home/daulet')


# clear console method
def cls():
    os.system('cls' if os.name=='nt' else 'clear')  


# Working with files (read and write)

# mode can be 'r' when the file will only be read, 
# 'w' for only writing (an existing file with the same name will be erased), 
# and 'a' opens the file for appending; any data written to the file is automatically added to the end. 
# 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

# reading from file in relative path
def read():
    currentPath = os.getcwd()
    print(currentPath)
    with open(os.path.join(currentPath, 'week-2/data/numbers.txt'), 'r') as file:
        line = file.readline()
        nums = line.split(' ')
        print('This is a list of nums from file: {0}'.format(nums))
        numsSum = 0
        for num in nums:
            numsSum += int(num)
        print('Sum of nums is: {0}'.format(numsSum))
        return numsSum


def write_to_file(nums: list):
    '''Write numbers from input list to file.

    Keyword arguments:
    nums -- list of numbers

    Returns: None

    '''
    current_path = os.getcwd()
    with open(os.path.join(current_path, 'week-2/data/even_numbers.txt'), 'w') as file:
        for num in nums:
            if (num % 2 == 0): 
                file.write(str(num) + ' ')

def show_files_and_dirs(dir_path: str):
    '''Show directories and files in current directory

    Keyword arguments:
    dir_path -- path of directory

    Returns: None

    '''

    with os.scandir(dir_path) as scan:
        for entry in scan:
            if (entry.is_file()): 
                print(entry.name)

    # subfolders = [ f.path for f in os.scandir(dir_path) if f.is_dir() ]
    # print(subfolders)

    # for root, dirs, files in os.walk(dir_path):
    #     print(root)
    #     print(dirs)
    #     print(files)

if __name__ == '__main__':
    # working_with_lists()
    # read()
    # print(write_to_file([5, 6, 10, 82, 19]))
    show_files_and_dirs(os.getcwd())