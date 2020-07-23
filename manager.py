from Data import data
from terminal import terminal

def load_data():
    list_ = [
        ("We are waiting for it to work...", "dir3/file2"),
        ("To be or not to be, that's the question", "dir1/dir2/file1"),
        ("hello world1", "dir1/dir2/file1"),
        ("hello world2", "dir1/dir2/file1"),
        ("hello world3", "dir1/dir2/file1"),
        ("hello world4", "dir1/dir2/file1")
    ]

    list_ = sorted(list_, key=lambda x: x[0].lower())
    for item in list_:
        data.insert(item[1], item[0])


def manager():
    load_data()
    print("begin")
    terminal()
