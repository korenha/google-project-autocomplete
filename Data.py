from collections import defaultdict
from utils import clear_string

class StringsData:
    def __init__(self):
        self.__dict = defaultdict(list)
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
        self.__list = sorted(self.__list, key=lambda x: x[0].lower())

    def get_sentences(self):
        return self.__list


class Data:
    def __init__(self):
        self.__strings_data = StringsData()
        self.__sentences_data = SentencesData()

    def insert(self, sentence, id):
        self.__strings_data.insert(sentence, id)

    def find(self, string: str):
        return self.__strings_data.find(string)

    def get_sentence(self, _id):
        return self.__sentences_data.get_sentence(_id)

    def get_url(self, _id):
        return self.__sentences_data.get_url(_id)

    def get_offset(self, _id):
        return self.__sentences_data.get_offset(_id)

    def get_sentences(self):
        return self.__sentences_data

data = Data()
