from manager import data

class AutoCompleteData:

    def __init__(self,complated_sentences,source_text,offset,score):
        self.completed_sentence: str = complated_sentences
        self.source_text: str = source_text
        self.offset: int = offset
        self.score: int = score

def get_score_after_changes(index):
    if index <= 4:
        return 6-index
    return 1

def get_with_change(substring,index,amount=5):
    compleated_sentences = list()
    if index != 0 and len(data.find(substring[:index])) == 0:
        return compleated_sentences,amount

    if index != len(substring) and len(data.find(substring[index+1:])) == 0:
        return compleated_sentences,amount

    for char in "abcdefghijklmnopqrstuvwxuz ":
        substring[index] = char
        compleated_sentences += get_perfect_completions(substring)
        for item in compleated_sentences:
            item.score -= get_score_after_changes(index)
        amount -= len(compleated_sentences)
        if(amount <= 0):
            break
    return compleated_sentences,amount

def get_with_add(substring,index,amount=5):
    compleated_sentences = list()
    if index != 0 and len(data.find(substring[:index])) == 0:
        return compleated_sentences,amount

    if index != len(substring) and len(data.find(substring[index:])) == 0:
        return compleated_sentences,amount

    for char in "abcdefghijklmnopqrstuvwxuz ":
        substring = substring[:index] + char + substring[index:]
        compleated_sentences += get_perfect_completions(substring)
        for item in compleated_sentences:
            item.score -= get_score_after_changes(index)
        amount -= len(compleated_sentences)
        if(amount <= 0):
            break
    return compleated_sentences,amount

def get_perfect_completions(substring):
    complated_sentences = list(data.find(substring))
    auto_complate = []
    for item in complated_sentences:
        auto = AutoCompleteData(data.get_sentence(item.get_id_sen()),
                                data.get_url(item.get_id_sen()),
                                item.get_offset(), len(substring) * 2)
        auto_complate.append(auto)
    return auto_complate

def get_best_k_completions(prefix: str):#->
    return get_perfect_completions(prefix)



def print_best_k_completions(list_: AutoCompleteData):
    for i,item in enumerate(list_):
        print(f"{i+1}) ", item.completed_sentence,f"( {item.source_text} )")#צריך להדפיס URL