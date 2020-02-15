import os
import csv
import json

class Actress:
    def __init__(self, year, age, name, movie):
        self.year = year
        self.age = age
        self.name = name
        self.movie = movie

    # this method is called when we print
    def __str__(self):
        return "I'm {0}, aged {1} and I starred in movie '{2}' in {3}".format(self.name, self.age, self.movie, self.year)


def actresses_to_csv(actresses: list):
    filename = os.getcwd() + '/created_actresses.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(actresses)


def csv_to_actress():
    filename = os.getcwd() + '/actresses.csv'

    # [Actress('1974', '37', 'Glenda Jackson', 'A Touch of Class'), Actress(), ..., etc.]
    actresses = []

    with open(filename, newline='') as file:
        reader = csv.reader(file)    # reader is iterable

        headers = next(reader)

        for row in reader:
            actress = Actress(row[1], row[2], row[3], row[4])
            actresses.append(actress)

    return actresses
            

def csv_to_data():
    filename = os.getcwd() + '/actresses.csv'

    # {'47' -> ['1974', '37', 'Glenda Jackson', 'A Touch of Class']}
    actresses_dict = {}

    # {'age' -> [22, 37, 28, ..., etc.]}
    data = {}

    with open(filename, newline='') as file:
        reader = csv.reader(file)    # reader is iterable

        headers = next(reader)
        print(headers)

        for header in headers:
            data[header] = []

        # print(data)

        for row in reader:
            # row = ['72', '1999', '26', 'Gwyneth Paltrow', 'Shakespeare in Love']
            # headers [header1, header2, ]
            for header, value in zip(headers, row):
                data[header].append(value)
                # print(header + ' ' + value)
        print(data)


def actresses_to_json(actresses: list):
    filename = os.getcwd() + '/actresses.json'

    # dictionary OK
    example = {'name': 'Brie Larson'} 
    # Helen Hayes,The Sin of Madelon Claudet

    # list OK
    example2 = [{'name': 'Brie Larson'}, {'name':'Helen Hayes'}]

    actresses_list = []

    for act in actresses:
        actresses_list.append(act.__dict__)
        print(act.__dict__)

    print()

    print(actresses_list)
    # actresses is a list of dicts

    # operate with LISTS and DICTIONARIES
    with open(filename, 'w') as file:
        json.dump(actresses_list, file, sort_keys=True, indent=4)

def json_to_actresses():
    filename = os.getcwd() + '/actresses.json'

    actresses = []
    with open(filename, 'r') as file:
        data = json.load(file)

        
        
        for dictionary in data:
            actress = Actress(dictionary['year'], dictionary['age'], dictionary['name'], dictionary['movie'])
            actresses.append(actress)

    return actresses
    
if __name__ == '__main__':
    # csv_to_data()
    actresses = csv_to_actress()   # actresses: list
    actresses_list = []
    # for act in actresses:
    #     print(act)
    #     actresses_list.append([act.year, act.age, act.name, act.movie])

    # print(actresses_list)

    # write to csv file
    # actresses_to_csv(actresses_list)

    actresses_to_json(actresses)


    # actresses_json = json_to_actresses()
    # for act in actresses_json:
    #     print(act)


    # Summary
    # 1) read from CSV -> actresses
    # 2) write actresses to CSV -> created_actresses.csv
    # 3) write actresses to JSON -> actresses.json
    # 4) read from actresses.json -> actresses


    # Binary example
    # 0x204395234AB0529845BF4098527345D94752345
    # - more performant
    # - takes less space

    '''
    XML example:
    <employee>
	    <name>Ivan</name>
	    <surname>Ivanov</surname>
    </employee>

    Same data but in JSON
    {
        "employee":{
            "name":"Ivan",
            "surname":"Ivanov"
        }
    }

    Binary data example:
    0x204395234AB0529845BF4098527345D94752345
    '''