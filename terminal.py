from manager import data
from utils import clear_string
from autoComplate import get_best_k_completions,print_best_k_completions
def get_input():
    string = ""
    new_input = input(string)
    while new_input == "":
        new_input = input(string)

    while new_input == "" or new_input[len(new_input)-1] != '#':
        string += new_input
        yield clear_string(string)
        new_input = input(string)

def terminal():
    while 1:
        print(">>>", end=" ")
        for string in get_input():
            the_best = get_best_k_completions(string)
            print_best_k_completions(the_best)
            print(">>>", end=" ")




