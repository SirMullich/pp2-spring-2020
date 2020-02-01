# keys = 1000 and 1024
# values = list, list of Strings
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes = True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    # muliple = 1000 or 1024
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    # traverse list
    # ex: SUFFIXES[multiple] -> ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    # ex: multiple = 1000
    for suffix in SUFFIXES[multiple]: # for (int i = 0; i < SUFFIXES[multiple].len; i++)
        # 1) 10000000 / 1000 -> 10000
        # 2) 10000 / 1000 -> 10
        size /= multiple # size = size / multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix) # string interpolation (build a string)

    raise ValueError('number too large')

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def tenth(num):
    if (num >= 90):
        return "90-100"
    elif (num >= 80):
        return "80-90"
    elif (num >= 70):
        return "70-80"
    else:
        return "0-70"

def greeting():
    name = input('Please input your name: ')
    return 'Welcome {0}'.format(name)

if __name__ == '__main__':
    # print(approximate_size(10000000, False))
    # print(approximate_size(1000000000000))
    # print(is_odd(101))
    # print(tenth(47))
    # print(tenth(94))
    # greet1 = greeting()
    # print(greet1)
    # print(approximate_size.__doc__)

    import sys
    print(sys.path)