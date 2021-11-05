"""
reverse the words
"""


def reverse_words(sentence: str) -> str:
    words = [w for w in sentence.split(" ") if w != '']
    word_arr = []
    for i in range(len(words), 0, -1):
        word_arr.append(words[i - 1])
    return " ".join(word_arr)


print(reverse_words("I    love  you     Dani!"))
