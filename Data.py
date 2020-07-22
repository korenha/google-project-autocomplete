import re
from collections import defaultdict
class StringDescribtor:
    def __init__(self, id_sentence, offset):
        self.__id_sentence: int = id_sentence
        self.__offset = offset

    def get_id_sen(self):
        return self.__id_sentence

    def get_string(self):
        return data.get_sentence(self.__id_sentence)

    def get_offset(self):
        return self.__offset


# class sentenceDescribtor:
#     def __init__(self, url, string):
#         self.__string = string
#         self.__url = url
#
#     def get_url(self):
#         return self.__url
#
#     def get_string(self):
#         return self.__string


class StringsData:
    def __init__(self):
        self.__dict = defaultdict(list)
        self.__max_size_of_list = 5

    def find(self, string):
        list_ =  self.__dict.get(string)
        if(not list_):
            return list()
        return list_[:]

    def __push_item(self, new_item, list_):
        l = [item.get_id_sen() for item in list_]
        id = new_item.get_id_sen()
        if id in l or len(list_) == self.__max_size_of_list:
            return list_
        list_.append(new_item)




    def insert(self, string, id, offset):
        list_ = self.find(string)
        if len(list_) == 0:
            self.__dict[clear_string(string)].append(StringDescribtor(id, offset))
        else:
            self.__push_item(StringDescribtor(id, offset), self.__dict[clear_string(string)])

class SentencesData:
    def __init__(self):
        self.__list = []

    def insert(self, value):
        self.__list.append(value)
        return len(self.__list) - 1

    def get_sentence(self, _id):
        return self.__list[_id][0]

    def get_url(self, _id):
        return self.__list[_id][1]


class Data:
    def __init__(self):
        self.__strings_data = StringsData()
        self.__sentences_data = SentencesData()

    def insert(self, url, sentence):
            sentence = clear_string(sentence)
            id = self.__sentences_data.insert((sentence, url))
            for j in range(len(sentence)):
                for k in range(j):
                    self.__strings_data.insert(sentence[k:j], id, k)

    def find(self, string: str):
        return self.__strings_data.find(string)

    def get_sentence(self, _id):
        return self.__sentences_data.get_sentence(_id)


class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int


def clear_string(string):
    string = string.lower().replace("  ", " ")

    return re.sub(r'[^a-z0-9 ]', '', string)


def get_best_k_completions(prefix: str):#->
    list_ = list(data.find(prefix))
    auto_complate = []
    for item in list_:
        auto = AutoCompleteData()
        auto.source_text = (data.get_sentence(item.get_id_sen()))
        auto_complate.append(auto)
    return auto_complate[:5]


def get_input():
    string = ""
    new_input = input(string)
    while new_input == "":
        new_input = input(string)

    while new_input == "" or new_input[len(new_input)-1] != '#':
        string += clear_string(new_input)
        yield string
        new_input = input(string)

def print_best_k_completions(list_: AutoCompleteData):
    for item in list_:
        print(item.source_text)#צריך להדפיס URL


def terminal():
    while 1:
        for string in get_input():
            the_best = get_best_k_completions(string)
            print_best_k_completions(the_best)


data = Data()


def load_data():
    list_ = [
        ("We are waiting for it to work...", "dir3/file2"),
        ("To be or not to be, that's the question", "dir1/dir2/file1"),
        ("hello world1", "dir1/dir2/file1"),
        ("hello world2", "dir1/dir2/file1"),
        ("hello world3", "dir1/dir2/file1"),
        ("hello world4", "dir1/dir2/file1")
            ]

    list_ = sorted(list_,key=lambda x: x[0].lower())
    for item in list_:
        data.insert(item[1], item[0])


def manager():
    load_data()
    terminal()

manager()