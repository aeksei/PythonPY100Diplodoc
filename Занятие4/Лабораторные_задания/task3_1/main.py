def get_count_char(str_: str) -> dict:

    str_ = str_.lower()
    char_dict = {}  # словарь для подсчета количества символов

    for char in str_:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def frequency_chars(char_dict: dict) -> dict:
    total_count = sum(char_dict.values())

    return {char: round(value / total_count, 3) for char, value in char_dict.items()}


if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    chars_counter = get_count_char(main_str)
    print(frequency_chars(chars_counter))
