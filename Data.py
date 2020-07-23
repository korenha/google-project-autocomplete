from collections import defaultdict
from utils import clear_string
import json
import datetime
import shelve

class SubstringData:
    def __init__(self):
        self.__dict = shelve.open("substring_dict", writeback=True)
        self.__max_size_of_list = 5

    def find(self, string):
        list_ =  self.__dict.get(string)
        if not list_:
            return list()
        return list_[:]

    def __push_item(self, id, list_):
        if len(list_) == self.__max_size_of_list or id in list_:
            return list_
        list_.append(id)
        return list_

    def insert(self, string, id):
        list_ = self.find(string)
        self.__dict[clear_string(string)] = self.__push_item(id, list_)

    def load_to_file(self, file_name):
        with open(file_name, "w") as the_file:
            json.dump([self.__dict], the_file)

    def load_from_file(self, file_name):
        with open(file_name, "r") as the_file:
            self.__dict = json.load(the_file)[0]


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

    def get_offset(self,_id):
        return self.__list[_id][2]

    def sort(self):
        self.__list = sorted(self.__list, key=lambda x: clear_string(x[0]))

    def get_sentences(self):
        return self.__list


class Data:
    def __init__(self):
        self.__substrings_data = SubstringData()
        self.__sentences_data = SentencesData()

    def insert(self, sentence, id):
        self.__substrings_data.insert(sentence, id)

    def find(self, string: str):
        return self.__substrings_data.find(string)

    def get_sentence(self, _id):
        return self.__sentences_data.get_sentence(_id)

    def get_url(self, _id):
        return self.__sentences_data.get_url(_id)

    def get_offset(self, _id):
        return self.__sentences_data.get_offset(_id)

    def get_sentences(self):
        return self.__sentences_data

    def load_to_file(self, file_name):
        time = datetime.datetime.now()
        self.__substrings_data.load_to_file(file_name)
        print(datetime.datetime.now()-time)

    def load_from_file(self, file_name):
        time = datetime.datetime.now()
        self.__substrings_data.load_from_file(file_name)
        print(datetime.datetime.now()-time)


data = Data()
