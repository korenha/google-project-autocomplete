from Data import data
from terminal import terminal


def load_data():
    list_ = [
        ("We are waiting for it to work...", "dir3/file2", 0),
        ("To be or not to be, that's the question", "dir1/dir2/file1", 1),
        ("hello world1", "dir1/dir2/file1", 2),
        ("hello world2", "dir1/dir2/file1", 3),
        ("hello world3", "dir1/dir2/file1", 4),
        ("hello world4", "dir1/dir2/file1", 5)
    ]

    list_ = sorted(list_, key=lambda x: x[0].lower())
    for item in list_:
        data.insert(item[1], item[0],item[2])


def manager():
    load_data()
    print("begin")
    terminal()
