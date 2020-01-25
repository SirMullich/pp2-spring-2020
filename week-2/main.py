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


if __name__ == '__main__':
    # print(is_it_true(3))
    # print(is_it_true('this is string'))
    # print(is_it_true(math.pi))
    # print(is_it_true(0.0))
    list_intro()


# print('Hello World')