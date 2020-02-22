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
    print(re.split("\s", "this             is    a    string", 2))


def softhints():
    pattern = r"." # any character
    text = "test string:      21"
    print(re.match(pattern, text).span()) # match FIRST
    print(re.search(pattern, text).group()) # search FIRST
    print(re.findall(pattern, text)) # find ALL

    pattern2 = r"kbtu|iitu"
    text2 = "in Almaty kbtu and iitu had a programming contest"
    print(re.match(pattern2, text2)) # None if text starts with 'in Almaty'
    print(re.search(pattern2, text2).span())
    print(re.search(pattern2, text2).group())
    print(re.findall(pattern2, text2))

    pattern3 = r"x+" # r"x{1,}

    pattern4 = r"\d*" # digits that occur 0 or more times
    text4 = "test string number 21"
    print(re.match(pattern4, text4).span())
    print(re.search(pattern4, text4).group())
    print(re.findall(pattern4, text4))

    pattern5 = r"\d+" # digits that occur 1 or more times
    print(re.search(pattern5, text4).group())
    print(re.findall(pattern5, text4))

    pattern6 = r"\d?" # 0 or 1 digit
    print(re.match(pattern6, text4))
    print(re.search(pattern6, text4))
    print(re.findall(pattern6, text4))

    pattern7 = r"23?1"     # 231, 21   -- 3 is optional
    print(re.search(pattern7, "test string is number 21").span())
    print(re.search(pattern7, "test string is number 231").span())
    print(re.search(pattern7, "test string is number 23331"))

    pattern8 = r"\w{3}"
    print(re.findall(pattern8, "test string number 21"))

    pattern9 = r"\w{3,5}\s+" # chars 3-5, with trailing whitespace
    print(re.findall(pattern9, "we are studying in kbtu. this class is pp-2"))

    print(re.findall(r"[xyz2]", "test string number 21"))
    print(re.findall(r"[^tesrin2gu\s]", "test string number 21")) # ^ exclude

    pattern10 = r"(number).(\d+)" # () for group
    text10 = "test string number 21, another number 34"
    print(re.findall(pattern10, text10))
    print(re.search(pattern10, text10).group()) # number 21
    print(re.search(pattern10, text10).group(1)) # number
    print(re.search(pattern10, text10).group(2)) # 21


    # Email
    # username@domain.zone
    # username = chars a-z 1 or more times
    # @ - separates username and domain
    # domain = chars a-z 1 or more times
    # . - separates domain and zone, use \. for '.' character
    # zone - chars a-z 2, 3, 4

    print('------ Email validation ----------')

    emailPattern1 = r"^[a-z]+@[a-z]+\.[a-z]{2,4}$" # $ ends with
    print(re.match(emailPattern1, 'asdfasdf'))
    print(re.match(emailPattern1, 'as67676@kbtu.kz'))
    print(re.match(emailPattern1, 'asdfasdf@mail'))
    print(re.match(emailPattern1, 'asdf@mail,ru'))
    print(re.match(emailPattern1, 'asdf@mail.ru'))
    print(re.match(emailPattern1, 'asdf@mail.ru8'))
    print(re.match(emailPattern1, 'asdf@mail.rupoi'))
    print(re.match(emailPattern1, ' fa5650a8dsfasdf@mail.ru'))


    email_pattern2 = r"([a-z]+)@([a-z]+)\.([a-z]{2,4})$" # $ ends with
    valid_email = 'daulet@kbtu.kz'
    match = re.match(email_pattern2, valid_email)
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    # print(match.group('zone')) # will not work

    email_pattern3 = r"(?P<username>[a-z]+)@(?P<domain>[a-z]+)\.(?P<zone>[a-z]{2,4})$" # $ ends with
    valid_email = 'daulet@kbtu.kz'
    match = re.match(email_pattern3, valid_email)
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print("Named groups")
    print(match.group('username'))
    print(match.group('domain'))
    print(match.group('zone'))

if __name__== '__main__':
    # w3_schools_examples()
    softhints()
