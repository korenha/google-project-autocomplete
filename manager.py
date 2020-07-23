from Data import data
from terminal import terminal


def fill_sentences():
    sentences = data.get_sentences()
    with open("technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt", encoding="utf8") as file:
        file_sentences = [line.rstrip() for line in file]
        for i, sentence in enumerate(file_sentences):
            string = sentence
            print(sentence)
            sentences.insert((string, "technology_texts/RFC/Tasks.txt", i))

    sentences.sort()


def fill_substrings_dict():
    counter = 0
    sentences = data.get_sentences()
    print(len(sentences.get_sentences()))
    for i, sentence in enumerate(sentences.get_sentences()):
        for j in range(len(sentence[0])):
            for k in range(j):
                data.insert(sentence[0][k:j], i)
                print(counter)
                counter += 1


def load_data():
    fill_sentences()
    fill_substrings_dict()

    # list_ = [
    #     ("We are waiting for it to work...", "dir3/file2", 0),
    #     ("To be or not to be, that's the question", "dir1/dir2/file1", 1),
    #     ("hello world1", "dir1/dir2/file1", 2),
    #     ("hello world2", "dir1/dir2/file1", 3),
    #     ("hello world3", "dir1/dir2/file1", 4),
    #     ("hello world4", "dir1/dir2/file1", 5)
    # ]


def manager():
    load_data()
    print("begin")
    terminal()
