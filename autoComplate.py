from Data import data


class AutoCompleteData:

    def __init__(self, complated_sentences, source_text, offset, score):
        self.completed_sentence: str = complated_sentences
        self.source_text: str = source_text
        self.offset: int = offset
        self.score: int = score

    def __eq__(self, other):
        if self.completed_sentence != other.completed_sentence:
            return False
        if self.source_text != other.source_text:
            return False
        if self.offset != other.offset:
            return False
        return True


alphabet = "abcdefghijklmnopqrstuvwxuz "


# def get_score_after_changes(index):
#     if index <= 3:
#         return 12 - 2 * (index + 1)
#     return 2
#
#
# def get_score_after_add_or_delete(index):
#     if index <= 3:
#         return 6 - index - 1
#     return 1


def push_list_to_list(auto_complete_list, new_list):
    for item in new_list:
        if item not in auto_complete_list:
            auto_complete_list.append(item)

        if len(auto_complete_list) == 5:
            return auto_complete_list

    return auto_complete_list


def get_with_change(substring, auto_complete_list, index, score):
    if index != 0 and len(data.find(substring[:index])) == 0:
        return auto_complete_list

    if index != len(substring) - 1 and len(data.find(substring[index + 1:])) == 0:
        return auto_complete_list

    for char in alphabet:
        substring = substring[:index] + str(char) + substring[index + 1:]
        completed_sentences = get_perfect_completions(substring)
        for item in completed_sentences:
            item.score -= score
        auto_complete_list = push_list_to_list(auto_complete_list, completed_sentences)
        if len(auto_complete_list) == 5:
            return auto_complete_list

    return auto_complete_list


def get_with_add(substring, auto_complete_list, index, score):
    if index != 0 and len(data.find(substring[:index])) == 0:
        return auto_complete_list

    if index == len(substring) - 1:
        return auto_complete_list

    for char in alphabet:
        substring = substring[:index + 1] + str(char) + substring[index + 1:]
        completed_sentences = get_perfect_completions(substring)
        for item in completed_sentences:
            item.score -= score
        auto_complete_list = push_list_to_list(auto_complete_list, completed_sentences)
        if len(auto_complete_list) == 5:
            return auto_complete_list
    return auto_complete_list


def get_with_delete(substring, auto_complete_list, index, score):
    if index != 0 and len(data.find(substring[:index])) == 0:
        return auto_complete_list

    if index != len(substring) - 1 and len(data.find(substring[index + 1:])) == 0:
        return auto_complete_list

    substring = substring[:index] + substring[index + 1:]
    completed_sentences = get_perfect_completions(substring)
    for item in completed_sentences:
        item.score -= score
    auto_complete_list = push_list_to_list(auto_complete_list, completed_sentences)
    if len(auto_complete_list) == 5:
        return auto_complete_list
    return auto_complete_list


def get_perfect_completions(substring):
    completed_sentences_id = list(data.find(substring))
    auto_complete = []
    for id in completed_sentences_id:
        auto = AutoCompleteData(data.get_sentence(id),
                                data.get_url(id),
                                data.get_offset(id), len(substring) * 2)
        auto_complete.append(auto)
    return auto_complete


def get_best_k_completions(prefix):  # ->
    auto_complete_sentences = get_perfect_completions(prefix)
    length = len(prefix)
    for index in range(4, length):
        if len(auto_complete_sentences) == 5:
            return auto_complete_sentences
        auto_complete_sentences = get_with_change(prefix, auto_complete_sentences, index, 1)

    for index in range(4, length):
        if len(auto_complete_sentences) == 5:
            return auto_complete_sentences
        auto_complete_sentences = get_with_delete(prefix, auto_complete_sentences, index, 2)

    for index in range(4, length + 1):
        if len(auto_complete_sentences) == 5:
            return auto_complete_sentences
        auto_complete_sentences = get_with_add(prefix, auto_complete_sentences, index, 2)

    functions_list = [
        [2, (3,), (get_with_change,)],
        [3, (2, 2), (get_with_delete, get_with_add)],
        [4, (3, 1, 1), (get_with_change, get_with_delete, get_with_add)],
        [5, (0, 0), (get_with_delete, get_with_add)],
        [6, (2,), (get_with_change,)],
        [8, (1,), (get_with_change,)],
        [10, (0,), (get_with_change,)]
    ]

    for list_ in functions_list:
        for index, func in zip(list_[1], list_[2]):
            if len(auto_complete_sentences) == 5:
                return auto_complete_sentences
            if index < length:
                auto_complete_sentences = func(prefix, auto_complete_sentences, index, list_[0])

    return auto_complete_sentences


def print_best_k_completions(list_: AutoCompleteData):
    for i, item in enumerate(list_):
        print(f"{i + 1}) ", item.completed_sentence, f"( {item.source_text} )", item.offset)  # צריך להדפיס URL
