def func1(): 
    return 1

def isEven(num):
    if (num % 2 == 0):
        return True
    else:
        return False

def built_in_functions():
    print(abs(-10))
    print(all([True, False, True]))
    print(any([True, False, True]))
    print(ascii("This is almost English Всем привет"))
    print(ascii('¯\_(ツ)_/¯'))
    print(bin(12341234))  # 0b is for binary, 0x is for hexadecimal
    print(hex(12341234))
    print(bool("True"))
    print(bool("Invalid boolean"))
    print(bool(""))
    print(bytearray('string example', 'UTF-8'))
    print(callable(func1))
    print(callable('func1'))
    print(chr(2020))
    eval('print(199)')
    exec('x = 1\ny= 10\nprint(x + y)')

    num_list = [8, 9, 10, 1, 4, 5, 3, 2, -7]
    print(' '.join([str(x) for x in filter(isEven, num_list)]))

    print(hash(100))
    print(hash('asdfasdf'))
    print(hash('my password'))  # hash input -> random number  (hash is one way function, hash must be consistent)
    print(hash('my password'))  # hash -> input (almost impossible)

    # security (off-topic)
    # private key: only you have, only know
    # public key: EVERYONE know
    # you: (private key1, public key1)         other: (private key2, public key2)

    # any message is encrypted using (private key1, public key2) --> other
    # other: to decrypt the message: (private key2, public key1) -> get the message


if __name__ == '__main__':
    built_in_functions()