def get_unique_words(str_words: str):
    words_list_without_empty_string = []
    for word in str_words.split(" "):
        if word:
            words_list_without_empty_string.append(word)

    return set(words_list_without_empty_string)


if __name__ == "__main__":
    print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
