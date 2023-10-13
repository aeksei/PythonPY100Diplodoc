if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]

    mean = sum(list_) / len(list_)  # среднее арифметическое
    new_list = [src_num - mean for src_num in list_]

    print(new_list)
