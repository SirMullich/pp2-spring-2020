import math

def is_it_true(anything):
    if anything:
        return 'TRUE'
    else: 
        return 'FALSE'


def list_intro():
    my_list = [9, 10, 1, 90, 83] # list of numbers
    print(my_list)
    
    # index: 0, 1, 2
    # index: -3, -2, -1    (len - 3, len - 2, len - 1)
    my_list_2 = ['my', 'her', 'university'] # list of string
    my_list_3 = ['string', 5, 9.0, [8, '45']] # list of many

    print(my_list_3)

    print(my_list_2[2])

    print(my_list_2[-3])

    # Slicing
    # start = 1 (INCLUSIVE), end = 3 (EXCLUSIVE)    
    print(my_list[1:3]) # [1, 3) -> 1, 2 (NOT 3)
    print(my_list[0:4])
    print(my_list[:4])

    print(my_list[2:])

    # only append 1 value
    my_list.append(98)
    print(my_list)

    my_list.insert(2, 1000)
    print(my_list)

    # adding two lists
    print(my_list + my_list_2)

    my_list.extend([2001, 2002, 2003, 2004])
    print(my_list)
    my_list.append([2001, 2002, 2003, 2004])
    print(my_list)

    my_list.append(90)
    # [9, 10, 1000, 1, 90, 83, 98, 2001, 2002, 2003, 2004, [2001, 2002, 2003, 2004], 90]

    print('Count of 90 in the list: {0}'.format(my_list.count(90)))

    # 'in' keyword
    print('in keyword: {0}'.format(90 in my_list))

    # index
    print('First index of 90 in the list: {0}'.format(my_list.index(90)))

    # print(my_list.index(86534))  # exception

    if 86534 in my_list:
        print(my_list.index(86534))

    # delete value at index 0
    del my_list[0]
    print(my_list)

    # remove value 90 from list
    my_list.remove(90)
    print('List after removing 90: {0}'.format(my_list))

    # pop
    print('Last value from list: {0}'.format(my_list.pop()))
    print(my_list)

    print('Boolean context of my_list: {0}'.format(is_it_true(my_list)))
    print('Boolean context of empty list: {0}'.format(is_it_true([])))

def tuple_demo(): 
    # immutable -- cannot be changed or modified
    # tuples are read-only
    my_tuple = (89, 1, 20, 100, 74)
    print(my_tuple[2])

    # my_tuple[2] = 1000 # raises exception
    # print(my_tuple)

    # x = 1
    # y = 2
    # z = 3
    # a = 4

    (x, y, z, a) = (1, 2, 3, 4)

    print('x = {0}'.format(x))

    (one, two) = range(1, 3)
    print(two)

    return (8, 9, 10)

def set_demo():
    # set in UNORDERED
    my_set = {8, 9, 8, 8, 8, 10} # multiple 8's
    print(my_set)

    # list is ORDERED
    my_list = [10, 10, 10, 1, 1, 1, 2]
    my_set_2 = set(my_list)
    print(my_set_2)

    my_set_2.add(10)
    my_set_2.add(100)
    my_set_2.add(100)
    print(my_set_2)

    print('Length of my_set_2 is: {0}'.format(len(my_set_2)))

    # same as extend method in list
    my_set_2.update({10, 1, -4})
    print(my_set_2)

    my_set_2.discard(-10000)
    #my_set_2.remove(-10000) # exception
    print(my_set_2)

    print(my_set_2.pop())
    print(my_set_2)
    my_set_2.clear()
    print(is_it_true(my_set_2))


if __name__ == '__main__':
    # print(is_it_true(3))
    # print(is_it_true('this is string'))
    # print(is_it_true(math.pi))
    # print(is_it_true(0.0))
    # list_intro()

    # (x, y, z) = tuple_demo()
    # print('Returned value from tuple_demo is: {0}'.format(x))
    set_demo()


# print('Hello World')











