from Data import data
from terminal import terminal
from utils import clear_string
from os import listdir
import glob, os


def fill_sentences(file):
    sentences = data.get_sentences()
    with open(file, encoding="utf8") as file:
        file_sentences = [line.rstrip() for line in file]
        for i, sentence in enumerate(file_sentences):
            sentences.insert((sentence, "technology_texts/RFC/Tasks.txt", i))

    sentences.sort()


def fill_substrings_dict():
    count = 0
    sentences = data.get_sentences()
    print(len(sentences.get_sentences()))
    for i, sentence in enumerate(sentences.get_sentences()):
        for j in range(len(sentence[0])):
            for k in range(11):
                print(count," - ", i )
                count += 1
                data.insert(clear_string(sentence[0][j:j+k]), i)

    # data.load_to_file("until_20.json")
    # data.load_from_file("until_20.json")


def load_data():
    count = 0
    for root, dirs, files in os.walk("./technology_texts/python-3.8.4-docs-text"):
        for file in files:
            if file.endswith(".txt"):
                count += 1
                print("file ",count )
                fill_sentences(os.path.join(root, file))
    fill_substrings_dict()


def manager():
    load_data()
    print("let start:")
    terminal()
