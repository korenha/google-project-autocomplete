import re
from collections import defaultdict
from utils import clear_string

class StringDescribtor:
    def __init__(self, id_sentence, offset):
        self.__id_sentence: int = id_sentence
        self.__offset = offset

    def get_id_sen(self):
        return self.__id_sentence

    def get_offset(self):
        return self.__offset

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
        if new_item.get_id_sen() in l or len(list_) == self.__max_size_of_list:
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
            sentance1 = clear_string(sentence)
            id = self.__sentences_data.insert((sentence, url))
            for j in range(len(sentance1)):
                for k in range(j):
                    self.__strings_data.insert(sentance1[k:j], id, k)

    def find(self, string: str):
        return self.__strings_data.find(string)

    def get_sentence(self, _id):
        return self.__sentences_data.get_sentence(_id)

    def get_url(self, _id):
        return self.__sentences_data.get_url(_id)


















