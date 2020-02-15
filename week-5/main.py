import re


def w3_schools_examples():
    txt = "The rain in Spain. Sometimes it also rains in Germany."
    # . = any character
    # * = 0 or many times
    # adsfasdf, '', 098a7dsf
    print(re.search(".*", txt))
    print(re.search("rain", txt))
    print(re.search("KBTU", txt))

    print(re.findall("rain", txt))
    print(re.split("rain", txt))
    print(re.sub("rain", "snow", txt))

    print(re.search("^The.*Germany.$", txt))
    print(re.search("^The.*Germany.$", "The rain in Spain. It's summer in Germany."))

    print(re.search("^The+", "The"))
    print(re.search("^The+", "Theee"))
    print(re.search("^The+", "Th"))
    print(re.search("^The+", "Theeeeeeeeeeeeeeeeee"))
    print(re.search("^The+", "Theeeeeeeeeeeeeeeeeepiausdf"))
    print(re.search("^The{2}", "Thee"))
    print(re.search("^The{2}", "The"))


    print(re.findall("Portugal", "The rain in Spain"))

    span1 = re.search("\s", "this           is    a    string")
    print('{0} started, {1} ended'.format(span1.start(), span1.end()))

    print(re.split("\s", "this           is    a    string"))
    print(re.split("\s", "this           is    a    string", 2))



if __name__== '__main__':
    w3_schools_examples()