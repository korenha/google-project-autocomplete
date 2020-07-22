from manager import data
from utils import clear_string
from autoComplate import AutoCompleteData
def get_input():
    string = ""
    new_input = input(string)
    while new_input == "":
        new_input = input(string)

    while new_input == "" or new_input[len(new_input)-1] != '#':
        string += clear_string(new_input)
        yield string
        new_input = input(string)

def get_best_k_completions(prefix: str):#->
    list_ = list(data.find(prefix))
    auto_complate = []
    for item in list_:
        auto = AutoCompleteData()
        auto.source_text = (data.get_sentence(item.get_id_sen()))
        auto_complate.append(auto)
    return auto_complate[:5]


def print_best_k_completions(list_: AutoCompleteData):
    for item in list_:
        print(item.source_text)#צריך להדפיס URL

def terminal():
    while 1:
        for string in get_input():
            the_best = get_best_k_completions(string)
            print_best_k_completions(the_best)




