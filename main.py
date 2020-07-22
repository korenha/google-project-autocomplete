from manager import manager


if __name__ == '__main__':
    manager()

# from utils import clear_string
#
# class TreeNode:
#     def __init__(self):
#         self.dict_letter = dict()
#
#
# def insert(sentence, root):
#     for char in sentence:
#         try:
#             root = root.dict_letter[char]
#         except KeyError:
#             root.dict_letter[char] = TreeNode()
#             root = root.dict_letter[char]
#
#
# root = TreeNode()
#
#
# def fill_sentences(root):
#     with open("technology_texts/RFC/Tasks.txt", encoding="utf8") as file:
#         file_sentences = [line.rstrip() for line in file]
#         for j,sentence in enumerate(file_sentences):
#             for i in range(len(sentence)):
#                 print(j,"-",i)
#                 insert(clear_string(sentence[i:]), root)
#
#
# fill_sentences(root)
# print("finish")